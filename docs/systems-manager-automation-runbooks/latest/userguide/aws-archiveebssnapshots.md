# `AWS-ArchiveEBSSnapshots`

**Description**

The `AWS-ArchiveEBSSnapshots` runbook helps you archive snapshots for
Amazon Elastic Block Store (Amazon EBS) volumes by specifying the tag you've applied to your snapshots.
Alternatively, you can provide the ID of a volume if your snapshots are not
tagged.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-ArchiveEBSSnapshots "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-ArchiveEBSSnapshots")

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

- Description

Type: String

Description: (Optional) A description for the Amazon EBS snapshot.

- DryRun

Type: String

Valid values: Yes | No

Description: (Required) Checks whether you have the required permissions
for the action, without actually making the request, and provides an error
response.

- RetentionCount

Type: String

Description: (Optional) The number of snapshots you want to archive. Don't
specify a value for this parameter if you specify a value for
`RetentionDays`.

- RetentionDays

Type: String

Description: (Optional) The number of previous days of snapshots you want
to archive. Don't specify a value for this parameter if you specify a value
for `RetentionCount`.

- SnapshotWithTag

Type: String

Valid values: Yes | No

Description: (Required) Specifies whether the snapshots you want to
archive are tagged.

- TagKey

Type: String

Description: (Optional) The key of the tag assigned to the snapshots you
want to archive.

- TagValue

Type: String

Description: (Optional) The value of the tag assigned to the snapshots you
want to archive.

- VolumeId

Type: String

Description: (Optional) The ID of the volume whose snapshots you want to
archive. Use this parameter if your snapshots are not tagged.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ec2:ArchiveSnapshots`
- `ec2:DescribeSnapshots`

**Document Steps**

`aws:executeScript` - Archives snapshots using the tag you specify
using the `TagKey` and `TagValue` parameters, or the
`VolumeId` parameter.
