# Training a model using Neptune ML

After you have processed the data that you exported from Neptune for model training,
you can start a model-training job using a `curl` (or `awscurl`)
command like the following:

```
curl \
  -X POST https://`(your Neptune endpoint)`/ml/modeltraining
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "`(a unique model-training job ID)`",
        "dataProcessingJobId" : "`(the data-processing job-id of a completed job)`",
        "trainModelS3Location" : "s3://`(your Amazon S3 bucket)`/neptune-model-graph-autotrainer"
      }'
```

The details of how to use this command are explained in [The modeltraining command](machine-learning-api-modeltraining.md "machine-learning-api-modeltraining.md"),
along with information about how to get the status of a running job, how to stop a running job,
and how to list all running jobs.

You can also supply a `previousModelTrainingJobId` to use information from
a completed Neptune ML model training job to accelerate the hyperparameter search in a
new training job. This is useful during [model
retraining on new graph data](machine-learning-overview-evolving-data-incremental.md#machine-learning-overview-model-retraining "machine-learning-overview-evolving-data-incremental.md#machine-learning-overview-model-retraining"), as well as [incremental training on the same graph
data](machine-learning-overview-evolving-data-incremental.md#machine-learning-overview-incremental "machine-learning-overview-evolving-data-incremental.md#machine-learning-overview-incremental"). Use a command like this one:

```
curl \
  -X POST https://`(your Neptune endpoint)`/ml/modeltraining
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "`(a unique model-training job ID)`",
        "dataProcessingJobId" : "`(the data-processing job-id of a completed job)`",
        "trainModelS3Location" : "s3://`(your Amazon S3 bucket)`/neptune-model-graph-autotrainer"
        "previousModelTrainingJobId" : "`(the model-training job-id of a completed job)`"
      }'
```

You can train your own model implementation on the Neptune ML training infrastructure
by supplying a `customModelTrainingParameters` object, like this:

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

See [The modeltraining command](machine-learning-api-modeltraining.md "machine-learning-api-modeltraining.md") for more information, such as about how
to get the status of a running job, how to stop a running job, and how to list all running jobs. See
[Custom models in Neptune ML](machine-learning-custom-models.md "machine-learning-custom-models.md")
for information about how to implement and use a custom model.

###### Topics

- [Models and model training in Amazon Neptune ML](machine-learning-models-and-training.md "machine-learning-models-and-training.md")
- [Customizing model
  hyperparameter configurations in Neptune ML](machine-learning-customizing-hyperparams.md "machine-learning-customizing-hyperparams.md")
- [Model training best practices](machine-learning-improve-model-performance.md "machine-learning-improve-model-performance.md")
