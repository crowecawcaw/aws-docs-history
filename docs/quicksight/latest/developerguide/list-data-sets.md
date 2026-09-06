

# ListDataSets
<a name="list-data-sets"></a>

Use the `ListDataSets` API operation to list all of the datasets that belong to a particular AWS account in an AWS Region. Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight list-data-sets 
    --aws-account-id {{AWSACCOUNTID}} 
    --page-size {{10}} 
    --max-items {{100}}
```

------

For more information about the `ListDataSets` API operation, see [ListDataSets](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListDataSets.html) in the *Amazon Quick Sight API Reference*.