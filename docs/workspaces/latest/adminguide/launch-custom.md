

# Create a dedicated Custom directory with WorkSpaces Personal
<a name="launch-custom"></a>

Before you create Windows 10 and 11 BYOL personal WorkSpaces and assign them to your users, managed with AWS IAM Identity Center Identity Providers (IdPs), you must create a dedicated Custom WorkSpaces directory. Personal WorkSpaces are not joined to any Microsoft Active Directory but can be managed with a Mobile Device Management (MDM) solution of your choice, such as JumpCloud. For more information about JumpCloud, see [this article](https://jumpcloud.com/support/integrate-with-aws-workspaces). For tutorials that use the other options, see [Create a directory for WorkSpaces Personal](launch-workspaces-tutorials.md).

**Note**  
Amazon WorkSpaces can't create or manage user accounts on personal WorkSpaces launched in a Custom directory. As an administrator, you will have to manage them.
Custom WorkSpaces directory is available in all AWS regions where Amazon WorkSpaces is offered except for Africa (Cape Town), Israel (Tel Aviv), and China (Ningxia).
Amazon WorkSpaces can't create or manage user accounts on WorkSpaces using Custom directories. To ensure the MDM agent software you use can create the user profile on the Windows WorkSpaces, contact the MDM solution providers. Creating the user profile allows your users to sign into the Windows desktop from Windows login screen.

**Contents**
+ [Requirements and limitations](#custom-requirements-limitations)
+ [Step 1: Enable IAM Identity Center and connect with your Identity Provider](#custom-step-1)
+ [Step 2: Create a dedicated Custom WorkSpaces directory](#custom-step-2)

## Requirements and limitations
<a name="custom-requirements-limitations"></a>
+ Custom WorkSpaces directories only support Windows 10 or 11 Bring Your Own License personal WorkSpaces.
+ Custom WorkSpaces directories only support DCV protocol.
+ Ensure you enable BYOL for your AWS account and you have your own AWS KMS server that your personal WorkSpaces can access for Windows 10 and 11 activation. For details, see [Bring Your Own Windows desktop licenses in WorkSpaces](byol-windows-images.md).
+ Ensure you pre-install the MDM agent software on the BYOL image that you imported to your AWS account.

## Step 1: Enable IAM Identity Center and connect with your Identity Provider
<a name="custom-step-1"></a>

To assign WorkSpaces to your users managed with your Identity Providers, the user information must be made available to AWS through AWS IAM Identity Center. We recommend using IAM Identity Center to manage your user's access to AWS resources. For more information, see [What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html). This is a one-time setup.

**To make user information available to AWS**

1. Enable IAM Identity Center on AWS. You can enable IAM Identity Center with your AWS organizations, especially if you are using a multi-account environment. You can also create an account instance of IAM Identity Center. For more information, see [ Enabling AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-set-up-for-idc.html). Each WorkSpaces directory can associate with one IAM Identity Center organization or account instance. Each IAM Identity Center instance can be associated with one or more WorkSpaces Personal directory.

   If you are using an organization instance and trying to create a WorkSpaces directory in one of the member accounts, ensure you have the following IAM Identity Center permissions. 
   + `"sso:DescribeInstance"`
   + `"sso:CreateApplication"`
   + `"sso:PutApplicationGrant"`
   + `"sso:PutApplicationAuthenticationMethod"`
   + `"sso:DeleteApplication"`
   + `"sso:DescribeApplication"`
   + `"sso:getApplicationGrant"`

   For more information, see [ Overview of managing access permissions to your IAM Identity Center resources](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-overview.html). Ensure that no Service Control Policies (SCPs) are blocking these permissions. To learn more about SCPs, see [ Service control policies (SCPs)](https://docs.aws.amazon.com/userguide/orgs_manage_policies_scps.html).

1. Configure IAM Identity Center and your Identity Provider (IdP) to automatically synchronize users from your IdP to your IAM Identity Center instance. For more information, see [ Getting started tutorials](https://docs.aws.amazon.com/singlesignon/latest/userguide/tutorials.html) and choose the specific tutorial for the IdP that you want to use. For example, [ Using IAM Identity Center to connect with your JumpCloud Directory Platform](https://docs.aws.amazon.com/singlesignon/latest/userguide/jumpcloud-idp.html).

1. Verify that the users you configured on your IdP are synchronized correctly to AWS IAM Identity Center instance. The first synchronization can take up to an hour depending the configuration of your IdP. 

## Step 2: Create a dedicated Custom WorkSpaces directory
<a name="custom-step-2"></a>

Create a dedicated WorkSpaces Personal directory that stores information about your personal WorkSpaces and your users.

**To create a dedicated Custom WorkSpaces directory**

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home).

1. In the navigation pane, choose **Directories**.

1. Choose **Create directory**.

1. On the **Create directory** page, for **WorkSpaces** type, choose **Personal**. For **WorkSpace device management**, choose **Custom**.

1. For **User identity source**, select the IAM Identity Center instance that you configured in [Step 1](https://docs.aws.amazon.com/) from the dropdown list. You won't be able to change the IAM Identity Center instance associated with the directory once the directory is created.
**Note**  
You have to specify an IAM Identity Center instance for the directory or you won't be able to launch personal WorkSpaces with the directory using the WorkSpaces console. WorkSpaces directories with no associated Identity Center are only compatible with WorkSpaces Core partner solutions.

1. For **Directory name**, enter a unique name for the directory.

1. For **VPC**, select the VPC that you used to launch your WorkSpaces. For more information, see [Configure a VPC for WorkSpaces Personal](amazon-workspaces-vpc.md).

1. For **Subnets**, select two subnets of your VPC that are not from the same Availability Zone. These subnets will be used to launch your personal WorkSpaces. For more information, see [Availability Zones for WorkSpaces Personal](azs-workspaces.md).
**Important**  
Make sure the WorkSpaces launched in the subnets have internet access, which is needed when users login to the Windows desktops. For more information, see [Provide internet access for WorkSpaces Personal](amazon-workspaces-internet-access.md).

1. For **Configuration**, select **Enable dedicated WorkSpace**. You must enable it to create a dedicated WorkSpaces Personal directory to launch Bring Your Own License (BYOL) Windows 10 or 11 personal WorkSpaces. 

1. (Optional) For **Tags**, specify the key pair value that you want to use for personal WorkSpaces in the directory.

1. Review the directory summary and choose **Create directory**. It takes several minutes for your directory to be connected. The initial status of the directory is `Creating`. When directory creation is complete, the status is `Active`. 

An IAM Identity Center application is also automatically created on your behalf once the directory is created. To find the application’s ARN go to the directory's summary page.

You can now use the directory to launch Windows 10 or 11 personal WorkSpaces that are enrolled to Microsoft Intune and joined to Microsoft Entra ID. For more information, see [Create a WorkSpace in WorkSpaces Personal](create-workspaces-personal.md). 

After you've created a WorkSpaces Personal directory, you can create a personal WorkSpace. For more information, see [Create a WorkSpace in WorkSpaces Personal](create-workspaces-personal.md)