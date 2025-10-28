# Use `DescribeImportSnapshotTasks` with a CLI

The following code examples show how to use `DescribeImportSnapshotTasks`.

CLI

**AWS CLI**

**To monitor an import snapshot task**

The following `describe-import-snapshot-tasks` example checks the status of the specified import snapshot task.

```
`aws ec2 describe-import-snapshot-tasks \
 --import-task-ids `import-snap-1234567890abcdef0``

```

Output for an import snapshot task that is in progress:

```
{
    "ImportSnapshotTasks": [
        {
            "Description": "My server VMDK",
            "ImportTaskId": "import-snap-1234567890abcdef0",
            "SnapshotTaskDetail": {
                "Description": "My server VMDK",
                "DiskImageSize": "705638400.0",
                "Format": "VMDK",
                "Progress": "42",
                "Status": "active",
                "StatusMessage": "downloading/converting",
                "UserBucket": {
                    "S3Bucket": "my-import-bucket",
                    "S3Key": "vms/my-server-vm.vmdk"
                }
            }
        }
    ]
}
```

Output for an import snapshot task that is completed. The ID of the resulting snapshot is provided by `SnapshotId`.

```
{
    "ImportSnapshotTasks": [
        {
            "Description": "My server VMDK",
            "ImportTaskId": "import-snap-1234567890abcdef0",
            "SnapshotTaskDetail": {
                "Description": "My server VMDK",
                "DiskImageSize": "705638400.0",
                "Format": "VMDK",
                "SnapshotId": "snap-1234567890abcdef0"
                "Status": "completed",
                "UserBucket": {
                    "S3Bucket": "my-import-bucket",
                    "S3Key": "vms/my-server-vm.vmdk"
                }
            }
        }
    ]
}
```

- For API details, see
  [DescribeImportSnapshotTasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-import-snapshot-tasks.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-import-snapshot-tasks.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example describes the specified snapshot import task.**

```
Get-EC2ImportSnapshotTask -ImportTaskId import-snap-abcdefgh

```

**Output:**

```
Description             ImportTaskId               SnapshotTaskDetail
-----------------       --------------------       ------------------
Disk Image Import 1     import-snap-abcdefgh       Amazon.EC2.Model.SnapshotTaskDetail
```

**Example 2: This example describes all your snapshot import tasks.**

```
Get-EC2ImportSnapshotTask

```

**Output:**

```
Description             ImportTaskId               SnapshotTaskDetail
-----------------       --------------------       ------------------
Disk Image Import 1     import-snap-abcdefgh       Amazon.EC2.Model.SnapshotTaskDetail
Disk Image Import 2     import-snap-hgfedcba       Amazon.EC2.Model.SnapshotTaskDetail
```

- For API details, see
  [DescribeImportSnapshotTasks](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example describes the specified snapshot import task.**

```
Get-EC2ImportSnapshotTask -ImportTaskId import-snap-abcdefgh

```

**Output:**

```
Description             ImportTaskId               SnapshotTaskDetail
-----------------       --------------------       ------------------
Disk Image Import 1     import-snap-abcdefgh       Amazon.EC2.Model.SnapshotTaskDetail
```

**Example 2: This example describes all your snapshot import tasks.**

```
Get-EC2ImportSnapshotTask

```

**Output:**

```
Description             ImportTaskId               SnapshotTaskDetail
-----------------       --------------------       ------------------
Disk Image Import 1     import-snap-abcdefgh       Amazon.EC2.Model.SnapshotTaskDetail
Disk Image Import 2     import-snap-hgfedcba       Amazon.EC2.Model.SnapshotTaskDetail
```

- For API details, see
  [DescribeImportSnapshotTasks](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
