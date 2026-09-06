

# SearchGroups
<a name="search-groups"></a>

Use the `SearchGroups` operation to search groups in a specified Quick Sight namespace using the supplied filters.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

CLI Input:

```
aws quicksight search-groups 
    --region {{us-west-2}} 
    --aws-account-id {{AWSACCOUNTID}} 
    --namespace {{default}} 
    --filters "[{\"{{Operator}}\": \"StringLike\", \"Name\": \"GROUP_NAME\", \"Value\": \"Mar\"}]"
```

------

For more information about the `SearchGroups` API operation, see [SearchGroups](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SearchGroups.html) in the *Amazon Quick Sight API Reference*.