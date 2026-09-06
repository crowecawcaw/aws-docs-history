

# View tags for a workspace
<a name="how-to-tag-workspace-list"></a>

Tags can help you identify and organize your AWS resources and manage access to them. For more information about tagging strategies, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).

## View tags for an Amazon Managed Service for Prometheus workspace (console)
<a name="how-to-tag-workspace-list-console"></a>

You can use the console to view the tags associated with a Amazon Managed Service for Prometheus workspace. 

1. Open the Amazon Managed Service for Prometheus console at [https://console.aws.amazon.com/prometheus/](https://console.aws.amazon.com/prometheus/home).

1. In the navigation pane, choose the menu icon.

1. Choose **All workspaces**.

1. Choose the workspace ID of the workspace that you want to manage.

1. Choose the **Tags** tab.

## View tags for an Amazon Managed Service for Prometheus workspace (AWS CLI)
<a name="how-to-tag-workspace-list-cli"></a>

Follow these steps to use the AWS CLI to view the AWS tags for an workspace. If no tags have been added, the returned list is empty.

At the terminal or command line, run the **list-tags-for-resource** command. For example, to view a list of tag keys and tag values for a workspace:

```
aws amp list-tags-for-resource --resource-arn arn:aws:aps:{{us-west-2}}:{{123456789012}}:workspace/{{IDstring}}
```

If successful, this command returns information similar to the following:

```
{
    "tags": {
        "Status": "Secret",
        "Team": "My-Team"
    }
}
```