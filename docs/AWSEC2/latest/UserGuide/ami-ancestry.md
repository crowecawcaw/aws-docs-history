

# Use AMI ancestry to trace the origin of an AMI
<a name="ami-ancestry"></a>

AMI ancestry helps you trace the origin of an AMI by returning the IDs and Regions of all its ancestor AMIs. When you create or copy an AMI, the new AMI retains the ID and Region of its source (parent) AMI. This enables you to track the chain of AMIs back to the root AMI.

**Key benefits**

Using AMI ancestry helps you:
+ Track AMI derivatives to ensure compliance with internal policies.
+ Identify potentially vulnerable AMIs when a security issue is found in an ancestor AMI.
+ Maintain visibility of AMI origins across multiple Regions.

**Topics**
+ [How AMI ancestry works](#how-ami-ancestry-works)
+ [Considerations](#ami-ancestry-conditions)
+ [View AMI ancestry](#view-ami-ancestry)
+ [Identify the source AMI](#identify-source-ami-used-to-create-new-ami)

## How AMI ancestry works
<a name="how-ami-ancestry-works"></a>

AMI ancestry identifies the parent AMI that was used to create the specified AMI, the parent's parent, and so on, up to the root AMI. Here's how it works:
+ Each AMI displays the ID and Region of its source (parent) AMI.
+ Starting with your selected AMI, the list of ancestry entries displays each parent AMI in sequence.
+ The list of ancestry entries traces back until it reaches the root AMI. The root AMI is one of the following: 
  + A public AMI from a [verified provider](sharing-amis.md#verified-ami-provider) (identified by its owner alias, which is either `amazon` or `aws-marketplace`).
  + An AMI with no recorded ancestor. For example, when using [RegisterImage](creating-an-ami-ebs.md#creating-launching-ami-from-snapshot) to create an AMI directly from a set of snapshots, there is no source AMI to track, unlike when creating an AMI from an instance.
  + An AMI whose source AMI is from a different [partition](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#partition).
  + The 50th AMI in the list. The maximum number of AMIs in an ancestry list is 50.

## Considerations
<a name="ami-ancestry-conditions"></a>
+ The ID and Region of the source AMI are only available for AMIs created using [CreateImage](creating-an-ami-ebs.md#how-to-create-ebs-ami), [CopyImage](CopyingAMIs.md#ami-copy-steps), or [CreateRestoreImageTask](store-restore-how-it-works.md#CreateRestoreImageTask).
+ For AMIs created using [CreateImage](creating-an-ami-ebs.md#how-to-create-ebs-ami) (creates an AMI from an instance), the source AMI ID is the ID of the AMI used to launch the instance.
+ The source AMI information is not available for:
  + AMIs created using [RegisterImage](creating-an-ami-ebs.md#creating-launching-ami-from-snapshot) because they were created from snapshots.
  + For some older AMIs.
+ The source AMI information is preserved when:
  + AMIs are copied across Regions.
  + Source AMIs are deregistered (deleted).
  + You don’t have access to the source AMIs.
+ Each ancestry list is limited to 50 AMIs.

## View AMI ancestry
<a name="view-ami-ancestry"></a>

You can view an AMI's ancestry using the following methods.

------
#### [ Console ]

**To view the ancestry of an AMI**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **AMIs**.

1. Select an AMI and choose the **AMI ancestry** tab.

1. The **AMI ancestry entries** table lists all the AMIs in the ancestry list.
   + **AMI ID** – The identifier of each AMI in the ancestry list. The first entry in the table is the selected AMI, followed by its ancestors.
   + **Source AMI ID** – The ID of the AMI from which the AMI in the **AMI ID** column was created. A dash (**-**) indicates the end of the AMI ancestry list.
   + **Source AMI Region** – The AWS Region where the source AMI is located.
   + **Ancestry level** – The position in the ancestry list, where:
     + **0 (input AMI)** indicates the selected AMI whose ancestry you want to know.
     + Increasing numbers show older ancestors.
     + **{{n}} (original AMI)** indicates the root AMI, with the number indicating how far back the ancestry list goes.
   + **Creation date** – When the AMI was created, in UTC format.
   + **Owner alias** – The alias of the AMI owner (for example, `amazon`). A dash (**-**) indicates that the AMI has no owner alias.

------
#### [ AWS CLI ]

**To view the ancestry of an AMI**  
Use the [get-image-ancestry](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-image-ancestry.html) command and specify the AMI ID.

```
aws ec2 get-image-ancestry \
    --image-id {{ami-1111111111EXAMPLE}} \
    --region {{us-east-1}}
```

The following is example output. The output lists AMIs in ancestry order: the first entry is the specified (input) AMI, followed by its parent, parent's parent, and so on, and ends with the root AMI.

```
{
    "ImageAncestryEntries": [
        {
            "CreationDate": "2025-01-17T18:37:50.000Z",
            "ImageId": "ami-1111111111EXAMPLE", // Input AMI
            "SourceImageId": "ami-2222222222EXAMPLE",
            "SourceImageRegion": "us-east-1"

        },
        {
            "CreationDate": "2025-01-17T18:37:50.000Z",
            "ImageId": "ami-2222222222EXAMPLE", // Parent AMI
            "SourceImageId": "ami-3333333333EXAMPLE",
            "SourceImageRegion": "us-east-1"
        },
        ...
        {
            "CreationDate": "2025-01-17T18:37:50.000Z",
            "ImageId": "ami-8888888888EXAMPLE", // Root AMI
            "ImageOwnerAlias": "aws-marketplace",
            "SourceImageId": "ami-9999999999EXAMPLE",
            "SourceImageRegion": "us-east-2"
        }
    ]
}
```

------
#### [ PowerShell ]

**To view the ancestry of an AMI**  
Use the [Get-EC2ImageAncestry](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2ImageAncestry.html) cmdlet.

```
Get-EC2ImageAncestry -ImageId {{ami-1111111111EXAMPLE}}
```

The following is example output. The output lists AMIs in ancestry order: the first entry is the specified (input) AMI, followed by its parent, parent's parent, and so on, and ends with the root AMI.

```
ImageAncestryEntries : {
    @{
        CreationDate = "2025-01-17T18:37:50.000Z"
        ImageId = "ami-1111111111EXAMPLE"    # Input AMI
        SourceImageId = "ami-2222222222EXAMPLE"
        SourceImageRegion = "us-east-1"
    },
    @{
        CreationDate = "2025-01-17T18:37:50.000Z"
        ImageId = "ami-2222222222EXAMPLE"    # Parent AMI
        SourceImageId = "ami-3333333333EXAMPLE"
        SourceImageRegion = "us-east-1"
    },
    ...
    @{
        CreationDate = "2025-01-17T18:37:50.000Z"
        ImageId = "ami-8888888888EXAMPLE"    # Root AMI
        ImageOwnerAlias = "aws-marketplace"
        SourceImageId = "ami-9999999999EXAMPLE"
        SourceImageRegion = "us-east-2"
    }
}
```

------

## Identify the source AMI
<a name="identify-source-ami-used-to-create-new-ami"></a>

If you only need to identify the immediate parent (source) AMI used to create an AMI, you can use the following methods.

------
#### [ Console ]

**To identify the source AMI used to create the selected AMI**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **AMIs**.

1. Select the AMI to view its details.

   The source AMI information appears in the following fields: **Source AMI ID** and **Source AMI Region**

------
#### [ AWS CLI ]

**To identify the source AMI used to create the specified AMI**  
Use the [describe-images](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html) command.

```
aws ec2 describe-images \
    --region {{us-east-1}} \
    --image-ids {{ami-0abcdef1234567890}} \
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

------
#### [ PowerShell ]

**To identify the source AMI used to create the specified AMI**  
Use the [Get-EC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2Image.html) cmdlet.

```
Get-EC2Image -ImageId {{ami-0abcdef1234567890}} | Select SourceImageId, SourceImageRegion
```

The following is example output.

```
SourceImageId           SourceImageRegion
-------------           -----------------
ami-0abcdef1234567890 us-west-2
```

------