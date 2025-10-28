# How Amazon creates AWS Windows AMIs

The following content is a high level overview of the process Amazon uses to create AWS Windows AMIs.
Details include what you can expect from an official AWS Windows AMI, as
well as the standards that Amazon uses to validate AMI security and reliability.

## Where AWS gets the Windows Server installation media

When a new version of Windows Server is released, we download the Windows ISO
from Microsoft and validate the hash Microsoft publishes. An initial AMI is then
created from the Windows distribution ISO. The drivers needed to boot on EC2 are
included in addition to our EC2 launch agent. To prepare this initial AMI for
public release, we perform automated processes to convert the ISO to an AMI.
This prepared AMI is used for the monthly automated update and release
process.

## What to expect from an official

AWS Windows AMI

Amazon provides AWS Windows AMIs with a variety of configurations for popular versions
of Microsoft supported Windows Server Operating Systems. As outlined in the previous
section, we start with the Windows Server ISO from Microsoft’s Volume Licensing Service
Center (VLSC) and validate the hash to ensure it matches Microsoft’s documentation for
new Windows Server operating systems.

We perform the following changes using automation on AWS to take the current
Windows Server AMIs and update them:

- Install all Microsoft recommended Windows security patches. We release images shortly
  after the monthly Microsoft patches are made available.
- Install the latest drivers for AWS hardware, including network and disk drivers, the
  EC2WinUtil utility for troubleshooting, as well as GPU
  drivers in selected AMIs.
- Include the following AWS launch agent software by default:
  - [EC2Launch v2](../../../AWSEC2/latest/UserGuide/ec2launch-v2.md "../../../AWSEC2/latest/UserGuide/ec2launch-v2.md") for Windows Server 2022 and 2025, and optionally
    for Windows Server 2019 and 2016 with specific AMIs.
  - [EC2Launch v1](../../../AWSEC2/latest/UserGuide/ec2launch.md "../../../AWSEC2/latest/UserGuide/ec2launch.md") for
    Windows Server 2016 and 2019.
  - [EC2Config](../../../AWSEC2/latest/UserGuide/ec2config-service.md "../../../AWSEC2/latest/UserGuide/ec2config-service.md") for Windows
    Server 2012 R2 and earlier.

- Configure Windows Time to use the [Amazon Time Sync Service](../../../AWSEC2/latest/UserGuide/set-time.md "../../../AWSEC2/latest/UserGuide/set-time.md").
- Change all power schemes to set the display to never turn off.
- Perform minor bug fixes – generally one-line registry changes to
  enable or disable features that we have found to improve performance on
  AWS.
- Tests and validates AMIs across new and existing EC2 platforms to help ensure
  compatibility, stability, and consistency before release.

For a more detailed list that includes initialization, installation,
and configuration settings that are applied, see [Updates applied for AWS Windows AMIs](windows-ami-configuration.md "windows-ami-configuration.md").

## How Amazon validates security, integrity, and authenticity of software on AMIs

We take a number of steps during the image build process, to maintain the
security, integrity, and authenticity of AWS Windows AMIs. A few
examples include:

- AWS Windows AMIs are built using source media obtained
  directly from Microsoft.
- Windows Updates are downloaded directly from Microsoft’s Windows
  Update Service by Windows, and installed on the instance used to create
  the AMI during the image build process.
- AWS Software is downloaded from secure S3 buckets and installed in
  the AMIs.
- Drivers, such as for the chipset and GPU, are obtained
  directly from the vendor, stored in secure S3 buckets, and installed on
  the AMIs during the image build process.

## How Amazon decides

which AWS Windows AMIs to offer

Each AMI is extensively tested prior to release to the public. We periodically streamline
our AMI offerings to simplify customer choice and to reduce costs.

- New AMI offerings are created for new OS releases. You can count on Amazon releasing
  _Base_, _Core_, and _SQL
  Express/Standard/Web/Enterprise_ offerings in English and other
  widely used languages. The primary difference between Base and Core offerings is
  that Base offerings have a desktop/GUI whereas Core offerings are PowerShell
  command line only. For more information, see [Windows Server Core](https://learn.microsoft.com/en-us/windows-server/administration/server-core/what-is-server-core "https://learn.microsoft.com/en-us/windows-server/administration/server-core/what-is-server-core") on the Microsoft website.
- New AMI offerings are created to support new platforms – for example,
  the Deep Learning andNvidia AMIs were created to support
  customers using our GPU-based instance types (P2 and P3, G3, and others).
- Less popular AMIs are sometimes removed. If we see a particular AMI is
  launched only a few times in its entire lifespan, we will remove it in
  favor of more widely used options.

If there is an AMI variant that you would like to see, let us know by opening a
support case, or by [providing feedback](https://repost.aws/knowledge-center/send-feedback-aws "https://repost.aws/knowledge-center/send-feedback-aws").

## Patches, security updates, and AMI

IDs

Amazon provides updated, fully-patched AWS Windows AMIs within five business days
of Microsoft's patch Tuesday (the second Tuesday of each month). The new AMIs
are available immediately from the **Images** page in the Amazon EC2
console. The new AMIs are available in the AWS Marketplace and the **Quick
Start** tab of the launch instance wizard within a few days of
their release.

###### Note

Instances launched from Windows Server 2019 and later AMIs may show a
Windows Update dialog message stating "Some settings are managed by your
organization." This message appears as a result of changes in Windows Server
2019 and does not impact the behavior of Windows Update or your ability to
manage update settings.

To remove this warning, see ["Some settings are managed by your organization"](../../../AWSEC2/latest/UserGuide/common-messages.md#some-settings-managed-by-org "../../../AWSEC2/latest/UserGuide/common-messages.md#some-settings-managed-by-org").

AWS Windows AMIs are publicly available for three months after they are released.
Within 10 days after the release of new AMIs, AWS changes access for AMIs that are more than
three months old to make them private.

After AWS makes an AMI private, you may no longer retrieve it by any method. In the
console, the **AMI ID** field for a private AMI states, `Cannot load 
 detail for `ami-1234567890abcdef0`. You may not be permitted to 
 view it.`

If an AMI is deprecated but is not yet marked private, you can still use it. However,
we recommend that you always use the latest version.

The AWS Windows AMIs; in each release have new AMI IDs. Therefore, we recommend
that you write scripts that locate the latest AWS Windows AMIs by their names,
rather than by their IDs. For more information, see the following
examples:

- [Get-EC2ImageByName](../../../powershell/latest/userguide/pstools-ec2-get-amis.md#pstools-ec2-get-ec2imagebyname "../../../powershell/latest/userguide/pstools-ec2-get-amis.md#pstools-ec2-get-ec2imagebyname") (AWS Tools for Windows PowerShell)
- [Query for the Latest AWS Windows AMI Using Systems Manager Parameter
  Store](https://aws.amazon.com/blogs/mt/query-for-the-latest-windows-ami-using-systems-manager-parameter-store/ "https://aws.amazon.com/blogs/mt/query-for-the-latest-windows-ami-using-systems-manager-parameter-store/")
- [Walkthrough: Looking Up Amazon Machine Image IDs](../../../AWSCloudFormation/latest/UserGuide/walkthrough-custom-resources-lambda-lookup-amiids.md "../../../AWSCloudFormation/latest/UserGuide/walkthrough-custom-resources-lambda-lookup-amiids.md")
  (AWS Lambda, AWS CloudFormation)
