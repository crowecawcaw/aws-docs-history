# Managing access to Amazon Neptune databases using IAM policies

[IAM
policies](../../../kms/latest/developerguide/iam-policies.md "../../../kms/latest/developerguide/iam-policies.md") are JSON objects that define permissions to use actions and resources.

You control access in AWS by creating policies and attaching them to AWS identities or resources. A policy defines permissions when associated with an identity or resource. AWS evaluates these policies when a principal makes a request. Most policies are stored in AWS as JSON documents. For more information about JSON policy documents, see [Overview of JSON policies](../../../IAM/latest/UserGuide/access_policies.md#access_policies-json "../../../IAM/latest/UserGuide/access_policies.md#access_policies-json") in the _IAM User Guide_.

Using policies, administrators specify who has access to what by defining which **principal** can perform **actions** on what **resources**, and under what **conditions**.

By default, users and roles have no permissions. An IAM administrator creates IAM policies and adds them to roles, which users can then assume. IAM policies define permissions regardless of the method used to perform the operation.

## Identity-Based Policies

Identity-based policies are JSON permissions policy documents that you attach to an identity (user, group, or role). These policies control what actions identities can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_.

Identity-based policies can be _inline policies_ (embedded directly into a single identity) or _managed policies_ (standalone policies attached to multiple identities). To learn how to choose between managed and inline policies, see [Choose between managed policies and inline policies](../../../IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.md "../../../IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.md") in the _IAM User Guide_.

## Using Service Control Policies (SCP) with AWS organizations

Service control policies (SCPs) are JSON policies that specify the maximum
permissions for an organization or organizational unit (OU) in
[AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/").
AWS Organizations is a service for grouping and centrally managing multiple AWS accounts
that your business owns. If you enable all features in an organization, then you
can apply service control policies (SCPs) to any or all of your accounts. The SCP
limits permissions for entities in member accounts, including each AWS account
root user. For more information about Organizations and SCPs, see [How SCPs work](../../../organizations/latest/userguide/orgs_manage_policies_about-scps.md "../../../organizations/latest/userguide/orgs_manage_policies_about-scps.md") in
the AWS Organizations User Guide.

Customers deploying Amazon Neptune in an AWS Account within an AWS Organization
can leverage SCPs to control which accounts can use Neptune. To ensure access to
Neptune within a member account, be sure to:

- Allow access to `rds:*` and `neptune-db:*` for Neptune database operations. Refer to
  [Why are Amazon RDS permissions and
  resources required to use Neptune Database?](https://aws.amazon.com/neptune/faqs/ "https://aws.amazon.com/neptune/faqs/") for details on why Amazon RDS permissions are needed for Neptune
  database.
- Allow access to `neptune-graph:*` for Neptune Analytics operations.

## Permissions Required to Use the

Amazon Neptune Console

For a user to work with the Amazon Neptune console, that user must have a minimum set of
permissions. These permissions allow the user to describe the Neptune resources for their
AWS account and to provide other related information, including Amazon EC2 security and network
information.

If you create an IAM policy that is more restrictive than the minimum required
permissions, the console won't function as intended for users with that IAM policy. To
ensure that those users can still use the Neptune console, also attach the
`NeptuneReadOnlyAccess` managed policy to the user, as described in [Using AWS managed policies to access
Amazon Neptune databases](security-iam-access-managed-policies.md "security-iam-access-managed-policies.md").

You don't need to allow minimum console permissions for users that are making calls only
to the AWS CLI or the Amazon Neptune API.

## Attaching an IAM Policy to an IAM user

To apply a managed or custom policy, you attach it to an IAM user. For a tutorial
on this topic, see [Create
and Attach Your First Customer Managed Policy](../../../IAM/latest/UserGuide/tutorial_managed-policies.md "../../../IAM/latest/UserGuide/tutorial_managed-policies.md") in the _IAM User
Guide_.

As you work through the tutorial, you can use one of the policy examples shown in this
section as a starting point and tailor it to your needs. At the end of the tutorial, you have
an IAM user with an attached policy that can use the `neptune-db:*`
action.

###### Important

- Changes to an IAM policy take up to 10 minutes to apply to the specified Neptune
  resources.
- IAM policies applied to a Neptune DB cluster apply to all instances in that
  cluster.

## Using different kinds of IAM policies for

controlling access to Neptune

To provide access to Neptune administrative actions or to data in a Neptune
DB cluster, you attach policies to an IAM user or role. For information about how to
attach an IAM policy to a user, see [Attaching an IAM Policy to an IAM user](#iam-auth-policy-attaching "#iam-auth-policy-attaching"). For information about attaching a policy
to a role, see [Adding
and Removing IAM Policies](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _IAM User Guide_.

For general access to Neptune, you can use one of Neptune's [managed policies](security-iam-access-managed-policies.md "security-iam-access-managed-policies.md").
For more restricted access, you can create your own custom policy using the [administrative actions](neptune-iam-admin-actions.md "neptune-iam-admin-actions.md") and [resources](iam-admin-resources.md "iam-admin-resources.md") that Neptune supports..

In a custom IAM policy, you can use two different kinds of policy statement
that control different modes of access to a Neptune DB cluster:

- [Administrative policy statements](iam-admin-policies.md "iam-admin-policies.md")   –  
  Administrative policy statements provide access to the [Neptune
  management APIs](api.md "api.md") that you use to create, configure and manage a DB cluster
  and its instances.

Because Neptune shares functionality with Amazon RDS, administrative actions,
resources, and condition keys in Neptune policies use an `rds:`
prefix by design.

- [Data-access policy statements](iam-data-access-policies.md "iam-data-access-policies.md")   –  
  Data-access policy statements use [data-access actions](iam-dp-actions.md "iam-dp-actions.md"),
  [resources](iam-data-resources.md "iam-data-resources.md"), and [condition
  keys](iam-data-condition-keys.md#iam-neptune-condition-keys "iam-data-condition-keys.md#iam-neptune-condition-keys") to control access the data that a DB cluster contains.

Neptune data-access actions, resources and condition keys use a
`neptune-db:` prefix.

## Using IAM condition context keys in Amazon Neptune

You can specify conditions in an IAM policy statement that controls access to
Neptune. The policy statement then takes effect only when the conditions are true.

For example, you might want a policy statement to take effect only after a
specific date, or allows access only when a specific value is present in the request.

To express conditions, you use predefined condition keys in the [`Condition`](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md")
element of a policy statement, together with [IAM
condition policy operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md") such as equals or less than.

If you specify multiple `Condition` elements in a statement, or
multiple keys in a single `Condition` element, AWS evaluates them using
a logical `AND` operation. If you specify multiple values for a single
condition key, AWS evaluates the condition using a logical `OR`
operation. All of the conditions must be met before the statement's permissions are
granted.

You can also use placeholder variables when you specify conditions. For example,
you can grant an IAM user permission to access a resource only if it is tagged with
their IAM user name. For more information, see [IAM Policy Elements:
Variables and Tags](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md") in the _IAM User Guide_.

The data type of a condition key determines which condition operators you can
use to compare values in the request with the values in the policy statement.
If you use a condition operator that is not compatible with that data type, the
match always fails and the policy statement never applies.

Neptune supports different sets of condition keys for administrative policy
statements than for data-access policy statements:

- [Condition keys for
  administrative policy statements](iam-admin-condition-keys.md "iam-admin-condition-keys.md")
- [Condition keys for
  data-access policy statements](iam-data-condition-keys.md#iam-neptune-condition-keys "iam-data-condition-keys.md#iam-neptune-condition-keys")

## Support for IAM policy and access-control features in Amazon Neptune

The following table shows what IAM features Neptune supports for
administrative policy statements and data-access policy statements:

| IAM features you can use with Neptune                                                                                                                                    | IAM feature | Administrative | Data-access |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | -------------- | ----------- |
| [Identity-based policies](#security_iam_access-manage-id-based-policies "#security_iam_access-manage-id-based-policies")                                                 | Yes         | Yes            |
| [Resource-based policies](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md") | No          | No             |
| [Policy actions](../../../IAM/latest/UserGuide/reference_policies_elements_action.md "../../../IAM/latest/UserGuide/reference_policies_elements_action.md")              | Yes         | Yes            |
| [Policy resources](../../../IAM/latest/UserGuide/reference_policies_elements_resource.md "../../../IAM/latest/UserGuide/reference_policies_elements_resource.md")        | Yes         | Yes            |
| [Global condition keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md")         | Yes         | (a subset)     |
| [Tag-based condition keys](iam-admin-condition-keys.md#iam-rds-tag-based-condition-keys "iam-admin-condition-keys.md#iam-rds-tag-based-condition-keys")                  | Yes         | No             |
| [Access Control Lists (ACLs)](../../../AmazonS3/latest/userguide/acls.md "../../../AmazonS3/latest/userguide/acls.md")                                                   | No          | No             |
| [Service control policies (SCPs)](#security_iam_access-manage-scp "#security_iam_access-manage-scp")                                                                     | Yes         | Yes            |
| [Service linked roles](security-iam-service-linked-roles.md "security-iam-service-linked-roles.md")                                                                      | Yes         | No             |

## IAM Policy Limitations

Changes to an IAM policy take up to 10 minutes to apply to the specified Neptune
resources.

IAM policies applied to a Neptune DB cluster apply to all instances in that
cluster.

Neptune does not currently support cross-account access control at the data plane level. Cross-account
access control is only supported when bulk-loading and by using role chaining. For more information, see
[Bulk load tutorial](bulk-load-tutorial-chain-roles.md#bulk-load-tutorial-chain-cross-account "bulk-load-tutorial-chain-roles.md#bulk-load-tutorial-chain-cross-account") .
