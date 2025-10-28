# Manage AMI sharing with an organization or OU

You can manage AMI sharing with organizations and organization units (OU) to control whether
they can launch Amazon EC2 instances.

## View the organizations and OUs with which an

AMI is shared

You can find the organizations and OUs with which you've shared your AMI.

Console

###### To check with which organizations and OUs you've shared your AMI

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **AMIs**.
3. Select your AMI in the list, choose the **Permissions** tab, and scroll
   down to **Shared organizations/OUs**.

To find AMIs that are shared with you, see [Find shared AMIs to use for Amazon EC2 instances](usingsharedamis-finding.md "usingsharedamis-finding.md").

AWS CLI

###### To check with which organizations and OUs you've shared your AMI

Use the [describe-image-attribute](../../../cli/latest/reference/ec2/describe-image-attribute.md "../../../cli/latest/reference/ec2/describe-image-attribute.md") command with
the `launchPermission` attribute.

```
aws ec2 describe-image-attribute \
    --image-id `ami-0abcdef1234567890` \
    --attribute launchPermission
```

The following is an example response.

```
{
    "ImageId": "ami-0abcdef1234567890",
    "LaunchPermissions": [
        {
            "OrganizationalUnitArn": "arn:aws:organizations::111122223333:ou/o-123example/ou-1234-5example"
        }
    ]
}
```

PowerShell

###### To check with which organizations and OUs you've shared your AMI

Use the [Get-EC2ImageAttribute](../../../powershell/latest/reference/items/Get-EC2ImageAttribute.md "../../../powershell/latest/reference/items/Get-EC2ImageAttribute.md") cmdlet.

```
Get-EC2ImageAttribute `
    -ImageId `ami-0abcdef1234567890` `
    -Attribute launchPermission
```

## Share an AMI with an organization or OU

You can share an AMI with an organization or OU.

###### Note

You do not need to share the Amazon EBS snapshots that an AMI references in order to share the
AMI. Only the AMI itself needs to be shared, and the system automatically
provides the instance with access to the referenced EBS snapshots for the
launch. However, you do need to share the KMS keys used to encrypt snapshots
that the AMI references. For more information, see [Allow organizations and OUs to use a KMS key](allow-org-ou-to-use-key.md "allow-org-ou-to-use-key.md").

Console

###### To share an AMI with an organization or an OU

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **AMIs**.
3. Select your AMI in the list, and then choose **Actions**, **Edit
   AMI permissions**.
4. Under **AMI availability**, choose
   **Private**.
5. Next to **Shared organizations/OUs**, choose
   **Add organization/OU ARN**.
6. For **Organization/OU ARN**, enter the organization ARN or OU ARN with
   which you want to share the AMI, and then choose **Share
   AMI**. Note that you must specify the full ARN, not
   just the ID.

To share this AMI with multiple organizations or OUs, repeat this step until you have
added all of the required organizations or OUs. 7. Choose **Save changes** when you're done. 8. (Optional) To view the organizations or OUs with which you have shared the AMI, select
the AMI in the list, choose the **Permissions** tab,
and scroll down to **Shared organizations/OUs**. To
find AMIs that are shared with you, see [Find shared AMIs to use for Amazon EC2 instances](usingsharedamis-finding.md "usingsharedamis-finding.md").

AWS CLI

###### To share an AMI with an organization

Use the [modify-image-attribute](../../../cli/latest/reference/ec2/modify-image-attribute.md "../../../cli/latest/reference/ec2/modify-image-attribute.md") command to grant launch
permissions for the specified AMI to the specified organization.

```
aws ec2 modify-image-attribute \
    --image-id `ami-0abcdef1234567890` \
    --launch-permission "Add=[{OrganizationArn=arn:aws:organizations::`123456789012`:organization/`o-123example`}]"
```

###### To share an AMI with an OU

The [modify-image-attribute](../../../cli/latest/reference/ec2/modify-image-attribute.md "../../../cli/latest/reference/ec2/modify-image-attribute.md") command grants launch permissions for the
specified AMI to the specified OU. Note that you must specify the full ARN, not
just the ID.

```
aws ec2 modify-image-attribute \
    --image-id `ami-0abcdef1234567890` \
    --launch-permission "Add=[{OrganizationalUnitArn=arn:aws:organizations::`123456789012`:ou/`o-123example`/`ou-1234-5example`}]"
```

PowerShell
Use the [Edit-EC2ImageAttribute](../../../powershell/latest/reference/items/Edit-EC2ImageAttribute.md "../../../powershell/latest/reference/items/Edit-EC2ImageAttribute.md") command (Tools for Windows PowerShell) to share
an AMI as shown in the following examples.

###### To share an AMI with an organization or an OU

The following command grants launch permissions for the specified AMI to the specified
organization.

```
Edit-EC2ImageAttribute `
    -ImageId `ami-0abcdef1234567890` `
    -Attribute launchPermission `
    -OperationType add `
    -OrganizationArn "arn:aws:organizations::`123456789012`:organization/`o-123example`"
```

###### To stop sharing an AMI with an organization or OU

The following command removes launch permissions for the specified AMI from the specified
organization:

```
Edit-EC2ImageAttribute `
    -ImageId `ami-0abcdef1234567890` `
    -Attribute launchPermission `
    -OperationType remove `
    -OrganizationArn "arn:aws:organizations::`123456789012`:organization/`o-123example`"
```

###### To stop sharing an AMI with all organizations, OUs, and AWS accounts

The following command removes all public and explicit launch permissions from
the specified AMI. Note that the owner of the AMI always has launch permissions
and is therefore unaffected by this command.

```
Reset-EC2ImageAttribute `
    -ImageId `ami-0abcdef1234567890` `
    -Attribute launchPermission
```

## Stop sharing an AMI with an organization or OU

You can stop sharing an AMI with an organization or OU.

###### Note

You can't stop sharing an AMI with a specific account if it's in an organization or OU
with which an AMI is shared. If you try to stop sharing the AMI by removing
launch permissions for the account, Amazon EC2 returns a success message. However,
the AMI continues to be shared with the account.

Console

###### To stop sharing an AMI with an organization or OU

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **AMIs**.
3. Select your AMI in the list, and then choose **Actions**, **Edit
   AMI permissions**.
4. Under **Shared organizations/OUs**, select the organizations or OUs with which you want to stop sharing the AMI, and then choose
   **Remove selected**.
5. Choose **Save changes** when you're done.
6. (Optional) To confirm that you have stopped sharing the AMI with the organizations or
   OUs, select the AMI in the list, choose the
   **Permissions** tab, and scroll down to
   **Shared organizations/OUs**.

AWS CLI

###### To stop sharing an AMI with an organization or OU

Use the [modify-image-attribute](../../../cli/latest/reference/ec2/modify-image-attribute.md "../../../cli/latest/reference/ec2/modify-image-attribute.md") command. This example removes launch
permissions for the specified AMI from the specified organization.

```
aws ec2 modify-image-attribute \
    --image-id `ami-0abcdef1234567890` \
    --launch-permission "Remove=[{OrganizationArn=arn:aws:organizations::`123456789012`:organization/`o-123example`}]"
```

###### To stop sharing an AMI with all organizations, OUs, and AWS accounts

Use the [reset-image-attribute](../../../cli/latest/reference/ec2/reset-image-attribute.md "../../../cli/latest/reference/ec2/reset-image-attribute.md") command. This example removes all
public and explicit launch permissions from the specified AMI. Note that the
owner of the AMI always has launch permissions and is therefore unaffected
by this command.

```
aws ec2 reset-image-attribute \
    --image-id `ami-0abcdef1234567890` \
    --attribute launchPermission
```

PowerShell

###### To stop sharing an AMI with an organization or OU

Use the [Edit-EC2ImageAttribute](../../../powershell/latest/reference/items/Edit-EC2ImageAttribute.md "../../../powershell/latest/reference/items/Edit-EC2ImageAttribute.md")
cmdlet. This example removes launch permissions for the specified
AMI from the specified organization.

```
Edit-EC2ImageAttribute `
    -ImageId `ami-0abcdef1234567890` `
    -Attribute launchPermission `
    -OperationType remove `
    -OrganizationArn "arn:aws:organizations::`123456789012`:organization/`o-123example`"
```

###### To stop sharing an AMI with all organizations, OUs, and AWS accounts

Use the [Reset-EC2ImageAttribute](../../../powershell/latest/reference/items/Reset-EC2ImageAttribute.md "../../../powershell/latest/reference/items/Reset-EC2ImageAttribute.md")
cmdlet. This example removes all public and explicit launch permissions from
the specified AMI. Note that the owner of the AMI always has launch
permissions and is therefore unaffected by this command.

```
Reset-EC2ImageAttribute `
    -ImageId `ami-0abcdef1234567890` `
    -Attribute LaunchPermission
```
