# Deleting resource groups from AWS Resource Groups

You can use the [AWS Resource Groups console](https://console.aws.amazon.com/resource-groups "https://console.aws.amazon.com/resource-groups") or the AWS CLI to delete resource groups from AWS Resource Groups.
Deleting a resource group does not delete the resources that are members of the group or
tags on member resources. It deletes only the group structure and any group-level
tags.

Console

###### To delete resource groups

1. Sign in to the [AWS Resource Groups console](https://console.aws.amazon.com/resource-groups "https://console.aws.amazon.com/resource-groups").
2. In the navigation pane, choose **[Saved Resource
   Groups](https://console.aws.amazon.com/resource-groups/groups "https://console.aws.amazon.com/resource-groups/groups")**.
3. Choose the name of the resource group that you want to delete, and then
   choose **View details**.
4. On the group's detail page, choose **Delete** in the top right corner.
5. When you are prompted to confirm the deletion, choose
   **Delete**.

AWS CLI & AWS SDKs

###### To delete resource groups

1. Run the following command, replacing
   `resource_group_name` with the name of your
   group.

```
`$` `aws resource-groups delete-group \
 --group-name `resource_group_name``
```

2. When you are prompted to confirm the deletion, type `yes`,
   and then press **Enter**.
