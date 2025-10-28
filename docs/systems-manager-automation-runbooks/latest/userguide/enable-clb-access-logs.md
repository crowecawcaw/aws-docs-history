# `AWS-EnableCLBAccessLogs`

**Description**

The `AWS-EnableCLBAccessLogs` runbook enables access logs for a Classic
Load Balancer.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableCLBAccessLogs "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableCLBAccessLogs")

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

- EmitInterval

Type: Integer

Valid values: 5 | 60

Default: 60

Description: (Optional) The interval for publishing the access logs in
minutes.

- LoadBalancerNames

Type: String

Description: (Required) A comma separated list of Classic Load Balancers
you want to enable access logs for.

- S3BucketName

Type: String

Description: (Required) The name of the Amazon Simple Storage Service (Amazon S3) bucket where the
access logs are stored.

- S3BucketPrefix

Type: String

Description: (Optional) The logical hierarchy you created for your Amazon S3
bucket, for example `my-bucket-prefix/prod`. If the prefix is not
provided, the log is placed at the root level of the bucket.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `elasticloadbalancing:ModifyLoadBalancerAttributes`
  **Document Steps**

- `aws:executeAwsApi` - Enables access logs for the Classic Load
  Balancers you specify in the `LoadBalancerNames`
  parameter.
  **Outputs**

EnableCLBAccessLogs.SuccessesLoadBalancers - List of load balancer names where
access logs were successfully enabled.

EnableCLBAccessLogs.FailedLoadBalancers - MapList of load balancer names where
enabling access logs failed and the reason for the failure.
