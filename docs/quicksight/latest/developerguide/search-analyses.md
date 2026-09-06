

# SearchAnalyses
<a name="search-analyses"></a>

Use the `SearchAnalyses` API operation to search for analyses that belong to the specified user. Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight search-analyses 
    --aws-account-id {{555555555555}} 
    --filters Operator={{StringEquals}},Name={{QUICKSIGHT_USER}},Value=arn:aws:quicksight:{{us-east-1}}:{{555555555555}}:user/default/{{USERNAME}} 
    --page-size {{10}} 
    --max-items {{100}}
```

If your `region` has already been configured within the CLI, it doesn't need to be included as an argument.

------

If your region has already been configured with the CLI, it does not need to be included in an argument.

For more information about the `SearchAnalyses` API operation, see [SearchAnalyses](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SearchAnalyses.html) in the *Amazon Quick Sight API Reference*.