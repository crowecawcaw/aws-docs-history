# Difference in

Proportions of Labels (DPL)

The difference in proportions of labels (DPL) compares the proportion of observed
outcomes with positive labels for facet _d_ with
the proportion of observed outcomes with positive labels of facet _a_ in a training dataset. For example, you could use it
to compare the proportion of middle-aged individuals (facet _a_) and other age groups (facet _d_)
approved for financial loans. Machine learning models try to mimic the training data
decisions as closely as possible. So a machine learning model trained on a dataset
with a high DPL is likely to reflect the same imbalance in its future
predictions.

The formula for the difference in proportions of labels is as follows:

        DPL = (qa -
qd)

Where:

- qa =
  na(1)/na
  is the proportion of facet _a_ who have an
  observed label value of 1. For example, the proportion of a middle-aged
  demographic who get approved for loans. Here
  na(1) represents the
  number of members of facet _a_ who get a
  positive outcome and na the is number of members of
  facet _a_.
- qd =
  nd(1)/nd
  is the proportion of facet _d_ who have an
  observed label value of 1. For example, the proportion of people outside the
  middle-aged demographic who get approved for loans. Here
  nd(1) represents the
  number of members of the facet _d_ who get
  a positive outcome and nd the is number of members of
  the facet _d_.
  If DPL is close enough to 0, then we say that _demographic
  parity_ has been achieved.

For binary and multicategory facet labels, the DPL values range over the interval
(-1, 1). For continuous labels, we set a threshold to collapse the labels to binary.

- Positive DPL values indicate that facet _a_ is has a higher proportion of positive outcomes when
  compared with facet _d_.
- Values of DPL near zero indicate a more equal proportion of positive
  outcomes between facets and a value of zero indicates perfect demographic
  parity.
- Negative DPL values indicate that facet _d_ has a higher proportion of positive outcomes when compared
  with facet _a_.
  Whether or not a high magnitude of DPL is problematic varies from one situation to
  another. In a problematic case, a high-magnitude DPL might be a signal of underlying
  issues in the data. For example, a dataset with high DPL might reflect historical
  biases or prejudices against age-based demographic groups that would be undesirable
  for a model to learn.
