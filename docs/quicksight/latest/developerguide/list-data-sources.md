

# ListDataSources
<a name="list-data-sources"></a>

Use the `ListDataSources` API operation to list all data sources in the current AWS Region that belong to a particular AWS account. Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight list-data-sources 
    --aws-account-id {{AWSACCOUNTID}} 
    --page-size {{10}} 
    --max-items {{100}}
```

------

For more information about the `ListDataSources` API operation, see [ListDataSources](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListDataSources.html) in the *Amazon Quick Sight API Reference*.