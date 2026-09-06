

# Manage Image Builder distribution settings
<a name="manage-distribution-settings"></a>

Before you configure distribution settings for your output images, we recommend that you verify availability for any underlying infrastructure or other requirements for instances that are launched from your output image in the distribution target Regions. For example, not all Regions support EC2 Mac Dedicated Hosts, which are required to launch instances from a macOS image. For more information about instance types and pricing for Dedicated Hosts, see [Amazon EC2 Dedicated Hosts Pricing](https://aws.amazon.com/ec2/dedicated-hosts/pricing/).

After you create distribution settings with Image Builder, you can manage them using the Image Builder console, the Image Builder API, or **imagebuilder** commands in the AWS CLI. With distribution settings, you can perform the following actions:

**AMI distribution**
+ Specify the name and description of your output AMI.
+ Authorize other AWS accounts, organizations, and OUs to launch the AMI from the owner's account. The owner account is billed for charges that are associated with the AMI.
**Note**  
To make an AMI public, set the launch permission authorized accounts to `all`. For information and examples, see **[ModifyImageAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyImageAttribute.html)** in the *Amazon EC2 API Reference*.
**Important**  
You cannot make AMIs with watermarks public. If your image recipe includes watermarks, or if the source AMI has watermarks attached, you cannot set launch permissions to public. Image Builder rejects the distribution configuration. Watermarks propagate automatically when you copy or distribute an AMI across Regions or accounts. For more information, see [Track AMI lineage with watermarks](ami-watermarks.md).
+ Create a copy of the output AMI for each of the specified target accounts, organizations, and OUs in the destination Region. The target accounts, organizations, and OUs own their AMI copies, and are billed for any associated charges. For more information about distributing your AMI to AWS Organizations and OUs, see [Share an AMI with organizations or OUs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/share-amis-with-organizations-and-OUs.html).
+ Copy the AMI to the owner's account in other AWS Regions.
+ Export VM image disks to Amazon Simple Storage Service (Amazon S3). For more information, see [Example: Create distribution settings for output VM disks from the AWS CLI](cr-upd-ami-distribution-settings.md#cli-create-vm-dist-config).

**Container image distribution**
+ Specify the ECR repository where Image Builder stores the output image in the distribution Region.

You can use your distribution settings in the following ways to deliver images to target Regions, accounts, AWS Organizations and organizational units (OUs) one time, or with every pipeline build:
+ To automatically deliver updated images to specified Regions, accounts, Organizations, and OUs, use distribution settings with an Image Builder pipeline that runs on a schedule.
+ To create a new image and deliver it to the specified Regions, accounts, Organizations, and OUs, use distribution settings with an Image Builder pipeline that you run one time from the Image Builder console, using **Run pipeline** from the **Actions** menu.
+ To create a new image and deliver it to the specified Regions, accounts, Organizations, and OUs, use distribution settings with the following API action or Image Builder command in the AWS CLI:
  + The **[CreateImage](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateImage.html)** action in the Image Builder API.
  + The **[create-image](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-image.html)** command in the AWS CLI.
+ To export virtual machine (VM) image disks to S3 buckets in target Regions as part of your regular image build process.

**Tip**  
When you have multiple resources of the same type, tagging helps you to identify a specific resource based on the tags you've assigned to it. For more information about tagging your resources using Image Builder commands in the AWS CLI, see the [Tag resources](tag-resources.md) section of this guide.

**Topics**
+ [List and view distribution configuration detail](distribution-settings-detail.md)
+ [Create and update AMI distribution configurations](cr-upd-ami-distribution-settings.md)
+ [Create and update distribution settings for container images](cr-upd-container-distribution-settings.md)
+ [Set up cross-account AMI distribution with Image Builder](cross-account-dist.md)
+ [Configure AMI distribution with an EC2 launch template](dist-using-launch-template.md)
+ [Use enhanced AMI distribution capabilities](distribution-enhanced_functionality.md)