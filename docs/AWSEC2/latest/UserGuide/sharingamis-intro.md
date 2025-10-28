# Make your AMI publicly available for use in Amazon EC2

You can make your AMI publicly available by sharing it with all AWS accounts.

If you want to prevent the public sharing of your AMIs, you can enable _block public access for AMIs_. This blocks any attempts to
make an AMI public, helping to prevent unauthorized access and potential misuse of AMI
data. Note that enabling block public access does not affect your AMIs that are already
publicly available; they remain publicly available. For more information, see [Understand block public access for AMIs](block-public-access-to-amis.md "block-public-access-to-amis.md").

To allow only specific accounts to use your AMI to launch instances, see [Share an AMI with specific AWS
accounts](sharingamis-explicit.md "sharingamis-explicit.md").

###### Contents

- [Considerations](#considerations-for-sharing-public-AMIs "#considerations-for-sharing-public-AMIs")
- [Share an AMI with all AWS accounts
  (share publicly)](#share-an-ami-publicly "#share-an-ami-publicly")

## Considerations

Consider the following before making an AMI public.

- **Ownership** – To make an AMI public,
  your AWS account must own the AMI.
- **Region** – AMIs are a Regional
  resource. When you share an AMI, it is available only in the Region from
  which you shared it. To make an AMI available in a different Region, copy
  the AMI to the Region and then share it. For more information, see [Copy an Amazon EC2 AMI](CopyingAMIs.md "CopyingAMIs.md").
- **Block public access** – To publicly share an AMI,
  [block public access for AMIs](block-public-access-to-amis.md "block-public-access-to-amis.md") must be disabled in each
  Region in which the AMI will be publicly shared. After you've publicly
  shared the AMI, you can re-enable block public access for AMIs to prevent
  further public sharing of your AMIs.
- **Some AMIs can't be made public** – If your AMI
  includes one of the following components, you can't make it public (but you
  can [share the AMI with specific
  AWS accounts](sharingamis-explicit.md "sharingamis-explicit.md")):
  - Encrypted volumes
  - Snapshots of encrypted volumes
  - Product codes

- **Avoid exposing sensitive data** – To
  avoid exposing sensitive data when you share an AMI, read the security
  considerations in [Recommendations for creating shared Linux AMIs](building-shared-amis.md "building-shared-amis.md") and follow the recommended
  actions.
- **Usage** – When you share an AMI,
  users can only launch instances from the AMI. They can’t delete, share, or
  modify it. However, after they have launched an instance using your AMI,
  they can then create an AMI from the instance they launched.
- **Automatic deprecation** – By default, the
  deprecation date of all public AMIs is set to two years from the AMI
  creation date. You can set the deprecation date to earlier than two years.
  To cancel the deprecation date, or to move the deprecation to a later date,
  you must make the AMI private by only [sharing it with specific AWS accounts](sharingamis-explicit.md "sharingamis-explicit.md").
- **Remove obsolete AMIs** – After a public AMI reaches
  its deprecation date, if no new instances were launched from the AMI for six
  or more months, AWS eventually removes the public sharing property so that
  obsolete AMIs don’t appear in the public AMI lists.
- **Billing** – You are not billed when your AMI is
  used by other AWS accounts to launch instances. The accounts that launch
  instances using the AMI are billed for the instances that they
  launch.

## Share an AMI with all AWS accounts

(share publicly)

After you make an AMI public, it is available in **Community AMIs** in the
console, which you can access from the **AMI Catalog** in the left
navigator in the EC2 console or when launching an instance using the console. Note
that it can take a short while for an AMI to appear in **Community
AMIs** after you make it public.

Console

###### To make an AMI public

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **AMIs**.
3. Select your AMI from the list, and then choose
   **Actions**, **Edit AMI
   permissions**.
4. Under **AMI availability**, choose
   **Public**.
5. Choose **Save changes**.

AWS CLI
Each AMI has a `launchPermission` property that controls which AWS accounts,
besides the owner's, are allowed to use that AMI to launch instances. By modifying
the `launchPermission` property of an AMI, you can make the AMI public
(which grants launch permissions to all AWS accounts), or share it with only the
AWS accounts that you specify.

You can add or remove account IDs from the list of accounts that have launch
permissions for an AMI. To make the AMI public, specify the `all` group.
You can specify both public and explicit launch permissions.

###### To make an AMI public

1. Use the [modify-image-attribute](../../../cli/latest/reference/ec2/modify-image-attribute.md "../../../cli/latest/reference/ec2/modify-image-attribute.md") command as follows to
   add the `all` group to the `launchPermission` list for
   the specified AMI.

```
aws ec2 modify-image-attribute \
    --image-id `ami-0abcdef1234567890` \
    --launch-permission "Add=[{Group=all}]"
```

2. To verify the launch permissions of the AMI, use the [describe-image-attribute](../../../cli/latest/reference/ec2/describe-image-attribute.md "../../../cli/latest/reference/ec2/describe-image-attribute.md") command.

```
aws ec2 describe-image-attribute \
    --image-id `ami-0abcdef1234567890` \
    --attribute launchPermission
```

3. (Optional) To make the AMI private again, remove the `all`
   group from its launch permissions. Note that the owner of the AMI always has
   launch permissions and is therefore unaffected by this command.

```
aws ec2 modify-image-attribute \
    --image-id `ami-0abcdef1234567890` \
    --launch-permission "Remove=[{Group=all}]"
```

PowerShell
Each AMI has a `launchPermission` property that controls which AWS accounts,
besides the owner's, are allowed to use that AMI to launch instances. By modifying
the `launchPermission` property of an AMI, you can make the AMI public
(which grants launch permissions to all AWS accounts), or share it with only the
AWS accounts that you specify.

You can add or remove account IDs from the list of accounts that have launch
permissions for an AMI. To make the AMI public, specify the `all` group.
You can specify both public and explicit launch permissions.

###### To make an AMI public

1. Use the [Edit-EC2ImageAttribute](../../../powershell/latest/reference/items/Edit-EC2ImageAttribute.md "../../../powershell/latest/reference/items/Edit-EC2ImageAttribute.md") command as follows to
   add the `all` group to the `launchPermission` list for
   the specified AMI.

```
Edit-EC2ImageAttribute `
    -ImageId `ami-0abcdef1234567890` `
    -Attribute launchPermission `
    -OperationType add `
    -UserGroup all
```

2. To verify the launch permissions of the AMI, use the following [Get-EC2ImageAttribute](../../../powershell/latest/reference/items/Get-EC2ImageAttribute.md "../../../powershell/latest/reference/items/Get-EC2ImageAttribute.md") command.

```
Get-EC2ImageAttribute `
    -ImageId `ami-0abcdef1234567890` `
    -Attribute launchPermission
```

3. (Optional) To make the AMI private again, remove the `all`
   group from its launch permissions. Note that the owner of the AMI always has
   launch permissions and is therefore unaffected by this command.

```
Edit-EC2ImageAttribute `
    -ImageId `ami-0abcdef1234567890` `
    -Attribute launchPermission `
    -OperationType remove `
    -UserGroup all
```
