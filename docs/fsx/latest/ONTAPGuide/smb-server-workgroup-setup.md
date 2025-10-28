# Setting up an SMB server in a workgroup

You can configure a Server Message Block (SMB) server in a workgroup as an alternative to joining an [SVM to a Microsoft Active Directory](ad-integration-ontap.md "ad-integration-ontap.md")
when the Microsoft Active Directory domain infrastructure is not available. A workgroup is a peer-to-peer network that uses the SMB protocol,
and has only local accounts and groups.

The process of setting up an SMB server as a member in a workgroup consists of the following:

- Creating the SMB server on a storage virtual machine (SVM).
- Creating local users and groups.
- Adding local users or groups as members of the workgroup.
  Keep in mind that SMB servers in workgroup mode do not support the following SMB features:

- SMB3 Witness protocol
- SMB3 CA shares
- SQL over SMB
- Folder Redirection
- Roaming Profiles
- Group Policy Object (GPO)
- Volume Snapshot Service (VSS)
  Also, an SMB server in workgroup mode supports only NTLM authentication and does not support Kerberos authentication.

The following procedures take you through the process of setting up an SMB server on an SVM in a workgroup, create local accounts,
and adding these accounts to the workgroup membership. You will use the NetApp ONTAP CLI from either the file system or
SVM management interface to implement these procedures. For more information, see [Using the NetApp ONTAP CLI](managing-resources-ontap-apps.md#netapp-ontap-cli "managing-resources-ontap-apps.md#netapp-ontap-cli").

###### Topics

- [Creating an SMB server in a workgroup](create-smb-server-workgroup.md "create-smb-server-workgroup.md")
- [Creating a local user account on the SMB server](smb-workgroup-create-local-accounts.md "smb-workgroup-create-local-accounts.md")
- [Creating local groups on the SMB server](smb-workgroup-create-local-groups.md "smb-workgroup-create-local-groups.md")
- [Adding local users to the local group](smb-workgroup-add-users-to-group.md "smb-workgroup-add-users-to-group.md")
