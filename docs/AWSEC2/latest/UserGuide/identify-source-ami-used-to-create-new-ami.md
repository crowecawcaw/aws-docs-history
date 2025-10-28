# Identify the source AMI used to

create a new Amazon EC2 AMI

You can identify the source AMI used to create a new AMI by checking the **Source
AMI ID** (console) or `sourceImageId` (AWS CLI) field on the new
AMI. This field contains the ID of the original AMI that was copied to create the
new AMI.

You can also find the Region where the source AMI was located by checking the
**Source AMI Region** (console) or
`sourceImageRegion` (AWS CLI) field.

###### Considerations

- The ID and Region of the source AMI only appear if the AMI was created by
  using the following API commands:

      + [CreateImage](creating-an-ami-ebs.md#how-to-create-ebs-ami "creating-an-ami-ebs.md#how-to-create-ebs-ami") – Creates an AMI from
       an instance.
      + [CopyImage](CopyingAMIs.md#ami-copy-steps "CopyingAMIs.md#ami-copy-steps") – Copies an AMI within the same
       Region or across Regions in the same partition.
      + [CreateRestoreImageTask](store-restore-how-it-works.md#CreateRestoreImageTask "store-restore-how-it-works.md#CreateRestoreImageTask") – Copies an
       AMI to another partition.

  If the AMI was created with any other API command, the ID and Region of the source AMI
  don't appear.

- For some older AMIs, the ID and Region of the source AMI might not be available.
- If the source AMI has been deleted, the ID and Region fields of the source AMI still
  appear on the new AMI.
- For AMIs created by using [CreateImage](creating-an-ami-ebs.md#how-to-create-ebs-ami "creating-an-ami-ebs.md#how-to-create-ebs-ami")
  (creates an AMI from an instance), the source AMI ID is the ID of the AMI
  used to launch the instance.

Console

###### To identify the source AMI used to create an AMI

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **AMIs**.
3. Select the AMI to view its details.

The source AMI information appears in the following fields:
**Source AMI ID** and **Source AMI
Region**

AWS CLI

###### To identify the source AMI used to create an AMI

Use the [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md") command and specify the ID and Region
of the AMI.

```
aws ec2 describe-images \
    --region `us-east-1` \
    --image-ids `ami-0abcdef1234567890` \
    --query "Images[].{ID:SourceImageId,Region:SourceImageRegion}"
```

The following is example output.

```
[
    {
        "ID": "ami-0abcdef1234567890",
        "Region": "us-west-2"
    }
}
```

PowerShell

###### To identify the source AMI used to create an AMI

Use the [Get-EC2Image](../../../powershell/latest/reference/items/Get-EC2Image.md "../../../powershell/latest/reference/items/Get-EC2Image.md")
cmdlet.

```
Get-EC2Image -ImageId `ami-0abcdef1234567890` | Select SourceImageId, SourceImageRegion
```

The following is example output.

```
SourceImageId           SourceImageRegion
-------------           -----------------
ami-0abcdef1234567890 us-west-2
```
