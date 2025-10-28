# AWS managed policies for routing control in Amazon Application Recovery Controller (ARC)

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AWS managed policy: AmazonRoute53RecoveryControlConfigFullAccess

You can attach `AmazonRoute53RecoveryControlConfigFullAccess` to your IAM entities.
This policy grants full access to actions for working with recovery control configuration in ARC. Attach
it to IAM users and other principals who need full access to recovery control configuration actions.

At your discretion, you can add access to additional Amazon Route 53 actions to enable users
to create health checks for routing controls. For example, you might allow permission for one or more of the following
actions: `route53:GetHealthCheck`, `route53:CreateHealthCheck`,
`route53:DeleteHealthCheck`, and `route53:ChangeTagsForResource`.

To view the permissions for this policy, see [AmazonRoute53RecoveryControlConfigFullAccess](../../../aws-managed-policy/latest/reference/AmazonRoute53RecoveryControlConfigFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonRoute53RecoveryControlConfigFullAccess.md") in the _AWS Managed Policy Reference_.

## AWS managed policy: AmazonRoute53RecoveryControlConfigReadOnlyAccess

You can attach `AmazonRoute53RecoveryControlConfigReadOnlyAccess` to your IAM entities. It's
useful for users who need to view routing control and safety rule configurations.
This policy grants read-only access to actions for working with recovery control configuration in ARC. These
users can't create, update, or delete recovery control resources.

To view the permissions for this policy, see [AmazonRoute53RecoveryControlConfigReadOnlyAccess](../../../aws-managed-policy/latest/reference/AmazonRoute53RecoveryControlConfigReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AmazonRoute53RecoveryControlConfigReadOnlyAccess.md") in the _AWS Managed Policy Reference_.

## AWS managed policy: AmazonRoute53RecoveryClusterFullAccess

You can attach `AmazonRoute53RecoveryClusterFullAccess` to your IAM entities.
This policy grants full access to actions for working with the cluster data plane in ARC. Attach
it to IAM users and other principals who need full access to updating and retrieving routing control states.

To view the permissions for this policy, see [AmazonRoute53RecoveryClusterFullAccess](../../../aws-managed-policy/latest/reference/AmazonRoute53RecoveryClusterFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonRoute53RecoveryClusterFullAccess.md") in the _AWS Managed Policy Reference_.

## AWS managed policy: AmazonRoute53RecoveryClusterReadOnlyAccess

You can attach `AmazonRoute53RecoveryClusterReadOnlyAccess` to your IAM entities.
This policy grants read-only access to the cluster data plane in ARC. These users can retrieve routing control states
but can't update them.

To view the permissions for this policy, see [AmazonRoute53RecoveryClusterReadOnlyAccess](../../../aws-managed-policy/latest/reference/AmazonRoute53RecoveryClusterReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AmazonRoute53RecoveryClusterReadOnlyAccess.md") in the _AWS Managed Policy Reference_.

## Updates for AWS managed

policies for routing control

For details about updates to AWS managed policies for routing control in ARC since this service
began tracking these changes, see [Updates to AWS managed
policies for Amazon Application Recovery Controller (ARC)](security-iam-awsmanpol.md#security-iam-awsmanpol-arc-updates "security-iam-awsmanpol.md#security-iam-awsmanpol-arc-updates"). For automatic alerts about changes to this page, subscribe to
the RSS feed on the ARC [Document history page](doc-history.md "doc-history.md").
