# Add a tag to a workspace

Adding tags to an Amazon Managed Service for Prometheus workspace can help you identify and organize your
AWS resources and manage access to them. First, you add one or more tags
(key-value pairs) to a workspace. After you have tags, you can create IAM policies
to manage access to the workspace based on these tags. You can use the the console
or the AWS CLI to add tags to an Amazon Managed Service for Prometheus workspace.

###### Important

Adding tags to a workspace can impact access to that workspace. Before you add
a tag to a workspace, make sure to review any IAM policies that might use tags
to control access to resources.

For more information about adding tags to an Amazon Managed Service for Prometheus workspace when you create
it, see [Create a Amazon Managed Service for Prometheus workspace](AMP-create-workspace.md "AMP-create-workspace.md").

###### Topics

- [Add a tag to a workspace
  (console)](#how-to-tag-workspace-add-console "#how-to-tag-workspace-add-console")
- [Add a tag to a workspace
  (AWS CLI)](#how-to-tag-workspace-add-cli "#how-to-tag-workspace-add-cli")

## Add a tag to a workspace

(console)

You can use the console to add one or more tags to a Amazon Managed Service for Prometheus workspace.

1. Open the Amazon Managed Service for Prometheus console at [https://console.aws.amazon.com/prometheus/](https://console.aws.amazon.com/prometheus/home "https://console.aws.amazon.com/prometheus/home").
2. In the navigation pane, choose the menu icon.
3. Choose **All workspaces**.
4. Choose the workspace ID of the workspace that you want to
   manage.
5. Choose the **Tags** tab.
6. If no tags have been added to the Amazon Managed Service for Prometheus workspace, choose
   **Create tag**. Otherwise, choose **Manage
   tags**.
7. In **Key**, enter a name for the tag. You can add an
   optional value for the tag in **Value**.
8. (Optional) To add another tag, choose **Add tag**
   again.
9. When you have finished adding tags, choose **Save
   changes**.

## Add a tag to a workspace

(AWS CLI)

Follow these steps to use the AWS CLI to add a tag to an Amazon Managed Service for Prometheus workspace. To
add a tag to a workspace when you create it, see [Create a Amazon Managed Service for Prometheus workspace](AMP-create-workspace.md "AMP-create-workspace.md").

In these steps, we assume that you have already installed a recent version of
the AWS CLI or updated to the current version. For more information, see [Installing the AWS Command Line Interface](../../../cli/latest/userguide/installing.md "../../../cli/latest/userguide/installing.md").

At the terminal or command line, run the **tag-resource**
command, specifying the Amazon Resource Name (ARN) of the workspace where you
want to add tags and the key and value of the tag you want to add. You can add
more than one tag to an workspace. For example, to tag an Amazon Managed Service for Prometheus workspace
named **My-Workspace** with two tags, a tag key named
`Status` with the tag value of
`Secret`, and a tag key named
`Team` with the tag value of
`My-Team`:

```
aws amp tag-resource --resource-arn arn:aws:aps:`us-west-2`:`123456789012`:workspaces/`IDstring`
--tags `Status`=`Secret`,`Team`=`My-Team`
```

If successful, this command returns nothing.
