# Tune a TabTransformer model

_Automatic model tuning_, also known as
hyperparameter tuning, finds the best version of a model by running many jobs that test
a range of hyperparameters on your training and validation datasets. Model tuning
focuses on the following hyperparameters:

###### Note

The learning objective function and evaluation metric are both automatically
assigned based on the type of classification task, which is determined by the number
of unique integers in the label column. For more information, see
[TabTransformer hyperparameters](tabtransformer-hyperparameters.md "tabtransformer-hyperparameters.md").

- A learning objective function to optimize during model training
- An evaluation metric that is used to evaluate model performance during
  validation
- A set of hyperparameters and a range of values for each to use when tuning the
  model automatically
  Automatic model tuning searches your chosen hyperparameters to find the combination of
  values that results in a model that optimizes the chosen evaluation metric.

###### Note

Automatic model tuning for TabTransformer is only available from the Amazon SageMaker SDKs,
not from the SageMaker AI console.

For more information about model tuning, see [Automatic model tuning with SageMaker AI](automatic-model-tuning.md "automatic-model-tuning.md").

## Evaluation metrics computed by the TabTransformer

algorithm

The SageMaker AI TabTransformer algorithm computes the following metrics to use for model validation.
The evaluation metric is automatically assigned based on the type of classification task,
which is determined by the number of unique integers in the label column.

| Metric Name      | Description              | Optimization Direction | Regex Pattern                    |
| ---------------- | ------------------------ | ---------------------- | -------------------------------- |
| `r2`             | r square                 | maximize               | `"metrics={'r2': (\\S+)}"`       |
| `f1_score`       | binary cross entropy     | maximize               | `"metrics={'f1': (\\S+)}"`       |
| `accuracy_score` | multiclass cross entropy | maximize               | `"metrics={'accuracy': (\\S+)}"` |

## Tunable TabTransformer hyperparameters

Tune the TabTransformer model with the following hyperparameters. The
hyperparameters that have the greatest effect on optimizing the TabTransformer
evaluation metrics are: `learning_rate`, `input_dim`,
`n_blocks`, `attn_dropout`, `mlp_dropout`, and
`frac_shared_embed`. For a list of all the TabTransformer
hyperparameters, see [TabTransformer hyperparameters](tabtransformer-hyperparameters.md "tabtransformer-hyperparameters.md").

| Parameter Name      | Parameter Type             | Recommended Ranges                      |
| ------------------- | -------------------------- | --------------------------------------- |
| `learning_rate`     | ContinuousParameterRanges  | MinValue: 0.001, MaxValue: 0.01         |
| `input_dim`         | CategoricalParameterRanges | [`16`, `32`, `64`, `128`, `256`, `512`] |
| `n_blocks`          | IntegerParameterRanges     | MinValue: 1, MaxValue: 12               |
| `attn_dropout`      | ContinuousParameterRanges  | MinValue: 0.0, MaxValue: 0.8            |
| `mlp_dropout`       | ContinuousParameterRanges  | MinValue: 0.0, MaxValue: 0.8            |
| `frac_shared_embed` | ContinuousParameterRanges  | MinValue: 0.0, MaxValue: 0.5            |
