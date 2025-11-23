#

Support sharing plans across accounts for ARC Region switch

Amazon Application Recovery Controller (ARC) integrates with AWS Resource Access Manager to enable resource sharing. AWS RAM is a
service that enables you to share resources with other AWS accounts or
through AWS Organizations. For ARC Region switch, you can share the Region switch plan.
(To use resources from another account in your plan, you use a crossAccount role.
To learn more, see [Cross-account resources](cross-account-resources-rs.md#cross-account-resources-rs-in-plan "cross-account-resources-rs.md#cross-account-resources-rs-in-plan").)

With AWS RAM, you share resources that you own by creating a
_resource share_. A resource share specifies the resources to share,
and the _participants_ to share them with. Participants can include:

- Specific AWS accounts inside or outside of owner's organization in AWS Organizations
- An organizational unit inside its organization in AWS Organizations
- Its entire organization in AWS Organizations
  For more information about AWS RAM, see the _[AWS RAM User Guide](../../../ram/latest/userguide.md "../../../ram/latest/userguide.md")_.

By using AWS Resource Access Manager to share plans across accounts in ARC, you can use one plan with
several different AWS accounts. When you opt to share a plan, other AWS accounts that
you specify can execute the plan to perform application recovery.

AWS RAM is a service that helps AWS customers to securely share resources across AWS accounts.
With AWS RAM, you can share resources within an organization or organizational units (OUs) in AWS Organizations,
by using IAM roles and users. AWS RAM is a centralized and controlled way to
share a plan.

When you share a plan, you can reduce the number of total plans that your organization requires. With
a shared plan, you can allocate the total cost of running the plan across different teams, to maximize the benefits
of ARC with lower cost. Sharing plans across accounts can also ease the process of onboarding multiple
applications to ARC, especially if you have a large number of applications distributed across
several accounts and operations teams.

To get started with cross-account sharing in ARC, you create a _resource share_ i
n AWS RAM. The resource share specifies _participants_ who are authorized to share
the plan that your account owns.

This topic explains how to share resources that you own, and how to use resources that are
shared with you.

###### Contents

- [Prerequisites for sharing plans](#sharing-prereqs-rs "#sharing-prereqs-rs")
- [Sharing a plan](#sharing-share-rs "#sharing-share-rs")
- [Unsharing a shared plan](#sharing-unshare-rs "#sharing-unshare-rs")
- [Identifying a shared plan](#sharing-identify-rs "#sharing-identify-rs")
- [Responsibilities and permissions for shared
  plans](#sharing-perms-rs "#sharing-perms-rs")
- [Billing costs](#sharing-billing-rs "#sharing-billing-rs")
- [Quotas](#sharing-quotas-rs "#sharing-quotas-rs")

## Prerequisites for sharing plans

- To share a plan, you must own it in your AWS account. This means that
  the resource must be allocated or provisioned in your account. You cannot share
  a plan that has been shared with you.
- To share a plan with your organization or an organizational unit in
  AWS Organizations, you must enable sharing with AWS Organizations. For more information, see
  [Enable sharing with AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the _AWS RAM User Guide_.

## Sharing a plan

When you share a plan, the participants that you specify to share the plan can view
and, if you grant additional permissions, execute the plan.

To share a plan, you must add it to a resource share. A resource share is an
AWS RAM resource that lets you share your resources across AWS accounts. A resource
share specifies the resources to share, and the participants they're shared with.
To share a plan you can create a new resource share or add the resource to an
existing resource share. To create a new resource share, you can use the
[AWS RAM console](https://console.aws.amazon.com/ram "https://console.aws.amazon.com/ram"), or use AWS RAM API operations
with the AWS Command Line Interface or AWS SDKs.

If you are part of an organization in AWS Organizations and sharing within your organization is
enabled, participants in your organization are automatically granted access to the shared
plan. Otherwise, participants receive an invitation to join the resource share and
are granted access to the shared plan after accepting the invitation.

You can share a plan that you own by using the AWS RAM console, or by using
AWS RAM API operations with the AWS CLI or SDKs.

###### To share a plan that you own by using the AWS RAM console

See [Creating a resource share](../../../ram/latest/userguide/working-with-sharing-create.md "../../../ram/latest/userguide/working-with-sharing-create.md") in the _AWS RAM User Guide_.

###### To share a plan that you own by using the AWS CLI

Use the [create-resource-share](../../../cli/latest/reference/ram/create-resource-share.md "../../../cli/latest/reference/ram/create-resource-share.md") command.

**Granting permissions to share plans**

Sharing plans across accounts requires the following additional permissions for the IAM principal sharing the plan by
using AWS RAM:

```
# read and execute plan permissions
"arc-region-switch:GetPlan",
"arc-region-switch:GetPlanInRegion",
"arc-region-switch:GetPlanExecution",
"arc-region-switch:ListPlanExecutionEvents",
"arc-region-switch:ListPlanExecutions",
"arc-region-switch:ListRoute53HealthChecks",
"arc-region-switch:GetPlanEvaluationStatus",
"arc-region-switch:StartPlanExecution",
"arc-region-switch:CancelPlanExecution",
"arc-region-switch:UpdatePlanExecution",
"arc-region-switch:UpdatePlanExecutionStep"
```

The owner who shares the plan must have the following permissions. If you attempt to share a
plan through AWS RAM without having these permissions, an error is returned.

```
"arc-region-switch:PutResourcePolicy" # Permission only apis
"arc-region-switch:DeleteResourcePolicy" # Permission only apis
"arc-region-switch:GetResourcePolicy" # Permission only apis
```

For more information about the way that AWS Resource Access Manager uses IAM see [How AWS Resource Access Manager uses IAM](../../../ram/latest/userguide/security-iam-policies.md "../../../ram/latest/userguide/security-iam-policies.md") in the _AWS RAM User Guide_.

## Unsharing a shared plan

When you unshare a plan, the following applies to participants and owners:

- Participants can no longer view or execute the unshared plan.

To unshare a shared plan that you own, remove it from the
resource share. You can do this by using the AWS RAM console or by using AWS RAM API operations
with the AWS CLI or SDKs.

###### To unshare a shared plan that you own using the AWS RAM console

See [Updating a resource share](../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update "../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update") in the _AWS RAM User Guide_.

###### To unshare a shared plan that you own using the AWS CLI

Use the [disassociate-resource-share](../../../cli/latest/reference/ram/disassociate-resource-share.md "../../../cli/latest/reference/ram/disassociate-resource-share.md") command.

## Identifying a shared plan

Owners and participants can identify shared plans by viewing information in AWS RAM.
They can also get information about shared resources by using the ARC console and
AWS CLI.

In general, to learn more about the resources that you've shared or that have been shared with you,
see the information in the AWS Resource Access Manager User Guide:

- As an owner, you can view all resources that you are sharing with others by using AWS RAM.
  For more information, see [Viewing your shared resources in AWS RAM](../../../ram/latest/userguide/working-with-sharing-view-sr.md "../../../ram/latest/userguide/working-with-sharing-view-sr.md").
- As a participant, you can view all resources shared with you by using AWS RAM. For more
  information, see [Viewing your shared resources in AWS RAM](../../../ram/latest/userguide/working-with-shared-view-sr.md "../../../ram/latest/userguide/working-with-shared-view-sr.md").

As an owner, you can determine if you're sharing a plan by viewing information in
the AWS Management Console or by using the AWS Command Line Interface with ARC API operations.

###### To identify if a plan that you own is shared by using the console

In the AWS Management Console, on the details page for a plan, see the **plan sharing status**.

As a participant, when a plan is shared with you, you typically must accept the share so that
you can access the plan.

## Responsibilities and permissions for shared

plans

### Permissions for owners

Participants can view or execute the plan (if they have the correct permissions).

### Permissions for participants

When you share a plan that you own with other AWS accounts, participants can
view or execute the plan (if they have the correct permissions).

When you share a plan by using AWS RAM, a participant has, by default, read-only permissions.
To review a list of read-only permissions for Region switch, see [Read-only permissions](security_iam_region_switch_read_only.md "security_iam_region_switch_read_only.md"). Participants need additional permissions
to execute a Region switch plan. Participants who need to execute plans need additional permissions.
Be aware that you cannot grant permission to a AWS RAM participant for the following operations:

- `ApprovePlanExecutionStep`
- `UpdatePlan`

## Billing costs

The owner of a plan in ARC is billed for costs associated with the plan. There are no
additional costs, for plan owners or for participants, for creating resources hosted in a plan.

For detailed pricing information and examples, see
[Amazon Application Recovery Controller (ARC) Pricing](https://aws.amazon.com//route53/pricing/#application-recovery-controller "https://aws.amazon.com//route53/pricing/#application-recovery-controller") and scroll
down to Amazon Application Recovery Controller (ARC).

## Quotas

All resources created in a shared plan count toward quotas for the plan owner.

For a list of Region switch plan quotas, see [Quotas for Region switch](quotas.md "quotas.md").
