# UpdateDataSourcePermissions

Use the `UpdateDataSourcePermissions` API operation to update the resource permissions for a data source. You can grant or revoke permissions in the same command. To use this operation, you need the ID of the data source whose permissions you want to update. The data source ID is part of the data source URL in Quick Sight. You can also use the `ListDataSources` API operation to get the ID.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight update-data-source-permissions
    --aws-account-id `AWSACCOUNTID`
    --data-source-id `DATASOURCEID`
    --grant-permissions Principal=arn:aws:quicksight:`us-east-1`:`AWSACCOUNTID`:user/default/`USER`NAME``,Actions=quicksight:DescribeDataSource,quicksight:DescribeDataSourcePermissions,quicksight:PassDataSource
    --revoke-permissions Principal=arn:aws:quicksight:`us-east-1`:`AWSACCOUNTID`:user/default/`USER`NAME``,Actions=quicksight:DescribeDataSource,quicksight:DescribeDataSourcePermissions,quicksight:PassDataSource
```

If your `region` has already been configured within the CLI, it doesn't need to be included as an argument.

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight update-data-source-permissions
    --cli-input-json file://`updatedatasourcepermissions`.json
```

If your region has already been configured with the CLI, it does not need to be included in an argument.

For more information about the `UpdateDataSourcePermissions` API operation, see [UpdateDataSourcePermissions](../APIReference/API_UpdateDataSourcePermissions.md "../APIReference/API_UpdateDataSourcePermissions.md") in the _Amazon Quick Sight API Reference_.
