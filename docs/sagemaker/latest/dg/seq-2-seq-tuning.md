# Tune a Sequence-to-Sequence Model

_Automatic model tuning_, also known as
hyperparameter tuning, finds the best version of a model by running many jobs that test
a range of hyperparameters on your dataset. You choose the tunable hyperparameters, a
range of values for each, and an objective metric. You choose the objective metric from
the metrics that the algorithm computes. Automatic model tuning searches the
hyperparameters chosen to find the combination of values that result in the model that
optimizes the objective metric.

For more information about model tuning, see [Automatic model tuning with SageMaker AI](automatic-model-tuning.md "automatic-model-tuning.md").

## Metrics Computed by the Sequence-to-Sequence

Algorithm

The sequence to sequence algorithm reports three metrics that are computed during
training. Choose one of them as an objective to optimize when tuning the
hyperparameter values.

| Metric<br>Name          | Description                                                                                                                                                                                                                                                                                                                                                                                                                       | Optimization Direction |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| `validation:accuracy`   | Accuracy<br>computed on the validation dataset.                                                                                                                                                                                                                                                                                                                                                                                   | Maximize               |
| `validation:bleu`       | [Bleu﻿](https://en.wikipedia.org/wiki/BLEU "https://en.wikipedia.org/wiki/BLEU")<br>score computed on the validation dataset. Because BLEU<br>computation is expensive, you can choose to compute BLEU on a<br>random subsample of the validation dataset to speed up the<br>overall training process.<br>Use<br>the `bleu_sample_size` parameter to specify the<br>subsample.                                                    | Maximize               |
| `validation:perplexity` | [Perplexity](https://en.wikipedia.org/wiki/Perplexity "https://en.wikipedia.org/wiki/Perplexity"), is a loss function computed on the<br>validation dataset. Perplexity measures the cross-entropy<br>between an empirical sample and the distribution predicted by a<br>model and so provides a measure of how well a model predicts the<br>sample values, Models that are good at predicting a sample have<br>a low perplexity. | Minimize               |

## Tunable

Sequence-to-Sequence Hyperparameters

You can tune the following hyperparameters for the SageMaker AI Sequence to Sequence
algorithm. The hyperparameters that have the greatest impact on sequence to sequence
objective metrics are: `batch_size`, `optimizer_type`,
`learning_rate`, `num_layers_encoder`, and
`num_layers_decoder`.

| Parameter<br>Name             | Parameter<br>Type         | Recommended Ranges                                                                                       |
| ----------------------------- | ------------------------- | -------------------------------------------------------------------------------------------------------- |
| `num_layers_encoder`          | IntegerParameterRange     | [1-10]                                                                                                   |
| `num_layers_decoder`          | IntegerParameterRange     | [1-10]                                                                                                   |
| `batch_size`                  | CategoricalParameterRange | [16,32,64,128,256,512,1024,2048]                                                                         |
| `optimizer_type`              | CategoricalParameterRange | ['adam', 'sgd', 'rmsprop']                                                                               |
| `weight_init_type`            | CategoricalParameterRange | ['xavier',<br>'uniform']                                                                                 |
| `weight_init_scale`           | ContinuousParameterRange  | For the xavier type: MinValue: 2.0, MaxValue: 3.0 For the<br>uniform type: MinValue: -1.0, MaxValue: 1.0 |
| `learning_rate`               | ContinuousParameterRange  | MinValue: 0.00005, MaxValue: 0.2                                                                         |
| `weight_decay`                | ContinuousParameterRange  | MinValue: 0.0, MaxValue: 0.1                                                                             |
| `momentum`                    | ContinuousParameterRange  | MinValue: 0.5, MaxValue: 0.9                                                                             |
| `clip_gradient`               | ContinuousParameterRange  | MinValue: 1.0, MaxValue: 5.0                                                                             |
| `rnn_num_hidden`              | CategoricalParameterRange | Applicable<br>only to recurrent neural networks (RNNs).<br>[128,256,512,1024,2048]                       |
| `cnn_num_hidden`              | CategoricalParameterRange | Applicable<br>only to convolutional neural networks (CNNs).<br>[128,256,512,1024,2048]                   |
| `num_embed_source`            | IntegerParameterRange     | [256-512]                                                                                                |
| `num_embed_target`            | IntegerParameterRange     | [256-512]                                                                                                |
| `embed_dropout_source`        | ContinuousParameterRange  | MinValue: 0.0, MaxValue: 0.5                                                                             |
| `embed_dropout_target`        | ContinuousParameterRange  | MinValue: 0.0, MaxValue: 0.5                                                                             |
| `rnn_decoder_hidden_dropout`  | ContinuousParameterRange  | MinValue: 0.0, MaxValue: 0.5                                                                             |
| `cnn_hidden_dropout`          | ContinuousParameterRange  | MinValue: 0.0, MaxValue: 0.5                                                                             |
| `lr_scheduler_type`           | CategoricalParameterRange | ['plateau\_reduce',<br>'fixed\_rate\_inv\_t',<br>'fixed\_rate\_inv\_sqrt\_t']                            |
| `plateau_reduce_lr_factor`    | ContinuousParameterRange  | MinValue: 0.1, MaxValue: 0.5                                                                             |
| `plateau_reduce_lr_threshold` | IntegerParameterRange     | [1-5]                                                                                                    |
| `fixed_rate_lr_half_life`     | IntegerParameterRange     | [10-30]                                                                                                  |
