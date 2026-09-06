

# Copy an Amazon EC2 AMI
<a name="CopyingAMIs"></a>

When you need a consistent Amazon EC2 instance configuration across multiple Regions, you can use a single Amazon Machine Image (AMI) as your template to launch all the instances. However, AMIs are Region-specific resources—to launch an instance in a specific AWS Region, the AMI must be located in that Region. Therefore, to use the same AMI in multiple Regions, you must copy it from the source Region to each target Region.

The method you use to copy an AMI depends on whether you're copying across Regions *within the same [partition](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#partition)* or *across different partitions*:
+ **Cross-Region copying** – Copy AMIs across Regions *within the same partition*, for example, across the Regions within the commercial partition. This copy method is described in this topic.
+ **Cross-partition copying** – Copy AMIs *from one partition to another partition*, for example, from the commercial partition to the AWS GovCloud (US) partition. For information about this copy method, see [Store and restore an AMI](ami-store-restore.md).
+ **Cross-account copying** – Create a copy of an AMI that another AWS account has [shared with your AWS account](sharingamis-explicit.md). This copy method is described in this topic.

The time taken to complete the copy operation for cross-Region and cross-account AMI copying is on a best-effort basis. If you need control over the completion time, you can specify a completion window ranging from 15 minutes to 48 hours, ensuring your AMI is copied within your required timeframe. Additional charges apply for time-based AMI copy operations. For more information, see [Time-based copies](https://docs.aws.amazon.com/ebs/latest/userguide/time-based-copies.html) in the *Amazon EBS User Guide*.

**Topics**
+ [Considerations](#copy-ami-considerations)
+ [Costs](#copy-ami-costs)
+ [Grant permissions to copy Amazon EC2 AMIs](copy-ami-permissions.md)
+ [Copy an AMI](#ami-copy-steps)
+ [Stop a pending AMI copy operation](#ami-copy-stop)
+ [How Amazon EC2 AMI copy works](how-ami-copy-works.md)

## Considerations
<a name="copy-ami-considerations"></a>
+ **Permission to copy AMIs** – You can use IAM policies to grant or deny users permission to copy AMIs. Starting October 28, 2024, you can specify resource-level permissions for the `CopyImage` action on the source AMI. Resource-level permissions for the new AMI are available as before.
+ **Launch permissions and Amazon S3 bucket permissions** – AWS does not copy launch permissions or Amazon S3 bucket permissions from the source AMI to the new AMI. After the copy operation is complete, you can apply launch permissions and Amazon S3 bucket permissions to the new AMI.
+ **Tags** – You can only copy user-defined AMI tags that you attached to the source AMI. System tags (prefixed with `aws:`) and user-defined tags that are attached by other AWS accounts will not be copied. When copying an AMI, you can attach new tags to the new AMI and its backing snapshots.
+ **Quotas for time-based AMI copies** – After you reach your *cumulative snapshot copy throughput quota*, subsequent time-based AMI copy requests fail. For more information, see [Quotas for time-based copies](https://docs.aws.amazon.com/ebs/latest/userguide/time-based-copies.html#time-based-copies-quota) in the *Amazon EBS User Guide*.
+ **Supported source-destination copies** – The location of the source AMI determines whether you can copy it and the allowed destinations for the new AMI:
  + If the source AMI is in a Region, you can copy it within that Region, to another Region, to an Outpost associated with that Region, or to a Local Zone in that Region.
  + If the source AMI is in a Local Zone, you can copy it within that Local Zone, to the parent Region of that Local Zone, or to certain other Local Zones with the same parent Region.
  + If the source AMI is on an Outpost, you can't copy it.
+ **CLI parameters for source and destination** – When using the CLI, the following parameters are supported for specifying the source location of the AMI to copy and the destination of the new AMI. Note that the copy operation must be initiated in the destination Region; if you omit the `--region` parameter, the destination assumes the default Region configured in your AWS CLI settings.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/CopyingAMIs.html)

## Costs
<a name="copy-ami-costs"></a>

There is no charge for copying an AMI when no completion time is specified. However, additional charges apply for time-based AMI copy operations. For more information, see [Time-based copies](https://docs.aws.amazon.com/ebs/latest/userguide/time-based-copies.html#time-based-copies-pricing) in the *Amazon EBS User Guide*.

Standard storage and data transfer rates apply. If you copy an EBS-backed AMI, you will incur charges for the storage of any additional EBS snapshots.

## Copy an AMI
<a name="ami-copy-steps"></a>

You can copy an AMI that you own or an AMI that was shared with you from another account. For the supported source and destination combinations, see [Considerations](#copy-ami-considerations).

------
#### [ Console ]

**To copy an AMI**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. From the console navigation bar, select the Region that contains the AMI.

1. In the navigation pane, choose **AMIs** to display the list of AMIs available to you in the Region.

1. If you don't see the AMI you want to copy, choose a different filter. You can filter by AMIs **Owned by me**, **Private images**, **Public images**, and **Disabled images**.

1. Select the AMI to copy, and then choose **Actions**, **Copy AMI**.

1. On the **Copy Amazon Machine Image (AMI)** page, specify the following information:

   1. **AMI copy name**: A name for the new AMI. You can include the operating system information in the name because Amazon EC2 does not provide this information when displaying details about the AMI.

   1. **AMI copy description**: By default, the description includes information about the source AMI so that you can distinguish a copy from its original. You can change this description as needed.

   1. **Destination Region**: The Region in which to copy the AMI. For more information, see [Cross-Region copying](how-ami-copy-works.md#copy-amis-across-regions) and [Cross-account copying](how-ami-copy-works.md#copy-ami-across-accounts).

   1. **Copy tags**: Select this checkbox to include your user-defined AMI tags when copying the AMI. System tags (prefixed with `aws:`) and user-defined tags that are attached by other AWS accounts will not be copied.

   1. **Time-based copy**: You can specify whether the copy operation completes within a specific timeframe or on a best-effort basis, as follows:
      + To complete the copy within a specific timeframe:
        + Select **Enable time-based copy**.
        + For **Completion duration**, enter the number of minutes (in 15-minute increments) allowed for the copy operation. The completion duration applies to all snapshots associated with the AMI.

          For more information, see [Time-based copies](https://docs.aws.amazon.com/ebs/latest/userguide/time-based-copies.html) in the *Amazon EBS User Guide*.
      + To complete the copy on a best-effort basis:
        + Leave **Enable time-based copy** unselected.

   1. (EBS-backed AMIs only) **Encrypt EBS snapshots of AMI copy**: Select this checkbox to encrypt the target snapshots, or to re-encrypt them using a different key. If encryption by default is enabled, the **Encrypt EBS snapshots of AMI copy** checkbox is selected and cannot be cleared. For more information, see [Encryption and copying](how-ami-copy-works.md#ami-copy-encryption).

   1. (EBS-backed AMIs only) **KMS key**: The KMS key to used to encrypt the target snapshots.

   1. **Tags**: You can tag the new AMI and the new snapshots with the same tags, or you can tag them with different tags.
      + To tag the new AMI and the new snapshots with the *same* tags, choose **Tag image and snapshots together**. The same tags are applied to the new AMI and every snapshot that is created.
      + To tag the new AMI and the new snapshots with *different* tags, choose **Tag image and snapshots separately**. Different tags are applied to the new AMI and the snapshots that are created. Note, however, that all the new snapshots that are created get the same tags; you can't tag each new snapshot with a different tag.

      To add a tag, choose **Add tag**, and enter the key and value for the tag. Repeat for each tag.

   1. When you're ready to copy the AMI, choose **Copy AMI**.

      The initial status of the new AMI is `Pending`. The AMI copy operation is complete when the status is `Available`.

------
#### [ AWS CLI ]

**To copy an AMI from one Region to another Region**  
Use the [copy-image](https://docs.aws.amazon.com/cli/latest/reference/ec2/copy-image.html) command. You must specify both the source and destination Regions. You specify the source Region using the `--source-region` parameter. You can specify the destination Region using the `--region` parameter (or omit this parameter to assume the default Region configured in your AWS CLI settings).

```
aws ec2 copy-image \
    --source-image-id {{ami-0abcdef1234567890}} \
    --source-region {{us-west-2}} \
    --name {{my-ami}} \
    --region {{us-east-1}}
```

When you encrypt a target snapshot during AMI copy, you must specify these additional parameters: `--encrypted` and `--kms-key-id`.

**To copy an AMI from a Region to a Local Zone**  
Use the [copy-image](https://docs.aws.amazon.com/cli/latest/reference/ec2/copy-image.html) command. You must specify both the source and destination. You specify the source Region using the `--source-region` parameter. You specify the destination Local Zone using the `--destination-availability-zone` parameter (you can use `--destination-availability-zone-id` instead). Note that you can only copy an AMI from a Region to a Local Zone within that same Region.

```
aws ec2 copy-image \
    --source-image-id {{ami-0abcdef1234567890}} \
    --source-region {{cn-north-1}} \
    --destination-availability-zone {{cn-north-1-pkx-1a}} \
    --name {{my-ami}} \
    --region {{cn-north-1}}
```

**To copy an AMI from a Local Zone to a Region**  
Use the [copy-image](https://docs.aws.amazon.com/cli/latest/reference/ec2/copy-image.html) command. You must specify both the source and destination. You specify the source Region using the `--source-region` parameter. You specify the destination Region using the `--region` parameter (or omit this parameter to assume the default Region configured in your AWS CLI settings). The source Local Zone is assumed from the location of the specified source AMI ID. Note that you can only copy an AMI from a Local Zone to its parent Region.

```
aws ec2 copy-image \
    --source-image-id {{ami-0abcdef1234567890}} \
    --source-region {{cn-north-1}} \
    --name {{my-ami}} \
    --region {{cn-north-1}}
```

**To copy an AMI from one Local Zone to another Local Zone**  
Use the [copy-image](https://docs.aws.amazon.com/cli/latest/reference/ec2/copy-image.html) command. You must specify both the source and destination. You specify the source Region of the Local Zone using the `--source-region` parameter. You specify the destination Local Zone using the `--destination-availability-zone` parameter (you can use `--destination-availability-zone-id` instead). The source Local Zone is assumed from the location of the specified source AMI ID. You specify the parent Region of the destination Local Zone using the `--region` parameter (or omit this parameter to assume the default Region configured in your AWS CLI settings).

```
aws ec2 copy-image \
    --source-image-id {{ami-0abcdef1234567890}} \
    --source-region {{cn-north-1}} \
    --destination-availability-zone {{cn-north-1-pkx-1a}} \
    --name {{my-ami}} \
    --region {{cn-north-1}}
```

------
#### [ PowerShell ]

**To copy an AMI from one Region to another Region**  
Use the [Copy-EC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Copy-EC2Image.html) cmdlet. You must specify both the source and destination Regions. You specify the source Region using the `-SourceRegion` parameter. You can specify the destination Region using the `-Region` parameter or the [Set-AWSDefaultRegion](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-installing-specifying-region.html) cmdlet.

```
Copy-EC2Image `
    -SourceImageId {{ami-0abcdef1234567890}} `
    -SourceRegion {{us-west-2}} `
    -Name {{my-ami}} `
    -Region {{us-east-1}}
```

When you encrypt a target snapshot during AMI copy, you must specify these additional parameters: `-Encrypted` and `-KmsKeyId`.

**To copy an AMI from a Region to a Local Zone**  
Use the [Copy-EC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Copy-EC2Image.html) cmdlet. You must specify both the source and destination. You specify the source Region using the `-SourceRegion` parameter. You specify the destination Local Zone using the `-DestinationAvailabilityZone` parameter (you can use `-DestinationAvailabilityZoneId` instead). Note that you can only copy an AMI from a Region to a Local Zone within that same Region.

```
Copy-EC2Image `
    -SourceImageId {{ami-0abcdef1234567890}} `
    -SourceRegion {{cn-north-1}} `
    -DestinationAvailabilityZone {{cn-north-1-pkx-1a}} `
    -Name {{my-ami}} `
    -Region {{cn-north-1}}
```

**To copy an AMI from a Local Zone to a Region**  
Use the [Copy-EC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Copy-EC2Image.html) cmdlet. You must specify both the source and destination. You specify the source Region using the `-SourceRegion` parameter. You specify the destination Region using the `-Region` parameter or the [Set-AWSDefaultRegion](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-installing-specifying-region.html) cmdlet. The source Local Zone is assumed from the location of the specified source AMI ID. Note that you can only copy an AMI from a Local Zone to its parent Region.

```
Copy-EC2Image `
    -SourceImageId {{ami-0abcdef1234567890}} `
    -SourceRegion {{cn-north-1}} `
    -Name {{my-ami}} `
    -Region {{cn-north-1}}
```

**To copy an AMI from one Local Zone to another Local Zone**  
Use the [Copy-EC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Copy-EC2Image.html) cmdlet. You must specify both the source and destination. You specify the source Region of the Local Zone using the `-SourceRegion` parameter. You specify the destination Local Zone using the `-DestinationAvailabilityZone` parameter (you can use `-DestinationAvailabilityZoneId` instead). The source Local Zone is assumed from the location of the specified source AMI ID. You specify the parent Region of the destination Local Zone using the `-Region` parameter or the [Set-AWSDefaultRegion](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-installing-specifying-region.html) cmdlet.

```
Copy-EC2Image `
    -SourceImageId {{ami-0abcdef1234567890}} `
    -SourceRegion {{cn-north-1}} `
    -DestinationAvailabilityZone {{cn-north-1-pkx-1a}} `
    -Name {{my-ami}} `
    -Region {{cn-north-1}}
```

------

## Stop a pending AMI copy operation
<a name="ami-copy-stop"></a>

You can stop a pending AMI copy using the following procedures.

------
#### [ Console ]

**To stop an AMI copy operation**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. From the navigation bar, select the destination Region from the Region selector.

1. In the navigation pane, choose **AMIs**.

1. Select the AMI to stop copying, and then choose **Actions**, **Deregister AMI**.

1. When asked for confirmation, choose **Deregister AMI**.

------
#### [ AWS CLI ]

**To stop an AMI copy operation**  
Use the [deregister-image](https://docs.aws.amazon.com/cli/latest/reference/ec2/deregister-image.html) command.

```
aws ec2 deregister-image --image-id {{ami-0abcdef1234567890}}
```

------
#### [ PowerShell ]

**To stop an AMI copy operation using**  
Use the [Unregister-EC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Unregister-EC2Image.html) cmdlet.

```
Unregister-EC2Image -ImageId {{ami-0abcdef1234567890}}
```

------