# Add a tag to a rule groups

namespace

Adding tags to an Amazon Managed Service for Prometheus rule groups namespaces can help you identify and
organize your AWS resources and manage access to them. First, you add one or more
tags (key-value pairs) to a rule groups namespace. After you have tags, you can
create IAM policies to manage access to the namespace based on these tags. You can
use the the console or the AWS CLI to add tags to an Amazon Managed Service for Prometheus rule groups namespace.

###### Important

Adding tags to a rule groups namespace can impact access to that rule groups
namespace. Before you add a tag, make sure to review any IAM policies that
might use tags to control access to resources.

For more information about adding tags to a rule groups namespace when you create
it, see [Create a rules file](AMP-ruler-rulesfile.md "AMP-ruler-rulesfile.md").

###### Topics

- [Add a tag to a
  rule groups namespace (console)](#how-to-tag-rule-groups-namespace-add-console "#how-to-tag-rule-groups-namespace-add-console")
- [Add a tag to a rule
  groups namespace (AWS CLI)](#how-to-tag-rule-groups-namespace-add-cli "#how-to-tag-rule-groups-namespace-add-cli")

## Add a tag to a

rule groups namespace (console)

You can use the console to add one or more tags to a Amazon Managed Service for Prometheus rule groups
namespace.

1. Open the Amazon Managed Service for Prometheus console at [https://console.aws.amazon.com/prometheus/](https://console.aws.amazon.com/prometheus/home "https://console.aws.amazon.com/prometheus/home").
2. In the navigation pane, choose the menu icon.
3. Choose **All workspaces**.
4. Choose the workspace ID of the workspace that you want to
   manage.
5. Choose the **Rules management** tab.
6. Choose the button next to the namespace name and choose
   **Edit**.
7. Choose **Create tags**, **Add new
   tag**.
8. In **Key**, enter a name for the tag. You can add an
   optional value for the tag in **Value**.
9. (Optional) To add another tag, choose **Add new tag**
   again.
10. When you have finished adding tags, choose **Save
    changes**.

## Add a tag to a rule

groups namespace (AWS CLI)

Follow these steps to use the AWS CLI to add a tag to an Amazon Managed Service for Prometheus rule groups
namespace. To add a tag to a rule groups namespace when you create it, see [Upload a rules configuration file to
Amazon Managed Service for Prometheus](AMP-rules-upload.md "AMP-rules-upload.md").

In these steps, we assume that you have already installed a recent version of
the AWS CLI or updated to the current version. For more information, see [Installing
the AWS Command Line Interface](../../../cli/latest/userguide/installing.md "../../../cli/latest/userguide/installing.md").

At the terminal or command line, run the **tag-resource**
command, specifying the Amazon Resource Name (ARN) of the rule groups namespace
where you want to add tags and the key and value of the tag you want to add. You
can add more than one tag to an rule groups namespace. For example, to tag an
Amazon Managed Service for Prometheus namespace named **My-Workspace** with two tags, a tag
key named `Status` with the tag value of
`Secret`, and a tag key named
`Team` with the tag value of
`My-Team`:

```
aws amp tag-resource \
    --resource-arn arn:aws:aps:`us-west-2`:`123456789012`:rulegroupsnamespace/`IDstring`/`namespace_name` \
    --tags `Status`=`Secret`,`Team`=`My-Team`
```

If successful, this command returns nothing.
