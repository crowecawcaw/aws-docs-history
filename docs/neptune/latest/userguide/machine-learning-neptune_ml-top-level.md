# Top-level elements in the

neptune_ml field in additionalParams

## The version element in neptune_ml

Specifies the version of training data configuration to generate.

(_Optional_), _Type_: string,
_Default_: "v2.0".

If you do include `version`, set it to `v2.0`.

## The jobs field in neptune_ml

Contains an array of training-data configuration objects, each of which
defines a data processing job, and contains:

- **`name`**   –  
  The name of the training data configuration to be created.

For example, a training data configuration with the name "job-number-1"
results in a training data configuration file named `job-number-1.json`.

- **`targets`**   –  
  A JSON array of node and edge class label targets that represent the
  machine-learning class labels for training purposes. See [The targets field in
  a neptune_ml object](machine-learning-neptune_ml-targets.md "machine-learning-neptune_ml-targets.md").
- **`features`**   –  
  A JSON array of node property features. See [The features field
  in neptune_ml](machine-learning-neptune_ml-features.md "machine-learning-neptune_ml-features.md").
