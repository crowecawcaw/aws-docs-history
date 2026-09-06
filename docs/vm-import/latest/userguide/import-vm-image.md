

# Import your VM as an image
<a name="import-vm-image"></a>

After exporting your VM from your virtualization environment, you can import it to Amazon EC2 using VM Import/Export. The import process is the same regardless of the origin of the VM.

**Topics**
+ [Prerequisites for importing a VM into Amazon EC2](#import-image-prereqs)
+ [Upload the image to Amazon S3](#upload-image)
+ [Import the VM](#import-vm)

## Prerequisites for importing a VM into Amazon EC2
<a name="import-image-prereqs"></a>
+ Create an Amazon Simple Storage Service (Amazon S3) bucket for storing the exported images or choose an existing bucket. The bucket must be in the Region where you want to import your VMs. For more information about S3 buckets, see the [Amazon Simple Storage Service User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).
+ Create an IAM role named `vmimport`. For more information, see [Required service role](required-permissions.md#vmimport-role).
+ If you have not already installed the AWS CLI on the computer you'll use to run the import commands, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/).
**Tip**  
In [supported AWS Regions](https://docs.aws.amazon.com/cloudshell/latest/userguide/supported-aws-regions.html), you can also use [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html) for a browser-based, pre-authenticated shell that launches directly from the AWS Management Console.

## Upload the image to Amazon S3
<a name="upload-image"></a>

Upload your VM image file to your S3 bucket using the upload tool of your choice. For information about uploading objects through the Amazon S3 console, see [Uploading Objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html).

## Import the VM
<a name="import-vm"></a>

After you upload your VM image file to Amazon S3, you can use the AWS CLI to import the image. These tools accept either the Amazon S3 bucket and path to the file, or a URL. Private Amazon S3 files provided through an `https://` URL require a [presigned URL]( https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html).

You can also use the *Import virtual machine images to AWS template* in the [Migration Hub Orchestrator](https://console.aws.amazon.com/migrationhub/orchestrator/) console to import your on-premises virtual machine images to AWS. For more information, see [Example 4: Import an image using Migration Hub Orchestrator](#import-vm-mho).

**Important**  
AWS VM Import/Export strongly recommends specifying a value for either the `--license-type` or `--usage-operation` parameter when you create a new VM Import task. This ensures your operating system is licensed appropriately and your billing is optimized. For more information, see [Licensing for your imported VMs](licensing.md).
AWS VM Import/Export only supports images that were natively installed inside the source VM and not those created using a physical-to-virtual (P2V) conversion process. For more information, see the [VM Import/Export Requirements](vmie_prereqs.md).

**Topics**
+ [Example 1: Import an image using an OVA file](#import-vm-single-disk)
+ [Example 2: Import an image with multiple disks](#import-vm-multi-disk)
+ [Example 3: Import with the encrypted option enabled](#import-vm-encrypted)
+ [Example 4: Import an image using Migration Hub Orchestrator](#import-vm-mho)

### Example 1: Import an image using an OVA file
<a name="import-vm-single-disk"></a>

------
#### [ AWS CLI ]

Use the following [import-image](https://docs.aws.amazon.com/cli/latest/reference/ec2/import-image.html) command.

```
aws ec2 import-image \
    --description "$(date '+%b %d %H:%M') {{My server VM}}" \
    --license-type "AWS" \
    --disk-containers '[{
    "Format": "OVA",
    "UserBucket": {
      "S3Bucket": "{{amzn-s3-demo-import-bucket}}",
      "S3Key": "{{vms}}/{{my-server-vm.ova}}"
    }
  }]'
```

------
#### [ PowerShell ]

Use the [Import-EC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Import-EC2Image.html) cmdlet as follows.

```
Import-EC2Image `
    -Description ((Get-Date -Format "MMM dd HH:mm ") + "{{My server OVA}}") `
    -LicenseType "AWS" `
    -DiskContainer @(
        @{
            Format = "OVA"
            UserBucket = @{
                S3Bucket = "{{amzn-s3-demo-import-bucket}}"
                S3Key = "{{vms}}/{{my-server-vm.ova}}"
            }
        }
    )
```

------

### Example 2: Import an image with multiple disks
<a name="import-vm-multi-disk"></a>

------
#### [ AWS CLI ]

Use the [import-image](https://docs.aws.amazon.com/cli/latest/reference/ec2/import-image.html) command.

```
aws ec2 import-image \
    --description "$(date '+%b %d %H:%M') {{My server disks}}" \
    --license-type "AWS" \
    --disk-containers '[
    {
      "Description": "{{First disk}}",
      "Format": "vmdk",
      "UserBucket": {
        "S3Bucket": "{{amzn-s3-demo-import-bucket}}",
        "S3Key": "{{disks}}/{{my-server-vm-disk2.vmdk}}"
      }
    },
    {
      "Description": "{{Second disk}}",
      "Format": "vmdk",
      "UserBucket": {
        "S3Bucket": "{{amzn-s3-demo-import-bucket}}",
        "S3Key": "{{disks}}/{{my-server-vm-disk2.vmdk}}"
      }
    }
  ]'
```

------
#### [ PowerShell ]

Use the [Import-EC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Import-EC2Image.html) cmdlet as follows.

```
Import-EC2Image `
    -Description ((Get-Date -Format "MMM dd HH:mm ") + "{{My server disks}}") `
    -LicenseType "AWS" `
    -DiskContainer @(
        @{
            Description = "{{First disk}}"
            Format = "vmdk"
            UserBucket = @{
                S3Bucket = "{{amzn-s3-demo-import-bucket}}"
                S3Key = "{{disks}}/{{my-server-vm-disk1.vmdk}}"
            }
        },
        @{
            Description = "{{Second disk}}"
            Format = "vmdk"
            UserBucket = @{
                S3Bucket = "{{amzn-s3-demo-import-bucket}}"
                S3Key = "{{disks}}/{{my-server-vm-disk2.vmdk}}"
            }
        }
    )
```

------

### Example 3: Import with the encrypted option enabled
<a name="import-vm-encrypted"></a>

The CMK provided for encryption must not be disabled during the entire import process. For more information, see [Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html) in the *Amazon EBS User Guide*.

------
#### [ AWS CLI ]

Use the following [import-image](https://docs.aws.amazon.com/cli/latest/reference/ec2/import-image.html) command.

```
aws ec2 import-image \
    --description "$(date '+%b %d %H:%M') {{My server OVA}}" \
    --encrypted \
    --kms-key-id {{0ea3fef3-80a7-4778-9d8c-1c0c6EXAMPLE}} \
    --disk-containers '[{
        "Format": "OVA",
        "UserBucket": {
          "S3Bucket": "{{amzn-s3-demo-import-bucket}}",
          "S3Key": "{{vms}}/{{my-server-vm.ova}}"
        }
    }]'
```

------
#### [ PowerShell ]

Use the [Import-EC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Import-EC2Image.html) cmdlet as follows.

```
Import-EC2Image `
    -Description ((Get-Date -Format "MMM dd HH:mm ") + "{{My server disks}}") `
    -LicenseType "AWS" `
    -DiskContainer @(
        @{
            Format = "OVA"
            UserBucket = @{
                S3Bucket = "{{amzn-s3-demo-import-bucket}}"
                S3Key = "{{vms}}/{{my-server-vm.ova}}"
            }0
        }
    ) `
    -Encrypted $true `
    -KmsKeyId "alias/aws/ebs"
```

------

### Example 4: Import an image using Migration Hub Orchestrator
<a name="import-vm-mho"></a>

------
#### [ Console ]

**To import an image using a template**

1. Open the [Migration Hub Orchestrator console](https://console.aws.amazon.com/migrationhub/orchestrator).

1. In the navigation pane, choose **Create migration workflow**.

1. On the **Choose a workflow template** page, choose the **Import virtual images to AWS** template.

1. Configure and submit your workflow to begin the VM import. For more information, see the [*AWS Migration Hub Orchestrator User Guide*](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/import-vm-images.html).

------