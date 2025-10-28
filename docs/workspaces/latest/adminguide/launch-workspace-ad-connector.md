# Create an AD Connector for WorkSpaces Personal

In this tutorial, we create an AD Connector. For tutorials
that use the other options, see [Create a directory for WorkSpaces Personal](launch-workspaces-tutorials.md "launch-workspaces-tutorials.md").

## Create an AD Connector

###### Note

AD Connector is made available to you free of charge to use with WorkSpaces.
If there are no WorkSpaces being used with your AD Connector directory for 30
consecutive days, this directory will be automatically deregistered for use with Amazon WorkSpaces,
and you will be charged for this directory as per the
[AWS Directory Service pricing terms](https://aws.amazon.com/directoryservice/pricing/ "https://aws.amazon.com/directoryservice/pricing/").

To delete empty directories, see
[Delete a directory for WorkSpaces Personal](delete-workspaces-directory.md "delete-workspaces-directory.md"). If
you delete your AD Connector directory, you can always create a new one when you want to start
using WorkSpaces again.

###### To create an AD Connector

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **Directories**.
3. Choose **Create directory**.
4. On the **Create directory** page, for **WorkSpaces type**
   choose **Personal**. Then, for **WorkSpace device management**
   choose **AWS Directory Service**.
5. Choose **Create directory**, which opens the **Set up a directory**
   page on the AWS Directory Service
6. Choose **AWS Managed Microsoft AD**, and then **Next**.
7. For **Organization name**, enter a unique organization name for
   your directory (for example, my-example-directory). This name must be at least four
   characters in length, consist of only alphanumeric characters and hyphens (-), and
   begin or end with a character other than a hyphen.
8. For **Connected directory DNS**, enter the fully-qualified name
   of your on-premises directory (for example, example.com).
9. For **Connected directory NetBIOS name**, enter the short name of
   your on-premises directory (for example, example).
10. For **Connector account username**, enter the user name of a user
    in your on-premises directory. The user must have permissions to read users and
    groups, create computer objects, and join computers to the domain.
11. For **Connector account password** and **Confirm
    password**, enter the password for the on-premises user.
12. For **DNS address**, enter the IP address of at least one DNS
    server in your on-premises directory.

###### Important

If you need to update your DNS server IP address after launching your WorkSpaces,
follow the procedure in [Update DNS servers for WorkSpaces Personal](update-dns-server.md "update-dns-server.md")
to ensure that your WorkSpaces get properly updated. 13. (Optional) For **Description**, enter a description for the
directory. 14. Keep **Size** as **Small**. 15. For **VPC**, select your VPC. 16. For **Subnets**, select your subnets. The DNS servers that you specified
must be accessible from each subnet. 17. Choose **Create directory**. 18. You will be brought back to the Create directory page on WorkSpaces console.
The initial status of the directory is `Requested` and then
`Creating`. When directory creation is complete (this might take
a few minutes), the status is `Active`.
