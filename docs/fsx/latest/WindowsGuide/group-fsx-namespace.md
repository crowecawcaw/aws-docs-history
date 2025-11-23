# Group multiple file systems under a single namespace

In this procedure, you will create a single domain-based namespace (`example.com\corp`) on two namespace
servers, in order to consolidate file shares stored on multiple FSx for Windows file systems (finance, marketing,
sales, home_directories). You will also set up four file shares under the namespace, each transparently
redirecting users to shares hosted on separate FSx for Windows file systems. This enables your users to access file shares using a common namespace instead of
having to specify the DNS names for each of the file systems hosting the file shares.

###### Note

Amazon FSx cannot be added to the root of the DFS share path.

###### To group multiple file systems into a common DFS namespace

1. If you don't already have DFS Namespace servers running, you can launch a pair of highly
   available DFS Namespace servers using the [setup-DFSN-servers.template](https://solution-references.s3.amazonaws.com/fsx/dfs/setup-DFSN-servers.template "https://solution-references.s3.amazonaws.com/fsx/dfs/setup-DFSN-servers.template") CloudFormation template. For more information on creating an CloudFormation
   stack, see [Creating a Stack on the AWS
   CloudFormation Console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md") in the _AWS CloudFormation User Guide_.
2. Connect to one of the DFS Namespace servers launched in the previous step as a user in the
   **AWS Delegated Administrators** group. For more information, see [Connecting to Your Windows
   Instance](../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md "../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md") in the _Amazon EC2 User Guide_.
3. Access the DFS Management Console by opening. Open the **Start** menu and run
   **dfsmgmt.msc**. This opens the DFS Management GUI tool.
4. Choose **Action** then **New Namespace**, type in the
   computer name of the first DFS Namespace server you launched for **Server**
   and choose **Next**.
5. For **Name**, type in the namespace you're creating (for example,
   **corp**).
6. Choose **Edit Settings** and set the appropriate permissions based on
   your requirements. Choose **Next**.
7. Leave the default **Domain-based namespace** option selected, leave the
   **Enable Windows Server 2008 mode** option selected, and choose
   **Next**.

###### Note

Windows Server 2008 mode is the latest available option for Namespaces. 8. Review the namespace settings and choose **Create**. 9. With the newly created namespace selected under **Namespaces** in the
navigation bar, choose **Action** then **Add Namespace
Server**. 10. Type in the computer name of the second DFS Namespace server you launched for
**Namespace server**. 11. Choose **Edit Settings**, set the appropriate permissions based on your
requirements, and choose **OK**. 12. Open the context (right-click) menu for the namespace you just created, choose
**New Folder**, type in the name of the folder (for example,
`finance` for **Name**, and choose
**OK**. 13. Type in the DNS name of the file share that you want the DFS Namespace folder to point to
in UNC format (for example, `\\fs-0123456789abcdef0.example.com\finance`)
for **Path to folder target** and choose **OK**. 14. If the share doesn't exist:

    1. Choose **Yes** to create it.
    2. From the **Create Share** dialog, choose
     **Browse**.
    3. Choose an existing folder, or create a new folder under **D$**, and
     choose **OK**.
    4. Set the appropriate share permissions, and choose **OK**.

15. From the **New Folder** dialog, choose **OK**. The new
    folder will be created under the namespace.
16. Repeat the last four steps for other folders you want to share under the same
    namespace.
