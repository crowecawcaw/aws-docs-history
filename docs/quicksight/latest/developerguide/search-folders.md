

# SearchFolders
<a name="search-folders"></a>

Use the `SearchFolders` operation to search the subfolders of a folder. 

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight search-folders 
    --aws-account-id {{AWSACCOUNTID}} 
    --filters Operator={{StringEquals}},Name={{QUICKSIGHT_USER}},Value=arn:aws:quicksight:{{us-east-1}}:{{AWSACCOUNTID}}:user/default/{{USER{{NAME}}}} 
    --max-results {{100}}
```

If your `region` has already been configured within the CLI, it doesn't need to be included as an argument.

------

If your region has already been configured with the CLI, it does not need to be included in an argument.

For more information on the SearchFolders operation, see [SearchFolders](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SearchFolders.html) in the * Quick Sight API Reference*.