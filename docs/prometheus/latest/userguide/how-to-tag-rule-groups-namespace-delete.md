# Remove a tag from a rule

groups namespace

You can remove one or more tags associated with a rule groups namespace. Removing
a tag does not delete the tag from other AWS resources that are associated with
that tag.

###### Important

Removing tags for a resource can impact access to that resource. Before you
remove a tag from a resource, make sure to review any IAM policies that might
use the key or value for a tag to control access to resources such as
repositories.

## Remove a tag

from an Amazon Managed Service for Prometheus rule groups namespace (console)

You can use the console to remove the association between a tag and a rule
groups namespace.

1. Open the Amazon Managed Service for Prometheus console at [https://console.aws.amazon.com/prometheus/](https://console.aws.amazon.com/prometheus/home "https://console.aws.amazon.com/prometheus/home").
2. In the navigation pane, choose the menu icon.
3. Choose **All workspaces**.
4. Choose the workspace ID of the workspace that you want to
   manage.
5. Choose the **Rules management** tab.
6. Choose the name of the namespace.
7. Choose **Manage tags**.
8. Next to the tag you want to delete, choose
   **Remove**.
9. When you have finished, choose **Save
   changes**.

## Remove a tag from an

Amazon Managed Service for Prometheus rule groups namespace (AWS CLI)

Follow these steps to use the AWS CLI to remove a tag from an rule groups
namespace. Removing a tag does not delete it, but simply removes the association
between the tag and the rule groups namespace.

###### Note

If you delete an Amazon Managed Service for Prometheus rule groups namespace, all tag associations are
removed from the deleted nnamespace. You do not have to remove tags before
you delete a namespace.

At the terminal or command line, run the **untag-resource**
command, specifying the Amazon Resource Name (ARN) of the rule groups namespace
where you want to remove tags and the tag key of the tag you want to remove. For
example, to remove a tag on a workspace named **My-Workspace**
with the tag key `Status`:

```
aws amp untag-resource --resource-arn rn:aws:aps:`us-west-2`:`123456789012`:rulegroupsnamespace/`IDstring`/`namespace_name` --tag-keys `Status`
```

If successful, this command returns nothing. To verify the tags associated
with the resource, run the **list-tags-for-resource**
command.
