# `AWS-EnableNeptuneClusterDeletionProtection`

**Description**

The `AWS-EnableNeptuneClusterDeletionProtection` runbook enables deletion protection for the Amazon Neptune cluster you specify.

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

Description: (Required) The ID of the Neptune cluster you want to enable deletion protection on.
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
- VerifyNeptuneDbEngine (`aws:assertAwsResourceProperty`) - Verifies the engine type of the specified DB cluster is `neptune`.
- VerifyNeptuneStatus (`aws:waitForAwsResourceProperty`) - Verifies that status of the cluster is `available`.
- EnableNeptuneDbDeletionProtection (`aws:executeAwsApi`) - Enables deletion protection on the Neptune DB cluster.
- VerifyNeptuneDbDeletionProtection (`aws:assertAwsResourceProperty`) - Verifies deletion protection is enabled on the DB cluster.

**Outputs**

- EnableNeptuneDbDeletionProtection.EnableNeptuneDbDeletionProtectionResponse - The output from the API operation.
