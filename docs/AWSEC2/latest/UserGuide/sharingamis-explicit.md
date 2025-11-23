# Share an AMI with specific AWS

accounts

You can share an AMI with specific AWS accounts without making the AMI public. All you
need are the AWS account IDs.

An AWS account ID is a 12-digit number, such as `012345678901`, that uniquely
identifies an AWS account. For more information, see [View AWS account
identifiers](../../../accounts/latest/reference/manage-acct-identifiers.md "../../../accounts/latest/reference/manage-acct-identifiers.md") in the _AWS Account Management Reference Guide_.

## Considerations

Consider the following when sharing AMIs with specific AWS accounts.

- **Ownership** – To share an AMI, your AWS account
  must own the AMI.
- **Sharing limits** – For the maximum
  number of entities to which an AMI can be shared within a Region, see the
  [Amazon EC2 service
  quotas](../../../general/latest/gr/ec2-service.md#limits_ec2 "../../../general/latest/gr/ec2-service.md#limits_ec2").
- **Tags** – You can't share user-defined tags (tags
  that you attach to an AMI). When you share an AMI, your user-defined tags
  are not available to any AWS account that the AMI is shared with.
- **Snapshots** –
  You do not need to share the Amazon EBS snapshots that an AMI references in order
  to share the AMI. You can share only the AMI itself; the system provides the
  instance access to the referenced EBS snapshots for the launch. However,
  you must share any KMS keys used to encrypt snapshots that an AMI references.
  For more information, see [Share an Amazon EBS snapshot](../../../ebs/latest/userguide/ebs-modifying-snapshot-permissions.md "../../../ebs/latest/userguide/ebs-modifying-snapshot-permissions.md") in the _Amazon EBS User Guide_.
- **Encryption and keys** – You can share AMIs that are
  backed by unencrypted and encrypted snapshots.
  - The encrypted snapshots must be encrypted with a KMS key. You can’t share AMIs that
    are backed by snapshots that are encrypted with the default AWS
    managed key.
  - If you share an AMI that is backed by encrypted snapshots, you
    must allow the AWS accounts to use the KMS keys that were used
    to encrypt the snapshots. For more
    information, see [Allow organizations and OUs to use a KMS key](allow-org-ou-to-use-key.md "allow-org-ou-to-use-key.md"). To set
    up the key policy that you need to launch Amazon EC2 Auto Scaling instances when you
    use a customer managed key for encryption, see [Required AWS KMS key policy for use with encrypted
    volumes](../../../autoscaling/ec2/userguide/key-policy-requirements-EBS-encryption.md "../../../autoscaling/ec2/userguide/key-policy-requirements-EBS-encryption.md") in the _Amazon EC2 Auto Scaling User Guide_.

- **Region** – AMIs are a Regional resource. When you
  share an AMI, it is only available in that Region. To make an AMI available
  in a different Region, copy the AMI to the Region and then share it. For
  more information, see [Copy an Amazon EC2 AMI](CopyingAMIs.md "CopyingAMIs.md").
- **Usage** – When you share an AMI, users can only
  launch instances from the AMI. They can’t delete, share, or modify it.
  However, after they have launched an instance using your AMI, they can then
  create an AMI from their instance.
- **Copying shared AMIs** – If users in
  another account want to copy a shared AMI, you must grant them read
  permissions for the storage that backs the AMI. For more information, see
  [Cross-account copying](how-ami-copy-works.md#copy-ami-across-accounts "how-ami-copy-works.md#copy-ami-across-accounts").
- **Billing** – You are not billed when your AMI is
  used by other AWS accounts to launch instances. The accounts that launch
  instances using the AMI are billed for the instances that they
  launch.

Console

###### To grant explicit launch permissions

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **AMIs**.
3. Select your AMI in the list, and then choose **Actions**,
   **Edit AMI permissions**.
4. Choose **Private**.
5. Under **Shared accounts**, choose
   **Add account ID**.
6. For **AWS account ID**, enter the AWS account ID with which you
   want to share the AMI, and then choose **Share
   AMI**.

To share this AMI with multiple accounts, repeat Steps 5 and 6
until you have added all the required account IDs. 7. Choose **Save changes** when you are done. 8. (Optional) To view the AWS account IDs with which you have shared the AMI, select
the AMI in the list, and choose the
**Permissions** tab. To find AMIs that are
shared with you, see [Find shared AMIs to use for Amazon EC2 instances](usingsharedamis-finding.md "usingsharedamis-finding.md").

AWS CLI
Use the [modify-image-attribute](../../../cli/latest/reference/ec2/modify-image-attribute.md "../../../cli/latest/reference/ec2/modify-image-attribute.md") command to share an
AMI as shown in the following examples.

###### To grant explicit launch permissions

The following example grants launch permissions for the specified AMI to the specified
AWS account.

```
aws ec2 modify-image-attribute \
    --image-id `ami-0abcdef1234567890` \
    --launch-permission "Add=[{UserId=`123456789012`}]"
```

###### To remove launch permissions for an account

The following example removes launch permissions for the specified AMI from the specified
AWS account.

```
aws ec2 modify-image-attribute \
    --image-id `ami-0abcdef1234567890` \
    --launch-permission "Remove=[{UserId=`123456789012`}]"
```

###### To remove all launch permissions

The following example removes all public and explicit launch permissions from the
specified AMI. Note that the owner of the AMI always has launch permissions and
is therefore unaffected by this command.

```
aws ec2 reset-image-attribute \
    --image-id `ami-0abcdef1234567890` \
    --attribute launchPermission
```

PowerShell
Use the [Edit-EC2ImageAttribute](../../../powershell/latest/reference/items/Edit-EC2ImageAttribute.md "../../../powershell/latest/reference/items/Edit-EC2ImageAttribute.md") command (Tools for Windows PowerShell) to share an
AMI as shown in the following examples.

###### To grant explicit launch permissions

The following example grants launch permissions for the specified AMI to the specified
AWS account.

```
Edit-EC2ImageAttribute `
    -ImageId `ami-0abcdef1234567890` `
    -Attribute launchPermission `
    -OperationType add `
    -UserId "`123456789012`"
```

###### To remove launch permissions for an account

The following example removes launch permissions for the specified AMI from the specified
AWS account.

```
Edit-EC2ImageAttribute `
    -ImageId `ami-0abcdef1234567890` `
    -Attribute launchPermission -OperationType remove `
    -UserId "`123456789012`"
```

###### To remove all launch permissions

The following exaple removes all public and explicit launch permissions from the
specified AMI. Note that the owner of the AMI always has launch permissions and
is therefore unaffected by this command.

```
Reset-EC2ImageAttribute `
    -ImageId `ami-0abcdef1234567890` `
    -Attribute launchPermission
```
