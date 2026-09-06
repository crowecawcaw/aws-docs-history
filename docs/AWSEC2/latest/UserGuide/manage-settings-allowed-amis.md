

# Manage the settings for Allowed AMIs
<a name="manage-settings-allowed-amis"></a>

You can manage the settings for Allowed AMIs. These settings are per Region per account.

**Topics**
+ [Enable Allowed AMIs](#enable-allowed-amis-criteria)
+ [Set the Allowed AMIs criteria](#update-allowed-amis-criteria)
+ [Disable Allowed AMIs](#disable-allowed-amis-criteria)
+ [Get the Allowed AMIs criteria](#identify-allowed-amis-state-and-criteria)
+ [Find AMIs that are allowed](#identify-amis-that-meet-allowed-amis-criteria)
+ [Find instances launched from AMIs that aren't allowed](#identify-instances-with-allowed-AMIs)

## Enable Allowed AMIs
<a name="enable-allowed-amis-criteria"></a>

You can enable Allowed AMIs and specify Allowed AMIs criteria. We recommend that you begin in audit mode, which shows you which AMIs would be affected by the criteria without actually restricting access.

------
#### [ Console ]

**To enable Allowed AMIs**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Dashboard**.

1. On the **Account attributes** card, under **Settings**, choose **Allowed AMIs**.

1. On the **Allowed AMIs** tab, choose **Manage**.

1. For **Allowed AMIs settings**, choose **Audit mode** or **Enabled**. We recommend that you begin in audit mode, test the criteria, and then return to this step to enable Allowed AMIs.

1. (Optional) For **AMI criteria**, enter the criteria in JSON format.

1. Choose **Update**.

------
#### [ AWS CLI ]

**To enable Allowed AMIs**  
Use the [enable-allowed-images-settings](https://docs.aws.amazon.com/cli/latest/reference/ec2/enable-allowed-images-settings.html) command.

```
aws ec2 enable-allowed-images-settings --allowed-images-settings-state enabled
```

To enable audit mode instead, specify `audit-mode` instead of `enabled`.

```
aws ec2 enable-allowed-images-settings --allowed-images-settings-state audit-mode
```

------
#### [ PowerShell ]

**To enable Allowed AMIs**  
Use the [Enable-EC2AllowedImagesSetting](https://docs.aws.amazon.com/powershell/latest/reference/items/Enable-EC2AllowedImagesSetting.html) cmdlet.

```
Enable-EC2AllowedImagesSetting -AllowedImagesSettingsState enabled
```

To enable audit mode instead, specify `audit-mode` instead of `enabled`.

```
Enable-EC2AllowedImagesSetting -AllowedImagesSettingsState audit-mode
```

------

## Set the Allowed AMIs criteria
<a name="update-allowed-amis-criteria"></a>

After you enable Allowed AMIs, you can set or replace the Allowed AMIs criteria.

For the correct configuration and valid values, see [Allowed AMIs configuration](ec2-allowed-amis.md#allowed-amis-json-configuration) and [Allowed AMIs parameters](ec2-allowed-amis.md#allowed-amis-criteria).

------
#### [ Console ]

**To set the Allowed AMIs criteria**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Dashboard**.

1. On the **Account attributes** card, under **Settings**, choose **Allowed AMIs**.

1. On the **Allowed AMIs** tab, choose **Manage**.

1. For **AMI criteria**, enter the criteria in JSON format.

1. Choose **Update**.

------
#### [ AWS CLI ]

**To set the Allowed AMIs criteria**  
Use the [replace-image-criteria-in-allowed-images-settings](https://docs.aws.amazon.com/cli/latest/reference/ec2/replace-image-criteria-in-allowed-images-settings.html) command and specify the JSON file that contains the Allowed AMIs criteria.

```
aws ec2 replace-image-criteria-in-allowed-images-settings --cli-input-json file://{{file_name.json}}
```

------
#### [ PowerShell ]

**To set the Allowed AMIs criteria**  
Use the [Set-EC2ImageCriteriaInAllowedImagesSetting](https://docs.aws.amazon.com/powershell/latest/reference/items/Set-EC2ImageCriteriaInAllowedImagesSetting.html) cmdlet and specify the JSON file that contains the Allowed AMIs criteria.

```
$imageCriteria = Get-Content -Path .\{{file_name.json}} | ConvertFrom-Json
Set-EC2ImageCriteriaInAllowedImagesSetting -ImageCriterion $imageCriteria
```

------

## Disable Allowed AMIs
<a name="disable-allowed-amis-criteria"></a>

You can disable Allowed AMIs as follows.

------
#### [ Console ]

**To disable Allowed AMIs**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Dashboard**.

1. On the **Account attributes** card, under **Settings**, choose **Allowed AMIs**.

1. On the **Allowed AMIs** tab, choose **Manage**.

1. For **Allowed AMIs settings**, choose **Disabled**.

1. Choose **Update**.

------
#### [ AWS CLI ]

**To disable Allowed AMIs**  
Use the [disable-allowed-images-settings](https://docs.aws.amazon.com/cli/latest/reference/ec2/disable-allowed-images-settings.html) command.

```
aws ec2 disable-allowed-images-settings
```

------
#### [ PowerShell ]

**To disable Allowed AMIs**  
Use the [Disable-EC2AllowedImagesSetting](https://docs.aws.amazon.com/powershell/latest/reference/items/Disable-EC2AllowedImagesSetting.html) cmdlet.

```
Disable-EC2AllowedImagesSetting
```

------

## Get the Allowed AMIs criteria
<a name="identify-allowed-amis-state-and-criteria"></a>

You can get the current state of the Allowed AMIs setting and the Allowed AMIs criteria.

------
#### [ Console ]

**To get the Allowed AMIs state and criteria**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Dashboard**.

1. On the **Account attributes** card, under **Settings**, choose **Allowed AMIs**.

1. On the **Allowed AMIs** tab, **Allowed AMIs settings** is set to **Enabled**, **Disabled**, or **Audit mode**.

1. If the state of Allowed AMIs is either **Enabled** or **Audit mode**, **AMI criteria**, displays the AMI criteria in JSON format.

------
#### [ AWS CLI ]

**To get the Allowed AMIs state and criteria**  
Use the [get-allowed-images-settings](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-allowed-images-settings.html) command.

```
aws ec2 get-allowed-images-settings
```

In the following example output, the state is `audit-mode` and the image criteria are set in the account.

```
{
    "State": "audit-mode",
    "ImageCriteria": [
        {
            "MarketplaceProductCodes": [
                "abcdefg1234567890"
            ]
        },
        {
            "ImageProviders": [
                "123456789012",
                "123456789013"
            ],
            "CreationDateCondition": {
                "MaximumDaysSinceCreated": 300
            }
        },
        {
            "ImageProviders": [
                "123456789014"
            ],
            "ImageNames": [
                "golden-ami-*"
            ]
        },
        {
            "ImageProviders": [
                "amazon"
            ],
            "DeprecationTimeCondition": {
                "MaximumDaysSinceDeprecated": 0
            }
        }
    ],
    "ManagedBy": "account"
}
```

------
#### [ PowerShell ]

**To get the Allowed AMIs state and criteria**  
Use the [Get-EC2AllowedImagesSetting](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2AllowedImagesSetting.html) cmdlet.

```
Get-EC2AllowedImagesSetting | Select-Object `
    State, `
    ManagedBy, `
    @{Name='ImageProviders'; Expression={($_.ImageCriteria.ImageProviders)}}, `
    @{Name='MarketplaceProductCodes'; Expression={($_.ImageCriteria.MarketplaceProductCodes)}}, `
    @{Name='ImageNames'; Expression={($_.ImageCriteria.ImageNames)}}, `
    @{Name='MaximumDaysSinceCreated'; Expression={($_.ImageCriteria.CreationDateCondition.MaximumDaysSinceCreated)}}, `
    @{Name='MaximumDaysSinceDeprecated'; Expression={($_.ImageCriteria.DeprecationTimeCondition.MaximumDaysSinceDeprecated)}}
```

In the following example output, the state is `audit-mode` and the image criteria are set in the account.

```
State      : audit-mode
ManagedBy  : account
ImageProviders            : {123456789012, 123456789013, 123456789014, amazon}
MarketplaceProductCodes   : {abcdefg1234567890}
ImageNames                : {golden-ami-*}
MaximumDaysSinceCreated  : 300
MaximumDaysSinceDeprecated: 0
```

------

## Find AMIs that are allowed
<a name="identify-amis-that-meet-allowed-amis-criteria"></a>

You can find the AMIs that are allowed or not allowed by the current Allowed AMIs criteria.

**Note**  
Allowed AMIs must be in audit mode.

------
#### [ Console ]

**To check whether an AMI meets the Allowed AMIs criteria**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **AMIs**.

1. Select the AMI.

1. On the **Details** tab (if you selected the checkbox) or in the summary area (if you selected the AMI ID), find the **Allowed image** field.
   + **Yes** – The AMI meets the Allowed AMIs criteria. This AMI will be available to users in your account after you enable Allowed AMIs.
   + **No** – The AMI does not meet the Allowed AMIs criteria.

1. In the navigation pane, choose **AMI Catalog**.

   An AMI marked **Not allowed** indicates an AMI that does not meet the Allowed AMIs criteria. This AMI won't be visible or available to users in your account when Allowed AMIs is enabled.

------
#### [ AWS CLI ]

**To check whether an AMI meets the Allowed AMIs criteria**  
Use the [describe-images](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html) command.

```
aws ec2 describe-images \
    --image-id {{ami-0abcdef1234567890}} \
    --query Images[].ImageAllowed \
    --output text
```

The following is example output.

```
True
```

**To find AMIs that meet the Allowed AMIs criteria**  
Use the [describe-images](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html) command.

```
aws ec2 describe-images \
    --filters "Name=image-allowed,Values=true" \
    --max-items 10 \
    --query Images[].ImageId
```

The following is example output.

```
ami-000eaaa8be2fd162a
ami-000f82db25e50de8e
ami-000fc21eb34c7a9a6
ami-0010b876f1287d7be
ami-0010b929226fe8eba
ami-0010957836340aead
ami-00112c992a47ba871
ami-00111759e194abcc1
ami-001112565ffcafa5e
ami-0011e45aaee9fba88
```

------
#### [ PowerShell ]

**To check whether an AMI meets the Allowed AMIs criteria**  
Use the [Get-EC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2Image.html) cmdlet.

```
(Get-EC2Image -ImageId {{ami-0abcdef1234567890}}).ImageAllowed
```

The following is example output.

```
True
```

**To find AMIs that meet the Allowed AMIs criteria**  
Use the [Get-EC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2Image.html) cmdlet.

```
Get-EC2Image `
    -Filter @{Name="image-allows";Values="true"} `
    -MaxResult 10 | `
    Select ImageId
```

The following is example output.

```
ami-000eaaa8be2fd162a
ami-000f82db25e50de8e
ami-000fc21eb34c7a9a6
ami-0010b876f1287d7be
ami-0010b929226fe8eba
ami-0010957836340aead
ami-00112c992a47ba871
ami-00111759e194abcc1
ami-001112565ffcafa5e
ami-0011e45aaee9fba88
```

------

## Find instances launched from AMIs that aren't allowed
<a name="identify-instances-with-allowed-AMIs"></a>

You can identify the instances that were launched using an AMI that does not meet the Allowed AMIs criteria.

------
#### [ Console ]

**To check whether an instance was launched using an AMI that isn't allowed**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. Select the instance.

1. On the **Details** tab, under **Instance details**, find **Allowed image**.
   + **Yes** – The AMI meets the Allowed AMIs criteria.
   + **No** – The AMI does not meet the Allowed AMIs criteria.

------
#### [ AWS CLI ]

**To find instances launched using AMIs that aren't allowed**  
Use the [describe-instance-image-metadata](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-image-metadata.html) command with the `image-allowed` filter.

```
aws ec2 describe-instance-image-metadata \
    --filters "Name=image-allowed,Values=false" \
    --query "InstanceImageMetadata[*].[InstanceId,ImageMetadata.ImageId]" \
    --output table
```

The following is example output.

```
--------------------------------------------------
|          DescribeInstanceImageMetadata         |
+----------------------+-------------------------+
|  i-08fd74f3f1595fdbd |  ami-09245d5773578a1d6  |
|  i-0b1bf24fd4f297ab9 |  ami-07cccf2bd80ed467f  |
|  i-026a2eb590b4f7234 |  ami-0c0ec0a3a3a4c34c0  |
|  i-006a6a4e8870c828f |  ami-0a70b9d193ae8a799  |
|  i-0781e91cfeca3179d |  ami-00c257e12d6828491  |
|  i-02b631e2a6ae7c2d9 |  ami-0bfddf4206f1fa7b9  |
+----------------------+-------------------------+
```

------
#### [ PowerShell ]

**To find instances launched using AMIs that aren't allowed**  
Use the [Get-EC2InstanceImageMetadata](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2InstanceImageMetadata.html) cmdlet.

```
Get-EC2InstanceImageMetadata `
    -Filter @{Name="image-allowed";Values="false"} | `
    Select InstanceId, @{Name='ImageId'; Expression={($_.ImageMetadata.ImageId)}}
```

The following is example output.

```
InstanceId          ImageId
----------          -------
i-08fd74f3f1595fdbd ami-09245d5773578a1d6
i-0b1bf24fd4f297ab9 ami-07cccf2bd80ed467f
i-026a2eb590b4f7234 ami-0c0ec0a3a3a4c34c0
i-006a6a4e8870c828f ami-0a70b9d193ae8a799
i-0781e91cfeca3179d ami-00c257e12d6828491
i-02b631e2a6ae7c2d9 ami-0bfddf4206f1fa7b9
```

------
#### [ AWS Config ]

You can add the **ec2-instance-launched-with-allowed-ami** AWS Config rule, configure it for your requirements, and then use it to evaluate your instances.

For more information, see [Adding AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_add-rules.html) and [ec2-instance-launched-with-allowed-ami](https://docs.aws.amazon.com/config/latest/developerguide/ec2-instance-launched-with-allowed-ami.html) in the *AWS Config Developer Guide*.

------