

# AWS managed policies for routing control in Amazon Application Recovery Controller (ARC)
<a name="security-iam-awsmanpol-routing"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

## AWS managed policy: AmazonRoute53RecoveryControlConfigFullAccess
<a name="security-iam-awsmanpol-AmazonRoute53RecoveryControlConfigFullAccess"></a>

You can attach `AmazonRoute53RecoveryControlConfigFullAccess` to your IAM entities. This policy grants full access to actions for working with recovery control configuration in ARC. Attach it to IAM users and other principals who need full access to recovery control configuration actions.

At your discretion, you can add access to additional Amazon Route 53 actions to enable users to create health checks for routing controls. For example, you might allow permission for one or more of the following actions: `route53:GetHealthCheck`, `route53:CreateHealthCheck`, `route53:DeleteHealthCheck`, and `route53:ChangeTagsForResource`.

To view the permissions for this policy, see [AmazonRoute53RecoveryControlConfigFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRoute53RecoveryControlConfigFullAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AmazonRoute53RecoveryControlConfigReadOnlyAccess
<a name="security-iam-awsmanpol-AmazonRoute53RecoveryControlConfigReadOnlyAccess"></a>

You can attach `AmazonRoute53RecoveryControlConfigReadOnlyAccess` to your IAM entities. It's useful for users who need to view routing control and safety rule configurations. This policy grants read-only access to actions for working with recovery control configuration in ARC. These users can't create, update, or delete recovery control resources.

To view the permissions for this policy, see [AmazonRoute53RecoveryControlConfigReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRoute53RecoveryControlConfigReadOnlyAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AmazonRoute53RecoveryClusterFullAccess
<a name="security-iam-awsmanpol-AmazonRoute53RecoveryClusterFullAccess"></a>

You can attach `AmazonRoute53RecoveryClusterFullAccess` to your IAM entities. This policy grants full access to actions for working with the cluster data plane in ARC. Attach it to IAM users and other principals who need full access to updating and retrieving routing control states.

To view the permissions for this policy, see [AmazonRoute53RecoveryClusterFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRoute53RecoveryClusterFullAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AmazonRoute53RecoveryClusterReadOnlyAccess
<a name="security-iam-awsmanpol-AmazonRoute53RecoveryClusterReadOnlyAccess"></a>

You can attach `AmazonRoute53RecoveryClusterReadOnlyAccess` to your IAM entities. This policy grants read-only access to the cluster data plane in ARC. These users can retrieve routing control states but can't update them.

To view the permissions for this policy, see [AmazonRoute53RecoveryClusterReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRoute53RecoveryClusterReadOnlyAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy
<a name="security-iam-awsmanpol-AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy"></a>

You can attach `AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy` to your IAM entities. This policy grants permissions for ARC Region switch plan execution and evaluation. Attach it to IAM roles used for Region switch plan execution.

**Permissions details**

This policy includes the following permissions:
+ `arc-region-switch:GetPlan` – Allows principals to retrieve configuration details for a Region switch plan.
+ `arc-region-switch:GetPlanExecution` – Allows principals to retrieve information about a specific Region switch plan execution.
+ `arc-region-switch:ListPlanExecutions` – Allows principals to list all executions of Region switch plans.
+ `iam:SimulatePrincipalPolicy` – Allows principals to simulate and evaluate what actions an IAM role can perform. This permission is scoped to IAM roles only and is used during plan evaluation to verify that necessary permissions are in place before executing a Region switch plan.
+ `cloudwatch:DescribeAlarms` – Allows principals to retrieve information about Amazon CloudWatch alarms.
+ `cloudwatch:DescribeAlarmHistory` – Allows principals to retrieve historical state changes for Amazon CloudWatch alarms.
+ `cloudwatch:GetMetricStatistics` – Allows principals to retrieve statistical data for Amazon CloudWatch metrics.

To view more details about the policy, including the latest version of the JSON policy document, see [AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonApplicationRecoveryControllerRegionSwitchPlanExecutionPolicy.html) in the *AWS Managed Policy Reference Guide*.

## Updates for AWS managed policies for routing control
<a name="security-iam-awsmanpol-routing-updates"></a>

For details about updates to AWS managed policies for routing control in ARC since this service began tracking these changes, see [Updates to AWS managed policies for Amazon Application Recovery Controller (ARC)](security-iam-awsmanpol.md#security-iam-awsmanpol-arc-updates). For automatic alerts about changes to this page, subscribe to the RSS feed on the ARC [Document history page](doc-history.md).