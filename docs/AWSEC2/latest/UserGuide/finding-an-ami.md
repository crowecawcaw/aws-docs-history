# Find an AMI that meets the requirements for your EC2 instance

An AMI includes the components and applications, such as the operating system and type of
root volume, required to launch an instance. To launch an instance, you must find an AMI
that meets your needs.

When selecting an AMI, consider the following requirements you might have for the
instances that you want to launch:

- The AWS Region of the AMI as AMI IDs are unique to each Region.
- The operating system (for example, Linux or Windows).
- The architecture (for example, 32-bit, 64-bit, or
  64-bit ARM).
- The root volume type (for example, Amazon EBS or instance store).
- The provider (for example, Amazon Web Services).
- Additional software (for example, SQL Server).

Console
You can select from the list of AMIs when you use the launch instance wizard,
or you can search all available AMIs using the **Images** page.

###### To find a Quick Start AMI using the launch instance wizard

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. From the navigation bar, select the Region in which to launch your instances.
   You can select any Region that's available to you, regardless of your location.
   AMI IDs are unique to each AWS Region.
3. From the console dashboard, choose **Launch
   instance**.
4. Under **Application and OS Images (Amazon Machine Image)**, choose
   **Quick Start**, choose the operating system (OS) for
   your instance, and then, from **Amazon Machine Image
   (AMI)**, select from one of the commonly used AMIs in the list.
   If you don't see the AMI that you want to use, choose **Browse more
   AMIs** to browse the full AMI catalog. For more information,
   see [Application and OS Images (Amazon Machine Image)](ec2-instance-launch-parameters.md#liw-ami "ec2-instance-launch-parameters.md#liw-ami").

###### To find an AMI using the AMIs page

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. From the navigation bar, select the Region in which to launch your instances.
   You can select any Region that's available to you, regardless of your location.
   AMI IDs are unique to each AWS Region.
3. In the navigation pane, choose **AMIs**.
4. (Optional) Use the filter and search options to scope the list of displayed
   AMIs to see only the AMIs that match your criteria.

For example, to list all AMIs provided by AWS, choose **Public
images**. Then use the search options to further scope the list of
displayed AMIs. Choose the **Search** bar and, from the menu,
choose **Owner alias**, then the **=**
operator, and then the value **amazon**. To find AMIs that
match a specific platform, for example Linux or Windows, choose the
**Search** bar again to choose
**Platform**, then the **=** operator, and
then the operating system from the list provided. 5. (Optional) Choose the **Preferences** icon to select which image
attributes to display, such as the root volume type. Alternatively, you
can select an AMI from the list and view its properties on the
**Details** tab. 6. Before you select an AMI, it's important that you check whether it's backed by
instance store or by Amazon EBS and that you are aware of the effects of this
difference. For more information, see [Root volume type](ComponentsAMIs.md#storage-for-the-root-device "ComponentsAMIs.md#storage-for-the-root-device"). 7. To launch an instance from this AMI, select it and then choose
**Launch instance from image**. For more information about
launching an instance using the console, see [Launch an EC2 instance using the launch
instance wizard in the console](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md"). If you're not ready to launch
the instance now, make note of the AMI ID for later.

AWS CLI
Use the [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md") command to find an AMI that meets your
requirements. By default, this command returns all AMIs that
are public, that you own, and that are shared with you.

###### To find an AMI owned by Amazon

Use the [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md") command with the `--owners`
option.

```
aws ec2 describe-images --owners amazon
```

###### To find a Windows AMI

Add the following filter to display only Windows AMIs.

```
--filters "Name=platform,Values=windows"
```

###### To find an EBS-backed AMI

Add the following filter to display only AMIs backed by Amazon EBS.

```
--filters "Name=root-device-type,Values=ebs"
```

PowerShell
Use the [Get-EC2Image](../../../powershell/latest/reference/items/Get-EC2Image.md "../../../powershell/latest/reference/items/Get-EC2Image.md")
cmdlet to find an AMI that meets your requirements. By default, this cmdlet
returns all AMIs that are public, that you own, or that are shared with you.

###### To find an AMI owned by Amazon

Use the [Get-EC2Image](../../../powershell/latest/reference/items/Get-EC2Image.md "../../../powershell/latest/reference/items/Get-EC2Image.md") command with the `-Owner`
parameter.

```
Get-EC2Image -Owner amazon
```

###### To find a Windows AMI

Add the following filter to display only Windows AMIs.

```
-Filter @{Name="platform"; Values="windows"}
```

For additional examples, see [Find an Amazon Machine Image Using
Windows PowerShell](../../../powershell/latest/userguide/pstools-ec2-get-amis.md "../../../powershell/latest/userguide/pstools-ec2-get-amis.md") in the _AWS Tools for PowerShell User Guide_.

###### Related resources

For more information about AMIs for a specific operating system, see the
following:

- Amazon Linux 2023 – [AL2023 on Amazon EC2](../../../linux/al2023/ug/ec2.md "../../../linux/al2023/ug/ec2.md") in the
  _Amazon Linux 2023 User Guide_
- Ubuntu – [Amazon EC2 AMI Locator](https://cloud-images.ubuntu.com/locator/ec2/ "https://cloud-images.ubuntu.com/locator/ec2/") on the _Canonical Ubuntu
  website_
- RHEL – [Red Hat
  Enterprise Linux Images (AMI) Available on Amazon Web Services (AWS)](https://access.redhat.com/solutions/15356 "https://access.redhat.com/solutions/15356") on
  the Red Hat website
- Windows Server – [AWS Windows AMI
  reference](../../../ec2/latest/windows-ami-reference/windows-amis.md "../../../ec2/latest/windows-ami-reference/windows-amis.md")
  For information about AMIs that you can subscribe to on the AWS Marketplace see
  [Paid AMIs in the AWS Marketplace for Amazon EC2 instances](paid-amis.md "paid-amis.md").

For information about using Systems Manager to help your users find the latest AMI that they should
use when launching an instance, see the following:

- [Reference AMIs using Systems Manager parameters](using-systems-manager-parameter-to-find-AMI.md "using-systems-manager-parameter-to-find-AMI.md")
- [Reference the latest AMIs using Systems Manager public parameters](finding-an-ami-parameter-store.md "finding-an-ami-parameter-store.md")
