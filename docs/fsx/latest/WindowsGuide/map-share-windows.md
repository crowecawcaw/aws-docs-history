

# Mapping a file share on an Amazon EC2 Windows instance
<a name="map-share-windows"></a>

You can map a file share on an EC2 Windows instance to access your FSx for Windows File Server file system by using the Windows File Explorer or the command prompt.

## To map a file share on an Amazon EC2 Windows instance (File Explorer)
<a name="map-file-share-ec2-win-comm"></a>

1. Launch the EC2 Windows instance and connect it to the Microsoft Active Directory that you joined your Amazon FSx file system to. To do this, choose one of the following procedures from the *AWS Directory Service Administration Guide*:
   + [Seamlessly join a Windows EC2 instance](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/launching_instance.html)
   + [Manually join a Windows instance](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/join_windows_instance.html)

1. Connect to your EC2 Windows instance. For more information, see [Connecting to your Windows instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.html) in the *Amazon EC2 User Guide*.

1. After you're connected, open File Explorer.

1. In the navigation pane, open the context (right-click) menu for **Network**, and choose **Map Network Drive**.

1. For **Drive**, choose a drive letter.

1. For **Folder**, enter either the file system's DNS name or a DNS alias associated with the file system, and the share name. 
**Important**  
Using an IP address instead of the DNS name could result in unavailability during the failover process of the Multi-AZ file system. Also, DNS names or associated DNS aliases are required for Kerberos-based authentication in Multi-AZ and Single-AZ file systems. 

   You can find the file system's DNS name and any associated DNS aliases on the [Amazon FSx console](https://console.aws.amazon.com/fsx) by choosing **Windows File Server**, **Network & security**. Or, you can find them in the response of the [CreateFileSystem](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateFileSystem.html) or [DescribeFileSystems](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileSystems.html) API operation. For more information about using DNS aliases, see [Managing DNS aliases](managing-dns-aliases.md).
   + For a Single-AZ file system joined to an AWS Managed Microsoft Active Directory, the DNS name looks like the following.

     ```
     fs-0123456789abcdef0.{{ad-domain}}.com
     ```
   + For a Single-AZ file system joined to a self-managed Active Directory, and any Multi-AZ file system, the DNS name looks like the following.

     ```
     amznfsxaa11bb22.{{ad-domain}}.com
     ```

   For example, to use a Single-AZ file system's DNS name, enter the following for **Folder**.

   ```
   \\fs-0123456789abcdef0.{{ad-domain}}.com\share
   ```

   To use a Multi-AZ file system's DNS name, enter the following for **Folder**.

   ```
   \\amznfsxaa11bb22.{{ad-domain}}.com\share
   ```

   To use a DNS alias associated with the file system, enter the following for **Folder**.

   ```
   \\{{fqdn-dns-alias}}\share
   ```

1. Choose an option for **Reconnect at sign-in**, which indicates whether the file share should reconnect at sign-in, and then choose **Finish**.

## To map a file share on an Amazon EC2 Windows instance (command prompt)
<a name="map-file-share-ec2-win-command"></a>

1. Launch the EC2 Windows instance and connect it to the Microsoft Active Directory that you joined your Amazon FSx file system to. To do this, choose one of the following procedures from the *AWS Directory Service Administration Guide*:
   + [Seamlessly join a Windows EC2 instance](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/launching_instance.html)
   + [Manually join a Windows instance](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/join_windows_instance.html)

1. Connect to your EC2 Windows instance as a user in your AWS Managed Microsoft AD directory. For more information, see [Connecting to your Windows instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.html) in the *Amazon EC2 User Guide*.

1. After you're connected, open a command prompt window.

1. Mount the file share using a drive letter of your choice, the file system's DNS name, and the share name. You can find the DNS name using the [Amazon FSx console](https://console.aws.amazon.com/fsx) by choosing **Windows File Server**, **Network & security**. Or, you can find them in the response of the `CreateFileSystem` or `DescribeFileSystems` API operation.
   + For a Single-AZ file system joined to an AWS Managed Microsoft Active Directory, the DNS name looks like the following.

     ```
     fs-0123456789abcdef0.{{ad-domain}}.com
     ```
   + For a Single-AZ file system joined to a self-managed Active Directory, and any Multi-AZ file system, the DNS name looks like the following.

     ```
     amznfsxaa11bb22.{{ad-domain}}.com
     ```

   The following is an example command to mount the file share.

   ```
   $ net use H: \\amzfsxaa11bb22.{{ad-domain}}.com\share /persistent:yes
   ```

   Instead of the `net use` command, you can also use any supported PowerShell command to mount a file share.

  