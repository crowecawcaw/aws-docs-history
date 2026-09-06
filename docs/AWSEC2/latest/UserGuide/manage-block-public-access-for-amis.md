

# Manage the block public access setting for AMIs
<a name="manage-block-public-access-for-amis"></a>

You can manage the block public access setting for your AMIs to control whether they can be publicly shared. You can enable, disable, or view the current block public access state for your AMIs using the Amazon EC2 console or the AWS CLI.

## View the block public access state for AMIs
<a name="get-block-public-access-state-for-amis"></a>

To see whether the public sharing of your AMIs is blocked in your account, you can view the state for block public access for AMIs. You must view the state in each AWS Region in which you want to see whether the public sharing of your AMIs is blocked.

**Required permissions**  
To get the current block public access setting for AMIs, you must have the `GetImageBlockPublicAccessState` IAM permission.

------
#### [ Console ]

**To view the block public access state for AMIs in the specified Region**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. From the navigation bar (at the top of the screen), select the Region in which to view the block public access state for AMIs.

1. In the navigation pane, choose **Dashboard**.

1. On the **Account attributes** card, under **Settings**, choose **Data protection and security**.

1. Under **Block public access for AMIs**, check the **Public access** field. The value is either **New public sharing blocked** or **New public sharing allowed**.

------
#### [ AWS CLI ]

**To get the block public access state for AMIs**  
Use the [ get-image-block-public-access-state](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-image-block-public-access-state.html) command. The value is either `block-new-sharing` or `unblocked`.

**Example: For a specific Region**

```
aws ec2 get-image-block-public-access-state --region {{us-east-1}}
```

The `ManagedBy` field indicates the entity that configured the setting. In this example, `account` indicates that the setting was configured directly in the account. A value of `declarative-policy` would mean the setting was configured by a declarative policy. For more information, see [Declarative policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative.html) in the *AWS Organizations User Guide*.

```
{
    "ImageBlockPublicAccessState": "block-new-sharing",
    "ManagedBy": "account"
}
```

**Example: For all Regions in your account**

```
echo -e "Region   \t Public Access State" ; \
echo -e "-------------- \t ----------------------" ; \
for region in $(
    aws ec2 describe-regions \
        --region us-east-1 \
        --query "Regions[*].[RegionName]" \
        --output text
    ); 
    do (output=$(
        aws ec2 get-image-block-public-access-state \
            --region $region \
            --output text)
        echo -e "$region \t $output" 
    );
done
```

The following is example output.

```
Region           Public Access State
--------------   ----------------------
ap-south-1       block-new-sharing
eu-north-1       unblocked
eu-west-3        block-new-sharing
...
```

------
#### [ PowerShell ]

**To get the block public access state for AMIs**  
Use the [Get-EC2ImageBlockPublicAccessState](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2ImageBlockPublicAccessState.html) cmdlet. The value is either `block-new-sharing` or `unblocked`.

**Example: For a specific Region**

```
Get-EC2ImageBlockPublicAccessState -Region {{us-east-1}}
```

The following is example output.

```
block-new-sharing
```

**Example: For all Regions in your account**

```
(Get-EC2Region).RegionName | `
    ForEach-Object {
        [PSCustomObject]@{
            Region   = $_
            PublicAccessState = (Get-EC2ImageBlockPublicAccessState -Region $_)
        }
} | `
Format-Table -AutoSize
```

The following is example output.

```
Region         PublicAccessState
------         -----------------
ap-south-1     block-new-sharing
eu-north-1     block-new-sharing
eu-west-3      block-new-sharing
...
```

------

## Enable block public access for AMIs
<a name="enable-block-public-access-for-amis"></a>

To prevent the public sharing of your AMIs, enable block public access for AMIs at the account level. You must enable block public access for AMIs in each AWS Region in which you want to prevent the public sharing of your AMIs. If you already have public AMIs, they will remain publicly available.

**Required permissions**  
To enable the block public access setting for AMIs, you must have the `EnableImageBlockPublicAccess` IAM permission.

**Considerations**
+ It can take up to 10 minutes to configure this setting. During this time, if you describe the public access state, the response is `unblocked`. When the configuration is completed, the response is `block-new-sharing`.

------
#### [ Console ]

**To enable block public access for AMIs in the specified Region**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. From the navigation bar (at the top of the screen), select the Region in which to enable block public access for AMIs.

1. In the navigation pane, choose **Dashboard**.

1. On the **Account attributes** card, under **Settings**, choose **Data protection and security**.

1. Under **Block public access for AMIs**, choose **Manage**.

1. Select the **Block new public sharing** checkbox, and then choose **Update**.

------
#### [ AWS CLI ]

**To enable block public access for AMIs**  
Use the [enable-image-block-public-access](https://docs.aws.amazon.com/cli/latest/reference/ec2/enable-image-block-public-access.html) command.

**Example: For a specific Region**

```
aws ec2 enable-image-block-public-access \
--region {{us-east-1}} \
--image-block-public-access-state block-new-sharing
```

The following is example output.

```
{ 
    "ImageBlockPublicAccessState": "block-new-sharing"
}
```

**Example: For all Regions in your account**

```
echo -e "Region   \t Public Access State" ; \
echo -e "-------------- \t ----------------------" ; \
for region in $(
    aws ec2 describe-regions \
        --region us-east-1 \
        --query "Regions[*].[RegionName]" \
        --output text
    ); 
    do (output=$(
        aws ec2 enable-image-block-public-access \
            --region $region \
            --image-block-public-access-state block-new-sharing \
            --output text)
        echo -e "$region \t $output" 
    );
done
```

The following is example output.

```
Region           Public Access State
--------------   ----------------------
ap-south-1       block-new-sharing
eu-north-1       block-new-sharing
eu-west-3        block-new-sharing
...
```

------
#### [ PowerShell ]

**To enable block public access for AMIs**  
Use the [Enable-EC2ImageBlockPublicAccess](https://docs.aws.amazon.com/powershell/latest/reference/items/Enable-EC2ImageBlockPublicAccess.html) command.

**Example: For a specific Region**

```
Enable-EC2ImageBlockPublicAccess `
    -Region {{us-east-1}} `
    -ImageBlockPublicAccessState block-new-sharing
```

The following is example output.

```
Value
-----
block-new-sharing
```

**Example: For all Regions in your account**

```
(Get-EC2Region).RegionName | `
    ForEach-Object {
    [PSCustomObject]@{
        Region            = $_
        PublicAccessState = (
        Enable-EC2ImageBlockPublicAccess `
         -Region $_ `
         -ImageBlockPublicAccessState block-new-sharing)
    }
} | `
Format-Table -AutoSize
```

The following is example output.

```
Region         PublicAccessState
------         -----------------
ap-south-1     block-new-sharing
eu-north-1     block-new-sharing
eu-west-3      block-new-sharing
...
```

------

## Disable block public access for AMIs
<a name="disable-block-public-access-for-amis"></a>

To allow the users in your account to publicly share your AMIs, disable block public access at the account level. You must disable block public access for AMIs in each AWS Region in which you want to allow the public sharing of your AMIs.

**Required permissions**  
To disable the block public access setting for AMIs, you must have the `DisableImageBlockPublicAccess` IAM permission.

**Considerations**
+ It can take up to 10 minutes to configure this setting. During this time, if you describe the public access state, the response is `block-new-sharing`. When the configuration is completed, the response is `unblocked`.

------
#### [ Console ]

**To disable block public access for AMIs in the specified Region**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. From the navigation bar (at the top of the screen), select the Region in which to disable block public access for AMIs.

1. In the navigation pane, choose **Dashboard**.

1. On the **Account attributes** card, under **Settings**, choose **Data protection and security**.

1. Under **Block public access for AMIs**, choose **Manage**.

1. Clear the **Block new public sharing** checkbox, and then choose **Update**.

1. Enter **confirm** when prompted for confirmation, and then choose **Allow public sharing**.

------
#### [ AWS CLI ]

**To disable block public access for AMIs**  
Use the [disable-image-block-public-access](https://docs.aws.amazon.com/cli/latest/reference/ec2/disable-image-block-public-access.html) command.

**Example: For a specific Region**

```
aws ec2 disable-image-block-public-access --region {{us-east-1}}
```

The following is example output.

```
{
   "ImageBlockPublicAccessState": "unblocked"
}
```

**Example: For all Regions in your account**

```
echo -e "Region   \t Public Access State" ; \
echo -e "-------------- \t ----------------------" ; \
for region in $(
    aws ec2 describe-regions \
        --region us-east-1 \
        --query "Regions[*].[RegionName]" \
        --output text
    ); 
    do (output=$(
        aws ec2 disable-image-block-public-access \
            --region $region \
            --output text)
        echo -e "$region \t $output" 
    );
done
```

The following is example output.

```
Region           Public Access State
--------------   ----------------------
ap-south-1       unblocked
eu-north-1       unblocked
eu-west-3        unblocked
...
```

------
#### [ PowerShell ]

**To disable block public access for AMIs**  
Use the [Disable-EC2ImageBlockPublicAccess](https://docs.aws.amazon.com/powershell/latest/reference/items/Disable-EC2ImageBlockPublicAccess.html) cmdlet.

**Example: For a specific Region**

```
Disable-EC2ImageBlockPublicAccess -Region {{us-east-1}}
```

The following is example output.

```
Value
-----
unblocked
```

**Example: For all Regions in your account**

```
(Get-EC2Region).RegionName | `
    ForEach-Object {
    [PSCustomObject]@{
        Region            = $_
        PublicAccessState = (Disable-EC2ImageBlockPublicAccess -Region $_)
    }
} | `
Format-Table -AutoSize
```

The following is example output.

```
Region         PublicAccessState
------         -----------------
ap-south-1     unblocked
eu-north-1     unblocked
eu-west-3      unblocked
...
```

------