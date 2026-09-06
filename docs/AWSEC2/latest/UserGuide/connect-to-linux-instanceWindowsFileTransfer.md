

# Transfer files to a Windows instance using RDP
<a name="connect-to-linux-instanceWindowsFileTransfer"></a>

You can work with your Windows instance in the same way that you would work with any Windows server. For example, you can transfer files between a Windows instance and your local computer using the local file sharing feature of the Microsoft Remote Desktop Connection (RDP) software. You can access local files on hard disk drives, DVD drives, portable media drives, and mapped network drives.

To access your local files from your Windows instances, you must enable the local file sharing feature by mapping the remote session drive to your local drive. The steps are slightly different depending on whether your local computer operating system is Windows or macOS X.

For more information about the prerequisites to connect using RDP, see [Prerequisites](connect-rdp.md#rdp-prereqs).

------
#### [ Windows ]

**To map the remote session drive to your local drive on your local Windows computer**

1. Open the Remote Desktop Connection client.

1. Choose **Show Options**.

1. Add the instance host name to the **Computer** field and username to the **User name** field, as follows:

   1. Under **Connection settings**, choose **Open...**, and browse to the RDP shortcut file that you downloaded from the Amazon EC2 console. The file contains the Public IPv4 DNS host name, which identifies the instance, and the Administrator user name.

   1. Select the file and choose **Open**. The **Computer** and **User name** fields are populated with the values from the RDP shortcut file.

   1. Choose **Save**.

1. Choose the **Local Resources** tab.

1. Under **Local devices and resources**, choose **More...**  
![RDP Local Resources window.](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/windows-connect-rdp-local-resources.png)

1. Open **Drives** and select the local drive to map to your Windows instance.

1. Choose **OK**.  
![RDP Local devices and resources window.](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/windows-connect-rdp-drives.png)

1. Choose **Connect** to connect to your Windows instance.

------
#### [ macOS X ]

**To map the remote session drive to your local folder on your local macOS X computer**

1. Open the Remote Desktop Connection client.

1. Browse to the RDP file that you downloaded from the Amazon EC2 console (when you initially connected to the instance), and drag it onto the Remote Desktop Connection client.

1. Open the context (right-click) menu for the RDP file, and choose **Edit**. 

1. Choose the **Folders** tab, and select the **Redirect folders** checkbox.  
![Microsoft Remote Desktop Edit PC window.](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/mac-map-folder-1.png)

1. Choose the **\+** icon at bottom left, browse to the folder to map, and choose **Open**. Repeat this step for every folder to map.

1. Choose **Save**.

1. Choose **Connect** to connect to your Windows instance. You'll be prompted for the password.

1. On the instance, in File Explorer, expand **This PC**, and find the shared folder from which you can access your local files. In the following screenshot, the **Desktop** folder on the local computer was mapped to the remote session drive on the instance.  
![Microsoft Remote Desktop Edit PC window.](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/mac-map-folder-2.png)

For more information on making local devices available to a remote session on a Mac computer, see [Get started with the macOS client](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-mac).

------