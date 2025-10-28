# Customizing model

hyperparameter configurations in Neptune ML

When you start a Neptune ML model-training job, Neptune ML automatically uses
the information inferred from the preceding [data-processing](machine-learning-on-graphs-processing.md "machine-learning-on-graphs-processing.md") job. It uses the
information to generate hyperparameter configuration ranges that are used to create a [SageMaker AI hyperparameter tuning
job](../../../sagemaker/latest/dg/automatic-model-tuning-how-it-works.md "../../../sagemaker/latest/dg/automatic-model-tuning-how-it-works.md") to train multiple models for your task. That way, you don’t have to specify
a long list of hyperparameter values for the models to be trained with. Instead, the model
hyperparameter ranges and defaults are selected based on the task type, graph type,
and the tuning-job settings.

However, you can also override the default hyperparameter configuration and provide
custom hyperparameters by modifying a JSON configuration file that the data-processing
job generates.

Using the Neptune ML [modelTraining
API](machine-learning-api-modeltraining.md "machine-learning-api-modeltraining.md"), you can control several high level hyperparameter tuning job settings like
`maxHPONumberOfTrainingJobs`, `maxHPOParallelTrainingJobs`, and
`trainingInstanceType`. For more fine-grained control over the model
hyperparameters, you can customize the `model-HPO-configuration.json` file
that the data-processing job generates. The file is saved in the Amazon S3 location that
you specified for processing-job output.

You can download the file, edit it to override the default hyperparameter
configurations, and upload it back to the same Amazon S3 location. Do not change the
name of the file, and be careful to follow these instructions as you edit.

To download the file from Amazon S3:

```
aws s3 cp \
  s3://`(bucket name)`/`(path to output folder)`/model-HPO-configuration.json \
  ./
```

When you have finished editing, upload the file back to where it was:

```
aws s3 cp \
  model-HPO-configuration.json \
  s3://`(bucket name)`/`(path to output folder)`/model-HPO-configuration.json
```

## Structure of the `model-HPO-configuration.json` file

The `model-HPO-configuration.json` file specifies the model to be trained,
the machine learning `task_type` and the hyperparameters that should be varied
or fixed for the various runs of model training.

The hyperparameters are categorized as belonging to various tiers that signify the
precedence given to the hyperparameters when the hyperparameter tuning job is invoked:

- Tier-1 hyperparameters have the highest precedence. If you set
  `maxHPONumberOfTrainingJobs` to a value less than 10, only Tier-1
  hyperparameters are tuned, and the rest take their default values.
- Tier-2 hyperparameters have lower precedence, so if you have
  more than 10 but less than 50 total training jobs for a tuning job, then both
  Tier-1 and Tier-2 hyperparameters are tuned.
- Tier 3 hyperparameters are tuned together with Tier-1 and Tier-2
  only if you have more than 50 total training jobs.
- Finally, fixed hyperparameters are not tuned at all,
  and always take their default values.

### Example of a `model-HPO-configuration.json` file

The following is a sample `model-HPO-configuration.json` file:

```
{
  "models": [
    {
      "model": "rgcn",
      "task_type": "node_class",
      "eval_metric": {
        "metric": "acc"
      },
      "eval_frequency": {
          "type":  "evaluate_every_epoch",
          "value":  1
      },
      "1-tier-param": [
        {
            "param": "num-hidden",
            "range": [16, 128],
            "type": "int",
            "inc_strategy": "power2"
        },
        {
          "param": "num-epochs",
          "range": [3,30],
          "inc_strategy": "linear",
          "inc_val": 1,
          "type": "int",
          "node_strategy": "perM"
        },
        {
          "param": "lr",
          "range": [0.001,0.01],
          "type": "float",
          "inc_strategy": "log"
        }
      ],
      "2-tier-param": [
        {
          "param": "dropout",
          "range": [0.0,0.5],
          "inc_strategy": "linear",
          "type": "float",
          "default": 0.3
        },
        {
          "param": "layer-norm",
          "type": "bool",
          "default": true
        }
      ],
      "3-tier-param": [
        {
          "param": "batch-size",
          "range": [128, 4096],
          "inc_strategy": "power2",
          "type": "int",
          "default": 1024
        },
        {
          "param": "fanout",
          "type": "int",
          "options": [[10, 30],[15, 30], [15, 30]],
          "default": [10, 15, 15]
        },
        {
          "param": "num-layer",
          "range": [1, 3],
          "inc_strategy": "linear",
          "inc_val": 1,
          "type": "int",
          "default": 2
        },
        {
          "param": "num-bases",
          "range": [0, 8],
          "inc_strategy": "linear",
          "inc_val": 2,
          "type": "int",
          "default": 0
        }
      ],
      "fixed-param": [
        {
          "param": "concat-node-embed",
          "type": "bool",
          "default": true
        },
        {
          "param": "use-self-loop",
          "type": "bool",
          "default": true
        },
        {
          "param": "low-mem",
          "type": "bool",
          "default": true
        },
        {
          "param": "l2norm",
          "type": "float",
          "default": 0
        }
      ]
    }
  ]
}

```

### Elements of a `model-HPO-configuration.json` file

The file contains a JSON object with a single top-level array named `models`
that contains a single model-configuration object. When customizing the file, make sure
the `models` array only has one model-configuration object in it. If your file
contains more than one model-configuration object, the tuning job will fail with a warning.

The model-configuration object contains the following top-level elements:

- **`model`**   –  
  (_String_) The model type to be trained (**do not modify**). Valid values are:

      + `"rgcn"`   –  
       This is the default for node classification and regression tasks, and for
       heterogeneous link prediction tasks.
      + `"transe"`   –  
       This is the default for KGE link prediction tasks.
      + `"distmult"`   –  
       This is an alternative model type for KGE link prediction tasks.
      + `"rotate"`   –  
       This is an alternative model type for KGE link prediction tasks.

  As a rule, don't directly modify the `model` value,
  because different model types often have substantially different
  applicable hyperparameters, which can result in a parsing error
  after the training job has started.

To change the model type, use the `modelName` parameter
in the [modelTraining
API](machine-learning-api-modeltraining.md#machine-learning-api-modeltraining-create-job "machine-learning-api-modeltraining.md#machine-learning-api-modeltraining-create-job") rather than change it in the `model-HPO-configuration.json`
file.

A way to change the model type and make fine-grain hyperparameter changes
is to copy the default model configuration template for the model that you want
to use and paste that into the `model-HPO-configuration.json` file.
There is a folder named `hpo-configuration-templates` in the same
Amazon S3 location as the `model-HPO-configuration.json` file if the
inferred task type supports multiple models. This folder contains all the
default hyperparameter configurations for the other models that are applicable
to the task.

For example, if you want to change the model and hyperparameter configurations
for a `KGE` link-prediction task from the default `transe`
model to a `distmult` model, simply paste the contents of the
`hpo-configuration-templates/distmult.json` file into the
`model-HPO-configuration.json` file and then edit the
hyperparameters as necessary.

###### Note

If you set the `modelName` parameter in the
`modelTraining` API and also change the `model` and hyperparameter
specification in the `model-HPO-configuration.json` file, and
these are different, the `model` value in the
`model-HPO-configuration.json` file takes precedence, and the
`modelName` value is ignored.

- **`task_type`**   –  
  (_String_) The machine learning task type inferred by
  or passed directly to the data-processing job (**do
  not modify**). Valid values are:

      + `"node_class"`
      + `"node_regression"`
      + `"link_prediction"`

  The data-processing job infers the task type by examining the exported
  dataset and the generated training-job configuration file for properties of
  the dataset.

This value should not be changed. If you want to train a different task,
you need to [run a new
data-processing job](machine-learning-on-graphs-processing.md "machine-learning-on-graphs-processing.md"). If the `task_type` value
is not what you were expecting, you should check the inputs to your data-processing
job to make sure that they are correct. This includes parameters to the
`modelTraining` API, as well as in the training-job configuration
file generated by the data-export process.

- **`eval_metric`**   –  
  (_String_) The evaluation metric should be used for
  evaluating the model performance and for selecting the best-performing
  model across HPO runs. Valid values are:

      + `"acc"`   –  
       Standard classification accuracy. This is the default for single-label
       classification tasks, unless imbalanced labels are found during data
       processing, in which case the default is `"F1"`.
      + `"acc_topk"`   –  
       The number of times the correct label is among the top **`k`** predictions. You can also set the value
       **`k`** by passing in `topk`
       as an extra key.
      + `"F1"`   –  
       The [F1 score](https://en.wikipedia.org/wiki/F-score "https://en.wikipedia.org/wiki/F-score").
      + `"mse"`   –  
       [Mean-squared
       error metric](https://en.wikipedia.org/wiki/Mean_squared_error "https://en.wikipedia.org/wiki/Mean_squared_error"), for regression tasks.
      + `"mrr"`   –  
       [Mean
       reciprocal rank metric](https://en.wikipedia.org/wiki/Mean_reciprocal_rank "https://en.wikipedia.org/wiki/Mean_reciprocal_rank").
      + `"precision"`   –  
       The model precision, calculated as the ratio of true positives to
       predicted positives: `= true-positives / (true-positives + false-positives)`.
      + `"recall"`   –  
       The model recall, calculated as the ratio of true positives to actual positives:
       `= true-positives / (true-positives + false-negatives)`.
      + `"roc_auc"`   –  
       The area under the [ROC
       curve](https://en.wikipedia.org/wiki/Receiver_operating_characteristic "https://en.wikipedia.org/wiki/Receiver_operating_characteristic"). This is the default for multi-label classification.

  For example, to change the metric to `F1`, change the
  `eval_metric` value as follows:

```
"  eval_metric": {
    "metric": "F1",
  },
```

Or, to change the metric to a `topk` accuracy score, you would
change `eval_metric` as follows:

```
  "eval_metric": {
    "metric": "acc_topk",
    "topk": 2
  },
```

- **`eval_frequency`**   –  
  (_Object_) Specifies how often during training the performance
  of the model on the validation set should be checked. Based on the validation
  performance, early stopping can then be initiated and the best model can be saved.

The `eval_frequency` object contains two elements, namely `"type"`
and `"value"`. For example:

```
  "eval_frequency": {
    "type":  "evaluate_every_pct",
    "value":  0.1
  },
```

Valid `type` values are:

    + **`evaluate_every_pct`**   –  
     Specifies the percentage of training to be completed for each evaluation.


    For `evaluate_every_pct`, the `"value"` field contains
     a floating-point number between zero and one which expresses that percentage.
    + **`evaluate_every_batch`**   –  
     Specifies the number of training batches to be completed for each evaluation.


    For `evaluate_every_batch`, the `"value"` field contains an integer
     which expresses that batch count.
    + **`evaluate_every_epoch`**   –  
     Specifies the number of epochs per evaluation, where a new epoch starts at midnight.


    For `evaluate_every_epoch`, the `"value"` field contains an integer
     which expresses that epoch count.

The default setting for `eval_frequency` is:

```
  "eval_frequency": {
    "type":  "evaluate_every_epoch",
    "value":  1
  },
```

- **`1-tier-param`**   –  
  (_Required_) An array of Tier-1 hyperparameters.

If you don't want to tune any hyperparameters, you can set this to an
empty array. This does not affect the total number of training jobs launched by
the SageMaker AI hyperparameter tuning job. It just means that all training jobs,
if there is more than 1 but less than 10, will run with the same set of
hyperparameters.

On the other hand, if you want to treat all your tunable hyperparameters
with equal significance then you can put all the hyperparameters in this array.

- **`2-tier-param`**   –  
  (_Required_) An array of Tier-2 hyperparameters.

These parameters are only tuned if `maxHPONumberOfTrainingJobs`
has a value greater than 10. Otherwise, they are fixed to the default values.

If you have a training budget of at most 10 training jobs or don't want
Tier-2 hyperparameters for any other reason, but you want to tune all tunable
hyperparameters, you can set this to an empty array.

- **`3-tier-param`**   –  
  (_Required_) An array of Tier-3 hyperparameters.

These parameters are only tuned if `maxHPONumberOfTrainingJobs`
has a value greater than 50. Otherwise, they are fixed to the default values.

If you don't want Tier-3 hyperparameters, you can set this to an empty array.

- **`fixed-param`**   –  
  (_Required_) An array of fixed hyperparameters that
  take only their default values and do not vary in different training jobs.

If you want to vary all hyperparameters, you can set this to an empty
array and either set the value for `maxHPONumberOfTrainingJobs`
large enough to vary all tiers or make all hyperparameters Tier-1.

The JSON object that represents each hyperparameter in `1-tier-param`,
`2-tier-param`, `3-tier-param`, and `fixed-param`
contains the following elements:

- **`param`**   –  
  (_String_) The name of the hyperparameter (**do not change**).

See the [list of valid
hyperparameter names in Neptune ML](#machine-learning-hyperparams-list "#machine-learning-hyperparams-list").

- **`type`**   –  
  (_String_) The hyperparameter type (**do not change**).

Valid types are: `bool`, `int`, and `float`.

- **`default`**   –  
  (_String_) The default value for the hyperparameter.

You can set a new default value.

Tunable hyperparameters can also contain the following elements:

- **`range`**   –  
  (_Array_) The range for a continuous tunable hyperparameter.

This should be an array with two values, namely the minimum and maximum
of the range (`[min, max]`).

- **`options`**   –  
  (_Array_) The options for a categorical tunable hyperparameter.

This array should contain all the options to consider:

```
  "options" : [value1, value2, ... valuen]
```

- **`inc_strategy`**   –  
  (_String_) The type of incremental change for continuous
  tunable hyperparameter ranges (**do not change**).

Valid values are `log`, `linear`, and `power2`.
This applies only when the range key is set.

Modifying this may result in not using the full range of your hyperparameter
for tuning.

- **`inc_val`**   –  
  (_Float_) The amount by which successive increments differ
  for continuous tunablehyperparameters (**do not change**).

This applies only when the range key is set.

Modifying this may result in not using the full range of your hyperparameter
for tuning.

- **`node_strategy`**   –  
  (_String_) Indicates that the effective range for this
  hyperparameter should change based on the number of nodes in the graph
  (**do not change**).

Valid values are `"perM"` (per million), `"per10M"` (per
10 million), and `"per100M"` (per 100 million).

Rather than change this value, change the `range` instead.

- **`edge_strategy`**   –  
  (_String_) Indicates that the effective range for this
  hyperparameter should change based on the number of edges in the graph (**do not change**).

Valid values are `"perM"` (per million), `"per10M"` (per
10 million), and `"per100M"` (per 100 million).

Rather than change this value, change the `range` instead.

### List of all the hyperparameters in Neptune ML

The following list contains all the hyperparameters that can be set anywhere in
Neptune ML, for any model type and task. Because they are not all applicable to
every model type, it is important that you only set hyperparameters in
the `model-HPO-configuration.json` file that appear in the template for
the model you're using.

- **`batch-size`**   –  
  The size of the batch of target nodes using in one forward pass.
  _Type_: `int`.

Setting this to a much larger value can cause memory issues for
training on GPU instances.

- **`concat-node-embed`**   –  
  Indicates whether to get the initial representation of a node by concatenating its
  processed features with learnable initial node embeddings in order to increase
  the expressivity of the model.
  _Type_: `bool`.
- **`dropout`**   –  
  The dropout probability applied to dropout layers.
  _Type_: `float`.
- **`edge-num-hidden`**   –  
  The hidden layer size or number of units for the edge feature module.
  Only used when `use-edge-features` is set to `True`.
  _Type_: float.
- **`enable-early-stop`**   –  
  Toggles whether or not to use the early stopping feature.
  _Type_: `bool`.
  _Default_: `true`.

Use this Boolean parameter to turn off the early stop feature.

- **`fanout`**   –  
  The number of neighbors to sample for a target node during neighbor sampling.
  _Type_: `int`.

This value is tightly coupled with `num-layers` and
should always be in the same hyperparameter tier. This is because you can
specify a fanout for each potential GNN layer.

Because this hyperparameter can cause model performance to vary
widely, it should be fixed or set as a Tier-2 or Tier-3 hyperparameter.
Setting it to a large value can cause memory issues for training on
GPU instance.

- **`gamma`**   –  
  The margin value in the score function.
  _Type_: `float`.

This applies to `KGE` link-prediction models only.

- **`l2norm`**   –  
  The weight decay value used in the optimizer which imposes an L2 normalization
  penalty on the weights.
  _Type_: `bool`.
- **`layer-norm`**   –  
  Indicates whether to use layer normalization for `rgcn` models.
  _Type_: `bool`.
- **`low-mem`**   –  
  Indicates whether to use a low-memory implementation of the relation
  message passing function at the expense of speed.
  _Type_: `bool`.
- **`lr`**   –  
  The learning rate. _Type_: `float`.

This should be set as a Tier-1 hyperparameter.

- **`neg-share`**   –  
  In link prediction, indicates whether positive sampled edges can share
  negative edge samples. _Type_: `bool`.
- **`num-bases`**   –  
  The number of bases for basis decomposition in a `rgcn` model.
  Using a value of `num-bases` that is less than the number of edge types
  in the graph acts as a regularizer for the `rgcn` model.
  _Type_: `int`.
- **`num-epochs`**   –  
  The number of epochs of training to run.
  _Type_: `int`.

An epoch is a complete training pass through the graph.

- **`num-hidden`**   –  
  The hidden layer size or number of units.
  _Type_: `int`.

This also sets the initial embedding size for featureless nodes.

Setting this to a much larger value without reducing `batch-size`
can cause out-of-memory issues for training on GPU instance.

- **`num-layer`**   –  
  The number of GNN layers in the model.
  _Type_: `int`.

This value is tightly coupled with the fanout parameter and should come after
fanout is set in the same hyperparameter tier.

Because this can cause model performance to vary widely, it should be fixed
or set as a Tier-2 or Tier-3 hyperparameter.

- **`num-negs`**   –  
  In link prediction, the number of negative samples per positive sample.
  _Type_: `int`.
- **`per-feat-name-embed`**   –  
  Indicates whether to embed each feature by independently transforming it
  before combining features. _Type_: `bool`.

When set to `true`, each feature per node is independently
transformed to a fixed dimension size before all the transformed features
for the node are concatenated and further transformed to the `num_hidden`
dimension.

When set to `false`, the features are concatenated without
any feature-specific transformations.

- **`regularization-coef`**   –  
  In link prediction, the coefficient of regularization loss.
  _Type_: `float`.
- **`rel-part`**   –  
  Indicates whether to use relation partition for `KGE` link prediction.
  _Type_: `bool`.
- **`sparse-lr`**   –  
  The learning rate for learnable-node embeddings. _Type_:
  `float`.

Learnable initial node embeddings are used for nodes without features or
when `concat-node-embed` is set. The parameters of the sparse
learnable node embedding layer are trained using a separate optimizer
which can have a separate learning rate.

- **`use-class-weight`**   –  
  Indicates whether to apply class weights for imbalanced classification tasks.
  If set to to `true`, the label counts are used to set a weight
  for each class label. _Type_: `bool`.
- **`use-edge-features`**   –  
  Indicates whether to use edge features during message passing. If set to
  `true`, a custom edge feature module is added to the RGCN layer
  for edge types that have features. _Type_: `bool`.
- **`use-self-loop`**   –  
  Indicates whether to include self loops in training a `rgcn` model.
  _Type_: `bool`.
- **`window-for-early-stop`**   –  
  Controls the number of latest validation scores to average to decide on an early
  stop. The default is 3. type=int. See also [Early stopping of the model training process in Neptune ML](machine-learning-improve-model-performance.md#machine-learning-model-training-early-stop "machine-learning-improve-model-performance.md#machine-learning-model-training-early-stop").
  _Type_: `int`. _Default_: `3`.

See .

## Customizing hyperparameters in Neptune ML

When you are editing the `model-HPO-configuration.json` file, the
following are the most common kinds of changes to make:

- Edit the minimum and/or maximum values of `range` hyperparameters.
- Set a hyperparameter to a fixed value by moving it to the
  `fixed-param` section and setting its default value to the fixed value
  you want it to take.
- Change the priority of a hyperparameter by placing it in
  a particular tier, editing its range, and making sure that its default
  value is set appropriately.
