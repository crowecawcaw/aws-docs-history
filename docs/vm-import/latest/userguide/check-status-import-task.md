# Monitor an import snapshot task

After you start an import snapshot task using VM Import/Export, you can monitor the import
operation. If the task status is `active`, it means that the import
task is in progress. The snapshot is ready to use when the status is `completed`.

AWS CLI

###### To get the status of an import snapshot task

Use the following [describe-import-snapshot-tasks](../../../cli/latest/reference/ec2/describe-import-snapshot-tasks.md "../../../cli/latest/reference/ec2/describe-import-snapshot-tasks.md")
command.

```
aws ec2 describe-import-snapshot-tasks \
    --import-task-ids `import-snap-1234567890abcdef0`
```

The following is example output.

```
{
    "ImportSnapshotTasks": [
        {
            "Description": "My server VM",
            "ImportTaskId": "import-snap-1234567890abcdef0",
            "SnapshotTaskDetail": {
                "Description": "My server VMDK",
                "DiskImageSize": "3.115815424E9",
                "Format": "VMDK",
                "Progress": "22",
                "Status": "active",
                "StatusMessage": "downloading/converting",
                "UserBucket": {
                    "S3Bucket": "amzn-s3-demo-import-bucket",
                    "S3Key": "vms/my-server-vm.vmdk"
                },
            }
        }
    ]
}
```

###### To get the status of all import snapshot tasks

Use the following [describe-import-snapshot-tasks](../../../cli/latest/reference/ec2/describe-import-snapshot-tasks.md "../../../cli/latest/reference/ec2/describe-import-snapshot-tasks.md")
command.

```
aws ec2 describe-import-snapshot-tasks \
    --query "ImportSnapshotTasks[*].{Description:Description, ImportTaskId:ImportTaskId, Status:SnapshotTaskDetail.Status, Progress: SnapshotTaskDetail.Progress, SnapshotID: SnapshotTaskDetail.SnapshotId,  S3Key: SnapshotTaskDetail.UserBucket.S3Key}" \
    --output table
```

The following is example output. You can display any additional fields that you need.

```
----------------------------------------------------------------------------------------------------------------------------
|                                                    DescribeImportSnapshotTasks                                           |
+--------------+--------------------------------+-------------+-----------+----------------------+-------------------------+
|  Description |         ImportTaskId           |   Status    | Progress  |        S3Key         |       SnapshotID        |
+--------------+--------------------------------+-------------+-----------+----------------------+-------------------------+
|  My server VM|  import-snap-1234567890abcdef0 |  active     |  19       |  my-server-vm.vmdk   |                         |
|  My server VM|  import-snap-1234567890abcdef1 |  completed  |  None     |  my-server-vm1.vmdk  |  snap-0bd3ea32600000000 |
|  My server VM|  import-snap-1234567890abcdef2 |  completed  |  None     |  my-server-vm2.vmdk  |  snap-090ec0d0eb1111111 |
|  My server VM|  import-snap-1234567890abcdef3 |  deleted    |  None     |  my-server-vm3.vmdk  |                         |
+--------------+--------------------------------+-------------+-----------+----------------------+-------------------------+
```

PowerShell

###### To get the status of an import snapshot task

Use the [Get-EC2ImportSnapshotTask](../../../powershell/latest/reference/items/Get-EC2ImportSnapshotTask.md "../../../powershell/latest/reference/items/Get-EC2ImportSnapshotTask.md") cmdlet as follows.

```
Get-EC2ImportSnapshotTask `
    -ImportTaskId `import-snap-1234567890abcdef0` |
        Format-List *,
           @{Name='SnapshotTaskDetail';Expression={ $_.SnapshotTaskDetail | Out-String }},
           @{Name='UserBucket';Expression={ $_.SnapshotTaskDetail.UserBucket | Out-String }}
```

The following is example output.

```
Description        : My server VM
ImportTaskId       : import-snap-1234567890abcdef0
SnapshotTaskDetail : Amazon.EC2.Model.SnapshotTaskDetail
Tags               :
SnapshotTaskDetail :
                     Description   :
                     DiskImageSize : 2495933952
                     Encrypted     :
                     Format        : VMDK
                     KmsKeyId      :
                     Progress      :
                     SnapshotId    : snap-111222333444aaabb
                     Status        : completed
                     StatusMessage :
                     Url           :
                     UserBucket    : Amazon.EC2.Model.UserBucketDetails
UserBucket         :
                     S3Bucket : amzn-s3-demo-import-bucket
                     S3Key    : my-server-vm.vmdk
```

###### To get the status of all import snapshot tasks

Use the [Get-EC2ImportSnapshotTask](../../../powershell/latest/reference/items/Get-EC2ImportSnapshotTask.md "../../../powershell/latest/reference/items/Get-EC2ImportSnapshotTask.md") cmdlet as follows.

```
Get-EC2ImportSnapshotTask |
    Format-Table Description, ImportTaskId,
        @{Name='Status';Expression={$_.SnapshotTaskDetail.Status}},
        @{Name='Progress';Expression={$_.SnapshotTaskDetail.Progress}},
        @{Name='SnapshotID';Expression={$_.SnapshotTaskDetail.SnapshotID}},
        @{Name='S3Key Source';Expression={$_.SnapshotTaskDetail.UserBucket.S3Key}}
```

The following is example output. You can display any additional fields that you need.

```
Description  ImportTaskId                  Status    Progress SnapshotID             S3Key Source
-----------  ------------                  ------    -------- ----------             ------------
My server VM import-snap-1234567890abcdef0 active    19                              my-server-vm.vmdk
My server VM import-snap-1234567890abcdef1 completed          snap-0450e071240000000 my-server-vm1.vmdk
My server VM import-snap-1234567890abcdef2 completed          snap-0bd3ea32601111111 my-server-vm2.vmdk
My server VM import-snap-1234567890abcdef3 deleted                                   my-server-vm3.vmdk
```
