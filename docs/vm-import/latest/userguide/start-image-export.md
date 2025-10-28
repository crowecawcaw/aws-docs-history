# Start an export image task

When you export your image using VM Import/Export, the exported file is written to the specified S3
bucket using the following S3 key:

```
`prefix`export-ami-`xxxxxxxxxxxxxxxxx`.`format`
```

For example, if the bucket name is `amzn-s3-demo-export-bucket`, the prefix is
`exports/`, and the format is VMDK, the exported image is written to
`amzn-s3-demo-export-bucket/exports/export-ami-1234567890abcdef0.vmdk`.

For information about the supported formats, see [Considerations for image export](limits-image-export.md "limits-image-export.md").

AWS CLI

###### To export an image

Use the [export-image](../../../cli/latest/reference/ec2/export-image.md "../../../cli/latest/reference/ec2/export-image.md") command.

```
aws ec2 export-image \
    --description "$(date '+%b %d %H:%M') My image export" \
    --image-id `ami-1234567890abcdef0` \
    --disk-image-format `VMDK` \
    --s3-export-location S3Bucket=`amzn-s3-demo-export-bucket`,S3Prefix=`exports/`
```

The following is example output.

```
{
    "Description": "Jul 15 16:31 My image export",
    "DiskImageFormat": "VMDK",
    "ExportImageTaskId": "export-ami-36a041c1000000000",
    "ImageId": "ami-1234567890abcdef0",
    "Progress": "0",
    "S3ExportLocation": {
        "S3Bucket": "amzn-s3-demo-export-bucket",
        "S3Prefix": "exports/"
    },
    "Status": "active",
    "StatusMessage": "validating"
}
```

PowerShell

###### To export an image

Use the [Export-EC2Image](../../../powershell/latest/reference/items/Export-EC2Image.md "../../../powershell/latest/reference/items/Export-EC2Image.md") cmdlet.

```
Export-EC2Image `
    -Description ((Get-Date -Format "MMM dd HH:mm ") + "My image export") `
    -ImageId `ami-1234567890abcdef0` `
    -DiskImageFormat VMDK `
    -S3ExportLocation_S3Bucket `amzn-s3-demo-export-bucket` `
    -S3ExportLocation_S3Prefix `exports/`
```

The following is example output.

```
Description       : Jul 15 16:35 My image export
DiskImageFormat   : VMDK
ExportImageTaskId : export-ami-36a041c1000000000
ImageId           : ami-1234567890abcdef0
Progress          : 0
RoleName          :
S3ExportLocation  : Amazon.EC2.Model.ExportTaskS3Location
Status            : active
StatusMessage     : validating
Tags              : {}
```
