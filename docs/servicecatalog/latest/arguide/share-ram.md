# Using AWS Resource Access Manager to share resources

AppRegistry integrates with AWS Resource Access Manager (AWS RAM) to enable resource sharing. AWS RAM is a
service that enables you to share AppRegistry applications and attribute groups with
other
AWS accounts
or through AWS Organizations.

With AWS RAM you share resources that you own by creating a resource share. A
resource share specifies the resources to share, and the consumers with whom to
share them. Consumers can include:

- Specific
  AWS accounts
  inside or outside of its organization in AWS Organizations
- An organizational unit inside its organization in AWS Organizations
- Its entire organization in AWS Organizations
  For more information about AWS RAM, see the [AWS RAM User
  Guide](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md").

###### Topics

- [Prerequisites for sharing applications and
  attributes](#preq-sharing-ram "#preq-sharing-ram")
- [Sharing and unsharing applications or
  attribute groups](#share-unshare-ram "#share-unshare-ram")

## Prerequisites for sharing applications and

attributes

These are the prerequisites to share applications and attributes:

- You must own the application or attribute group in your
  AWS account.
  This means that the resource must be provisioned in your account. You
  cannot share an application or attribute group that has been shared with
  you.
- You must have access to [AWS Organizations](../../../organizations/latest/userguide/orgs_reference_available-policies.md "../../../organizations/latest/userguide/orgs_reference_available-policies.md")
  and [AWS RAM](../../../ram/latest/userguide/security-iam-managed-policies.md "../../../ram/latest/userguide/security-iam-managed-policies.md").
- You must enable sharing with AWS Organizations. For more information, see
  [Enable Sharing with AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the _AWS RAM User Guide_.

## Sharing and unsharing applications or

attribute groups

This section describes how to share or unshare an AppRegistry application or
attribute group with AWS RAM.

When you share an application or attribute group using the AppRegistry console, you
create a resource share. A resource share is an AWS RAM resource that lets you
share your resources across
AWS accounts.
It specifies the resources to share, and the consumers with whom they are
shared.

You can share an application or attribute group that you own using the AppRegistry
console, AWS RAM console, or the AWS CLI.

- To share an application or attribute group that you own using the
  AppRegistry console, you can either share an application or attribute group
  when you create it in the AppRegistry console, or you can access **Shares** for the specific application or
  attribute group you want to share.

- To share an application or attribute group that you own using the
  AWS RAM console, see [Creating a Resource
  Share](../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-create "../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-create")
  in the _AWS RAM User
  Guide_.
- To share an application or attribute group that you own using the
  AWS CLI, use the [create-resource-share](../../../cli/latest/reference/ram/create-resource-share.md "../../../cli/latest/reference/ram/create-resource-share.md")
  command. For more information, see [AWS Resource Access Manager API Reference](../../../cli/latest/reference/ram/index.md "../../../cli/latest/reference/ram/index.md").

To unshare a shared application or attribute group that you own, you must
remove it from the resource share. You can do unshare using the AppRegistry
console, AWS RAM console, or AWS CLI.

- To unshare a shared application or attribute group using the AppRegistry console, choose the application or attribute
  group from **Applications** or **Attribute Groups**. Then select **Shares**, and choose **Delete** for that application or attribute group.
- To unshare a shared an application or attribute group that you own
  using the AWS RAM console, see [Updating a Resource Share](../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update "../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update") in the _AWS RAM User Guide_.
- To unshare a shared an application or attribute group that you own
  using the AWS CLI, use the
  [disassociate-resource-share](../../../cli/latest/reference/ram/disassociate-resource-share.md "../../../cli/latest/reference/ram/disassociate-resource-share.md")
  command. For more information, see [AWS Resource Access Manager API Reference](../../../cli/latest/reference/ram/index.md "../../../cli/latest/reference/ram/index.md").
