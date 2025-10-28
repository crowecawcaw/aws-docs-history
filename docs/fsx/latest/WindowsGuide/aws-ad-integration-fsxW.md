# Working with Microsoft Active Directory

When you create an FSx for Windows File Server file system, you join it to your Active Directory domain to
provide user authentication and file- and folder-level access control. Amazon FSx works with Microsoft Active Directory
to integrate with your existing Microsoft Windows environments. Amazon FSx provides two options using your FSx for Windows File Server file system
with Active Directory: [Using Amazon FSx with AWS Directory Service for Microsoft Active Directory](fsx-aws-managed-ad.md "fsx-aws-managed-ad.md") and
[Using a self-managed Microsoft Active Directory](self-managed-AD.md "self-managed-AD.md").

Active Directory is the Microsoft directory service used to store information about
objects on the network and make this information easy for administrators and users to find and
use. These objects typically include shared resources such as file servers and network user and
computer accounts.

Your users can then use
their existing user identities in Active Directory to authenticate themselves and access the FSx for Windows File Server
file system. Users can also use their existing identities to control access to individual files
and folders. In addition, you can migrate your existing files and folders along with their
security access control list (ACL) configuration to Amazon FSx without any modifications.

###### Note

Amazon FSx supports [Microsoft
Azure Active Directory Domain Services](https://docs.microsoft.com/en-us/azure/active-directory-domain-services/overview "https://docs.microsoft.com/en-us/azure/active-directory-domain-services/overview"), which you can join to a [Microsoft Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis "https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis").

After you create a joined Active Directory configuration for a file system, you can update
only the following properties:

- Service user credentials
- DNS server IP addresses
  You _cannot_ change the following properties for your joined Microsoft AD after you've created the file system:

- DomainName
- OrganizationalUnitDistinguishedName
- FileSystemAdministratorsGroup
  However, you can create a new file system from a backup and change
  these properties in the new file system's Microsoft Active Directory integration configuration.
  For more information, see [Restoring backups to new file system](using-backups.md#restoring-backups "using-backups.md#restoring-backups").

###### Note

Amazon FSx does not support [Active Directory Connector](../../../directoryservice/latest/admin-guide/directory_ad_connector.md "../../../directoryservice/latest/admin-guide/directory_ad_connector.md") and
[Simple Active Directory](../../../directoryservice/latest/admin-guide/directory_simple_ad.md "../../../directoryservice/latest/admin-guide/directory_simple_ad.md").

Your FSx for Windows File Server may become **Misconfigured** if there is a change in your Active Directory configuration that disrupts the connection to your file system.
To return your file system to the **Available** state, select the **Attempt Recovery** button
in the Amazon FSx console, or use the `StartMisconfiguredStateRecovery` command in the Amazon FSx API or console.
For more information see [File system is in a misconfigured state](misconfigured-ad-config.md "misconfigured-ad-config.md").

###### Topics

- [Using Amazon FSx with AWS Directory Service for Microsoft Active Directory](fsx-aws-managed-ad.md "fsx-aws-managed-ad.md")
- [Using a self-managed Microsoft Active Directory](self-managed-AD.md "self-managed-AD.md")
