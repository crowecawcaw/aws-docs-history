• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# AWS managed policies for

AWS Systems Manager

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

###### Topics

- [AWS managed
  policy: AmazonSSMServiceRolePolicy](#security-iam-awsmanpol-AmazonSSMServiceRolePolicy "#security-iam-awsmanpol-AmazonSSMServiceRolePolicy")
- [AWS managed policy:
  AmazonSSMAutomationRole](#security-iam-awsmanpol-AmazonSSMAutomationRole "#security-iam-awsmanpol-AmazonSSMAutomationRole")
- [AWS managed policy:
  AmazonSSMReadOnlyAccess](#security-iam-awsmanpol-AmazonSSMReadOnlyAccess "#security-iam-awsmanpol-AmazonSSMReadOnlyAccess")
- [AWS managed policy: AWSSystemsManagerOpsDataSyncServiceRolePolicy](#security-iam-awsmanpol-AWSSystemsManagerOpsDataSyncServiceRolePolicy "#security-iam-awsmanpol-AWSSystemsManagerOpsDataSyncServiceRolePolicy")
- [AWS
  managed policy: AmazonSSMManagedEC2InstanceDefaultPolicy](#security-iam-awsmanpol-AmazonSSMManagedEC2InstanceDefaultPolicy "#security-iam-awsmanpol-AmazonSSMManagedEC2InstanceDefaultPolicy")
- [AWS managed policy:
  SSMQuickSetupRolePolicy](#security-iam-awsmanpol-SSMQuickSetupRolePolicy "#security-iam-awsmanpol-SSMQuickSetupRolePolicy")
- [AWS managed
  policy: AWSQuickSetupDeploymentRolePolicy](#security-iam-awsmanpol-AWSQuickSetupDeploymentRolePolicy "#security-iam-awsmanpol-AWSQuickSetupDeploymentRolePolicy")
- [AWS managed policy: AWSQuickSetupPatchPolicyDeploymentRolePolicy](#security-iam-awsmanpol-AWSQuickSetupPatchPolicyDeploymentRolePolicy "#security-iam-awsmanpol-AWSQuickSetupPatchPolicyDeploymentRolePolicy")
- [AWS
  managed policy: AWSQuickSetupPatchPolicyBaselineAccess](#security-iam-awsmanpol-AWSQuickSetupPatchPolicyBaselineAccess "#security-iam-awsmanpol-AWSQuickSetupPatchPolicyBaselineAccess")
- [AWS managed policy:
  AWSSystemsManagerEnableExplorerExecutionPolicy](#security-iam-awsmanpol-AWSSystemsManagerEnableExplorerExecutionPolicy "#security-iam-awsmanpol-AWSSystemsManagerEnableExplorerExecutionPolicy")
- [AWS managed policy:
  AWSSystemsManagerEnableConfigRecordingExecutionPolicy](#security-iam-awsmanpol-AWSSystemsManagerEnableConfigRecordingExecutionPolicy "#security-iam-awsmanpol-AWSSystemsManagerEnableConfigRecordingExecutionPolicy")
- [AWS managed policy: AWSQuickSetupDevOpsGuruPermissionsBoundary](#security-iam-awsmanpol-AWSQuickSetupDevOpsGuruPermissionsBoundary "#security-iam-awsmanpol-AWSQuickSetupDevOpsGuruPermissionsBoundary")
- [AWS managed policy: AWSQuickSetupDistributorPermissionsBoundary](#security-iam-awsmanpol-AWSQuickSetupDistributorPermissionsBoundary "#security-iam-awsmanpol-AWSQuickSetupDistributorPermissionsBoundary")
- [AWS managed policy: AWSQuickSetupSSMHostMgmtPermissionsBoundary](#security-iam-awsmanpol-AWSQuickSetupSSMHostMgmtPermissionsBoundary "#security-iam-awsmanpol-AWSQuickSetupSSMHostMgmtPermissionsBoundary")
- [AWS managed policy: AWSQuickSetupPatchPolicyPermissionsBoundary](#security-iam-awsmanpol-AWSQuickSetupPatchPolicyPermissionsBoundary "#security-iam-awsmanpol-AWSQuickSetupPatchPolicyPermissionsBoundary")
- [AWS
  managed policy: AWSQuickSetupSchedulerPermissionsBoundary](#security-iam-awsmanpol-AWSQuickSetupSchedulerPermissionsBoundary "#security-iam-awsmanpol-AWSQuickSetupSchedulerPermissionsBoundary")
- [AWS
  managed policy: AWSQuickSetupCFGCPacksPermissionsBoundary](#security-iam-awsmanpol-AWSQuickSetupCFGCPacksPermissionsBoundary "#security-iam-awsmanpol-AWSQuickSetupCFGCPacksPermissionsBoundary")
- [AWS managed policy: AWSQuickSetupStartStopInstancesExecutionPolicy](#security-iam-awsmanpol-AWSQuickSetupStartStopInstancesExecutionPolicy "#security-iam-awsmanpol-AWSQuickSetupStartStopInstancesExecutionPolicy")
- [AWS managed policy: AWSQuickSetupStartSSMAssociationsExecutionPolicy](#security-iam-awsmanpol-AWSQuickSetupStartSSMAssociationsExecutionPolicy "#security-iam-awsmanpol-AWSQuickSetupStartSSMAssociationsExecutionPolicy")
- [AWS managed policy: AWS-SSM-DiagnosisAutomation-AdministrationRolePolicy](#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-AdministrationRolePolicy "#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-AdministrationRolePolicy")
- [AWS managed policy: AWS-SSM-DiagnosisAutomation-ExecutionRolePolicy](#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-ExecutionRolePolicy "#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-ExecutionRolePolicy")
- [AWS managed policy:
  AWS-SSM-RemediationAutomation-AdministrationRolePolicy](#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-AdministrationRolePolicy "#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-AdministrationRolePolicy")
- [AWS managed policy: AWS-SSM-RemediationAutomation-ExecutionRolePolicy](#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-ExecutionRolePolicy "#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-ExecutionRolePolicy")
- [AWS managed policy: AWSQuickSetupSSMManageResourcesExecutionPolicy](#security-iam-awsmanpol-AWSQuickSetupSSMManageResourcesExecutionPolicy "#security-iam-awsmanpol-AWSQuickSetupSSMManageResourcesExecutionPolicy")
- [AWS managed policy: AWSQuickSetupSSMLifecycleManagementExecutionPolicy](#security-iam-awsmanpol-AWSQuickSetupSSMLifecycleManagementExecutionPolicy "#security-iam-awsmanpol-AWSQuickSetupSSMLifecycleManagementExecutionPolicy")
- [AWS
  managed policy: AWSQuickSetupSSMDeploymentRolePolicy](#security-iam-awsmanpol-AWSQuickSetupSSMDeploymentRolePolicy "#security-iam-awsmanpol-AWSQuickSetupSSMDeploymentRolePolicy")
- [AWS managed policy: AWSQuickSetupSSMDeploymentS3BucketRolePolicy](#security-iam-awsmanpol-AWSQuickSetupSSMDeploymentS3BucketRolePolicy "#security-iam-awsmanpol-AWSQuickSetupSSMDeploymentS3BucketRolePolicy")
- [AWS
  managed policy: AWSQuickSetupEnableDHMCExecutionPolicy](#security-iam-awsmanpol-AWSQuickSetupEnableDHMCExecutionPolicy "#security-iam-awsmanpol-AWSQuickSetupEnableDHMCExecutionPolicy")
- [AWS
  managed policy: AWSQuickSetupEnableAREXExecutionPolicy](#security-iam-awsmanpol-AWSQuickSetupEnableAREXExecutionPolicy "#security-iam-awsmanpol-AWSQuickSetupEnableAREXExecutionPolicy")
- [AWS managed policy: AWSQuickSetupManagedInstanceProfileExecutionPolicy](#security-iam-awsmanpol-AWSQuickSetupManagedInstanceProfileExecutionPolicy "#security-iam-awsmanpol-AWSQuickSetupManagedInstanceProfileExecutionPolicy")
- [AWS managed policy: AWSQuickSetupManageJITNAResourcesExecutionPolicy](#security-iam-awsmanpol-AWSQuickSetupManageJITNAResourcesExecutionPolicy "#security-iam-awsmanpol-AWSQuickSetupManageJITNAResourcesExecutionPolicy")
- [AWS
  managed policy: AWSQuickSetupJITNADeploymentRolePolicy](#security-iam-awsmanpol-AWSQuickSetupJITNADeploymentRolePolicy "#security-iam-awsmanpol-AWSQuickSetupJITNADeploymentRolePolicy")
- [AWS managed policy: AWSSystemsManagerJustInTimeAccessServicePolicy](#security-iam-awsmanpol-AWSSystemsManagerJustInTimeAccessServicePolicy "#security-iam-awsmanpol-AWSSystemsManagerJustInTimeAccessServicePolicy")
- [AWS managed policy: AWSSystemsManagerJustInTimeAccessTokenPolicy](#security-iam-awsmanpol-AWSSystemsManagerJustInTimeAccessTokenPolicy "#security-iam-awsmanpol-AWSSystemsManagerJustInTimeAccessTokenPolicy")
- [AWS managed policy: AWSSystemsManagerJustInTimeAccessTokenSessionPolicy](#security-iam-awsmanpol-AWSSystemsManagerJustInTimeAccessTokenSessionPolicy "#security-iam-awsmanpol-AWSSystemsManagerJustInTimeAccessTokenSessionPolicy")
- [AWS managed policy:
  AWSSystemsManagerJustInTimeNodeAccessRolePropagationPolicy](#security-iam-awsmanpol-AWSSystemsManagerJustInTimeNodeAccessRolePropagationPolicy "#security-iam-awsmanpol-AWSSystemsManagerJustInTimeNodeAccessRolePropagationPolicy")
- [AWS managed policy: AWSSystemsManagerNotificationsServicePolicy](#security-iam-awsmanpol-AWSSystemsManagerNotificationsServicePolicy "#security-iam-awsmanpol-AWSSystemsManagerNotificationsServicePolicy")
- [AWS
  managed policy: AWS-SSM-Automation-DiagnosisBucketPolicy](#security-iam-awsmanpol-AWS-SSM-Automation-DiagnosisBucketPolicy "#security-iam-awsmanpol-AWS-SSM-Automation-DiagnosisBucketPolicy")
- [AWS managed policy:
  AWS-SSM-RemediationAutomation-OperationalAccountAdministrationRolePolicy](#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-OperationalAccountAdministrationRolePolicy "#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-OperationalAccountAdministrationRolePolicy")
- [AWS managed policy:
  AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy](#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy "#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy")
- [Systems Manager updates to AWS managed
  policies](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")
- [Additional managed policies for Systems Manager](#policies-list "#policies-list")

## AWS managed

policy: AmazonSSMServiceRolePolicy

This policy provides access to a number of AWS resources that are managed by
AWS Systems Manager or used in Systems Manager operations.

You can't attach `AmazonSSMServiceRolePolicy` to your AWS Identity and Access Management (IAM)
entities. This policy is attached to a service-linked role that allows AWS Systems Manager to
perform actions on your behalf. For more information, see [Using roles to collect inventory and view OpsData](using-service-linked-roles-service-action-1.md "using-service-linked-roles-service-action-1.md").

**Permissions details**

This policy includes the following permissions.

- `ssm` – Allows principals to start and step executions for
  both Run Command and Automation; and to retrieve information about Run Command and
  Automation operations; to retrieve information about Parameter Store parameters
  Change Calendar calendars; to update and retrieve information about Systems Manager service
  settings for OpsCenterresources; and to read information about tags that have
  have applied to resources.
- `cloudformation` – Allows principals to retrieve information
  about stackset operations and stackset instances, and to delete stacksets on the
  resource
  `arn:aws:cloudformation:*:*:stackset/AWS-QuickSetup-SSM*:*`.
  Allows principals to delete stack instances that are associated with the
  following resources:

```
arn:aws:cloudformation:*:*:stackset/AWS-QuickSetup-SSM*:*
arn:aws:cloudformation:*:*:stackset-target/AWS-QuickSetup-SSM*:*
arn:aws:cloudformation:*:*:type/resource/*
```

- `cloudwatch` – Allows principals to retrieve information
  about Amazon CloudWatch alarms.
- `compute-optimizer` – Allows principals to retrieve the
  enrollment (opt in) status of an account to the AWS Compute Optimizer service, and to
  retrieve recommendations for Amazon EC2 instances that meet a specific set of stated
  requirements.
- `config` – Allows principals to retrieve information
  remediation configurations and configuration recorders in AWS Config, and to
  determine whether specified AWS Config rules and AWS resources are
  compliant.
- `events` – Allows principals retrieve information about EventBridge
  rules; to create EventBridge rules and targets exclusively for the the Systems Manager service
  (`ssm.amazonaws.com`); and to delete rules and
  targets for the resource
  `arn:aws:events:*:*:rule/SSMExplorerManagedRule`.
- `ec2` – Allows principals to retrieve information about
  Amazon EC2 instances..
- `iam` – Allows principals to pass roles permissions for the
  Systems Manager service (`ssm.amazonaws.com`).
- `lambda` – Allows principals to invoke Lambda functions that
  are configured specifically for use by Systems Manager.
- `resource-explorer-2` – Allows principals to retrieve data
  about EC2 instances to determine whether or not each instance is currently
  managed by Systems Manager.

The action `resource-explorer-2:CreateManagedView` is allowed for
the
`arn:aws:resource-explorer-2:*:*:managed-view/AWSManagedViewForSSM*`
resource.

- `resource-groups` – Allows principals to retrieve list
  resource groups and their members from AWS Resource Groups of resources that belong to a
  resource group.
- `securityhub` – Allows principals to retrieve information
  about AWS Security Hub CSPM hub resources in the current account.
- `states` – Allows principals to start and retrieve
  information for AWS Step Functions that are configured specifically for use by
  Systems Manager.
- `support` – Allows principals to retrieve information about
  checks and cases in AWS Trusted Advisor.
- `tag` – Allows principals to retrieve information about all
  the tagged or previously tagged resources that are located in a specified
  AWS Region for an account.

To view more details about the policy, including the latest version of the JSON policy
document, see [AmazonSSMServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonSSMServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonSSMServiceRolePolicy.md") in the _AWS Managed Policy Reference
Guide_.

## AWS managed policy:

AmazonSSMAutomationRole

You can attach the `AmazonSSMAutomationRole` policy to your IAM
identities. This policy provides permissions for the AWS Systems Manager Automation service to run
activities defined within Automation runbooks.

**Permissions details**

This policy includes the following permissions.

- `lambda` – Allows principals to invoke Lambda functions with
  names that begin with "Automation". This is required for Automation runbooks to
  execute Lambda functions as part of their workflow.
- `ec2` – Allows principals to perform various Amazon EC2
  operations including creating, copying, and deregistering images; managing
  snapshots; starting, running, stopping, and terminating instances; managing
  instance status; and creating, deleting, and describing tags. These permissions
  enable Automation runbooks to manage Amazon EC2 resources during execution.
- `cloudformation` – Allows principals to create, describe,
  update, and delete CloudFormation stacks. This enables Automation runbooks to manage
  infrastructure as code through CloudFormation.
- `ssm` – Allows principals to use all Systems Manager actions. This
  comprehensive access is required for Automation runbooks to interact with all
  Systems Manager capabilities.
- `sns` – Allows principals to publish messages to Amazon SNS
  topics with names that begin with "Automation". This enables Automation runbooks
  to send notifications during execution.
- `ssmmessages` – Allows principals to open data channels to
  Systems Manager sessions. This enables Automation runbooks to establish communication
  channels for session-based operations.

To view more details about the policy, including the latest version of the JSON policy
document, see [AmazonSSMAutomationRole](../../../aws-managed-policy/latest/reference/AmazonSSMAutomationRole.md "../../../aws-managed-policy/latest/reference/AmazonSSMAutomationRole.md") in the _AWS Managed Policy Reference
Guide_.

## AWS managed policy:

AmazonSSMReadOnlyAccess

You can attach the `AmazonSSMReadOnlyAccess` policy to your IAM
identities. This policy grants read-only access to AWS Systems Manager API operations including
`Describe*`, `Get*`, and `List*`.

To view more details about the policy, including the latest version of the JSON policy
document, see [AmazonSSMReadOnlyAccess](../../../aws-managed-policy/latest/reference/AmazonSSMReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AmazonSSMReadOnlyAccess.md") in the _AWS Managed Policy Reference
Guide_.

## AWS managed policy: AWSSystemsManagerOpsDataSyncServiceRolePolicy

You can't attach `AWSSystemsManagerOpsDataSyncServiceRolePolicy` to your
IAM entities. This policy is attached to a service-linked role that allows
Systems Manager to perform actions on your behalf. For more information, see [Using roles to create OpsData and OpsItems for Explorer](using-service-linked-roles-service-action-3.md "using-service-linked-roles-service-action-3.md").

`AWSSystemsManagerOpsDataSyncServiceRolePolicy` allows the
`AWSServiceRoleForSystemsManagerOpsDataSync` service-linked role to
create and update OpsItems and OpsData from AWS Security Hub CSPM findings.

The policy allows Systems Manager to complete the following actions on all related
resources (`"Resource": "*"`), except where indicated:

- `ssm:GetOpsItem` [1]
- `ssm:UpdateOpsItem` [1]
- `ssm:CreateOpsItem`
- `ssm:AddTagsToResource` [2]
- `ssm:UpdateServiceSetting` [3]
- `ssm:GetServiceSetting` [3]
- `securityhub:GetFindings`
- `securityhub:GetFindings`
- `securityhub:BatchUpdateFindings` [4]

[1] The `ssm:GetOpsItem` and `ssm:UpdateOpsItem` actions are
allowed permissions by the following condition for the Systems Manager service
only.

```
"Condition": {
    "StringEquals": {
        "aws:ResourceTag/ExplorerSecurityHubOpsItem": "true"
    }
}
```

[2] The `ssm:AddTagsToResource` action is allowed permissions for the
following resource only.

```
arn:aws:ssm:*:*:opsitem/*
```

[3] The `ssm:UpdateServiceSetting` and `ssm:GetServiceSetting`
actions are allowed permissions for the following resources only.

```
arn:aws:ssm:*:*:servicesetting/ssm/opsitem/*
arn:aws:ssm:*:*:servicesetting/ssm/opsdata/*
```

[4] The `securityhub:BatchUpdateFindings` are denied permissions by the
following condition for the Systems Manager service only.

```
{
			"Effect": "Deny",
			"Action": "securityhub:BatchUpdateFindings",
			"Resource": "*",
			"Condition": {
				"StringEquals": {
					"securityhub:ASFFSyntaxPath/Workflow.Status": "SUPPRESSED"
				}
			}
		},
		{
			"Effect": "Deny",
			"Action": "securityhub:BatchUpdateFindings",
			"Resource": "*",
			"Condition": {
				"Null": {
					"securityhub:ASFFSyntaxPath/Confidence": false
				}
			}
		},
		{
			"Effect": "Deny",
			"Action": "securityhub:BatchUpdateFindings",
			"Resource": "*",
			"Condition": {
				"Null": {
					"securityhub:ASFFSyntaxPath/Criticality": false
				}
			}
		},
		{
			"Effect": "Deny",
			"Action": "securityhub:BatchUpdateFindings",
			"Resource": "*",
			"Condition": {
				"Null": {
					"securityhub:ASFFSyntaxPath/Note.Text": false
				}
			}
		},
		{
			"Effect": "Deny",
			"Action": "securityhub:BatchUpdateFindings",
			"Resource": "*",
			"Condition": {
				"Null": {
					"securityhub:ASFFSyntaxPath/Note.UpdatedBy": false
				}
			}
		},
		{
			"Effect": "Deny",
			"Action": "securityhub:BatchUpdateFindings",
			"Resource": "*",
			"Condition": {
				"Null": {
					"securityhub:ASFFSyntaxPath/RelatedFindings": false
				}
			}
		},
		{
			"Effect": "Deny",
			"Action": "securityhub:BatchUpdateFindings",
			"Resource": "*",
			"Condition": {
				"Null": {
					"securityhub:ASFFSyntaxPath/Types": false
				}
			}
		},
		{
			"Effect": "Deny",
			"Action": "securityhub:BatchUpdateFindings",
			"Resource": "*",
			"Condition": {
				"Null": {
					"securityhub:ASFFSyntaxPath/UserDefinedFields.key": false
				}
			}
		},
		{
			"Effect": "Deny",
			"Action": "securityhub:BatchUpdateFindings",
			"Resource": "*",
			"Condition": {
				"Null": {
					"securityhub:ASFFSyntaxPath/UserDefinedFields.value": false
				}
			}
		},
		{
			"Effect": "Deny",
			"Action": "securityhub:BatchUpdateFindings",
			"Resource": "*",
			"Condition": {
				"Null": {
					"securityhub:ASFFSyntaxPath/VerificationState": false
				}
			}
```

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSSystemsManagerOpsDataSyncServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSSystemsManagerOpsDataSyncServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSSystemsManagerOpsDataSyncServiceRolePolicy.md") in the _AWS
Managed Policy Reference Guide_.

## AWS

managed policy: AmazonSSMManagedEC2InstanceDefaultPolicy

You should only attach `AmazonSSMManagedEC2InstanceDefaultPolicy` to IAM
roles for Amazon EC2 instances that you want to have permission to use Systems Manager
functionality. You shouldn't attached this role to other IAM entities, such as IAM
users and IAM groups, or to IAM roles that serve other purposes. For more
information, see [Managing EC2
instances automatically with Default Host Management Configuration](fleet-manager-default-host-management-configuration.md "fleet-manager-default-host-management-configuration.md").

This policy grants permissions that allow SSM Agent on your Amazon EC2 instance to
communicate with the Systems Manager service in the cloud in order to perform a variety of tasks.
It also grants permissions for the two services that provide authorization tokens to
ensure that operations are performed on the correct instance.

**Permissions details**

This policy includes the following permissions.

- `ssm` – Allows principals to retrieve Documents, execute
  commands using Run Command, establish sessions using Session Manager, collect an inventory
  of the instance, and scan for patches and patch compliance using
  Patch Manager.
- `ssmmessages` – Allows principals to access, for each
  instance, a personalized authorization token that was created by the _[Amazon Message Gateway Service](../../../service-authorization/latest/reference/list_amazonmessagegatewayservice.md "../../../service-authorization/latest/reference/list_amazonmessagegatewayservice.md")_. Systems Manager validates the
  personalized authorization token against the Amazon Resource Name (ARN) of the
  instance that was provided in the API operation. This access is necessary to
  ensure that SSM Agent performs the API operations on the correct instance.
- `ec2messages` – Allows principals to access, for each
  instance, a personalized authorization token that was created by the _[Amazon Message Delivery Service](../../../service-authorization/latest/reference/list_amazonmessagegatewayservice.md "../../../service-authorization/latest/reference/list_amazonmessagegatewayservice.md")_. Systems Manager validates the
  personalized authorization token against the Amazon Resource Name (ARN) of the
  instance that was provided in the API operation. This access is necessary to
  ensure that SSM Agent performs the API operations on the correct instance.

For related information about the `ssmmessages` and
`ec2messages` endpoints, including the differences between the two, see
[Agent-related API operations
(ssmmessages and ec2messages endpoints)](systems-manager-setting-up-messageAPIs.md#message-services "systems-manager-setting-up-messageAPIs.md#message-services").

To view more details about the policy, including the latest version of the JSON policy
document, see [AmazonSSMManagedEC2InstanceDefaultPolicy](../../../aws-managed-policy/latest/reference/AmazonSSMManagedEC2InstanceDefaultPolicy.md "../../../aws-managed-policy/latest/reference/AmazonSSMManagedEC2InstanceDefaultPolicy.md") in the _AWS Managed
Policy Reference Guide_.

## AWS managed policy:

SSMQuickSetupRolePolicy

You can't attach SSMQuickSetupRolePolicy to your IAM entities. This policy is
attached to a service-linked role that allows Systems Manager to perform actions on your
behalf. For more information, see [Using roles to maintain Quick Setup-provisioned resource health and consistency](using-service-linked-roles-service-action-5.md "using-service-linked-roles-service-action-5.md").

This policy grants read-only
permissions that allow Systems Manager to check configuration health, ensure consistent use of
parameters and provisioned resources, and remediate resources when drift is detected. It
also grants administrative permissions for creating a service-linked role.

**Permissions details**

This policy includes the following permissions.

- `ssm` – Allows principals to read information Resource Data
  Syncs and SSM Documents in Systems Manager, including in delegated administrator
  accounts. This is required so Quick Setup can determine the state that configured
  resources are intended to be in.
- `organizations` – Allows principals to read information
  about the member accounts that belong to an organization as configured in
  AWS Organizations. This is required so Quick Setup can identify all accounts in an
  organization where resource health checks are to be performed.
- `cloudformation` – Allows principals to read information
  from CloudFormation. This is required so Quick Setup can gather data about the CloudFormation stacks
  used to manage the state of resources and CloudFormation stackset operations.

To view more details about the policy, including the latest version of the JSON policy
document, see [SSMQuickSetupRolePolicy](../../../aws-managed-policy/latest/reference/SSMQuickSetupRolePolicy.md "../../../aws-managed-policy/latest/reference/SSMQuickSetupRolePolicy.md") in the _AWS Managed Policy Reference
Guide_.

## AWS managed

policy: AWSQuickSetupDeploymentRolePolicy

The managed policy `AWSQuickSetupDeploymentRolePolicy` supports
multiple Quick Setup configuration types. These configuration types create IAM roles and
automations that configure frequently used Amazon Web Services services and features with
recommended best practices.

You can attach `AWSQuickSetupDeploymentRolePolicy` to your IAM
entities.

This policy grants administrative permissions needed to create resources associated
with the following Quick Setup configurations:

- [Set up Amazon EC2 host management using
  Quick Setup](quick-setup-host-management.md "quick-setup-host-management.md")
- [Create an AWS Config configuration recorder
  using Quick Setup](quick-setup-config.md "quick-setup-config.md")
- [Deploy AWS Config conformance pack using
  Quick Setup](quick-setup-cpack.md "quick-setup-cpack.md")
- [Set up DevOps Guru using Quick Setup](quick-setup-devops.md "quick-setup-devops.md")
- [Deploy Distributor packages using
  Quick Setup](quick-setup-distributor.md "quick-setup-distributor.md")
- [Stop and start EC2 instances automatically
  on a schedule using Quick Setup](quick-setup-scheduler.md "quick-setup-scheduler.md")

**Permissions details**

This policy includes the following permissions.

- `ssm` – Allows principals to read, create, update, and
  delete SSM documents with names beginning with "AWSQuickSetup-" or
  "AWSOperationsPack-" when called via CloudFormation; to read specific AWS owned
  documents including "AWSQuickSetupType-ManageInstanceProfile",
  "AWSQuickSetupType-ConfigureDevOpsGuru", and "AWSQuickSetupType-DeployConformancePack";
  to create, update, and delete associations for Quick Setup documents and AWS owned documents
  when called via CloudFormation; and to clean up legacy resources tagged with
  `QuickSetupID`. This enables Quick Setup to deploy and manage
  automation workflows and associations.
- `cloudformation` – Allows principals to read information
  about CloudFormation stacks and stack sets; and to create, update, and delete CloudFormation
  stacks and change sets for resources with names beginning with
  "StackSet-AWS-QuickSetup-". This enables Quick Setup to manage infrastructure
  deployments across accounts and regions.
- `config` – Allows principals to read information about
  AWS Config conformance packs and their status; and to create and delete
  conformance packs with names beginning with "AWS-QuickSetup-" when called via
  CloudFormation. This enables Quick Setup to deploy compliance monitoring
  configurations.
- `events` – Allows principals to manage EventBridge rules and
  targets for resources with names containing "QuickSetup-". This enables Quick Setup
  to create scheduled automation workflows.
- `iam` – Allows principals to create service-linked roles for
  AWS Config and Systems Manager; to create, manage, and delete IAM roles with names
  beginning with "AWS-QuickSetup-" or "AWSOperationsPack-" when called via CloudFormation;
  to pass these roles to Systems Manager and EventBridge services; to attach specific AWS managed
  policies to these roles; and to set permissions boundaries using specific
  Quick Setup managed policies. This enables Quick Setup to create the necessary service
  roles for its operations.
- `resource-groups` – Allows principals to retrieve resource
  group queries. This enables Quick Setup to target specific sets of resources for
  configuration management.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSQuickSetupDeploymentRolePolicy](../../../aws-managed-policy/latest/reference/AWSQuickSetupDeploymentRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSQuickSetupDeploymentRolePolicy.md") in the _AWS Managed Policy
Reference Guide_.

## AWS managed policy: AWSQuickSetupPatchPolicyDeploymentRolePolicy

The managed policy `AWSQuickSetupPatchPolicyDeploymentRolePolicy`
supports the [Configure patching for instances in an
organization using a Quick Setup patch policy](quick-setup-patch-manager.md "quick-setup-patch-manager.md") Quick Setup type. This configuration type
helps automate patching of applications and nodes in a single account or across your
organization.

You can attach `AWSQuickSetupPatchPolicyDeploymentRolePolicy` to
your IAM entities. Systems Manager also attaches this policy to a service role that allows
Systems Manager to perform actions on your behalf.

This policy grants administrative permissions that allow Quick Setup to create resources
associated with a patch policy configuration.

**Permissions details**

This policy includes the following permissions.

- `iam` – Allows principals to manage and delete IAM roles
  required for Automation configuration tasks; and to manage Automation role
  policies.
- `cloudformation` – Allows principals to read CloudFormation stack
  information; and to control CloudFormation stacks that were created by Quick Setup using
  CloudFormation stack sets.
- `ssm` – Allows principals to create, update, read, and
  delete Automation runbooks required for configuration tasks; and to create,
  update, and delete State Manager associations.

- `resource-groups` – Allows principals to retrieve resource
  queries that are associated with resource groups targeted by Quick Setup
  configurations.

- `s3` – Allows principals to list Amazon S3 buckets; and to manage
  the buckets for storing patch policy access logs.
- `lambda` – Allows principals to manage AWS Lambda remediation
  functions that maintain configurations in the correct state.
- `logs` – Allows principals to describe and manage log groups
  for Lambda configuration resources.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSQuickSetupPatchPolicyDeploymentRolePolicy](../../../aws-managed-policy/latest/reference/AWSQuickSetupPatchPolicyDeploymentRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSQuickSetupPatchPolicyDeploymentRolePolicy.md") in the _AWS Managed
Policy Reference Guide_.

## AWS

managed policy: AWSQuickSetupPatchPolicyBaselineAccess

The managed policy `AWSQuickSetupPatchPolicyBaselineAccess`
supports the [Configure patching for instances in an
organization using a Quick Setup patch policy](quick-setup-patch-manager.md "quick-setup-patch-manager.md") Quick Setup type. This configuration type
helps automate patching of applications and nodes in a single account or across your
organization.

You can attach `AWSQuickSetupPatchPolicyBaselineAccess` to your
IAM entities. Systems Manager also attaches this policy to a service role that allows
Systems Manager to perform actions on your behalf.

This policy provides read-only permissions to access patch baselines that have been
configured by an administrator in the current AWS account or organization using
Quick Setup. The patch baselines are stored in an Amazon S3 bucket and can be used for patching
instances in a single account or across an entire organization.

**Permissions details**

This policy includes the following permission.

- `s3` – Allows principals to read patch baseline overrides
  stored in Amazon S3 buckets.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSQuickSetupPatchPolicyBaselineAccess](../../../aws-managed-policy/latest/reference/AWSQuickSetupPatchPolicyBaselineAccess.md "../../../aws-managed-policy/latest/reference/AWSQuickSetupPatchPolicyBaselineAccess.md") in the _AWS Managed
Policy Reference Guide_.

## AWS managed policy:

`AWSSystemsManagerEnableExplorerExecutionPolicy`

The managed policy `AWSSystemsManagerEnableExplorerExecutionPolicy`
supports enabling Explorer, a tool in AWS Systems Manager.

You can attach `AWSSystemsManagerEnableExplorerExecutionPolicy` to
your IAM entities. Systems Manager also attaches this policy to a service role that allows
Systems Manager to perform actions on your behalf.

This policy grants administrative permissions for enabling Explorer. This includes
permissions to update related Systems Manager service settings, and to create a service-linked
role for Systems Manager.

**Permissions details**

This policy includes the following permissions.

- `config` – Allows principals to help enable Explorer by
  providing read-only access to configuration recorder details.
- `iam` – Allows principals to help enable Explorer.
- `ssm` – Allows principals to start an Automation workflow
  that enables Explorer.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSSystemsManagerEnableExplorerExecutionPolicy](../../../aws-managed-policy/latest/reference/AWSSystemsManagerEnableExplorerExecutionPolicy.md "../../../aws-managed-policy/latest/reference/AWSSystemsManagerEnableExplorerExecutionPolicy.md") in the _AWS
Managed Policy Reference Guide_.

## AWS managed policy:

`AWSSystemsManagerEnableConfigRecordingExecutionPolicy`

The managed policy
`AWSSystemsManagerEnableConfigRecordingExecutionPolicy` supports
the [Create an AWS Config configuration recorder
using Quick Setup](quick-setup-config.md "quick-setup-config.md") Quick Setup
configuration type. This configuration type enables Quick Setup to track and record changes
to the AWS resource types you choose for AWS Config. It also enables Quick Setup to configure
delivery and notifications options for the recorded data.

You can attach
`AWSSystemsManagerEnableConfigRecordingExecutionPolicy` to your
IAM entities. Systems Manager also attaches this policy to a service role that allows
Systems Manager to perform actions on your behalf.

This policy grants administrative permissions that allow Quick Setup to enable and
configure AWS Config configuration recording.

**Permissions details**

This policy includes the following permissions.

- `s3` – Allows principals to create and configure Amazon S3
  buckets for delivery of configuration recordings.
- `sns` – Allows principals to list and create Amazon SNS
  topics.
- `config` – Allows principals to configure and start the
  configuration recorder; and to help enable Explorer.
- `iam` – Allows principals to create, get, and pass a
  service-linked role for AWS Config; and to create a service-linked role for Systems Manager;
  and to help enable Explorer.
- `ssm` – Allows principals to start an Automation workflow
  that enables Explorer.
- `compute-optimizer` – Allows principals to help enable
  Explorer by providing read-only access to determine whether a resource is
  enrolled with AWS Compute Optimizer.
- `support` – Allows principals to help enable Explorer by
  providing read-only access to determine whether a resource is enrolled with
  AWS Compute Optimizer.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSSystemsManagerEnableConfigRecordingExecutionPolicy](../../../aws-managed-policy/latest/reference/AWSSystemsManagerEnableConfigRecordingExecutionPolicy.md "../../../aws-managed-policy/latest/reference/AWSSystemsManagerEnableConfigRecordingExecutionPolicy.md") in the
_AWS Managed Policy Reference Guide_.

## AWS managed policy: AWSQuickSetupDevOpsGuruPermissionsBoundary

###### Note

This policy is a _permissions boundary_. A
permissions boundary sets the maximum permissions that an identity-based policy can
grant to an IAM entity. You should not use and attach Quick Setup permissions
boundary policies on your own. Quick Setup permissions boundary policies should only be
attached to Quick Setup managed roles. For more information about permissions
boundaries, see [Permissions
boundaries for IAM entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") in the
_IAM User Guide_.

The managed policy `AWSQuickSetupDevOpsGuruPermissionsBoundary`
supports the [Set up DevOps Guru using Quick Setup](quick-setup-devops.md "quick-setup-devops.md")
type. The configuration type enables the machine learning-powered Amazon DevOps Guru. The DevOps Guru
service can help improve an application’s operational performance and availability.

When you create an `AWSQuickSetupDevOpsGuruPermissionsBoundary`
configuration using Quick Setup, the system applies this permissions boundary to the IAM
roles that are created when the configuration is deployed. The permissions boundary
limits the scope of the roles that Quick Setup creates.

This policy grants administrative permissions that allow Quick Setup to enable and
configure Amazon DevOps Guru.

**Permissions details**

This policy includes the following permissions.

- `iam` – Allows principals to create service-linked roles for
  DevOps Guru and Systems Manager; and to list roles that help enable Explorer.
- `cloudformation` – Allows principals to list and describe
  CloudFormation stacks.
- `sns` – Allows principals to list and create Amazon SNS
  topics.
- `devops-guru` – Allows principals to configure DevOps Guru; and to
  add a notification channel.
- `config` – – Allows principals to help enable
  Explorer by providing read-only access to configuration recorder details.
- `ssm` – Allows principals to start an Automation workflow
  that enables Explorer; and to read and update Explorer service settings.
- `compute-optimizer` – Allows principals to help enable
  Explorer by providing read-only access to determine whether a resource is
  enrolled with AWS Compute Optimizer.
- `support` – Allows principals to help enable Explorer by
  providing read-only access to determine whether a resource is enrolled with
  AWS Compute Optimizer.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSQuickSetupDevOpsGuruPermissionsBoundary](../../../aws-managed-policy/latest/reference/AWSQuickSetupDevOpsGuruPermissionsBoundary.md "../../../aws-managed-policy/latest/reference/AWSQuickSetupDevOpsGuruPermissionsBoundary.md") in the _AWS Managed
Policy Reference Guide_.

## AWS managed policy: AWSQuickSetupDistributorPermissionsBoundary

###### Note

This policy is a _permissions boundary_. A
permissions boundary sets the maximum permissions that an identity-based policy can
grant to an IAM entity. You should not use and attach Quick Setup permissions
boundary policies on your own. Quick Setup permissions boundary policies should only be
attached to Quick Setup managed roles. For more information about permissions
boundaries, see [Permissions
boundaries for IAM entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") in the
_IAM User Guide_.

The managed policy `AWSQuickSetupDistributorPermissionsBoundary`
supports the [Deploy Distributor packages using
Quick Setup](quick-setup-distributor.md "quick-setup-distributor.md") Quick Setup configuration type. The
configuration type helps enable the distribution of software packages, such as agents,
to your Amazon Elastic Compute Cloud (Amazon EC2) instances, using Distributor, a tool in AWS Systems Manager.

When you create an `AWSQuickSetupDistributorPermissionsBoundary`
configuration using Quick Setup, the system applies this permissions boundary to the IAM
roles that are created when the configuration is deployed. The permissions boundary
limits the scope of the roles that Quick Setup creates.

This policy grants administrative permissions that allow Quick Setup to enable the
distribution of software packages, such as agents, to your Amazon EC2 instances using
Distributor.

**Permissions details**

This policy includes the following permissions.

- `iam` – Allows principals to get and pass the Distributor
  automation role; to create, read, update, and delete the default instance role;
  to pass the default instance role to Amazon EC2 and Systems Manager; to attach instance
  management policies to instance roles; to create a service-linked role for
  Systems Manager; to add the default instance role to instance profiles; to read
  information about IAM roles and instance profiles; and to create the default
  instance profile.
- `ec2` – Allows principals to associate the default instance
  profile with EC2 instances; and to help enable Explorer.
- `ssm` – Allows principals to start automation workflows that
  which configure instances and install packages; and to help start the automation
  workflow that enables Explorer; and to read and update Explorer service
  settings.
- `config` – Allows principals to help enable Explorer by
  providing read-only access to configuration recorder details.
- `compute-optimizer` – Allows principals to help enable
  Explorer by providing read-only access to determine whether a resource is
  enrolled with AWS Compute Optimizer.
- `support` – Allows principals to help enable Explorer by
  providing read-only access to determine whether a resource is enrolled with
  AWS Compute Optimizer.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSQuickSetupDistributorPermissionsBoundary](../../../aws-managed-policy/latest/reference/AWSQuickSetupDistributorPermissionsBoundary.md "../../../aws-managed-policy/latest/reference/AWSQuickSetupDistributorPermissionsBoundary.md") in the _AWS Managed
Policy Reference Guide_.

## AWS managed policy: AWSQuickSetupSSMHostMgmtPermissionsBoundary

###### Note

This policy is a _permissions boundary_. A
permissions boundary sets the maximum permissions that an identity-based policy can
grant to an IAM entity. You should not use and attach Quick Setup permissions
boundary policies on your own. Quick Setup permissions boundary policies should only be
attached to Quick Setup managed roles. For more information about permissions
boundaries, see [Permissions
boundaries for IAM entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") in the
_IAM User Guide_.

The managed policy `AWSQuickSetupSSMHostMgmtPermissionsBoundary`
supports the [Set up Amazon EC2 host management using
Quick Setup](quick-setup-host-management.md "quick-setup-host-management.md") Quick Setup configuration type. This
configuration type configures IAM roles and enables commonly used Systems Manager tools to
securely manage your Amazon EC2 instances.

When you create an `AWSQuickSetupSSMHostMgmtPermissionsBoundary`
configuration using Quick Setup, the system applies this permissions boundary to the IAM
roles that are created when the configuration is deployed. The permissions boundary
limits the scope of the roles that Quick Setup creates.

This policy grants administrative permissions that allow Quick Setup to enable and
configure Systems Manager tools needed for securely managing EC2 instances.

**Permissions details**

This policy includes the following permissions.

- `iam` – Allows principals to get and pass the service role
  to Automation. Allows principals to create, read, update, and delete the default
  instance role; to pass the default instance role to Amazon EC2 and Systems Manager;
  to attach instance management policies to instance roles; to create a
  service-linked role for Systems Manager; to add the default instance role to
  instance profiles; to read information about IAM roles and instance profiles;
  and to create the default instance profile.
- `ec2` – Allows principals to associate and disassociate the
  default instance profile with EC2 instances.
- `ssm` – Allows principals to start Automation workflows that
  enable Explorer; to read and update Explorer service settings; to configure
  instances; and to enable Systems Manager tools on instances.
- `compute-optimizer` – Allows principals to help enable
  Explorer by providing read-only access to determine whether a resource is
  enrolled with AWS Compute Optimizer.
- `support` – Allows principals to help enable Explorer by
  providing read-only access to determine whether a resource is enrolled with
  AWS Compute Optimizer.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSQuickSetupSSMHostMgmtPermissionsBoundary](../../../aws-managed-policy/latest/reference/AWSQuickSetupSSMHostMgmtPermissionsBoundary.md "../../../aws-managed-policy/latest/reference/AWSQuickSetupSSMHostMgmtPermissionsBoundary.md") in the _AWS Managed
Policy Reference Guide_.

## AWS managed policy: AWSQuickSetupPatchPolicyPermissionsBoundary

###### Note

This policy is a _permissions boundary_. A
permissions boundary sets the maximum permissions that an identity-based policy can
grant to an IAM entity. You should not use and attach Quick Setup permissions
boundary policies on your own. Quick Setup permissions boundary policies should only be
attached to Quick Setup managed roles. For more information about permissions
boundaries, see [Permissions
boundaries for IAM entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") in the
_IAM User Guide_.

The managed policy `AWSQuickSetupPatchPolicyPermissionsBoundary`
supports the [Configure patching for instances in an
organization using a Quick Setup patch policy](quick-setup-patch-manager.md "quick-setup-patch-manager.md") Quick Setup type. This configuration type
helps automate patching of applications and nodes in a single account or across your
organization.

When you create an `AWSQuickSetupPatchPolicyPermissionsBoundary`
configuration using Quick Setup, the system applies this permissions boundary to the IAM
roles that are created when the configuration is deployed. The permissions boundary
limits the scope of the roles that Quick Setup creates.

This policy grants administrative permissions that allow Quick Setup to enable and
configure patch policies in Patch Manager, a tool in AWS Systems Manager.

**Permissions details**

This policy includes the following permissions.

- `iam` – Allows principals to get the Patch Manager Automation
  role; to pass Automation roles to Patch Manager patching operations; to create the
  default instance role, `AmazonSSMRoleForInstancesQuickSetup`; to pass
  the default instance role to Amazon EC2 and Systems Manager; to attach selected AWS managed
  policies to the instance role; to create a service-linked role for Systems Manager; to add
  the default instance role to instance profiles; to read information about
  instance profiles and roles; to create a default instance profile; and to tag
  roles that have permissions to read patch baseline overrides.
- `ssm` – Allows principals to update the instance role this
  is managed by Systems Manager; to manage associations created by Patch Manager patch policies
  created in Quick Setup; to tag instances targeted by a patch policy configuration;
  to read information about instances and patching status; to start Automation
  workflows that configure, enable and remediate instance patching; to start
  automation workflows that enable Explorer; to help enable Explorer; and to read
  and update Explorer service settings.
- `ec2` – Allows principals to associate and disassociate the
  default instance profile with EC2 instances; to tag instances targeted by a
  patch policy configuration; to tag instances targeted by a patch policy
  configuration; and to help enable Explorer.
- `s3` – Allows principals to create and configure S3 buckets
  to store patch baseline overrides.
- `lambda` – Allows principals to invoke AWS Lambda functions
  that configure patching and to perform clean-up operations after a Quick Setup
  patch policy configuration is deleted.
- `logs` – Allows principals to configure logging for Patch Manager
  Quick Setup AWS Lambda functions.
- `config` – Allows principals to help enable Explorer by
  providing read-only access to configuration recorder details.
- `compute-optimizer` – Allows principals to help enable
  Explorer by providing read-only access to determine whether a resource is
  enrolled with AWS Compute Optimizer.
- `support` – Allows principals to help enable Explorer by
  providing read-only access to determine whether a resource is enrolled with
  AWS Compute Optimizer.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSQuickSetupPatchPolicyPermissionsBoundary](../../../aws-managed-policy/latest/reference/AWSQuickSetupPatchPolicyPermissionsBoundary.md "../../../aws-managed-policy/latest/reference/AWSQuickSetupPatchPolicyPermissionsBoundary.md") in the _AWS Managed
Policy Reference Guide_.

## AWS

managed policy: AWSQuickSetupSchedulerPermissionsBoundary

###### Note

This policy is a _permissions boundary_. A
permissions boundary sets the maximum permissions that an identity-based policy can
grant to an IAM entity. You should not use and attach Quick Setup permissions
boundary policies on your own. Quick Setup permissions boundary policies should only be
attached to Quick Setup managed roles. For more information about permissions
boundaries, see [Permissions
boundaries for IAM entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") in the
_IAM User Guide_.

The managed policy `AWSQuickSetupSchedulerPermissionsBoundary`
supports the [Stop and start EC2 instances automatically
on a schedule using Quick Setup](quick-setup-scheduler.md "quick-setup-scheduler.md") Quick Setup configuration type. This configuration type lets you stop and start your EC2
instances and other resources at the times you specify.

When you create an `AWSQuickSetupSchedulerPermissionsBoundary`
configuration using Quick Setup, the system applies this permissions boundary to the IAM
roles that are created when the configuration is deployed. The permissions boundary
limits the scope of the roles that Quick Setup creates.

This policy grants administrative permissions that allow Quick Setup to enable and
configure scheduled operations on EC2 instances and other resources.

**Permissions details**

This policy includes the following permissions.

- `iam` – Allows principals to retrieve and pass roles for
  instance management automation actions; to manage, pass, and attach default
  instance roles for EC2 instance management; to create default instance profiles;
  to add default instance roles to instance profiles; to create a service-linked
  role for Systems Manager; to read information about IAM roles and instance profiles;
  to associate a default instance profile with EC2 instances; and to start
  Automation workflows to configure instances and enable Systems Manager tools on
  them.
- `ssm` – Allows principals to start Automation workflows that
  enable Explorer; and to read and update Explorer service settings.
- ec2 – Allows principals to locate targeted instances and to start and
  stop them on a schedule.
- `config` – Allows principals to help enable Explorer by
  providing read-only access to configuration recorder details.
- `compute-optimizer` – Allows principals to help enable
  Explorer by providing read-only access to determine whether a resource is
  enrolled with AWS Compute Optimizer.
- `support` – Allows principals to help enable Explorer by
  providing read-only access to AWS Trusted Advisor checks for an account.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSQuickSetupSchedulerPermissionsBoundary](../../../aws-managed-policy/latest/reference/AWSQuickSetupSchedulerPermissionsBoundary.md "../../../aws-managed-policy/latest/reference/AWSQuickSetupSchedulerPermissionsBoundary.md") in the _AWS Managed
Policy Reference Guide_.

## AWS

managed policy: AWSQuickSetupCFGCPacksPermissionsBoundary

###### Note

This policy is a _permissions boundary_. A
permissions boundary sets the maximum permissions that an identity-based policy can
grant to an IAM entity. You should not use and attach Quick Setup permissions
boundary policies on your own. Quick Setup permissions boundary policies should only be
attached to Quick Setup managed roles. For more information about permissions
boundaries, see [Permissions
boundaries for IAM entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") in the
_IAM User Guide_.

The managed policy
`AWSQuickSetupCFGCPacksPermissionsBoundary`supports the [Deploy AWS Config conformance pack using
Quick Setup](quick-setup-cpack.md "quick-setup-cpack.md") Quick Setup
configuration type. This configuration type deploys AWS Config conformance packs.
Conformance packs are collections of AWS Config rules and remediation actions that can be
deployed as a single entity.

When you create an `AWSQuickSetupCFGCPacksPermissionsBoundary`
configuration using Quick Setup, the system applies this permissions boundary to the IAM
roles that are created when the configuration is deployed. The permissions boundary
limits the scope of the roles that Quick Setup creates.

This policy grants administrative permissions that allow Quick Setup to deploy AWS Config
conformance packs.

**Permissions details**

This policy includes the following permissions.

- `iam` – Allows principals to create, get, and pass a
  service-linked role for AWS Config.
- `sns` – Allows principals to list platform applications in
  Amazon SNS.
- `config` – Allows principals to deploy AWS Config conformance
  packs; to get the status of conformance packs; and to get information about
  configuration recorders.
- `ssm` – Allows principals to get information about SSM
  documents and Automation workflows; to get information about resource tags; and
  to get information about and update service settings.
- `compute-optimizer` – Allows principals to get the opt-in
  status of an account.
- `support` – Allows principals to get information about
  AWS Trusted Advisor checks.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSQuickSetupCFGCPacksPermissionsBoundary](../../../aws-managed-policy/latest/reference/AWSQuickSetupCFGCPacksConfigurationPolicy.md "../../../aws-managed-policy/latest/reference/AWSQuickSetupCFGCPacksConfigurationPolicy.md") in the _AWS Managed
Policy Reference Guide_.

## AWS managed policy: AWSQuickSetupStartStopInstancesExecutionPolicy

You can attach `AWSQuickSetupStartStopInstancesExecutionPolicy` to your
IAM entities. This policy provides permissions for Quick Setup to manage the starting and
stopping of Amazon EC2 instances using Systems Manager automation.

**Permissions details**

This policy includes the following permissions.

- `ec2` – Allows principals to describe Amazon EC2 instances, their
  status, regions, and tags. Also allows starting and stopping specific Amazon EC2
  instances.
- `ssm` – Allows principals to get calendar state from
  Quick Setup change calendars, start associations, and execute automation documents
  for instance scheduling.
- `iam` – Allows principals to pass Quick Setup IAM roles to
  Systems Manager for automation execution, with conditions that restrict the service to
  ssm.amazonaws.com and specific resource ARNs.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSQuickSetupStartStopInstancesExecutionPolicy](../../../aws-managed-policy/latest/reference/AWSQuickSetupStartStopInstancesExecutionPolicy.md "../../../aws-managed-policy/latest/reference/AWSQuickSetupStartStopInstancesExecutionPolicy.md") in the _AWS
Managed Policy Reference Guide_.

## AWS managed policy: AWSQuickSetupStartSSMAssociationsExecutionPolicy

This policy grants permissions that allow Quick Setup to run the
`AWSQuickSetupType-Scheduler-ChangeCalendarState` Automation runbook.
This runbook is used to manage change calendar states for scheduled operations in
Quick Setup configurations.

You can attach `AWSQuickSetupStartSSMAssociationsExecutionPolicy` to your
IAM entities. Systems Manager also attaches this policy to a service role that allows
Systems Manager to perform actions on your behalf.

**Permissions details**

This policy includes the following permissions.

- `ssm` – Allows principals to start automation executions
  specifically for the
  `AWSQuickSetupType-Scheduler-ChangeCalendarState` document. This
  is required for Quick Setup to manage change calendar states for scheduled
  operations.
- `iam` – Allows principals to pass roles with names that
  begin with "AWS-QuickSetup-" to the Systems Manager service. This permission is restricted
  to use with specific SSM documents related to change calendar management. This
  is required for Quick Setup to pass the appropriate execution role to the
  automation process.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSQuickSetupStartSSMAssociationsExecutionPolicy](../../../aws-managed-policy/latest/reference/AWSQuickSetupStartSSMAssociationsExecutionPolicy.md "../../../aws-managed-policy/latest/reference/AWSQuickSetupStartSSMAssociationsExecutionPolicy.md") in the _AWS
Managed Policy Reference Guide_.

## AWS managed policy: AWS-SSM-DiagnosisAutomation-AdministrationRolePolicy

The policy `AWS-SSM-DiagnosisAutomation-AdministrationRolePolicy` provides
permissions for diagnosing issues with nodes that interact with Systems Manager services by
starting Automation workflows in accounts and Regions where nodes are managed.

You can attach `AWS-SSM-DiagnosisAutomation-AdministrationRolePolicy` to
your IAM entities. Systems Manager also attaches this policy to a service role that allows
Systems Manager to perform diagnosis actions on your behalf.

**Permissions details**

This policy includes the following permissions.

- `ssm` – Allows principals to run specific Automation
  runbooks that diagnose node issues, access the execution status for workflows,
  and retrieve automation execution details. The policy grants permissions to
  describe automation executions, describe automation step executions, get
  automation execution details, and start automation executions for
  diagnosis-related documents.
- `kms` – Allows principals to use customer-specified
  AWS Key Management Service keys for decryption and data key generation when accessing encrypted
  objects in Amazon S3 buckets used for diagnosis operations. These permissions are
  restricted to keys tagged with `SystemsManagerManaged` and used via
  Amazon S3 service with specific encryption context requirements.
- `sts` – Allows principals to assume diagnosis execution
  roles to run Automation runbooks in the same account. This permission is
  restricted to roles with the `AWS-SSM-DiagnosisExecutionRole` naming
  pattern and includes a condition to ensure the resource account matches the
  principal account.
- `iam` – Allows principals to pass the diagnosis
  administration role to Systems Manager to run Automation runbooks. This permission is
  restricted to roles with the `AWS-SSM-DiagnosisAdminRole` naming
  pattern and can only be passed to the Systems Manager service.
- `s3` – Allows principals to access, read, write, and delete
  objects in Amazon S3 buckets used for diagnosis operations. These permissions are
  restricted to buckets with the `do-not-delete-ssm-diagnosis-` naming
  pattern and include conditions to ensure operations are performed within the
  same account.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWS-SSM-DiagnosisAutomation-AdministrationRolePolicy](../../../aws-managed-policy/latest/reference/AWS-SSM-DiagnosisAutomation-AdministrationRolePolicy.md "../../../aws-managed-policy/latest/reference/AWS-SSM-DiagnosisAutomation-AdministrationRolePolicy.md") in the _AWS
Managed Policy Reference Guide_.

## AWS managed policy: AWS-SSM-DiagnosisAutomation-ExecutionRolePolicy

The managed policy `AWS-SSM-DiagnosisAutomation-ExecutionRolePolicy`
provides administrative permission for running Automation runbooks in a targeted
AWS account and Region to diagnose issues with managed nodes that interact with Systems Manager
services.

You can attach `AWS-SSM-DiagnosisAutomation-ExecutionRolePolicy` to your
IAM entities. Systems Manager also attaches this policy to a service role that allows
Systems Manager to perform actions on your behalf.

**Permissions details**

This policy includes the following permissions.

- `ec2` – Allows principals to describe Amazon EC2 and Amazon VPC
  resources and their configurations to diagnose issues with Systems Manager services.
  This includes permissions to describe VPCs, VPC attributes, VPC endpoints,
  subnets, security groups, instances, instance status, network ACLs, and internet gateways.
- `ssm` – Allows principals to run diagnosis-specific
  Automation runbooks and access the automation workflow status and execution
  metadata. This includes permissions to describe automation step executions,
  describe instance information, describe automation executions, describe activations,
  get automation execution details, get service settings, and start automation executions for specific AWS unmanaged
  EC2 diagnosis documents.
- `kms` – Allows principals to use customer-specified
  AWS Key Management Service keys for decryption and data key generation when accessing encrypted
  objects in Amazon S3 buckets used for diagnosis operations. These permissions are
  restricted to keys tagged with `SystemsManagerManaged` and used via
  Amazon S3 service with specific encryption context requirements for diagnosis
  buckets.
- `iam` – Allows principals to pass the diagnosis execution
  role to Systems Manager to run Automation documents. This permission is restricted to
  roles with the `AWS-SSM-DiagnosisExecutionRole` naming pattern and
  can only be passed to the Systems Manager service.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWS-SSM-DiagnosisAutomation-ExecutionRolePolicy](../../../aws-managed-policy/latest/reference/AWS-SSM-DiagnosisAutomation-ExecutionRolePolicy.md "../../../aws-managed-policy/latest/reference/AWS-SSM-DiagnosisAutomation-ExecutionRolePolicy.md") in the _AWS
Managed Policy Reference Guide_.

## AWS managed policy:

AWS-SSM-RemediationAutomation-AdministrationRolePolicy

The policy `AWS-SSM-RemediationAutomation-AdministrationRolePolicy`
provides permissions for remediating issues with Systems Manager services by executing activities
defined within Automation documents, primarily used for running the Automation
documents. This policy enables starting Automation workflows in accounts and Regions
where nodes are managed to address connectivity and configuration issues.

You can attach `AWS-SSM-RemediationAutomation-AdministrationRolePolicy` to
your IAM entities. Systems Manager also attaches this policy to a service role that allows
Systems Manager to perform remediation actions on your behalf.

**Permissions details**

This policy includes the following permissions.

- `ssm` – Allows principals to run specific Automation
  runbooks that remediate node issues, access the execution status for workflows,
  and retrieve automation execution details. The policy grants permissions to
  describe automation executions, describe automation step executions, get
  automation execution details, and start automation executions for
  remediation-related documents.
- `kms` – Allows principals to use customer-specified
  AWS Key Management Service keys for decryption and data key generation when accessing encrypted
  objects in Amazon S3 buckets used for remediation operations. These permissions are
  restricted to keys tagged with `SystemsManagerManaged` and used via
  Amazon S3 service with specific encryption context requirements.
- `sts` – Allows principals to assume remediation execution
  roles to run Automation runbooks in the same account. This permission is
  restricted to roles with the `AWS-SSM-RemediationExecutionRole`
  naming pattern and includes a condition to ensure the resource account matches
  the principal account.
- `iam` – Allows principals to pass the remediation
  administration role to Systems Manager to run Automation runbooks. This permission is
  restricted to roles with the `AWS-SSM-RemediationAdminRole` naming
  pattern and can only be passed to the Systems Manager service.
- `s3` – Allows principals to access, read, write, and delete
  objects in Amazon S3 buckets used for remediation operations. These permissions are
  restricted to buckets with the `do-not-delete-ssm-diagnosis-` naming
  pattern and include conditions to ensure operations are performed within the
  same account.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWS-SSM-RemediationAutomation-AdministrationRolePolicy](../../../aws-managed-policy/latest/reference/AWS-SSM-RemediationAutomation-AdministrationRolePolicy.md "../../../aws-managed-policy/latest/reference/AWS-SSM-RemediationAutomation-AdministrationRolePolicy.md") in the
_AWS Managed Policy Reference Guide_.

## AWS managed policy: AWS-SSM-RemediationAutomation-ExecutionRolePolicy

The managed policy `AWS-SSM-RemediationAutomation-ExecutionRolePolicy`
provides permissions for running Automation runbooks in a specific target account and
Region to remediate networking and connectivity issues with managed nodes that interact
with Systems Manager services. This policy enables remediation activities defined within
Automation documents, primarily used for running the Automation documents to address
connectivity and configuration issues.

You can attach the policy to your IAM entities. Systems Manager also attaches this policy to a
service role that allows Systems Manager to perform remediation actions on your behalf.

**Permissions details**

This policy includes the following permissions.

- `ssm` – Allows principals to retrieve information about
  Automation executions and their step executions, and to start specific
  remediation Automation runbooks including
  `AWS-OrchestrateUnmanagedEC2Actions` and
  `AWS-RemediateSSMAgent` documents. The policy grants permissions
  to describe automation executions, describe automation step executions, get
  automation execution details, and start automation executions for
  remediation-related documents.
- `ec2` – Allows principals to describe and modify Amazon VPC
  networking resources to remediate connectivity issues. This includes:
  - Describing Amazon VPC attributes, subnets, Amazon VPC endpoints, and security
    groups.
  - Creating Amazon VPC endpoints for Systems Manager services (`ssm`,
    `ssmmessages`, and `ec2messages`) with
    required tags.
  - Modifying Amazon VPC attributes to enable DNS support and hostnames.
  - Creating and managing security groups with specific tags for Amazon VPC
    endpoint access.
  - Authorizing and revoking security group rules for HTTPS access with
    appropriate tags.
  - Creating tags on Amazon VPC endpoints, security groups, and security group
    rules during resource creation.

- `kms` – Allows principals to use customer-specified
  AWS Key Management Service keys for decryption and data key generation when accessing encrypted
  objects in Amazon S3 buckets used for remediation operations. These permissions are
  restricted to keys tagged with `SystemsManagerManaged` and used via
  Amazon S3 service with specific encryption context requirements.
- `iam` – Allows principals to pass the remediation execution
  role to Systems Manager to run Automation runbooks. This permission is restricted to
  roles with the `AWS-SSM-RemediationExecutionRole` naming pattern and
  can only be passed to the Systems Manager service.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWS-SSM-RemediationAutomation-ExecutionRolePolicy](../../../aws-managed-policy/latest/reference/AWS-SSM-RemediationAutomation-ExecutionRolePolicy.md "../../../aws-managed-policy/latest/reference/AWS-SSM-RemediationAutomation-ExecutionRolePolicy.md") in the _AWS
Managed Policy Reference Guide_.

## AWS managed policy: AWSQuickSetupSSMManageResourcesExecutionPolicy

This policy grants permissions that allow Quick Setup to run the
`AWSQuickSetupType-SSM-SetupResources` Automation runbook. This runbook
creates IAM roles for Quick Setup associations, which in turn are created by a
`AWSQuickSetupType-SSM` deployment. It also grants permissions to clean
up an associated Amazon S3 bucket on during a Quick Setup delete operation.

You can attach the policy to your IAM entities. Systems Manager also attaches this policy
to a service role that allows Systems Manager to perform actions on your behalf.

**Permissions details**

This policy includes the following permissions.

- `iam` – Allows principals to list and manage IAM roles for
  use with Quick Setup Systems Manager Explorer operations; to view, attach, and detach IAM policies
  for use with Quick Setup and Systems Manager Explorer These permissions are required so Quick Setup can
  create the roles needed for some of its configuration operations.
- `s3` – Allows principals to retrieve information about
  objects in, and to delete objects from Amazon S3 buckets, in the principal account,
  that are used specifically in Quick Setup configuration operations. This is
  required so that S3 objects that are no longer needed after configuration can be
  removed.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSQuickSetupSSMManageResourcesExecutionPolicy](../../../aws-managed-policy/latest/reference/AWSQuickSetupSSMManageResourcesExecutionPolicy.md "../../../aws-managed-policy/latest/reference/AWSQuickSetupSSMManageResourcesExecutionPolicy.md") in the _AWS
Managed Policy Reference Guide_.

## AWS managed policy: AWSQuickSetupSSMLifecycleManagementExecutionPolicy

The `AWSQuickSetupSSMLifecycleManagementExecutionPolicy` policy grants
administrative permissions that allow Quick Setup to run the a CloudFormation custom resource on
lifecycle events during Quick Setup deployment in Systems Manager.

You can attach this policy to your IAM entities. Systems Manager also attaches this policy
to a service role that allows Systems Manager to perform actions on your behalf.

**Permissions details**

This policy includes the following permissions.

- `ssm` – Allows principals to get information about
  automation executions and start automation executions for setting up certain
  Quick Setup operations.
- `iam` – Allows principals to pass roles from IAM for
  setting up certain Quick Setup resources.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSQuickSetupSSMLifecycleManagementExecutionPolicy](../../../aws-managed-policy/latest/reference/AWSQuickSetupSSMLifecycleManagementExecutionPolicy.md "../../../aws-managed-policy/latest/reference/AWSQuickSetupSSMLifecycleManagementExecutionPolicy.md") in the _AWS
Managed Policy Reference Guide_.

## AWS

managed policy: AWSQuickSetupSSMDeploymentRolePolicy

The managed policy `AWSQuickSetupSSMDeploymentRolePolicy` grants
administrative permissions that allow Quick Setup to create resources that are used during
the Systems Manager onboarding process.

Though you can manually attach this policy to your IAM entities, this is not
recommended. Quick Setup creates entities that attach this policy to a service role that
allows Systems Manager to perform actions on your behalf.

This policy is not related to the [SSMQuickSetupRolePolicy policy](using-service-linked-roles-service-action-5.md "using-service-linked-roles-service-action-5.md"), which is used to provide
permissions for the `AWSServiceRoleForSSMQuickSetup` service-linked
role.

**Permissions details**

This policy includes the following permissions.

- `ssm` – Allows principals to manage associations for certain
  resources that are created using AWS CloudFormation templates and a specific set of SSM
  documents; to manage roles and role policies using for diagnosing and
  remediating managed nodes through CloudFormation templates; and to attach and delete
  policies for Quick Setup lifecycle events
- `iam` – Allows principals to tag roles and pass roles
  permissions for the Systems Manager service and Lambda service, and to pass role
  permissions for diagnosis operations.
- `lambda` – Allows principals to tag and manage functions for
  the Quick Setup lifecycle in the principal account using CloudFormation templates.
- `cloudformation` – Allows principals to read information
  from CloudFormation. This is required so Quick Setup can gather data about the CloudFormation stacks
  used to manage the state of resources and CloudFormation stackset operations.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSQuickSetupSSMDeploymentRolePolicy](../../../aws-managed-policy/latest/reference/AWSQuickSetupSSMDeploymentRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSQuickSetupSSMDeploymentRolePolicy.md") in the _AWS Managed Policy
Reference Guide_.

## AWS managed policy: AWSQuickSetupSSMDeploymentS3BucketRolePolicy

The `AWSQuickSetupSSMDeploymentS3BucketRolePolicy` policy grants
permissions for listing all S3 buckets in an account; and for managing and retrieving
information about specific buckets in the principal account that are managed through
CloudFormation templates.

You can attach `AWSQuickSetupSSMDeploymentS3BucketRolePolicy` to your IAM
entities. Systems Manager also attaches this policy to a service role that allows Systems Manager to
perform actions on your behalf.

**Permissions details**

This policy includes the following permissions.

- `s3` – Allows principals list all S3 buckets in an account;
  and to manage and retrieve information about specific buckets in the principal
  account that are managed through CloudFormation templates.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSQuickSetupSSMDeploymentS3BucketRolePolicy](../../../aws-managed-policy/latest/reference/AWSQuickSetupSSMDeploymentS3BucketRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSQuickSetupSSMDeploymentS3BucketRolePolicy.md") in the _AWS Managed
Policy Reference Guide_.

## AWS

managed policy: AWSQuickSetupEnableDHMCExecutionPolicy

This policy grants administrative permissions that allow principals to run the
`AWSQuickSetupType-EnableDHMC` Automation runbook, which enables
Default Host Management Configuration. The Default Host Management Configuration setting
allows Systems Manager to automatically manage Amazon EC2 instances as _managed
instances_. A managed instance is an EC2 instance that is configured for
use with Systems Manager. This policy also grants permissions for creating IAM roles that are
specified in Systems Manager service settings as the default roles for SSM Agent.

You can attach
`AWSQuickSetupEnableDHMCExecutionPolicy` to your
IAM entities. Systems Manager also attaches this policy to a service role that allows
Systems Manager to perform actions on your behalf.

**Permissions details**

This policy includes the following permissions.

- `ssm` – Allows principals to update and get information
  about Systems Manager service settings.
- `iam` – Allows principals to create and retrieve information
  about IAM roles for Quick Setup operations.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSQuickSetupEnableDHMCExecutionPolicy](../../../aws-managed-policy/latest/reference/AWSQuickSetupEnableDHMCExecutionPolicy.md "../../../aws-managed-policy/latest/reference/AWSQuickSetupEnableDHMCExecutionPolicy.md") in the
_AWS Managed Policy Reference Guide_.

## AWS

managed policy: AWSQuickSetupEnableAREXExecutionPolicy

This policy grants administrative permissions that allow Systems Manager to run the
`AWSQuickSetupType-EnableAREX` Automation runbook, which enables
AWS Resource Explorer for use with Systems Manager. Resource Explorer makes it possible to view resources in your
account with a search experience similar to an Internet search engine. The policy also
grants permissions for managing Resource Explorer indexes and views.

You can attach `AWSQuickSetupEnableAREXExecutionPolicy` to
your IAM entities. Systems Manager also attaches this policy to a service role that allows
Systems Manager to perform actions on your behalf.

**Permissions details**

This policy includes the following permissions.

- `iam` – Allows principals to to create a service-linked role
  in the AWS Identity and Access Management (IAM) service.
- `resource-explorer-2` – Allows principals to retrieve
  information about Resource Explorer views and indexes; to create Resource Explorer views and indexes;
  to change the index type for indexes displayed in Quick Setup.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSQuickSetupEnableAREXExecutionPolicy](../../../aws-managed-policy/latest/reference/AWSQuickSetupEnableAREXExecutionPolicy.md "../../../aws-managed-policy/latest/reference/AWSQuickSetupEnableAREXExecutionPolicy.md") in the
_AWS Managed Policy Reference Guide_.

## AWS managed policy: AWSQuickSetupManagedInstanceProfileExecutionPolicy

This policy grants administrative permissions that allow Systems Manager to create a default
IAM instance profile for the Quick Setup tool, and to attach it to Amazon EC2 instances that
don't already have an instance profile attached. The policy also grants Systems Manager the
ability to attach permissions to existing instance profiles. This is done to ensure that
the permissions required for Systems Manager to communicate with SSM Agent on EC2 instances are
in place.

You can attach `AWSQuickSetupManagedInstanceProfileExecutionPolicy`
to your IAM entities. Systems Manager also attaches this policy to a service role that
allows Systems Manager to perform actions on your behalf.

**Permissions details**

This policy includes the following permissions.

- `ssm` – Allows principals to start automation workflows
  associated with Quick Setup processes.
- `ec2` – Allows principals to attach IAM instance profiles
  to EC2 instances that are managed by Quick Setup.
- `iam` – Allows principals to create, update, and retrieve
  information about roles from IAM that are used in Quick Setup processes; to
  create IAM instance profiles; to attach the
  `AmazonSSMManagedInstanceCore` managed policy to IAM instance
  profiles.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSQuickSetupManagedInstanceProfileExecutionPolicy](../../../aws-managed-policy/latest/reference/AWSQuickSetupManagedInstanceProfileExecutionPolicy.md "../../../aws-managed-policy/latest/reference/AWSQuickSetupManagedInstanceProfileExecutionPolicy.md") in the _AWS
Managed Policy Reference Guide_.

## AWS managed policy: AWSQuickSetupManageJITNAResourcesExecutionPolicy

The managed policy
`AWSQuickSetupManageJITNAResourcesExecutionPolicy` enables
Quick Setup, a tool in Systems Manager, to set up just-in-time node access.

You can attach `AWSQuickSetupManageJITNAResourcesExecutionPolicy`
to your IAM entities. Systems Manager also attaches this policy to a service role that
allows Systems Manager to perform actions on your behalf.

This policy grants administrative permissions that allow Systems Manager to create resources
associated with just-in-time node access.

**Permissions details**

This policy includes the following permissions.

- `ssm` – Allows principals to get and update the service
  setting that specifies the identity provider for just-in-time node
  access.
- `iam` – Allows principals to create, tag, and get roles,
  attach role policies for just-in-time node access managed policies, and create
  service-linked roles for just-in-time node access and notifications.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSQuickSetupManageJITNAResourcesExecutionPolicy](../../../aws-managed-policy/latest/reference/AWSQuickSetupManageJITNAResourcesExecutionPolicy.md "../../../aws-managed-policy/latest/reference/AWSQuickSetupManageJITNAResourcesExecutionPolicy.md") in the _AWS
Managed Policy Reference Guide_.

## AWS

managed policy: AWSQuickSetupJITNADeploymentRolePolicy

The managed policy `AWSQuickSetupJITNADeploymentRolePolicy` allows
Quick Setup to deploy the configuration type required to set up just-in-time node
access.

You can attach `AWSQuickSetupJITNADeploymentRolePolicy` to your
IAM entities. Systems Manager also attaches this policy to a service role that allows
Systems Manager to perform actions on your behalf.

This policy grants administrative permissions that allow Systems Manager to create resources
associated with just-in-time node access.

**Permissions details**

This policy includes the following permissions.

- `cloudformation` – Allows principals to create, update,
  delete, and read CloudFormation stacks.
- `ssm` – Allows principals to create, delete, update, and
  read State Manager associations that are called by CloudFormation.
- `iam` – Allows principals create, delete, read and tag IAM
  roles that are called by CloudFormation.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSQuickSetupJITNADeploymentRolePolicy](../../../aws-managed-policy/latest/reference/AWSQuickSetupJITNADeploymentRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSQuickSetupJITNADeploymentRolePolicy.md") in the _AWS Managed
Policy Reference Guide_.

## AWS managed policy: AWSSystemsManagerJustInTimeAccessServicePolicy

The managed policy `AWSSystemsManagerJustInTimeAccessServicePolicy`
provides access to AWS resources managed or used by the AWS Systems Manager just-in-time access
framework. This policy update adds automation execution tagging permissions to enable
customers to scope down operator permissions to specific tags.

You can't attach `AWSSystemsManagerJustInTimeAccessServicePolicy` to your
IAM entities. This policy is attached to a service-linked role that allows
Systems Manager to perform actions on your behalf. For more information, see [Using roles to enable just-in-time node access](using-service-linked-roles-service-action-8.md "using-service-linked-roles-service-action-8.md").

This policy grants administrative permissions that allows access to resources
associated with just-in-time node access.

**Permissions details**

This policy includes the following permissions.

- `ssm` – Allows principals to create and manage OpsItems, add
  tags to OpsItems and automation executions, get and update OpsItems, retrieve and
  describe documents, describe OpsItems and sessions, list documents and tags for
  managed instances.
- `ssm-guiconnect` – Allows principals to list
  connections.
- `identitystore` – Allows principals to get user and group
  IDs, describe users, and list group membership.
- `sso-directory` – Allows principals to describe users and
  determine if a user is a member of a group.
- `sso` – Allows principals to describe registered Regions and
  list instances and directory associations.
- `cloudwatch` – Allows principals to put metric data for the
  `AWS/SSM/JustInTimeAccess` namespace.
- `ec2` – Allows principals to describe tags.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSSystemsManagerJustInTimeAccessServicePolicy](../../../aws-managed-policy/latest/reference/AWSSystemsManagerJustInTimeAccessServicePolicy.md "../../../aws-managed-policy/latest/reference/AWSSystemsManagerJustInTimeAccessServicePolicy.md") in the _AWS
Managed Policy Reference Guide_.

## AWS managed policy: AWSSystemsManagerJustInTimeAccessTokenPolicy

The managed policy `AWSSystemsManagerJustInTimeAccessTokenPolicy` provides
permissions for users to establish secure connections to Amazon EC2 instances and managed
instances through Session Manager and Systems Manager GUI Connect RDP connections as part of just-in-time node
access workflows.

You can attach `AWSSystemsManagerJustInTimeAccessTokenPolicy` to your IAM
entities.

This policy grants contributor permissions that allow users to start and manage secure
sessions, establish RDP connections, and perform necessary cryptographic operations for
just-in-time node access.

**Permissions details**

This policy includes the following permissions.

- `ssm` – Allows principals to start Session Manager sessions on
  Amazon EC2 instances and managed instances using the SSM-SessionManagerRunShell
  document. Also allows terminating and resuming sessions, retrieving command
  invocation details, and sending commands to instances for SSO user setup when
  called through Systems Manager GUI Connect. Additionally allows starting port forwarding sessions for
  RDP connections when called through Systems Manager GUI Connect.
- `ssmmessages` – Allows principals to open data channels for
  secure communication during Session Manager sessions.
- `ssm-guiconnect` – Allows principals to start, get details
  about, and cancel Systems Manager GUI Connect RDP connections to instances.
- `kms` – Allows principals to generate data keys for Session Manager
  encryption and create grants for RDP connections. These permissions are
  restricted to AWS KMS keys tagged with
  `SystemsManagerJustInTimeNodeAccessManaged=true`. Grant creation
  is further restricted to be used only through the Systems Manager GUI Connect service.
- `sso` – Allows principals to list directory associations
  when called through Systems Manager GUI Connect. This is required for RDP SSO user setup.
- `identitystore` – Allows principals to describe users in the
  identity store when called through Systems Manager GUI Connect. This is required for RDP SSO user
  setup.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSSystemsManagerJustInTimeAccessTokenPolicy](../../../aws-managed-policy/latest/reference/AWSSystemsManagerJustInTimeAccessTokenPolicy.md "../../../aws-managed-policy/latest/reference/AWSSystemsManagerJustInTimeAccessTokenPolicy.md") in the _AWS Managed
Policy Reference Guide_.

## AWS managed policy: AWSSystemsManagerJustInTimeAccessTokenSessionPolicy

The managed policy
`AWSSystemsManagerJustInTimeAccessTokenSessionPolicy` allows
Systems Manager to apply scoped down permissions to a just-in-time node access token.

You can attach
`AWSSystemsManagerJustInTimeAccessTokenSessionPolicy` to your
IAM entities.

This policy grants administrative permissions that allow Systems Manager to scope down
permissions for just-in-time node access tokens.

**Permissions details**

This policy includes the following permissions.

- `ssm` – Allows principals to start Session Manager sessions using
  the `SSM-SessionManagerRunShell` document. Also when called first via
  `ssm-guiconnect`, start sessions using the
  `AWS-StartPortForwardingSession` document, list command
  invocations, and send commands using the `AWSSSO-CreateSSOUser`
  document.
- `ssm-guiconnect` – Allows principals to cancel, get, and
  start connections on all resources.
- `kms` – Allows principals to create grants and generate data
  keys for keys tagged with `SystemsManagerJustInTimeNodeAccessManaged`
  when called via `ssm-guiconnect` through an AWS service.
- `sso` – Allows principals to list directory associations
  when called via `ssm-guiconnect`.
- `identitystore` – Allows principals to describe a user when
  called via `ssm-guiconnect`.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSSystemsManagerJustInTimeAccessTokenSessionPolicy](../../../aws-managed-policy/latest/reference/AWSSystemsManagerJustInTimeAccessTokenSessionPolicy.md "../../../aws-managed-policy/latest/reference/AWSSystemsManagerJustInTimeAccessTokenSessionPolicy.md") in the _AWS
Managed Policy Reference Guide_.

## AWS managed policy:

AWSSystemsManagerJustInTimeNodeAccessRolePropagationPolicy

The managed policy
`AWSSystemsManagerJustInTimeNodeAccessRolePropagationPolicy`
allows Systems Manager to share deny-access policies from the delegated administrator account
to member accounts, and replicate the policies across multiple AWS Regions.

You can attach
`AWSSystemsManagerJustInTimeNodeAccessRolePropagationPolicy` to
your IAM entities.

This policy provides the administrative permissions necessary for Systems Manager to share
and create deny-access policies. This ensures that deny-access policies are applied to
all accounts in an AWS Organizations organization and Regions configured for just-in-time node
access.

**Permissions details**

This policy includes the following permissions.

- `ssm` – Allows principals to manage SSM documents and
  resource policies.
- `ssm-quicksetup` – Allows principals to read Quick Setup
  configuration managers.
- `organizations` – Allows principals to list details about an
  AWS Organizations organization and delegated administrators.
- `ram` – Allows principals to create, tag, and describe
  resource shares.
- `iam` – Allows principals to describe a service role.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSSystemsManagerJustInTimeNodeAccessRolePropagationPolicy](../../../aws-managed-policy/latest/reference/AWSSystemsManagerJustInTimeNodeAccessRolePropagationPolicy.md "../../../aws-managed-policy/latest/reference/AWSSystemsManagerJustInTimeNodeAccessRolePropagationPolicy.md") in the
_AWS Managed Policy Reference Guide_.

## AWS managed policy: AWSSystemsManagerNotificationsServicePolicy

The managed policy `AWSSystemsManagerNotificationsServicePolicy`
allows Systems Manager to send email notifications for just-in-time node access requests to
access request approvers.

You can't attach `AWSSystemsManagerJustInTimeAccessServicePolicy` to your
IAM entities. This policy is attached to a service-linked role that allows
Systems Manager to perform actions on your behalf. For more information, see [Using roles to send just-in-time node access request notifications](using-service-linked-roles-service-action-9.md "using-service-linked-roles-service-action-9.md").

This policy grants administrative permissions that allow Systems Manager to send email
notifications for just-in-time node access requests to access request approvers.

**Permissions details**

This policy includes the following permissions.

- `identitystore` – Allows principals to list and describe
  users and group membership.
- `sso` – Allows principals to list instances, directories,
  and describe registered Regions.
- `sso-directory` – Allows principals to describe users and
  list members in a group.
- `iam` – Allows principals to get information about
  roles.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWSSystemsManagerNotificationsServicePolicy](../../../aws-managed-policy/latest/reference/AWSSystemsManagerNotificationsServicePolicy.md "../../../aws-managed-policy/latest/reference/AWSSystemsManagerNotificationsServicePolicy.md") in the _AWS Managed
Policy Reference Guide_.

## AWS

managed policy: AWS-SSM-Automation-DiagnosisBucketPolicy

The managed policy `AWS-SSM-Automation-DiagnosisBucketPolicy` provides
permissions for diagnosing issues with nodes that interact with AWS Systems Manager services, by
allowing access to S3 buckets that are used for diagnosis and remediation of
issues.

You can attach the `AWS-SSM-Automation-DiagnosisBucketPolicy` policy to
your IAM identities. Systems Manager also attaches this policy to an IAM role that allows
Systems Manager to perform diagnosis actions on your behalf.

**Permissions details**

This policy includes the following permissions.

- `s3` – Allows principals to access and write objects to an
  Amazon S3 bucket.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWS-SSM-Automation-DiagnosisBucketPolicy](../../../aws-managed-policy/latest/reference/AWS-SSM-Automation-DiagnosisBucketPolicy.md "../../../aws-managed-policy/latest/reference/AWS-SSM-Automation-DiagnosisBucketPolicy.md") in the _AWS Managed
Policy Reference Guide_.

## AWS managed policy:

AWS-SSM-RemediationAutomation-OperationalAccountAdministrationRolePolicy

The managed policy
`AWS-SSM-RemediationAutomation-OperationalAccountAdministrationRolePolicy`
provides permissions for an operational account to diagnose issues with nodes by
providing organization-specific permissions.

You can attach
`AWS-SSM-RemediationAutomation-OperationalAccountAdministrationRolePolicy`
to your IAM identities. Systems Manager also attaches this policy to an IAM role that allows
Systems Manager to perform diagnosis actions on your behalf.

**Permissions details**

This policy includes the following permissions.

- `organizations` – Allows principals to list a root of the
  organization, and get member accounts to determine target accounts.
- `sts` – Allows principals to assume remediation execution
  roles to run SSM Automation documents across accounts and Regions, within the
  same organization.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWS-SSM-RemediationAutomation-OperationalAccountAdministrationRolePolicy](../../../aws-managed-policy/latest/reference/AWS-SSM-RemediationAutomation-OperationalAccountAdministrationRolePolicy.md "../../../aws-managed-policy/latest/reference/AWS-SSM-RemediationAutomation-OperationalAccountAdministrationRolePolicy.md") in
the _AWS Managed Policy Reference Guide_.

## AWS managed policy:

AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy

The managed policy
`AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy`
provides permissions for an operational account to diagnose issues with nodes by
providing organization-specific permissions.

You can attach the
`AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy`
policy to your IAM identities. Systems Manager also attaches this policy to an IAM role that
allows Systems Manager to perform diagnosis actions on your behalf.

**Permissions details**

This policy includes the following permissions.

- `organizations` – Allows principals to list a root of the
  organization, and get member accounts to determine target accounts.
- `sts` – Allows principals to assume diagnosis execution
  roles to run SSM Automation documents across accounts and Regions, within the
  same organization.

To view more details about the policy, including the latest version of the JSON policy
document, see [AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy](../../../aws-managed-policy/latest/reference/AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy.md "../../../aws-managed-policy/latest/reference/AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy.md") in
the _AWS Managed Policy Reference Guide_.

## Systems Manager updates to AWS managed

policies

In the following table, view details about updates to AWS managed policies for
Systems Manager since this service began tracking these changes on March 12, 2021. For
information about other managed policies for the Systems Manager service, see [Additional managed policies for Systems Manager](#policies-list "#policies-list") later in this topic. For
automatic alerts about changes to this page, subscribe to the RSS feed on the
Systems Manager [Document history](systems-manager-release-history.md "systems-manager-release-history.md") page.

| Change                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Date               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [AWS-SSM-DiagnosisAutomation-ExecutionRolePolicy](#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-ExecutionRolePolicy "#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-ExecutionRolePolicy") –<br>Updated managed policy                                                                                                                                                                                                                                                                                                                                                                                                                              | Systems Manager updated the managed policy to add additional EC2 and SSM permissions for enhanced diagnosis capabilities. The policy now includes permissions to describe EC2 instance status and network ACLs, as well as SSM activations and service settings, providing more comprehensive diagnostic information for troubleshooting managed node issues.                                                                                                                                                                                                                                        | December 19, 2025  |
| [AWSQuickSetupDeploymentRolePolicy](#security-iam-awsmanpol-AWSQuickSetupDeploymentRolePolicy "#security-iam-awsmanpol-AWSQuickSetupDeploymentRolePolicy") –<br>Updated managed policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Systems Manager updated the managed policy<br>`AWSQuickSetupDeploymentRolePolicy` to add support for<br>two additional SSM documents:<br>`AWSQuickSetupType-ConfigureDevOpsGuru` and<br>`AWSQuickSetupType-DeployConformancePack`. These additions<br>enable Quick Setup to deploy DevOps Guru configurations and conformance<br>packs through the policy.                                                                                                                                                                                                                                           | December 15, 2025  |
| [AWSSystemsManagerJustInTimeAccessTokenPolicy](#security-iam-awsmanpol-AWSSystemsManagerJustInTimeAccessTokenPolicy "#security-iam-awsmanpol-AWSSystemsManagerJustInTimeAccessTokenPolicy") –<br>Update to an existing policy                                                                                                                                                                                                                                                                                                                                                                                                                                 | Systems Manager updated the managed policy<br>`AWSSystemsManagerJustInTimeAccessTokenPolicy`. The<br>statement (`SID`) `TerminateAndResumeSession`<br>has been renamed to<br>`TerminateAndResumeSessionAndOpenDataChannel` and now<br>includes the `ssmmessages:OpenDataChannel` action,<br>combining session management and data channel permissions into a<br>single statement.                                                                                                                                                                                                                    | September 25, 2025 |
| Updated managed policies:<br>• [AWSQuickSetupSSMLifecycleManagementExecutionPolicy](#security-iam-awsmanpol-AWSQuickSetupSSMLifecycleManagementExecutionPolicy "#security-iam-awsmanpol-AWSQuickSetupSSMLifecycleManagementExecutionPolicy")<br>• [AWSQuickSetupPatchPolicyPermissionsBoundary](#security-iam-awsmanpol-AWSQuickSetupPatchPolicyPermissionsBoundary "#security-iam-awsmanpol-AWSQuickSetupPatchPolicyPermissionsBoundary")<br>• [AWSQuickSetupManagedInstanceProfileExecutionPolicy](#security-iam-awsmanpol-AWSQuickSetupManagedInstanceProfileExecutionPolicy "#security-iam-awsmanpol-AWSQuickSetupManagedInstanceProfileExecutionPolicy") | Systems Manager updated three managed policies to add support for<br>starting Automation executions on additional Systems Manager resources,<br>including specific Automation runbooks and SSM Command<br>documents.                                                                                                                                                                                                                                                                                                                                                                                 | September 12, 2025 |
| [AWSQuickSetupStartStopInstancesExecutionPolicy](#security-iam-awsmanpol-AWSQuickSetupStartStopInstancesExecutionPolicy "#security-iam-awsmanpol-AWSQuickSetupStartStopInstancesExecutionPolicy") –<br>Updated managed policy                                                                                                                                                                                                                                                                                                                                                                                                                                 | Systems Manager updated the managed policy to refine permissions for<br>Quick Setup scheduler configuration. The policy now provides more<br>specific permissions for starting and stopping Amazon EC2 instances,<br>accessing change calendars, and executing automation documents with<br>enhanced security conditions.                                                                                                                                                                                                                                                                            | September 12, 2025 |
| [AWSQuickSetupStartSSMAssociationsExecutionPolicy](#security-iam-awsmanpol-AWSQuickSetupStartSSMAssociationsExecutionPolicy "#security-iam-awsmanpol-AWSQuickSetupStartSSMAssociationsExecutionPolicy")<br>– Updated managed policy                                                                                                                                                                                                                                                                                                                                                                                                                           | Systems Manager updated the managed policy to change the automation<br>document from `AWSQuickSetupType-StartSSMAssociations` to<br>`AWSQuickSetupType-Scheduler-ChangeCalendarState`.<br>This update changes the policy's purpose from starting SSM<br>associations to managing change calendar states for scheduled<br>operations.                                                                                                                                                                                                                                                                 | September 12, 2025 |
| [AmazonSSMAutomationRole](#security-iam-awsmanpol-AmazonSSMAutomationRole "#security-iam-awsmanpol-AmazonSSMAutomationRole") – Update to an existing<br>policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Systems Manager added new permissions to allow Automation runbooks<br>to establish communication channels for session-based<br>operations.<br>Added the `ssmmessages:OpenDataChannel` permission for<br>the resource `arn:*:ssm:*:*:session/*`.                                                                                                                                                                                                                                                                                                                                                      | September 11, 2025 |
| [AWSSystemsManagerJustInTimeAccessServicePolicy](#security-iam-awsmanpol-AWSSystemsManagerJustInTimeAccessServicePolicy "#security-iam-awsmanpol-AWSSystemsManagerJustInTimeAccessServicePolicy") –<br>Updated managed policy                                                                                                                                                                                                                                                                                                                                                                                                                                 | Systems Manager updated the managed policy to add automation<br>execution tagging permissions. The service needs to tag automation<br>executions with<br>`SystemsManagerJustInTimeNodeAccessManaged=true` tag<br>to enable customers to scope down operator permissions to specific<br>tags.                                                                                                                                                                                                                                                                                                         | August 25, 2025    |
| [AWSQuickSetupStartSSMAssociationsExecutionPolicy](#security-iam-awsmanpol-AWSQuickSetupStartSSMAssociationsExecutionPolicy "#security-iam-awsmanpol-AWSQuickSetupStartSSMAssociationsExecutionPolicy")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                                                                                       | Systems Manager added a new policy to allow Quick Setup to run the<br>`AWSQuickSetupType-StartSSMAssociations` Automation<br>runbook. This runbook is used to start State Manager associations that<br>are created by Quick Setup configurations.                                                                                                                                                                                                                                                                                                                                                    | August 12, 2025    |
| [AWSQuickSetupStartStopInstancesExecutionPolicy](#security-iam-awsmanpol-AWSQuickSetupStartStopInstancesExecutionPolicy "#security-iam-awsmanpol-AWSQuickSetupStartStopInstancesExecutionPolicy") –<br>New policy                                                                                                                                                                                                                                                                                                                                                                                                                                             | Systems Manager added a new policy to allow Quick Setup to start and<br>stop Amazon EC2 instances on a schedule. This policy provides the<br>necessary permissions for the Quick Setup scheduler configuration type<br>to manage instance state based on defined schedules.                                                                                                                                                                                                                                                                                                                          | August 12, 2025    |
| [AWSQuickSetupDeploymentRolePolicy](#security-iam-awsmanpol-AWSQuickSetupDeploymentRolePolicy "#security-iam-awsmanpol-AWSQuickSetupDeploymentRolePolicy") – Update to<br>documentation                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Systems Manager has updated the<br>`AWSQuickSetupDeploymentRolePolicy` managed policy to<br>grant permissions for additional resources. In addition, the<br>documentation for `AWSQuickSetupDeploymentRolePolicy` has<br>been updated with more detailed descriptions of the permissions<br>granted by this policy for Quick Setup configuration management<br>operations.                                                                                                                                                                                                                           | August 12, 2025    |
| [AWS-SSM-RemediationAutomation-ExecutionRolePolicy](#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-ExecutionRolePolicy "#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-ExecutionRolePolicy")<br>– Update to an existing policy                                                                                                                                                                                                                                                                                                                                                                                                                  | Systems Manager updated the managed policy to improve the security<br>posture of the ssm:StartAutomationExecution API by requiring<br>permissions for both "document" and "automation-execution" resource<br>types. The updated policy provides more comprehensive and detailed<br>permissions for remediation automation execution, including enhanced<br>descriptions for networking remediation capabilities, more specific<br>Amazon VPC endpoint creation permissions, detailed security group<br>management permissions, and improved resource tagging controls for<br>remediation operations. | July 16th, 2025    |
| [AWS-SSM-RemediationAutomation-AdministrationRolePolicy](#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-AdministrationRolePolicy "#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-AdministrationRolePolicy")<br>– Update to an existing policy                                                                                                                                                                                                                                                                                                                                                                                                   | Systems Manager updated the managed policy to support API<br>authorization improvements for remediation automation operations.<br>The updated policy enhances permissions for executing activities<br>defined within Automation documents, with improved security controls<br>and resource access patterns for remediation workflows.                                                                                                                                                                                                                                                                | July 16th, 2025    |
| [AWS-SSM-DiagnosisAutomation-ExecutionRolePolicy](#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-ExecutionRolePolicy "#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-ExecutionRolePolicy") –<br>Update to an existing policy                                                                                                                                                                                                                                                                                                                                                                                                                        | Systems Manager updated the managed policy to provide more detailed<br>and accurate permissions for diagnosis automation execution. The<br>updated policy includes enhanced descriptions for Amazon EC2 and Amazon VPC<br>resource access, more specific SSM automation permissions, and<br>improved AWS KMS and IAM permission descriptions with proper<br>resource restrictions.                                                                                                                                                                                                                   | July 16th, 2025    |
| [AWS-SSM-DiagnosisAutomation-AdministrationRolePolicy](#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-AdministrationRolePolicy "#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-AdministrationRolePolicy")<br>– Update to an existing policy                                                                                                                                                                                                                                                                                                                                                                                                         | Systems Manager updated the managed policy to provide more specific<br>permissions and security conditions for diagnosis automation<br>operations. The updated policy provides enhanced security controls<br>for AWS KMS key usage, Amazon S3 bucket access, and role assumptions, with<br>stricter resource-based conditions and account-level<br>restrictions.                                                                                                                                                                                                                                     | July 16th, 2025    |
| [AWSQuickSetupDeploymentRolePolicy](#security-iam-awsmanpol-AWSQuickSetupDeploymentRolePolicy "#security-iam-awsmanpol-AWSQuickSetupDeploymentRolePolicy") – Update to a<br>policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Systems Manager added permissions to the managed policy<br>`AWSQuickSetupDeploymentRolePolicy` for accessing the<br>Amazon owned runbook [AWSQuickSetupType-ManageInstanceProfile](https://console.aws.amazon.com/systems-manager/documents/AWSQuickSetupType-ManageInstanceProfile/content "https://console.aws.amazon.com/systems-manager/documents/AWSQuickSetupType-ManageInstanceProfile/content"). This<br>permission makes it possible for Quick Setup to create associations<br>using the managed policy instead of inline policies.                                                         | July 14th, 2025    |
| [AmazonSSMAutomationRole](#security-iam-awsmanpol-AmazonSSMAutomationRole "#security-iam-awsmanpol-AmazonSSMAutomationRole") – Update to<br>documentation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Systems Manager added comprehensive documentation for the existing<br>`AmazonSSMAutomationRole` policy, which provides<br>permissions for the Systems Manager Automation service to run activities<br>defined within Automation runbooks.                                                                                                                                                                                                                                                                                                                                                            | July 15, 2025      |
| [AWSSystemsManagerJustInTimeNodeAccessRolePropagationPolicy](#security-iam-awsmanpol-AWSSystemsManagerJustInTimeNodeAccessRolePropagationPolicy "#security-iam-awsmanpol-AWSSystemsManagerJustInTimeNodeAccessRolePropagationPolicy")<br>– Update to an policy                                                                                                                                                                                                                                                                                                                                                                                                | Systems Manager added permissions to allow Systems Manager to tag a<br>resource shared by AWS Resource Access Manager for just-in-time node access.                                                                                                                                                                                                                                                                                                                                                                                                                                                  | April 30th, 2025   |
| [AWSQuickSetupManageJITNAResourcesExecutionPolicy](#security-iam-awsmanpol-AWSQuickSetupManageJITNAResourcesExecutionPolicy "#security-iam-awsmanpol-AWSQuickSetupManageJITNAResourcesExecutionPolicy")<br>– Update to a policy                                                                                                                                                                                                                                                                                                                                                                                                                               | Systems Manager added permissions to allow Systems Manager to tag IAM<br>roles created for just-in-time node access.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | April 30th, 2025   |
| [AWSSystemsManagerJustInTimeAccessTokenSessionPolicy](#security-iam-awsmanpol-AWSSystemsManagerJustInTimeAccessTokenSessionPolicy "#security-iam-awsmanpol-AWSSystemsManagerJustInTimeAccessTokenSessionPolicy")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                                                                              | Systems Manager added a new policy to allow Systems Manager to apply<br>scoped down permissions to a just-in-time node access token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | April 30th, 2025   |
| [AWSSystemsManagerNotificationsServicePolicy](#security-iam-awsmanpol-AWSSystemsManagerNotificationsServicePolicy "#security-iam-awsmanpol-AWSSystemsManagerNotificationsServicePolicy") – New<br>policy                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Systems Manager added a new policy to allow Systems Manager to send email<br>notifications for just-in-time node access requests to access<br>request approvers.                                                                                                                                                                                                                                                                                                                                                                                                                                     | April 30th, 2025   |
| [AWSSystemsManagerJustInTimeNodeAccessRolePropagationPolicy](#security-iam-awsmanpol-AWSSystemsManagerJustInTimeNodeAccessRolePropagationPolicy "#security-iam-awsmanpol-AWSSystemsManagerJustInTimeNodeAccessRolePropagationPolicy")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                                                         | Systems Manager added a new policy to allow Systems Manager to replicate<br>approval policies to different Regions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | April 30th, 2025   |
| [AWSSystemsManagerJustInTimeAccessTokenPolicy](#security-iam-awsmanpol-AWSSystemsManagerJustInTimeAccessTokenPolicy "#security-iam-awsmanpol-AWSSystemsManagerJustInTimeAccessTokenPolicy") –<br>New policy                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Systems Manager added a new policy to allow Systems Manager to generate<br>access tokens used for just-in-time node access.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | April 30th, 2025   |
| [AWSSystemsManagerJustInTimeAccessServicePolicy](#security-iam-awsmanpol-AWSSystemsManagerJustInTimeAccessServicePolicy "#security-iam-awsmanpol-AWSSystemsManagerJustInTimeAccessServicePolicy") –<br>New policy                                                                                                                                                                                                                                                                                                                                                                                                                                             | Systems Manager added a new policy to provide permissions to AWS<br>resources managed or used by the Systems Manager just-in-time node access<br>feature.                                                                                                                                                                                                                                                                                                                                                                                                                                            | April 30th, 2025   |
| [AWSQuickSetupManageJITNAResourcesExecutionPolicy](#security-iam-awsmanpol-AWSQuickSetupManageJITNAResourcesExecutionPolicy "#security-iam-awsmanpol-AWSQuickSetupManageJITNAResourcesExecutionPolicy")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                                                                                       | Systems Manager added a new policy to allow Quick Setup, a tool in<br>Systems Manager, to create the IAM roles necessary for just-in-time node<br>access.                                                                                                                                                                                                                                                                                                                                                                                                                                            | April 30th, 2025   |
| [AWSQuickSetupJITNADeploymentRolePolicy](#security-iam-awsmanpol-AWSQuickSetupJITNADeploymentRolePolicy "#security-iam-awsmanpol-AWSQuickSetupJITNADeploymentRolePolicy") – New<br>policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Systems Manager added a new policy that provides permissions that<br>allow Quick Setup to deploy the configuration type required to set up<br>just-in-time node access.                                                                                                                                                                                                                                                                                                                                                                                                                              | April 30th, 2025   |
| [AWSSystemsManagerJustInTimeNodeAccessRolePropagationPolicy](#security-iam-awsmanpol-AWSSystemsManagerJustInTimeNodeAccessRolePropagationPolicy "#security-iam-awsmanpol-AWSSystemsManagerJustInTimeNodeAccessRolePropagationPolicy")<br>– Update to an policy                                                                                                                                                                                                                                                                                                                                                                                                | Systems Manager added permissions to allow Systems Manager to tag a<br>resource shared by AWS Resource Access Manager for just-in-time node access.                                                                                                                                                                                                                                                                                                                                                                                                                                                  | April 30th, 2025   |
| [AWSQuickSetupManageJITNAResourcesExecutionPolicy](#security-iam-awsmanpol-AWSQuickSetupManageJITNAResourcesExecutionPolicy "#security-iam-awsmanpol-AWSQuickSetupManageJITNAResourcesExecutionPolicy")<br>– Update to an policy                                                                                                                                                                                                                                                                                                                                                                                                                              | Systems Manager added permissions to allow Systems Manager to tag IAM<br>roles created for just-in-time node access.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | April 30th, 2025   |
| [AWSSystemsManagerJustInTimeAccessTokenSessionPolicy](#security-iam-awsmanpol-AWSSystemsManagerJustInTimeAccessTokenSessionPolicy "#security-iam-awsmanpol-AWSSystemsManagerJustInTimeAccessTokenSessionPolicy")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                                                                              | Systems Manager added a new policy to allow Systems Manager to apply<br>scoped down permissions to a just-in-time node access token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | April 30th, 2025   |
| [AWSSystemsManagerNotificationsServicePolicy](#security-iam-awsmanpol-AWSSystemsManagerNotificationsServicePolicy "#security-iam-awsmanpol-AWSSystemsManagerNotificationsServicePolicy") – New<br>policy                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Systems Manager added a new policy to allow Systems Manager to send email<br>notifications for just-in-time node access requests to access<br>request approvers.                                                                                                                                                                                                                                                                                                                                                                                                                                     | April 30th, 2025   |
| [AWSSystemsManagerJustInTimeNodeAccessRolePropagationPolicy](#security-iam-awsmanpol-AWSSystemsManagerJustInTimeNodeAccessRolePropagationPolicy "#security-iam-awsmanpol-AWSSystemsManagerJustInTimeNodeAccessRolePropagationPolicy")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                                                         | Systems Manager added a new policy to allow Systems Manager to replicate<br>approval policies to different Regions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | April 30th, 2025   |
| [AWSSystemsManagerJustInTimeAccessTokenPolicy](#security-iam-awsmanpol-AWSSystemsManagerJustInTimeAccessTokenPolicy "#security-iam-awsmanpol-AWSSystemsManagerJustInTimeAccessTokenPolicy") –<br>New policy                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Systems Manager added a new policy to allow Systems Manager to generate<br>access tokens used for just-in-time node access.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | April 30th, 2025   |
| [AWSSystemsManagerJustInTimeAccessServicePolicy](#security-iam-awsmanpol-AWSSystemsManagerJustInTimeAccessServicePolicy "#security-iam-awsmanpol-AWSSystemsManagerJustInTimeAccessServicePolicy") –<br>New policy                                                                                                                                                                                                                                                                                                                                                                                                                                             | Systems Manager added a new policy to provide permissions to AWS<br>resources managed or used by the Systems Manager just-in-time node access<br>feature.                                                                                                                                                                                                                                                                                                                                                                                                                                            | April 30th, 2025   |
| [AWSQuickSetupManageJITNAResourcesExecutionPolicy](#security-iam-awsmanpol-AWSQuickSetupManageJITNAResourcesExecutionPolicy "#security-iam-awsmanpol-AWSQuickSetupManageJITNAResourcesExecutionPolicy")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                                                                                       | Systems Manager added a new policy to allow Quick Setup, a tool in<br>Systems Manager, to create the IAM roles necessary for just-in-time node<br>access.                                                                                                                                                                                                                                                                                                                                                                                                                                            | April 30th, 2025   |
| [AWSQuickSetupJITNADeploymentRolePolicy](#security-iam-awsmanpol-AWSQuickSetupJITNADeploymentRolePolicy "#security-iam-awsmanpol-AWSQuickSetupJITNADeploymentRolePolicy") – New<br>policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Systems Manager added a new policy that provides permissions that<br>allow Quick Setup to deploy the configuration type required to set up<br>just-in-time node access.                                                                                                                                                                                                                                                                                                                                                                                                                              | April 30th, 2025   |
| [AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy](#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy "#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                     | Systems Manager added a new policy that provides permissions for an<br>operational account to diagnose issues with nodes by providing<br>organization-specific permissions.                                                                                                                                                                                                                                                                                                                                                                                                                          | November 21, 2024  |
| [AWS-SSM-RemediationAutomation-OperationalAccountAdministrationRolePolicy](#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-OperationalAccountAdministrationRolePolicy "#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-OperationalAccountAdministrationRolePolicy")<br>– New policy                                                                                                                                                                                                                                                                                                                                                               | Systems Manager added a new policy that provides permissions for an<br>operational account to diagnose issues with nodes by providing<br>organization-specific permissions.                                                                                                                                                                                                                                                                                                                                                                                                                          | November 21, 2024  |
| [AWS-SSM-Automation-DiagnosisBucketPolicy](#security-iam-awsmanpol-AWS-SSM-Automation-DiagnosisBucketPolicy "#security-iam-awsmanpol-AWS-SSM-Automation-DiagnosisBucketPolicy")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Systems Manager added a new policy to support starting Automation<br>workflows that diagnose issues with managed nodes in targeted<br>accounts and Regions.                                                                                                                                                                                                                                                                                                                                                                                                                                          | November 21, 2024  |
| [AmazonSSMServiceRolePolicy](#security-iam-awsmanpol-AmazonSSMServiceRolePolicy "#security-iam-awsmanpol-AmazonSSMServiceRolePolicy") –<br>Update to an existing policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Systems Manager added new permissions to allow AWS Resource Explorer to gather<br>details about Amazon EC2 instances and display the results in widgets in<br>the new Systems Manager Dashboard.                                                                                                                                                                                                                                                                                                                                                                                                     | November 21, 2024  |
| [SSMQuickSetupRolePolicy](#security-iam-awsmanpol-SSMQuickSetupRolePolicy "#security-iam-awsmanpol-SSMQuickSetupRolePolicy") – Update to<br>an existing policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Systems Manager has updated the managed policy<br>`SSMQuickSetupRolePolicy`. This updates allows the<br>associated service-linked role<br>`AWSServiceRoleForSSMQuickSetup` to manage resource data<br>syncs.                                                                                                                                                                                                                                                                                                                                                                                         | November 21, 2024  |
| [AWS-SSM-DiagnosisAutomation-AdministrationRolePolicy](#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-AdministrationRolePolicy "#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-AdministrationRolePolicy") – New policy                                                                                                                                                                                                                                                                                                                                                                                                                              | Systems Manager added a new policy to support starting Automation workflows<br>that diagnose issues with managed nodes in targeted account and<br>Regions.                                                                                                                                                                                                                                                                                                                                                                                                                                           | November 21, 2024  |
| [AWS-SSM-DiagnosisAutomation-ExecutionRolePolicy](#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-ExecutionRolePolicy "#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-ExecutionRolePolicy")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                                                                                          | Systems Manager added a new policy to support starting Automation workflows<br>that diagnose issues with managed nodes in a targeted account and<br>Region.                                                                                                                                                                                                                                                                                                                                                                                                                                          | November 21, 2024  |
| [AWS-SSM-RemediationAutomation-AdministrationRolePolicy](#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-AdministrationRolePolicy "#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-AdministrationRolePolicy")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                                                                     | Systems Manager added a new policy to support starting Automation workflows<br>that remediate issues in managed nodes in targeted accounts and<br>Regions.                                                                                                                                                                                                                                                                                                                                                                                                                                           | November 21, 2024  |
| [AWS-SSM-RemediationAutomation-ExecutionRolePolicy](#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-ExecutionRolePolicy "#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-ExecutionRolePolicy")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                                                                                    | Systems Manager added a new policy to support starting Automation workflows<br>that remediate issues in managed nodes in a targeted account and<br>Region.                                                                                                                                                                                                                                                                                                                                                                                                                                           | November 21, 2024  |
| [AWSQuickSetupSSMDeploymentRolePolicy](#security-iam-awsmanpol-AWSQuickSetupSSMDeploymentRolePolicy "#security-iam-awsmanpol-AWSQuickSetupSSMDeploymentRolePolicy") – Update to<br>an policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Systems Manager added permissions to allow Systems Manager to tag IAM<br>roles and Lambda created for the unified console.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | May 7th, 2025      |
| [AWSQuickSetupSSMManageResourcesExecutionPolicy](#security-iam-awsmanpol-AWSQuickSetupSSMManageResourcesExecutionPolicy "#security-iam-awsmanpol-AWSQuickSetupSSMManageResourcesExecutionPolicy")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                                                                                             | Systems Manager added a new policy to support running an operation in Quick Setup<br>that creates IAM roles for Quick Setup associations, which in turn are<br>created by a `AWSQuickSetupType-SSM` deployment.                                                                                                                                                                                                                                                                                                                                                                                      | November 21, 2024  |
| [AWSQuickSetupSSMLifecycleManagementExecutionPolicy](#security-iam-awsmanpol-AWSQuickSetupSSMLifecycleManagementExecutionPolicy "#security-iam-awsmanpol-AWSQuickSetupSSMLifecycleManagementExecutionPolicy")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                                                                                 | Systems Manager added a new policy to support Quick Setup running a CloudFormation custom<br>resource on lifecycle events during a Quick Setup deployment.                                                                                                                                                                                                                                                                                                                                                                                                                                           | November 21, 2024  |
| [AWSQuickSetupSSMDeploymentRolePolicy](#security-iam-awsmanpol-AWSQuickSetupSSMDeploymentRolePolicy "#security-iam-awsmanpol-AWSQuickSetupSSMDeploymentRolePolicy")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Systems Manager added a new policy to support granting administrative<br>permissions that allow Quick Setup to create resources that are using<br>during the Systems Manager onboarding process.                                                                                                                                                                                                                                                                                                                                                                                                     | November 21, 2024  |
| [AWSQuickSetupSSMDeploymentS3BucketRolePolicy](#security-iam-awsmanpol-AWSQuickSetupSSMDeploymentS3BucketRolePolicy "#security-iam-awsmanpol-AWSQuickSetupSSMDeploymentS3BucketRolePolicy")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Systems Manager added a new policy to support managing and retrieving<br>information about specific buckets in the principal account that are<br>managed through CloudFormation templates                                                                                                                                                                                                                                                                                                                                                                                                            | November 21, 2024  |
| [AWSQuickSetupEnableDHMCExecutionPolicy](#security-iam-awsmanpol-AWSQuickSetupEnableDHMCExecutionPolicy "#security-iam-awsmanpol-AWSQuickSetupEnableDHMCExecutionPolicy")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Systems Manager is introducing a new policy to allow Quick Setup to create an<br>IAM role that itself uses the existing [AmazonSSMManagedEC2InstanceDefaultPolicy](#security-iam-awsmanpol-AmazonSSMManagedEC2InstanceDefaultPolicy "#security-iam-awsmanpol-AmazonSSMManagedEC2InstanceDefaultPolicy").<br>This policy contains all the permissions required for SSM Agent to<br>communicate with Systems Manager service. The new policy also allows modifications<br>to the Systems Manager service settings.                                                                                     | November 21, 2024  |
| [AWSQuickSetupEnableAREXExecutionPolicy](#security-iam-awsmanpol-AWSQuickSetupEnableAREXExecutionPolicy "#security-iam-awsmanpol-AWSQuickSetupEnableAREXExecutionPolicy")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Systems Manager added a new policy to allow Quick Setup to create a service-linked<br>role for AWS Resource Explorer, for accessing Resource Explorer views and aggregator<br>indexes.                                                                                                                                                                                                                                                                                                                                                                                                               | November 21, 2024  |
| [AWSQuickSetupManagedInstanceProfileExecutionPolicy](#security-iam-awsmanpol-AWSQuickSetupManagedInstanceProfileExecutionPolicy "#security-iam-awsmanpol-AWSQuickSetupManagedInstanceProfileExecutionPolicy")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                                                                                 | Systems Manager added a new policy to allow Quick Setup to create a default<br>Quick Setup instance profile and to attach it to any Amazon EC2 instances<br>that lack an associated instance profile. This new policy also<br>allows Quick Setup to attach permissions to existing profiles to ensure<br>that all required Systems Manager permissions have been granted.                                                                                                                                                                                                                            | November 21, 2024  |
| [SSMQuickSetupRolePolicy](#security-iam-awsmanpol-SSMQuickSetupRolePolicy "#security-iam-awsmanpol-SSMQuickSetupRolePolicy") – Update<br>to an existing policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Systems Manager added new permissions to allow Quick Setup to check the<br>health of additional AWS CloudFormation stack sets that it has<br>created.                                                                                                                                                                                                                                                                                                                                                                                                                                                | August 13, 2024    |
| [AmazonSSMManagedEC2InstanceDefaultPolicy](#security-iam-awsmanpol-AmazonSSMManagedEC2InstanceDefaultPolicy "#security-iam-awsmanpol-AmazonSSMManagedEC2InstanceDefaultPolicy")<br>– Update to an existing policy                                                                                                                                                                                                                                                                                                                                                                                                                                             | Systems Manager has added statement IDs (Sids) to the JSON policy for<br>`AmazonSSMManagedEC2InstanceDefaultPolicy`. These Sids<br>provide inline descriptions of the purpose of each policy statement.                                                                                                                                                                                                                                                                                                                                                                                              | July 18, 2024      |
| [SSMQuickSetupRolePolicy](#security-iam-awsmanpol-SSMQuickSetupRolePolicy "#security-iam-awsmanpol-SSMQuickSetupRolePolicy") – New<br>policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Systems Manager added a new policy to allow Quick Setup to check the<br>health of deployed resources and remediate instances that have drifted<br>from the original configuration.                                                                                                                                                                                                                                                                                                                                                                                                                   | July 3, 2024       |
| [AWSQuickSetupDeploymentRolePolicy](#security-iam-awsmanpol-SSMQuickSetupRolePolicy "#security-iam-awsmanpol-SSMQuickSetupRolePolicy") –<br>New policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Systems Manager added a new policy to support multiple Quick Setup<br>configuration types that create IAM roles and automations, which in<br>turn configure frequently used Amazon Web Services services and features with<br>recommended best practices.                                                                                                                                                                                                                                                                                                                                            | July 3, 2024       |
| [AWSQuickSetupPatchPolicyDeploymentRolePolicy](#security-iam-awsmanpol-AWSQuickSetupPatchPolicyDeploymentRolePolicy "#security-iam-awsmanpol-AWSQuickSetupPatchPolicyDeploymentRolePolicy")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Systems Manager added a new policy to allow Quick Setup to create<br>resources associated with Patch Manager patch policy Quick Setup<br>configurations.                                                                                                                                                                                                                                                                                                                                                                                                                                             | July 3, 2024       |
| [AWSQuickSetupPatchPolicyBaselineAccess](#security-iam-awsmanpol-AWSQuickSetupPatchPolicyBaselineAccess "#security-iam-awsmanpol-AWSQuickSetupPatchPolicyBaselineAccess") – New<br>policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Systems Manager added a new policy to allow Quick Setup to access patch<br>baselines in Patch Manager with read-only permissions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | July 3, 2024       |
| [AWSSystemsManagerEnableExplorerExecutionPolicy](#security-iam-awsmanpol-AWSSystemsManagerEnableExplorerExecutionPolicy "#security-iam-awsmanpol-AWSSystemsManagerEnableExplorerExecutionPolicy") – New<br>policy                                                                                                                                                                                                                                                                                                                                                                                                                                             | Systems Manager added a new policy to allow Quick Setup to grant<br>administrative permissions for enabling Explorer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | July 3, 2024       |
| [AWSSystemsManagerEnableConfigRecordingExecutionPolicy](#security-iam-awsmanpol-AWSSystemsManagerEnableConfigRecordingExecutionPolicy "#security-iam-awsmanpol-AWSSystemsManagerEnableConfigRecordingExecutionPolicy")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                                                                        | Systems Manager added a new policy to allow Quick Setup to enable and<br>configure AWS Config configuration recording.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | July 3, 2024       |
| [AWSQuickSetupDevOpsGuruPermissionsBoundary](#security-iam-awsmanpol-AWSQuickSetupDevOpsGuruPermissionsBoundary "#security-iam-awsmanpol-AWSQuickSetupDevOpsGuruPermissionsBoundary") – New<br>policy                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Systems Manager added a new policy to allow Quick Setup to enable and<br>configure Amazon DevOps Guru.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | July 3, 2024       |
| [AWSQuickSetupDistributorPermissionsBoundary](#security-iam-awsmanpol-AWSQuickSetupDistributorPermissionsBoundary "#security-iam-awsmanpol-AWSQuickSetupDistributorPermissionsBoundary") – New<br>policy                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Systems Manager added a new policy to allow Quick Setup to enable and<br>configure Distributor, a tool in AWS Systems Manager.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | July 3, 2024       |
| [AWSQuickSetupSSMHostMgmtPermissionsBoundary](#security-iam-awsmanpol-AWSQuickSetupSSMHostMgmtPermissionsBoundary "#security-iam-awsmanpol-AWSQuickSetupSSMHostMgmtPermissionsBoundary") – New<br>policy                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Systems Manager added a new policy to allow Quick Setup to enable and<br>configure Systems Manager tools for securely managing Amazon EC2 instances.                                                                                                                                                                                                                                                                                                                                                                                                                                                 | July 3, 2024       |
| [AWSQuickSetupPatchPolicyPermissionsBoundary](#security-iam-awsmanpol-AWSQuickSetupPatchPolicyPermissionsBoundary "#security-iam-awsmanpol-AWSQuickSetupPatchPolicyPermissionsBoundary") – New<br>policy                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Systems Manager added a new policy to allow Quick Setup to enable and<br>configure patch policies in Patch Manager, a tool in AWS Systems Manager.                                                                                                                                                                                                                                                                                                                                                                                                                                                   | July 3, 2024       |
| [AWSQuickSetupSchedulerPermissionsBoundary](#security-iam-awsmanpol-AWSQuickSetupSchedulerPermissionsBoundary "#security-iam-awsmanpol-AWSQuickSetupSchedulerPermissionsBoundary") – New<br>policy                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Systems Manager added a new policy to allow Quick Setup to enable and<br>configure scheduled operations on Amazon EC2 instances and other<br>resources.                                                                                                                                                                                                                                                                                                                                                                                                                                              | July 3, 2024       |
| [AWSQuickSetupCFGCPacksPermissionsBoundary](#security-iam-awsmanpol-AWSQuickSetupCFGCPacksPermissionsBoundary "#security-iam-awsmanpol-AWSQuickSetupCFGCPacksPermissionsBoundary") – New<br>policy                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Systems Manager added a new policy to allow Quick Setup to deploy<br>AWS Config conformance packs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | July 3, 2024       |
| [AWSSystemsManagerOpsDataSyncServiceRolePolicy](#security-iam-awsmanpol-AWSSystemsManagerOpsDataSyncServiceRolePolicy "#security-iam-awsmanpol-AWSSystemsManagerOpsDataSyncServiceRolePolicy")<br>– Update to an existing policy                                                                                                                                                                                                                                                                                                                                                                                                                              | OpsCenter updated the policy to improve the security of the service<br>code within the service-linked role for Explorer to manage<br>OpsData-related operations.                                                                                                                                                                                                                                                                                                                                                                                                                                     | July 3, 2023       |
| [AmazonSSMManagedEC2InstanceDefaultPolicy](#security-iam-awsmanpol-AmazonSSMManagedEC2InstanceDefaultPolicy "#security-iam-awsmanpol-AmazonSSMManagedEC2InstanceDefaultPolicy")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Systems Manager added a new policy to allow Systems Manager<br>functionality on Amazon EC2 instances without the use of an IAM<br>instance profile.                                                                                                                                                                                                                                                                                                                                                                                                                                                  | August 18, 2022    |
| [AmazonSSMServiceRolePolicy](#security-iam-awsmanpol-AmazonSSMServiceRolePolicy "#security-iam-awsmanpol-AmazonSSMServiceRolePolicy") – Update to an<br>existing policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Systems Manager added new permissions to allow Explorer to create a<br>managed rule when you turn on Security Hub CSPM from Explorer or OpsCenter. New<br>permissions were added to check that config and the<br>compute-optimizer meet the necessary requirements before allowing<br>OpsData.                                                                                                                                                                                                                                                                                                       | April 27, 2021     |
| [AWSSystemsManagerOpsDataSyncServiceRolePolicy](#security-iam-awsmanpol-AWSSystemsManagerOpsDataSyncServiceRolePolicy "#security-iam-awsmanpol-AWSSystemsManagerOpsDataSyncServiceRolePolicy")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                                                                                                | Systems Manager added a new policy to create and update OpsItems and<br>OpsData from Security Hub CSPM findings in Explorer and OpsCenter.                                                                                                                                                                                                                                                                                                                                                                                                                                                           | April 27, 2021     |
| `AmazonSSMServiceRolePolicy` – Update to<br>an existing policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Systems Manager added new permissions to allow viewing aggregate<br>OpsData and OpsItems details from multiple accounts and AWS Regions<br>in Explorer.                                                                                                                                                                                                                                                                                                                                                                                                                                              | March 24, 2021     |
| Systems Manager started tracking<br>changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Systems Manager started tracking changes for its AWS managed<br>policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | March 12, 2021     |

## Additional managed policies for Systems Manager

In addition to the managed policies described earlier in this topic, the following
policies are also supported by Systems Manager.

- [`AmazonSSMAutomationApproverAccess`](../../../aws-managed-policy/latest/reference/AmazonSSMAutomationApproverAccess.md "../../../aws-managed-policy/latest/reference/AmazonSSMAutomationApproverAccess.md") –
  AWS managed policy that allows access to view automation executions and send
  approval decisions to automation that is waiting for approval.
- [`AmazonSSMDirectoryServiceAccess`](../../../aws-managed-policy/latest/reference/AmazonSSMDirectoryServiceAccess.md "../../../aws-managed-policy/latest/reference/AmazonSSMDirectoryServiceAccess.md") –
  AWS managed policy that that allows SSM Agent to access Directory Service on behalf of the
  user for requests to join the domain by the managed node.
- [`AmazonSSMFullAccess`](../../../aws-managed-policy/latest/reference/AmazonSSMFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonSSMFullAccess.md") – AWS managed
  policy that grants full access to the Systems Manager API and documents.
- [`AmazonSSMMaintenanceWindowRole`](../../../aws-managed-policy/latest/reference/AmazonSSMMaintenanceWindowRole.md "../../../aws-managed-policy/latest/reference/AmazonSSMMaintenanceWindowRole.md") –
  AWS managed policy that provides maintenance windows with permissions to the
  Systems Manager API.
- [`AmazonSSMManagedInstanceCore`](../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md "../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md") –
  AWS managed policy that allows a node to use Systems Manager service core
  functionality.
- [`AmazonSSMPatchAssociation`](../../../aws-managed-policy/latest/reference/AmazonSSMPatchAssociation.md "../../../aws-managed-policy/latest/reference/AmazonSSMPatchAssociation.md") – AWS
  managed policy that provides access to child instances for patch association
  operations.
- [`AmazonSSMReadOnlyAccess`](../../../aws-managed-policy/latest/reference/AmazonSSMReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AmazonSSMReadOnlyAccess.md") – AWS
  managed policy that grants access to Systems Manager read-only API operations,
  such as `Get*` and `List*`.
- [`AWSSSMOpsInsightsServiceRolePolicy`](../../../aws-managed-policy/latest/reference/AWSSSMOpsInsightsServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSSSMOpsInsightsServiceRolePolicy.md")
  – AWS managed policy that provides permissions for creating and
  updating operational insight _OpsItems_ in
  Systems Manager. Used to provide permissions through the service-linked role
  [AWSServiceRoleForAmazonSSM_OpsInsights](using-service-linked-roles-service-action-4.md "using-service-linked-roles-service-action-4.md").
- [`AWSSystemsManagerAccountDiscoveryServicePolicy`](../../../aws-managed-policy/latest/reference/AWSSystemsManagerAccountDiscoveryServicePolicy.md "../../../aws-managed-policy/latest/reference/AWSSystemsManagerAccountDiscoveryServicePolicy.md")
  – AWS managed policy that grants Systems Manager permission to discover
  AWS account information.
- [`AmazonEC2RoleforSSM`](../../../aws-managed-policy/latest/reference/AmazonEC2RoleforSSM.md "../../../aws-managed-policy/latest/reference/AmazonEC2RoleforSSM.md") – This policy
  is no longer supported and should not be used. In its place, use the
  `AmazonSSMManagedInstanceCore` policy to allow
  Systems Manager service core functionality on EC2 instances. For information,
  see [Configure instance permissions required for Systems Manager](setup-instance-permissions.md "setup-instance-permissions.md").
