# Choose between managed policies

and inline policies

Consider your use cases when deciding between managed and inline policies. In most cases,
we recommend that you use managed policies instead of inline policies.

###### Note

You can use both managed and inline policies together to define common and unique
permissions for a principal entity.

Managed policies provide the following features:

**Reusability**

A single managed policy can be attached to multiple principal entities (users,
groups, and roles). You can create a library of policies that define useful
permissions for your AWS account, and then attach these policies to principal
entities as needed.

**Central change management**

When you change a managed policy, the change is applied to all principal
entities that the policy is attached to. For example, if you want to add
permission for a new AWS API, you can update a customer managed policy or
associate an AWS managed policy to add the permission. If you're using an
AWS managed policy, AWS updates the policy. When a managed policy is
updated, the changes are applied to all principal entities that the managed
policy is attached to. In contrast, to change an inline policy, you must
individually edit each identity that contains the inline policy. For example, if
a group and a role both contain the same inline policy, you must individually
edit both principal entities to change that policy.

**Versioning and rolling back**

When you change a customer managed policy, the changed policy doesn't
overwrite the existing policy. Instead, IAM creates a new version of the
managed policy. IAM stores up to five versions of your customer managed
policies. You can use policy versions to revert a policy to an earlier version
as needed.

###### Note

A policy version is different from a `Version` policy element.
The `Version` policy element is used within a policy and defines
the version of the policy language. To learn more about policy versions, see
[Versioning IAM policies](access_policies_managed-versioning.md "access_policies_managed-versioning.md"). To learn more
about the `Version` policy element see [IAM JSON policy elements:
Version](reference_policies_elements_version.md "reference_policies_elements_version.md").

**Delegating permissions management**

You can allow users in your AWS account to attach and detach policies while
maintaining control over the permissions defined in those policies. To do this,
designate some users as full administrators—that is, administrators that
can create, update, and delete policies. You can then designate other users as
limited administrators. Those limited administrators can attach policies to
other principal entities, but only the policies that you have allowed them to
attach.

For more information about delegating permissions management, see [Controlling access to policies](access_controlling.md#access_controlling-policies "access_controlling.md#access_controlling-policies").

**Larger policy character limits**

The maximum character size limit for managed policies is greater than the
character limit for group inline policies. If you reach the inline policy's character
size limit, you can create more IAM groups and attach the managed policy to
the group.

For more information on quotas and limits, see [IAM and AWS STS quotas](reference_iam-quotas.md "reference_iam-quotas.md").

**Automatic updates for AWS managed policies**

AWS maintains AWS managed policies and updates them when necessary, for
example, to add permissions for new AWS services, without you having to make
changes. The updates are automatically applied to the principal entities that
you have attached the AWS managed policy to.

## Get started with managed

policies

We recommend using policies that [grant least
privilege](access_policies.md#grant-least-priv "access_policies.md#grant-least-priv"), or granting only the permissions required to perform a task. The
most secure way to grant least privilege is to write a customer managed policy with only
the permissions needed by your team. You must create a process to allow your team to
request more permissions when necessary. It takes time and expertise to [create IAM customer managed
policies](access_policies_create-console.md "access_policies_create-console.md") that provide your team with only the permissions they need.

To get started adding permissions to your IAM identities (users, groups of users,
and roles), you can use [AWS managed policies](access_policies_managed-vs-inline.md#aws-managed-policies "access_policies_managed-vs-inline.md#aws-managed-policies"). AWS managed policies don't grant least
privilege permissions. You must consider the security risk of granting your principals
more permissions than they need to do their job.

You can attach AWS managed policies, including job functions, to any IAM identity.
For more information, see [Adding and removing IAM identity
permissions](access_policies_manage-attach-detach.md "access_policies_manage-attach-detach.md").

To switch to least privilege permissions, you can run AWS Identity and Access Management and Access Analyzer to monitor
the principals with AWS managed policies. After learning which permissions they are
using, then you can write or generate a customer managed policy with only the required
permissions for your team. This is less secure, but provides more flexibility as you
learn how your team is using AWS. For more information, see [IAM Access Analyzer policy generation](access-analyzer-policy-generation.md "access-analyzer-policy-generation.md").

AWS managed policies are designed to provide permissions for many common use cases.
For more information about AWS managed policies that are designed for specific job
functions, see [AWS managed policies for job functions](access_policies_job-functions.md "access_policies_job-functions.md").

For a list of AWS managed policies, see [AWS
Managed Policy Reference Guide](../../../aws-managed-policy/latest/reference/about-managed-policy-reference.md "../../../aws-managed-policy/latest/reference/about-managed-policy-reference.md").

## Using inline policies

Inline policies are useful if you want to maintain a strict one-to-one relationship
between a policy and the identity to which it is applied. For example, if you want to be
sure that the permissions in a policy are not inadvertently assigned to an identity
other than the one they're intended for. When you use an inline policy, the permissions
in the policy cannot be inadvertently attached to the wrong identity. In addition, when
you use the AWS Management Console to delete that identity, the policies embedded in the identity are
deleted as well because they are part of the principal entity.
