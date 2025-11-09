# Post-training Data and Model

Bias Metrics

Amazon SageMaker Clarify provides eleven post-training data and model bias metrics to help quantify
various conceptions of fairness. These concepts cannot all be satisfied simultaneously and
the selection depends on specifics of the cases involving potential bias being analyzed.
Most of these metrics are a combination of the numbers taken from the binary classification
confusion matrices for the different demographic groups. Because fairness and bias can be
defined by a wide range of metrics, human judgment is required to understand and choose
which metrics are relevant to the individual use case, and customers should consult with
appropriate stakeholders to determine the appropriate measure of fairness for their
application.

We use the following notation to discuss the bias metrics. The conceptual model described
here is for binary classification, where events are labeled as having only two possible
outcomes in their sample space, referred to as positive (with value 1) and negative (with
value 0). This framework is usually extensible to multicategory classification in a
straightforward way or to cases involving continuous valued outcomes when needed. In the
binary classification case, positive and negative labels are assigned to outcomes recorded
in a raw dataset for a favored facet _a_ and for a
disfavored facet _d_. These labels y are referred to as
_observed labels_ to distinguish them from the _predicted
labels_ y' that are assigned by a machine learning model during the training
or inferences stages of the ML lifecycle. These labels are used to define probability
distributions Pa(y) and Pd(y) for their
respective facet outcomes.

- labels:
  - y represents the n observed labels for event outcomes in a training
    dataset.
  - y' represents the predicted labels for the n observed labels in the
    dataset by a trained model.

- outcomes:
  - A positive outcome (with value 1) for a sample, such as an application
    acceptance.
    - n(1) is the number of observed labels
      for positive outcomes (acceptances).
    - n'(1) is the number of predicted labels
      for positive outcomes (acceptances).

  - A negative outcome (with value 0) for a sample, such as an application
    rejection.
    - n(0) is the number of observed labels
      for negative outcomes (rejections).
    - n'(0) is the number of predicted labels
      for negative outcomes (rejections).

- facet values:
  - facet _a_ – The feature value that
    defines a demographic that bias favors.
    - na is the number of observed labels for the
      favored facet value: na =
      na(1) +
      na(0) the sum
      of the positive and negative observed labels for the value facet
      _a_.
    - n'a is the number of predicted labels for
      the favored facet value: n'a =
      n'a(1) +
      n'a(0) the sum
      of the positive and negative predicted outcome labels for the facet
      value _a_. Note that
      n'a = na.

  - facet _d_ – The feature value that
    defines a demographic that bias disfavors.
    - nd is the number of observed labels for the
      disfavored facet value: nd =
      nd(1) +
      nd(0) the sum
      of the positive and negative observed labels for the facet value
      _d_.
    - n'd is the number of predicted labels for
      the disfavored facet value: n'd =
      n'd(1) +
      n'd(0) the sum
      of the positive and negative predicted labels for the facet value
      _d_. Note that
      n'd = nd.

- probability distributions for outcomes of the labeled facet data outcomes:

      + Pa(y) is the probability distribution of the
       observed labels for facet *a*. For binary
       labeled data, this distribution is given by the ratio of the number of
       samples in facet *a* labeled with positive
       outcomes to the total number,
       Pa(y1) =
       na(1)/
       na, and the ratio of the number of samples with
       negative outcomes to the total number,
       Pa(y0) =
       na(0)/
       na.
      + Pd(y) is the probability distribution of the
       observed labels for facet *d*. For binary
       labeled data, this distribution is given by the number of samples in facet
       *d* labeled with positive outcomes to
       the total number, Pd(y1) =
       nd(1)/
       nd, and the ratio of the number of samples with
       negative outcomes to the total number,
       Pd(y0) =
       nd(0)/
       nd.

  The following table contains a cheat sheet for quick guidance and links to the
  post-training bias metrics.

Post-training bias metrics

| Post-training bias metric                                                                                                                                   | Description                                                                                                                                                           | Example question                                                                                                                                   | Interpreting metric values                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Difference in Positive<br>Proportions in Predicted Labels (DPPL)](clarify-post-training-bias-metric-dppl.md "clarify-post-training-bias-metric-dppl.md")   | Measures the difference in the proportion of positive predictions between<br>the favored facet *a<br>• and the disfavored<br>facet *d\*.                              | Has there been an imbalance across demographic groups in the predicted<br>positive outcomes that might indicate bias?                              | Range for normalized binary & multicategory facet labels:<br>`[-1,+1]`<br>Range for continuous labels: (-∞, +∞)<br>Interpretation:<br>• Positive values indicate that the favored facet _a_ has a higher proportion of<br>predicted positive outcomes.<br>• Values near zero indicate a more equal proportion of predicted<br>positive outcomes between facets.<br>• Negative values indicate the disfavored facet _d_ has a higher proportion of<br>predicted positive outcomes.                                                                                                                                                                       |
| [Disparate Impact (DI)](clarify-post-training-bias-metric-di.md "clarify-post-training-bias-metric-di.md")                                                  | Measures the ratio of proportions of the predicted labels for the favored<br>facet *a<br>• and the disfavored facet<br>*d\*.                                          | Has there been an imbalance across demographic groups in the predicted<br>positive outcomes that might indicate bias?                              | Range for normalized binary, multicategory facet, and continuous<br>labels: [0,∞)<br>Interpretation:<br>• Values less than 1 indicate the favored facet _a_ has a higher proportion of<br>predicted positive outcomes.<br>• A value of 1 indicates that we have demographic parity.<br>• Values greater than 1 indicate the disfavored facet _d_ has a higher proportion of<br>predicted positive outcomes.                                                                                                                                                                                                                                             |
| [Conditional Demographic<br>Disparity in Predicted Labels (CDDPL)](clarify-post-training-bias-metric-cddpl.md "clarify-post-training-bias-metric-cddpl.md") | Measures the disparity of predicted labels between the facets as a whole,<br>but also by subgroups.                                                                   | Do some demographic groups have a larger proportion of rejections for<br>loan application outcomes than their proportion of acceptances?           | The range of CDDPL values for binary, multicategory, and continuous<br>outcomes: `[-1, +1]`<br>• Positive values indicate outcomes where facet _d_ is rejected more than accepted.<br>• Near zero indicates no demographic disparity on<br>average.<br>• Negative values indicate outcomes where facet _a_ is rejected more than<br>accepted.                                                                                                                                                                                                                                                                                                           |
| [Counterfactual Fliptest<br>(FT)](clarify-post-training-bias-metric-ft.md "clarify-post-training-bias-metric-ft.md")                                        | Examines each member of facet *d<br>• and<br>assesses whether similar members of facet *a<br>• have different model predictions.                                      | Is one group of a specific-age demographic matched closely on all<br>features with a different age group, yet paid more on average?                | The range for binary and multicategory facet labels is `[-1,<br>+1]`.<br>• Positive values occur when the number of unfavorable<br>counterfactual fliptest decisions for the disfavored facet<br>*d<br>• exceeds the favorable<br>ones.<br>• Values near zero occur when the number of unfavorable and<br>favorable counterfactual fliptest decisions balance out.<br>• Negative values occur when the number of unfavorable<br>counterfactual fliptest decisions for the disfavored facet<br>*d<br>• is less than the<br>favorable ones.                                                                                                               |
| [Accuracy Difference (AD)](clarify-post-training-bias-metric-ad.md "clarify-post-training-bias-metric-ad.md")                                               | Measures the difference between the prediction accuracy for the favored<br>and disfavored facets.                                                                     | Does the model predict labels as accurately for applications across all<br>demographic groups?                                                     | The range for binary and multicategory facet labels is `[-1,<br>+1]`.<br>• Positive values indicate that facet _d_ suffers more from some combination of false<br>positives (Type I errors) or false negatives (Type II errors).<br>This means there is a potential bias against the disfavored<br>facet _d_.<br>• Values near zero occur when the prediction accuracy for facet<br>*a<br>• is similar to that for<br>facet *d*.<br>• Negative values indicate that facet *a* suffers more from some combination of false<br>positives (Type I errors) or false negatives (Type II errors).<br>This means the is a bias against the favored facet *a\*. |
| [Recall Difference (RD)](clarify-post-training-bias-metric-rd.md "clarify-post-training-bias-metric-rd.md")                                                 | Compares the recall of the model for the favored and disfavored facets.                                                                                               | Is there an age-based bias in lending due to a model having higher recall<br>for one age group as compared to another?                             | Range for binary and multicategory classification: `[-1,<br>+1]`.<br>• Positive values suggest that the model finds more of the true<br>positives for facet *a<br>• and is<br>biased against the disfavored facet *d*.<br>• Values near zero suggest that the model finds about the same<br>number of true positives in both facets and is not<br>biased.<br>• Negative values suggest that the model finds more of the true<br>positives for facet *d<br>• and is<br>biased against the favored facet _a_.                                                                                                                                             |
| [Difference in Conditional<br>Acceptance (DCAcc)](clarify-post-training-bias-metric-dcacc.md "clarify-post-training-bias-metric-dcacc.md")                  | Compares the observed labels to the labels predicted by a model. Assesses<br>whether this is the same across facets for predicted positive outcomes<br>(acceptances). | When comparing one age group to another, are loans accepted more<br>frequently, or less often than predicted (based on qualifications)?            | The range for binary, multicategory facet, and continuous labels:<br>(-∞, +∞).<br>• Positive values indicate a possible bias against the qualified<br>applicants from the disfavored facet _d_.<br>• Values near zero indicate that qualified applicants from both<br>facets are being accepted in a similar way.<br>• Negative values indicate a possible bias against the qualified<br>applicants from the favored facet _a_.                                                                                                                                                                                                                         |
| [Difference in Acceptance Rates<br>(DAR)](clarify-post-training-bias-metric-dar.md "clarify-post-training-bias-metric-dar.md")                              | Measures the difference in the ratios of the observed positive outcomes<br>(TP) to the predicted positives (TP + FP) between the favored and disfavored<br>facets.    | Does the model have equal precision when predicting loan acceptances for<br>qualified applicants across all age groups?                            | The range for binary, multicategory facet, and continuous labels is<br>`[-1, +1]`.<br>• Positive values indicate a possible bias against facet<br>*d<br>• caused by the<br>occurrence of relatively more false positives in the disfavored<br>facet *d*.<br>• Values near zero indicate the observed labels for positive<br>outcomes (acceptances) are being predicted with equal precision<br>for both facets by the model.<br>• Negative values indicate a possible bias against facet<br>*a<br>• caused by the<br>occurrence of relatively more false positives in the favored<br>facet _a_.                                                         |
| [Specificity difference<br>(SD)](clarify-post-training-bias-metric-sd.md "clarify-post-training-bias-metric-sd.md")                                         | Compares the specificity of the model between favored and disfavored<br>facets.                                                                                       | Is there an age-based bias in lending because the model predicts a higher<br>specificity for one age group as compared to another?                 | Range for binary and multicategory classification: `[-1,<br>+1]`.<br>• Positive values suggest that the model finds less false<br>positives for facet *d<br>• and is<br>biased against the disfavored facet *d*.<br>• Values near zero suggest that the model finds a similar number<br>of false positives in both facets and is not biased.<br>• Negative values suggest that the model finds less false<br>positives for facet *a<br>• and is<br>biased against the favored facet _a_.                                                                                                                                                                |
| [Difference in Conditional<br>Rejection (DCR)](clarify-post-training-bias-metric-dcr.md "clarify-post-training-bias-metric-dcr.md")                         | Compares the observed labels to the labels predicted by a model and<br>assesses whether this is the same across facets for negative outcomes<br>(rejections).         | Are there more or less rejections for loan applications than predicted<br>for one age group as compared to another based on qualifications?        | The range for binary, multicategory facet, and continuous labels:<br>(-∞, +∞).<br>• Positive values indicate a possible bias against the qualified<br>applicants from the disfavored facet _d_.<br>• Values near zero indicate that qualified applicants from both<br>facets are being rejected in a similar way.<br>• Negative values indicate a possible bias against the qualified<br>applicants from the favored facet _a_.                                                                                                                                                                                                                         |
| [Difference in Rejection Rates<br>(DRR)](clarify-post-training-bias-metric-drr.md "clarify-post-training-bias-metric-drr.md")                               | Measures the difference in the ratios of the observed negative outcomes<br>(TN) to the predicted negatives (TN + FN) between the disfavored and favored<br>facets.    | Does the model have equal precision when predicting loan rejections for<br>unqualified applicants across all age groups?                           | The range for binary, multicategory facet, and continuous labels is<br>`[-1, +1]`.<br>• Positive values indicate a possible bias caused by the<br>occurrence of relatively more false negatives in the favored<br>facet _a_.<br>• Values near zero indicate that negative outcomes (rejections)<br>are being predicted with equal precision for both facets.<br>• Negative values indicate a possible bias caused by the<br>occurrence of relatively more false negatives in the disfavored<br>facet _d_.                                                                                                                                               |
| [Treatment Equality (TE)](clarify-post-training-bias-metric-te.md "clarify-post-training-bias-metric-te.md")                                                | Measures the difference in the ratio of false positives to false<br>negatives between the favored and disfavored facets.                                              | In loan applications, is the relative ratio of false positives to false<br>negatives the same across all age demographics?                         | The range for binary and multicategory facet labels: (-∞, +∞).<br>• Positive values occur when the ratio of false positives to<br>false negatives for facet _a_<br>is greater than that for facet _d_.<br>• Values near zero occur when the ratio of false positives to<br>false negatives for facet _a_<br>is similar to that for facet _d_.<br>• Negative values occur when the ratio of false positives to<br>false negatives for facet _a_<br>is less than that for facet _d_.                                                                                                                                                                      |
| [Generalized entropy (GE)](clarify-post-training-bias-metric-ge.md "clarify-post-training-bias-metric-ge.md")                                               | Measures the inequality in benefits `b` assigned to each input<br>by the model predictions.                                                                           | Of two candidate models for loan application classification, does one<br>lead to a more uneven distribution of desired outcomes than the<br>other? | The range for binary and multicategory labels: (0, 0.5). GE is undefined<br>when the model predicts only false negatives.<br>• Zero values occur when all predictions are correct or all<br>predictions are false positives.<br>• Positive values indicate inequality in benefits; 0.5<br>corresponds to the largest inequality.                                                                                                                                                                                                                                                                                                                        |

For additional information about post-training bias metrics, see [A Family of Fairness Measures for Machine Learning in Finance](https://pages.awscloud.com/rs/112-TZM-766/images/Fairness.Measures.for.Machine.Learning.in.Finance.pdf "https://pages.awscloud.com/rs/112-TZM-766/images/Fairness.Measures.for.Machine.Learning.in.Finance.pdf").

###### Topics

- [Difference in Positive
  Proportions in Predicted Labels (DPPL)](clarify-post-training-bias-metric-dppl.md "clarify-post-training-bias-metric-dppl.md")
- [Disparate Impact (DI)](clarify-post-training-bias-metric-di.md "clarify-post-training-bias-metric-di.md")
- [Difference in Conditional
  Acceptance (DCAcc)](clarify-post-training-bias-metric-dcacc.md "clarify-post-training-bias-metric-dcacc.md")
- [Difference in Conditional
  Rejection (DCR)](clarify-post-training-bias-metric-dcr.md "clarify-post-training-bias-metric-dcr.md")
- [Specificity difference
  (SD)](clarify-post-training-bias-metric-sd.md "clarify-post-training-bias-metric-sd.md")
- [Recall Difference (RD)](clarify-post-training-bias-metric-rd.md "clarify-post-training-bias-metric-rd.md")
- [Difference in Acceptance Rates
  (DAR)](clarify-post-training-bias-metric-dar.md "clarify-post-training-bias-metric-dar.md")
- [Difference in Rejection Rates
  (DRR)](clarify-post-training-bias-metric-drr.md "clarify-post-training-bias-metric-drr.md")
- [Accuracy Difference (AD)](clarify-post-training-bias-metric-ad.md "clarify-post-training-bias-metric-ad.md")
- [Treatment Equality (TE)](clarify-post-training-bias-metric-te.md "clarify-post-training-bias-metric-te.md")
- [Conditional Demographic
  Disparity in Predicted Labels (CDDPL)](clarify-post-training-bias-metric-cddpl.md "clarify-post-training-bias-metric-cddpl.md")
- [Counterfactual Fliptest
  (FT)](clarify-post-training-bias-metric-ft.md "clarify-post-training-bias-metric-ft.md")
- [Generalized entropy (GE)](clarify-post-training-bias-metric-ge.md "clarify-post-training-bias-metric-ge.md")
