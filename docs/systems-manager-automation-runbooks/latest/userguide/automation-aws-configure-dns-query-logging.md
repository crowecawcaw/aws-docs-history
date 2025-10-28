# `AWSSupport-ConfigureDNSQueryLogging`

**Description**

The `AWSSupport-ConfigureDNSQueryLogging` runbook configures logging
for DNS queries that originate in your virtual private cloud (VPC) or for Amazon Route 53
hosted zones. You can choose to publish query logs to Amazon CloudWatch Logs, Amazon Simple Storage Service (Amazon S3), or
Amazon Data Firehose. For more information about query logging and resolver query logs, see
[Public DNS query logging](../../../Route53/latest/DeveloperGuide/query-logs.md "../../../Route53/latest/DeveloperGuide/query-logs.md") and
[Resolver query
logging](../../../Route53/latest/DeveloperGuide/resolver-query-logs.md "../../../Route53/latest/DeveloperGuide/resolver-query-logs.md") .

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-ConfigureDNSQueryLogging "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-ConfigureDNSQueryLogging")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- LogDestinationArn

Type: String

Description: (Optional) The ARN of the CloudWatch Logs group, Amazon S3 bucket or Firehose
stream you want to send query logs to. Note that Route 53 public DNS query
logging only supports CloudWatch Logs groups. If you do not specify a value for this
parameter, the automation creates a CloudWatch Logs group with the format `AWSSupport-ConfigureDNSQueryLogging-{automation:
 `EXECUTION_ID` }` , and an IAM
resource policy to publish the query logs. The CloudWatch Logs group created by the
automation has a retention period of 14 days.

- QueryLogType

Type: String

Description: (Optional) The types of queries you want to log.

Valid values: Public | Resolver/Private

Default: Public

- ResourceId

Type: String

Description: (Required) The ID of the resource whose queries you want to
log. If you specify `Public` for the `QueryLogType`
parameter, the resource must be the ID of a Route 53 private hosted zone. If
you specify `Resolver/Private` for the `QueryLogType`
parameter, the resource must be the ID of a VPC.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ec2:DescribeVpcs`
- `firehose:ListTagsForDeliveryStream`
- `firehose:PutRecord`
- `firehose:PutRecordBatch`
- `firehose:TagDeliveryStream`
- `iam:AttachRolePolicy`
- `iam:CreatePolicy`
- `iam:CreateRole`
- `iam:CreateServiceLinkedRole`
- `iam:DeletePolicy`
- `iam:DeleteRole`
- `iam:DeleteRolePolicy`
- `iam:GetPolicy`
- `iam:GetRole`
- `iam:PassRole`
- `iam:PutRolePolicy`
- `iam:TagRole`
- `iam:UpdateRole`
- `logs:CreateLogDelivery`
- `logs:CreateLogGroup`
- `logs:DeleteLogDelivery`
- `logs:DeleteLogGroup`
- `logs:DescribeLogGroups`
- `logs:DescribeLogStreams`
- `logs:DescribeResourcePolicies`
- `logs:ListLogDeliveries`
- `logs:PutResourcePolicy`
- `logs:PutRetentionPolicy`
- `logs:UpdateLogDelivery`
- `route53:CreateQueryLoggingConfig`
- `route53:DeleteQueryLoggingConfig`
- `route53:GetHostedZone`
- `route53resolver:AssociateResolverQueryLogConfig`
- `route53resolver:CreateResolverQueryLogConfig`
- `route53resolver:DeleteResolverQueryLogConfig`
- `s3:GetBucketAcl`

**Document Steps**

- `aws:executeScript` - Verifies the resource you specify for the
  `ResourceId` parameter exists, and checks whether the
  resource type matches the required `QueryLogType` option.
- `aws:executeScript` - Verifies that the value you specify for the
  `LogDestinationArn` parameter matches the required
  `QueryLogType` .
- `aws:executeScript` - Verifies the required permissions for Route 53
  to publish logs to the CloudWatch Logs log group, and creates the required IAM
  resource policy if it doesn't exist.
- `aws:executeScript` - Enables the DNS query logging on the
  selected destination.
