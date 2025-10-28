# Model training best practices

There are things you can do to improve the performance of Neptune ML models.

## Choose the right node property

Not all the properties in your graph may be meaningful or relevant to your
machine learning tasks. Any irrelevant properties should be excluded during data export.

Here are some best practices:

- Use domain experts to help evaluate the importance of features and
  the feasibility of using them for predictions.
- Remove the features that you determine are redundant or irrelevant
  to reduce noise in the data and unimportant correlations.
- Iterate as you build your model. Adjust the features, feature
  combinations, and tuning objectives as you go along.

[Feature Processing](../../../machine-learning/latest/dg/feature-processing.md "../../../machine-learning/latest/dg/feature-processing.md") in
the Amazon Machine Learning Developer Guide provides additional guidelines for feature processing that are
relevant to Neptune ML.

## Handle outlier data points

An outlier is a data point that is significantly different from the remaining
data. Data outliers can spoil or mislead the training process, resulting in
longer training time or less accurate models. Unless they are truly important,
you should eliminate outliers before exporting the data.

## Remove duplicate nodes and edges

Graphs stored in Neptune may have duplicate nodes or edges. These redundant
elements will introduce noise for ML model training. Eliminate duplicate
nodes or edges before exporting the data.

## Tune the graph structure

When the graph is exported, you can change the way features are processed and how the
graph is constructed, to improve the model performance.

Here are some best practices:

- When an edge property has the meaning of categories of edges, it is worth
  turning it into edge types in some cases.
- The default normalization policy used for a numerical property is
  `min-max`, but in some cases other normalization policies work better.
  You can preprocess the property and change the normalization policy as explained
  in [Elements of a model-HPO-configuration.json file](machine-learning-customizing-hyperparams.md#machine-learning-hyperparams-file-elements "machine-learning-customizing-hyperparams.md#machine-learning-hyperparams-file-elements").
- The export process automatically generates feature types based on
  property types. For example, it treats `String` properties as categorical
  features and `Float` and `Int` properties as numerical features.
  If you need to, you can modify the feature type after export (see [Elements of a model-HPO-configuration.json file](machine-learning-customizing-hyperparams.md#machine-learning-hyperparams-file-elements "machine-learning-customizing-hyperparams.md#machine-learning-hyperparams-file-elements")).

## Tune the hyperparameter ranges and defaults

The data-processing operation infers hyperparameter configuration ranges from the graph.
If the generated model hyperparameter ranges and defaults don't work well for your graph
data, you can edit the HPO configuration file to create your own hyperparameter
tuning strategy.

Here are some best practices:

- When the graph goes large, the default hidden dimension size may not be
  large enough to contain all the information. You can change the `num-hidden`
  hyperparameter to control the hidden dimension size.
- For knowledge graph embedding (KGE) models, you may want to change the
  specific model being used according to your graph structure and budget.

`TrainsE` models have difficulty in dealing with one-to-many
(1-N), many-to-one (N-1), and many-to-many (N-N) relations. `DistMult`
models have difficulty in dealing with symmetric relations. `RotatE`
is good at modeling all kinds of relations but is more expensive than
`TrainsE` and `DistMult` during training.

- In some cases, when both node identification and node
  feature information are important, you should use `concat-node-embed`
  to tell the Neptune ML model to get the initial representation of a
  node by concatenating its features with its initial embeddings.
- When you are getting reasonably good performance over some
  hyperparameters, you can adjust the hyperparameter search space according
  to those results.

## Early stopping of the model training process in Neptune ML

Early stopping can significantly reduce the model-training run time and associated
costs without degrading model performance. It also prevent the model from overfitting
on the training data.

Early stopping depends on regular measurements of validation-set performance. Initially,
performance improves as training proceeds, but when the model starts overfitting, it
starts to decline again. The early stopping feature identifies the point at which the model starts
overfitting and halts model training at that point.

Neptune ML monitors the validation metric calls and compares the most recent validation
metric to the average of validation metrics over the last **`n`**
evaluations, where **`n`** is a number set using the
`window-for-early-stop` parameter. As soon as the validation metric is worse than
that average, Neptune ML stops the model training and saves the best model so far.

You can control early stopping using the following parameters:

- **`window-for-early-stop`**   –  
  The value of this parameter is an integer that specifies the number of recent validation
  scores to average when deciding on an early stop. The default value is `3`.
- **`enable-early-stop`**   –  
  Use this Boolean parameter to turn off the early stop feature. By default, its value
  is `true`.

## Early stopping of the HPO process in Neptune ML

The early stop feature in Neptune ML also stops training jobs that are not
performing well compared to other training jobs, using the SageMaker AI HPO warm-start feature.
This too can reduce costs and improve the quality of HPO.

See [Run
a warm start hyperparameter tuning job](../../../sagemaker/latest/dg/automatic-model-tuning-warm-start.md "../../../sagemaker/latest/dg/automatic-model-tuning-warm-start.md") for a description of how this works.

Warm start provides the ability to pass information learned from previous training
jobs to subsequent training jobs and provides two distinct benefits:

- First, the results of previous training jobs are used to select good
  combinations of hyperparameters to search over in the new tuning job.
- Second, it allows early stopping to access more model runs, which reduces
  tuning time.

This feature is enabled automatically in Neptune ML, and allows you strike a balance
between model training time and performance. If you are satisfied with the performance of
the current model, you can use that model. Otherwise, you run more HPOs that are warm-started
with the results of previous runs so as to discover a better model.

## Get professional support services

AWS offers professional support services to help you with problems in your
machine learning on Neptune projects. If you get stuck, reach out to [AWS support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").
