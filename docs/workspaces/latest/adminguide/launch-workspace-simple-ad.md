

# Create a Simple AD directory for WorkSpaces Personal
<a name="launch-workspace-simple-ad"></a>

In this tutorial, we launch a WorkSpace that uses Simple AD. For tutorials that use the other options, see [Create a directory for WorkSpaces Personal](launch-workspaces-tutorials.md).

**Note**  
New customer onboarding to Simple AD is not permitted after July 30, 2026. For more information, see [ Simple AD availability changes](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple-ad-availability-change.html).
Simple AD is not available in every AWS Region. Verify the supported Regions and [ select a Region](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/getting-started.html#select-region) for your Simple AD directory. For more information about the supported Regions for Simple AD, see [ Region Availability for AWS Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/regions.html).
Simple AD is made available to you free of charge to use with WorkSpaces. If there are no WorkSpaces being used with your Simple AD directory for 30 consecutive days, this directory will be automatically deregistered for use with Amazon WorkSpaces, and you will be charged for this directory as per the [AWS Directory Service pricing terms](https://aws.amazon.com/directoryservice/pricing/).
[ Simple AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_getting_started.html) currently supports only IPv4 addressing, meaning that when creating a directory, the associated VPC will be configured with an IPv4 CIDR block and does not support IPv6 networks.

When you create a Simple AD directory. Directory Service creates two directory servers, one in each of the private subnets of your VPC. There are no users in the directory initially. Add a user after you create the WorkSpace. For more information, see [Create a WorkSpace in WorkSpaces Personal](create-workspaces-personal.md)

**To create a Simple AD directory**

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home).

1. In the navigation pane, choose **Directories**.

1. Choose **Create directory**.

1. On the **Create directory** page, for **WorkSpaces type** choose **Personal**. Then, for **WorkSpace device management** choose **AWS Directory Service**.

1. Choose **Create directory**, which opens the **Set up a directory** page on the AWS Directory Service

1. Choose **Simple AD**, and then **Next**.

1. Configure the directory as follows:

   1. For **Organization name**, enter a unique organization name for your directory (for example, my-example-directory). This name must be at least four characters in length, consist of only alphanumeric characters and hyphens (-), and begin or end with a character other than a hyphen.

   1. For **Directory DNS name**, enter the fully-qualified name for the directory (for example, example.com).
**Important**  
If you need to update your DNS server after launching your WorkSpaces, follow the procedure in [Update DNS servers for WorkSpaces Personal](update-dns-server.md) to ensure that your WorkSpaces get properly updated.

   1. For **NetBIOS name**, enter a short name for the directory (for example, example).

   1. For **Admin password** and **Confirm password**, enter a password for the directory administrator account. For more information about the password requirements, see [How to Create a Microsoft AD Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/create_managed_ad.html) in the *AWS Directory Service Administration Guide*.

   1. (Optional) For **Description**, enter a description for the directory.

   1. For **Directory size**, choose **Small**.

   1. For **VPC**, select the VPC that you created.

   1. For **Subnets**, select the two private subnets (with the CIDR blocks `10.0.1.0/24` and `10.0.2.0/24`).

   1. Choose **Next**.

1. Choose **Create directory**.

1. You will be brought back to the Create directory page on WorkSpaces console. The initial status of the directory is `Requested` and then `Creating`. When directory creation is complete (this might take a few minutes), the status is `Active`.

**What happens during directory creation**

WorkSpaces completes the following tasks on your behalf:
+ Creates an IAM role to allow the WorkSpaces service to create elastic network interfaces and list your WorkSpaces directories. This role has the name `workspaces_DefaultRole`.
+ Sets up a Simple AD directory in the VPC that is used to store user and WorkSpace information. The directory has an administrator account with the user name Administrator and the specified password.
+ Creates two security groups, one for directory controllers and another for WorkSpaces in the directory.

After you’ve created an Simple AD directory, you can register it with Amazon WorkSpaces. For more information, see [Register an existing Directory Service directory with WorkSpaces Personal](register-deregister-directory.md)