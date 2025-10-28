# Processing the graph data exported from Neptune for training

The data-processing step takes the Neptune graph data created by the export process
and creates the information that is used by the [Deep
Graph Library (DGL)](https://www.dgl.ai/ "https://www.dgl.ai/") during training. This includes performing various data mappings
and transformations:

- Parsing nodes and edges to construct the graph- and ID-mapping files
  required by DGL.
- Converting node and edge properties into the node and edge features
  required by DGL.
- Splitting the data into training, validation, and test sets.

## Managing the data-processing step for Neptune ML

After you have exported the data from Neptune that you want to use for model training,
you can start a data-processing job using a `curl` (or `awscurl`)
command like the following:

```
curl \
  -X POST https://`(your Neptune endpoint)`/ml/dataprocessing \
  -H 'Content-Type: application/json' \
  -d '{
        "inputDataS3Location" : "s3://`(Amazon S3 bucket name)`/`(path to your input folder)`",
        "id" : "`(a job ID for the new job)`",
        "processedDataS3Location" : "s3://`(S3 bucket name)`/`(path to your output folder)`",
        "configFileName" : "training-job-configuration.json"
      }'
```

The details of how to use this command are explained in [The dataprocessing command](machine-learning-api-dataprocessing.md "machine-learning-api-dataprocessing.md"),
along with information about how to get the status of a running job, how to stop a running job,
and how to list all running jobs.

## Processing updated graph data for Neptune ML

You can also supply a `previousDataProcessingJobId` to the API to ensure
that the new data processing job uses the same processing method as a previous job.
This is required when you want to get predictions for updated graph data in Neptune,
either by retraining the old model on the new data, or by recomputing the model artifacts
on the new data.

You do this by using a `curl` (or `awscurl`) command like this:

```
curl \
  -X POST https://`(your Neptune endpoint)`/ml/dataprocessing \
  -H 'Content-Type: application/json' \
  -d '{ "inputDataS3Location" : "s3://`(Amazon S3 bucket name)`/`(path to your input folder)`",
        "id" : "`(a job ID for the new job)`",
        "processedDataS3Location" : "s3://`(Amazon S3 bucket name)`/`(path to your output folder)`",
        "previousDataProcessingJobId", "`(the job ID of the previous data-processing job)`"}'
```

Set the value of the `previousDataProcessingJobId` parameter to the
job ID of the previous-data processing job that corresponds to the trained model.

###### Note

Node deletions in the updated graph are currently not supported.
If nodes have been removed in an updated graph, you have to start a completely
new data processing job rather than use `previousDataProcessingJobId`.
