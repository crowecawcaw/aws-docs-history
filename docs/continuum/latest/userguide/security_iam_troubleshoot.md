

# Troubleshooting AWS Continuum identity and access
<a name="security_iam_troubleshoot"></a>

Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS Continuum and IAM.

To change permissions, use an identity authorized to update the relevant IAM policies, or ask your AWS administrator to make the changes.

**Topics**
+ [I want to allow people outside of my AWS account to access my AWS Continuum resources](#security_iam_troubleshoot-cross-account-access)
+ [I am not authorized to use an integration when I create or update an environment](#security_iam_troubleshoot-env-integration-authorization)
+ [I am not authorized to create the Continuum collector service-linked role](#security_iam_troubleshoot-collector-slr)
+ [I am not authorized to configure a service-linked recorder for the collector](#security_iam_troubleshoot-collector-slrec)
+ [I am not authorized to pass the collector data-access role](#security_iam_troubleshoot-collector-passrole)
+ [I can't read or update the resource policy on my collector](#security_iam_troubleshoot-collector-resource-policy)
+ [I am not authorized to associate a collector with my environment](#security_iam_troubleshoot-collector-association)
+ [My Amazon S3 integration can't access my bucket](#security_iam_troubleshoot-integration-s3)
+ [I am not authorized to pass the role for an integration](#security_iam_troubleshoot-integration-passrole)

## I want to allow people outside of my AWS account to access my AWS Continuum resources
<a name="security_iam_troubleshoot-cross-account-access"></a>

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant people access to your resources.

To learn more, consult the following:
+ To learn whether AWS Continuum supports these features, see [How AWS Continuum works with IAM](security_iam_service-with-iam.md).
+ To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you own](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html) in the *IAM User Guide*.
+ To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) in the *IAM User Guide*.
+ To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html) in the *IAM User Guide*.
+ To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

## I am not authorized to use an integration when I create or update an environment
<a name="security_iam_troubleshoot-env-integration-authorization"></a>

You might see an `AccessDeniedException` error when you create or update an AWS Continuum environment that references an integration. This can happen when the caller can create or update the environment but can't use its referenced integration. AWS Continuum checks that the caller can use the referenced integration before it accepts the environment configuration.

To resolve this error, grant the calling principal the permission for the operation that you are performing:
+ When creating an environment, `continuum:CreateEnvironment` on the account- and Region-scoped `environments/*` resource and on every referenced integration ARN.
+ When updating source configuration, `continuum:UpdateEnvironment` on the environment ARN and on every referenced integration ARN.

For information about read actions and resource guidance for these console tasks, see [Using the AWS Continuum console](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-console).

## I am not authorized to create the Continuum collector service-linked role
<a name="security_iam_troubleshoot-collector-slr"></a>

You might see an `AccessDeniedException` error when you create a collector, or when you create the service-linked role that the collector uses, if you don't have permission to create that role. AWS Continuum uses the service-linked role named `AWSServiceRoleForContinuumCollector`, which trusts the `collector.continuum.amazonaws.com` service principal. Creating this role requires the `iam:CreateServiceLinkedRole` action.

To resolve this error, grant the calling principal the `iam:CreateServiceLinkedRole` action for the `collector.continuum.amazonaws.com` service-linked role. For more information about this role, see [Using service-linked roles for AWS Continuum](using-service-linked-roles.md).

## I am not authorized to configure a service-linked recorder for the collector
<a name="security_iam_troubleshoot-collector-slrec"></a>

You might see an `AccessDeniedException` error when the collector configures the service-linked recorder that it uses to record resource configuration, if the calling principal lacks the required permission.

To resolve this recorder authorization error, grant the calling principal both of the following permissions:
+ `config:DescribeConfigurationRecorders`
+ `config:PutServiceLinkedConfigurationRecorder`

## I am not authorized to pass the collector data-access role
<a name="security_iam_troubleshoot-collector-passrole"></a>

You might see an `AccessDeniedException` error when you call `AssociateCollector` to associate a collector with an environment and provide a collector data-access role. AWS Continuum assumes this role when it requests an authorization decision for the collector, so you must have permission to pass the role to AWS Continuum.

To resolve this error, grant the calling principal the `iam:PassRole` action for the exact collector data-access role. For an example policy and the full association procedure, see [Authorizing an environment to use collector data](cv-adding-context.md#cv-adding-context-cross-account).

## I can't read or update the resource policy on my collector
<a name="security_iam_troubleshoot-collector-resource-policy"></a>

You might see an `AccessDeniedException` error when you call `GetResourcePolicy` or `PutResourcePolicy` to manage the resource policy on a collector. This happens when the calling principal doesn't have permission for these actions on the collector, or when the principal doesn't belong to the collector's AWS account.

To resolve this error, grant the calling principal the `continuum:GetResourcePolicy` and `continuum:PutResourcePolicy` actions for the collector ARN, and make sure that the principal belongs to the collector account.

If `PutResourcePolicy` instead returns a `ConflictException` error, the stored policy changed after you read it. Repeat the read-and-update procedure to preserve the latest policy statements when you retry. For instructions on updating a collector resource policy, see [Authorizing an environment to use collector data](cv-adding-context.md#cv-adding-context-cross-account).

## I am not authorized to associate a collector with my environment
<a name="security_iam_troubleshoot-collector-association"></a>

You might see an `AccessDeniedException` error when you call `AssociateCollector` to associate a collector with an environment. This happens when the caller lacks required permissions or the collector data-access role lacks permission to access the collector. AWS Continuum assumes the data-access role and checks its access to the collector before creating the association.

To resolve this error, ask an IAM administrator to grant the caller both of the following permissions:
+ `continuum:AssociateCollector` for the environment.
+ `iam:PassRole` for the collector data-access role. For more information, see [I am not authorized to pass the collector data-access role](#security_iam_troubleshoot-collector-passrole).

Grant the collector data-access role `continuum:GetCollectorDataAccessAuthorization` for the collector ARN. The caller's permissions do not replace this role permission. Confirm that the role trust policy allows AWS Continuum (`continuum.amazonaws.com`) to assume the role.

For cross-account access, also confirm that the collector resource policy grants the environment account `continuum:GetCollectorDataAccessAuthorization` for the exact collector ARN. For the full list of checks, see [Troubleshooting collector authorization](cv-adding-context.md#cv-adding-context-cross-account-troubleshooting).

## My Amazon S3 integration can't access my bucket
<a name="security_iam_troubleshoot-integration-s3"></a>

You might see an access-validation failure or an `AccessDeniedException` error when you create an Amazon S3 integration, or when AWS Continuum tries to read your code from the bucket. AWS Continuum assumes the IAM role that you supply for the integration and then reads objects from the bucket, so this error usually means that the role, its trust policy, or its permissions are misconfigured.

To resolve this error, verify the following:
+ The role ARN uses the `/continuum/integrations/` path.
+ The integration role trust policy and external ID match the integration.
+ The role's permissions policy grants `s3:ListBucket` on the bucket without conditions. It also grants `s3:GetObject` and `s3:GetObjectVersion` on the code and context prefixes that your environment uses.

If role validation succeeds, verify that the console operator has `continuum:CreateIntegration` and `iam:PassRole` for the exact integration role. For the complete console permission guidance, see [Using the AWS Continuum console](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-console).

For the full set of bucket permissions, the trust policy, and the integration procedure, see [Getting started through Amazon S3](cv-getting-started.md#cv-getting-started-s3).

## I am not authorized to pass the role for an integration
<a name="security_iam_troubleshoot-integration-passrole"></a>

You might see an `AccessDeniedException` error that mentions `iam:PassRole` when you create an integration that supplies an IAM role for AWS Continuum to use, such as an Amazon S3 integration. This happens when the calling principal doesn't have permission to pass the specified role to AWS Continuum.

To resolve this error, grant the calling principal the `iam:PassRole` action for the exact role that the integration uses. For an Amazon S3 integration, the role must belong to the same account and use the `/continuum/integrations/` path. Restrict the permission by using the `iam:PassedToService` condition key with the value `continuum.amazonaws.com`.