

# `AWSSupportRemediator-DisablePublicAccessOnRdsSnapshot`

**Description**

Disables public access for an Amazon Relational Database Service (Amazon RDS) snapshot by removing the `all` value from the `restore` attribute.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [Amazon RDS Public Snapshots](https://docs.aws.amazon.com/awssupport/latest/user/security-checks.html#amazon-rds-public-snapshots).

If the snapshot does not exist or is not publicly shared, the automation completes successfully without making changes.

Availability impact: Removing public (`all`) access prevents any AWS account that depends on it from restoring this snapshot. To keep specific accounts able to restore the snapshot, share it explicitly with their account IDs. Use `ModifyDBSnapshotAttribute` or `ModifyDBClusterSnapshotAttribute` with `ValuesToAdd` instead of restoring public access.

**Important considerations**  
You are responsible for reviewing automation actions before they run.
This automation might cause stack drift if the resource is part of an AWS CloudFormation stack.
Access to `AWSSupportRemediator-*` runbooks requires an active Business Support\+, Enterprise Support, or Unified Operations Support plan. For more information, see [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/) on the AWS website.

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ SnapshotArn

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the Amazon RDS snapshot.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `rds:DescribeDBClusterSnapshotAttributes`
+ `rds:DescribeDBSnapshotAttributes`
+ `rds:ModifyDBClusterSnapshotAttribute`
+ `rds:ModifyDBSnapshotAttribute`

**Document Steps**

1. **validateSnapshot** - Validates whether the Amazon RDS snapshot exists and is publicly shared.

1. **branchOnChangeRequired** - Branches on whether the snapshot requires public access removal and the snapshot type.

1. **disableClusterSnapshotPublicAccess** - Removes public access from the Amazon RDS cluster snapshot by removing the `all` value from the `restore` attribute.

1. **disableDBSnapshotPublicAccess** - Removes public access from the Amazon RDS DB snapshot by removing the `all` value from the `restore` attribute.

**Outputs**
+ validateSnapshot.ChangeRequired: Whether the snapshot requires public access removal.
+ validateSnapshot.ValidationMessage: A message describing the validation result.