# `AWS-EnableNeptuneDbAuditLogsToCloudWatch`

**Description**

The `AWS-EnableNeptuneDbAuditLogsToCloudWatch` runbook helps you send audit logs for an Amazon Neptune DB cluster to Amazon CloudWatch Logs.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableNeptuneDbAuditLogsToCloudWatch "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableNeptuneDbAuditLogsToCloudWatch")

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

- DbClusterResourceId

Type: String

Description: (Required) The resource ID of the Neptune DB cluster you want to enable audit logs for.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:GetAutomationExecution`
- `ssm:StartAutomationExecution`
- `neptune:DescribeDBCluster`
- `neptune:ModifyDBCluster`
- `rds:DescribeDBClusters`
- `rds:ModifyDBCluster`

**Document Steps**

- GetNeptuneDbClusterIdentifier (`aws:executeAwsApi`) - Returns the ID of the Neptune DB cluster.
- VerifyNeptuneDbEngine (`aws:assertAwsResourceProperty`) - Verifies the Neptune DB engine type is `neptune`.
- EnableNeptuneDbAuditLogs (`aws:executeAwsApi`) - Enables audit logs for the Neptune DB cluster to be sent CloudWatch Logs.
- VerifyNeptuneDbStatus (`aws:waitAwsResourceProperty`) - Verifies the Neptune DB cluster status is `available`.
- VerifyNeptuneDbAuditLogs (`aws:executeScript`) - Verifies that audit logs were successfully configured to send to CloudWatch Logs.
