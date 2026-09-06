

# Use AMI watermarks to track and identify AMIs
<a name="ami-watermark"></a>

An AMI watermark is an identifier that you attach to your private AMIs to track provenance and enforce governance policies. Watermarks persist across the full AMI lifecycle:
+ If you create a new AMI from a running instance that was launched from a watermarked AMI, the new AMI inherits the watermark.
+ If you copy a watermarked AMI, the copy carries the watermark.
+ If you share a watermarked AMI with another account, the watermark remains visible to the recipient.

**Key benefits**
+ Track provenance across accounts and Regions—identify which AMIs derive from your approved base images.
+ Filter and find related AMIs across your accounts.
+ Help AMI consumers discover and identify trusted AMIs associated with a project or organization.
+ Enforce governance by combining watermarks with [Allowed AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-allowed-amis.html) to restrict instance launches to only AMIs carrying approved watermarks.

**Topics**
+ [How AMI watermarks work](#ami-watermark-how-it-works)
+ [Required permissions](#ami-watermark-permissions)
+ [Attach a watermark to an AMI](#ami-watermark-attach)
+ [Detach a watermark from an AMI](#ami-watermark-detach)
+ [View AMI watermarks](#ami-watermark-view)
+ [Filter AMIs by watermark](#ami-watermark-filter)

## How AMI watermarks work
<a name="ami-watermark-how-it-works"></a>

AMI watermarks are structured identifiers that you attach to your AMIs. The following describes the key characteristics of watermarks:
+ **Persists** – When you attach a watermark to an AMI, it carries forward to all derivative AMIs.
+ **Owner-only** – Only the AMI owner can attach watermarks to an AMI.
+ **Visible to everyone** – Anyone with access to the AMI can view its watermarks.
+ **Limit of 5** – An AMI can have up to a total of 5 watermarks.
+ **Not available on public AMIs** – You can't attach watermarks to public AMIs or make AMIs public if they have a watermark.
+ **Filterable** – You can filter AMIs by watermark when using `describe-images`.

### Watermark format
<a name="ami-watermark-format"></a>

A watermark is a structured object with the following fields:
+ `WatermarkKey` – The unique identifier for the watermark, composed of `{{account-id}}:{{watermark-name}}`. The account ID portion is the 12-digit AWS account ID of the AMI owner. The watermark name portion is a customer-specified name.
+ `SourceImageRegion` – The Region of the AMI to which you originally attached the watermark.
+ `SourceImageId` – The AMI to which you originally attached the watermark.
+ `SourceImageCreationDate` – The creation date of the AMI to which you originally attached the watermark.
+ `WatermarkCreationTime` – The timestamp of when you applied the watermark.

The watermark name must be 3–128 characters and can contain alphanumeric characters, parentheses (()), square brackets ([]), spaces, periods (.), slashes (/), dashes (-), single quotes ('), at-signs (@), or underscores (\_).

## Required permissions
<a name="ami-watermark-permissions"></a>

To work with AMI watermarks, you need the following IAM permissions:
+ `ec2:AttachImageWatermark` – To attach a watermark to an AMI.
+ `ec2:DetachImageWatermark` – To detach a watermark from an AMI.
+ `ec2:DescribeImages` – To view watermarks on AMIs.

## Attach a watermark to an AMI
<a name="ami-watermark-attach"></a>

You can attach a watermark to an AMI by using the console, the AWS CLI, or PowerShell.

------
#### [ Console ]

**To attach a watermark to an AMI**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **AMIs**.

1. Select the AMI.

1. On the **Details** tab, in the **Watermarks** section, choose **Manage watermarks**.

1. Enter a watermark name and choose **Attach**.

------
#### [ AWS CLI ]

**To attach a watermark to an AMI**  
Use the [attach-image-watermark](https://docs.aws.amazon.com/cli/latest/reference/ec2/attach-image-watermark.html) command.

```
aws ec2 attach-image-watermark \
    --image-id {{ami-1111111111EXAMPLE}} \
    --image-watermark-name "{{prod-baseline}}"
```

The following is example output.

```
{
    "WatermarkKey": "123456789012:prod-baseline"
}
```

------
#### [ PowerShell ]

**To attach a watermark to an AMI**  
Use the [Add-EC2ImageWatermark](https://docs.aws.amazon.com/powershell/latest/reference/items/Add-EC2ImageWatermark.html) cmdlet.

```
Add-EC2ImageWatermark `
    -ImageId {{ami-1111111111EXAMPLE}} `
    -ImageWatermarkName "{{prod-baseline}}"
```

------

You can attach up to 5 watermarks to a single AMI.

## Detach a watermark from an AMI
<a name="ami-watermark-detach"></a>

You can detach a watermark from an AMI by using the console, the AWS CLI, or PowerShell.

------
#### [ Console ]

**To detach a watermark from an AMI**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **AMIs**.

1. Select the AMI.

1. On the **Details** tab, in the **Watermarks** section, choose **Manage watermarks**.

1. Select the watermark to remove, then choose **Remove**.

------
#### [ AWS CLI ]

**To detach a watermark from an AMI**  
Use the [detach-image-watermark](https://docs.aws.amazon.com/cli/latest/reference/ec2/detach-image-watermark.html) command.

```
aws ec2 detach-image-watermark \
    --image-id {{ami-1111111111EXAMPLE}} \
    --image-watermark-key "{{111122223333:prod-baseline}}"
```

------
#### [ PowerShell ]

**To detach a watermark from an AMI**  
Use the [Remove-EC2ImageWatermark](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2ImageWatermark.html) cmdlet.

```
Remove-EC2ImageWatermark `
    -ImageId {{ami-1111111111EXAMPLE}} `
    -ImageWatermarkKey "{{111122223333:prod-baseline}}"
```

------

**Note**  
Detaching a watermark from an AMI does not remove it from derivative AMIs that already carry the watermark. To ensure watermarks remain persistent, grant the `ec2:DetachImageWatermark` permission only to trusted administrators who need to manage watermarks.

## View AMI watermarks
<a name="ami-watermark-view"></a>

You can view watermarks for an AMI by using the console, the AWS CLI, or PowerShell.

------
#### [ Console ]

**To view watermarks for an AMI**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **AMIs**.

1. Select the AMI.

1. View the watermarks in the **Watermarks** section of the **Details** tab.

------
#### [ AWS CLI ]

**To view watermarks for an AMI**  
Use the [describe-images](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html) command.

```
aws ec2 describe-images \
    --image-ids {{ami-046863d776a820ccd}} \
    --region {{us-east-1}}
```

The response includes the `ImageWatermarks` array for each AMI.

```
{
    "Images": [
        {
            "ImageId": "ami-046863d776a820ccd",
            "Public": false,
            "OwnerId": "123456789012",
            ...
            "ImageWatermarks": [
                {
                    "WatermarkKey": "111122223333:prod-baseline",
                    "Region": "us-east-1",
                    "SourceImageId": "ami-0b752bf1df193a6c4",
                    "SourceImageCreationDate": "2024-07-10T08:15:00",
                    "CreationDate": "2024-07-12T14:30:00"
                },
                {
                    "WatermarkKey": "222222222222:security-approved",
                    "Region": "eu-north-1",
                    "SourceImageId": "ami-12345678",
                    "SourceImageCreationDate": "2024-06-01T10:00:00",
                    "CreationDate": "2024-06-05T09:45:00"
                }
            ]
        }
    ]
}
```

------
#### [ PowerShell ]

**To view watermarks for an AMI**  
Use the [Get-EC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2Image.html) cmdlet.

```
(Get-EC2Image -ImageId {{ami-046863d776a820ccd}}).ImageWatermarks
```

------

## Filter AMIs by watermark
<a name="ami-watermark-filter"></a>

You can filter AMIs by watermark by using the console, the AWS CLI, or PowerShell.

------
#### [ Console ]

**To filter AMIs by watermark**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **AMIs**.

1. In the search bar, choose the **Watermark key** filter and enter the watermark key value.

------
#### [ AWS CLI ]

**To filter AMIs by watermark**  
Use the [describe-images](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html) command with the `image-watermark-key` filter.

```
aws ec2 describe-images \
    --filters "Name=image-watermark-key,Values={{111122223333:prod-baseline}}"
```

This returns all AMIs you have access to that carry the specified watermark, including derivative AMIs that inherited it through copy operations.

------
#### [ PowerShell ]

**To filter AMIs by watermark**  
Use the [Get-EC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2Image.html) cmdlet with the `-Filter` parameter.

```
Get-EC2Image `
    -Filter @{Name="image-watermark-key"; Values="{{111122223333:prod-baseline}}"}
```

This returns all AMIs you have access to that carry the specified watermark, including derivative AMIs that inherited it through copy operations.

------