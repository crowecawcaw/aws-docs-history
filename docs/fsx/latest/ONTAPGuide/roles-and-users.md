# ONTAP roles and users

NetApp ONTAP includes a robust and extensible role-based access control (RBAC) capability.
ONTAP roles define user capabilities and privileges when using the ONTAP CLI and REST API.
Each role defines a different level of administrative capabilities and privileges. You assign roles to
users for the purpose of controlling their access to FSx for ONTAP resources when using the ONTAP REST API and CLI.
There are ONTAP roles available separately for FSx for ONTAP file system users and storage virtual machine (SVM) users.

When you create an FSx for ONTAP file system, a default ONTAP user is created at the file system level and at
the SVM level. You can create additional file system and SVM users, and you can create additional SVM roles to meet the needs of
your organization. This chapters explains ONTAP users and roles, and provides detailed procedures for creating additional
users and SVM roles.

## File system administrator roles and users

The default ONTAP file system user is `fsxadmin`, which has the `fsxadmin`
role assigned to it. There are two predefined roles that you can assign to file system users, listed as follows:

- **`fsxadmin`**—Administrators with this role have unrestricted
  rights in the ONTAP system. They can configure all file system and SVM-level resources available
  on FSx for ONTAP file systems.
- **`fsxadmin-readonly`**—Administrators
  with this role can view everything at the file system level but can't make any changes.

This role is well-suited for use with monitoring applications such as NetApp Harvest
because it has read-only access to all available resources and their properties, but cannot make any changes to them.

You can create additional file system users and assign them either the `fsxadmin` or
`fsxadmin-readonly` role. You can't create new roles or modify the existing roles. For more information,
see [Creating new ONTAP users for file system and SVM administration](#file-system-roles-and-users "#file-system-roles-and-users").

The following table describes the level of access that file system administrator roles
have for ONTAP CLI and REST API commands and command directories.

| Role name           | Level of access                                          | To the following commands or command directories                                                   |
| ------------------- | -------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `fsxadmin`          | all                                                      | All command directories available in FSx for ONTAP                                                 |
| `fsxadmin-readonly` | all                                                      | `security login password`<br>For managing own user account local password and key information only |
| none                | `security`                                               |
| readonly            | All other command directories available in FSx for ONTAP |

## SVM administrator roles and users

Each SVM has a separate authentication domain and can be managed
independently by its own administrators. For each SVM on your file system, the default user
is _vsadmin_, which has the `vsadmin` role assigned by default.
In addition to the `vsadmin` role, there are other predefined SVM roles that provide
scoped down permissions that you can assign to SVM users. You can also create custom roles
that provide the level of access control that meet your organization's needs.

The predefined roles for SVM administrators and their capabilities are as follows:

| Role name          | Capabilities                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `vsadmin`          | • Manage your user account, local password, and key information<br>• Manage volumes, except for volume moves<br>• Manage quotas, qtrees, Snapshot copies, and files<br>• Manage LUNs<br>• Perform SnapLock operations, except for privileged delete<br>• Configure protocols: NFS, SMB, and iSCSI<br>• Configure services: DNS, LDAP, and NIS<br>• Monitor jobs<br>• Monitor network connections and the network interface<br>• Monitor the health of the SVM |
| `vsadmin-volume`   | • Manage your user account, local password, and key information<br>• Manage volumes, including volume moves<br>• Manage quotas, qtrees, Snapshot copies, and files<br>• Manage LUNs<br>• Configure protocols: NFS, SMB, and iSCSI<br>• Configure services: DNS, LDAP, and NIS<br>• Monitor the network interface<br>• Monitor the health of the SVM                                                                                                           |
| `vsadmin-protocol` | • Manage your user account, local password, and key information<br>• Manage LUNs<br>• Configure protocols: NFS, SMB, and iSCSI<br>• Configure services: DNS, LDAP, and NIS<br>• Monitor network interface<br>• Monitor the health of the SVM                                                                                                                                                                                                                  |
| `vsadmin-backup`   | • Manage your user account, local password, and key information<br>• Manage NDMP operations<br>• Make a restored volume read/write<br>• Manage SnapMirror relationships and Snapshot copies<br>• View volumes and network information                                                                                                                                                                                                                         |
| `vsadmin-snaplock` | • Manage your user account, local password, and key information<br>• Manage volumes, except for volume moves<br>• Manage quotas, qtrees, Snapshot copies, and files<br>• Perform SnapLock operations, including privileged delete<br>• Configure protocols: NFS and SMB<br>• Configure services: DNS, LDAP, and NIS<br>• Monitor jobs<br>• Monitor network connections and the network interface                                                              |
| `vsadmin-readonly` | • Manage your user account, local password, and key information<br>• Monitor the health of the SVM<br>• Monitor the network interface<br>• View volumes and LUNs<br>• View services and protocols                                                                                                                                                                                                                                                             |

For more information on how to create a new SVM role, see [Creating SVM roles](creating-new-svm-roles.md "creating-new-svm-roles.md").

## Using Active Directory to authenticate ONTAP users

You can authenticate Windows Active Directory domain users' access to an FSx for ONTAP file system and SVM.
You must do the following tasks before Active Directory accounts can access your file system:

- You need configure Active Directory domain controller access to the SVM.

The SVM you use to configure as a gateway or tunnel for Active Directory domain controller access must either have CIFS enabled, be joined to an Active Directory,
or both. If you are not enabling CIFS and only joining the tunnel SVM to an Active Directory, ensure that the SVM is joined to your Active Directory.
For more information, see [How joining SVMs to Microsoft Active Directory works](self-managed-AD-join.md "self-managed-AD-join.md").

- You need to enable an Active Directory domain user account to access the file system.

You can use either password authentication or SSH public key authentication for Windows domain users accessing the
ONTAP CLI or REST API.

For procedures describing how to use for configuring Active Directory authentication for file system and SVM administrators, see
[Configuring Active Directory authentication for ONTAP users](set-up-ad-auth.md "set-up-ad-auth.md").

## Creating new ONTAP users for file system and SVM administration

Each ONTAP user is associated with an SVM or the file system. File system users with
the `fsxadmin` role can create new SVM roles and users by using the
[`security login create`](../../../docs.netapp.com/us-en/ontap-cli-9141/security-login-create.md "../../../docs.netapp.com/us-en/ontap-cli-9141/security-login-create.md")
ONTAP CLI command.

The `security login create` command creates a login method for the management utility.
A login method consists of a user name, an application (access method), and an authentication method.
A user name can be associated with multiple applications. It can optionally include an access-control
role name. If an Active Directory, LDAP, or NIS group name is used, then the login method gives access
to users belonging to the specified group. If the user is a member of multiple groups provisioned in
the security login table, then the user will get access to a combined list of the commands authorized
for the individual groups.

For information describing how to create a new ONTAP user, see [Creating ONTAP users](create-new-ontap-users.md "create-new-ontap-users.md").

###### Topics

- [Creating ONTAP users](create-new-ontap-users.md "create-new-ontap-users.md")
- [Creating SVM roles](creating-new-svm-roles.md "creating-new-svm-roles.md")
- [Configuring Active Directory authentication for ONTAP users](set-up-ad-auth.md "set-up-ad-auth.md")
- [Configuring public key authentication](public-key-auth.md "public-key-auth.md")
- [Updating password requirements for file system and SVM roles](update-password-requirements.md "update-password-requirements.md")
- [Updating the fsxadmin account password fails](updating-admin-password.md "updating-admin-password.md")
