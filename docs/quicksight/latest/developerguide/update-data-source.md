

# UpdateDataSource
<a name="update-data-source"></a>

Use the `UpdateDataSource` API operation to update a data source. To use this operation, you need the ID of the data source that you want to update. The data source ID is part of the data source URL in Quick Sight. You can also use the `ListDataSources` API operation to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight update-data-source 
    --aws-account-id {{AWSACCOUNTID}} 
    --data-source-id {{DATASOURCEID}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight update-data-source 
    --cli-input-json file://{{updatedatasource}}.json
```

------

For more information about the `UpdateDataSource` API operation, see [UpdateDataSource](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDataSource.html) in the *Amazon Quick Sight API Reference*.