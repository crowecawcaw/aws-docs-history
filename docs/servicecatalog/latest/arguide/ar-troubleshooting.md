# Troubleshooting in AppRegistry

If you encounter issues when working with AppRegistry, consult the topics in this section.

###### Topics

- [How to I resolve a resource tagging error for my application
  resources?](#resource-error-tagging-status "#resource-error-tagging-status")

## How to I resolve a resource tagging error for my application

resources?

When a resource can't be successfully tagged or untagged with the `awsApplication` tag, the
resource appears in the **Resource tagging error status** list. This list displays
any resources that encountered tagging errors in the last 85 days, with a **Tag status** of
**Error**.

Resource tagging errors can include any valid error code returned by the AWS service that hosts the resource that you want to tag.
Common errors include the following:

- **You do not have permissions to tag or untag this resource** — Tagging and
  untagging resources requires specific permissions. Review [Required
  permissions for Resource Groups and Toolkit for Eclipse](../../../ARG/latest/userguide/gettingstarted-prereqs-permissions.md#gettingstarted-prereqs-permissions-te "../../../ARG/latest/userguide/gettingstarted-prereqs-permissions.md#gettingstarted-prereqs-permissions-te") for more information about using AWS managed policies or manually adding
  the necessary permissions to tag and untag resources.
- **You can't add a global resource to an application** —
  Not all global resources can be tagged or untagged from any AWS Region. Some global resources,
  such as [Global Networks](../../../network-manager/latest/tgwnm/what-are-global-networks.md "../../../network-manager/latest/tgwnm/what-are-global-networks.md"),
  must be tagged from a specific region only, usually the Home Region. You can [Learn more about the differences
  between Regional and global resources](../../../ram/latest/userguide/working-with-regional-vs-global.md#regional-resources "../../../ram/latest/userguide/working-with-regional-vs-global.md#regional-resources") in the _AWS Resource Access Manager User Guide_.
