# Import your VM as an image

After exporting your VM from your virtualization environment, you can import it to Amazon EC2
using VM Import/Export. The import process is the same regardless of the origin of the VM.

###### Tasks

- [Prerequisites for importing a VM into Amazon EC2](#import-image-prereqs "#import-image-prereqs")
- [Upload the image to Amazon S3](#upload-image "#upload-image")
- [Import the VM](#import-vm "#import-vm")

## Prerequisites for importing a VM into Amazon EC2

- Create an Amazon Simple Storage Service (Amazon S3) bucket for storing the exported images or choose
  an existing bucket. The bucket must be in the Region where you
  want to import your VMs. For more information about S3 buckets,
  see the [Amazon Simple Storage Service User Guide](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md").
- Create an IAM role named `vmimport`. For more information,
  see [Required service role](required-permissions.md#vmimport-role "required-permissions.md#vmimport-role").
- If you have not already installed the AWS CLI on the computer you'll use
  to run the import commands, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

###### Tip

In [supported
AWS Regions](../../../cloudshell/latest/userguide/supported-aws-regions.md "../../../cloudshell/latest/userguide/supported-aws-regions.md"), you can also use [AWS CloudShell](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md") for a
browser-based, pre-authenticated shell that launches directly from the
AWS Management Console.

## Upload the image to Amazon S3

Upload your VM image file to your S3 bucket using the upload tool of your
choice. For information about uploading objects through the Amazon S3 console, see
[Uploading Objects](../../../AmazonS3/latest/userguide/upload-objects.md "../../../AmazonS3/latest/userguide/upload-objects.md").

## Import the VM

After you upload your VM image file to Amazon S3, you can use the AWS CLI to import the
image. These tools accept either the S3 bucket and path to the file or a URL for a
public Amazon S3 file. Private Amazon S3 files require a [presigned URL](../../../AmazonS3/latest/userguide/ShareObjectPreSignedURL.md "../../../AmazonS3/latest/userguide/ShareObjectPreSignedURL.md").

You can also use the _Import virtual machine images to AWS
template_ in the [Migration Hub
Orchestrator](https://console.aws.amazon.com/migrationhub/orchestrator/ "https://console.aws.amazon.com/migrationhub/orchestrator/") console to import your on-premises virtual machine images
to AWS. For more information, see [Example 4: Import an image using Migration Hub Orchestrator](#import-vm-mho "#import-vm-mho").

###### Important

- AWS VM Import/Export strongly recommends specifying a value for either the
  `--license-type` or `--usage-operation` parameter
  when you create a new VM Import task. This ensures your operating system is
  licensed appropriately and your billing is optimized. For more information,
  see [Licensing for your imported VMs](licensing.md "licensing.md").
- AWS VM Import/Export only supports images that were natively installed inside
  the source VM and not those created using a physical-to-virtual (P2V) conversion
  process. For more information, see the [VM Import/Export Requirements](vmie_prereqs.md "vmie_prereqs.md").

###### Examples

- [Example 1: Import an image using an OVA file](#import-vm-single-disk "#import-vm-single-disk")
- [Example 2: Import an image with multiple disks](#import-vm-multi-disk "#import-vm-multi-disk")
- [Example 3: Import with the encrypted option enabled](#import-vm-encrypted "#import-vm-encrypted")
- [Example 4: Import an image using Migration Hub Orchestrator](#import-vm-mho "#import-vm-mho")

### Example 1: Import an image using an OVA file

AWS CLI
Use the following [import-image](../../../cli/latest/reference/ec2/import-image.md "../../../cli/latest/reference/ec2/import-image.md")
command.

```
aws ec2 import-image \
    --description "$(date '+%b %d %H:%M') `My server VM`" \
    --license-type "AWS" \
    --disk-containers '[{
    "Format": "OVA",
    "UserBucket": {
      "S3Bucket": "`amzn-s3-demo-import-bucket`",
      "S3Key": "`vms`/`my-server-vm.ova`"
    }
  }]'
```

PowerShell
Use the [Import-EC2Image](../../../powershell/latest/reference/items/Import-EC2Image.md "../../../powershell/latest/reference/items/Import-EC2Image.md") cmdlet as follows.

```
Import-EC2Image `
    -Description ((Get-Date -Format "MMM dd HH:mm ") + "`My server OVA`") `
    -LicenseType "AWS" `
    -DiskContainer @(
        @{
            Format = "OVA"
            UserBucket = @{
                S3Bucket = "`amzn-s3-demo-import-bucket`"
                S3Key = "`vms`/`my-server-vm.ova`"
            }
        }
    )
```

### Example 2: Import an image with multiple disks

AWS CLI
Use the [import-image](../../../cli/latest/reference/ec2/import-image.md "../../../cli/latest/reference/ec2/import-image.md")
command.

```
aws ec2 import-image \
    --description "$(date '+%b %d %H:%M') `My server disks`" \
    --license-type "AWS" \
    --disk-containers '[
    {
      "Description": "`First disk`",
      "Format": "vmdk",
      "UserBucket": {
        "S3Bucket": "`amzn-s3-demo-import-bucket`",
        "S3Key": "`disks`/`my-server-vm-disk2.vmdk`"
      }
    },
    {
      "Description": "`Second disk`",
      "Format": "vmdk",
      "UserBucket": {
        "S3Bucket": "`amzn-s3-demo-import-bucket`",
        "S3Key": "`disks`/`my-server-vm-disk2.vmdk`"
      }
    }
  ]'
```

PowerShell
Use the [Import-EC2Image](../../../powershell/latest/reference/items/Import-EC2Image.md "../../../powershell/latest/reference/items/Import-EC2Image.md") cmdlet as follows.

```
Import-EC2Image `
    -Description ((Get-Date -Format "MMM dd HH:mm ") + "`My server disks`") `
    -LicenseType "AWS" `
    -DiskContainer @(
        @{
            Description = "`First disk`"
            Format = "vmdk"
            UserBucket = @{
                S3Bucket = "`amzn-s3-demo-import-bucket`"
                S3Key = "`disks`/`my-server-vm-disk1.vmdk`"
            }
        },
        @{
            Description = "`Second disk`"
            Format = "vmdk"
            UserBucket = @{
                S3Bucket = "`amzn-s3-demo-import-bucket`"
                S3Key = "`disks`/`my-server-vm-disk2.vmdk`"
            }
        }
    )
```

### Example 3: Import with the encrypted option enabled

The CMK provided for encryption must not be disabled during the entire import process.
For more information, see [Amazon EBS encryption](../../../ebs/latest/userguide/ebs-encryption.md "../../../ebs/latest/userguide/ebs-encryption.md") in the _Amazon EBS User Guide_.

AWS CLI
Use the following [import-image](../../../cli/latest/reference/ec2/import-image.md "../../../cli/latest/reference/ec2/import-image.md") command.

```
aws ec2 import-image \
    --description "$(date '+%b %d %H:%M') `My server OVA`" \
    --encrypted \
    --kms-key-id `0ea3fef3-80a7-4778-9d8c-1c0c6EXAMPLE` \
    --disk-containers '[{
        "Format": "OVA",
        "UserBucket": {
          "S3Bucket": "`amzn-s3-demo-import-bucket`",
          "S3Key": "`vms`/`my-server-vm.ova`"
        }
    }]'
```

PowerShell
Use the [Import-EC2Image](../../../powershell/latest/reference/items/Import-EC2Image.md "../../../powershell/latest/reference/items/Import-EC2Image.md") cmdlet as follows.

```
Import-EC2Image `
    -Description ((Get-Date -Format "MMM dd HH:mm ") + "`My server disks`") `
    -LicenseType "AWS" `
    -DiskContainer @(
        @{
            Format = "OVA"
            UserBucket = @{
                S3Bucket = "`amzn-s3-demo-import-bucket`"
                S3Key = "`vms`/`my-server-vm.ova`"
            }0
        }
    ) `
    -Encrypted $true `
    -KmsKeyId "alias/aws/ebs"
```

### Example 4: Import an image using Migration Hub Orchestrator

Console

###### To import an image using a template

1. Open the [Migration Hub Orchestrator
   console](https://console.aws.amazon.com/migrationhub/orchestrator "https://console.aws.amazon.com/migrationhub/orchestrator").
2. In the navigation pane, choose **Create migration
   workflow**.
3. On the **Choose a workflow template** page,
   choose the **Import virtual images to AWS**
   template.
4. Configure and submit your workflow to begin the VM import. For more
   information, see the [_AWS Migration Hub Orchestrator User Guide_](../../../migrationhub-orchestrator/latest/userguide/import-vm-images.md "../../../migrationhub-orchestrator/latest/userguide/import-vm-images.md").
