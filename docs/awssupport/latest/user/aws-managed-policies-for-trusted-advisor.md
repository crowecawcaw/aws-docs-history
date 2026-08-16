# AWS managed policies for AWS Trusted Advisor

Trusted Advisor has the following AWS managed policies.

###### Contents

- [AWS managed policy: AWSTrustedAdvisorPriorityFullAccess](aws-managed-policies-for-trusted-advisor.md#security-iam-support-TA-priority-full-access-policy "aws-managed-policies-for-trusted-advisor.md#security-iam-support-TA-priority-full-access-policy")
- [AWS managed policy: AWSTrustedAdvisorPriorityReadOnlyAccess](aws-managed-policies-for-trusted-advisor.md#security-iam-support-TA-priority-read-only-policy "aws-managed-policies-for-trusted-advisor.md#security-iam-support-TA-priority-read-only-policy")
- [AWS managed policy: AWSTrustedAdvisorServiceRolePolicy](aws-managed-policies-for-trusted-advisor.md#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy "aws-managed-policies-for-trusted-advisor.md#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy")
- [AWS managed policy: AWSTrustedAdvisorReportingServiceRolePolicy](aws-managed-policies-for-trusted-advisor.md#security-iam-awsmanpol-AWSTrustedAdvisorReportingServiceRolePolicy "aws-managed-policies-for-trusted-advisor.md#security-iam-awsmanpol-AWSTrustedAdvisorReportingServiceRolePolicy")
- [Trusted Advisor updates to AWS managed policies](aws-managed-policies-for-trusted-advisor.md#security-iam-awsmanpol-updates-trusted-advisor "aws-managed-policies-for-trusted-advisor.md#security-iam-awsmanpol-updates-trusted-advisor")

## AWS managed policy: AWSTrustedAdvisorPriorityFullAccess

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

To view the full JSON policy document, see [AWSTrustedAdvisorPriorityFullAccess](../../../aws-managed-policy/latest/reference/AWSTrustedAdvisorPriorityFullAccess.md "../../../aws-managed-policy/latest/reference/AWSTrustedAdvisorPriorityFullAccess.md") in the _AWS Managed Policy Reference_.

## AWS managed policy: AWSTrustedAdvisorPriorityReadOnlyAccess

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

To view the full JSON policy document, see [AWSTrustedAdvisorPriorityReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSTrustedAdvisorPriorityReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSTrustedAdvisorPriorityReadOnlyAccess.md") in the _AWS Managed Policy Reference_.

## AWS managed policy: AWSTrustedAdvisorServiceRolePolicy

This policy is attached to the `AWSServiceRoleForTrustedAdvisor`
service-linked role. It allows the service-linked role to perform actions for you. You
can't attach the [AWSTrustedAdvisorServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSTrustedAdvisorServiceRolePolicy$jsonEditor "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSTrustedAdvisorServiceRolePolicy$jsonEditor") to your AWS Identity and Access Management
(IAM) entities. For more information, see [Using service-linked roles for Trusted Advisor](using-service-linked-roles-ta.md "using-service-linked-roles-ta.md").

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

To view the full JSON policy document, see [AWSTrustedAdvisorServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSTrustedAdvisorServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSTrustedAdvisorServiceRolePolicy.md") in the _AWS Managed Policy Reference_.

## AWS managed policy: AWSTrustedAdvisorReportingServiceRolePolicy

This policy is attached to the `AWSServiceRoleForTrustedAdvisorReporting`
service-linked role that allows Trusted Advisor to perform actions for the organizational view
feature. You can't attach the [AWSTrustedAdvisorReportingServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSTrustedAdvisorReportingServiceRolePolicy$jsonEditor "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSTrustedAdvisorReportingServiceRolePolicy$jsonEditor") to your
IAM entities. For more information, see [Using service-linked roles for Trusted Advisor](using-service-linked-roles-ta.md "using-service-linked-roles-ta.md").

This policy grants administrative permissions that allow the service-linked role to
perform AWS Organizations actions.

**Permissions details**

This policy includes the following permissions.

- `organizations` – Describes your organization and lists the
  service access, accounts, parents, children, and organizational units

To view the full JSON policy document, see [AWSTrustedAdvisorReportingServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSTrustedAdvisorReportingServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSTrustedAdvisorReportingServiceRolePolicy.md") in the _AWS Managed Policy Reference_.

## Trusted Advisor updates to AWS managed policies

View details about updates to AWS managed policies for AWS Support and Trusted Advisor since
these services began tracking these changes. For automatic alerts about changes to this
page, subscribe to the RSS feed on the [Document history](History.md "History.md")
page.

The following table describes important updates to the Trusted Advisor managed policies since
August 10, 2021.

Trusted Advisor| Change | Description | Date |
| --- | --- | --- |
| [AWSTrustedAdvisorServiceRolePolicy](#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy "#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy")<br>Update to an existing policy. | Trusted Advisor added new actions to grant the<br>`ecs:ListClusters`,<br>`ecs:ListTasks`,<br>`ecs:DescribeTasks`, and<br>`ecs:ListTaskDefinitionFamilies` permissions. | May 14, 2026 |
| [AWSTrustedAdvisorServiceRolePolicy](#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy "#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy")<br>Update to an existing policy. | Trusted Advisor added new actions to grant the<br>`elasticloadbalancing:DescribeListeners,` and<br>`elasticloadbalancing:DescribeRules` permissions. | October 30, 2024 |
| [AWSTrustedAdvisorServiceRolePolicy](#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy "#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy")<br>Update to an existing policy. | Trusted Advisor added new actions to grant the<br>`access-analyzer:ListAnalyzers`,<br>`cloudwatch:ListMetrics`,<br>`dax:DescribeClusters`,<br>`ec2:DescribeNatGateways`,<br>`ec2:DescribeRouteTables`,<br>`ec2:DescribeVpcEndpoints`,<br>`ec2:GetManagedPrefixListEntries`,<br>`elasticloadbalancing:DescribeTargetHealth`,<br>`iam:ListSAMLProviders`,<br>`kafka:DescribeClusterV2`<br>`network-firewall:ListFirewalls`<br>`network-firewall:DescribeFirewall` and<br>`sqs:GetQueueAttributes` permissions. | June 11, 2024 |
| [AWSTrustedAdvisorServiceRolePolicy](#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy "#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy")<br>Update to an existing policy. | Trusted Advisor added new actions to grant the<br>`cloudtrail:GetTrail`<br>`cloudtrail:ListTrails`<br>`cloudtrail:GetEventSelectors`<br>`outposts:GetOutpost`,<br>`outposts:ListAssets` and<br>`outposts:ListOutposts` permissions. | January 18, 2024 |
| [AWSTrustedAdvisorPriorityFullAccess](#security-iam-support-TA-priority-full-access-policy "#security-iam-support-TA-priority-full-access-policy")<br>Update to an existing policy. | Trusted Advisor updated the `AWSTrustedAdvisorPriorityFullAccess` AWS managed policy to include statement IDs. | December 6, 2023 |
| [AWSTrustedAdvisorPriorityReadOnlyAccess](#security-iam-support-TA-priority-read-only-policy "#security-iam-support-TA-priority-read-only-policy")<br>Update to an existing policy. | Trusted Advisor updated the `AWSTrustedAdvisorPriorityReadOnlyAccess` AWS managed policy to include statement IDs. | December 6, 2023 |
| [AWSTrustedAdvisorServiceRolePolicy](#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy "#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy")<br>– Update to an existing policy | Trusted Advisor added new actions to grant the<br>`ec2:DescribeRegions`<br>`s3:GetLifecycleConfiguration`<br>`ecs:DescribeTaskDefinition` and<br>`ecs:ListTaskDefinitions` permissions. | November 9, 2023 |
| [AWSTrustedAdvisorServiceRolePolicy](#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy "#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy")<br>– Update to an existing policy | Trusted Advisor added new IAM actions<br>`route53resolver:ListResolverEndpoints`,<br>`route53resolver:ListResolverEndpointIpAddresses`,<br>`ec2:DescribeSubnets`,<br>`kafka:ListClustersV2` and<br>`kafka:ListNodes` to onboard<br>new resilience checks. | September 14, 2023 |
| [AWSTrustedAdvisorReportingServiceRolePolicy](#security-iam-awsmanpol-AWSTrustedAdvisorReportingServiceRolePolicy "#security-iam-awsmanpol-AWSTrustedAdvisorReportingServiceRolePolicy")<br>V2 of managed policy attached on Trusted Advisor `AWSServiceRoleForTrustedAdvisorReporting`<br>service-linked role | Upgrade AWS managed policy to V2 for the Trusted Advisor `AWSServiceRoleForTrustedAdvisorReporting`<br>service-linked role. The V2 will add one more IAM action `organizations:ListDelegatedAdministrators` | Feb 28, 2023 |
| [AWSTrustedAdvisorPriorityFullAccess](#security-iam-support-TA-priority-full-access-policy "#security-iam-support-TA-priority-full-access-policy")<br>and [AWSTrustedAdvisorPriorityReadOnlyAccess](#security-iam-support-TA-priority-read-only-policy "#security-iam-support-TA-priority-read-only-policy")<br>New AWS managed policies for the Trusted Advisor | Trusted Advisor added two new managed policies that you can use to<br>control access to Trusted Advisor Priority. | August 17, 2022 |
| [AWSTrustedAdvisorServiceRolePolicy](#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy "#security-iam-awsmanpol-AWSTrustedAdvisorServiceRolePolicy")<br>– Update to an existing policy | Trusted Advisor added new actions to grant the<br>`DescribeTargetGroups` and<br>`GetAccountPublicAccessBlock` permissions.<br>The `DescribeTargetGroup` permission is required for<br>the *_Auto Scaling Group Health Check_<br>• to retrieve<br>non-Classic Load Balancers that are attached to an Auto Scaling group.<br>The `GetAccountPublicAccessBlock` permission is<br>required for the *_Amazon S3 Bucket Permissions_<br>• check<br>to retrieve the block public access settings for an<br>AWS account. | August 10, 2021 |
| Change log published | Trusted Advisor started tracking changes for its AWS managed policies. | August 10, 2021 |
