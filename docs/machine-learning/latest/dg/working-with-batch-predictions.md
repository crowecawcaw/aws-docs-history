We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Reviewing Batch Prediction Metrics

After Amazon Machine Learning (Amazon ML) creates a batch prediction, it provides two metrics: `Records
 seen` and `Records failed to process`. `Records seen` tells you
how many records Amazon ML looked at when it ran your batch prediction. `Records failed to
 process` tells you how many records Amazon ML could not process.

To allow Amazon ML to process failed records, check the formatting of the records in the data
used to create your datasource, and make sure that all of the required attributes are present
and all of the data is correct. After fixing your data, you can either recreate your batch
prediction, or create a new datasource with the failed records, and then create a new batch
prediction using the new datasource.

## Reviewing Batch Prediction Metrics (Console)

To see the metrics in the Amazon ML console, open the **Batch prediction
summary** page and look in the **Processed Info** section.

## Reviewing Batch Prediction Metrics and Details (API)

You can use the Amazon ML APIs to retrieve details about `BatchPrediction` objects,
including the record metrics. Amazon ML provides the following batch prediction API calls:

- `CreateBatchPrediction`
- `UpdateBatchPrediction`
- `DeleteBatchPrediction`
- `GetBatchPrediction`
- `DescribeBatchPredictions`

For more information, see the [Amazon ML API Reference](../APIReference.md "../APIReference.md").
