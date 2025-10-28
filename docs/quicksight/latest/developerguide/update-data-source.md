# UpdateDataSource

Use the `UpdateDataSource` API operation to update a data source. To use this operation, you need the ID of the data source that you want to update. The data source ID is part of the data source URL in Quick Sight. You can also use the `ListDataSources` API operation to get the ID.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight update-data-source
    --aws-account-id `AWSACCOUNTID`
    --data-source-id `DATASOURCEID`
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight update-data-source
    --cli-input-json file://`updatedatasource`.json
```

For more information about the `UpdateDataSource` API operation, see [UpdateDataSource](../APIReference/API_UpdateDataSource.md "../APIReference/API_UpdateDataSource.md") in the _Amazon Quick Sight API Reference_.
