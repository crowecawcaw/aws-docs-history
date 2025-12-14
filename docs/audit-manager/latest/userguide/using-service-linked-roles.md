# Using service-linked roles for AWS Audit Manager

AWS Audit Manager uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to Audit Manager. Service-linked roles are predefined by Audit Manager and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up AWS Audit Manager easier because you don’t have to

manually add the necessary permissions. Audit Manager defines the permissions of its
service-linked roles, and unless defined otherwise, only Audit Manager can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

For information about other services that support service-linked roles, see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes**
in the **Service-Linked Role** column. Choose a
**Yes** with a link to view the service-linked role documentation for
that service.

## Service-linked role permissions for AWS Audit Manager

Audit Manager uses the service-linked role named
`**AWSServiceRoleForAuditManager**`, which enables access to AWS services and resources used or managed by AWS Audit Manager.

The `AWSServiceRoleForAuditManager` service-linked role trusts the
`auditmanager.amazonaws.com` service to assume the role.

The role permissions policy, [`AWSAuditManagerServiceRolePolicy`](../../../aws-managed-policy/latest/reference/AWSAuditManagerServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerServiceRolePolicy.md"), allows Audit Manager to collect
automated evidence about your AWS usage. More specifically, it can take the following
actions on your behalf.

- Audit Manager can use AWS Security Hub CSPM to collect **compliance
  check** evidence. In this case, Audit Manager uses the following permission
  to report the results of security checks directly from AWS Security Hub CSPM. It then
  attaches the results to your relevant assessment controls as evidence.
  - `securityhub:DescribeStandards`

###### Note

For more information about which specific Security Hub CSPM controls Audit Manager can
describe, see [AWS Security Hub CSPM controls supported by AWS Audit Manager](control-data-sources-ash.md "control-data-sources-ash.md").

- Audit Manager can use AWS Config to collect **compliance check**
  evidence. In this case, Audit Manager uses the following permissions to report the
  results of AWS Config rule evaluations directly from AWS Config. It then attaches the
  results to your relevant assessment controls as evidence.
  - `config:DescribeConfigRules`
  - `config:DescribeDeliveryChannels`
  - `config:ListDiscoveredResources`

###### Note

For more information about which specific AWS Config rules Audit Manager can describe,
see [AWS Config Rules supported by AWS Audit Manager](control-data-sources-config.md "control-data-sources-config.md").

- Audit Manager can use AWS CloudTrail to collect **user
  activity** evidence. In this case, Audit Manager uses the following
  permissions to capture user activity from CloudTrail logs. It then attaches the
  activity to your relevant assessment controls as evidence.
  - `cloudtrail:DescribeTrails`
  - `cloudtrail:LookupEvents`

###### Note

For more information about which specific CloudTrail events Audit Manager can describe,
see [AWS CloudTrail event names supported by AWS Audit Manager](control-data-sources-cloudtrail.md "control-data-sources-cloudtrail.md").

- Audit Manager can use AWS API calls to collect **resource
  configuration** evidence. In this case, Audit Manager uses the following
  permissions to call read-only APIs that describe your resource configurations
  for the following AWS services. It then attaches the API responses to your
  relevant assessment controls as evidence.
  - `acm:GetAccountConfiguration`
  - `acm:ListCertificates`
  - `apigateway:GET`
  - `autoscaling:DescribeAutoScalingGroups`
  - `backup:ListBackupPlans`
  - `backup:ListRecoveryPointsByResource`
  - `bedrock:GetCustomModel`
  - `bedrock:GetFoundationModel`
  - `bedrock:GetModelCustomizationJob`
  - `bedrock:GetModelInvocationLoggingConfiguration`
  - `bedrock:ListCustomModels`
  - `bedrock:ListFoundationModels`
  - `bedrock:ListGuardrails`
  - `bedrock:ListModelCustomizationJobs`
  - `cloudfront:GetDistribution`
  - `cloudfront:GetDistributionConfig`
  - `cloudfront:ListDistributions`
  - `cloudtrail:DescribeTrails`
  - `cloudtrail:GetTrail`
  - `cloudtrail:ListTrails`
  - `cloudtrail:LookupEvents`
  - `cloudwatch:DescribeAlarms`
  - `cloudwatch:DescribeAlarmsForMetric`
  - `cloudwatch:GetMetricStatistics`
  - `cloudwatch:ListMetrics`
  - `cognito-idp:DescribeUserPool`
  - `config:DescribeConfigRules`
  - `config:DescribeDeliveryChannels`
  - `config:ListDiscoveredResources`
  - `directconnect:DescribeDirectConnectGateways`
  - `directconnect:DescribeVirtualGateways`
  - `dynamodb:DescribeBackup`
  - `dynamodb:DescribeContinuousBackups`
  - `dynamodb:DescribeTable`
  - `dynamodb:DescribeTableReplicaAutoScaling`
  - `dynamodb:ListBackups`
  - `dynamodb:ListGlobalTables`
  - `dynamodb:ListTables`
  - `ec2:DescribeAddresses`
  - `ec2:DescribeCustomerGateways`
  - `ec2:DescribeEgressOnlyInternetGateways`
  - `ec2:DescribeFlowLogs`
  - `ec2:DescribeInstanceCreditSpecifications`
  - `ec2:DescribeInstanceAttribute`
  - `ec2:DescribeInstances`
  - `ec2:DescribeInternetGateways`
  - `ec2:DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations`
  - `ec2:DescribeLocalGateways`
  - `ec2:DescribeLocalGatewayVirtualInterfaces`
  - `ec2:DescribeNatGateways`
  - `ec2:DescribeNetworkAcls`
  - `ec2:DescribeRouteTables`
  - `ec2:DescribeSecurityGroups`
  - `ec2:DescribeSecurityGroupRules`
  - `ec2:DescribeSnapshots`
  - `ec2:DescribeTransitGateways`
  - `ec2:DescribeVolumes`
  - `ec2:DescribeVpcEndpoints`
  - `ec2:DescribeVpcEndpointConnections`
  - `ec2:DescribeVpcEndpointServiceConfigurations`
  - `ec2:DescribeVpcPeeringConnections`
  - `ec2:DescribeVpcs`
  - `ec2:DescribeVpnConnections`
  - `ec2:DescribeVpnGateways`
  - `ec2:GetEbsDefaultKmsKeyId`
  - `ec2:GetEbsEncryptionByDefault`
  - `ec2:GetLaunchTemplateData`
  - `ecs:DescribeClusters`
  - `eks:DescribeAddonVersions`
  - `elasticache:DescribeCacheClusters`
  - `elasticache:DescribeServiceUpdates`
  - `elasticfilesystem:DescribeAccessPoints`
  - `elasticfilesystem:DescribeFileSystems`
  - `elasticloadbalancing:DescribeLoadBalancers`
  - `elasticloadbalancing:DescribeSslPolicies`
  - `elasticloadbalancing:DescribeTargetGroups`
  - `elasticmapreduce:ListClusters`
  - `elasticmapreduce:ListSecurityConfigurations`
  - `es:DescribeDomains`
  - `es:DescribeDomain`
  - `es:DescribeDomainConfig`
  - `es:ListDomainNames`
  - `events:DeleteRule`
  - `events:DescribeRule`
  - `events:DisableRule`
  - `events:EnableRule`
  - `events:ListConnections`
  - `events:ListEventBuses`
  - `events:ListEventSources`
  - `events:ListRules`
  - `events:ListTargetsByRule`
  - `events:PutRule`
  - `events:PutTargets`
  - `events:RemoveTargets`
  - `firehose:ListDeliveryStreams`
  - `fsx:DescribeFileSystems`
  - `guardduty:ListDetectors`
  - `iam:GenerateCredentialReport`
  - `iam:GetAccessKeyLastUsed`
  - `iam:GetAccountAuthorizationDetails`
  - `iam:GetAccountPasswordPolicy`
  - `iam:GetAccountSummary`
  - `iam:GetCredentialReport`
  - `iam:GetGroupPolicy`
  - `iam:GetPolicy`
  - `iam:GetPolicyVersion`
  - `iam:GetRolePolicy`
  - `iam:GetUser`
  - `iam:GetUserPolicy`
  - `iam:ListAccessKeys`
  - `iam:ListAttachedGroupPolicies`
  - `iam:ListAttachedRolePolicies`
  - `iam:ListAttachedUserPolicies`
  - `iam:ListEntitiesForPolicy`
  - `iam:ListGroupPolicies`
  - `iam:ListGroups`
  - `iam:ListGroupsForUser`
  - `iam:ListMfaDeviceTags`
  - `iam:ListMfaDevices`
  - `iam:ListOpenIdConnectProviders`
  - `iam:ListPolicies`
  - `iam:ListPolicyVersions`
  - `iam:ListRolePolicies`
  - `iam:ListRoles`
  - `iam:ListSamlProviders`
  - `iam:ListUserPolicies`
  - `iam:ListUsers`
  - `iam:ListVirtualMFADevices`
  - `kafka:ListClusters`
  - `kafka:ListKafkaVersions`
  - `kinesis:ListStreams`
  - `kms:DescribeKey`
  - `kms:GetKeyPolicy`
  - `kms:GetKeyRotationStatus`
  - `kms:ListGrants`
  - `kms:ListKeyPolicies`
  - `kms:ListKeys`
  - `lambda:ListFunctions`
  - `license-manager:ListAssociationsForLicenseConfiguration`
  - `license-manager:ListLicenseConfigurations`
  - `license-manager:ListUsageForLicenseConfiguration`
  - `logs:DescribeDestinations`
  - `logs:DescribeExportTasks`
  - `logs:DescribeLogGroups`
  - `logs:DescribeMetricFilters`
  - `logs:DescribeResourcePolicies`
  - `logs:FilterLogEvents`
  - `logs:GetDataProtectionPolicy`
  - `organizations:DescribeOrganization`
  - `organizations:DescribePolicy`
  - `rds:DescribeCertificates`
  - `rds:DescribeDBClusterEndpoints`
  - `rds:DescribeDBClusterParameterGroups`
  - `rds:DescribeDBClusters`
  - `rds:DescribeDBInstances`
  - `rds:DescribeDBInstanceAutomatedBackups`
  - `rds:DescribeDBSecurityGroups`
  - `redshift:DescribeClusters`
  - `redshift:DescribeClusterSnapshots`
  - `redshift:DescribeLoggingStatus`
  - `route53:GetQueryLoggingConfig`
  - `s3:GetBucketAcl`
  - `s3:GetBucketLogging`
  - `s3:GetBucketOwnershipControls`
  - `s3:GetBucketPolicy`
    - This API action operates within the scope of the AWS account
      where the service-linked-role is available. It can't access
      cross-account bucket policies.

  - `s3:GetBucketPublicAccessBlock`
  - `s3:GetBucketTagging`
  - `s3:GetBucketVersioning`
  - `s3:GetEncryptionConfiguration`
  - `s3:GetLifecycleConfiguration`
  - `s3:ListAllMyBuckets`
  - `sagemaker:DescribeAlgorithm`
  - `sagemaker:DescribeDomain`
  - `sagemaker:DescribeEndpoint`
  - `sagemaker:DescribeEndpointConfig`
  - `sagemaker:DescribeFlowDefinition`
  - `sagemaker:DescribeHumanTaskUi`
  - `sagemaker:DescribeLabelingJob`
  - `sagemaker:DescribeModel`
  - `sagemaker:DescribeModelBiasJobDefinition`
  - `sagemaker:DescribeModelCard`
  - `sagemaker:DescribeModelQualityJobDefinition`
  - `sagemaker:DescribeTrainingJob`
  - `sagemaker:DescribeUserProfile`
  - `sagemaker:ListAlgorithms`
  - `sagemaker:ListDomains`
  - `sagemaker:ListEndpointConfigs`
  - `sagemaker:ListEndpoints`
  - `sagemaker:ListFlowDefinitions`
  - `sagemaker:ListHumanTaskUis`
  - `sagemaker:ListLabelingJobs`
  - `sagemaker:ListModels`
  - `sagemaker:ListModelBiasJobDefinitions`
  - `sagemaker:ListModelCards`
  - `sagemaker:ListModelQualityJobDefinitions`
  - `sagemaker:ListMonitoringAlerts`
  - `sagemaker:ListMonitoringSchedules`
  - `sagemaker:ListTrainingJobs`
  - `sagemaker:ListUserProfiles`
  - `securityhub:DescribeStandards`
  - `secretsmanager:DescribeSecret`
  - `secretsmanager:ListSecrets`
  - `sns:ListTagsForResource`
  - `sns:ListTopics`
  - `sqs:ListQueues`
  - `waf-regional:GetLoggingConfiguration`
  - `waf-regional:GetRule`
  - `waf-regional:GetWebAcl`
  - `waf-regional:ListRuleGroups`
  - `waf-regional:ListRules`
  - `waf-regional:ListSubscribedRuleGroups`
  - `waf-regional:ListWebACLs`
  - `waf:GetRule`
  - `waf:GetRuleGroup`
  - `waf:ListActivatedRulesInRuleGroup`
  - `waf:ListRuleGroups`
  - `waf:ListRules`
  - `waf:ListWebAcls`
  - `wafv2:ListWebAcls`

###### Note

For more information about the specific API calls that Audit Manager can describe,
see [Supported API calls for custom
control data sources](control-data-sources-api.md#apis-for-custom-control-data-sources "control-data-sources-api.md#apis-for-custom-control-data-sources").

To view the full permissions details of the service-linked role
`AWSServiceRoleForAuditManager`, see [AWSAuditManagerServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSAuditManagerServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerServiceRolePolicy.md") in the _AWS
Managed Policy Reference Guide_.

You must configure permissions to allow an IAM entity (such as a user, group, or
role) to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating the AWS Audit Manager service-linked role

You don't need to manually create a service-linked role. When you enable AWS Audit Manager, the

service automatically creates the service-linked role for you. You can enable Audit Manager
from the onboarding page of the AWS Management Console, or via the API or AWS CLI. For more
information, see [Enabling AWS Audit Manager](setup-audit-manager.md "setup-audit-manager.md") in this user guide.

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account.

## Editing the AWS Audit Manager service-linked role

AWS Audit Manager doesn't allow you to edit the `AWSServiceRoleForAuditManager` service-linked role.
After you create a service-linked role, you can't change the name of the role because
various entities might reference the role. However, you can edit the description of the
role using IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

###### To allow an IAM entity to edit the description of the `AWSServiceRoleForAuditManager`

service-linked role

Add the following statement to the permissions policy for the IAM entity that needs to
edit the description of a service-linked role.

```
{
    "Effect": "Allow",
    "Action": [
        "iam:UpdateRoleDescription"
    ],
    "Resource": "arn:aws:iam::*:role/aws-service-role/auditmanager.amazonaws.com/AWSServiceRoleForAuditManager*",
    "Condition": {"StringLike": {"iam:AWSServiceName": "auditmanager.amazonaws.com"}}
}
```

## Deleting the AWS Audit Manager service-linked role

If you no longer need to use Audit Manager, we recommend that you delete the
`AWSServiceRoleForAuditManager` service-linked role. That way, you don't have an unused
entity that isn't actively monitored or maintained. However, you must clean up the
service-linked role before you can delete it.

###### Cleaning up the service-linked role

Before you can use IAM to delete the Audit Manager service-linked role, you must first
confirm that the role has no active sessions and remove any resources used by the
role. To do so, ensure that Audit Manager is deregistered in all AWS Regions. After you
deregister, Audit Manager no longer uses the service-linked role.

For instructions on how to deregister Audit Manager, see the following resources:

- [Disabling AWS Audit Manager](disable.md "disable.md") in this guide
- [DeregisterAccount](../APIReference/API_DeregisterAccount.md "../APIReference/API_DeregisterAccount.md") in the _AWS Audit Manager API Reference_
- [deregister-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/deregister-account.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/deregister-account.html") in the _AWS CLI Reference for AWS Audit Manager_

For instructions on how to delete Audit Manager resources manually, see [Deletion of Audit Manager data](data-protection.md#data-deletion-and-retention "data-protection.md#data-deletion-and-retention") in this guide.

###### Deleting the service-linked role

You can delete the service-linked role using the IAM console, the AWS Command Line Interface
(AWS CLI), or the IAM API.

IAM console
Follow these steps to delete a service-linked role in the IAM
console.

###### To delete a service-linked role (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose
   **Roles**. Then select the check box next to
   `AWSServiceRoleForAuditManager`, not the name or row itself.
3. Under **Role actions** at the top of the
   page, choose **Delete**.
4. In the confirmation dialog box, review the last accessed
   information, which shows when each of the selected roles last
   accessed an AWS service. This helps you to confirm whether the
   role is currently active. If you want to proceed, enter
   `AWSServiceRoleForAuditManager` in the text input field and
   choose **Delete** to submit the service-linked role
   for deletion.
5. Watch the IAM console notifications to monitor the progress of
   the service-linked role deletion. Because the IAM service-linked
   role deletion is asynchronous, after you submit the role for
   deletion, the deletion task can succeed or fail. If the task
   succeeds, then the role is removed from the list and a success
   message appears at the top of the page.

AWS CLI
You can use IAM commands from the AWS CLI to delete a service-linked role.

###### To delete a service-linked role (AWS CLI)

1. Enter the following command to list the role in your account:

```
aws iam get-role --role-name AWSServiceRoleForAuditManager
```

2. Because a service-linked role can't be deleted if it's being used or
   has associated resources, you must submit a deletion request. That
   request can be denied if these conditions aren't met. You must
   capture the `deletion-task-id` from the response to check
   the status of the deletion task.

Enter the following command to submit a service-linked role deletion
request:

```
aws iam delete-service-linked-role --role-name AWSServiceRoleForAuditManager
```

3. Use the following command to check the status of the deletion task:

```
aws iam get-service-linked-role-deletion-status --deletion-task-id `deletion-task-id`
```

The status of the deletion task can be `NOT_STARTED`,
`IN_PROGRESS`, `SUCCEEDED`, or
`FAILED`. If the deletion fails, the call returns the
reason that it failed so that you can troubleshoot.

IAM API
You can use the IAM API to delete a service-linked role.

###### To delete a service-linked role (API)

1. Call [GetRole](../../../IAM/latest/APIReference/API_GetRole.md "../../../IAM/latest/APIReference/API_GetRole.md") to list the role in your
   account. In the request, specify `AWSServiceRoleForAuditManager` as the
   `RoleName`.
2. Because a service-linked role can't be deleted if it's being used
   or has associated resources, you must submit a deletion request.
   That request can be denied if these conditions aren't met. You must
   capture the `DeletionTaskId` from the response to check
   the status of the deletion task.

To submit a deletion request for a service-linked role, call
[DeleteServiceLinkedRole](../../../IAM/latest/APIReference/API_DeleteServiceLinkedRole.md "../../../IAM/latest/APIReference/API_DeleteServiceLinkedRole.md"). In the request, specify
`AWSServiceRoleForAuditManager` as the `RoleName`. 3. To check the status of the deletion, call [GetServiceLinkedRoleDeletionStatus](../../../IAM/latest/APIReference/API_GetServiceLinkedRoleDeletionStatus.md "../../../IAM/latest/APIReference/API_GetServiceLinkedRoleDeletionStatus.md"). In the request,
specify the `DeletionTaskId`.

The status of the deletion task can be `NOT_STARTED`,
`IN_PROGRESS`, `SUCCEEDED`, or
`FAILED`. If the deletion fails, the call returns the
reason that it failed so that you can troubleshoot.

### Tips for deleting the Audit Manager service-linked

role

The deletion process for the Audit Manager service-linked role might fail if Audit Manager is using
the role or has associated resources. This can happen in the following
scenarios:

1. Your account is still registered with Audit Manager in one or more
   AWS Regions.
2. Your account is part of an AWS organization, and the management account
   or the delegated administrator account is still onboarded to Audit Manager.

To resolve a failed deletion issue, start by checking whether your AWS account is
part of an Organization. You can do this by calling the [DescribeOrganization](../../../organizations/latest/APIReference/API_DescribeOrganization.md "../../../organizations/latest/APIReference/API_DescribeOrganization.md") API operation, or by navigating to the AWS Organizations
console.

###### If your AWS account is part of an organization

1. Use your management account to [remove your delegated administrator in Audit Manager](remove-delegated-admin.md "remove-delegated-admin.md") in all
   AWS Regions where you added one.
2. Use your management account to [deregister Audit Manager](disable.md "disable.md") in all AWS Regions where you used the
   service.
3. Try again to delete the service-linked role by following the steps in the previous procedure.

###### If your AWS account is not part of an organization

1. Make sure that you [deregistered Audit Manager](disable.md "disable.md") in all AWS Regions where you used the
   service.
2. Try again to delete the service-linked role by following the steps in the previous procedure.

After you deregister from Audit Manager, the service will stop using the service-linked role. You can then delete the role successfully.

## Supported Regions for AWS Audit Manager service-linked roles

AWS Audit Manager supports using service-linked roles in all of the AWS Regions where the service is
available. For more information, see [AWS service endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").
