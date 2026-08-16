# Tagging your directory

Tags are key-value pairs that you can assign to your Directory Service directories to help you organize
and manage your resources. You can use tags to categorize directories by purpose, environment,
cost allocation, and other criteria. Each tag consists of a required tag key and an optional tag value. Tag keys
must be unique for each directory.

For more information about tagging strategies, see [Tagging
best practices](../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md "../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md").

You can run the following commands from
[AWS CloudShell](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md"), which comes with
the [AWS CLI](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md") and
[AWS Tools for PowerShell](../../../powershell/latest/userguide/pstools-welcome.md "../../../powershell/latest/userguide/pstools-welcome.md") pre-installed. AWS CloudShell automatically
configures your credentials.

1. Sign in to the AWS Management Console.
2. Open [AWS CloudShell](https://console.aws.amazon.com/cloudshell/home "https://console.aws.amazon.com/cloudshell/home").
   Run `pwsh` to use the PowerShell commands.

## Add tags to your directory

You can add tags to your directory using the AWS CLI or PowerShell:

AWS CLI

###### To add tags to your directory with the AWS CLI

- Run the following command, replacing the directory ID and
  tag values with your own:

```
aws ds add-tags-to-resource \
  --resource-id `d-1234567890` \
  --tags Key=`MyTagName1`,Value=`MyTagValue1` \
         Key=`MyTagName2`,Value=`MyTagValue2`
```

For more information, see [`add-tags-to-resource`](../../../cli/latest/reference/ds/add-tags-to-resource.md "../../../cli/latest/reference/ds/add-tags-to-resource.md").

PowerShell

###### To add tags to your directory with PowerShell

- Run the following command, replacing the directory
  ID and tag values with your own:

```
Add-DSResourceTag `
  -ResourceId `d-1234567890` `
  -Tag @{Key="`MyTagName1`"; Value="`MyTagValue1`"}, `
       @{Key="`MyTagName2`"; Value="`MyTagValue2`"}
```

For more information, see [`Add-DSResourceTag`](../../../powershell/latest/reference/items/Add-DSResourceTag.md "../../../powershell/latest/reference/items/Add-DSResourceTag.md").

## List tags on your directory

You can list existing tags on your directory using the AWS CLI or PowerShell:

AWS CLI

###### To list tags on your directory with the AWS CLI

- Run the following command, replacing the directory ID with
  your own:

```
aws ds list-tags-for-resource \
  --resource-id `d-1234567890`
```

For more information, see [`list-tags-for-resource`](../../../cli/latest/reference/ds/list-tags-for-resource.md "../../../cli/latest/reference/ds/list-tags-for-resource.md").

PowerShell

###### To list tags on your directory with PowerShell

- Run the following command, replacing the directory
  ID with your own:

```
Get-DSResourceTag `
  -ResourceId `d-1234567890`
```

For more information, see [`Get-DSResourceTag`](../../../powershell/latest/reference/items/Get-DSResourceTag.md "../../../powershell/latest/reference/items/Get-DSResourceTag.md").

## Update a tag on your directory

To update the value of an existing tag, use the same add command with the existing key
name and a new value. This overwrites the previous value.

AWS CLI

###### To update a tag on your directory with the AWS CLI

- Run the following command, replacing the directory ID, tag
  key, and new value with your own:

```
aws ds add-tags-to-resource \
  --resource-id `d-1234567890` \
  --tags Key=`MyTagName1`,Value=`MyNewTagValue1`
```

For more information, see [`add-tags-to-resource`](../../../cli/latest/reference/ds/add-tags-to-resource.md "../../../cli/latest/reference/ds/add-tags-to-resource.md").

PowerShell

###### To update a tag on your directory with PowerShell

- Run the following command, replacing the directory
  ID, tag key, and new value with your own:

```
Add-DSResourceTag `
  -ResourceId `d-1234567890` `
  -Tag @{Key="`MyTagName1`"; Value="`MyNewTagValue1`"}
```

For more information, see [`Add-DSResourceTag`](../../../powershell/latest/reference/items/Add-DSResourceTag.md "../../../powershell/latest/reference/items/Add-DSResourceTag.md").

## Remove tags from your directory

You can remove tags from your directory using the AWS CLI or PowerShell:

AWS CLI

###### To remove tags from your directory with the AWS CLI

- Run the following command, replacing the directory ID and tag
  key names with your own:

```
aws ds remove-tags-from-resource \
  --resource-id `d-1234567890` \
  --tag-keys `MyTagName1` `MyTagName2`
```

For more information, see [`remove-tags-from-resource`](../../../cli/latest/reference/ds/remove-tags-from-resource.md "../../../cli/latest/reference/ds/remove-tags-from-resource.md").

PowerShell

###### To remove tags from your directory with PowerShell

- Run the following command, replacing the directory
  ID and tag key names with your own:

```
Remove-DSResourceTag `
  -ResourceId `d-1234567890` `
  -TagKey "`MyTagName1`", `
          "`MyTagName2`" `
  -Force
```

For more information, see [`Remove-DSResourceTag`](../../../powershell/latest/reference/items/Remove-DSResourceTag.md "../../../powershell/latest/reference/items/Remove-DSResourceTag.md").
