# Monitor an export image task

After you start an image export using VM Import/Export, you can monitor the export operation.

AWS CLI

###### To monitor an export image task

Use the following [describe-export-image-tasks](../../../cli/latest/reference/ec2/describe-export-image-tasks.md "../../../cli/latest/reference/ec2/describe-export-image-tasks.md") command.

```
aws ec2 describe-export-image-tasks \
    --export-image-task-ids `export-ami-1234567890abcdef0`
```

The following is example output. The status shown is `active`, which
means that the export task is in progress. The image is ready to use when the status is
`completed`.

```
{
  "ExportImageTasks": [
      {
          "Description": "Jul 15 16:31 My image export",
          "ExportImageTaskId": "export-ami-1234567890abcdef0",
          "Progress": "21",
          "S3ExportLocation": {
              "S3Bucket": "amzn-s3-demo-export-bucket",
              "S3Prefix": "exports/"
          },
          "Status": "active",
          "StatusMessage": "updating"
      }
  ]
}
```

###### To monitor all export image tasks

Use the following [describe-export-image-tasks](../../../cli/latest/reference/ec2/describe-export-image-tasks.md "../../../cli/latest/reference/ec2/describe-export-image-tasks.md") command.

```
aws ec2 describe-export-image-tasks \
  --query "ExportImageTasks[*].{\
    Description:Description,\
    ExportImageTaskId:ExportImageTaskId,\
    ImageId:ImageId,\
    Status:Status,\
    Progress:Progress,\
    S3Bucket:S3ExportLocation.S3Bucket}" \
  --output table

```

The following is example output.

````
--------------------------------------------------------------------------------------------------------------------------------------------------
|                                                      DescribeExportImageTasks                                                                  | +------------------------------+-------------------------------+------------------------+-----------+------------------------------+-------------+
|          Description         |       ExportImageTaskId       |        ImageId         | Progress  |          S3Bucket            |   Status    | +------------------------------+-------------------------------+------------------------+-----------+------------------------------+-------------+
|  Jul 15 16:35 My image export|  export-ami-1234567890abcdef0 |                        |  80       |  amzn-s3-demo-export-bucket  |  active     |
|  Jul 15 16:31 My image export|  export-ami-1234567890abcdef1 |  ami-ab34567890abcdef0 |  None     |  amzn-s3-demo-export-bucket  |  completed  | +------------------------------+-------------------------------+------------------------+-----------+------------------------------+-------------+ ``` PowerShell ###### To monitor an export image task Use the [Get-EC2ExportImageTask](../../../powershell/latest/reference/items/Get-EC2ExportImageTask.md "../../../powershell/latest/reference/items/Get-EC2ExportImageTask.md") cmdlet as follows. ``` Get-EC2ExportImageTask ` -ExportImageTaskId `export-ami-1234567890abcdef0` | Format-List *, @{Name='S3ExportLocation';Expression={$_.S3ExportLocation | Format-List | Out-String}} ``` The following is example output. The status shown is `active`, which means that the export task is in progress. The image is ready to use when the status is `completed`. ``` Description       : Jul 15 16:35 My image export ExportImageTaskId : export-ami-1234567890abcdef0 ImageId           : ami-ab34567890abcdeff Progress          : 80 S3ExportLocation  : Amazon.EC2.Model.ExportTaskS3Location Status            : active StatusMessage     : converting Tags              : {} S3ExportLocation  : S3Bucket : amzn-s3-demo-export-bucket S3Prefix : exports/ ``` ###### To monitor all export image tasks Use the [Get-EC2ExportImageTask](../../../powershell/latest/reference/items/Get-EC2ExportImageTask.md "../../../powershell/latest/reference/items/Get-EC2ExportImageTask.md") cmdlet as follows. ``` Get-EC2ExportImageTask | Format-Table Description, ExportImageTaskId, ImageId, Status, Progress, @{Name='S3Bucket';Expression={$_.S3ExportLocation.S3Bucket}} ``` The following is example output. ``` Description                  ExportImageTaskId            ImageId               Status    Progress S3Bucket -----------                  -----------------            -------               ------    -------- -------- Jul 15 16:35 My image export export-ami-1234567890abcdef0                       active    80       amzn-s3-demo-export-bucket Jul 15 16:31 My image export export-ami-1234567890abcdef1 ami-ab34567890abcdef0 completed          amzn-s3-demo-export-bucket ```
````
