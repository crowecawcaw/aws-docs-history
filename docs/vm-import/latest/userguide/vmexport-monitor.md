# Monitor an instance export task

After you start an instance export task using VM Import/Export, you can monitor the export
operation.

AWS CLI

###### To monitor an instance export task

Use the following [describe-export-tasks](../../../cli/latest/reference/ec2/describe-export-tasks.md "../../../cli/latest/reference/ec2/describe-export-tasks.md")
command.

```
aws ec2 describe-export-tasks \
    --export-task-ids `export-i-1234567890abcdef0`
```

The following is example output. The status shown is `active`.
The VM is ready to use when the status is `completed`.

```
{
    "ExportTasks": [
        {
            "ExportTaskId": "export-i-1234567890abcdef0",
            "ExportToS3Task": {
                "ContainerFormat": "ova",
                "DiskImageFormat": "VMDK",
                "S3Bucket": "amzn-s3-demo-export-bucket",
                "S3Key": "vms/export-i-1234567890abcdef0.ova"
            },
            "InstanceExportDetails": {
                "InstanceId": "i-1234567890abcdef0",
                "TargetEnvironment": "vmware"
            },
            "State": "active"
        }
    ]
}

```

###### To monitor all instance export tasks

Use the following [describe-export-tasks](../../../cli/latest/reference/ec2/describe-export-tasks.md "../../../cli/latest/reference/ec2/describe-export-tasks.md")
command.

```
aws ec2 describe-export-tasks \
    --query "ExportTasks[*].{Description:Description,ExportTaskId:ExportTaskId,State:State,S3Bucket:ExportToS3Task.S3Bucket,InstanceId:InstanceExportDetails.InstanceId}" \
    --output table
```

The following is example output. You can display any additional fields
that you need.

````
------------------------------------------------------------------------------------------------------------------------------------
|                                                    DescribeExportTasks                                                           | +----------------------------------+-----------------------------+----------------------+-----------------------------+------------+
|            Description           |        ExportTaskId         |      InstanceId      |     S3Bucket                |    State   | +----------------------------------+-----------------------------+----------------------+-----------------------------+------------+
|  Jul 15 01:18 My instance export |  export-i-01234567890abaaaa |  None                |  amzn-s3-demo-export-bucket |  active    |
|  Jul 15 11:01 My instance export |  export-i-01234567890abbbbb |  None                |  amzn-s3-demo-export-bucket |  active    |
|  Jul 13 11:00 My instance export |  export-i-01234567890accccc |  i-0abcdef1234567890 |  amzn-s3-demo-export-bucket |  completed | +----------------------------------+-----------------------------+----------------------+-----------------------------+------------+ ``` PowerShell ###### To monitor an instance export task Use the [Get-EC2ExportTask](../../../powershell/latest/reference/items/Get-EC2ExportTask.md "../../../powershell/latest/reference/items/Get-EC2ExportTask.md") cmdlet as follows. ``` Get-EC2ExportTask ` -ExportTaskId `export-i-1234567890abcdef0` | Format-List *, @{Name='ExportToS3Task';Expression={$_.ExportToS3Task | Out-string}}, @{Name='InstanceExportDetails';Expression={$_.InstanceExportDetails | Out-string}} ``` The following is example output. The status shown is `active`. The VM is ready to use when the status is `completed`. ``` Description           : Jul 15 14:55 My instance export ExportTaskId          : export-i-1234567890abcdef0 ExportToS3Task        : Amazon.EC2.Model.ExportToS3Task InstanceExportDetails : Amazon.EC2.Model.InstanceExportDetails State                 : completed StatusMessage         : Tags                  : {} ExportToS3Task        : ContainerFormat : ova DiskImageFormat : VMDK S3Bucket        : amzn-s3-demo-export-bucket S3Key           : vms/export-i-1234567890abcdef0.ova InstanceExportDetails : InstanceId        : i-1234567890abcdef0 TargetEnvironment : vmware ``` ###### To monitor all instance export tasks Use the [Get-EC2ExportTask](../../../powershell/latest/reference/items/Get-EC2ExportTask.md "../../../powershell/latest/reference/items/Get-EC2ExportTask.md") cmdlet as follows. ``` Get-EC2ExportTask | Format-Table Description, ExportTaskId, State, @{Name='S3Bucket';Expression={$_.ExportToS3Task.S3Bucket}}, @{Name='InstanceId';Expression={$_.InstanceExportDetails.InstanceId}} ``` The following is example output. You can display any additional fields that you need. ``` Description                     ExportTaskId               State     S3Bucket                     InstanceId -----------                     ------------               -----     --------                     ---------- Jul 15 01:18 My instance export export-i-01234567890abaaaa active    amzn-s3-demo-export-bucket Jul 15 11:01 My instance export export-i-01234567890abbbbb active    amzn-s3-demo-export-bucket Jul 13 11:00 My instance export export-i-01234567890accccc completed amzn-s3-demo-export-bucket   i-0abcdef1234567890 ```
````
