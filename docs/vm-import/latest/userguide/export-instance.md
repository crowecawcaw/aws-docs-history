# Start an instance export task

When you export your instance using VM Import/Export, the exported file is written to the
specified S3 bucket using the following S3 key:

```
`prefix`export-i-`xxxxxxxxxxxxxxxxx`.`format`
```

For example, if the bucket name is `amzn-s3-demo-export-bucket`, the prefix is `vms/`,
and the format is OVA, the exported file is written to `amzn-s3-demo-export-bucket/vms/export-i-1234567890abcdef0.ova`.

For more information about the supported formats, see [Considerations for image export](limits-image-export.md "limits-image-export.md").

###### Important

Your instance might reboot during the export process. Ensure that you are
performing this action when some downtime is acceptable.

AWS CLI

###### To export an instance

Use the [create-instance-export-task](../../../cli/latest/reference/ec2/create-instance-export-task.md "../../../cli/latest/reference/ec2/create-instance-export-task.md") command.

```
aws ec2 create-instance-export-task \
    --description "$(date '+%b %d %H:%M') `My instance export`" \
    --instance-id `i-1234567890abcdef0` \
    --target-environment `vmware` \
    --export-to-s3-task '{
        "ContainerFormat": "ova",
        "DiskImageFormat": "VMDK",
        "S3Bucket": "`amzn-s3-demo-export-bucket`",
        "S3Prefix": "`vms/`"
    }'
```

The following is an example response. The status shown is `active`, which
means that the export task is in progress. The instance export is finished when the status is
`completed`.

```
{
    "ExportTask": {
        "Description": "Jul 15 14:55 My instance export",
        "ExportTaskId": "export-i-021345abcdef6789",
        "ExportToS3Task": {
            "ContainerFormat": "ova",
            "DiskImageFormat": "vmdk",
            "S3Bucket": "amzn-s3-demo-export-bucket",
            "S3Key": "vms/export-i-021345abcdef6789.ova"
        },
        "InstanceExportDetails": {
            "InstanceId": "i-1234567890abcdef0",
            "TargetEnvironment": "vmware"
        },
        "State": "active"
    }
}
```

PowerShell

###### To export an instance

Use the [New-EC2InstanceExportTask](../../../powershell/latest/reference/items/New-EC2InstanceExportTask.md "../../../powershell/latest/reference/items/New-EC2InstanceExportTask.md") cmdlet.

```
New-EC2InstanceExportTask `
    -Description ((Get-Date -Format "MMM dd HH:mm ") + "`My instance export`") `
    -InstanceId "`i-1234567890abcdef0`" `
    -TargetEnvironment "vmware" `
    -ExportToS3Task_ContainerFormat "ova" `
    -ExportToS3Task_DiskImageFormat "VMDK" `
    -ExportToS3Task_S3Bucket "`amzn-s3-demo-export-bucket`" `
    -ExportToS3Task_S3Prefix "`vms/`"
```

The following is an example response. The status shown is `active`, which
means that the export task is in progress. The instance export is finished when the status is
`completed`.

```
Description           : Jul 15 14:53 My instance export
ExportTaskId          : export-i-021345abcdef6789
ExportToS3Task        : Amazon.EC2.Model.ExportToS3Task
InstanceExportDetails : Amazon.EC2.Model.InstanceExportDetails
State                 : active
StatusMessage         :
Tags                  : {}
```
