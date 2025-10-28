# CancelIngestion

Use the `CancelIngestion` operation to cancel an ongoing ingestion of
data into SPICE.

To use this operation, you need the ID of the dataset that is undergoing the ingestion
that you want to cancel and the ID of the ingestion you want to cancel. You can use the
`ListDataSets` operation to list all datasets and their corresponding
dataset IDs. You can use the `ListIngestions` operation to list all ingestion
IDs.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight cancel-ingestion
    --aws-account-id `AWSACCOUNTID`
    --data-set-id `DATASETID`
    --ingestion-id `INGESTIONID`
```

For more information about the `CancelIngestion` operation, see [CancelIngestion](../APIReference/API_CancelIngestion.md "../APIReference/API_CancelIngestion.md") in the _Quick Sight API Reference_.
