# SearchGroups

Use the `SearchGroups` operation to search groups in a specified Quick Sight namespace using the supplied filters.

Following is an example AWS CLI command for this operation.

AWS CLI
CLI Input:

```
aws quicksight search-groups
    --region `us-west-2`
    --aws-account-id `AWSACCOUNTID`
    --namespace `default`
    --filters "[{\"`Operator`\": \"StringLike\", \"Name\": \"GROUP_NAME\", \"Value\": \"Mar\"}]"
```

For more information about the `SearchGroups` API operation, see [SearchGroups](../APIReference/API_SearchGroups.md "../APIReference/API_SearchGroups.md") in the _Amazon Quick Sight API Reference_.
