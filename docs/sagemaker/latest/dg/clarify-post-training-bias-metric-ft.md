# Counterfactual Fliptest

(FT)

The fliptest is an approach that looks at each member of facet _d_ and assesses whether similar members of facet _a_ have different model predictions. The members of facet _a_ are chosen to be k-nearest neighbors of the observation
from facet _d_. We assess how many nearest neighbors of
the opposite group receive a different prediction, where the flipped prediction can go
from positive to negative and vice versa.

The formula for the counterfactual fliptest is the difference in the cardinality of
two sets divided by the number of members of facet _d_:

        FT = (F+ -
F-)/nd

Where:

- F+ = is the number of disfavored facet _d_ members with an unfavorable outcome whose nearest
  neighbors in favored facet _a_ received a
  favorable outcome.
- F- = is the number of disfavored facet _d_ members with a favorable outcome whose nearest
  neighbors in favored facet _a_ received an
  unfavorable outcome.
- nd is the sample size of facet _d_.
  The range of values for the counterfactual fliptest for binary and multicategory facet
  labels is [-1, +1]. For continuous labels, we set a threshold to collapse the labels to
  binary.

- Positive values occur when the number of unfavorable counterfactual fliptest
  decisions for the disfavored facet _d_ exceeds
  the favorable ones.
- Values near zero occur when the number of unfavorable and favorable
  counterfactual fliptest decisions balance out.
- Negative values occur when the number of unfavorable counterfactual fliptest
  decisions for the disfavored facet _d_ is less
  than the favorable ones.
