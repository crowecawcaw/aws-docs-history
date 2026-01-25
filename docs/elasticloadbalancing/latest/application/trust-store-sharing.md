# Share your Elastic Load Balancing trust store for Application Load Balancers

Elastic Load Balancing integrates with AWS Resource Access Manager (AWS RAM) to enable trust store sharing. AWS RAM is a service that enables you
to securely share your Elastic Load Balancing trust store resources across AWS accounts and within your organization or
organizational units (OUs). If you have multiple accounts, you can create a trust store once and use
AWS RAM to make it usable by other accounts. If your account is managed by AWS Organizations, you can share trust
stores with all the accounts in the organization or only accounts within specified organizational units
(OUs).

With AWS RAM, you share resources that you own by creating a _resource share_. A resource
share specifies the resources to share, and the consumers with whom to share them. In this model, the AWS account
that owns the trust store (owner) shares it with other AWS accounts (consumers). Consumers can associate
shared trust stores to their Application Load Balancer listeners in the same way they associate trust stores in their own account.

A trust store owner can share a trust store with:

- Specific AWS accounts inside or outside of its organization in AWS Organizations
- An organizational unit inside its organization in AWS Organizations
- Its entire organization in AWS Organizations

###### Contents

- [Prerequisites](#sharing-prereqs "#sharing-prereqs")
- [Permissions](#sharing-perms "#sharing-perms")
- [Share a trust store](#sharing-share "#sharing-share")
- [Stop sharing a trust store](#sharing-unshare "#sharing-unshare")
- [Billing and metering](#sharing-billing "#sharing-billing")

## Prerequisites for trust store sharing

- You must create a resource share using AWS Resource Access Manager. For more information, see [Create a resource share](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-create "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-create") in the _AWS RAM User Guide_.
- To share a trust store, you must own it in your AWS account. You cannot share
  a trust store that has been shared with you.
- To share a trust store with your organization or an organizational unit in
  AWS Organizations, you must enable sharing with AWS Organizations. For more information, see
  [Enable Sharing with AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the
  _AWS RAM User Guide_.

## Permissions for shared trust stores

### Trust store owners

- Trust store owners can create a trust store.
- Trust store owners can use a trust store with load balancers in the same account.
- Trust store owners can share a trust store with other AWS accounts or AWS Organizations.
- Trust store owners can unshare a trust store from any AWS account or AWS Organizations.
- Trust store owners cannot prevent load balancers from using a trust store in the same account .
- Trust store owners can list all Application Load Balancers using a shared trust store.
- Trust store owners can delete a trust store if there are no current associations.
- Trust store owners can delete associations with a shared trust store.
- Trust store owners receive CloudTrail logs when a shared trust store is used.

### Trust store consumers

- Trust store consumers can view shared trust stores.
- Trust store consumers can create or modify listeners using a trust store in the same account.
- Trust store consumers can create or modify listeners using a shared trust store.
- Trust store consumers cannot create a listener using a trust store that's no longer shared.
- Trust store consumers cannot modify a shared trust store.
- Trust store consumers can view a shared trust store ARN when associated to a listener.
- Trust store consumers receive CloudTrail logs when creating or modifying a listener using a shared trust store.

### Managed permissions

When sharing a trust store, the resource share uses managed permissions to control which actions
are allowed by the trust store consumer. You can use the default managed permissions
`AWSRAMPermissionElasticLoadBalancingTrustStore`, which includes all available
permissions, or create your own customer managed permissions. The `DescribeTrustStores`,
`DescribeTrustStoreRevocations`, and `DescribeTrustStoreAssociations`
permissions are always enabled and can not be removed.

The following permissions are supported for trust store resource shares:

**elasticloadbalancing:CreateListener**

Can attach a shared trust store to a new listener.

**elasticloadbalancing:ModifyListener**

Can attach a shared trust store to an existing listener.

**elasticloadbalancing:GetTrustStoreCaCertificatesBundle**

Can download the ca certificate bundle associated with the shared trust store.

**elasticloadbalancing:GetTrustStoreRevocationContent**

Can download the revocation file associated with the shared trust store.

**elasticloadbalancing:DescribeTrustStores (Default)**

Can list all trust stores owned and shared with the account.

**elasticloadbalancing:DescribeTrustStoreRevocations (Default)**

Can list all revocation content for the given trust store arn.

**elasticloadbalancing:DescribeTrustStoreAssociations (Default)**

Can list all resources in the trust store consumer account that are associated with the shared trust store.

## Share a trust store

To share a trust store, you must add it to a resource share. A resource share is an
AWS RAM resource that lets you share your resources across AWS accounts. A resource
share specifies the resources to share, the consumers with whom they are shared, and what
actions principals can perform. When you share a trust store using the Amazon EC2 console, you
add it to an existing resource share. To add the trust store to a new resource share, you
must first create the resource share using the [AWS RAM
console](https://console.aws.amazon.com/ram "https://console.aws.amazon.com/ram").

When you share a trust store that you own with other AWS accounts, you enable
those accounts to associate their Application Load Balancer listeners with trust stores in your account.

If you are part of an organization in AWS Organizations and sharing within your organization is
enabled, consumers in your organization are automatically granted access to the shared
trust store. Otherwise, consumers receive an invitation to join the resource share and
are granted access to the shared trust store after accepting the invitation.

You can share a trust store that you own using the Amazon EC2 console, AWS RAM console, or
the AWS CLI.

###### To share a trust store that you own using the Amazon EC2 console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose **Trust Stores**.
3. Select the trust store name to view its details page.
4. On the **Sharing** tab, choose **Share trust store**.
5. On the **Share trust store** page, under **Resource shares**, select which resource shares your trust store will be shared with.
6. (Optional) If you need to create a new resource share, select the **Create a resource share in RAM console** link.
7. Select **Share trust store**.

###### To share a trust store that you own using the AWS RAM console

See [Creating a Resource Share](../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-create "../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-create") in the
_AWS RAM User Guide_.

###### To share a trust store that you own using the AWS CLI

Use the [create-resource-share](../../../cli/latest/reference/ram/create-resource-share.md "../../../cli/latest/reference/ram/create-resource-share.md") command.

## Stop sharing a trust store

To stop sharing a trust store that you own, you must remove it from the
resource share. Existing associations persist after you stop sharing your trust store,
however new associations to a previously shared trust store are not allowed. When either
the trust store owner or the trust store consumer deletes an association, it is
deleted from both accounts. If a trust store consumer wants to leave a resource share,
they must ask the owner of the resource share to remove the account.

###### Deleting associations

Trust store owners can forcefully delete existing trust store associations using
the [DeleteTrustStoreAssociation](../APIReference/API_DeleteSharedTrustStoreAssociation.md "../APIReference/API_DeleteSharedTrustStoreAssociation.md") command. When an association
is deleted, any load balancer listeners using the trust store can no longer
verify client certificates and will fail TLS handshakes.

You can stop sharing a trust store using the Amazon EC2 console, AWS RAM console, or the AWS CLI.

###### To stop sharing a trust store that you own using the Amazon EC2 console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose **Trust Stores**.
3. Select the trust store name to view its details page.
4. On the **Sharing** tab, under **Resource sharing**, select the resource shares to stop sharing with.
5. Choose **Remove**.

###### To stop sharing a trust store that you own using the AWS RAM console

See [Updating a Resource Share](../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update "../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update") in the _AWS RAM User Guide_.

###### To stop sharing a trust store that you own using the AWS CLI

Use the [disassociate-resource-share](../../../cli/latest/reference/ram/disassociate-resource-share.md "../../../cli/latest/reference/ram/disassociate-resource-share.md") command.

## Billing and metering

Shared trust stores incur the same standard trust store rate, billed per hour, per trust store association with an Application Load Balancer.

For more information, including the specific rate per region, see [Elastic Load Balancing pricing](https://aws.amazon.com/elasticloadbalancing/pricing/ "https://aws.amazon.com/elasticloadbalancing/pricing/")
