# Starting an Amazon FSx remote PowerShell session

This topic provides instructions for starting a long-lived remote PowerShell session on your FSx for Windows File Server file server.

###### To start a remote PowerShell session on your file system

1. Connect to a compute instance that has network connectivity with your file system as
   a user that is a member of the delegated FSx Administrators Group that you chose when
   you created the file system.
2. Open a Windows PowerShell window on the compute instance.
3. In the PowerShell, enter the following command to open a long-lived remote session on your Amazon FSx
   file system. Replace `Remote-PowerShell-Endpoint`
   with the Windows Remote PowerShell endpoint of file system that you want to administer. Use
   `FsxRemoteAdmin` as the session configuration name.

```
`PS C:\Users\delegateadmin>` `enter-pssession -ComputerName `Remote-PowerShell-Endpoint` -ConfigurationName FsxRemoteAdmin`
``[fs-0123456789abcdef0]: PS>``
```

If your instance is not part of the Amazon FSx Active Directory domain, you are prompted to enter
user credentials in a pop-up. Enter the credentials of the user that is a member
of the FSx Administrators Group. If your instance is joined to the domain, you will not
be asked for credentials.

###### Important

The Windows Remote PowerShell endpoint might change if you are using self-managed Active Directory configuration and change the service account without
proper Active Directory Group Policy settings. For more information, see [Changing the Amazon FSx service account](changing-ad-service-account.md "changing-ad-service-account.md") for more details.
