# Transfer files to a Windows instance using RDP

You can work with your Windows instance in the same way that you would work with any Windows
server. For example, you can transfer files between a Windows instance and your local
computer using the local file sharing feature of the Microsoft Remote Desktop Connection (RDP)
software. You can access local files on hard disk drives, DVD drives, portable media
drives, and mapped network drives.

To access your local files from your Windows instances, you must enable the local file
sharing feature by mapping the remote session drive to your local drive. The steps are
slightly different depending on whether your local computer operating system is Windows
or macOS X.

For more information about the prerequisites to connect using RDP, see [Prerequisites](connect-rdp.md#rdp-prereqs "connect-rdp.md#rdp-prereqs").

Windows

###### To map the remote session drive to your local drive on your local

Windows computer

1. Open the Remote Desktop Connection client.
2. Choose **Show Options**.
3. Add the instance host name to the **Computer**
   field and username to the **User name** field, as
   follows:
   1. Under **Connection settings**, choose
      **Open...**, and browse to the RDP
      shortcut file that you downloaded from the Amazon EC2 console.
      The file contains the Public IPv4 DNS host name, which
      identifies the instance, and the Administrator user
      name.
   2. Select the file and choose **Open**. The
      **Computer** and **User
      name** fields are populated with the values
      from the RDP shortcut file.
   3. Choose **Save**.

4. Choose the **Local Resources** tab.
5. Under **Local devices and resources**, choose
   **More...**

![RDP Local Resources window.](images/windows-connect-rdp-local-resources.png) 6. Open **Drives** and select the local drive to map
to your Windows instance. 7. Choose **OK**.

![RDP Local devices and resources window.](images/windows-connect-rdp-drives.png) 8. Choose **Connect** to connect to your Windows
instance.

macOS X

###### To map the remote session drive to your local folder on your local

macOS X computer

1. Open the Remote Desktop Connection client.
2. Browse to the RDP file that you downloaded from the Amazon EC2 console
   (when you initially connected to the instance), and drag it onto the
   Remote Desktop Connection client.
3. Right-click the RDP file, and choose **Edit**.
4. Choose the **Folders** tab, and select the
   **Redirect folders** checkbox.

![Microsoft Remote Desktop Edit PC window.](images/mac-map-folder-1.png) 5. Choose the **+** icon at bottom left, browse to
the folder to map, and choose **Open**. Repeat this
step for every folder to map. 6. Choose **Save**. 7. Choose **Connect** to connect to your Windows
instance. You'll be prompted for the password. 8. On the instance, in File Explorer, expand **This PC**, and find the
shared folder from which you can access your local files. In the
following screenshot, the **Desktop** folder on the
local computer was mapped to the remote session drive on the
instance.

![Microsoft Remote Desktop Edit PC window.](images/mac-map-folder-2.png)

For more information on making local devices available to a remote session
on a Mac computer, see [Get started with the macOS client](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-mac "https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-mac").
