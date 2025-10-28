# Edit tags for a rule

groups namespace

You can change the value for a tag associated with a rule groups namespace. You
can also change the name of the key, which is equivalent to removing the current tag
and adding a different one with the new name and the same value as the other key.

###### Important

Editing tags for an rule groups namespace can impact access to it. Before you
edit the name (key) or value of a tag for a resource, make sure to review any
IAM policies that might use the key or value for a tag to control access to
resources.

## Edit a tag for

an Amazon Managed Service for Prometheus rule groups namespace (console)

You can use the console to edit the tags associated with a Amazon Managed Service for Prometheus rule
groups namespace.

1. Open the Amazon Managed Service for Prometheus console at [https://console.aws.amazon.com/prometheus/](https://console.aws.amazon.com/prometheus/home "https://console.aws.amazon.com/prometheus/home").
2. In the navigation pane, choose the menu icon.
3. Choose **All workspaces**.
4. Choose the workspace ID of the workspace that you want to
   manage.
5. Choose the **Rules management** tab.
6. Choose the name of the namespace.
7. Choose **Manage tags**, **Add new
   tag**.
8. To change the value of an existing tag, enter the new value for
   **Value**.
9. o add an additional tag, choose **Add new
   tag**.
10. When you have finished adding and editing tags, choose **Save
    changes**.

## Edit tags for an

Amazon Managed Service for Prometheus rule groups namespace (AWS CLI)

Follow these steps to use the AWS CLI to update a tag for a rule groups
namespace. You can change the value for an existing key, or add another key.

At the terminal or command line, run the **tag-resource**
command, specifying the Amazon Resource Name (ARN) of the resource where you
want to update a tag and specify the tag key and tag value:

```
aws amp tag-resource --resource-arn rn:aws:aps:`us-west-2`:`123456789012`:rulegroupsnamespace/`IDstring`/`namespace_name` --tags `Team`=`New-Team`
```
