# Mapping a file share on an Amazon EC2 Windows instance

You can map a file share on an EC2 Windows instance to access your FSx for Windows File Server file system by using the Windows File Explorer
or the command prompt.

1. Launch the EC2 Windows instance and connect it to the Microsoft Active Directory
   that you joined your Amazon FSx file system to. To do this, choose one of the
   following procedures from the _AWS Directory Service Administration Guide_:
   - [Seamlessly join a Windows
     EC2 instance](../../../directoryservice/latest/admin-guide/launching_instance.md "../../../directoryservice/latest/admin-guide/launching_instance.md")
   - [Manually join a Windows
     instance](../../../directoryservice/latest/admin-guide/join_windows_instance.md "../../../directoryservice/latest/admin-guide/join_windows_instance.md")

2. Connect to your EC2 Windows instance. For more information, see [Connecting to your
   Windows instance](../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md "../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md") in the _Amazon EC2 User Guide_.
3. After you're connected, open File Explorer.
4. In the navigation pane, open the context (right-click) menu for
   **Network**, and choose **Map Network
   Drive**.
5. For **Drive**, choose a drive letter.
6. For **Folder**, enter either the file system's DNS name or a DNS
   alias associated with the file system, and the share name.

###### Important

Using an IP address instead of the DNS name could result in unavailability
during the failover process of the Multi-AZ file system. Also, DNS names or associated
DNS aliases are required for Kerberos-based authentication in Multi-AZ and Single-AZ file systems.

You can find the file system's DNS name and any associated DNS aliases on the
[Amazon FSx console](https://console.aws.amazon.com/fsx "https://console.aws.amazon.com/fsx") by choosing
**Windows File Server**, **Network &
security**. Or, you can find them in the response of the [CreateFileSystem](../APIReference/API_CreateFileSystem.md "../APIReference/API_CreateFileSystem.md") or [DescribeFileSystems](../APIReference/API_DescribeFileSystems.md "../APIReference/API_DescribeFileSystems.md") API operation. For more information about using DNS
aliases, see [Managing DNS aliases](managing-dns-aliases.md "managing-dns-aliases.md").

    * For a Single-AZ file system joined to an AWS Managed Microsoft Active Directory, the DNS name looks like the
     following.



    ```
    fs-0123456789abcdef0.`ad-domain`.com
    ```
    * For a Single-AZ file system joined to a self-managed Active Directory, and any Multi-AZ file
     system, the DNS name looks like the following.



    ```
    amznfsxaa11bb22.`ad-domain`.com
    ```

For example, to use a Single-AZ file system's DNS name, enter the following for
**Folder**.

```
\\fs-0123456789abcdef0.`ad-domain`.com\share
```

To use a Multi-AZ file system's DNS name, enter the following for
**Folder**.

```
\\amznfsxaa11bb22.`ad-domain`.com\share
```

To use a DNS alias associated with the file system, enter the following for
**Folder**.

```
\\`fqdn-dns-alias`\share
```

7. Choose an option for **Reconnect at sign-in**, which indicates
   whether the file share should reconnect at sign-in, and then choose
   **Finish**.
1. Launch the EC2 Windows instance and connect it to the Microsoft Active Directory

that you joined your Amazon FSx file system to. To do this, choose one of the
following procedures from the _AWS Directory Service Administration Guide_:

    * [Seamlessly join a Windows
     EC2 instance](../../../directoryservice/latest/admin-guide/launching_instance.md "../../../directoryservice/latest/admin-guide/launching_instance.md")
    * [Manually join a Windows
     instance](../../../directoryservice/latest/admin-guide/join_windows_instance.md "../../../directoryservice/latest/admin-guide/join_windows_instance.md")

2.  Connect to your EC2 Windows instance as a user in your AWS Managed Microsoft AD directory. For
    more information, see [Connecting to your
    Windows instance](../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md "../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md") in the _Amazon EC2 User Guide_.
3.  After you're connected, open a command prompt window.
4.  Mount the file share using a drive letter of your choice, the file system's DNS
    name, and the share name. You can find the DNS name using the [Amazon FSx console](https://console.aws.amazon.com/fsx "https://console.aws.amazon.com/fsx") by choosing **Windows File
    Server**, **Network & security**. Or, you can find
    them in the response of the `CreateFileSystem` or
    `DescribeFileSystems` API operation.

        * For a Single-AZ file system joined to an AWS Managed Microsoft Active Directory, the DNS name looks like the
         following.



        ```
        fs-0123456789abcdef0.`ad-domain`.com
        ```
        * For a Single-AZ file system joined to a self-managed Active Directory, and any Multi-AZ file
         system, the DNS name looks like the following.



        ```
        amznfsxaa11bb22.`ad-domain`.com
        ```

    The following is an example command to mount the file share.

```
`$` net use H: \\amzfsxaa11bb22.`ad-domain`.com\share /persistent:yes
```

Instead of the `net use` command, you can also use any supported
PowerShell command to mount a file share.
