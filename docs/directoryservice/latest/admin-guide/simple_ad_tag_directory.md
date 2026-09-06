

# Tagging your directory
<a name="simple_ad_tag_directory"></a>

Tags are key-value pairs that you can assign to your Directory Service directories to help you organize and manage your resources. You can use tags to categorize directories by purpose, environment, cost allocation, and other criteria. Each tag consists of a required tag key and an optional tag value. Tag keys must be unique for each directory.

For more information about tagging strategies, see [Tagging best practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html).

You can run the following commands from [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html), which comes with the AWS CLI, PowerShell, and [AWS.Tools for PowerShell](https://aws.amazon.com/powershell/) pre-installed, and credentials are automatically configured.

1. Sign in to the AWS Management Console.

1. Open [AWS CloudShell](https://console.aws.amazon.com/cloudshell/home). Run `pwsh` to use the PowerShell commands.

## Add tags to your directory
<a name="simple_ad_tag_directory_add"></a>

You can add tags to your directory using the AWS CLI or PowerShell:

------
#### [ AWS CLI ]

**To add tags to your directory with the AWS CLI**
+ Open the AWS CLI. Run the following command, replacing the directory ID and tag values with your own:

  ```
  aws ds add-tags-to-resource \
    --resource-id {{d-1234567890}} \
    --tags Key={{MyTagName1}},Value={{MyTagValue1}} \
           Key={{MyTagName2}},Value={{MyTagValue2}}
  ```

  For more information, see [`add-tags-to-resource`](https://docs.aws.amazon.com/cli/latest/reference/ds/add-tags-to-resource.html).

------
#### [ PowerShell ]

**To add tags to your directory with PowerShell**
+ Open PowerShell. Run the following command, replacing the directory ID and tag values with your own:

  ```
  Add-DSResourceTag `
    -ResourceId {{d-1234567890}} `
    -Tag @{Key="{{MyTagName1}}"; Value="{{MyTagValue1}}"}, `
         @{Key="{{MyTagName2}}"; Value="{{MyTagValue2}}"}
  ```

  For more information, see [`Add-DSResourceTag`](https://docs.aws.amazon.com/powershell/latest/reference/items/Add-DSResourceTag.html).

------

## List tags on your directory
<a name="simple_ad_tag_directory_list"></a>

You can list existing tags on your directory using the AWS CLI or PowerShell:

------
#### [ AWS CLI ]

**To list tags on your directory with the AWS CLI**
+ Open the AWS CLI. Run the following command, replacing the directory ID with your own:

  ```
  aws ds list-tags-for-resource \
    --resource-id {{d-1234567890}}
  ```

  For more information, see [`list-tags-for-resource`](https://docs.aws.amazon.com/cli/latest/reference/ds/list-tags-for-resource.html).

------
#### [ PowerShell ]

**To list tags on your directory with PowerShell**
+ Open PowerShell. Run the following command, replacing the directory ID with your own:

  ```
  Get-DSResourceTag `
    -ResourceId {{d-1234567890}}
  ```

  For more information, see [`Get-DSResourceTag`](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-DSResourceTag.html).

------

## Update a tag on your directory
<a name="simple_ad_tag_directory_update"></a>

To update the value of an existing tag, use the same add command with the existing key name and a new value. This overwrites the previous value.

------
#### [ AWS CLI ]

**To update a tag on your directory with the AWS CLI**
+ Open the AWS CLI. Run the following command, replacing the directory ID, tag key, and new value with your own:

  ```
  aws ds add-tags-to-resource \
    --resource-id {{d-1234567890}} \
    --tags Key={{MyTagName1}},Value={{MyNewTagValue1}}
  ```

  For more information, see [`add-tags-to-resource`](https://docs.aws.amazon.com/cli/latest/reference/ds/add-tags-to-resource.html).

------
#### [ PowerShell ]

**To update a tag on your directory with PowerShell**
+ Open PowerShell. Run the following command, replacing the directory ID, tag key, and new value with your own:

  ```
  Add-DSResourceTag `
    -ResourceId {{d-1234567890}} `
    -Tag @{Key="{{MyTagName1}}"; Value="{{MyNewTagValue1}}"}
  ```

  For more information, see [`Add-DSResourceTag`](https://docs.aws.amazon.com/powershell/latest/reference/items/Add-DSResourceTag.html).

------

## Remove tags from your directory
<a name="simple_ad_tag_directory_remove"></a>

You can remove tags from your directory using the AWS CLI or PowerShell:

------
#### [ AWS CLI ]

**To remove tags from your directory with the AWS CLI**
+ Open the AWS CLI. Run the following command, replacing the directory ID and tag key names with your own:

  ```
  aws ds remove-tags-from-resource \
    --resource-id {{d-1234567890}} \
    --tag-keys {{MyTagName1}} {{MyTagName2}}
  ```

  For more information, see [`remove-tags-from-resource`](https://docs.aws.amazon.com/cli/latest/reference/ds/remove-tags-from-resource.html).

------
#### [ PowerShell ]

**To remove tags from your directory with PowerShell**
+ Open PowerShell. Run the following command, replacing the directory ID and tag key names with your own:

  ```
  Remove-DSResourceTag `
    -ResourceId {{d-1234567890}} `
    -TagKey "{{MyTagName1}}", `
            "{{MyTagName2}}" `
    -Force
  ```

  For more information, see [`Remove-DSResourceTag`](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-DSResourceTag.html).

------