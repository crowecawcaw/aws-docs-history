# Create an AWS Managed Microsoft AD directory for WorkSpaces Personal

In this tutorial, we create an AWS Managed Microsoft AD directory. For tutorials
that use the other options, see [Create a directory for WorkSpaces Personal](launch-workspaces-tutorials.md "launch-workspaces-tutorials.md").

First, create an AWS Managed Microsoft AD directory. Directory Service creates two directory servers, one in each of the
private subnets of your VPC. Note that there are no users in the directory initially. You
will add a user in the next step when you launch the WorkSpace.

###### Note

- Shared directories are not currently supported for use with Amazon WorkSpaces.
- If your AWS Managed Microsoft AD directory has been configured for multi-Region replication,
  only the directory in the primary Region can be registered for use with Amazon WorkSpaces. Attempts
  to register the directory in a replicated Region for use with Amazon WorkSpaces will fail.
  Multi-Region replication with AWS Managed Microsoft AD isn't supported for use with Amazon WorkSpaces
  within replicated Regions.

###### To create an AWS Managed Microsoft AD directory

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **Directories**.
3. Choose **Create directory**.
4. On the **Create directory** page, for **WorkSpaces type**
   choose **Personal**. Then, for **WorkSpace device management**
   choose **AWS Directory Service**.
5. Choose **Create directory**, which opens the **Set up a directory**
   page on the AWS Directory Service
6. Choose **AWS Managed Microsoft AD**, and then **Next**.
7. Configure the directory as follows:
   1. For **Organization name**, enter a unique organization name
      for your directory (for example, my-demo-directory). This name must be at least
      four characters in length, consist of only alphanumeric characters and hyphens
      (-), and begin or end with a character other than a hyphen.
   2. For **Directory DNS**, enter the fully-qualified name for
      the directory (for example, workspaces.demo.com).

   ###### Important

   If you need to update your DNS server after launching your WorkSpaces,
   follow the procedure in [Update DNS servers for WorkSpaces Personal](update-dns-server.md "update-dns-server.md")
   to ensure that your WorkSpaces get properly updated. 3. For **NetBIOS name**, enter a short name for the directory
   (for example, workspaces). 4. For **Admin password** and **Confirm
   password**, enter a password for the directory administrator
   account. For more information about the password requirements, see [Create Your AWS Managed
   Microsoft AD Directory](../../../directoryservice/latest/admin-guide/create_managed_ad.md "../../../directoryservice/latest/admin-guide/create_managed_ad.md") in the
   _AWS Directory Service Administration Guide_. 5. (Optional) For **Description**, enter a description for the
   directory. 6. For **VPC**, select the VPC that you created. 7. For **Subnets**, select the two private subnets (with the CIDR blocks
   `10.0.1.0/24` and `10.0.2.0/24`). 8. Choose **Next Step**.

8. Choose **Create directory**.
9. You will be brought back to the Create directory page on WorkSpaces console.
   The initial status of the directory is `Requested` and then
   `Creating`. When directory creation is complete (this might take
   a few minutes), the status is `Active`.
   After you’ve created an AWS Managed Microsoft AD directory, you can register it with Amazon WorkSpaces.
   For more information, see [Register an existing Directory Service directory with WorkSpaces Personal](register-deregister-directory.md "register-deregister-directory.md")
