

# AWS managed policies for readiness check in ARC
<a name="security-iam-awsmanpol-readiness"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

## AWS managed policy: Route53RecoveryReadinessServiceRolePolicy
<a name="security-iam-awsmanpol-Route53RecoveryReadinessServiceRolePolicy"></a>

You can't attach `Route53RecoveryReadinessServiceRolePolicy` to your IAM entities. This policy is attached to a service-linked role that allows Amazon Application Recovery Controller (ARC) to access AWS services and resources that are used or managed by ARC. For more information, see [Using service-linked role for readiness check in ARC](using-service-linked-roles-readiness.md).

## AWS managed policy: AmazonRoute53RecoveryReadinessFullAccess
<a name="security-iam-awsmanpol-AmazonRoute53RecoveryReadinessFullAccess"></a>

You can attach `AmazonRoute53RecoveryReadinessFullAccess` to your IAM entities. This policy grants full access to actions for working with recovery readiness (readiness check) in ARC. Attach it to IAM users and other principals who need full access to recovery readiness actions.

To view the permissions for this policy, see [AmazonRoute53RecoveryReadinessFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRoute53RecoveryReadinessFullAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AmazonRoute53RecoveryReadinessReadOnlyAccess
<a name="security-iam-awsmanpol-AmazonRoute53RecoveryReadinessReadOnlyAccess"></a>

You can attach `AmazonRoute53RecoveryReadinessReadOnlyAccess` to your IAM entities. This policy grants read-only access to actions for working with recovery readiness in ARC. It's useful for users who need to view readiness statuses and recovery group configurations. These users can't create, update, or delete recovery readiness resources.

To view the permissions for this policy, see [AmazonRoute53RecoveryReadinessReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRoute53RecoveryReadinessReadOnlyAccess.html) in the *AWS Managed Policy Reference*.

## Updates for AWS managed policies for readiness
<a name="security-iam-awsmanpol-readiness-updates"></a>

For details about updates to AWS managed policies for readiness check in ARC since this service began tracking these changes, see [Updates to AWS managed policies for Amazon Application Recovery Controller (ARC)](security-iam-awsmanpol.md#security-iam-awsmanpol-arc-updates). For automatic alerts about changes to this page, subscribe to the RSS feed on the ARC [Document history page](doc-history.md).