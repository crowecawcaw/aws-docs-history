# Metrics reference

The following sections describe the metrics that are available in Amazon SageMaker Canvas for each model
type.

## Metrics for numeric prediction

The following list defines the metrics for numeric prediction in SageMaker Canvas and gives you
information about how you can use them.

- InferenceLatency – The approximate amount of time between making a
  request for a model prediction to receiving it from a real-time endpoint to
  which the model is deployed. This metric is measured in seconds and is only
  available for models built with the **Ensembling**mode.
- MAE – Mean absolute error. On average, the prediction for the target
  column is +/- {MAE} from the actual value.

Measures how different the predicted and actual values are when they're
averaged over all values. MAE is commonly used in numeric prediction to
understand model prediction error. If the predictions are linear, MAE represents
the average distance from a predicted line to the actual value. MAE is defined
as the sum of absolute errors divided by the number of observations. Values
range from 0 to infinity, with smaller numbers indicating a better model fit to
the data.

- MAPE – Mean absolute percent error. On average, the prediction for the
  target column is +/- {MAPE} % from the actual value.

MAPE is the mean of the absolute differences between the actual values and the
predicted or estimated values, divided by the actual values and expressed as a
percentage. A lower MAPE indicates better performance, as it means that the
predicted or estimated values are closer to the actual values.

- MSE – Mean squared error, or the average of the squared differences
  between the predicted and actual values.

MSE values are always positive. The better a model is at predicting the actual
values, the smaller the MSE value is.

- R2 – The percentage of the difference in the target column that can be
  explained by the input column.

Quantifies how much a model can explain the variance of a dependent variable.
Values range from one (1) to negative one (-1). Higher numbers indicate a higher
fraction of explained variability. Values close to zero (0) indicate that very
little of the dependent variable can be explained by the model. Negative values
indicate a poor fit and that the model is outperformed by a constant function
(or a horizontal line).

- RMSE – Root mean squared error, or the standard deviation of the
  errors.

Measures the square root of the squared difference between predicted and
actual values, and is averaged over all values. It is used to understand model
prediction error, and it's an important metric to indicate the presence of large
model errors and outliers. Values range from zero (0) to infinity, with smaller
numbers indicating a better model fit to the data. RMSE is dependent on scale,
and should not be used to compare datasets of different types.

## Metrics for categorical prediction

This section defines the metrics for categorical prediction in SageMaker Canvas and gives you
information about how you can use them.

The following is a list of available metrics for 2-category prediction:

- Accuracy – The percentage of correct predictions.

Or, the ratio of the number of correctly predicted items to the total number
of predictions. Accuracy measures how close the predicted class values are to
the actual values. Values for accuracy metrics vary between zero (0) and one
(1). A value of 1 indicates perfect accuracy, and 0 indicates complete
inaccuracy.

- AUC – A value between 0 and 1 that indicates how well your model is
  able to separate the categories in your dataset. A value of 1 indicates that it
  was able to separate the categories perfectly.
- BalancedAccuracy – Measures the ratio of accurate predictions to all
  predictions.

This ratio is calculated after normalizing true positives (TP) and true
negatives (TN) by the total number of positive (P) and negative (N) values. It
is defined as follows: `0.5*((TP/P)+(TN/N))`, with values ranging
from 0 to 1. The balanced accuracy metric gives a better measure of accuracy
when the number of positives or negatives differ greatly from each other in an
imbalanced dataset, such as when only 1% of email is spam.

- F1 – A balanced measure of accuracy that takes class balance into
  account.

It is the harmonic mean of the precision and recall scores, defined as
follows: `F1 = 2 * (precision * recall) / (precision + recall)`. F1
scores vary between 0 and 1. A score of 1 indicates the best possible
performance, and 0 indicates the worst.

- InferenceLatency – The approximate amount of time between making a
  request for a model prediction to receiving it from a real-time endpoint to
  which the model is deployed. This metric is measured in seconds and is only
  available for models built with the **Ensembling**mode.
- LogLoss – Log loss, also known as cross-entropy loss, is a metric used
  to evaluate the quality of the probability outputs, rather than the outputs
  themselves. Log loss is an important metric to indicate when a model makes
  incorrect predictions with high probabilities. Values range from 0 to infinity.
  A value of 0 represents a model that perfectly predicts the data.
- Precision – Of all the times that {category x} was predicted, the
  prediction was correct {precision}% of the time.

Precision measures how well an algorithm predicts the true positives (TP) out
of all of the positives that it identifies. It is defined as follows:
`Precision = TP/(TP+FP)`, with values ranging from zero (0) to
one (1). Precision is an important metric when the cost of a false positive is
high. For example, the cost of a false positive is very high if an airplane
safety system is falsely deemed safe to fly. A false positive (FP) reflects a
positive prediction that is actually negative in the data.

- Recall – The model correctly predicted {recall}% to be {category x}
  when {target_column} was actually {category x}.

Recall measures how well an algorithm correctly predicts all of the true
positives (TP) in a dataset. A true positive is a positive prediction that is
also an actual positive value in the data. Recall is defined as follows:
`Recall = TP/(TP+FN)`, with values ranging from 0 to 1. Higher
scores reflect a better ability of the model to predict true positives (TP) in
the data. Note that it is often insufficient to measure only recall, because
predicting every output as a true positive yields a perfect recall score.

The following is a list of available metrics for 3+ category prediction:

- Accuracy – The percentage of correct predictions.

Or, the ratio of the number of correctly predicted items to the total number
of predictions. Accuracy measures how close the predicted class values are to
the actual values. Values for accuracy metrics vary between zero (0) and one
(1). A value of 1 indicates perfect accuracy, and 0 indicates complete
inaccuracy.

- BalancedAccuracy – Measures the ratio of accurate predictions to all
  predictions.

This ratio is calculated after normalizing true positives (TP) and true
negatives (TN) by the total number of positive (P) and negative (N) values. It
is defined as follows: `0.5*((TP/P)+(TN/N))`, with values ranging
from 0 to 1. The balanced accuracy metric gives a better measure of accuracy
when the number of positives or negatives differ greatly from each other in an
imbalanced dataset, such as when only 1% of email is spam.

- F1macro – The F1macro score applies F1 scoring by calculating the
  precision and recall, and then taking their harmonic mean to calculate the F1
  score for each class. Then, the F1macro averages the individual scores to obtain
  the F1macro score. F1macro scores vary between 0 and 1. A score of 1 indicates
  the best possible performance, and 0 indicates the worst.
- InferenceLatency – The approximate amount of time between making a
  request for a model prediction to receiving it from a real-time endpoint to
  which the model is deployed. This metric is measured in seconds and is only
  available for models built with the **Ensembling**mode.
- LogLoss – Log loss, also known as cross-entropy loss, is a metric used
  to evaluate the quality of the probability outputs, rather than the outputs
  themselves. Log loss is an important metric to indicate when a model makes
  incorrect predictions with high probabilities. Values range from 0 to infinity.
  A value of 0 represents a model that perfectly predicts the data.
- PrecisionMacro – Measures precision by calculating precision for each
  class and averaging scores to obtain precision for several classes. Scores range
  from zero (0) to one (1). Higher scores reflect the model's ability to predict
  true positives (TP) out of all of the positives that it identifies, averaged
  across multiple classes.
- RecallMacro – Measures recall by calculating recall for each class and
  averaging scores to obtain recall for several classes. Scores range from 0 to 1.
  Higher scores reflect the model's ability to predict true positives (TP) in a
  dataset, whereas a true positive reflects a positive prediction that is also an
  actual positive value in the data. It is often insufficient to measure only
  recall, because predicting every output as a true positive will yield a perfect
  recall score.

Note that for 3+ category prediction, you also receive the average F1, Accuracy,
Precision, and Recall metrics. The scores for these metrics are just the metric scores
averaged for all categories.

## Metrics for image and text prediction

The following is a list of available metrics for image prediction and text
prediction.

- Accuracy – The percentage of correct predictions.

Or, the ratio of the number of correctly predicted items to the total number
of predictions. Accuracy measures how close the predicted class values are to
the actual values. Values for accuracy metrics vary between zero (0) and one
(1). A value of 1 indicates perfect accuracy, and 0 indicates complete
inaccuracy.

- F1 – A balanced measure of accuracy that takes class balance into
  account.

It is the harmonic mean of the precision and recall scores, defined as
follows: `F1 = 2 * (precision * recall) / (precision + recall)`. F1
scores vary between 0 and 1. A score of 1 indicates the best possible
performance, and 0 indicates the worst.

- Precision – Of all the times that {category x} was predicted, the
  prediction was correct {precision}% of the time.

Precision measures how well an algorithm predicts the true positives (TP) out
of all of the positives that it identifies. It is defined as follows:
`Precision = TP/(TP+FP)`, with values ranging from zero (0) to
one (1). Precision is an important metric when the cost of a false positive is
high. For example, the cost of a false positive is very high if an airplane
safety system is falsely deemed safe to fly. A false positive (FP) reflects a
positive prediction that is actually negative in the data.

- Recall – The model correctly predicted {recall}% to be {category x}
  when {target_column} was actually {category x}.

Recall measures how well an algorithm correctly predicts all of the true
positives (TP) in a dataset. A true positive is a positive prediction that is
also an actual positive value in the data. Recall is defined as follows:
`Recall = TP/(TP+FN)`, with values ranging from 0 to 1. Higher
scores reflect a better ability of the model to predict true positives (TP) in
the data. Note that it is often insufficient to measure only recall, because
predicting every output as a true positive yields a perfect recall score.

Note that for image and text prediction models where you are predicting 3 or more
categories, you also receive the _average_ F1,
Accuracy, Precision, and Recall metrics. The scores for these metrics are just the
metric scores average for all categories.

## Metrics for time series

forecasts

The following defines the advanced metrics for time series forecasts in Amazon SageMaker Canvas and
gives you information about how you can use them.

- Average Weighted Quantile Loss (wQL) – Evaluates the forecast by
  averaging the accuracy at the P10, P50, and P90 quantiles. A lower value
  indicates a more accurate model.
- Weighted Absolute Percent Error (WAPE) – The sum of the absolute error
  normalized by the sum of the absolute target, which measures the overall
  deviation of forecasted values from observed values. A lower value indicates a
  more accurate model, where WAPE = 0 is a model with no errors.
- Root Mean Square Error (RMSE) – The square root of the average squared
  errors. A lower RMSE indicates a more accurate model, where RMSE = 0 is a model
  with no errors.
- Mean Absolute Percent Error (MAPE) – The percentage error (percent
  difference of the mean forecasted value versus the actual value) averaged over
  all time points. A lower value indicates a more accurate model, where MAPE = 0
  is a model with no errors.
- Mean Absolute Scaled Error (MASE) – The mean absolute error of the
  forecast normalized by the mean absolute error of a simple baseline forecasting
  method. A lower value indicates a more accurate model, where MASE < 1 is
  estimated to be better than the baseline and MASE > 1 is estimated to be
  worse than the baseline.
