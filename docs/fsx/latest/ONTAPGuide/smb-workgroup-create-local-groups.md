# Creating local groups on the SMB server

You can create local groups that can be used for authorizing access to data associated with the SVM over an SMB connection.
You can also assign privileges that define what user rights or capabilities a member of the group has.

Local group functionality is enabled by default when the SVM is created. When you create a local group, you must specify a
name for the group and you must specify the SVM with which to associate the group. You can specify a group name with or without
the local domain name, and you can optionally specify a description for the local group. You cannot add a local group to another
local group.

###### To create a local group on the SMB server

1. create the local group using the
   [**vserver cifs users-and-groups local-group create**](https://docs.netapp.com/us-en/ontap-cli/vserver-cifs-users-and-groups-local-group-create.html "https://docs.netapp.com/us-en/ontap-cli/vserver-cifs-users-and-groups-local-group-create.html")
   ONTAP CLI command.

```
vserver cifs users-and-groups local-group create -vserver `svm_name` -group-name `group_name` [-description `local_group_description`
```

Including a description for the local group is useful. 2. Verify that the group was successfully created:

```
vserver cifs users-and-groups local-group show -vserver `svm_name`
```

The following example creates a local group `SMB_SERVER01\engineering` associated with SVM `svm1`:

```
`FSxIdabcde123456::>` `vserver cifs users-and-groups local-group create -vserver svm1 -group-name SMB_SERVER01\engineering`
```

```
`FSxIdabcde123456::>` `vserver cifs users-and-groups local-group show -vserver svm1`

`Vserver Group Name Description
---------------- ---------------------------- ----------------------------
svm1 BUILTIN\Administrators Built-in Administrators group
svm1 BUILTIN\Backup Operators Backup Operators group
svm1 BUILTIN\Guests Built-in Guests group
svm1 BUILTIN\Power Users Restricted administrative privileges
svm1 BUILTIN\Users All users
svm1 SMB_SERVER01\engineering`
```
