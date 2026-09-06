

# DescribeGroup
<a name="describe-group"></a>

Use the `DescribeGroup` API operation to view an Amazon Quick Sight group's description and Amazon Resource Name (ARN). You can find a group name by calling the `ListGroups` API operation.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight describe-group 
    --group-name {{GROUPNAME}} 
    --aws-account-id {{AWSACCOUNTID}} 
    --namespace {{default}}
```

------

For more information about the `DescribeGroup` API operation, see [DescribeGroup](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeGroup.html) in the *Amazon Quick Sight API Reference*.