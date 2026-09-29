# Application-Family–Mechanism Evidence Map

The application–mechanism map summarizes how the operational applications reviewed in the paper relate to the congestion mechanisms used in the synthesis.

The map is intended as a qualitative evidence summary, not a meta-analysis.

## Marker assignment

Direct support is cell-specific. A study contributes to `direct_supporting_study_count` only when it is coded to the relevant operational application family, directly evaluates or reports the relevant congestion mechanism or a mechanism-specific outcome, and provides a traffic-flow or congestion outcome supporting that relationship. Classification as [D] denotes direct evidence for at least one coded congestion-control claim and does not imply direct support for every Figure 2 cell.

**● Direct, repeated support**

Requires `direct_supporting_study_count >= 2` and broadly consistent coded direct findings, with no direct-supporting study reporting an explicit negative, mixed, or strongly conditional result for that cell.

**○ Direct, limited or mixed support**

Requires `direct_supporting_study_count >= 1` and either `direct_supporting_study_count = 1` or at least one negative, mixed, or strongly conditional direct finding.

**□ Indirect relationship**

Requires `direct_supporting_study_count = 0` and `indirect_supporting_study_count >= 1`.

**— No substantive relationship identified**

Requires `direct_supporting_study_count = 0` and `indirect_supporting_study_count = 0`.

Marker categories describe the pattern of support in the retained coded set, not methodological quality, field validation, causal certainty across settings, deployment readiness, or treatment-effect magnitude. Several consistent simulation studies may therefore yield ● while the evidence setting remains simulation. A dash indicates only that no substantive relationship was identified in the retained corpus.

## Source data and aggregation

The map is aggregated mechanically from the study-level audit in `data/Table_S5_Study_Application_Mechanism_Audit.csv`. That file has one row per study × application family × congestion mechanism, coded DIRECT, INDIRECT or NONE. A finding pattern is recorded for direct relationships only. No study-level field is reinterpreted during aggregation.

The cell-level result is `data/Table_S4_Application_Mechanism_Evidence_Map.csv`. For each of the 72 cells it records:

- the final marker and its meaning;
- the direct and indirect supporting-study counts, IDs and citations;
- counts of direct findings by pattern (consistently positive, mixed, negative, strongly conditional);
- the evidence roles and evidence settings of the supporting studies;
- representative supporting metrics;
- a short cell rationale.

The final map contains 108 direct and 60 indirect study–cell links, giving 5 ●, 35 ○, 5 □ and 27 — cells.

Study count is descriptive. It is not interpreted as an effect-size estimate or an evidence-quality score.

The map should therefore be read together with the study context, evidence setting, congestion metric and limitations reported elsewhere in the review.
