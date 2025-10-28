# Setting the maximum amount of shadow copy storage

You define the maximum amount of storage that
shadow copies can consume on a file system using the `Set-FsxShadowStorage` custom
PowerShell command. You can specify the maximum size that shadow copies can grow to by using either the
`-Maxsize` or the `-Default` parameters. Using `Default` sets the maximum
to 10% of the file system's storage capacity. You cannot specify the `-Maxsize` and
`-Default` parameters in the same command.

Using `-Maxsize`, you can define shadow copy storage as follows:

- In bytes: `Set-FsxShadowStorage -Maxsize 2500000000`
- In kilobytes, megabytes, gigabytes, or other units: `Set-FsxShadowStorage -Maxsize
(2500MB)` or `Set-FsxShadowStorage -Maxsize (2.5GB)`
- As a percentage of the overall storage: `Set-FsxShadowStorage -Maxsize "20%"`
- As unbounded: `Set-FsxShadowStorage -Maxsize "UNBOUNDED"`
  Use `-Default` to set shadow storage to use up to 10 percent of the file system:
  `Set-FsxShadowStorage -Default`. To learn more about using the default option, see
  [Configuring shadow copies to use the default storage and schedule](setting-up-fsx-shadow-copies.md "setting-up-fsx-shadow-copies.md").

###### To set the amount of shadow copy storage on an FSx for Windows File Server file system

1. Connect to a compute instance
   that has network connectivity with your file system as a user that is a member of the file system administrators
   group. In AWS Managed Microsoft AD, that group is **AWS Delegated FSx
   Administrators**. In your self-managed Microsoft AD, that group is
   **Domain Admins** or the custom group that you specified for
   administration when you created your file system. For more information, see [Connecting to Your Windows
   Instance](../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md "../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md") in the _Amazon EC2 User Guide_.
2. Open a Windows PowerShell window on the compute instance.
3. Use the following command to open a remote PowerShell session on your Amazon FSx file system.
   Replace
   `FSxFileSystem-Remote-PowerShell-Endpoint`
   with the Windows Remote PowerShell endpoint of file system that you want to administer.
   You can find the Windows Remote PowerShell endpoint in the Amazon FSx console, in the **Network & Security** section of the file system details screen,
   or in the response of the `DescribeFileSystem` API operation.

```
`PS C:\Users\delegateadmin>` enter-pssession -computername `FSxFileSystem-Remote-PowerShell-Endpoint` -configurationname fsxremoteadmin
```

4. Verify that shadow copy storage is not already configured on the file system using the following command.

```
`[fs-1234567890abcef12]: PS>`Get-FsxShadowStorage
No Fsx Shadow Storage Configured
```

5. Set the amount of shadow storage to 10 percent of the volume and the maximum number of shadow copes to 20 using the
   `-Default` option.

```
`[fs-1234567890abcef12]: PS>`Set-FsxShadowStorage -Default
FSx Shadow Storage Configuration

AllocatedSpace UsedSpace    MaxSpace MaxShadowCopyNumber
-------------- ---------    -------- -------------------
             0         0 32530536858                  20

```

You can limit the maximum number of shadow copies allowed on your file system
by using the `Set-FSxShadowStorage` command with the `-MaxShadowCopyNumber` parameter and specifying a value from 1-500.
By default, the maximum number of shadow copies is set to 20, as recommended for by Microsoft for active workloads.
