# Monitor an import image task

You can monitor the progress of an import image task for VM Import/Export. The following
are the status values for an import image task:

- `active` — The import task is in progress.
- `deleting` — The import task is being canceled.
- `deleted` — The import task is canceled.
- `updating` — Import status is updating.
- `validating` — The imported image is being
  validated.
- `validated` — The imported image was validated.
- `converting` — The imported image is being converted into
  an AMI.
- `completed` — The import task is completed and the AMI is
  ready to use.

AWS CLI

###### To get the status of an import image task

Use the following [describe-import-image-tasks](../../../cli/latest/reference/ec2/describe-import-image-tasks.md "../../../cli/latest/reference/ec2/describe-import-image-tasks.md")
command.

```
aws ec2 describe-import-image-tasks \
    --import-task-ids `import-ami-1234567890abcdef0`
```

The following is example output. When the import task is completed, the ID
of the AMI is provided in `ImageId`.

```
{
    "ImportImageTasks": [
        {
            "ImportTaskId": "import-ami-01234567890abcdef",
            "ImageId": "ami-1234567890EXAMPLE",
            "SnapshotDetails": [
                {
                    "DiskImageSize": 705638400.0,
                    "Format": "ova",
                    "SnapshotId": "snap-111222333444aaabb",
                    "Status": "completed",
                    "UserBucket": {
                        "S3Bucket": "amzn-s3-demo-import-bucket",
                        "S3Key": "vms/my-server-vm.ova"
                    }
                }
            ],
            "Status": "completed"
        }
    ]
}
```

###### To get the status of all import image tasks

Use the following [describe-import-image-tasks](../../../cli/latest/reference/ec2/describe-import-image-tasks.md "../../../cli/latest/reference/ec2/describe-import-image-tasks.md") command. The
**sed** command truncates the status message. If the
task fails and the status message is long, it makes the table harder to read.

```
aws ec2 describe-import-image-tasks \
  --query "ImportImageTasks[*].{Description:Description, Progress:Progress, Status:Status, ImportTaskId:ImportTaskId, StatusMessage:StatusMessage}" \
  --output table | \
    sed 's/\(.\{120\}\).*/\1|/'
```

The following is example output. You can display any additional fields
that you need.

```
+---------------------+-------------------------------+-----------+----------+-----------------
|    Description      |         ImportTaskId          | Progress  | Status   |  StatusMessage |
+----------------------------------+------------------+-----------+----------+----------------+
|  My server disks    |  import-ami-01234567890abaaaa |  62       |  active  |  booting       |
|  My server OVA      |  import-ami-01234567890abbbbb |  62       |  active  |  booting       |
|  My server disks    |  import-ami-01234567890accccc |  62       |  active  |  booting       |
+----------------------------------+------------------+-----------+----------+----------------+
```

PowerShell

###### To get the status of an import image task

Use the [Get-EC2ImportImageTask](../../../powershell/latest/reference/items/Get-EC2ImportImageTask.md "../../../powershell/latest/reference/items/Get-EC2ImportImageTask.md") cmdlet as follows.

```
Get-EC2ImportImageTask `
    -ImportTaskId `import-ami-01234567890abcdef` |
        Format-List ImportTaskId, Status, Progress, ImageId,
           @{Name='SnapshotDetails';Expression={ $_.SnapshotDetails | Out-String }},
           @{Name='UserBucket';Expression={ $_.SnapshotDetails.UserBucket | Out-String }},
```

The following is example output. When the import task is completed, the ID
of the AMI is provided in `ImageId`.

```
ImportTaskId          : import-ami-01234567890abcdef
Status                : completed
Progress              :
ImageId               : ami-1234567890EXAMPLE
SnapshotDetails       :
                        Description   :
                        DeviceName    : /dev/sda1
                        DiskImageSize : 549272064
                        Format        : VMDK
                        Progress      :
                        SnapshotId    : snap-111222333444aaabb
                        Status        : completed
                        StatusMessage :
                        Url           :
                        UserBucket    : Amazon.EC2.Model.UserBucketDetails
UserBucket            :
                        S3Bucket : amzn-s3-demo-import-bucket
                        S3Key    : vms/my-server-vm.ova
```

###### To get the status of all import image tasks

Use the [Get-EC2ImportImageTask](../../../powershell/latest/reference/items/Get-EC2ImportImageTask.md "../../../powershell/latest/reference/items/Get-EC2ImportImageTask.md") cmdlet as follows.

```
Get-EC2ImportImageTask |
    Format-Table Description, ImportTaskId, Progress, Status, StatusMessage -AutoSize
```

The following is example output. You can display any additional fields
that you need.

```
Description       ImportTaskId                 Progress Status     StatusMessage
----------------- ------------                 -------- ------     -------------
My server disks   import-ami-01234567890abaaaa 62       active     booting
My server OVA     import-ami-01234567890abbbbb 62       active     booting
My server disks   import-ami-01234567890accccc          completed
```
