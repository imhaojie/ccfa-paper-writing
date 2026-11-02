#!/usr/bin/env python3

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from audit_prose import audit


class AuditProseTests(unittest.TestCase):
    def audit_tex_findings(self, body: str):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "paper.tex"
            path.write_text(body, encoding="utf-8")
            return audit([path])

    def audit_tex(self, body: str) -> set[str]:
        return {finding.code for finding in self.audit_tex_findings(body)}

    def test_detects_defensive_disclaimer_and_hedge_stack(self) -> None:
        codes = self.audit_tex(
            r"""
\documentclass{article}
\begin{document}
This paper is not intended to provide a general theory. The evidence may
potentially suggest an effect.
\end{document}
"""
        )
        self.assertIn("DEFENSIVE_DISCLAIMER", codes)
        self.assertIn("HEDGE_STACK", codes)

    def test_does_not_treat_may_appear_as_a_hedge_stack(self) -> None:
        codes = self.audit_tex(
            r"""
\documentclass{article}
\begin{document}
Genuine sources such as loudspeakers may appear stationary.
\end{document}
"""
        )
        self.assertNotIn("HEDGE_STACK", codes)

    def test_ignores_latex_preamble(self) -> None:
        codes = self.audit_tex(
            r"""
\documentclass{article}
\pdfinfo{/TemplateVersion (2027.1) /Tracking (disabled)}
\begin{document}
The method selects motion using audio.
\end{document}
"""
        )
        self.assertNotIn("PARENTHESIS_DENSITY", codes)

    def test_detects_abstract_citation(self) -> None:
        codes = self.audit_tex(
            r"""
\documentclass{article}
\begin{document}
\begin{abstract}
Prior work studies this problem \citep{example}.
\end{abstract}
\end{document}
"""
        )
        self.assertIn("CITATION_IN_ABSTRACT", codes)

    def test_detects_reporting_lead_and_prose_versus(self) -> None:
        codes = self.audit_tex(
            r"""
\documentclass{article}
\begin{document}
\section{Experiments}
Table 2 shows our method vs. the baseline.
\end{document}
"""
        )
        self.assertIn("REPORTING_LEAD", codes)
        self.assertIn("PROSE_VERSUS", codes)

    def test_detects_authorial_first_person_and_active_voice(self) -> None:
        findings = self.audit_tex_findings(
            r"""
\documentclass{article}
\begin{document}
We evaluate our method on AVSBench. The proposed model selects
audio-consistent motion. The experiments show a stable gain.
\end{document}
"""
        )
        codes = {finding.code for finding in findings}
        self.assertIn("AUTHORIAL_FIRST_PERSON", codes)
        self.assertIn("ACTIVE_TRANSITIVE_VOICE", codes)
        self.assertEqual(
            {finding.severity for finding in findings if finding.code == "AUTHORIAL_FIRST_PERSON"},
            {"low"},
        )

    def test_detects_acronym_subject_active_voice(self) -> None:
        codes = self.audit_tex(
            r"""
\documentclass{article}
\begin{document}
Spectral--Kinematic Alignment (SKA) is introduced for verification.
SKA selects audio-consistent motion.
\end{document}
"""
        )
        self.assertIn("ACTIVE_TRANSITIVE_VOICE", codes)

    def test_accepts_passive_house_style(self) -> None:
        codes = self.audit_tex(
            r"""
\documentclass{article}
\begin{document}
The model is evaluated on AVSBench. Audio-consistent motion is selected
by the proposed model. A stable gain is observed across the experiments.
\end{document}
"""
        )
        self.assertNotIn("AUTHORIAL_FIRST_PERSON", codes)
        self.assertNotIn("ACTIVE_TRANSITIVE_VOICE", codes)

    def test_does_not_treat_us_acronym_as_first_person(self) -> None:
        codes = self.audit_tex(
            r"""
\documentclass{article}
\begin{document}
Results for the US subset are reported separately.
\end{document}
"""
        )
        self.assertNotIn("AUTHORIAL_FIRST_PERSON", codes)

    def test_detects_acronym_before_definition(self) -> None:
        codes = self.audit_tex(
            r"""
\documentclass{article}
\begin{document}
SKA is used for motion selection. Spectral--Kinematic Alignment (SKA)
is defined later.
\end{document}
"""
        )
        self.assertIn("ACRONYM_BEFORE_DEFINITION", codes)

    def test_accepts_definition_before_acronym_use(self) -> None:
        codes = self.audit_tex(
            r"""
\documentclass{article}
\begin{document}
Spectral--Kinematic Alignment (SKA) is introduced for motion selection.
Audio-consistent motion is selected by SKA.
\end{document}
"""
        )
        self.assertNotIn("ACRONYM_BEFORE_DEFINITION", codes)

    def test_abstract_definition_remains_valid_in_body(self) -> None:
        codes = self.audit_tex(
            r"""
\documentclass{article}
\begin{document}
\begin{abstract}
Audio-Visual Segmentation (AVS) is studied.
\end{abstract}
\section{Introduction}
AVS requires pixel-level localization.
\end{document}
"""
        )
        self.assertNotIn("ACRONYM_BEFORE_DEFINITION", codes)
        self.assertNotIn("ACRONYM_REDEFINITION", codes)

    def test_detects_redefinition_after_abstract(self) -> None:
        codes = self.audit_tex(
            r"""
\documentclass{article}
\begin{document}
\begin{abstract}
Audio-Visual Segmentation (AVS) is studied.
\end{abstract}
\section{Introduction}
Audio-Visual Segmentation (AVS) requires pixel-level localization.
\end{document}
"""
        )
        self.assertIn("ACRONYM_REDEFINITION", codes)

    def test_accepts_uppercase_component_in_mixed_identifier_definition(self) -> None:
        codes = self.audit_tex(
            r"""
\documentclass{article}
\begin{document}
Semantic Segment Anything Model (Semantic-SAM) priors are cached.
\end{document}
"""
        )
        self.assertNotIn("ACRONYM_BEFORE_DEFINITION", codes)


if __name__ == "__main__":
    unittest.main()
