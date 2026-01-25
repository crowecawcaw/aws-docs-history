#

Support cross-account for clusters in ARC

Amazon Application Recovery Controller (ARC) integrates with AWS Resource Access Manager to enable resource sharing. AWS RAM is a
service that enables you to share resources with other AWS accounts or
through AWS Organizations. For ARC routing control, you can share the cluster resource.

With AWS RAM, you share resources that you own by creating a
_resource share_. A resource share specifies the resources to share,
and the _participants_ to share them with. Participants can include:

- Specific AWS accounts inside or outside of owner's organization in AWS Organizations
- An organizational unit inside its organization in AWS Organizations
- Its entire organization in AWS Organizations
  For more information about AWS RAM, see the _[AWS RAM User Guide](../../../ram/latest/userguide.md "../../../ram/latest/userguide.md")_.

By using AWS Resource Access Manager to share cluster resources across accounts in ARC, you can use one cluster to host control
panels and routing controls owned by several different AWS accounts. When you opt to share a cluster, other AWS accounts that
you specify can use the cluster to host their own control panels and routing controls, allowing more control and flexibility over
routing capabilities across different teams.

AWS RAM is a service that helps AWS customers to securely share resources across AWS accounts. With AWS RAM, you can share resources
within an organization or organizational units (OUs) in AWS Organizations, by using IAM roles and users. AWS RAM is a centralized and controlled way to
share a cluster.

When you share a cluster, you can reduce the number of total clusters that your organization requires. With
a shared cluster, you can allocate the total cost of running the cluster across different teams, to maximize the benefits
of ARC with lower cost. (Creating resources that are hosted in a cluster does not have additional costs, for the owner or for
participants.) Sharing clusters across accounts can also ease the process of onboarding multiple applications to ARC,
especially if you have a large number of applications distributed across several accounts and operations teams.

To get started with cross-account sharing in ARC, you create a _resource share_ in AWS RAM. The resource share
specifies _participants_ who are authorized to share the cluster that your account owns. Then, participants can
create resources, such as control panels and routing controls, in the cluster, by using the AWS Management Console or by running
ARC API operations using the AWS Command Line Interface or AWS SDKs.

This topic explains how to share resources that you own, and how to use resources that are
shared with you.

###### Contents

- [Prerequisites for sharing clusters](#sharing-prereqs "#sharing-prereqs")
- [Sharing a cluster](#sharing-share "#sharing-share")
- [Unsharing a shared cluster](#sharing-unshare "#sharing-unshare")
- [Identifying a shared cluster](#sharing-identify "#sharing-identify")
- [Responsibilities and permissions for shared
  clusters](#sharing-perms "#sharing-perms")
- [Billing costs](#sharing-billing "#sharing-billing")
- [Quotas](#sharing-quotas "#sharing-quotas")

## Prerequisites for sharing clusters

- To share a cluster, you must own it in your AWS account. This means that
  the resource must be allocated or provisioned in your account. You cannot share
  a cluster that has been shared with you.
- To share a cluster with your organization or an organizational unit in
  AWS Organizations, you must enable sharing with AWS Organizations. For more information, see
  [Enable sharing with AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the
  _AWS RAM User Guide_.
- AWS RAM resource shares for global resources like clusters must be created in US East (N. Virginia) Region (us-east-1).

## Sharing a cluster

When you share a cluster that you own, the participants that you specify to share the
cluster can create and host their own ARC resources in the cluster.

To share a cluster, you must add it to a resource share. A resource share is an
AWS RAM resource that lets you share your resources across AWS accounts. A resource
share specifies the resources to share, and the participants they're shared with.
To share a cluster you can create a new resource share or add the resource to an
existing resource share. To create a new resource share, you can use the
[AWS RAM console](https://console.aws.amazon.com/ram "https://console.aws.amazon.com/ram"), or use AWS RAM API operations
with the AWS Command Line Interface or AWS SDKs.

If you are part of an organization in AWS Organizations and sharing within your organization is
enabled, participants in your organization are automatically granted access to the shared
cluster. Otherwise, participants receive an invitation to join the resource share and
are granted access to the shared cluster after accepting the invitation.

You can share a cluster that you own by using the AWS RAM console, or by using
AWS RAM API operations with the AWS CLI or SDKs.

###### To share a cluster that you own by using the AWS RAM console

See [Creating a resource share](../../../ram/latest/userguide/working-with-sharing-create.md "../../../ram/latest/userguide/working-with-sharing-create.md") in the _AWS RAM User Guide_.

###### To share a cluster that you own by using the AWS CLI

Use the [create-resource-share](../../../cli/latest/reference/ram/create-resource-share.md "../../../cli/latest/reference/ram/create-resource-share.md") command.

**Granting permissions to share clusters**

Sharing clusters across accounts requires permissions for the IAM principal sharing the cluster via AWS RAM.

We recommend using the `AmazonRoute53RecoveryControlConfigFullAccess` managed IAM policy to ensure that your IAM principals have the required permissions to share and use shared clusters.

Sharing a cluster using a custom IAM policy requires `route53-recovery-control-config:PutResourcePolicy`, `route53-recovery-control-config:GetResourcePolicy`, and `route53-recovery-control-config:DeleteResourcePolicy` permissions for that cluster. `PutResourcePolicy` and `DeleteResourcePolicy` are permission-only IAM actions. Attempting to share a cluster through AWS RAM without having these permissions will result in an error.

For more information about the way that AWS Resource Access Manager uses IAM see [How AWS Resource Access Manager uses IAM](../../../ram/latest/userguide/security-iam-policies.md "../../../ram/latest/userguide/security-iam-policies.md") in the _AWS RAM User Guide_.

## Unsharing a shared cluster

When you unshare a cluster, the following applies to participants and owners:

- Current participant resources continue to exist in the unshared cluster.
- Participants can continue to update routing control states in the unshared cluster,
  to manage routing for application failover.
- Participants can no longer create new resources in the unshared cluster.
- If participants still have resources in an unshared cluster, the owner cannot
  delete the shared cluster.

To unshare a shared cluster that you own, remove it from the
resource share. You can do this by using the AWS RAM console or by using AWS RAM API operations
with the AWS CLI or SDKs.

###### To unshare a shared cluster that you own using the AWS RAM console

See [Updating a resource share](../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update "../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update") in the _AWS RAM User Guide_.

###### To unshare a shared cluster that you own using the AWS CLI

Use the [disassociate-resource-share](../../../cli/latest/reference/ram/disassociate-resource-share.md "../../../cli/latest/reference/ram/disassociate-resource-share.md") command.

## Identifying a shared cluster

Owners and participants can identify shared clusters by viewing information in AWS RAM.
They can also get information about shared resources by using the ARC console and
AWS CLI.

In general, to learn more about the resources that you've shared or that have been shared with you,
see the information in the AWS Resource Access Manager User Guide:

- As an owner, you can view all resources that you are sharing with others by using AWS RAM.
  For more information, see [Viewing your shared resources in AWS RAM](../../../ram/latest/userguide/working-with-sharing-view-sr.md "../../../ram/latest/userguide/working-with-sharing-view-sr.md").
- As a participant, you can view all resources shared with you by using AWS RAM. For more
  information, see [Viewing your shared resources in AWS RAM](../../../ram/latest/userguide/working-with-shared-view-sr.md "../../../ram/latest/userguide/working-with-shared-view-sr.md").

As an owner, you can determine if you're sharing a cluster by viewing information in
the AWS Management Console or by using the AWS Command Line Interface with ARC API operations.

###### To identify if a cluster that you own is shared by using the console

In the AWS Management Console, on the details page for a cluster, see the **Cluster sharing status**.

###### To identify if a cluster that you own is shared by using the AWS CLI

Use the [get-resource-policy](../../../recovery-cluster/latest/api/resourcepolicy-resourcearn.md "../../../recovery-cluster/latest/api/resourcepolicy-resourcearn.md") command.
If there is a resource policy for a cluster, the command returns information about the policy.

As a participant, when a cluster is shared with you, you typically must accept the share. In
addition, the **Owner** field for the cluster contains the account of the cluster
owner.

## Responsibilities and permissions for shared

clusters

### Permissions for owners

When you share a cluster that you own with other AWS accounts, participants who are
permitted to use the cluster can create control panels, routing controls, and other
resources in the cluster.

As a cluster owner, you are responsible for creating, managing, and deleting clusters.
You can't modify or delete resources created by participants, such as routing controls and
safety rules. For example, you can't update a routing control created by a participant
to change the routing control state.

However, you can view the details for routing controls that are
created by participants in a cluster that you own. For example, you can view
routing control states by calling a [ARC
routing control API operation](actions.md "actions.md"), using the AWS Command Line Interface or AWS SDKs.

If you need to modify resources create by participants, they can set up a
role in IAM with permission to access the resources, and add your account to the role.

### Permissions for participants

In general, participants can create and use control panels, routing controls, safety rules,
and health checks that they create in a cluster that is shared
with them. They can only view, modify, or delete cluster resources in the shared cluster
if they own the resources. For example, participants
can create and delete safety rules for control panels that they have created.

The following restrictions apply for participants:

- Participants cannot view, modify, or delete control panels created by
  other accounts using a shared cluster.
- Participants cannot view, create, or modify routing controls, including
  routing control states, for resources created in a shared cluster by other accounts.
- Participants cannot create, modify, or view safety rules created by
  other accounts in a shared cluster.
- Participants cannot add resources in the default control panel in a shared
  cluster because it belongs to the cluster owner.

As noted, participants cannot create routing controls in the default control panel
for a shared cluster, because the cluster owner owns the default control panel. However, the
cluster owner can create a cross-account IAM role that provides permission to
access the default control panel for the cluster. Then, the owner can grant a participant
permissions to assume the role, so that the participant can access the default control
panel to use it however the owner has specified through the role's permissions.

## Billing costs

The owner of a cluster in ARC is billed for costs associated with the cluster. There are no
additional costs, for cluster owners or for participants, for creating resources hosted in a cluster.

For detailed pricing information and examples, see
[Amazon Application Recovery Controller (ARC) Pricing](https://aws.amazon.com//route53/pricing/#application-recovery-controller "https://aws.amazon.com//route53/pricing/#application-recovery-controller") and scroll
down to Amazon Application Recovery Controller (ARC).

## Quotas

All resources created in a shared cluster—including resources created by all participants with
access to the shared cluster—count toward quotas in effect for the cluster
and other resources, such as routing controls. If accounts that share the cluster resource have a
higher quota than the cluster owner's quotas, the cluster owner's quotas takes precedence over
the quotas for the accounts that are sharing.

To better understand how this works, see the following examples. To illustrate how quotas work
with resource sharing, for these examples, let's say that the cluster owner
is Owner and an account that the cluster has been shared with is Participant.

**Control panels quota**
Quotas are enforced for Owner's total control panels per cluster.

For example, say Owner has a quota of 50 for the number of control panels per cluster, and has
13 control panels in the cluster. Now, say that Participant has the quota set to 150.
In this scenario, Participant can only create up to 37 control panels (that is, 50-13)
in the shared cluster.

In addition, if other accounts that share the cluster also create control
panels, those also all count toward the cluster overall quota of 50 control panels.

**Routing control quotas**
Routing controls have multiple quotas: a quota per control panel,
a quota per cluster, and a quota per safety rule. Owner's quotas take precedence for all of these quotas.

For example, say Owner has a quota of 300 for the number of routing controls per cluster,
and already has 300 routing controls in the cluster. Now, say that Participant has this
quota set to 500. In this scenario, Participant cannot create any new routing controls
in the shared cluster.

**Safety rules quotas**
Quotas are enforced for Owner's safety rules per control panel quota.

For example, say Owner has a quota of 20 for the number of safety rules per control panel
and Participant has this quota set to 80. In this scenario, because Owner's lower limit takes
precedence, Participant can only create up to 20 safety rules in a control panel in the shared
cluster.

For a list of routing control quotas, see [Quotas for routing control](routing-control.md "routing-control.md").
