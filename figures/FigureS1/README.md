# Supplementary Figure S1

Figure S1. Evidence settings across AV/CAV congestion-control application families. Rows are the eight application families of the application–mechanism audit (Table S5); a study is counted once in a family when it has at least one direct or indirect relationship coded to that family. Columns are the six controlled evidence settings from the study-level coding in the retained corpus (Table S2). Each cell reports unique studies. Families and evidence settings are both non-exclusive, so cells, rows and columns should not be summed to the corpus or audit totals. The right-hand column gives the number of audited studies in each family.

Sources (repository `data/` folder):
- `Table_S5_Study_Application_Mechanism_Audit.csv` (final adjudicated audit)
- `Table_S2_Retained_Corpus.csv` (final adjudicated corpus)

This version replaces the earlier heatmap, which counted corpus-level operational-application codes rather than the audit families used in the manuscript text and Figure 2.

Of the 77 audited studies, 76 have at least one coded relationship. The October 2026 coverage update added six audited studies (Cai et al., 2024; Jang et al., 2025; Stern et al., 2018; Vishnoi et al., 2024; Wang et al., 2025; Wu et al., 2022), which adds the field-experiment counts for traffic smoothing (Jang et al., 2025) and speed harmonization (Wang et al., 2025) and the test-track count for traffic smoothing (Stern et al., 2018). Families count both direct and indirect relationships, so the final-QA directness changes do not alter family membership; the evidence-setting corrections (Shladover et al., 2012, simulation only) remove one platooning × field count. Daganzo et al. (2002) contributes to three families but has no controlled evidence setting in Table S2, so it appears in the family totals but in no setting column. A zero means no coded combination in this corpus, not that no such evidence exists.

Files:
- `Figure_S1.png` (600 dpi), `Figure_S1.svg`, `Figure_S1.pdf`: the figure.
- `Figure_S1_matrix.csv`: the plotted counts, with the family totals.
- `Figure_S1_cell_membership.csv`: the audit study IDs and corpus IDs behind each cell.
- `corpus_profile_counts.csv`: corpus-level marginal counts reported in Section 2.1 (roles, evidence settings, operational-application codes), computed from Table S2.
- `source_provenance.json`: SHA-256 of both input files and the counting rule.

Reproduce with Python and matplotlib (Liberation Sans font):

```
python figures/FigureS1/build_figure_s1.py data/Table_S5_Study_Application_Mechanism_Audit.csv data/Table_S2_Retained_Corpus.csv
```
