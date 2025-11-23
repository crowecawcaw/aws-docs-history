# Evaluate and release

The evaluate and release focus area provides best practices for
making a responsible release decision, given the release criteria
from [Release criteria](release-criteria.md "release-criteria.md"), the evaluation datasets from [Dataset planning](dataset-planning.md "dataset-planning.md"), and the AI system design from [System planning](system-planning.md "system-planning.md"). The release
decision is a binary (yes or no) decision that aggregates the results
of testing the AI system against each individual release criterion.
A well-designed decision factors in the compounded uncertainty in
the individual criterion decisions, that is have we met each
criterion with the required confidence (for example, are we at
least 95% confident that the release criteria have been satisfied?).
If a specific release criterion is not met, release may still be
possible if the residual risk is disclosed through Monitoring
transparency mechanisms. Otherwise, you should return to [System planning](system-planning.md "system-planning.md") to review options for baking and filtering
mitigations.

###### Focus areas

- [System evaluation](raier01.md "raier01.md")
- [Aggregate results](raier02.md "raier02.md")
- [Address unmet release criteria](raier03.md "raier03.md")
