# AV/CAV Congestion Review Data

This repository contains the study-level coding and supporting synthesis files for:

**Autonomous Vehicles as Active Agents for Congestion Mitigation: A Review of Longitudinal, Lateral, Cooperative, and Learning-Based Traffic Control Strategies**

**Authors:** Amirali Ataee Naeini, Ashkan Teymouri, and Michael H. Zhang

## Overview

The review examines how autonomous and connected autonomous vehicles may act as traffic-control agents for congestion mitigation, with a primary focus on freeway bottlenecks and mixed traffic.

The literature review was conducted using a semi-systematic process that combined AI-assisted literature discovery with manual bibliographic verification, eligibility screening, coding, and narrative synthesis. Undermind AI and Perplexity were used only to identify candidate publications. Final inclusion decisions, coding, interpretation, and synthesis were performed manually.

The current manuscript-linked corpus contains **91 retained publications**. These were selected from **216 unique and verifiable records**, which in turn were obtained from **254 candidate records** after bibliographic verification and deduplication.

## Files

### `data/retained_corpus.csv`
The final 91-publication manuscript corpus. It contains the harmonized coding used in the review, including congestion mechanism, AV/CAV decision lever, design method, coordination/implementation mode, operational application, facility or system scale, mixed-traffic condition, evidence setting, congestion metric, key finding, and main limitation.

### `data/verified_screening_matrix.csv`
The 216 unique and verifiable records that remained after bibliographic verification and deduplication.

### `data/screening_flow.csv`
The record counts used to document the literature-selection process.

### `data/application_mechanism_evidence_map.csv`
Cell-level support for the application–mechanism synthesis map, including supporting-study counts, study identifiers, evidence settings, facility tags, common design methods, and a short rationale for each cell.

### `data/application_mechanism_figure_matrix.csv`
A compact application × mechanism matrix used to construct the synthesis figure.

### `data/study_application_mechanism_audit.csv`
Study-level audit used to support the application–mechanism map.

### `data/manuscript_reference_match_audit.csv`
Reference-level audit showing how the papers cited in the manuscript were matched to the screening matrix or separately verified.

### `figures/FigureS1/Figure_S1_matrix.csv` 
Contains the plotted counts. 

### `figures/FigureS1/Figure_S1_cell_membership.csv` 
Lists contributing corpus IDs for each cell. 

### `figures/FigureS1/corpus_profile_counts.csv` 
Contains the marginal counts used in Section 2.

Reproduce with Python, numpy, and matplotlib: `python build_figure_s1.py /path/to/retained_corpus.csv`.

## Coding structure

The review separates several concepts that are often grouped together in AV/CAV studies:

- **Congestion mechanism:** the traffic-flow process or system consequence being targeted.
- **Decision lever:** the executable AV/CAV action, such as acceleration, desired speed, headway, lane choice, merge/yield, route choice, or access decision.
- **Design method:** the method used to compute or learn the control action, such as rule-based control, optimal control, MPC, game-theoretic control, or RL/MARL.
- **Coordination/implementation mode:** how information and control authority are organized, such as onboard, cooperative V2V, infrastructure-assisted, centralized, or distributed control.
- **Operational application:** the traffic-management function being implemented.
- **Facility/system scale:** the physical or network setting.
- **Mixed-traffic condition:** assumptions about penetration, controllability, human behavior, communication, and related factors.
- **Evidence setting:** analytical/theoretical, simulation, test-track, field experiment, observational/open-road data, or network/demand model.
- **Congestion metric:** the outcome used to evaluate the congestion claim.

`key_finding` and `main_limitation` are descriptive synthesis fields rather than additional taxonomy dimensions.

Baseline/comparator is not coded as a corpus-wide taxonomy field. It is used only where needed for study-specific comparison in the synthesis.

## Application–mechanism map

The synthesis map uses the following markers:

- **●** direct relationship with repeated support in the retained literature
- **○** direct relationship with limited, mixed, or strongly conditional support
- **□** indirect or mediated relationship
- **—** no substantive relationship identified in the coded support set

The marker assignment is a structured qualitative synthesis rather than a meta-analysis or numerical ranking. More detail is provided in [`docs/evidence_map_method.md`](docs/evidence_map_method.md).

## Figure S1 - Evidence settings across AV/CAV congestion-control application families
Cells report numbers of retained studies coded to each application–evidence-setting combination. Application and evidence-setting fields are multi-label, so counts are non-exclusive and should not be summed as independent study totals.

The eight application labels and six evidence-setting labels are matched exactly after splitting the existing fields on semicolons and trimming whitespace. Each study is counted once per cell. Eighty of 96 records have at least one listed application. Five records have no label matching the six controlled evidence settings; their original values are recorded in source_provenance.json. A zero is a zero coded combination, not a statement that no evidence exists outside this corpus. No facility bins, role changes, or quality/maturity scores are introduced.

## Notes on source availability

Three retained references were not available in full text during the final corpus reconciliation:

- Mahmassani (2016)
- Richards (1956)
- Treiber and Kesting (2012)

These entries are clearly flagged in `retained_corpus.csv`. No detailed study coding was inferred where the source could not be checked directly.

Copyrighted article PDFs are not included in this repository.

## Citation

Please cite the accompanying review and this repository when using the coding or synthesis files. Repository citation metadata are provided in `CITATION.cff`.

## License

The author-created coding, synthesis files, and documentation are released under the license stated in `LICENSE.md`. Third-party publications and bibliographic content remain subject to their original terms.
