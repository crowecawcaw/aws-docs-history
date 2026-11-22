

# `AWSSupportRemediator-DisablePublicAccessOnEbsSnapshot`

**Description**

Disables public access permission on an Amazon Elastic Block Store (Amazon EBS) volume snapshot by removing the `all` group from its create-volume permission using the [ModifySnapshotAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySnapshotAttribute.html) API.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [Amazon EBS Public Snapshots](https://docs.aws.amazon.com/awssupport/latest/user/security-checks.html#amazon-ebs-public-snapshots).

If the Amazon EBS snapshot does not exist or public access is already disabled, the automation completes successfully without making changes.

Some snapshots might be intentionally shared publicly. Running this runbook on such snapshots might cause availability issues for consumers that rely on public access.

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
+ SnapshotId

  Type: String

  Description: (Required) The ID of the Amazon EBS snapshot to disable public access on.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `ec2:DescribeSnapshotAttribute`
+ `ec2:DescribeSnapshots`
+ `ec2:ModifySnapshotAttribute`

**Document Steps**

1. **validateSnapshot** - Validates that the Amazon EBS snapshot exists and determines whether public access is currently enabled.

1. **branchOnIfChangeRequired** - Branches on whether the automation must disable public access on the Amazon EBS snapshot.

1. **disablePublicAccessAndVerify** - Disables public access on the Amazon EBS snapshot using the ModifySnapshotAttribute API and verifies that the snapshot no longer grants public access.

**Outputs**
+ validateSnapshot.ChangeRequired: Whether a change is required.
+ validateSnapshot.ValidationMessage: The reason when no change is required.
+ disablePublicAccessAndVerify.Message: Confirmation message after public access is disabled.