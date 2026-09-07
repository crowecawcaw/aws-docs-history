

# Infrastructure setup
<a name="infrastucture-setup"></a>

Use the following steps to set up your customer’s AWS account. As the technology partner, you perform some steps, and your customer also performs some steps.

**Topics**
+ [Enable AWS account for Bring Your Own Protocol](#enable-account-for-byop)
+ [Grant partner solution access to AWS account](#grant-partner-solution-access)
+ [Enable the account for BYOL and conﬁgure the BYOL CIDR block (Windows client OS ONLY)](#enable-BYOL)
+ [Import the Windows Client OS image (BYOL-BYOP)](#import-image)
+ [Configure the directory](#configure-the-directory)
+ [Add a security group to a WorkSpaces directory](#add-security)
+ [Deploy Amazon WorkSpaces Core desktops](#deploy-desktop)
+ [Custom images](#custom-images)

## Enable AWS account for Bring Your Own Protocol
<a name="enable-account-for-byop"></a>

To enable the customer AWS account for BYOP, customers must contact their AWS account manager. For select technology partners with hosted managed solutions, BYOP might be enabled at the technology partner solution level. In that case, the customer account won't need to have BYOP enabled within their account.

## Grant partner solution access to AWS account
<a name="grant-partner-solution-access"></a>

Partner step and Customer step – Create a technology partner solution connection to the customer's AWS account.

For more information, see [AWS security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html) in the IAM User Guide. This connection can be done with secret and access keys for self-managed solutions. The preferred method is to use an assume role capability. For more information, see [How to Use External ID When Granting Access to Your AWS Resources](https://aws.amazon.com/blogs/security/how-to-use-external-id-when-granting-access-to-your-aws-resources/) at the AWS Security Blog.

If assume role access is being used, the technology partner creates an assume role from the technology partner solution's AWS account to the customer's AWS account. You can provide the customer with an AWS CloudFormation template to automate creation of the role with permissions or instructions on permissions as needed.

If assume role access is being used, instruct your customer to use tag-based authorization. This limits exposure to customer resources from the role granted to the partner solution. For more information, see [Tag-based authorization guidelines](tag-based-auth-guidelines.md).

## Enable the account for BYOL and conﬁgure the BYOL CIDR block (Windows client OS ONLY)
<a name="enable-BYOL"></a>

Follow these steps to enable Bring Your Own Licenses (BYOL), conﬁgure the BYOL Classless Inter-Domain Routing (CIDR) block, and register the directory.

1. *(Customer step)* – Enable BYOL.

   1. For information on how to enable BYOL see [Bring Your Own Windows desktop licenses](https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html) in the *Amazon WorkSpaces Administration Guide*.

1. *(Partner step)* – List and configure the management CIDR ranges.

   1. This is the management CIDR block that is required for the WorkSpaces dedicated control plane. WorkSpaces desktops have two elastic network interfaces: one network interface for the management network and another for access to a customer's virtual private cloud (VPC).

      First use the [DescribeAccountModifications](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeAccountModifications.html) API to see if the customer has configured the CIDR block already. If they haven't, use the [ListAvailableManagementCidrRanges](https://docs.aws.amazon.com/workspaces/latest/api/API_ListAvailableManagementCidrRanges.html) API to provide a list of CIDR block ranges for the customer to select. Then use the [ModifyAccount](https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyAccount.html) API to configure BYOL and provide the CIDR block.
**Important**  
This action can not be changed once configured.

## Import the Windows Client OS image (BYOL-BYOP)
<a name="import-image"></a>

Use the following steps to import the image.

1. *(Customer step)* – The customer must have an image within Amazon Elastic Compute Cloud (Amazon EC2) as an Amazon Machine Image (AMI). For more information, see [Importing a VM as an image using VM Import/Export](https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-image-import.html) in the *VM Import/Export User Guide*.

1. *(Partner step)* – List the AMIs and display them to the customer admin by using the [DescribeImages](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImages.html) API.

   ```
   describe-images - (EC2)
   "VirtualizationType" (filter)
   "Description" (display)
   "PlatformDetails" (display)
   "EnaSupport" (display) - instance types limit
   "Hypervisor" (display) - instance types limit
   "State" (filter)
   "ImageId" (display)
   "VolumeType" (display)
   "VolumeSize" (display) - make sure meets WS requirements
   "Encrypted" (display and filter) not supported
   "OwnerId" (display)
   "ImageType": "machine" (filter)
   "Name" (display)
   ```

1. *(Customer step)* – Select the Amazon EC2 AMI.

1. *(Partner step)* – Import the image. Make sure to use the BYOP import ingestion process with the [ImportWorkspaceImage](https://docs.aws.amazon.com/workspaces/latest/api/API_ImportWorkspaceImage.html) Amazon WorkSpaces Core API. When doing so, choose an ingestion process option that meets your needs. For more information about the ingestion process options available, see [IngestionProcess](https://docs.aws.amazon.com/workspaces/latest/api/API_ImportWorkspaceImage.html#WorkSpaces-ImportWorkspaceImage-request-IngestionProcess) in the *WorkSpaces API Reference*.

   Following is an example command using the AWS CLI:

   ```
   aws workspaces import-workspace-image --ec2-image-id {{ami-example123}} --ingestion-process BYOL_REGULAR_BYOP --image-name {{win10-ent-img01}} --image-description “{{Windows 10 Enterprise}}”
   ```

1. *(Partner step)* – Display the status of the import by using the [DescribeWorkspaceImages](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceImages.html) API.

## Configure the directory
<a name="configure-the-directory"></a>

Complete the following steps to configure the directory.

1. *(Partner step)* – Present the directories that the customer admin would choose for WorkSpaces using the [DescribeWorkspaceDirectories](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceDirectories.html) API. Amazon WorkSpaces requires that you pre-configure a directory within the AWS Directory Service.

1. *(Partner step)* – Register the directory to AWS for this WorkSpaces to access using the [RegisterWorkspaceDirectory](https://docs.aws.amazon.com/workspaces/latest/api/API_RegisterWorkspaceDirectory.html) API. This step is used for adding the desktop to Active Directory. Note that BYOL requires a tenancy of DEDICATED, all others must use SHARED

## Add a security group to a WorkSpaces directory
<a name="add-security"></a>

You must allow for access from the customer VPC into the Amazon WorkSpaces Core desktop. WorkSpaces desktops, including Amazon WorkSpaces Core desktops, have a security group attached to the customer VPC elastic network interface. By default, this security group blocks all traffic.

For Remote Desktop Protocol (RDP) access or access from any other protocol that will be accessing the desktop, you must add or modify a security group to the WorkSpaces directory. For more information, see [Security groups for your WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-security-groups.html) in the *Amazon WorkSpaces Administration Guide*.

You can also add this new default security group to existing WorkSpaces without rebuilding them. For more information, see [To add a security group to an existing WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-security-groups.html#security_group_existing_workspace) in the *Amazon WorkSpaces Administration Guide*. Use caution when modifying or deleting these security groups. Customers are responsible for the “security in the cloud." For more information, see [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/).

## Deploy Amazon WorkSpaces Core desktops
<a name="deploy-desktop"></a>

Complete the following steps to deploy the Amazon WorkSpaces Core desktops.

1. *(Partner and customer step)* – Create a bundle using the [CreateWorkspaceBundle](https://docs.aws.amazon.com/workspaces/latest/api/API_CreateWorkspaceBundle.html) API. Initially only needed for BYOL deployments. BYOL customers import their image first. They will need to create a bundle to deploy desktops. Unlike shared tenancy deployments where WorkSpaces provides a bundle which includes an image.

   ```
   CreateWorkspaceBundle (Amazon WorkSpaces)
      "BundleDescription"
      "BundleName"
      "ComputeType"
      "ImageId"
      "RootStorage" - "Capacity"
      "Tags": [
      "UserStorage"
         "Capacity"
   ```

1. *(Partner and customer step)* – Create a WorkSpace using the [CreateWorkspaces](https://docs.aws.amazon.com/workspaces/latest/api/API_CreateWorkspaces.html) API.
**Note**  
Amazon WorkSpaces Core (BYOP) supports user-decoupled and regular user-assigned WorkSpaces.

   Following is an example command using the AWS CLI:

   ```
   aws workspaces create-workspaces --workspaces DirectoryId={{d-example123}},UserName='"[UNDEFINED]"',WorkspaceName={{desktop1}},BundleId={{wsb-example123}}
   ```

   For `RunningMode`, the `AUTO_STOP` mode isn't available for Amazon WorkSpaces Core. Instead, a new running mode value of `MANUAL` is available for technology partner solutions to power manage the workspace and offer hourly usage of the instance. With the `MANUAL` mode, technology partner solutions use the `StartWorkSpaces` and `StopWorkSpaces` API operations to manage the workspaces. The customer is only charged for the hours when the WorkSpace is in the `AVAILABLE` state.
**Note**  
To ensure that no workspaces are inadvertently charging the customer for unknown periods of time, manual workspaces in the `AVAILABLE` state will be stopped after a sufficiently long period of time (greater than or equal to 48 hours). Manual workspaces are subject to an automatic maintenance window schedule once a month, similar to the current `AUTO_STOP` workspaces detailed here. You can opt out of this maintenance schedule by using the `ModifyWorkspaceCreationProperties` API operation. 

## Custom images
<a name="custom-images"></a>

After you deploy a WorkSpace, you can customize the image being used by customers moving forward. For example, if you use a shared tenancy bundle for BYOP and you’d like to install a partner solution agent, or install productivity or proprietary applications within an image. This is often referred to as *golden image creation*.

You can customize an image using the [CreateWorkspaceImage](https://docs.aws.amazon.com/workspaces/latest/api/API_CreateWorkspaceImage.html) API. You can then use use the [CreateWorkspaceBundle](https://docs.aws.amazon.com/workspaces/latest/api/API_CreateWorkspaceBundle.html) or [UpdateWorkspaceBundle](https://docs.aws.amazon.com/workspaces/latest/api/API_UpdateWorkspaceBundle.html) API. Then deploy WorkSpaces as described within this document.