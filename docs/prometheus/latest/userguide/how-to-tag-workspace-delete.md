# Remove a tag from a workspace

You can remove one or more tags associated with a workspace. Removing a tag does
not delete the tag from other AWS resources that are associated with that
tag.

###### Important

Removing tags for a Amazon Managed Service for Prometheus workspace can impact access to that workspace.
Before you remove a tag from a workspace, make sure to review any IAM policies
that might use the key or value for a tag to control access to resources such as
repositories.

## Remove a tag from an

Amazon Managed Service for Prometheus workspace (console)

You can use the console to remove the association between a tag and a
workspace.

1. Open the Amazon Managed Service for Prometheus console at [https://console.aws.amazon.com/prometheus/](https://console.aws.amazon.com/prometheus/home "https://console.aws.amazon.com/prometheus/home").
2. In the navigation pane, choose the menu icon.
3. Choose **All workspaces**.
4. Choose the workspace ID of the workspace that you want to
   manage.
5. Choose the **Tags** tab.
6. Choose **Manage tags**.
7. Find the tag that you want to delete, and choose
   **Remove**.

## Remove a tag from an Amazon Managed Service for Prometheus

workspace (AWS CLI)

Follow these steps to use the AWS CLI to remove a tag from an workspace.
Removing a tag does not delete it, but simply removes the association between
the tag and the workspace.

###### Note

If you delete an Amazon Managed Service for Prometheus workspace, all tag associations are removed
from the deleted workspace. You do not have to remove tags before you delete
a workspace.

At the terminal or command line, run the **untag-resource**
command, specifying the Amazon Resource Name (ARN) of the workspace where you
want to remove tags and the tag key of the tag you want to remove. For example,
to remove a tag on a workspace named **My-Workspace** with the
tag key `Status`:

```
aws amp untag-resource --resource-arn arn:aws:aps:`us-west-2`:`123456789012`:workspace/`IDstring` --tag-keys `Status`
```

If successful, this command returns nothing. To verify the tags associated
with the workspace, run the **list-tags-for-resource**
command.
