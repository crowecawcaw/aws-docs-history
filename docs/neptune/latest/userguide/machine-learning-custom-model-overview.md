# Overview of custom models in Neptune ML

## When to use a custom model

in Neptune ML

Neptune ML's built-in models handle all the standard tasks supported by Neptune ML,
but there may be cases where you want to have more granular control over the model for
a particular task, or need to customize the model training process. For example, a
custom model is appropriate in the following situations:

- Feature encoding for text features of very large text models need to
  be run on GPU.
- You want to use your own custom Graph Neural Network (GNN) model
  developed in Deep Graph Library (DGL).
- You want to use tabular models or ensemble models for node
  classification and regression.

## Workflow for developing

and using a custom model in Neptune ML

Custom model support in Neptune ML is designed to integrate seamlessly into
existing Neptune ML workflows. It works by running custom code in your source
module on Neptune ML's infrastructure to train the model. Just as is the case
for a built-in mode, Neptune ML automatically launches a SageMaker AI HyperParameter
tuning job and selects the best model according to the evaluation metric.
It then uses the implementation provided in your source module to generate model
artifacts for deployment.

Data export, training configuration, and data preprocessing is the same for
a custom model as for a built-in one.

After data preprocessing is when you can iteratively and interactively
develop and test your custom model implementation using Python. When your model
is production-ready, you can upload the resulting Python module to Amazon S3 like this:

```
aws s3 cp --recursive `(source path to module)` s3://`(bucket name)`/`(destination path for your module)`
```

Then, you can use the normal [default](machine-learning-overview.md#machine-learning-overview-starting-workflow "machine-learning-overview.md#machine-learning-overview-starting-workflow") or the [incremental](machine-learning-overview-evolving-data-incremental.md#machine-learning-overview-incremental "machine-learning-overview-evolving-data-incremental.md#machine-learning-overview-incremental") data workflow to
deploy the model to production, with a few differences.

For model training using a custom model, you must provide a
`customModelTrainingParameters` JSON object to the Neptune ML model
training API to ensure that your custom code is used. The fields in the
`customModelTrainingParameters` object are as follows:

- **`sourceS3DirectoryPath`**   –  
  (_Required_) The path to the Amazon S3 location where the Python module
  implementing your model is located. This must point to a valid existing Amazon S3 location
  that contains, at a minimum, a training script, a transform script, and a
  `model-hpo-configuration.json` file.
- **`trainingEntryPointScript`**   –  
  (_Optional_) The name of the entry point in your module of a script
  that performs model training and takes hyperparameters as command-line arguments,
  including fixed hyperparameters.

_Default_: `training.py`.

- **`transformEntryPointScript`**   –  
  (_Optional_) The name of the entry point in your module of a script
  that should be run after the best model from the hyperparameter search has been identified,
  to compute the model artifacts necessary for model deployment. It should be able to run
  with no command-line arguments.

_Default_: `transform.py`.

For example:

```
curl \
  -X POST https://`(your Neptune endpoint)`/ml/modeltraining
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "`(a unique model-training job ID)`",
        "dataProcessingJobId" : "`(the data-processing job-id of a completed job)`",
        "trainModelS3Location" : "s3://`(your Amazon S3 bucket)`/neptune-model-graph-autotrainer"
        "modelName": "custom",
        "customModelTrainingParameters" : {
          "sourceS3DirectoryPath": "s3://`(your Amazon S3 bucket)`/`(path to your Python module)`",
          "trainingEntryPointScript": "`(your training script entry-point name in the Python module)`",
          "transformEntryPointScript": "`(your transform script entry-point name in the Python module)`"
        }
      }'
```

Similarly, to enable a custom model transform, you must provide a `customModelTransformParameters`
JSON object to the Neptune ML model transform API, with field values that are compatible with
the saved model parameters from the training job. The `customModelTransformParameters`
object contains these fields:

- **`sourceS3DirectoryPath`**   –  
  (_Required_) The path to the Amazon S3 location where the Python module
  implementing your model is located. This must point to a valid existing Amazon S3 location
  that contains, at a minimum, a training script, a transform script, and a
  `model-hpo-configuration.json` file.
- **`transformEntryPointScript`**   –  
  (_Optional_) The name of the entry point in your module of a script
  that should be run after the best model from the hyperparameter search has been identified,
  to compute the model artifacts necessary for model deployment. It should be able to run
  with no command-line arguments.

_Default_: `transform.py`.

For example:

```
curl \
  -X POST https://`(your Neptune endpoint)`/ml/modeltransform
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "`(a unique model-training job ID)`",
        "trainingJobName" : "`(name of a completed SageMaker AI training job)`",
        "modelTransformOutputS3Location" : "s3://`(your Amazon S3 bucket)`/neptune-model-transform/"
        "customModelTransformParameters" : {
          "sourceS3DirectoryPath": "s3://`(your Amazon S3 bucket)`/`(path to your Python module)`",
          "transformEntryPointScript": "`(your transform script entry-point name in the Python module)`"
        }
      }'
```
