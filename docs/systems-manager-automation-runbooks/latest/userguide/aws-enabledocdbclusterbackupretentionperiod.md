# `AWS-EnableDocDbClusterBackupRetentionPeriod`

**Description**

The `AWS-EnableDocDbClusterBackupRetentionPeriod` runbook enables a backup retention period for the Amazon DocumentDB cluster you specify. This feature sets the total number of days for which an automated backup is retained. To modify a cluster, the cluster must be in the available state with an engine type of `docdb`.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableDocDbClusterBackupRetentionPeriod "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableDocDbClusterBackupRetentionPeriod")

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

- DBClusterResourceId

Type: String

Description: (Required) The resource ID for the Amazon DocumentDB cluster you want to enable the backup retention period for.

- BackupRetentionPeriod

Type: Integer

Description: (Required) The number of days for which automated backups are retained. Must be a value from 7-35 days.

- PreferredBackupWindow

Type: String

Description: (Optional) A daily time range in Universal Time Coordinated (UTC) in the format hh24:mm-hh24:mm, for example 07:14-07:44. The value must be at least 30 minutes and can't conflict with the preferred maintenance window.

- `ssm:GetAutomationExecution`
- `ssm:StartAutomationExecution`
- `docdb:DescribeDBClusters`
- `docdb:ModifyDBCluster`
- `rds:DescribeDBClusters`
- `rds:ModifyDBCluster`

**Document Steps**

- GetDocDbClusterIdentifier (`aws:executeAwsApi`) - Returns the Amazon DocumentDB cluster identifier using the provided resource ID.
- VerifyDocDbEngine (`aws:assertAwsResourceProperty`) - Verifies the Amazon DocumentDB engine type is `docdb` to prevent inadvertent changes to other Amazon RDS engine types.
- VerifyDocDbStatus (`aws:waitAwsResourceProperty`) - Verifies the Amazon DocumentDB cluster status is `available`.
- ModifyDocDbRetentionPeriod (`aws:executeAwsApi`) - Sets the retention period using the provided values for the specified Amazon DocumentDB cluster.
- VerifyDocDbBackupsEnabled (`aws:executeScript`) - Verifies the retention period for the Amazon DocumentDB cluster and the preferred back up window, if specified, were successfully set.

**Outputs**

ModifyDocDbRetentionPeriod.ModifyDbClusterResponse - Response from the `ModifyDBCluster` API operation.

VerifyDocDbBackupsEnabled.VerifyDbClusterBackupsEnabledResponse - Output from the `VerifyDocDbBackupsEnabled` step confirming successful modification of the Amazon DocumentDB cluster.
