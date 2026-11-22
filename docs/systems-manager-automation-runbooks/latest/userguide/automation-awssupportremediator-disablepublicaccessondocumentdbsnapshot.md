

# `AWSSupportRemediator-DisablePublicAccessOnDocumentDbSnapshot`

**Description**

Disables public access for an Amazon DocumentDB manual cluster snapshot by removing `all` from the snapshot's `restore` attribute values.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [Amazon DocumentDB manual cluster snapshots should not be public](https://docs.aws.amazon.com/securityhub/latest/userguide/documentdb-controls.html#documentdb-3).

If the snapshot does not exist or is not publicly shared, the automation completes successfully without making changes.

Removing public access prevents other AWS accounts from restoring the snapshot through the public `all` sharing value. The automation preserves sharing with specific AWS account IDs.

To restore public access after this automation runs, modify the snapshot's `restore` attribute to add `all` to the attribute values.

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
+ DBClusterSnapshotArn

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the Amazon DocumentDB manual cluster snapshot.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `rds:DescribeDBClusterSnapshotAttributes`
+ `rds:ModifyDBClusterSnapshotAttribute`

**Document Steps**

1. **validateSnapshot** - Validates that the Amazon DocumentDB manual cluster snapshot exists and checks whether it is publicly shared.

1. **branchOnChangeRequired** - Branches on whether the snapshot needs to be updated to remove public access.

1. **disableClusterSnapshotPublicAccess** - Removes public access from the Amazon DocumentDB manual cluster snapshot by removing `all` from the `restore` attribute values.

**Outputs**
+ validateSnapshot.ChangeRequired: Whether the snapshot needs to be updated to remove public access.
+ validateSnapshot.ValidationMessage: Information about the validation result.