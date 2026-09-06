

# DescribeDataSet
<a name="describe-data-set"></a>

Use the `DescribeDataSet` API operation to describe a dataset. To use this operation, you need the ID of the dataset that you want to describe. The dataset ID is part of the dataset URL in Quick Sight. You can also use the `ListDataSets` API operation to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight describe-data-set 
    --aws-account-id {{AWSACCOUNTID}} 
    --data-set-id {{DATASETID}}
```

------

For more information about the `DescribeDataSet` API operation, see [DescribeDataSet](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeDataSet.html) in the *Amazon Quick Sight API Reference*.