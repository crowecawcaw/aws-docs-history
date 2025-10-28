# Find shared AMIs to use for Amazon EC2 instances

You can use the Amazon EC2 console or the command line to find public or private shared
AMIs to use with your Amazon EC2 instances.

AMIs are a Regional resource. When you search for a shared AMI (public or private),
you must search for it from the same Region from which it is shared. To make an AMI
available in a different Region, copy the AMI to the Region, and then share it. For more
information, see [Copy an Amazon EC2 AMI](CopyingAMIs.md "CopyingAMIs.md").

Console
The console provides an AMI filter field. You can also scope your searches using the
filters provided in the **Search** field.

###### To find a shared or AMI

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **AMIs**.
3. In the first filter, choose one of the following options:
   - **Private images** – Lists all AMIs that are
     shared with you.
   - **Public images** – Lists all public AMIs.

4. (Optional) To display only the public images from Amazon, choose the
   **Search** field and then, from the menu options,
   choose **Owner alias**, then **=**,
   and then **amazon**.
5. (Optional) Add filters to scope your search to AMIs that meet
   your requirements.

###### To find a shared public AMI from a [verified

provider](sharing-amis.md#verified-ami-provider "sharing-amis.md#verified-ami-provider")

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **AMI Catalog**.
3. Choose **Community AMIs**.
4. In the **Refine results** pane, select
   **Verified provider**. The **Verified provider**
   label indicates that the AMIs are from Amazon or a verified partner.

AWS CLI
Use the [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md") command
to list AMIs. You can scope the list to the types of AMIs that interest you,
as shown in the following examples.

###### To list all public AMIs

The following command lists all public AMIs, including any public AMIs that you own.

```
aws ec2 describe-images --executable-users all
```

###### To list AMIs with explicit launch permissions

The following command lists the AMIs for which you have explicit launch
permissions. This list does not include any AMIs that you own.

```
aws ec2 describe-images --executable-users self
```

###### To list AMIs owned by verified providers

The following command lists the AMIs owned by [verified providers](sharing-amis.md#verified-ami-provider "sharing-amis.md#verified-ami-provider"). Public AMIs owned by verified providers
(either Amazon or verified partners) have an aliased owner, which
appears as `amazon`, `aws-backup-vault`, or
`aws-marketplace` in the account field. This helps you to
easily find AMIs from verified providers. Other users can't alias their
AMIs.

```
aws ec2 describe-images \
    --owners amazon aws-marketplace \
    --query 'Images[*].[ImageId]' \
    --output text
```

###### To list AMIs owned by an account

The following command lists the AMIs owned by the specified AWS account.

```
aws ec2 describe-images --owners `123456789012`
```

###### To scope AMIs using a filter

To reduce the number of displayed AMIs, use a filter to list only the types of
AMIs that interest you. For example, use the following filter to display only
EBS-backed AMIs.

```
--filters "Name=root-device-type,Values=ebs"
```

PowerShell
Use the [Get-EC2Image](../../../powershell/latest/reference/items/Get-EC2Image.md "../../../powershell/latest/reference/items/Get-EC2Image.md") cmdlet
(Tools for Windows PowerShell) to list AMIs. You can scope the list to the types of AMIs that interest you,
as shown in the following examples.

###### To list all public AMIs

The following command lists all public AMIs, including any public AMIs that you own.

```
Get-EC2Image -ExecutableUser all
```

###### To list AMIs with explicit launch permissions

The following command lists the AMIs for which you have explicit launch
permissions. This list does not include any AMIs that you own.

```
Get-EC2Image -ExecutableUser self
```

###### To list AMIs owned by verified providers

The following command lists the AMIs owned by [verified providers](sharing-amis.md#verified-ami-provider "sharing-amis.md#verified-ami-provider"). Public AMIs owned by verified providers
(either Amazon or verified partners) have an aliased owner, which
appears as `amazon`, `aws-backup-vault`, or
`aws-marketplace` in the account field. This helps you to
easily find AMIs from verified providers. Other users can't alias their
AMIs.

```
Get-EC2Image -Owner amazon aws-marketplace
```

###### To list AMIs owned by an account

The following command lists the AMIs owned by the specified AWS account.

```
Get-EC2Image -Owner `123456789012`
```

###### To scope AMIs using a filter

To reduce the number of displayed AMIs, use a filter to list only the types of
AMIs that interest you. For example, use the following filter to display only
EBS-backed AMIs.

```
-Filter @{Name="root-device-type"; Values="ebs"}
```
