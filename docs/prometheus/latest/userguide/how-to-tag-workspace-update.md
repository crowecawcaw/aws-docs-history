# Edit tags for a workspace

You can change the value for a tag associated with a workspace. You can also
change the name of the key, which is equivalent to removing the current tag and
adding a different one with the new name and the same value as the other key.

###### Important

Editing tags for an Amazon Managed Service for Prometheus workspace can impact access to that workspace.
Before you edit the name (key) or value of a tag for a workspace, make sure to
review any IAM policies that might use the key or value for a tag to control
access to resources such as repositories.

## Edit a tag for an

Amazon Managed Service for Prometheus workspace (console)

You can use the console to edit the tags associated with a Amazon Managed Service for Prometheus
workspace.

1. Open the Amazon Managed Service for Prometheus console at [https://console.aws.amazon.com/prometheus/](https://console.aws.amazon.com/prometheus/home "https://console.aws.amazon.com/prometheus/home").
2. In the navigation pane, choose the menu icon.
3. Choose **All workspaces**.
4. Choose the workspace ID of the workspace that you want to
   manage.
5. Choose the **Tags** tab.
6. If no tags have been added to the workspace, choose **Create
   tag**. Otherwise, choose **Manage
   tags**.
7. In **Key**, enter a name for the tag. You can add an
   optional value for the tag in **Value**.
8. (Optional) To add another tag, choose **Add tag**
   again.
9. When you have finished adding tags, choose **Save
   changes**.

## Edit tags for an Amazon Managed Service for Prometheus

workspace (AWS CLI)

Follow these steps to use the AWS CLI to update a tag for a workspace. You can
change the value for an existing key, or add another key.

At the terminal or command line, run the **tag-resource**
command, specifying the Amazon Resource Name (ARN) of the Amazon Managed Service for Prometheus workspace
where you want to update a tag and specify the tag key and tag value:

```
aws amp tag-resource --resource-arn arn:aws:aps:`us-west-2`:`123456789012`:workspace/`IDstring` --tags `Team`=`New-Team`
```
