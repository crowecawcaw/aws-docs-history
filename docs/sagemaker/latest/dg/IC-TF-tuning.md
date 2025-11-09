# Tune an Image Classification - TensorFlow model

_Automatic model tuning_, also known as
hyperparameter tuning, finds the best version of a model by running many jobs that test
a range of hyperparameters on your dataset. You choose the tunable hyperparameters, a
range of values for each, and an objective metric. You choose the objective metric from
the metrics that the algorithm computes. Automatic model tuning searches the
hyperparameters chosen to find the combination of values that result in the model that
optimizes the objective metric.

For more information about model tuning, see [Automatic model tuning with SageMaker AI](automatic-model-tuning.md "automatic-model-tuning.md").

## Metrics computed by the Image Classification - TensorFlow

algorithm

The image classification algorithm is a supervised algorithm. It reports an
accuracy metric that is computed during training. When tuning the model, choose this
metric as the objective metric.

| Metric Name           | Description                                                                                | Optimization Direction |
| --------------------- | ------------------------------------------------------------------------------------------ | ---------------------- |
| `validation:accuracy` | The ratio of the number of correct predictions to the total<br>number of predictions made. | Maximize               |

## Tunable Image Classification - TensorFlow

hyperparameters

Tune an image classification model with the following hyperparameters. The
hyperparameters that have the greatest impact on image classification objective
metrics are: `batch_size`, `learning_rate`, and
`optimizer`. Tune the optimizer-related hyperparameters, such as
`momentum`, `regularizers_l2`, `beta_1`,
`beta_2`, and `eps` based on the
selected `optimizer`. For example, use `beta_1` and
`beta_2` only when `adam` is the
`optimizer`.

For more information about which hyperparameters are used for each `optimizer`, see
[Image Classification - TensorFlow
Hyperparameters](IC-TF-Hyperparameter.md "IC-TF-Hyperparameter.md").

| Parameter Name         | Parameter Type             | Recommended Ranges                                            |
| ---------------------- | -------------------------- | ------------------------------------------------------------- |
| `batch_size`           | IntegerParameterRanges     | MinValue: 8, MaxValue: 512                                    |
| `beta_1`               | ContinuousParameterRanges  | MinValue: 1e-6, MaxValue: 0.999                               |
| `beta_2`               | ContinuousParameterRanges  | MinValue: 1e-6, MaxValue: 0.999                               |
| `eps`                  | ContinuousParameterRanges  | MinValue: 1e-8, MaxValue: 1.0                                 |
| `learning_rate`        | ContinuousParameterRanges  | MinValue: 1e-6, MaxValue: 0.5                                 |
| `momentum`             | ContinuousParameterRanges  | MinValue: 0.0, MaxValue: 0.999                                |
| `optimizer`            | CategoricalParameterRanges | ['sgd', ‘adam’, ‘rmsprop’, 'nesterov', 'adagrad', 'adadelta'] |
| `regularizers_l2`      | ContinuousParameterRanges  | MinValue: 0.0, MaxValue: 0.999                                |
| `train_only_top_layer` | ContinuousParameterRanges  | ['True', 'False']                                             |
