

# Mounting a file share on an Amazon EC2 Mac instance
<a name="map-share-mac"></a>

You can mount a file share on an Amazon EC2 Mac instance that is either joined to your Active Directory or not joined to access your FSx for Windows File Server file system. If the instance is not joined to your Active Directory, be sure to update the DHCP options set for the Amazon Virtual Private Cloud (Amazon VPC) in which the instance resides to include the DNS name servers for your Active Directory domain. Then relaunch the instance.

## To mount a file share on an Amazon EC2 Mac instance (GUI)
<a name="map-file-share-ec2-mac-vnc"></a>

1. Launch the EC2 Mac instance. To do this, choose one of the following procedures from the *Amazon EC2 User Guide*:
   + [Launch a Mac instance using the console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html#mac-instance-launch)
   + [Launch a Mac instance using the AWS CLI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html#mac-instance-launch-cli)

1. Connect to your EC2 Mac instance using Virtual Network Computing (VNC). For more information, see [Connect to your instance using VNC](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html#mac-instance-vnc) in the *Amazon EC2 User Guide*.

1. On your EC2 Mac instance, connect to your Amazon FSx file share, as follows:

   1. Open Finder, choose **Go**, and then choose **Connect to Server**.

   1. In the **Connect to Server** dialog box, enter either the file system's DNS name or a DNS alias associated with the file system, and the share name. Then choose **Connect**. 

      You can find the file system's DNS name and any associated DNS aliases on the [Amazon FSx console](https://console.aws.amazon.com/fsx) by choosing **Windows File Server**, **Network & security**. Or, you can find them in the response of the [CreateFileSystem](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateFileSystem.html) or [DescribeFileSystems](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileSystems.html) API operation. For more information about using DNS aliases, see [Managing DNS aliases](managing-dns-aliases.md).   
![Mac connection screenshot showing the DNS and share names of the file system pane.](http://docs.aws.amazon.com/fsx/latest/WindowsGuide/images/mac-instance-connect1.png)

   1. On the next screen, choose **Connect** to continue.

   1. Enter your Microsoft Active Directory (AD) credentials for the Amazon FSx service account, as shown in the following example. Then choose **Connect**.  
![Mac connection screenshot showing how to enter user credentials for the file system pane.](http://docs.aws.amazon.com/fsx/latest/WindowsGuide/images/mac-instance-connect2.png)

   1. If the connection is successful, you can see the Amazon FSx share, under **Locations** in your Finder window.

## To mount a file share on an Amazon EC2 Mac instance (command line)
<a name="map-file-share-ec2-mac-command"></a>

1. Launch the EC2 Mac instance. To do this, choose one of the following procedures from the *Amazon EC2 User Guide*:
   + [Launch a Mac instance using the console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html#mac-instance-launch)
   + [Launch a Mac instance using the AWS CLI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html#mac-instance-launch-cli)

1. Connect to your EC2 Mac instance using Virtual Network Computing (VNC). For more information, see [Connect to your instance using VNC](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html#mac-instance-vnc) in the *Amazon EC2 User Guide*.

1. Mount the file share with the following command.

   ```
   mount_smbfs //{{file_system_dns_name}}/{{file_share mount_point}}
   ```

   You can find the DNS name on the [Amazon FSx console](https://console.aws.amazon.com/fsx) by choosing **Windows File Server**, **Network & security**. Or, you can find them in the response of the `CreateFileSystem` or `DescribeFileSystems` API operation.
   + For a Single-AZ file system joined to an AWS Managed Microsoft Active Directory, the DNS name looks like the following.

     ```
     fs-0123456789abcdef0.{{ad-domain}}.com
     ```
   + For a Single-AZ file system joined to a self-managed Active Directory, and any Multi-AZ file system, the DNS name looks like the following.

     ```
     amznfsxaa11bb22.{{ad-domain}}.com
     ```

   The mount command used in this procedure does the following at the given points:
   + `//{{file_system_dns_name}}/{{file_share}}` – Specifies the DNS name and share of the file system to mount.
   + {{mount\_point}} – The directory on the EC2 instance that you are mounting the file system to.

  