# DeleteDataSet

Use the `DeleteDataSet` API operation to delete a dataset. To use this operation, you need the ID of the dataset that you want to delete. The dataset ID is part of the dataset URL in Quick Sight. You can also use the `ListDataSets` API operation to get the ID.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight delete-data-set
    --aws-account-id `AWSACCOUNTID`
    --data-set-id `DATASETID`
```

For more information about the `DeleteDataSet` API operation, see [DeleteDataSet](../APIReference/API_DeleteDataSet.md "../APIReference/API_DeleteDataSet.md") in the _Amazon Quick Sight API Reference_.
