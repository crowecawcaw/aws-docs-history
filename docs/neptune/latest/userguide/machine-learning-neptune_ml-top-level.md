

# Top-level elements in the neptune\_ml field in additionalParams
<a name="machine-learning-neptune_ml-top-level"></a>

## The version element in neptune\_ml
<a name="machine-learning-neptune_ml-version"></a>

Specifies the version of training data configuration to generate.

(*Optional*), *Type*: string, *Default*: "v2.0".

If you do include `version`, set it to `v2.0`.

## The jobs field in neptune\_ml
<a name="machine-learning-neptune_ml-jobs"></a>

Contains an array of training-data configuration objects, each of which defines a data processing job, and contains:
+ **`name`**   –   The name of the training data configuration to be created.

   For example, a training data configuration with the name "job-number-1" results in a training data configuration file named `job-number-1.json`.
+ **`targets`**   –   A JSON array of node and edge class label targets that represent the machine-learning class labels for training purposes. See [The targets field in a neptune\_ml object](machine-learning-neptune_ml-targets.md).
+ **`features`**   –   A JSON array of node property features. See [The features field in neptune\_ml](machine-learning-neptune_ml-features.md).