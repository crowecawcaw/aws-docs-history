# Infrastructure setup

Use the following steps to set up your customer’s AWS account. As the technology partner,
you perform some steps, and your customer also performs some steps.

###### Topics

- [Enable AWS account for Bring Your Own
  Protocol](#enable-account-for-byop "#enable-account-for-byop")
- [Grant partner solution access to
  AWS account](#grant-partner-solution-access "#grant-partner-solution-access")
- [Enable the account for BYOL and conﬁgure the BYOL CIDR block
  (Windows client OS ONLY)](#enable-BYOL "#enable-BYOL")
- [Import the Windows Client OS image (BYOL-BYOP)](#import-image "#import-image")
- [Configure the directory](#configure-the-directory "#configure-the-directory")
- [Add a security group to a WorkSpaces directory](#add-security "#add-security")
- [Deploy Amazon WorkSpaces Core desktops](#deploy-desktop "#deploy-desktop")
- [Custom images](#custom-images "#custom-images")

## Enable AWS account for Bring Your Own

Protocol

To enable the customer AWS account for BYOP, customers must contact their AWS account
manager. For select technology partners with hosted managed solutions, BYOP might be enabled at
the technology partner solution level. In that case, the customer account won't need to have BYOP
enabled within their account.

## Grant partner solution access to

AWS account

Partner step and Customer step – Create a technology partner solution connection to the
customer's AWS account.

For more information, see [AWS security credentials](../../../IAM/latest/UserGuide/security-creds.md "../../../IAM/latest/UserGuide/security-creds.md") in the IAM User
Guide. This connection can be done with secret and access keys for self-managed solutions. The
preferred method is to use an assume role capability. For more information, see [How to
Use External ID When Granting Access to Your AWS Resources](https://aws.amazon.com/blogs/security/how-to-use-external-id-when-granting-access-to-your-aws-resources/ "https://aws.amazon.com/blogs/security/how-to-use-external-id-when-granting-access-to-your-aws-resources/") at the AWS Security
Blog.

If assume role access is being used, the technology partner creates an assume role from the
technology partner solution's AWS account to the customer's AWS account. You can provide the
customer with an AWS CloudFormation template to automate creation of the role with permissions or
instructions on permissions as needed.

If assume role access is being used, instruct your customer to use tag-based authorization.
This limits exposure to customer resources from the role granted to the partner solution. For
more information, see [Tag-based authorization guidelines](tag-based-auth-guidelines.md "tag-based-auth-guidelines.md").

## Enable the account for BYOL and conﬁgure the BYOL CIDR block

(Windows client OS ONLY)

Follow these steps to enable Bring Your Own Licenses (BYOL), conﬁgure the BYOL Classless
Inter-Domain Routing (CIDR) block, and register the directory.

1. _(Customer step)_ – Enable BYOL.
   1. For information on how to enable BYOL see [Bring Your Own Windows desktop
      licenses](../../../workspaces/latest/adminguide/byol-windows-images.md "../../../workspaces/latest/adminguide/byol-windows-images.md") in the _Amazon WorkSpaces Administration Guide_.

2. _(Partner step)_ – List and configure the management CIDR
   ranges.
   1. This is the management CIDR block that is required for the WorkSpaces dedicated control
      plane. WorkSpaces desktops have two elastic network interfaces: one network interface for the
      management network and another for access to a customer's virtual private cloud (VPC).

   First use the [DescribeAccountModifications](../../../workspaces/latest/api/API_DescribeAccountModifications.md "../../../workspaces/latest/api/API_DescribeAccountModifications.md") API to see if the customer has configured the CIDR
   block already. If they haven't, use the [ListAvailableManagementCidrRanges](../../../workspaces/latest/api/API_ListAvailableManagementCidrRanges.md "../../../workspaces/latest/api/API_ListAvailableManagementCidrRanges.md") API to provide a list of CIDR block ranges for
   the customer to select. Then use the [ModifyAccount](../../../workspaces/latest/api/API_ModifyAccount.md "../../../workspaces/latest/api/API_ModifyAccount.md") API to configure
   BYOL and provide the CIDR block.

   ###### Important

   This action can not be changed once configured.

## Import the Windows Client OS image (BYOL-BYOP)

Use the following steps to import the image.

1. _(Customer step)_ – The customer must have an image within
   Amazon Elastic Compute Cloud (Amazon EC2) as an Amazon Machine Image (AMI). For more information, see [Importing a
   VM as an image using VM Import/Export](../../../vm-import/latest/userguide/vmimport-image-import.md "../../../vm-import/latest/userguide/vmimport-image-import.md") in the _VM Import/Export User
   Guide_.
2. _(Partner step)_ – List the AMIs and display them to the
   customer admin by using the [DescribeImages](../../../AWSEC2/latest/APIReference/API_DescribeImages.md "../../../AWSEC2/latest/APIReference/API_DescribeImages.md") API.

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

3. _(Customer step)_ – Select the Amazon EC2 AMI.
4. _(Partner step)_ – Import the image. Make sure to use the BYOP
   import ingestion process with the [ImportWorkspaceImage](../../../workspaces/latest/api/API_ImportWorkspaceImage.md "../../../workspaces/latest/api/API_ImportWorkspaceImage.md")
   Amazon WorkSpaces Core API. When doing so, choose an ingestion process option that meets your needs. For
   more information about the ingestion process options available, see [IngestionProcess](../../../workspaces/latest/api/API_ImportWorkspaceImage.md#WorkSpaces-ImportWorkspaceImage-request-IngestionProcess "../../../workspaces/latest/api/API_ImportWorkspaceImage.md#WorkSpaces-ImportWorkspaceImage-request-IngestionProcess") in the _WorkSpaces API Reference_.

Following is an example command using the AWS CLI:

```
aws workspaces import-workspace-image --ec2-image-id `ami-example123` --ingestion-process BYOL_REGULAR_BYOP --image-name `win10-ent-img01` --image-description “`Windows 10 Enterprise`”
```

5. _(Partner step)_ – Display the status of the import by using the
   [DescribeWorkspaceImages](../../../workspaces/latest/api/API_DescribeWorkspaceImages.md "../../../workspaces/latest/api/API_DescribeWorkspaceImages.md") API.

## Configure the directory

Complete the following steps to configure the directory.

1. _(Partner step)_ – Present the directories that the customer
   admin would choose for WorkSpaces using the [DescribeWorkspaceDirectories](../../../workspaces/latest/api/API_DescribeWorkspaceDirectories.md "../../../workspaces/latest/api/API_DescribeWorkspaceDirectories.md") API. Amazon WorkSpaces requires that you pre-configure a
   directory within the AWS Directory Service.
2. _(Partner step)_ – Register the directory to AWS for this
   WorkSpaces to access using the [RegisterWorkspaceDirectory](../../../workspaces/latest/api/API_RegisterWorkspaceDirectory.md "../../../workspaces/latest/api/API_RegisterWorkspaceDirectory.md") API. This step is used for adding the desktop to Active
   Directory. Note that BYOL requires a tenancy of DEDICATED, all others must use SHARED

## Add a security group to a WorkSpaces directory

You must allow for access from the customer VPC into the Amazon WorkSpaces Core desktop. WorkSpaces desktops,
including Amazon WorkSpaces Core desktops, have a security group attached to the customer VPC elastic network
interface. By default, this security group blocks all traffic.

For Remote Desktop Protocol (RDP) access or access from any other protocol that will be
accessing the desktop, you must add or modify a security group to the WorkSpaces directory. For more
information, see [Security groups for
your WorkSpaces](../../../workspaces/latest/adminguide/amazon-workspaces-security-groups.md "../../../workspaces/latest/adminguide/amazon-workspaces-security-groups.md") in the _Amazon WorkSpaces Administration
Guide_.

You can also add this new default security group to existing WorkSpaces without rebuilding them.
For more information, see [To add a security group to an existing WorkSpace](../../../workspaces/latest/adminguide/amazon-workspaces-security-groups.md#security_group_existing_workspace "../../../workspaces/latest/adminguide/amazon-workspaces-security-groups.md#security_group_existing_workspace") in the _Amazon WorkSpaces Administration Guide_. Use caution when modifying or deleting these
security groups. Customers are responsible for the “security in the cloud." For more information,
see [Shared
Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/").

## Deploy Amazon WorkSpaces Core desktops

Complete the following steps to deploy the Amazon WorkSpaces Core desktops.

1. _(Partner and customer step)_ – Create a bundle using the [CreateWorkspaceBundle](../../../workspaces/latest/api/API_CreateWorkspaceBundle.md "../../../workspaces/latest/api/API_CreateWorkspaceBundle.md") API. Initially only needed for BYOL deployments. BYOL customers
   import their image first. They will need to create a bundle to deploy desktops. Unlike shared
   tenancy deployments where WorkSpaces provides a bundle which includes an image.

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

2. _(Partner and customer step)_ – Create a WorkSpace using the
   [CreateWorkspaces](../../../workspaces/latest/api/API_CreateWorkspaces.md "../../../workspaces/latest/api/API_CreateWorkspaces.md") API.

###### Note

Amazon WorkSpaces Core (BYOP) supports user-decoupled and regular user-assigned WorkSpaces.

Following is an example command using the AWS CLI:

```
aws workspaces create-workspaces --workspaces DirectoryId=`d-example123`,UserName='"[UNDEFINED]"',WorkspaceName=`desktop1`,BundleId=`wsb-example123`
```

For `RunningMode`, the `AUTO_STOP` mode isn't available for
Amazon WorkSpaces Core. Instead, a new running mode value of `MANUAL` is available for technology
partner solutions to power manage the workspace and offer hourly usage of the instance. With
the `MANUAL` mode, technology partner solutions use the `StartWorkSpaces`
and `StopWorkSpaces` API operations to manage the workspaces. The customer is only
charged for the hours when the WorkSpace is in the `AVAILABLE` state.

###### Note

To ensure that no workspaces are inadvertently charging the customer for unknown periods
of time, manual workspaces in the `AVAILABLE` state will be stopped after a
sufficiently long period of time (greater than or equal to 48 hours). Manual workspaces are
subject to an automatic maintenance window schedule once a month, similar to the current
`AUTO_STOP` workspaces detailed here. You can opt out of this maintenance schedule
by using the `ModifyWorkspaceCreationProperties` API operation.

## Custom images

After you deploy a WorkSpace, you can customize the image being used by customers moving
forward. For example, if you use a shared tenancy bundle for BYOP and you’d like to install a
partner solution agent, or install productivity or proprietary applications within an image. This
is often referred to as _golden image creation_.

You can customize an image using the [CreateWorkspaceImage](../../../workspaces/latest/api/API_CreateWorkspaceImage.md "../../../workspaces/latest/api/API_CreateWorkspaceImage.md") API. You
can then use use the [CreateWorkspaceBundle](../../../workspaces/latest/api/API_CreateWorkspaceBundle.md "../../../workspaces/latest/api/API_CreateWorkspaceBundle.md") or
[UpdateWorkspaceBundle](../../../workspaces/latest/api/API_UpdateWorkspaceBundle.md "../../../workspaces/latest/api/API_UpdateWorkspaceBundle.md") API. Then deploy WorkSpaces as described within this document.
