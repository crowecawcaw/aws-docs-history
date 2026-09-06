

# Import a disk as an EBS snapshot using VM Import/Export
<a name="vmimport-import-snapshot"></a>

VM Import/Export enables you to import your disks as Amazon EBS snapshots. After the snapshot is created, you can create an EBS volume from the snapshot, and then attach the volume to an EC2 instance.

An imported snapshot has an arbitrary volume ID that should not be used for any purpose.

## Prerequisites for importing a snapshot
<a name="import-snapshot-prerequisites"></a>
+ The following disk formats are supported: Virtual Hard Disk (VHD/VHDX), ESX Virtual Machine Disk (VMDK), and raw.
+ You must first upload your disks to Amazon S3.
+ If you have not already installed the AWS CLI on the computer you'll use to run the import commands, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/).
**Tip**  
In [supported AWS Regions](https://docs.aws.amazon.com/cloudshell/latest/userguide/supported-aws-regions.html), you can also use [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html) for a browser-based, pre-authenticated shell that launches directly from the AWS Management Console.

## Start an import snapshot task
<a name="start-import-task"></a>

You can specify the URL of the S3 bucket that contains the disk image or provide the S3 bucket name and key.

------
#### [ AWS CLI ]

**To import a snapshot**  
Use the [import-snapshot](https://docs.aws.amazon.com/cli/latest/reference/ec2/import-snapshot.html) command.

```
aws ec2 import-snapshot \
    --description "{{My server VM}}" \
    --disk-container "file://{{C:\import\containers.json}}"
```

The file `containers.json` is a JSON document that contains the required information.

```
{
    "Description": "My server VM",
    "Format": "VMDK",
    "UserBucket": {
        "S3Bucket": "amzn-s3-demo-import-bucket",
        "S3Key": "vms/my-server-vm.vmdk"
    }
}
```

The following is example output.

```
{
    "Description": "My server VM",
    "ImportTaskId": "import-snap-1234567890abcdef0",
    "SnapshotTaskDetail": {
        "Description": "My server VMDK",
        "DiskImageSize": "0.0",
        "Format": "VMDK",
        "Progress": "3",
        "Status": "active",
        "StatusMessage": "pending",
        "UserBucket": {
            "S3Bucket": "amzn-s3-demo-import-bucket",
            "S3Key": "vms/my-server-vm.vmdk"
        }
    }
}
```

------
#### [ PowerShell ]

**To import a snapshot**  
Use the [Import-EC2Snapshot](https://docs.aws.amazon.com/powershell/latest/reference/items/Import-EC2Snapshot.html) cmdlet.

```
Import-EC2Snapshot `
    -DiskContainer_Description "My server VM" `
    -DiskContainer_Format "VMDK" `
    -DiskContainer_S3Bucket "amzn-s3-demo-import-bucket" `
    -DiskContainer_S3Key "vms/my-server-vm.vmdk"
```

The following is example output.

```
Description  ImportTaskId                  SnapshotTaskDetail                  Tags
-----------  ------------                  ------------------                  ----
My server VM import-snap-1234567890abcdef0 Amazon.EC2.Model.SnapshotTaskDetail
```

------