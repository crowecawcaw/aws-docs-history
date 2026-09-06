

# DeleteDataSource
<a name="delete-data-source"></a>

Use the `DeleteDataSource` API operation to permanently delete a data source from Amazon Quick Sight. To use this operation, you need the ID of the data source that you want to delete. The data source ID is part of the data source URL in Quick Sight. You can also use the `ListDataSources` API operation to get the ID.

**Note**  
Deleting a data source breaks all datasets that reference it.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight delete-data-source 
    --aws-account-id {{AWSACCOUNTID}} 
    --data-source-id {{DATASOURCEID}}
```

------

For more information about the `DeleteDataSource` API operation, see [DeleteDataSource](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteDataSource.html) in the *Amazon Quick Sight API Reference*.