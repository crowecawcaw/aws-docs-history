# Tag Amazon Managed Grafana workspaces

Use the procedures in this section to work with tags for Amazon Managed Grafana workspaces.

###### Topics

Adding tags (key-value pairs) to an Amazon Managed Grafana workspace can help you identify
and organize your AWS resources. First, you add one or more tags to a
workspace, then you can create IAM policies to manage access to the workspace
based on these tags. You can use the console or the AWS CLI to add tags to an
Amazon Managed Grafana workspace.

###### Important

Adding tags to a workspace can impact access to that workspace. Before you
add a tag to a workspace, make sure to review any IAM policies that might
use tags to control access to resources.

For more information about adding tags to an Amazon Managed Grafana workspace when you
create it, see [Create an Amazon Managed Grafana workspace](AMG-create-workspace.md "AMG-create-workspace.md") in Amazon Managed Grafana User Guide.

Console
You can use the console to add one or more tags to an
Amazon Managed Grafana workspace.

1. Open the Amazon Managed Grafana console at [https://console.aws.amazon.com/grafana/](https://console.aws.amazon.com/grafana/ "https://console.aws.amazon.com/grafana/").
2. In the navigation pane on the left, choose the menu
   icon.
3. Choose **All workspaces**.
4. Choose the workspace ID of the workspace that you want to
   manage.
5. Choose the **Tags** tab.
6. Choose **Manage tags**.
7. In the **Key** field, enter a name for
   the tag. You can add an optional value for the tag in the
   **Value** field.
8. (Optional) To add another tag, choose **Add
   tag**.
9. When you have finished adding tags, choose **Save
   changes**.

CLI
Follow these steps to use the AWS CLI to add one or more
tags to an Amazon Managed Grafana workspace:

- At the terminal or command line, run the
  `tag-resource` command, specifying the Amazon
  Resource Name (ARN) of the workspace where you want to add
  tags to and the key and the value of the tag you want to
  add. You can add more than one tag to a workspace. For
  example, to tag the Grafana workspace
  `My-Workspace` with a tag key
  named `Name` with the tag value of
  `my_key_value`, run the
  following command:

```
aws grafana tag-resource --resource-arn arn:aws:grafana:`us-west-2`:`123456789012`:/workspace/`My-Workspace` --tags "`Name`=`my_key_value`"
```

You can view the tags associated with a Amazon Managed Grafana workspace. For more
information about tagging strategies, see [Tagging AWS resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md") in
AWS General Reference.

Console
You can use the console to view the tags associated with an
Amazon Managed Grafana workspace.

1. Open the Amazon Managed Grafana console at [https://console.aws.amazon.com/grafana/](https://console.aws.amazon.com/grafana/ "https://console.aws.amazon.com/grafana/").
2. In the navigation pane on the left, choose the menu
   icon.
3. Choose **All workspaces**.
4. Choose the workspace ID of the workspace that you want to
   manage.
5. Choose the **Tags** tab.

CLI
Follow these steps to use the AWS CLI to view the AWS tags for
an Amazon Managed Grafana workspace. If no tags have been added, the
returned list is empty.

At the terminal or command line, run the
**list-tags-for-resource** command. For
example, to view a list of tag keys and tag values for a workspace,
run the following command:

```
aws grafana list-tags-for-resource --resoure-arn arn:aws:grafana:`us-west-2`:/workspace/`workspace-IDstring`
```

If successful, this command returns information similar to the
following:

```
{
    "tags": {
        "Status": "Secret",
        "Team": "My-Team"
    }
}
```

You can change the value of a tag associated with a workspace in a single call
using `TagResource` API. To update the key of an existing tag, you
must combine the `UntagResource` and `TagResource`
APIs.

###### Important

Editing tags for an Amazon Managed Grafana workspace can impact access to that
workspace. Before you edit a tag for a workspace, make sure to review any
IAM policies that might use the key or value of a tag to control access to
resources such as repositories.

Console
You can use the console to edit the tags associated with Amazon Managed Grafana
workspace.

1. Open the Amazon Managed Grafana console at [Grafana Console](https://console.aws.amazon.com/grafana/ "https://console.aws.amazon.com/grafana/").
2. In the navigation pane on the left, choose the menu
   icon.
3. Choose **All workspaces**.
4. Choose the workspace ID of the workspace that you want to
   manage.
5. Choose the **Tags** tab.
6. Choose **Manage tags**.
7. In the **Key** field, enter a name for
   the tag. You can add an optional value for the tag in the
   **value** field.
8. When you have finished editing tags, choose **Save
   changes**.

CLI
Follow these steps to use the AWS CLI to update a tag for a
workspace. You can change the value of an existing key, or add
another key.

At the terminal or command line, run the
**tag-resource** command, specifying the Amazon
Resource Name (ARN) of the Amazon Managed Grafana workspace where you want to
update a tag and specify the tag key and tag value.

For example, to change a tag's value with a new value,
`Key_value_new`, run the following
command.

```
aws grafana tag-resource \
    --resource-arn arn:aws:grafana:`us-west-2`:`123456789012`:/workspace/`workspace-IDstring` \
    --tags "`Name`=`Key_value_new`"
```

To change a tag's key with a new name,
`Name_new`, run the following commands:

```
aws grafana untag-resource --resource-arn arn:aws:grafana:`us-west-2`:`123456789012`:/workspace/`workspace-IDstring` --tag-keys Items=`Name`
aws grafana tag-resource --resource-arn arn:aws:grafana:`us-west-2`:`123456789012`:/workspace/`workspace-IDstring` --tags "`Name_new`=`Key_value_old`"
```

You can remove one or more tags associated with a workspace. Removing a tag
does not delete the tag from other AWS resources that are associated with that
tag.

###### Important

Removing tags from an Amazon Managed Grafana workspace can impact access to that
workspace. Before you remove a tag from a workspace, make sure to review any
IAM policies that might use the key or value of a tag to control access to
resources such as workspaces.

Console
You can use the console to remove the association between a tag
and a workspace.

1. Open the Amazon Managed Grafana console at [Grafana Console](https://console.aws.amazon.com/grafana/ "https://console.aws.amazon.com/grafana/").
2. In the navigation pane on the left, choose the menu
   icon.
3. Choose **All workspaces**.
4. Choose the workspace ID of the workspace that you want to
   manage.
5. Choose the **Tags** tab.
6. Choose **Manage tags**.
7. Find the tag you want to delete, and choose
   **Remove**.
8. When you have finished removing tags, choose
   **Save changes**.

CLI
Follow these steps to use the AWS CLI to remove a tag from a
workspace. Removing a tag does not delete the tag from other
resources, but it simply removes the association between the tag and
the workspace.

###### Note

If you delete an Amazon Managed Grafana workspace, all tag associations are
removed from the deleted workspace. You do not have to remove
tags before you delete a workspace.

At the terminal or command line, run the
**untag-resource** command, specifying the
Amazon Resource Name (ARN) of the workspace where you want to remove
tags and the tag key of the tag you want to remove. For example, to
remove a tag on a workspace named
`workspace-IDstring` with the tag key
`Name`, run the following command:

```
aws grafana untag-resource --resoure-arn arn:aws:grafana:`us-west-2`:/workspaces/`workspace-IDstring` --tag-keys Items=`Name`
```

If successful, this command returns an empty response. To verify
that the tags associated with the workspace have been removed, run
the **list-tags-for-resource** command.
