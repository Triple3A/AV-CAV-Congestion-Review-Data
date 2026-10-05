# AV/CAV Congestion Review Data

This repository contains the study-level coding and supporting synthesis files for:

**Autonomous Vehicles as Active Congestion-Control Agents: A Mechanism-Based Review of Freeway Bottlenecks in Mixed Traffic**

**Authors:** Amirali Ataee Naeini, Ashkan Teymouri, and Michael H. Zhang

## Overview

The review examines how autonomous and connected automated vehicles may act as traffic-control agents for congestion mitigation. Its main focus is freeway bottlenecks and mixed traffic.

The literature review followed a semi-systematic process. AI-assisted literature discovery was combined with manual bibliographic verification, eligibility screening, coding and narrative synthesis. Undermind AI and Perplexity were used only to identify candidate publications.

The manuscript-linked corpus contains **99 retained publications**, selected in three steps:

- **266 candidate records** were identified.
- **228 verified records** remained after bibliographic verification and deduplication.
- **99 publications** were retained after eligibility assessment.

## Files

The file names match the supplementary tables cited in the manuscript's Data Availability Statement.

| File | Content |
|---|---|
| `data/Table_S1_Verified_Screening_Matrix.csv` | The 228 verified records and their record-level screening disposition. |
| `data/Table_S2_Retained_Corpus.csv` | The final retained corpus of 99 publications, with review roles (62 [D], 27 [M], 10 [C]), the nine taxonomy dimensions, and descriptive fields (key finding, main limitation, comparator/reference condition). |
| `data/Table_S3_Screening_Flow.csv` | The record counts shown in Figure 1. |
| `data/Table_S4_Application_Mechanism_Evidence_Map.csv` | One row per cell of the 8 × 9 application-family × congestion-mechanism map (Figure 2). Each row gives the final marker, the direct and indirect supporting studies, finding-pattern counts, evidence settings, representative metrics and a cell rationale. |
| `data/Table_S5_Study_Application_Mechanism_Audit.csv` | The study-level application–mechanism audit of 77 retained studies. It has one row per study × family × mechanism relationship. Each row gives the directness (DIRECT, INDIRECT or NONE), a finding pattern for direct relationships, the supporting metric, the evidence setting, a full-text rationale and the source location. |
| `data/Table_S6_Independent_Coding_Agreement.csv` | Exact-set agreement between the lead author's coding and a second author's independent coding of a 19-study subset, by dimension, with mean Jaccard similarity as a secondary set-overlap diagnostic and an adjudication summary. |
| `data/Table_S6_legacy_label_review.csv` | The 12 comparisons in which the frozen lead coding carried a label outside the final codebook, with how each was treated. None was excluded. |
| `data/evidence_role_reconciliation.csv` | The re-check of the 11 audit reassessments from [D] to [M]: 10 were confirmed and one was restored to [D]. |
| `data/independent_coding_check_adjudication.csv` | One row per disagreement (105 rows). Each row gives both coders' codes, the adjudicated code, the rationale and which records changed. |
| `data/Table_S7_Taxonomy_Figure2_Crosswalk.csv` | Crosswalk from the study-level congestion-mechanism and operational-application codes (Appendix B and Table S2) to the nine Figure 2 mechanism columns and eight application families, with each aggregation rule. |
| `data/qa_final_coding_changes.csv` | Every coding change made in the final pre-submission check and in the October 2026 coverage update, with the old and new value and the basis (execution rule, strict capacity-drop rule, evidence-setting check, reference metadata, added studies and full-text audit). |
| `figures/Figure2/` | Figure 2 (SVG, PDF and 600 dpi PNG) and the script that draws it from Table S4. |
| `figures/Figure3/` | Figure 3, the evaluation framework (SVG, PDF and 600 dpi PNG), and the script that draws it. Category lists in the figure are illustrative; `data/Table_S7_Taxonomy_Figure2_Crosswalk.csv` gives the full mapping. |
| `figures/FigureS1/` | Supplementary Figure S1 with its source script and derived counts. See the README in that folder. |
| `scripts/build_evidence_map.py` | Aggregates Table S5 into Table S4; writes `scripts/evidence_map_validation.json`. |
| `docs/evidence_map_method.md` | The marker rules for Table S4 and Figure 2. |
| `CODEBOOK.md` | Coding definitions and conventions. |

## Coding structure

The review separates several concepts that are often grouped together in AV/CAV studies:

- **Congestion mechanism:** the traffic-flow process or system consequence being targeted.
- **Decision lever:** the executable AV/CAV action, such as acceleration, desired speed, headway, lane choice, merge/yield, route choice or access decision.
- **Design method:** the method used to compute or learn the control action, such as rule-based control, optimal control, MPC, game-theoretic control or RL/MARL.
- **Coordination/implementation mode:** how information and control authority are organized, such as onboard, cooperative V2V, infrastructure-assisted, centralized or distributed control.
- **Operational application:** the traffic-management function being implemented.
- **Operating context:** facility context and spatial/system scale.
- **Mixed-traffic and deployment conditions:** assumptions about penetration, controllability, human behavior, communication and related factors.
- **Evidence setting:** analytical/theoretical, simulation, test-track, field experiment, observational/open-road data or network/demand model.
- **Congestion metric:** the outcome used to evaluate the congestion claim.

`key_finding`, `main_limitation` and `comparator_reference_condition` are descriptive extraction fields, not taxonomy dimensions.

## Application–mechanism map (Table S4, Figure 2)

The map is aggregated mechanically from the study-level audit in Table S5:

- **●** repeated, consistently positive direct support: at least two direct supporting studies, all coded consistently positive;
- **○** one direct supporting study, or at least one direct finding that is mixed, negative or strongly conditional;
- **□** indirect support only;
- **—** no substantive relationship identified in the coded set.

The final map contains 106 direct and 76 indirect study–cell links. It has 4 ●, 34 ○, 7 □ and 27 — cells.

Rebuild Table S4 and Figure 2 with:

```
python scripts/build_evidence_map.py data/Table_S5_Study_Application_Mechanism_Audit.csv data/Table_S4_Application_Mechanism_Evidence_Map.csv
python figures/Figure2/build_figure_2.py data/Table_S4_Application_Mechanism_Evidence_Map.csv figures/Figure2
```

Markers describe the pattern of support, not study quality or deployment readiness. See [`docs/evidence_map_method.md`](docs/evidence_map_method.md).

## Independent coding check (Table S6)

A second author independently coded a stratified subset of 19 retained studies. Agreement is percentage agreement, computed separately for each dimension:

- **Single-label fields** agree when the two values are identical.
- **Multi-label fields** agree only when the complete normalized label sets are identical (exact-set agreement). Nested, partially overlapping or disjoint sets count as disagreements.

Normalization covers formatting only (whitespace, capitalization, delimiters, duplicates, order) and old wording that is equivalent to a final-codebook label. Agreement ranged from 10.5% (congestion mechanism) to 100% (evidence role).

Mean Jaccard similarity (|A ∩ B| / |A ∪ B|) is reported separately as a secondary set-overlap diagnostic. It is not combined with exact-set agreement.

In 12 comparisons the frozen lead coding carried a label outside the final codebook. One ("Queueing/delay") is old wording of "Queue formation / discharge" and was normalized before comparison. The other 11 are substantive or unresolved labels; they were kept and counted. No comparison was excluded. See `data/Table_S6_legacy_label_review.csv`.

Finding pattern, which separates filled from open Figure 2 markers, agreed in 6 of 10 cells coded direct by both authors (60.0%).

All 105 disagreements were resolved through discussion and adjudication using the coding definitions. The adjudicated codes are the ones in Tables S2, S4 and S5.

## Final pre-submission check

The final check applied two rules to every audit relationship (see `CODEBOOK.md` and `docs/evidence_map_method.md`):

- **Execution rule.** A relationship is direct only when AVs/CAVs execute the controlled action, including infrastructure-computed commands that they execute automatically. Infrastructure-executed control and guidance that depends on human compliance give indirect support only.
- **Strict capacity-drop rule.** Direct capacity-drop support needs a sustainable or reference pre-breakdown flow compared with sustained post-breakdown or queue discharge under comparable conditions.

Nine audit relationships changed from direct to indirect, one study (Yang et al., 2018) changed from [D] to [M], and evidence settings were corrected for two experiments and five reviews. All changes are listed in `data/qa_final_coding_changes.csv`.

## Coverage update (October 2026)

A targeted coverage check added six candidate records to Table S1. One was retained (Jang et al., 2025) and five were excluded under the existing criteria, with the reason recorded in Table S1. Wang et al. (2025), a second study from the same 100-vehicle I-24 field test, was already in Table S1 but had been excluded without a recorded reason; it was reinstated as direct evidence. The corpus is now 99 publications (266 candidates, 228 verified, 129 excluded).

Six studies were added to the application–mechanism audit from their full texts: the two new studies and four previously coded primary studies that had been outside the audit (Cai et al., 2024; Stern et al., 2018; Vishnoi et al., 2024; Wu et al., 2022). Three Table S2 fields were corrected from the full texts (Stern et al., 2018, decision lever and design method; Wu et al., 2022, decision lever and operational application; Vishnoi et al., 2024, facility context). Cai et al. (2024) is placed in integrated longitudinal–lateral control, which makes that family's merging-turbulence cell filled; placed in cooperative merging instead, the map would keep three filled cells. All changes are logged in `data/qa_final_coding_changes.csv`.

## Figure S1

Figure S1 cross-tabulates the audit's application families (Table S5) against the study-level evidence settings (Table S2). Counts are unique studies per cell. Families and settings are both non-exclusive, so the counts do not sum to the corpus total.

Rebuild it with:

```
python figures/FigureS1/build_figure_s1.py data/Table_S5_Study_Application_Mechanism_Audit.csv data/Table_S2_Retained_Corpus.csv
```

## Notes on source availability

Three retained references were not available in full text during the final corpus reconciliation:

- Mahmassani (2016)
- Richards (1956)
- Treiber and Kesting (2013)

These entries are flagged in `Table_S2_Retained_Corpus.csv`. No detailed study coding was inferred where the source could not be checked directly.

Copyrighted article PDFs are not included in this repository.

## Search audit trail

> **To do before tagging the release (delete this note afterwards):** the manuscript's Methods describe a discovery audit trail (discovery dates, topic families, representative search formulations, citation tracing and the final TRID validation queries). It is not yet in this repository. Add it, for example as `docs/search_audit_trail.md`, and list it in the Files table.

## Citation

Please cite the accompanying review and this repository when using the coding or synthesis files. Repository citation metadata are provided in `CITATION.cff`. Cite the tagged release that accompanies the submitted manuscript rather than the moving `main` branch.

## License

The author-created coding, synthesis files and documentation are released under the license stated in `LICENSE.md`. Third-party publications and bibliographic content remain subject to their original terms.
