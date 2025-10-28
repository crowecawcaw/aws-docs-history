# DeleteDataSource

Use the `DeleteDataSource` API operation to permanently delete a data source from Amazon Quick Sight. To use this operation, you need the ID of the data source that you want to delete. The data source ID is part of the data source URL in Quick Sight. You can also use the `ListDataSources` API operation to get the ID.

###### Note

Deleting a data source breaks all datasets that reference it.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight delete-data-source
    --aws-account-id `AWSACCOUNTID`
    --data-source-id `DATASOURCEID`
```

For more information about the `DeleteDataSource` API operation, see [DeleteDataSource](../APIReference/API_DeleteDataSource.md "../APIReference/API_DeleteDataSource.md") in the _Amazon Quick Sight API Reference_.
