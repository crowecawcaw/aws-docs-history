# Tuning a Semantic Segmentation Model

_Automatic model tuning_, also known as
hyperparameter tuning, finds the best version of a model by running many jobs that test
a range of hyperparameters on your dataset. You choose the tunable hyperparameters, a
range of values for each, and an objective metric. You choose the objective metric from
the metrics that the algorithm computes. Automatic model tuning searches the
hyperparameters chosen to find the combination of values that result in the model that
optimizes the objective metric.

## Metrics Computed by the Semantic

Segmentation Algorithm

The semantic segmentation algorithm reports two validation metrics. When tuning
hyperparameter values, choose one of these metrics as the objective.

| Metric Name                 | Description                                                                                                                                                                                           | Optimization Direction |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| `validation:mIOU`           | The area of the intersection of the predicted segmentation and<br>the ground truth divided by the area of union between them for<br>images in the validation set. Also known as the Jaccard<br>Index. | Maximize               |
| `validation:pixel_accuracy` | The percentage of pixels that are correctly classified in images<br>from the validation set.                                                                                                          | Maximize               |

## Tunable Semantic Segmentation Hyperparameters

You can tune the following hyperparameters for the semantic segmentation
algorithm.

| Parameter Name    | Parameter Type             | Recommended Ranges             |
| ----------------- | -------------------------- | ------------------------------ |
| `learning_rate`   | ContinuousParameterRange   | MinValue: 1e-4, MaxValue: 1e-1 |
| `mini_batch_size` | IntegerParameterRanges     | MinValue: 1, MaxValue: 128     |
| `momentum`        | ContinuousParameterRange   | MinValue: 0.9, MaxValue: 0.999 |
| `optimzer`        | CategoricalParameterRanges | ['sgd', 'adam', 'adadelta']    |
| `weight_decay`    | ContinuousParameterRange   | MinValue: 1e-5, MaxValue: 1e-3 |
