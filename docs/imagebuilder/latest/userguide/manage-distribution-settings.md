# Manage Image Builder distribution settings

Before you configure distribution settings for your output images, we recommend that you
verify availability for any underlying infrastructure or other requirements for instances
that are launched from your output image in the distribution target Regions. For example,
not all Regions support EC2 Mac Dedicated Hosts, which are required to launch
instances from a macOS image. For more information about instance types and pricing for
Dedicated Hosts, see [Amazon EC2
Dedicated Hosts Pricing](https://aws.amazon.com/ec2/dedicated-hosts/pricing/ "https://aws.amazon.com/ec2/dedicated-hosts/pricing/").

After you create distribution settings with Image Builder, you can manage them using the Image Builder console,
the Image Builder API, or **imagebuilder** commands in the AWS CLI. With distribution
settings, you can perform the following actions:

###### AMI distribution

- Specify the name and description of your output AMI.
- Authorize other AWS accounts, organizations, and OUs to launch the AMI from
  the owner's account. The owner account is billed for charges that are associated
  with the AMI.

###### Note

To make an AMI public, set the launch permission authorized accounts to
`all`. For information and examples, see
**[ModifyImageAttribute](../../../AWSEC2/latest/APIReference/API_ModifyImageAttribute.md "../../../AWSEC2/latest/APIReference/API_ModifyImageAttribute.md")** in the _Amazon EC2 API Reference_.

- Create a copy of the output AMI for each of the specified target accounts,
  organizations, and OUs in the destination Region. The target accounts, organizations,
  and OUs own their AMI copies, and are billed for any associated charges. For more information about
  distributing your AMI to AWS Organizations and OUs, see [Share an AMI with
  organizations or OUs](../../../AWSEC2/latest/UserGuide/share-amis-with-organizations-and-OUs.md "../../../AWSEC2/latest/UserGuide/share-amis-with-organizations-and-OUs.md").
- Copy the AMI to the owner's account in other AWS Regions.
- Export VM image disks to Amazon Simple Storage Service (Amazon S3). For more information, see
  [Example: Create
  distribution settings for output VM disks from the AWS CLI](cr-upd-ami-distribution-settings.md#cli-create-vm-dist-config "cr-upd-ami-distribution-settings.md#cli-create-vm-dist-config").

###### Container image distribution

- Specify the ECR repository where Image Builder stores the output image in the
  distribution Region.
  You can use your distribution settings in the following ways to deliver images to target
  Regions, accounts, AWS Organizations and organizational units (OUs) one time, or with every pipeline
  build:

- To automatically deliver updated images to specified Regions, accounts, Organizations,
  and OUs, use distribution settings with an Image Builder pipeline that runs on a schedule.
- To create a new image and deliver it to the specified Regions, accounts, Organizations,
  and OUs, use distribution settings with an Image Builder pipeline that you run one time
  from the Image Builder console, using **Run pipeline** from the
  **Actions** menu.
- To create a new image and deliver it to the specified Regions, accounts, Organizations,
  and OUs, use distribution settings with the following API action or Image Builder command in the AWS CLI:
  - The **[CreateImage](../APIReference/API_CreateImage.md "../APIReference/API_CreateImage.md")**
    action in the Image Builder API.
  - The **[create-image](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-image.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-image.html")**
    command in the AWS CLI.

- To export virtual machine (VM) image disks to S3 buckets in target Regions
  as part of your regular image build process.

###### Tip

When you have multiple resources of the same type, tagging helps you to
identify a specific resource based on the tags you've assigned to it.
For more information about tagging your resources using Image Builder commands
in the AWS CLI, see the [Tag resources](tag-resources.md "tag-resources.md")
section of this guide.

###### Contents

- [List and view distribution configuration detail](distribution-settings-detail.md "distribution-settings-detail.md")
- [Create and update AMI distribution configurations](cr-upd-ami-distribution-settings.md "cr-upd-ami-distribution-settings.md")
- [Create and update distribution settings
  for container images](cr-upd-container-distribution-settings.md "cr-upd-container-distribution-settings.md")
- [Set up cross-account AMI distribution with Image Builder](cross-account-dist.md "cross-account-dist.md")
- [Configure AMI distribution with
  an EC2 launch template](dist-using-launch-template.md "dist-using-launch-template.md")
- [Use enhanced AMI distribution capabilities](distribution-enhanced_functionality.md "distribution-enhanced_functionality.md")
