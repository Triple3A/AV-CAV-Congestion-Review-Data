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

## Supporting information

The detailed basis for each cell is recorded in `data/application_mechanism_evidence_map.csv`, including:

- supporting-study count;
- supporting study IDs;
- direct versus indirect relationship;
- evidence settings;
- typical facilities;
- common design methods;
- a short rationale.

Study count is descriptive and is not interpreted as an effect-size estimate or evidence-quality score.

The map should therefore be read together with the study context, evidence setting, congestion metric, and limitations reported elsewhere in the review.
