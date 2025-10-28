# UpdateDataSetPermissions

Use the `UpdateDataSetPermissions` API operation to update the
permissions on a dataset. You can grant or revoke permissions in the same command.
To use this operation, you need the ID of the dataset whose permissions that you
want to update. The dataset ID is part of the dataset URL in Quick Sight. You can also
use the `ListDataSets` API operation to get the ID.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight update-data-set-permissions
    --aws-account-id `AWSACCOUNTID`
    --data-set-id `DATASETID`
    --grant-permissions Principal=arn:aws:quicksight:`us-east-1`:`AWSACCOUNTID`:user/default/`USERNAME`,Actions=quicksight:DescribeDataSet,quicksight:DescribeDataSetPermissions,quicksight:PassDataSet,quicksight:DescribeIngestion,quicksight:ListIngestions
    --revoke-permissions Principal=arn:aws:quicksight:`us-east-1`:`AWSACCOUNTID`:user/default/`USERNAME`,Actions=quicksight:DescribeDataSet,quicksight:DescribeDataSetPermissions,quicksight:PassDataSet,quicksight:DescribeIngestion,quicksight:ListIngestions
```

If your `region` has already been configured with the CLI, it
doesn't need to be included as an argument.

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight update-data-set-permissions
    --cli-input-json file://`updatedatasetpermissions`.json
```

If your region has already been configured with the CLI, it does not need to be included in an argument.

For more information about the `UpdateDataSetPermissions` API operation, see [UpdateDataSetPermissions](../APIReference/API_UpdateDataSetPermissions.md "../APIReference/API_UpdateDataSetPermissions.md") in the _Amazon Quick Sight API Reference_.
