# Difference in Positive

Proportions in Predicted Labels (DPPL)

The difference in positive proportions in predicted labels (DPPL) metric determines
whether the model predicts outcomes differently for each facet. It is defined as the
difference between the proportion of positive predictions (y’ = 1) for facet _a_ and the proportion of positive predictions (y’ = 1) for
facet _d_. For example, if the model predictions grant
loans to 60% of a middle-aged group (facet _a_) and 50%
other age groups (facet _d_), it might be biased
against facet _d_. In this example, you must determine
whether the 10% difference is material to a case for bias.

A comparison of difference in proportions of labels (DPL), a measure of pre-training
bias, with DPPL, a measure of post-training bias, assesses whether bias in positive
proportions that are initially present in the dataset changes after training. If DPPL is
larger than DPL, then bias in positive proportions increased after training. If DPPL is
smaller than DPL, the model did not increase bias in positive proportions after
training. Comparing DPL against DPPL does not guarantee that the model reduces bias
along all dimensions. For example, the model may still be biased when considering other
metrics such as [Counterfactual Fliptest
(FT)](clarify-post-training-bias-metric-ft.md "clarify-post-training-bias-metric-ft.md") or [Accuracy Difference (AD)](clarify-post-training-bias-metric-ad.md "clarify-post-training-bias-metric-ad.md"). For more information about
bias detection, see the blog post [Learn how Amazon SageMaker Clarify helps detect bias](https://aws.amazon.com/blogs/machine-learning/learn-how-amazon-sagemaker-clarify-helps-detect-bias/ "https://aws.amazon.com/blogs/machine-learning/learn-how-amazon-sagemaker-clarify-helps-detect-bias/"). See [Difference in
Proportions of Labels (DPL)](clarify-data-bias-metric-true-label-imbalance.md "clarify-data-bias-metric-true-label-imbalance.md") for more information
about DPL.

The formula for the DPPL is:

        DPPL = q'a -
q'd

Where:

- q'a =
  n'a(1)/na
  is the predicted proportion of facet _a_ who
  get a positive outcome of value 1. In our example, the proportion of a
  middle-aged facet predicted to get granted a loan. Here
  n'a(1) represents the
  number of members of facet _a_ who get a
  positive predicted outcome of value 1 and na the is
  number of members of facet _a_.
- q'd =
  n'd(1)/nd
  is the predicted proportion of facet _d_ who
  get a positive outcome of value 1. In our example, a facet of older and younger
  people predicted to get granted a loan. Here
  n'd(1) represents the
  number of members of facet _d_ who get a
  positive predicted outcome and nd the is number of
  members of facet _d_.
  If DPPL is close enough to 0, it means that post-training _demographic
  parity_ has been achieved.

For binary and multicategory facet labels, the normalized DPL values range over the
interval [-1, 1]. For continuous labels, the values vary over the interval (-∞,
+∞).

- Positive DPPL values indicate that facet _a_
  has a higher proportion of predicted positive outcomes when compared with facet
  _d_.

This is referred to as _positive bias_.

- Values of DPPL near zero indicate a more equal proportion of predicted
  positive outcomes between facets _a_ and
  _d_ and a value of zero indicates perfect
  demographic parity.
- Negative DPPL values indicate that facet _d_
  has a higher proportion of predicted positive outcomes when compared with facet
  _a_. This is referred to as
  _negative bias_.
