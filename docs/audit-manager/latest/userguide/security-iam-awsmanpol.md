# AWS managed policies for AWS Audit Manager

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

- [AWS managed policy: AWSAuditManagerAdministratorAccess](#security-iam-awsmanpol-AWSAuditManagerAdministratorAccess "#security-iam-awsmanpol-AWSAuditManagerAdministratorAccess")
- [AWS managed policy: AWSAuditManagerServiceRolePolicy](#security-iam-awsmanpol-AWSAuditManagerServiceRolePolicy "#security-iam-awsmanpol-AWSAuditManagerServiceRolePolicy")
- [AWS Audit Manager updates to AWS managed
  policies](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")

## AWS managed policy: AWSAuditManagerAdministratorAccess

You can attach the `AWSAuditManagerAdministratorAccess` policy to your
IAM identities.

This policy grants administrative permissions that allow full administration
access to AWS Audit Manager. This access includes the ability to enable and disable AWS Audit Manager,
change settings in AWS Audit Manager, and manage all Audit Manager resources such as assessments,
frameworks, controls, and assessment reports.

AWS Audit Manager requires broad permissions across multiple AWS services. This is
because AWS Audit Manager integrates with multiple AWS services to collect evidence
automatically from the AWS account and services in scope of an assessment.

**Permissions details**

This policy includes the following permissions:

- `Audit Manager` – Allows principals full permissions on AWS Audit Manager
  resources.
- `Organizations` – Allows principals to list accounts and
  organizational units, and to register or deregister a delegated
  administrator. This is required so that you can enable multi-account support
  and allow AWS Audit Manager to run assessments over multiple accounts and consolidate
  evidence into a delegated administrator account.
- `iam` – Allows principals to get and list users in IAM
  and create a service-linked role. This is required so that you can designate
  audit owners and delegates for an assessment. This policy also allows
  principals to delete the service-linked role and retrieve the deletion
  status. This is required so that AWS Audit Manager can clean up resources and delete
  the service-linked role for you when you choose to disable the service in
  the AWS Management Console.
- `s3` – Allows principals to list available Amazon Simple Storage Service
  (Amazon S3) buckets. This capability is required so that you can designate the S3
  bucket in which you want to store evidence reports or upload manual
  evidence.
- `kms` – Allows principals to list and describe keys,
  list aliases, and create grants. This is required so that you can choose
  customer managed keys for data encryption.
- `sns` – Allows principals to list subscription topics in
  Amazon SNS. This is required so that you can specify which SNS topic you want
  AWS Audit Manager to send notifications to.
- `events` – Allows principals to list and manage checks
  from AWS Security Hub. This is required so that AWS Audit Manager can automatically collect
  AWS Security Hub findings for the AWS services that are monitored by AWS Security Hub.
  It can then convert this data into evidence to be included in your AWS Audit Manager
  assessments.
- `tag` – Allows principals to retrieve tagged resources.
  This is required so that you can use tags as a search filter when browsing
  frameworks, controls, and assessments in AWS Audit Manager.
- `controlcatalog` – Allows principals to list the
  domains, objectives, and common controls that are provided by AWS Control
  Catalog. This is required so that you can use the common controls feature in
  AWS Audit Manager. With these permissions in place, you can view a list of common
  controls in the AWS Audit Manager control library, and filter controls by domain and
  objective. You can also use common controls as an evidence source when you
  create a custom control.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AuditManagerAccess",
 "Effect": "Allow",
 "Action": [
 "auditmanager:*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "OrganizationsAccess",
 "Effect": "Allow",
 "Action": [
 "organizations:ListAccountsForParent",
 "organizations:ListAccounts",
 "organizations:DescribeOrganization",
 "organizations:DescribeOrganizationalUnit",
 "organizations:DescribeAccount",
 "organizations:ListParents",
 "organizations:ListChildren"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowOnlyAuditManagerIntegration",
 "Effect": "Allow",
 "Action": [
 "organizations:RegisterDelegatedAdministrator",
 "organizations:DeregisterDelegatedAdministrator",
 "organizations:EnableAWSServiceAccess"
 ],
 "Resource": "*",
 "Condition": {
 "StringLikeIfExists": {
 "organizations:ServicePrincipal": [
 "auditmanager.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "IAMAccess",
 "Effect": "Allow",
 "Action": [
 "iam:GetUser",
 "iam:ListUsers",
 "iam:ListRoles"
 ],
 "Resource": "*"
 },
 {
 "Sid": "IAMAccessCreateSLR",
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/auditmanager.amazonaws.com/AWSServiceRoleForAuditManager*",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "auditmanager.amazonaws.com"
 }
 }
 },
 {
 "Sid": "IAMAccessManageSLR",
 "Effect": "Allow",
 "Action": [
 "iam:DeleteServiceLinkedRole",
 "iam:UpdateRoleDescription",
 "iam:GetServiceLinkedRoleDeletionStatus"
 ],
 "Resource": "arn:aws:iam::*:role/aws-service-role/auditmanager.amazonaws.com/AWSServiceRoleForAuditManager*"
 },
 {
 "Sid": "S3Access",
 "Effect": "Allow",
 "Action": [
 "s3:ListAllMyBuckets"
 ],
 "Resource": "*"
 },
 {
 "Sid": "KmsAccess",
 "Effect": "Allow",
 "Action": [
 "kms:DescribeKey",
 "kms:ListKeys",
 "kms:ListAliases"
 ],
 "Resource": "*"
 },
 {
 "Sid": "KmsCreateGrantAccess",
 "Effect": "Allow",
 "Action": [
 "kms:CreateGrant"
 ],
 "Resource": "*",
 "Condition": {
 "Bool": {
 "kms:GrantIsForAWSResource": "true"
 },
 "StringLike": {
 "kms:ViaService": "auditmanager.*.amazonaws.com"
 }
 }
 },
 {
 "Sid": "SNSAccess",
 "Effect": "Allow",
 "Action": [
 "sns:ListTopics"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CreateEventsAccess",
 "Effect": "Allow",
 "Action": [
 "events:PutRule"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "events:detail-type": "Security Hub Findings - Imported"
 },
 "ForAllValues:StringEquals": {
 "events:source": [
 "aws.securityhub"
 ]
 }
 }
 },
 {
 "Sid": "EventsAccess",
 "Effect": "Allow",
 "Action": [
 "events:DeleteRule",
 "events:DescribeRule",
 "events:EnableRule",
 "events:DisableRule",
 "events:ListTargetsByRule",
 "events:PutTargets",
 "events:RemoveTargets"
 ],
 "Resource": "arn:aws:events:*:*:rule/AuditManagerSecurityHubFindingsReceiver"
 },
 {
 "Sid": "TagAccess",
 "Effect": "Allow",
 "Action": [
 "tag:GetResources"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ControlCatalogAccess",
 "Effect": "Allow",
 "Action": [
 "controlcatalog:ListCommonControls",
 "controlcatalog:ListDomains",
 "controlcatalog:ListObjectives"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy: AWSAuditManagerServiceRolePolicy

You can't attach `AWSAuditManagerServiceRolePolicy` to your IAM
entities. This policy is attached to a service-linked role,
`AWSServiceRoleForAuditManager`, that allows AWS Audit Manager to perform
actions on your behalf. For more information, see [Using service-linked roles for AWS Audit Manager](using-service-linked-roles.md "using-service-linked-roles.md").

The role permissions policy, `AWSAuditManagerServiceRolePolicy`, allows
AWS Audit Manager to collect automated evidence by doing the following on your behalf:

- Collect data from the following data sources:
  - Management events from AWS CloudTrail
  - Compliance checks from AWS Config Rules
  - Compliance checks from AWS Security Hub

- Use API calls to describe your resource configurations for the following
  AWS services.

###### Tip

For more information about the API calls that Audit Manager uses to collect
evidence from these services, see [Supported API calls for custom
control data sources](control-data-sources-api.md#apis-for-custom-control-data-sources "control-data-sources-api.md#apis-for-custom-control-data-sources") in this
guide.

    + Amazon API Gateway
    + AWS Backup
    + Amazon Bedrock
    + AWS Certificate Manager
    + Amazon CloudFront
    + AWS CloudTrail
    + Amazon CloudWatch
    + Amazon CloudWatch Logs
    + Amazon Cognito user pools
    + AWS Config
    + Amazon Data Firehose
    + AWS Direct Connect
    + Amazon DynamoDB
    + Amazon EC2
    + Amazon EC2 Auto Scaling
    + Amazon Elastic Container Service
    + Amazon Elastic File System
    + Amazon Elastic Kubernetes Service
    + Amazon ElastiCache
    + Elastic Load Balancing
    + Amazon EMR
    + Amazon EventBridge
    + Amazon FSx
    + Amazon GuardDuty
    + AWS Identity and Access Management (IAM)
    + Amazon Kinesis
    + AWS KMS
    + AWS Lambda
    + AWS License Manager
    + Amazon Managed Streaming for Apache Kafka
    + Amazon OpenSearch Service
    + AWS Organizations
    + Amazon Relational Database Service
    + Amazon Redshift
    + Amazon Route 53
    + Amazon S3
    + Amazon SageMaker AI
    + AWS Secrets Manager
    + AWS Security Hub
    + Amazon Simple Notification Service
    + Amazon Simple Queue Service
    + AWS WAF

**Permissions details**

`AWSAuditManagerServiceRolePolicy` allows AWS Audit Manager to complete the
following actions on the specified resources:

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
- `iam:ListGroupsForUser`
- `iam:ListGroupPolicies`
- `iam:ListGroups`
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

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "acm:GetAccountConfiguration",
 "acm:ListCertificates",
 "autoscaling:DescribeAutoScalingGroups",
 "backup:ListBackupPlans",
 "backup:ListRecoveryPointsByResource",
 "bedrock:GetCustomModel",
 "bedrock:GetFoundationModel",
 "bedrock:GetModelCustomizationJob",
 "bedrock:GetModelInvocationLoggingConfiguration",
 "bedrock:ListCustomModels",
 "bedrock:ListFoundationModels",
 "bedrock:ListGuardrails",
 "bedrock:ListModelCustomizationJobs",
 "cloudfront:GetDistribution",
 "cloudfront:GetDistributionConfig",
 "cloudfront:ListDistributions",
 "cloudtrail:GetTrail",
 "cloudtrail:ListTrails",
 "cloudtrail:DescribeTrails",
 "cloudtrail:LookupEvents",
 "cloudwatch:DescribeAlarms",
 "cloudwatch:DescribeAlarmsForMetric",
 "cloudwatch:GetMetricStatistics",
 "cloudwatch:ListMetrics",
 "cognito-idp:DescribeUserPool",
 "config:DescribeConfigRules",
 "config:DescribeDeliveryChannels",
 "config:ListDiscoveredResources",
 "directconnect:DescribeDirectConnectGateways",
 "directconnect:DescribeVirtualGateways",
 "dynamodb:DescribeContinuousBackups",
 "dynamodb:DescribeBackup",
 "dynamodb:DescribeTableReplicaAutoScaling",
 "dynamodb:DescribeTable",
 "dynamodb:ListBackups",
 "dynamodb:ListGlobalTables",
 "dynamodb:ListTables",
 "ec2:DescribeInstanceCreditSpecifications",
 "ec2:DescribeInstanceAttribute",
 "ec2:DescribeSecurityGroupRules",
 "ec2:DescribeVpcEndpointConnections",
 "ec2:DescribeVpcEndpointServiceConfigurations",
 "ec2:GetLaunchTemplateData",
 "ec2:DescribeAddresses",
 "ec2:DescribeCustomerGateways",
 "ec2:DescribeEgressOnlyInternetGateways",
 "ec2:DescribeFlowLogs",
 "ec2:DescribeInstances",
 "ec2:DescribeInternetGateways",
 "ec2:DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations",
 "ec2:DescribeLocalGateways",
 "ec2:DescribeLocalGatewayVirtualInterfaces",
 "ec2:DescribeNatGateways",
 "ec2:DescribeNetworkAcls",
 "ec2:DescribeRouteTables",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSnapshots",
 "ec2:DescribeTransitGateways",
 "ec2:DescribeVolumes",
 "ec2:DescribeVpcEndpoints",
 "ec2:DescribeVpcPeeringConnections",
 "ec2:DescribeVpcs",
 "ec2:DescribeVpnConnections",
 "ec2:DescribeVpnGateways",
 "ec2:GetEbsDefaultKmsKeyId",
 "ec2:GetEbsEncryptionByDefault",
 "ecs:DescribeClusters",
 "eks:DescribeAddonVersions",
 "elasticache:DescribeCacheClusters",
 "elasticache:DescribeServiceUpdates",
 "elasticfilesystem:DescribeAccessPoints",
 "elasticfilesystem:DescribeFileSystems",
 "elasticloadbalancing:DescribeLoadBalancers",
 "elasticloadbalancing:DescribeSslPolicies",
 "elasticloadbalancing:DescribeTargetGroups",
 "elasticmapreduce:ListClusters",
 "elasticmapreduce:ListSecurityConfigurations",
 "events:DescribeRule",
 "events:ListConnections",
 "events:ListEventBuses",
 "events:ListEventSources",
 "events:ListRules",
 "firehose:ListDeliveryStreams",
 "fsx:DescribeFileSystems",
 "guardduty:ListDetectors",
 "iam:GenerateCredentialReport",
 "iam:GetAccountAuthorizationDetails",
 "iam:GetAccessKeyLastUsed",
 "iam:GetCredentialReport",
 "iam:GetGroupPolicy",
 "iam:GetPolicy",
 "iam:GetPolicyVersion",
 "iam:GetRolePolicy",
 "iam:GetUser",
 "iam:GetUserPolicy",
 "iam:GetAccountPasswordPolicy",
 "iam:GetAccountSummary",
 "iam:ListAttachedGroupPolicies",
 "iam:ListAttachedUserPolicies",
 "iam:ListEntitiesForPolicy",
 "iam:ListGroupsForUser",
 "iam:ListGroupPolicies",
 "iam:ListGroups",
 "iam:ListOpenIdConnectProviders",
 "iam:ListPolicies",
 "iam:ListRolePolicies",
 "iam:ListRoles",
 "iam:ListSamlProviders",
 "iam:ListUserPolicies",
 "iam:ListUsers",
 "iam:ListVirtualMFADevices",
 "iam:ListPolicyVersions",
 "iam:ListAccessKeys",
 "iam:ListAttachedRolePolicies",
 "iam:ListMfaDeviceTags",
 "iam:ListMfaDevices",
 "kafka:ListClusters",
 "kafka:ListKafkaVersions",
 "kinesis:ListStreams",
 "kms:DescribeKey",
 "kms:GetKeyPolicy",
 "kms:GetKeyRotationStatus",
 "kms:ListGrants",
 "kms:ListKeyPolicies",
 "kms:ListKeys",
 "lambda:ListFunctions",
 "license-manager:ListAssociationsForLicenseConfiguration",
 "license-manager:ListLicenseConfigurations",
 "license-manager:ListUsageForLicenseConfiguration",
 "logs:DescribeDestinations",
 "logs:DescribeExportTasks",
 "logs:DescribeLogGroups",
 "logs:DescribeMetricFilters",
 "logs:DescribeResourcePolicies",
 "logs:FilterLogEvents",
 "logs:GetDataProtectionPolicy",
 "es:DescribeDomains",
 "es:DescribeDomain",
 "es:DescribeDomainConfig",
 "es:ListDomainNames",
 "organizations:DescribeOrganization",
 "organizations:DescribePolicy",
 "rds:DescribeCertificates",
 "rds:DescribeDBClusterEndpoints",
 "rds:DescribeDBClusterParameterGroups",
 "rds:DescribeDBInstances",
 "rds:DescribeDBSecurityGroups",
 "rds:DescribeDBClusters",
 "rds:DescribeDBInstanceAutomatedBackups",
 "redshift:DescribeClusters",
 "redshift:DescribeClusterSnapshots",
 "redshift:DescribeLoggingStatus",
 "route53:GetQueryLoggingConfig",
 "sagemaker:DescribeAlgorithm",
 "sagemaker:DescribeFlowDefinition",
 "sagemaker:DescribeHumanTaskUi",
 "sagemaker:DescribeModelBiasJobDefinition",
 "sagemaker:DescribeModelCard",
 "sagemaker:DescribeModelQualityJobDefinition",
 "sagemaker:DescribeDomain",
 "sagemaker:DescribeEndpoint",
 "sagemaker:DescribeEndpointConfig",
 "sagemaker:DescribeLabelingJob",
 "sagemaker:DescribeModel",
 "sagemaker:DescribeTrainingJob",
 "sagemaker:DescribeUserProfile",
 "sagemaker:ListAlgorithms",
 "sagemaker:ListDomains",
 "sagemaker:ListEndpoints",
 "sagemaker:ListEndpointConfigs",
 "sagemaker:ListFlowDefinitions",
 "sagemaker:ListHumanTaskUis",
 "sagemaker:ListLabelingJobs",
 "sagemaker:ListModels",
 "sagemaker:ListModelBiasJobDefinitions",
 "sagemaker:ListModelCards",
 "sagemaker:ListModelQualityJobDefinitions",
 "sagemaker:ListMonitoringAlerts",
 "sagemaker:ListMonitoringSchedules",
 "sagemaker:ListTrainingJobs",
 "sagemaker:ListUserProfiles",
 "s3:GetBucketPublicAccessBlock",
 "s3:GetBucketVersioning",
 "s3:GetEncryptionConfiguration",
 "s3:GetLifecycleConfiguration",
 "s3:ListAllMyBuckets",
 "secretsmanager:DescribeSecret",
 "secretsmanager:ListSecrets",
 "securityhub:DescribeStandards",
 "sns:ListTagsForResource",
 "sns:ListTopics",
 "sqs:ListQueues",
 "waf-regional:GetRule",
 "waf-regional:GetWebAcl",
 "waf:GetRule",
 "waf:GetRuleGroup",
 "waf:ListActivatedRulesInRuleGroup",
 "waf:ListWebAcls",
 "wafv2:ListWebAcls",
 "waf-regional:GetLoggingConfiguration",
 "waf-regional:ListRuleGroups",
 "waf-regional:ListSubscribedRuleGroups",
 "waf-regional:ListWebACLs",
 "waf-regional:ListRules",
 "waf:ListRuleGroups",
 "waf:ListRules"
 ],
 "Resource": "*",
 "Sid": "APIsAccess"
 },
 {
 "Sid": "S3Access",
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketAcl",
 "s3:GetBucketLogging",
 "s3:GetBucketOwnershipControls",
 "s3:GetBucketPolicy",
 "s3:GetBucketTagging"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": [
 "${aws:PrincipalAccount}"
 ]
 }
 }
 },
 {
 "Sid": "APIGatewayAccess",
 "Effect": "Allow",
 "Action": [
 "apigateway:GET"
 ],
 "Resource": [
 "arn:aws:apigateway:*::/restapis",
 "arn:aws:apigateway:*::/restapis/*/stages/*",
 "arn:aws:apigateway:*::/restapis/*/stages"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": [
 "${aws:PrincipalAccount}"
 ]
 }
 }
 },
 {
 "Sid": "CreateEventsAccess",
 "Effect": "Allow",
 "Action": [
 "events:PutRule"
 ],
 "Resource": "arn:aws:events:*:*:rule/AuditManagerSecurityHubFindingsReceiver",
 "Condition": {
 "StringEquals": {
 "events:detail-type": "Security Hub Findings - Imported"
 },
 "Null": {
 "events:source": "false"
 },
 "ForAllValues:StringEquals": {
 "events:source": [
 "aws.securityhub"
 ]
 }
 }
 },
 {
 "Sid": "EventsAccess",
 "Effect": "Allow",
 "Action": [
 "events:DeleteRule",
 "events:DescribeRule",
 "events:EnableRule",
 "events:DisableRule",
 "events:ListTargetsByRule",
 "events:PutTargets",
 "events:RemoveTargets"
 ],
 "Resource": "arn:aws:events:*:*:rule/AuditManagerSecurityHubFindingsReceiver"
 }
 ]
}`

```

## AWS Audit Manager updates to AWS managed

policies

View details about updates to AWS managed policies for AWS Audit Manager since this
service began tracking these changes. For automatic alerts about changes to this
page, subscribe to the RSS feed on the AWS Audit Manager [Document history](doc-history.md "doc-history.md")
page.

| Change                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Date       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| [AWSAuditManagerServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSAuditManagerServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSAuditManagerServiceRolePolicy") – Update to an<br>existing policy       | The service-linked role now allows AWS Audit Manager to perform the<br>`bedrock:ListGuardrails` action.<br>This API action is required to support the [AWS Generative AI Best Practices<br>Framework v2](aws-generative-ai-best-practices.md "aws-generative-ai-best-practices.md"). It<br>allows Audit Manager to collect automated evidence about the guardrails<br>that are in place for your generative AI model data training<br>data sets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 09/24/2024 |
| [AWSAuditManagerServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSAuditManagerServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSAuditManagerServiceRolePolicy") – Update to an<br>existing policy       | We added the following permissions to<br>`AWSAuditManagerServiceRolePolicy`. AWS Audit Manager can now<br>perform the following actions to collect automated evidence about<br>the resources in your AWS account.<br>• `sagemaker:DescribeAlgorithm`<br>• `sagemaker:DescribeDomain`<br>• `sagemaker:DescribeEndpoint`<br>• `sagemaker:DescribeFlowDefinition`<br>• `sagemaker:DescribeHumanTaskUi`<br>• `sagemaker:DescribeLabelingJob`<br>• `sagemaker:DescribeModel`<br>• `sagemaker:DescribeModelBiasJobDefinition`<br>• `sagemaker:DescribeModelCard`<br>• `sagemaker:DescribeModelQualityJobDefinition`<br>• `sagemaker:DescribeTrainingJob`<br>• `sagemaker:DescribeUserProfile`<br>• `sagemaker:ListAlgorithms`<br>• `sagemaker:ListDomains`<br>• `sagemaker:ListEndpoints`<br>• `sagemaker:ListFlowDefinitions`<br>• `sagemaker:ListHumanTaskUis`<br>• `sagemaker:ListLabelingJobs`<br>• `sagemaker:ListModels`<br>• `sagemaker:ListModelBiasJobDefinitions`<br>• `sagemaker:ListModelCards`<br>• `sagemaker:ListModelQualityJobDefinitions`<br>• `sagemaker:ListMonitoringAlerts`<br>• `sagemaker:ListMonitoringSchedules`<br>• `sagemaker:ListTrainingJobs`<br>• `sagemaker:ListUserProfiles`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 06/10/2024 |
| [AWSAuditManagerServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSAuditManagerServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSAuditManagerServiceRolePolicy") – Update to an<br>existing policy       | We added the following permissions to<br>`AWSAuditManagerServiceRolePolicy`. AWS Audit Manager can now<br>perform the following actions to collect automated evidence about<br>the resources in your AWS account.<br>• `iam:ListAttachedGroupPolicies`<br>• `iam:ListAttachedUserPolicies`<br>• `iam:ListGroupsForUser`<br>• `es:ListDomainNames`<br>We also added a new resource in the<br>`APIGatewayAccess` section of the policy<br>(`arn:aws:apigateway:*::/restapis`).The<br>policy now grants the specified permission (in this case, the<br>`apigateway:GET` action) not only on the stages<br>and stage resources of API Gateway REST APIs, but also on the<br>REST APIs themselves. This change effectively expands the scope<br>of the policy to include the ability to retrieve information<br>about the API Gateway REST APIs themselves, in addition to the<br>stages and stage resources associated with those<br>APIs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 05/17/2024 |
| [AWSAuditManagerAdministratorAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSAuditManagerAdministratorAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSAuditManagerAdministratorAccess") – Update to<br>an existing policy | We added the following permissions to<br>`AWSAuditManagerAdministratorAccess`:<br>• `controlcatalog:ListCommonControls`<br>• `controlcatalog:ListDomains`<br>• `controlcatalog:ListObjectives`<br>This update allows you to view the control<br>domains, control objectives, and common controls that are<br>provided by AWS Control Catalog. These permissions are<br>required if you want to use the common controls feature in<br>AWS Audit Manager.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 05/15/2024 |
| [AWSAuditManagerServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSAuditManagerServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSAuditManagerServiceRolePolicy")<br>– Update to an existing policy       | We added the following permissions to<br>`AWSAuditManagerServiceRolePolicy`. AWS Audit Manager can now<br>perform the following actions to collect automated evidence about<br>the resources in your AWS account.<br>• `apigateway:GET`<br>• `autoscaling:DescribeAutoScalingGroups`<br>• `backup:ListBackupPlans`<br>• `cloudfront:GetDistribution`<br>• `cloudfront:GetDistributionConfig`<br>• `cloudfront:ListDistributions`<br>• `cloudtrail:GetTrail`<br>• `cloudtrail:ListTrails`<br>• `dynamodb:DescribeContinuousBackups`<br>• `dynamodb:DescribeBackup`<br>• `dynamodb:DescribeTableReplicaAutoScaling`<br>• `ec2:DescribeInstanceCreditSpecifications`<br>• `ec2:DescribeInstanceAttribute`<br>• `ec2:DescribeSecurityGroupRules`<br>• `ec2:DescribeVpcEndpointConnections`<br>• `ec2:DescribeVpcEndpointServiceConfigurations`<br>• `ec2:GetLaunchTemplateData`<br>• `es:DescribeDomains`<br>• `es:DescribeDomain`<br>• `es:DescribeDomainConfig`<br>• `iam:GetAccessKeyLastUsed`<br>• `iam:GetGroupPolicy`<br>• `iam:GetPolicy`<br>• `iam:GetPolicyVersion`<br>• `iam:GetRolePolicy`<br>• `iam:GetUser`<br>• `iam:GetUserPolicy`<br>• `iam:ListAccessKeys`<br>• `iam:ListAttachedRolePolicies`<br>• `iam:ListMfaDeviceTags`<br>• `iam:ListMfaDevices`<br>• `iam:ListPolicyVersions`<br>• `logs:GetDataProtectionPolicy`<br>• `rds:DescribeDBInstanceAutomatedBackups`<br>• `rds:DescribeDBClusterEndpoints`<br>• `rds:DescribeDBClusterParameterGroups`<br>• `redshift:DescribeClusterSnapshots`<br>• `redshift:DescribeLoggingStatus`<br>• `s3:GetBucketAcl`<br>• `s3:GetBucketLogging`<br>• `s3:GetBucketOwnershipControls`<br>• `s3:GetBucketTagging`<br>• `sagemaker:DescribeEndpointConfig`<br>• `sagemaker:ListEndpointConfigs`<br>• `secretsmanager:DescribeSecret`<br>• `secretsmanager:ListSecrets`<br>• `sns:ListTagsForResource`<br>• `waf-regional:GetRule`<br>• `waf-regional:GetWebAcl`<br>• `waf-regional:ListRules`<br>• `waf:GetRule`<br>• `waf:GetRuleGroup`<br>• `waf:ListRuleGroups`<br>• `waf:ListRules`<br>• `waf:ListWebAcls`<br>• `wafv2:ListWebAcls`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 05/15/2024 |
| [AWSAuditManagerServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSAuditManagerServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSAuditManagerServiceRolePolicy")<br>– Update to an existing policy       | The service-linked role now allows AWS Audit Manager to perform the<br>`s3:GetBucketPolicy` action.<br>This API action is required to support the [AWS Generative AI Best Practices<br>Framework v2](aws-generative-ai-best-practices.md "aws-generative-ai-best-practices.md"). It<br>allows Audit Manager to collect automated evidence about the policy<br>restrictions that are in place for your generative AI model data<br>training data sets.<br>The `GetBucketPolicy` action operates within the<br>scope of the AWS account where the service-linked-role is<br>available. It can't access cross-account bucket policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 12/06/2023 |
| [AWSAuditManagerServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSAuditManagerServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSAuditManagerServiceRolePolicy")<br>– Update to an existing policy       | We added the following permissions to<br>`AWSAuditManagerServiceRolePolicy`. AWS Audit Manager can now<br>perform the following actions to collect automated evidence about<br>the resources in your AWS account.<br>• `acm:GetAccountConfiguration`<br>• `acm:ListCertificates`<br>• `backup:ListRecoveryPointsByResource`<br>• `bedrock:GetCustomModel`<br>• `bedrock:GetFoundationModel`<br>• `bedrock:GetModelCustomizationJob`<br>• `bedrock:GetModelInvocationLoggingConfiguration`<br>• `bedrock:ListCustomModels`<br>• `bedrock:ListFoundationModels`<br>• `bedrock:ListModelCustomizationJobs`<br>• `cloudtrail:LookupEvents`<br>• `cloudwatch:DescribeAlarmsForMetric`<br>• `cloudwatch:GetMetricStatistics`<br>• `cloudwatch:ListMetrics`<br>• `directconnect:DescribeDirectConnectGateways`<br>• `directconnect:DescribeVirtualGateways`<br>• `dynamodb:ListBackups`<br>• `dynamodb:ListGlobalTables`<br>• `ec2:DescribeAddresses`<br>• `ec2:DescribeCustomerGateways`<br>• `ec2:DescribeEgressOnlyInternetGateways`<br>• `ec2:DescribeInternetGateways`<br>• `ec2:DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations`<br>• `ec2:DescribeLocalGateways`<br>• `ec2:DescribeLocalGatewayVirtualInterfaces`<br>• `ec2:DescribeNatGateways`<br>• `ec2:DescribeTransitGateways`<br>• `ec2:DescribeVpcPeeringConnections`<br>• `ec2:DescribeVpnConnections`<br>• `ec2:DescribeVpnGateways`<br>• `ec2:GetEbsDefaultKmsKeyId`<br>• `ec2:GetEbsEncryptionByDefault`<br>• `ecs:DescribeClusters`<br>• `eks:DescribeAddonVersions`<br>• `elasticache:DescribeCacheClusters`<br>• `elasticache:DescribeServiceUpdates`<br>• `elasticfilesystem:DescribeAccessPoints`<br>• `elasticloadbalancing:DescribeLoadBalancers`<br>• `elasticloadbalancing:DescribeSslPolicies`<br>• `elasticloadbalancing:DescribeTargetGroups`<br>• `elasticmapreduce:ListClusters`<br>• `elasticmapreduce:ListSecurityConfigurations`<br>• `events:ListConnections`<br>• `events:ListEventBuses`<br>• `events:ListEventSources`<br>• `events:ListRules`<br>• `firehose:ListDeliveryStreams`<br>• `fsx:DescribeFileSystems`<br>• `iam:GetAccountPasswordPolicy`<br>• `iam:GetCredentialReport`<br>• `iam:ListOpenIdConnectProviders`<br>• `iam:ListSamlProviders`<br>• `iam:ListVirtualMFADevices`<br>• `kafka:ListClusters`<br>• `kafka:ListKafkaVersions`<br>• `kinesis:ListStreams`<br>• `lambda:ListFunctions`<br>• `logs:DescribeDestinations`<br>• `logs:DescribeExportTasks`<br>• `logs:DescribeLogGroups`<br>• `logs:DescribeMetricFilters`<br>• `logs:DescribeResourcePolicies`<br>• `logs:FilterLogEvents`<br>• `rds:DescribeCertificates`<br>• `rds:DescribeDbClusterEndpoints`<br>• `rds:DescribeDbClusterParameterGroups`<br>• `rds:DescribeDbClusters`<br>• `rds:DescribeDbSecurityGroups`<br>• `redshift:DescribeClusters`<br>• `s3:GetBucketPublicAccessBlock`<br>• `s3:GetBucketVersioning`<br>• `sns:ListTopics`<br>• `sqs:ListQueues`<br>• `waf-regional:GetLoggingConfiguration`<br>• `waf-regional:ListRuleGroups`<br>• `waf-regional:ListSubscribedRuleGroups`<br>• `waf-regional:ListWebACLs` | 11/06/2023 |
| [AWSAuditManagerServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSAuditManagerServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSAuditManagerServiceRolePolicy")<br>– Update to an existing policy       | We added the following permissions to<br>`AWSAuditManagerServiceRolePolicy`:<br>• `dynamodb:DescribeTable`<br>• `dynamodb:ListTables`<br>• `ec2:DescribeVolumes`<br>• `kms:GetKeyPolicy`<br>• `kms:GetKeyRotationStatus`<br>• `kms:ListKeyPolicies`<br>• `rds:DescribeDBInstances`<br>• `redshift:DescribeClusters`<br>• `s3:GetEncryptionConfiguration`<br>• `s3:ListAllMyBuckets`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 07/07/2022 |
| [AWSAuditManagerServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSAuditManagerServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSAuditManagerServiceRolePolicy") – Update to<br>an existing policy       | The service-linked role now allows AWS Audit Manager to perform the<br>`organizations:DescribeOrganization`<br>action.<br>We also scoped down the `CreateEventsAccess`<br>resource from a wildcard (`*`) to a specific type of<br>resource<br>(`arn:aws:events:*:*:rule/AuditManagerSecurityHubFindingsReceiver`).<br>Lastly, we added a `Null` condition operator for<br>the `events:source` condition key to confirm that a<br>source value exists and its value is not null.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 05/20/2022 |
| [AWSAuditManagerAdministratorAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSAuditManagerAdministratorAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSAuditManagerAdministratorAccess") – Update<br>to an existing policy | We updated the key condition policy for<br>`events:source` to reflect that this is a<br>multi-valued key.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 04/29/2022 |
| [AWSAuditManagerServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSAuditManagerServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSAuditManagerServiceRolePolicy") – Update to<br>an existing policy       | We updated the key condition policy for<br>`events:source` to reflect that this is a<br>multi-valued key.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 03/16/2022 |
| AWS Audit Manager started tracking changes                                                                                                                                                                                                        | AWS Audit Manager started tracking changes for its AWS managed<br>policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 05/06/2021 |
