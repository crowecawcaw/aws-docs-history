# AWS managed policies for

AWS Trusted Advisor

Trusted Advisor has the following AWS managed policies.

###### Contents

- [AWS managed
  policy: AWSTrustedAdvisorPriorityFullAccess](aws-managed-policies-for-trusted-advisor.md#security-iam-support-TA-priority-full-access-policy "aws-managed-policies-for-trusted-advisor.md#security-iam-support-TA-priority-full-access-policy")
- [AWS managed
  policy: AWSTrustedAdvisorPriorityReadOnlyAccess](aws-managed-policies-for-trusted-advisor.md#security-iam-support-TA-priority-read-only-policy "aws-managed-policies-for-trusted-advisor.md#security-iam-support-TA-priority-read-only-policy")
- [AWS
  managed policy: AWSTrustedAdvisorServiceRolePolicy](aws-managed-policies-for-trusted-advisor.md#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy "aws-managed-policies-for-trusted-advisor.md#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy")
- [AWS managed policy:
  AWSTrustedAdvisorReportingServiceRolePolicy](aws-managed-policies-for-trusted-advisor.md#security-iam-awsmanpol-AWSTrustedAdvisorReportingServiceRolePolicy "aws-managed-policies-for-trusted-advisor.md#security-iam-awsmanpol-AWSTrustedAdvisorReportingServiceRolePolicy")
- [Trusted Advisor updates to AWS
  managed policies](aws-managed-policies-for-trusted-advisor.md#security-iam-awsmanpol-updates-trusted-advisor "aws-managed-policies-for-trusted-advisor.md#security-iam-awsmanpol-updates-trusted-advisor")

## AWS managed

policy: AWSTrustedAdvisorPriorityFullAccess

The [AWSTrustedAdvisorPriorityFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSTrustedAdvisorPriorityFullAccess$jsonEditor "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSTrustedAdvisorPriorityFullAccess$jsonEditor") policy grants full
access to Trusted Advisor Priority. This policy also allows the user to add Trusted Advisor as a trusted
service with AWS Organizations and to specify the delegated administrator accounts for
Trusted Advisor Priority.

**Permissions details**

In the first statement, the policy includes the following permissions for
`trustedadvisor`:

- Describes your account and organization.
- Describes identified risks from Trusted Advisor Priority. The permissions
  allow
  you to download and update the risk status.
- Describes your configurations for Trusted Advisor Priority email notifications. The
  permissions allow you to configure the email notifications and disable them for
  your delegated administrators.
- Sets up Trusted Advisor so that your account can enable AWS Organizations.

In the second statement, the policy includes the following permissions for
`organizations`:

- Describes your Trusted Advisor account and organization.
- Lists the AWS services that you enabled to use Organizations.

In the third statement, the policy includes the following permissions for
`organizations`:

- Lists the delegated administrators for Trusted Advisor Priority.
- Enables and disables trusted access with Organizations.

In the fourth statement, the policy includes the following permissions for
`iam`:

- Creates the `AWSServiceRoleForTrustedAdvisorReporting`
  service-linked role.

In the fifth statement, the policy includes the following permissions for
`organizations`:

- Allows you to register and deregister delegated administrators for
  Trusted Advisor Priority.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AWSTrustedAdvisorPriorityFullAccess",
 "Effect": "Allow",
 "Action": [
 "trustedadvisor:DescribeAccount*",
 "trustedadvisor:DescribeOrganization",
 "trustedadvisor:DescribeRisk*",
 "trustedadvisor:DownloadRisk",
 "trustedadvisor:UpdateRiskStatus",
 "trustedadvisor:DescribeNotificationConfigurations",
 "trustedadvisor:UpdateNotificationConfigurations",
 "trustedadvisor:DeleteNotificationConfigurationForDelegatedAdmin",
 "trustedadvisor:SetOrganizationAccess"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowAccessForOrganization",
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeAccount",
 "organizations:DescribeOrganization",
 "organizations:ListAWSServiceAccessForOrganization"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowListDelegatedAdministrators",
 "Effect": "Allow",
 "Action": [
 "organizations:ListDelegatedAdministrators",
 "organizations:EnableAWSServiceAccess",
 "organizations:DisableAWSServiceAccess"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "organizations:ServicePrincipal": [
 "reporting.trustedadvisor.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "AllowCreateServiceLinkedRole",
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/reporting.trustedadvisor.amazonaws.com/AWSServiceRoleForTrustedAdvisorReporting",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "reporting.trustedadvisor.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AllowRegisterDelegatedAdministrators",
 "Effect": "Allow",
 "Action": [
 "organizations:RegisterDelegatedAdministrator",
 "organizations:DeregisterDelegatedAdministrator"
 ],
 "Resource": "arn:aws:organizations::*:*",
 "Condition": {
 "StringEquals": {
 "organizations:ServicePrincipal": [
 "reporting.trustedadvisor.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

## AWS managed

policy: AWSTrustedAdvisorPriorityReadOnlyAccess

The [AWSTrustedAdvisorPriorityReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSTrustedAdvisorPriorityReadOnlyAccess$jsonEditor "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSTrustedAdvisorPriorityReadOnlyAccess$jsonEditor") policy grants
read-only permissions to Trusted Advisor Priority, including permission to view the delegated
administrator accounts.

**Permissions details**

In the first statement, the policy includes the following permissions for
`trustedadvisor`:

- Describes your Trusted Advisor account and organization.
- Describes the identified risks from Trusted Advisor Priority and allows you to download
  them.
- Describes the configurations for Trusted Advisor Priority email notifications.

In the second and third statement, the policy includes the following permissions for
`organizations`:

- Describes your organization with Organizations.
- Lists the AWS services that you enabled to use Organizations.
- Lists the delegated administrators for Trusted Advisor Priority

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AWSTrustedAdvisorPriorityReadOnlyAccess",
 "Effect": "Allow",
 "Action": [
 "trustedadvisor:DescribeAccount*",
 "trustedadvisor:DescribeOrganization",
 "trustedadvisor:DescribeRisk*",
 "trustedadvisor:DownloadRisk",
 "trustedadvisor:DescribeNotificationConfigurations"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowAccessForOrganization",
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeOrganization",
 "organizations:ListAWSServiceAccessForOrganization"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowListDelegatedAdministrators",
 "Effect": "Allow",
 "Action": [
 "organizations:ListDelegatedAdministrators"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "organizations:ServicePrincipal": [
 "reporting.trustedadvisor.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

## AWS

managed policy: AWSTrustedAdvisorServiceRolePolicy

This policy is attached to the `AWSServiceRoleForTrustedAdvisor`
service-linked role. It allows the service-linked role to perform actions for you. You
can't attach the [AWSTrustedAdvisorServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSTrustedAdvisorServiceRolePolicy$jsonEditor "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSTrustedAdvisorServiceRolePolicy$jsonEditor") to your AWS Identity and Access Management
(IAM) entities. For more information, see [Using service-linked roles for
Trusted Advisor](using-service-linked-roles-ta.md "using-service-linked-roles-ta.md").

This policy grants administrative permissions that allow the service-linked role to
access AWS services. These permissions allow the checks for Trusted Advisor to evaluate your
account.

**Permissions details**

This policy includes the following permissions.

- `accessanalyzer` – Describes AWS Identity and Access Management Access Analyzer resources
- `Auto Scaling` – Describes Amazon EC2 Auto Scaling account quotas and
  resources
- `cloudformation` – Describes AWS CloudFormation (CloudFormation) account
  quotas and stacks
- `cloudfront` – Describes Amazon CloudFront distributions
- `cloudtrail` – Describes AWS CloudTrail (CloudTrail) trails
- `dynamodb` – Describes Amazon DynamoDB account quotas and
  resources
- `dynamodbaccelerator` – Describes DynamoDB Accelerator resources
- `ec2` – Describes Amazon Elastic Compute Cloud (Amazon EC2) account quotas and
  resources
- `elasticloadbalancing` – Describes Elastic Load Balancing (ELB) account
  quotas and resources
- `iam` – Gets IAM resources, such as credentials, password
  policy, and certificates
- `networkfirewall` – Describes AWS Network Firewall resources
- `kinesis` – Describes Amazon Kinesis (Kinesis) account quotas
- `rds` – Describes Amazon Relational Database Service (Amazon RDS) resources
- `redshift` – Describes Amazon Redshift resources
- `route53` – Describes Amazon Route 53 account quotas and
  resources
- `s3` – Describes Amazon Simple Storage Service (Amazon S3) resources
- `ses` – Gets Amazon Simple Email Service (Amazon SES) send quotas
- `sqs` – Lists Amazon Simple Queue Service (Amazon SQS) queues
- `cloudwatch` – Gets Amazon CloudWatch Events (CloudWatch Events) metric
  statistics
- `ce` – Gets Cost Explorer Service (Cost Explorer)
  recommendations
- `route53resolver` – Gets Amazon Route 53 Resolver Resolver Endpoints and
  resources
- `kafka` – Gets Amazon Managed Streaming for Apache Kafka resources
- `ecs` – Gets Amazon ECS resources
- `outposts` – Gets AWS Outposts resources

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "TrustedAdvisorServiceRolePermissions",
 "Effect": "Allow",
 "Action": [
 "access-analyzer:ListAnalyzers",
 "autoscaling:DescribeAccountLimits",
 "autoscaling:DescribeAutoScalingGroups",
 "autoscaling:DescribeLaunchConfigurations",
 "ce:GetReservationPurchaseRecommendation",
 "ce:GetSavingsPlansPurchaseRecommendation",
 "cloudformation:DescribeAccountLimits",
 "cloudformation:DescribeStacks",
 "cloudformation:ListStacks",
 "cloudfront:ListDistributions",
 "cloudtrail:DescribeTrails",
 "cloudtrail:GetTrailStatus",
 "cloudtrail:GetTrail",
 "cloudtrail:ListTrails",
 "cloudtrail:GetEventSelectors",
 "cloudwatch:GetMetricStatistics",
 "cloudwatch:ListMetrics",
 "dax:DescribeClusters",
 "dynamodb:DescribeLimits",
 "dynamodb:DescribeTable",
 "dynamodb:ListTables",
 "ec2:DescribeAddresses",
 "ec2:DescribeReservedInstances",
 "ec2:DescribeInstances",
 "ec2:DescribeVpcs",
 "ec2:DescribeInternetGateways",
 "ec2:DescribeImages",
 "ec2:DescribeNatGateways",
 "ec2:DescribeVolumes",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeRegions",
 "ec2:DescribeReservedInstancesOfferings",
 "ec2:DescribeRouteTables",
 "ec2:DescribeSnapshots",
 "ec2:DescribeVpcEndpoints",
 "ec2:DescribeVpnConnections",
 "ec2:DescribeVpnGateways",
 "ec2:DescribeLaunchTemplateVersions",
 "ec2:GetManagedPrefixListEntries",
 "ecs:DescribeTaskDefinition",
 "ecs:ListTaskDefinitions",
 "elasticloadbalancing:DescribeAccountLimits",
 "elasticloadbalancing:DescribeInstanceHealth",
 "elasticloadbalancing:DescribeLoadBalancerAttributes",
 "elasticloadbalancing:DescribeLoadBalancerPolicies",
 "elasticloadbalancing:DescribeLoadBalancerPolicyTypes",
 "elasticloadbalancing:DescribeLoadBalancers",
 "elasticloadbalancing:DescribeListeners",
 "elasticloadbalancing:DescribeRules",
 "elasticloadbalancing:DescribeTargetGroups",
 "elasticloadbalancing:DescribeTargetHealth",
 "iam:GenerateCredentialReport",
 "iam:GetAccountPasswordPolicy",
 "iam:GetAccountSummary",
 "iam:GetCredentialReport",
 "iam:GetServerCertificate",
 "iam:ListServerCertificates",
 "iam:ListSAMLProviders",
 "kinesis:DescribeLimits",
 "kafka:DescribeClusterV2",
 "kafka:ListClustersV2",
 "kafka:ListNodes",
 "network-firewall:ListFirewalls",
 "network-firewall:DescribeFirewall",
 "outposts:GetOutpost",
 "outposts:ListAssets",
 "outposts:ListOutposts",
 "rds:DescribeAccountAttributes",
 "rds:DescribeDBClusters",
 "rds:DescribeDBEngineVersions",
 "rds:DescribeDBInstances",
 "rds:DescribeDBParameterGroups",
 "rds:DescribeDBParameters",
 "rds:DescribeDBSecurityGroups",
 "rds:DescribeDBSnapshots",
 "rds:DescribeDBSubnetGroups",
 "rds:DescribeEngineDefaultParameters",
 "rds:DescribeEvents",
 "rds:DescribeOptionGroupOptions",
 "rds:DescribeOptionGroups",
 "rds:DescribeOrderableDBInstanceOptions",
 "rds:DescribeReservedDBInstances",
 "rds:DescribeReservedDBInstancesOfferings",
 "rds:ListTagsForResource",
 "redshift:DescribeClusters",
 "redshift:DescribeReservedNodeOfferings",
 "redshift:DescribeReservedNodes",
 "route53:GetAccountLimit",
 "route53:GetHealthCheck",
 "route53:GetHostedZone",
 "route53:ListHealthChecks",
 "route53:ListHostedZones",
 "route53:ListHostedZonesByName",
 "route53:ListResourceRecordSets",
 "route53resolver:ListResolverEndpoints",
 "route53resolver:ListResolverEndpointIpAddresses",
 "s3:GetAccountPublicAccessBlock",
 "s3:GetBucketAcl",
 "s3:GetBucketPolicy",
 "s3:GetBucketPolicyStatus",
 "s3:GetBucketLocation",
 "s3:GetBucketLogging",
 "s3:GetBucketVersioning",
 "s3:GetBucketPublicAccessBlock",
 "s3:GetLifecycleConfiguration",
 "s3:ListBucket",
 "s3:ListAllMyBuckets",
 "ses:GetSendQuota",
 "sqs:GetQueueAttributes",
 "sqs:ListQueues"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy:

AWSTrustedAdvisorReportingServiceRolePolicy

This policy is attached to the `AWSServiceRoleForTrustedAdvisorReporting`
service-linked role that allows Trusted Advisor to perform actions for the organizational view
feature. You can't attach the [AWSTrustedAdvisorReportingServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSTrustedAdvisorReportingServiceRolePolicy$jsonEditor "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSTrustedAdvisorReportingServiceRolePolicy$jsonEditor") to your
IAM entities. For more information, see [Using service-linked roles for
Trusted Advisor](using-service-linked-roles-ta.md "using-service-linked-roles-ta.md").

This policy grants administrative permissions that allow the service-linked role to
perform AWS Organizations actions.

**Permissions details**

This policy includes the following permissions.

- `organizations` – Describes your organization and lists the
  service access, accounts, parents, children, and organizational units

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "organizations:DescribeOrganization",
 "organizations:ListAWSServiceAccessForOrganization",
 "organizations:ListAccounts",
 "organizations:ListAccountsForParent",
 "organizations:ListDelegatedAdministrators",
 "organizations:ListOrganizationalUnitsForParent",
 "organizations:ListChildren",
 "organizations:ListParents",
 "organizations:DescribeOrganizationalUnit",
 "organizations:DescribeAccount"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

## Trusted Advisor updates to AWS

managed policies

View details about updates to AWS managed policies for AWS Support and Trusted Advisor since
these services began tracking these changes. For automatic alerts about changes to this
page, subscribe to the RSS feed on the [Document history](History.md "History.md")
page.

The following table describes important updates to the Trusted Advisor managed policies since
August 10, 2021.

| Trusted Advisor                                                                                                                                                                                                                                                                                                                                            | Change                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description        | Date |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ---- |
| [AWSTrustedAdvisorServiceRolePolicy](#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy "#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy") Update to an existing policy.                                                                                                                                                                | Trusted Advisor added new actions to grant the `elasticloadbalancing:DescribeListeners,` and `elasticloadbalancing:DescribeRules` permissions.                                                                                                                                                                                                                                                                                                                                | October 30, 2024   |
| [AWSTrustedAdvisorServiceRolePolicy](#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy "#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy") Update to an existing policy.                                                                                                                                                                | Trusted Advisor added new actions to grant the `access-analyzer:ListAnalyzers`, `cloudwatch:ListMetrics`, `dax:DescribeClusters`, `ec2:DescribeNatGateways`, `ec2:DescribeRouteTables`, `ec2:DescribeVpcEndpoints`, `ec2:GetManagedPrefixListEntries`, `elasticloadbalancing:DescribeTargetHealth`, `iam:ListSAMLProviders`, `kafka:DescribeClusterV2` `network-firewall:ListFirewalls` `network-firewall:DescribeFirewall` and `sqs:GetQueueAttributes` permissions.         | June 11, 2024      |
| [AWSTrustedAdvisorServiceRolePolicy](#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy "#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy") Update to an existing policy.                                                                                                                                                                | Trusted Advisor added new actions to grant the `cloudtrail:GetTrail` `cloudtrail:ListTrails` `cloudtrail:GetEventSelectors` `outposts:GetOutpost`, `outposts:ListAssets` and `outposts:ListOutposts` permissions.                                                                                                                                                                                                                                                             | January 18, 2024   |
| [AWSTrustedAdvisorPriorityFullAccess](#security-iam-support-TA-priority-full-access-policy "#security-iam-support-TA-priority-full-access-policy") Update to an existing policy.                                                                                                                                                                           | Trusted Advisor updated the `AWSTrustedAdvisorPriorityFullAccess` AWS managed policy to include statement IDs.                                                                                                                                                                                                                                                                                                                                                                | December 6, 2023   |
| [AWSTrustedAdvisorPriorityReadOnlyAccess](#security-iam-support-TA-priority-read-only-policy "#security-iam-support-TA-priority-read-only-policy") Update to an existing policy.                                                                                                                                                                           | Trusted Advisor updated the `AWSTrustedAdvisorPriorityReadOnlyAccess` AWS managed policy to include statement IDs.                                                                                                                                                                                                                                                                                                                                                            | December 6, 2023   |
| [AWSTrustedAdvisorServiceRolePolicy](#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy "#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy") – Update to an existing policy                                                                                                                                                               | Trusted Advisor added new actions to grant the `ec2:DescribeRegions` `s3:GetLifecycleConfiguration` `ecs:DescribeTaskDefinition` and `ecs:ListTaskDefinitions` permissions.                                                                                                                                                                                                                                                                                                   | November 9, 2023   |
| [AWSTrustedAdvisorServiceRolePolicy](#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy "#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy") – Update to an existing policy                                                                                                                                                               | Trusted Advisor added new IAM actions `route53resolver:ListResolverEndpoints`, `route53resolver:ListResolverEndpointIpAddresses`, `ec2:DescribeSubnets`, `kafka:ListClustersV2` and `kafka:ListNodes` to onboard new resilience checks.                                                                                                                                                                                                                                       | September 14, 2023 |
| [AWSTrustedAdvisorReportingServiceRolePolicy](#security-iam-awsmanpol-AWSTrustedAdvisorReportingServiceRolePolicy "#security-iam-awsmanpol-AWSTrustedAdvisorReportingServiceRolePolicy") V2 of managed policy attached on Trusted Advisor `AWSServiceRoleForTrustedAdvisorReporting` service-linked role                                                   | Upgrade AWS managed policy to V2 for the Trusted Advisor `AWSServiceRoleForTrustedAdvisorReporting` service-linked role. The V2 will add one more IAM action `organizations:ListDelegatedAdministrators`                                                                                                                                                                                                                                                                      | Feb 28, 2023       |
| [AWSTrustedAdvisorPriorityFullAccess](#security-iam-support-TA-priority-full-access-policy "#security-iam-support-TA-priority-full-access-policy") and [AWSTrustedAdvisorPriorityReadOnlyAccess](#security-iam-support-TA-priority-read-only-policy "#security-iam-support-TA-priority-read-only-policy") New AWS managed policies for the Trusted Advisor | Trusted Advisor added two new managed policies that you can use to control access to Trusted Advisor Priority.                                                                                                                                                                                                                                                                                                                                                                | August 17, 2022    |
| [AWSTrustedAdvisorServiceRolePolicy](#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy "#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy") – Update to an existing policy                                                                                                                                                               | Trusted Advisor added new actions to grant the `DescribeTargetGroups` and `GetAccountPublicAccessBlock` permissions. The `DescribeTargetGroup` permission is required for the **Auto Scaling Group Health Check** to retrieve non-Classic Load Balancers that are attached to an Auto Scaling group. The `GetAccountPublicAccessBlock` permission is required for the **Amazon S3 Bucket Permissions** check to retrieve the block public access settings for an AWS account. | August 10, 2021    |
| Change log published                                                                                                                                                                                                                                                                                                                                       | Trusted Advisor started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                                                                                                        | August 10, 2021    |
