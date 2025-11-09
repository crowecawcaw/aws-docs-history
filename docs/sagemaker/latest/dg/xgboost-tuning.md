# Tune an XGBoost Model

_Automatic model tuning_, also known as
hyperparameter tuning, finds the best version of a model by running many jobs that test
a range of hyperparameters on your training and validation datasets. You choose three
types of hyperparameters:

- a learning `objective` function to optimize during model
  training
- an `eval_metric` to use to evaluate model performance during
  validation
- a set of hyperparameters and a range of values for each to use when tuning the
  model automatically
  You choose the evaluation metric from set of evaluation metrics that the algorithm
  computes. Automatic model tuning searches the hyperparameters chosen to find the
  combination of values that result in the model that optimizes the evaluation metric.

###### Note

Automatic model tuning for XGBoost 0.90 is only available from the Amazon SageMaker SDKs,
not from the SageMaker AI console.

For more information about model tuning, see [Automatic model tuning with SageMaker AI](automatic-model-tuning.md "automatic-model-tuning.md").

## Evaluation Metrics Computed by the XGBoost

Algorithm

The XGBoost algorithm computes the following metrics to use for model validation.
When tuning the model, choose one of these metrics to evaluate the model. For full
list of valid `eval_metric` values, refer to [XGBoost Learning Task Parameters](https://github.com/dmlc/xgboost/blob/master/doc/parameter.rst#learning-task-parameters "https://github.com/dmlc/xgboost/blob/master/doc/parameter.rst#learning-task-parameters")

| Metric Name           | Description                                                                                       | Optimization Direction |
| --------------------- | ------------------------------------------------------------------------------------------------- | ---------------------- |
| `validation:accuracy` | Classification rate, calculated as #(right)/#(all<br>cases).                                      | Maximize               |
| `validation:auc`      | Area under the curve.                                                                             | Maximize               |
| `validation:error`    | Binary classification error rate, calculated as #(wrong<br>cases)/#(all cases).                   | Minimize               |
| `validation:f1`       | Indicator of classification accuracy, calculated as the<br>harmonic mean of precision and recall. | Maximize               |
| `validation:logloss`  | Negative log-likelihood.                                                                          | Minimize               |
| `validation:mae`      | Mean absolute error.                                                                              | Minimize               |
| `validation:map`      | Mean average precision.                                                                           | Maximize               |
| `validation:merror`   | Multiclass classification error rate, calculated as #(wrong<br>cases)/#(all cases).               | Minimize               |
| `validation:mlogloss` | Negative log-likelihood for multiclass classification.                                            | Minimize               |
| `validation:mse`      | Mean squared error.                                                                               | Minimize               |
| `validation:ndcg`     | Normalized Discounted Cumulative Gain.                                                            | Maximize               |
| `validation:rmse`     | Root mean square error.                                                                           | Minimize               |

## Tunable XGBoost Hyperparameters

Tune the XGBoost model with the following hyperparameters. The hyperparameters
that have the greatest effect on optimizing the XGBoost evaluation metrics are:
`alpha`, `min_child_weight`, `subsample`,
`eta`, and `num_round`.

| Parameter Name      | Parameter<br>Type         | Recommended Ranges           |
| ------------------- | ------------------------- | ---------------------------- |
| `alpha`             | ContinuousParameterRanges | MinValue: 0, MaxValue: 1000  |
| `colsample_bylevel` | ContinuousParameterRanges | MinValue: 0.1, MaxValue: 1   |
| `colsample_bynode`  | ContinuousParameterRanges | MinValue: 0.1, MaxValue: 1   |
| `colsample_bytree`  | ContinuousParameterRanges | MinValue: 0.5, MaxValue: 1   |
| `eta`               | ContinuousParameterRanges | MinValue: 0.1, MaxValue: 0.5 |
| `gamma`             | ContinuousParameterRanges | MinValue: 0, MaxValue: 5     |
| `lambda`            | ContinuousParameterRanges | MinValue: 0, MaxValue: 1000  |
| `max_delta_step`    | IntegerParameterRanges    | [0, 10]                      |
| `max_depth`         | IntegerParameterRanges    | [0, 10]                      |
| `min_child_weight`  | ContinuousParameterRanges | MinValue: 0, MaxValue: 120   |
| `num_round`         | IntegerParameterRanges    | [1, 4000]                    |
| `subsample`         | ContinuousParameterRanges | MinValue: 0.5, MaxValue: 1   |
