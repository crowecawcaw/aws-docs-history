# Datasets format and objective

metric for image classification

In this section we learn about the available formats for datasets used in image
classification as well as the objective metric used to evaluate the predictive quality of
machine learning model candidates. The metrics calculated for candidates are specified using
an array of [MetricDatum](../APIReference/API_MetricDatum.md "../APIReference/API_MetricDatum.md") types.

## Datasets formats

Autopilot supports .png, .jpg, and .jpeg image formats. If your dataset contains all
.png images use `image/png`, if it contains all .jpg or .jpeg images use
`image/jpeg`, and if your dataset contains a mix of image formats use
`image/*`.

## Objective metric

The following list contains the names of the metrics that are currently available to
measure the performance of models for image classification.

**`Accuracy`**

The ratio of the number of correctly classified items to the total number of
(correctly and incorrectly) classified items. Accuracy measures how close the
predicted class values are to the actual values. Values for accuracy metrics vary
between zero (0) and one (1). A value of 1 indicates perfect accuracy, and 0 indicates
perfect inaccuracy.
