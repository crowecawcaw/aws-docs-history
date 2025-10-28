# DescribeDataSource

Use the `DescribeDataSource` API operation to describe a data source. To use this operation, you need the ID of the data source that you want to view. The data source ID is part of the data source URL in Quick Sight. You can also use the `ListDataSources` API operation to get the ID.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight describe-data-source
    --aws-account-id `AWSACCOUNTID`
    --data-source-id `DATASOURCEID`
```

For more information about the `DescribeDataSource` API operation, see [DescribeDataSource](../APIReference/API_DescribeDataSource.md "../APIReference/API_DescribeDataSource.md") in the _Amazon Quick Sight API Reference_.
