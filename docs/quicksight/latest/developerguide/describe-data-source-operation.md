

# DescribeDataSourcePermissions
<a name="describe-data-source-operation"></a>

Use the `DescribeDataSourcePermissions` API operation to describe the resource permissions for a data source. To use this operation, you need the ID of the data source whose permissions you want to view. The data source ID is part of the data source URL in Quick Sight. You can also use the `ListDataSources` API operation to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight describe-data-source-permissions 
    --aws-account-id {{AWSACCOUNTID}} 
    --data-source-id {{DATASOURCEID}}
```

------

For more information about the `DescribeDataSourcePermissions` API operation, see [DescribeDataSourcePermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeDataSourcePermissions.html) in the *Amazon Quick Sight API Reference*.