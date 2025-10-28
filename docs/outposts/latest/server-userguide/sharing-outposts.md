# Share your AWS Outposts resources

With Outpost sharing, Outpost owners can share their Outposts and Outpost resources,
including Outpost sites and subnets, with other AWS accounts under the same AWS
organization. As an Outpost owner, you can create and manage Outpost resources centrally, and
share the resources across multiple AWS accounts within your AWS organization. This allows
other consumers to use Outpost sites, configure VPCs, and launch and run instances on the shared
Outpost.

In this model, the AWS account that owns the Outpost resources
(_owner_) shares the resources with other AWS accounts
(_consumers_) in the same organization. Consumers can create resources on
Outposts that are shared with them in the same way that they would create resources on Outposts
that they create in their own account. The owner is responsible for managing the Outpost and
resources that they create in it. Owners can change or revoke shared access at any time. With
the exception of instances that consume Capacity Reservations, owners can also view, modify, and
delete resources that consumers create on shared Outposts. Owners can't modify instances that
consumers launch into Capacity Reservations that they have shared.

Consumers are responsible for managing the resources that they create on Outposts that are
shared with them, including any resources that consume Capacity Reservations. Consumers can't
view or modify resources owned by other consumers or by the Outpost owner. They also can't
modify Outposts that are shared with them.

An Outpost owner can share Outpost resources with:

- Specific AWS accounts inside of its organization in AWS Organizations.
- An organizational unit inside of its organization in AWS Organizations.
- Its entire organization in AWS Organizations.

###### Contents

- [Shareable Outpost resources](#sharing-resources "#sharing-resources")
- [Prerequisites for sharing Outposts resources](#sharing-prereqs "#sharing-prereqs")
- [Related services](#sharing-related "#sharing-related")
- [Sharing across Availability Zones](#sharing-azs "#sharing-azs")
- [Sharing an Outpost resource](#sharing-share "#sharing-share")
- [Unsharing a shared Outpost resource](#sharing-unshare "#sharing-unshare")
- [Identifying a shared Outpost resource](#sharing-identify "#sharing-identify")
- [Shared Outpost resource permissions](#sharing-perms "#sharing-perms")
- [Billing and metering](#sharing-billing "#sharing-billing")
- [Limitations](#sharing-quotas "#sharing-quotas")

## Shareable Outpost resources

An Outpost owner can share the Outpost resources listed in this section with
consumers.

For Outposts server resources, see [Working with shared AWS Outposts resources](sharing-outposts.md "sharing-outposts.md").

These are the resources available for Outposts servers. For Outposts rack
resources, see [Working with
shared AWS Outposts resources](../userguide/sharing-outposts.md "../userguide/sharing-outposts.md") in the AWS Outposts User Guide for Outposts racks.

- Allocated Dedicated Hosts – Consumers with
  access to this resource can:
  - Launch and run EC2 instances on a Dedicated Host.

- Outposts – Consumers with access to this
  resource can:
  - Create and manage subnets on the Outpost.
  - Use the AWS Outposts API to view information about the Outpost.

- Sites – Consumers with access to this resource
  can:
  - Create, manage, and control an Outpost at the site.

- Subnets – Consumers with access to this resource
  can:

      + View information about subnets.
      + Launch and run EC2 instances in subnets.

  Use the Amazon VPC console to share an Outpost subnet. For more information, see [Sharing a
  subnet](../../../vpc/latest/userguide/vpc-sharing.md#vpc-sharing-share-subnet "../../../vpc/latest/userguide/vpc-sharing.md#vpc-sharing-share-subnet") in the _Amazon VPC User Guide_.

## Prerequisites for sharing Outposts resources

- To share an Outpost resource with your organization or an organizational unit in
  AWS Organizations, you must enable sharing with AWS Organizations. For more information, see [Enable Sharing with AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the _AWS RAM User Guide_.
- To share an Outpost resource, you must own it in your AWS account. You can't share
  an Outpost resource that has been shared with you.
- To share an Outpost resource, you must share it with an account that is within your
  organization.

## Related services

Outpost resource sharing integrates with AWS Resource Access Manager (AWS RAM). AWS RAM is a service that
enables you to share your AWS resources with any AWS account or through AWS Organizations. With
AWS RAM, you share resources that you own by creating a _resource share_. A
resource share specifies the resources to share, and the consumers with whom to share them.
Consumers can be individual AWS accounts, organizational units, or an entire organization in
AWS Organizations.

For more information about AWS RAM, see the _[AWS RAM User Guide](../../../ram/latest/userguide.md "../../../ram/latest/userguide.md")_.

## Sharing across Availability Zones

To ensure that resources are distributed across the Availability Zones for a Region, we
independently map Availability Zones to names for each account. This could lead to
Availability Zone naming differences across accounts. For example, the Availability Zone
`us-east-1a` for your AWS account might not have the same location as
`us-east-1a` for another AWS account.

To identify the location of your Outpost resource relative to your accounts, you must use
the _Availability Zone ID_ (AZ ID). The AZ ID is a unique and consistent
identifier for an Availability Zone across all AWS accounts. For example,
`use1-az1` is an AZ ID for the `us-east-1` Region and it is the same
location in every AWS account.

###### To view the IDs for the Availability Zones in your account

1. Navigate to the [AWS RAM console](https://console.aws.amazon.com/ram/home#home: "https://console.aws.amazon.com/ram/home#home:") in the AWS RAM console.
2. The AZ IDs for the current Region are displayed in the **Your AZ ID**
   panel on the right-hand side of the screen.

###### Note

Local gateway route tables are in the same AZ as their Outpost, so you do not need to
specify an AZ ID for route tables.

## Sharing an Outpost resource

When an owner shares an Outpost with a consumer, the consumer can create resources on the
Outpost in the same way that they would create resources on Outposts that they create in their
own account. Consumers with access to shared local gateway route tables can create and manage
VPC associations. For more information, see [Shareable Outpost resources](#sharing-resources "#sharing-resources").

To share an Outpost resource, you must add it to a resource share. A resource share is an
AWS RAM resource that lets you share your resources across AWS accounts. A resource share
specifies the resources to share, and the consumers with whom they are shared. When you share
an Outpost resource using the AWS Outposts console, you add it to an existing resource share. To
add the Outpost resource to a new resource share, you must first create the resource share
using the [AWS RAM console](https://console.aws.amazon.com/ram "https://console.aws.amazon.com/ram").

If you are part of an organization in AWS Organizations and sharing within your organization is
enabled, you can grant consumers in your organization access from the AWS RAM console to the
shared Outpost resource. Otherwise, consumers receive an invitation to join the resource share
and are granted access to the shared Outpost resource after accepting the invitation.

You can share an Outpost resource that you own using the AWS Outposts console, AWS RAM console, or
the AWS CLI.

###### To share an Outpost that you own using the AWS Outposts console

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home "https://console.aws.amazon.com/outposts/home").
2. On the navigation pane, choose **Outposts**.
3. Select the Outpost, and then choose **Actions**, **View
   details**.
4. On the **Outpost summary** page, choose **Resource
   shares**.
5. Choose **Create resource share**.

You are redirected to the AWS RAM console to finish sharing the Outpost using the following
procedure. To share a local gateway route table that you own, use the following procedure as
well.

###### To share an Outpost or local gateway route table that you own using the AWS RAM

console

See [Creating a Resource Share](../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-create "../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-create") in the _AWS RAM User Guide_.

###### To share an Outpost or local gateway route table that you own using the AWS CLI

Use the [create-resource-share](../../../cli/latest/reference/ram/create-resource-share.md "../../../cli/latest/reference/ram/create-resource-share.md") command.

## Unsharing a shared Outpost resource

When you unshare your Outpost with a consumer, the consumer can no longer do the
following:

- View the Outpost in the AWS Outposts console.
- Create new subnets on the Outpost.
- Create new Amazon EBS volumes on the Outpost.
- View the Outpost details and instance types using the AWS Outposts console or the
  AWS CLI.

Subnets, volumes, or instances that the consumer created during the shared period are not
deleted and the consumer can continue to do the following:

- Access and modify these resources.
- Launch new instances on an existing subnet that the consumer created.

To prevent the consumer from accessing their resources and launching new instances on your
Outpost, request that the consumer delete their resources.

When a shared local gateway route table is unshared, the consumer can no longer create new
VPC associations to it. Any existing VPC associations that the consumer created remain
associated with the route table. Resources in these VPCs can continue to route traffic to the
local gateway. To prevent this, request that the consumer delete the VPC associations.

To unshare a shared Outpost resource that you own, you must remove it from the resource
share. You can do this using the AWS RAM console or the AWS CLI.

###### To unshare a shared Outpost resource that you own using the AWS RAM console

See [Updating a Resource Share](../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update "../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update") in the _AWS RAM User Guide_.

###### To unshare a shared Outpost resource that you own using the AWS CLI

Use the [disassociate-resource-share](../../../cli/latest/reference/ram/disassociate-resource-share.md "../../../cli/latest/reference/ram/disassociate-resource-share.md") command.

## Identifying a shared Outpost resource

Owners and consumers can identify shared Outposts using the AWS Outposts console and AWS CLI. They
can identify shared local gateway route tables using the AWS CLI.

###### To identify a shared Outpost using the AWS Outposts console

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home "https://console.aws.amazon.com/outposts/home").
2. On the navigation pane, choose **Outposts**.
3. Select the Outpost, and then choose **Actions**, **View
   details**.
4. On the **Outpost summary** page, view the **Owner
   ID** to identify the AWS account ID of the Outpost owner.

###### To identify a shared Outpost resource using the AWS CLI

Use the [list-outposts](../../../cli/latest/reference/outposts/list-outposts.md "../../../cli/latest/reference/outposts/list-outposts.md")
and [describe-local-gateway-route-tables](../../../cli/latest/reference/ec2/describe-local-gateway-route-tables.md "../../../cli/latest/reference/ec2/describe-local-gateway-route-tables.md") commands. These commands return the Outpost
resources that you own and Outpost resources that are shared with you. `OwnerId`
shows the AWS account ID of the Outpost resource owner.

## Shared Outpost resource permissions

### Permissions for owners

Owners are responsible for managing the Outpost and resources that they create in it.
Owners can change or revoke shared access at any time. They can use AWS Organizations to view,
modify, and delete resources that consumers create on shared Outposts.

### Permissions for consumers

Consumers can create resources on Outposts that are shared with them in the same way
that they would create resources on Outposts that they create in their own account.
Consumers are responsible for managing the resources that they launch onto Outposts that are
shared with them. Consumers can't view or modify resources owned by other consumers or by
the Outpost owner, and they can't modify Outposts that are shared with them.

## Billing and metering

Owners are billed for Outposts and Outpost resources that they share. They are also billed
for any data transfer charges associated with their Outpost's service link VPN traffic from
the AWS Region.

There are no additional charges for sharing local gateway route tables. For shared
subnets, the VPC owner is billed for VPC-level resources such as AWS Direct Connect and VPN connections,
NAT gateways, and Private Link connections.

Consumers are billed for application resources that they create on shared Outposts, such
as load balancers and Amazon RDS databases. Consumers are also billed for chargeable data transfers
from the AWS Region.

## Limitations

The following limitations apply to working with AWS Outposts sharing:

- Limitations for shared subnets apply to working with AWS Outposts sharing. For more
  information about VPC sharing limits, see [Limitations](../../../vpc/latest/userguide/vpc-sharing.md#vpc-share-limitations "../../../vpc/latest/userguide/vpc-sharing.md#vpc-share-limitations") in
  the _Amazon Virtual Private Cloud User Guide_.
- Service quotas apply per individual account.
