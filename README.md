# AV/CAV Congestion Review Data

This repository contains the study-level coding and supporting synthesis files for:

**Autonomous Vehicles as Active Agents for Congestion Mitigation: A Review of Longitudinal, Lateral, Cooperative, and Learning-Based Traffic Control Strategies**

**Authors:** Amirali Ataee Naeini, Ashkan Teymouri, and Michael H. Zhang

## Overview

The review examines how autonomous and connected automated vehicles may act as traffic-control agents for congestion mitigation. Its main focus is freeway bottlenecks and mixed traffic.

The literature review followed a semi-systematic process. AI-assisted literature discovery was combined with manual bibliographic verification, eligibility screening, coding and narrative synthesis. Undermind AI and Perplexity were used only to identify candidate publications.

The manuscript-linked corpus contains **97 retained publications**, selected in three steps:

- **260 candidate records** were identified.
- **222 verified records** remained after bibliographic verification and deduplication.
- **97 publications** were retained after eligibility assessment.

## Files

The file names match the supplementary tables cited in the manuscript's Data Availability Statement.

| File | Content |
|---|---|
| `data/Table_S1_Verified_Screening_Matrix.csv` | The 222 verified records and their record-level screening disposition. |
| `data/Table_S2_Retained_Corpus.csv` | The final retained corpus of 97 publications, with review roles (62 [D], 25 [M], 10 [C]), the nine taxonomy dimensions, and descriptive fields (key finding, main limitation, comparator/reference condition). |
| `data/Table_S3_Screening_Flow.csv` | The record counts shown in Figure 1. |
| `data/Table_S4_Application_Mechanism_Evidence_Map.csv` | One row per cell of the 8 × 9 application-family × congestion-mechanism map (Figure 2). Each row gives the final marker, the direct and indirect supporting studies, finding-pattern counts, evidence settings, representative metrics and a cell rationale. |
| `data/Table_S5_Study_Application_Mechanism_Audit.csv` | The study-level application–mechanism audit of 71 retained studies. It has one row per study × family × mechanism relationship. Each row gives the directness (DIRECT, INDIRECT or NONE), a finding pattern for direct relationships, the supporting metric, the evidence setting, a full-text rationale and the source location. |
| `data/Table_S6_Independent_Coding_Agreement.csv` | Agreement between the lead author's coding and a second author's independent coding of a 19-study subset, by dimension, with an adjudication summary. The rows prefixed "Panel B –" hold the sensitivity analysis described below. |
| `data/Table_S6_sensitivity_excluded_comparisons.csv` | The 12 comparisons set aside in the Panel B sensitivity analysis. |
| `data/evidence_role_reconciliation.csv` | The full-text check of the 11 audit reassessments from [D] to [M]: 10 were confirmed and one was restored to [D]. |
| `data/independent_coding_check_adjudication.csv` | One row per non-identical coding (105 rows). Each row gives both coders' codes, the adjudicated code, the rationale, the full-text source, and which records changed. |
| `figures/FigureS1/` | Supplementary Figure S1 with its source script and derived counts. See the README in that folder. |
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

- **●** at least two direct supporting studies, all with consistently positive findings;
- **○** one direct supporting study, or at least one direct finding that is mixed, negative or strongly conditional;
- **□** indirect support only;
- **—** no substantive relationship identified in the coded set.

The final map contains 108 direct and 60 indirect study–cell links. It has 5 ●, 35 ○, 5 □ and 27 — cells.

Markers describe the pattern of support, not study quality or deployment readiness. See [`docs/evidence_map_method.md`](docs/evidence_map_method.md).

## Independent coding check (Table S6)

A second author independently coded a stratified subset of 19 retained studies. Agreement is percentage agreement, computed separately for each dimension:

- **Single-label fields** agree when the two values are identical.
- **Multi-label fields** agree when the two label sets are identical, or when one coder's labels are wholly contained in the other's.

Agreement ranged from 47.4% to 100%.

Panel B is a sensitivity analysis. It sets aside 12 comparisons in which the lead coding still carried labels from before the final codebook, and there the lower bound is 57.9%.

All non-identical codings were adjudicated against the full texts and the coding definitions. The adjudicated codes are the ones in Tables S2, S4 and S5.

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
- Treiber and Kesting (2012)

These entries are flagged in `Table_S2_Retained_Corpus.csv`. No detailed study coding was inferred where the source could not be checked directly.

Copyrighted article PDFs are not included in this repository.

## Citation

Please cite the accompanying review and this repository when using the coding or synthesis files. Repository citation metadata are provided in `CITATION.cff`.

## License

The author-created coding, synthesis files and documentation are released under the license stated in `LICENSE.md`. Third-party publications and bibliographic content remain subject to their original terms.
