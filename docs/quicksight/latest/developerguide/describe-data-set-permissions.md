# DescribeDataSetPermissions

Use the `DescribeDataSetPermissions` API operation to describe the
permissions on a dataset. To use this operation, you need the ID of the dataset
whose permissions that you want to view. The dataset ID is part of the dataset URL
in Quick Sight. You can also use the `ListDataSets` API operation to get the ID.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight describe-data-set-permissions
    --aws-account-id `AWSACCOUNTID`
    --data-set-id `DATASETID`
```

For more information about the `DescribeDataSetPermissions` API operation, see [DescribeDataSetPermissions](../APIReference/API_DescribeDataSetPermissions.md "../APIReference/API_DescribeDataSetPermissions.md") in the _Amazon Quick Sight API Reference_.
