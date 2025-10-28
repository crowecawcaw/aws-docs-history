# `AWSSupport-RestoreEC2InstanceFromSnapshot`

**Description**

The `AWSSupport-RestoreEC2InstanceFromSnapshot` runbook helps you
identify and restore an Amazon Elastic Compute Cloud (Amazon EC2) instance from a working Amazon Elastic Block Store (Amazon EBS)
snapshot of the root volume.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-RestoreEC2InstanceFromSnapshot "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-RestoreEC2InstanceFromSnapshot")

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

- EndDate

Type: String

Description: (Optional) The last date you want the automation to look for
a snapshot.

- InplaceSwap

Type: Boolean

Valid values: true | false

Description: (Optional) If the value for this parameter is set to
`true`, the newly created volume from the snapshot replaces
the existing root volume attached to your instance.

- InstanceId

Type: String

Description: (Required) The ID of the instance you want to restore from a
snapshot.

- LookForInstanceStatusCheck

Type: Boolean

Valid values: true | false

Default: true

Description: (Optional) If the value for this parameter is set to
`true`, the automation checks whether instance status checks
fail on the test instances launched from the snapshots.

- SkipSnapshotsBy

Type: String

Description: (Optional) The interval at which snapshots are skipped when
searching for snapshots to restore your instance. For example, if there are
100 snapshots available, and you specify a value of 2 for this parameter,
then every third snapshot is reviewed.

Default: 0

- SnapshotId

Type: String

Description: (Optional) The ID of a snapshot you want to restore the
instance from.

- StartDate

Type: String

Description: (Optional) The first date you want the automation to look for
a snapshot.

- TotalSnapshotsToLook

Type: String

Description: (Optional) The number of snapshots the automation
reviews.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `ssm:DescribeInstanceInformation`
- `ec2:AttachVolume`
- `ec2:CreateImage`
- `ec2:CreateTags`
- `ec2:CreateVolume`
- `ec2:DeleteTags`
- `ec2:DeregisterImage`
- `ec2:DescribeInstances`
- `ec2:DescribeInstanceStatus`
- `ec2:DescribeImages`
- `ec2:DescribeSnapshots`
- `ec2:DescribeVolumes`
- `ec2:DetachVolume`
- `ec2:RunInstances`
- `ec2:StartInstances`
- `ec2:StopInstances`
- `ec2:TerminateInstances`
- `cloudwatch:GetMetricData`

**Document Steps**

1. `aws:executeAwsApi` - Gathers details about the target
   instance.
2. `aws:assertAwsResourceProperty` - Verifies the target instance
   exists.
3. `aws:assertAwsResourceProperty` - Verifies the root volume is
   an Amazon EBS volume.
4. `aws:assertAwsResourceProperty` - Verifies that another
   automation isn't already running that targets this instance.
5. `aws:executeAwsApi` - Tags the target instance.
6. `aws:executeAwsApi` - Creates an AMI of the instance.
7. `aws:executeAwsApi` - Gathers details about the AMI created
   in the previous step.
8. `aws:waitForAwsResourceProperty` - Waits for the AMI state to
   become `available` before proceeding.
9. `aws:executeScript` - Launches a new instance from the newly
   created AMI.
10. `aws:assertAwsResourceProperty` - Verifies the instance state
    is `available`.
11. `aws:executeAwsApi` - Gathers details about the newly launched
    instance.
12. `aws:branch` - Branches based on whether you provided a value
    for the `SnapshotId` parameter.
13. `aws:executeScript` - Returns a list of snapshots within the
    time period specified.
14. `aws:executeAwsApi` - Stops the instance.
15. `aws:waitForAwsResourceProperty` - Waits for the volume state
    to be `available`.
16. `aws:waitForAwsResourceProperty` - Waits for the instance state
    to be `stopped`.
17. `aws:executeAwsApi` - Detaches the root volume.
18. `aws:waitForAwsResourceProperty` - Waits for the root volume to
    be detached.
19. `aws:executeAwsApi` - Attaches the new root volume.
20. `aws:waitForAwsResourceProperty` - Waits for the new volume to
    be attached.
21. `aws:executeAwsApi` - Starts the instance.
22. `aws:waitForAwsResourceProperty` - Waits for the instance state
    to be `available`.
23. `aws:waitForAwsResourceProperty` - Waits for system and
    instance status checks to pass for the instance.
24. `aws:executeScript` - Runs a script to find a snapshot that can
    be used to successfully create a volume.
25. `aws:executeScript` - Runs a script to recover the instance
    using the newly created volume from the snapshot identified by the
    automation, or using the volume created from the snapshot you specified in
    the `SnapshotId` parameter.
26. `aws:executeScript` - Deletes resources created by the
    automation.

**Outputs**

launchCloneInstance.InstanceIds

ListSnapshotByDate.finalSnapshots

ListSnapshotByDate.remainingSnapshotToBeCheckedInSameDateRange

findWorkingSnapshot.workingSnapshot

InstanceRecovery.result
