# Managing SMB shares

To manage SMB file shares on your Amazon FSx file system, you can use the Microsoft Windows Shared Folders GUI.
The Shared Folders GUI provides a central location for managing all shared folders in
your storage virtual machine (SVM). The following procedures detail how to create, update, and remove your
file shares.

###### Note

You can also manage SMB file shares by using the NetApp System Manager. For more information, see
[Using NetApp System Manager with NetApp Console](managing-resources-ontap-apps.md#netapp-sysmgr-bluexp "managing-resources-ontap-apps.md#netapp-sysmgr-bluexp").

###### To connect shared folders to your Amazon FSx file system

1. Launch your Amazon EC2 instance and connect it to the Microsoft Active Directory
   that your Amazon FSx file system is joined to. To do this, choose one of the
   following procedures from the _AWS Directory Service Administration Guide_:
   - [Seamlessly join a
     Windows EC2 instance](../../../directoryservice/latest/admin-guide/launching_instance.md "../../../directoryservice/latest/admin-guide/launching_instance.md")
   - [Manually join a
     Windows instance](../../../directoryservice/latest/admin-guide/join_windows_instance.md "../../../directoryservice/latest/admin-guide/join_windows_instance.md")

2. Connect to your instance as a user that is a member of the file system
   administrators group. For more information, see [Connecting to
   Your Windows Instance](../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md "../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md") in the
   _Amazon EC2 User Guide_.
3. Open the **Start** menu and run
   **fsmgmt.msc** using **Run As
   Administrator**. Doing this opens the Shared Folders GUI
   tool.
4. For **Action**, choose **Connect to another
   computer**.
5. For **Another computer**, enter the DNS name for your storage
   virtual machine (SVM), for example
   `netbios_name.corp.example.com`.

To find your SVM's DNS name on the Amazon FSx console, choose
**Storage virtual machines**, choose your SVM, and then
scroll down to **Endpoints** until you find **SMB DNS
name**. You can also get the DNS name in the response of the [DescribeStorageVirtualMachines](../APIReference/API_DescribeStorageVirtualMachines.md "../APIReference/API_DescribeStorageVirtualMachines.md") API operation. 6. Choose **OK**. An entry for your Amazon FSx file system then
appears in the list for the Shared Folders tool.
Now that Shared Folders is connected to your Amazon FSx file system, you can manage the
Windows file shares on the file system with the following actions:

###### Note

We recommend that you locate your SMB shares on a volume other than your root
volume.

- **Create a new file share** – In the Shared
  Folders tool, choose **Shares** in the left pane to see the
  active shares for your Amazon FSx file system. Volumes are shown mounted on the path
  chosen during volume creation. Choose **New Share** and
  complete the Create a Shared Folder wizard.

You have to create the local folder prior to creating the new file share. You
can do so as follows:

    + Using the Shared Folders tool: choose **Browse** when
     specifying a local folder path, choose **Make new
     folder** to create the local folder.
    + Using command line:



    ```
    New-Item -Type Directory -Path \\`netbios_name.corp.example.com`\C$`volume_path`\`MyNewFolder`
    ```

- **Modify a file share** – In the Shared
  Folders tool, open the context (right-click) menu for the file share that you
  want to modify in the right pane, and choose **Properties**.
  Modify the properties and choose **OK**.
- **Remove a file share** – In the Shared
  Folders tool, open the context (right-click) menu for the file share that you
  want to remove in the right pane, and then choose **Stop
  Sharing**.

###### Note

Removing file shares from the GUI is possible only if you connected to
**fsmgmt.msc** using the DNS name of the Amazon FSx file
system. If you connected using the IP address or DNS alias name of the file
system, the **Stop Sharing** option won't work and the
file share isn't removed.
