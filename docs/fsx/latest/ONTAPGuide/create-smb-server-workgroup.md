# Creating an SMB server in a workgroup

You can use the [**vserver cifs create**](https://docs.netapp.com/us-en/ontap-cli/vserver-cifs-create.html "https://docs.netapp.com/us-en/ontap-cli/vserver-cifs-create.html") ONTAP CLI
command to create an SMB server on the SVM and specify the workgroup to which it belongs.

## Before you begin

The SVM and volumes (and interfaces) that you are using to serve data must have been configured to allow the SMB protocol.

The LIFs must be able to connect to the DNS servers that are configured on the SVM. A CIFS license may be required on the file system, however
a CIFS license is not required if the SMB server will be used for authentication only.

###### To create an SMB server in a workgroup

1. To access the ONTAP CLI, establish an SSH session on the management port of the
   Amazon FSx for NetApp ONTAP file system or SVM by running the following command. Replace
   `management_endpoint_ip` with the IP address of the file system's
   management port.

```
`[~]$` `ssh fsxadmin@`management_endpoint_ip``
```

For more information, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 2. Create the SMB server in a workgroup:

```
`FSxIdabcde123456::>` vserver cifs create -vserver `vserver_name` -cifs-server `cifs_server_name` -workgroup `workgroup_name` [-comment `workgroup_description`]
```

The following command creates the SMB server `smb_server01` in the workgroup `workgroup01`:

```
`FSxIdabcde123456::>` vserver cifs create -vserver svm1 -cifs-server SMB_SERVER01 -workgroup workgroup01
```

If you are connected to management port of the SVM, you do not need to specify a `-vserver`. 3. Verify the SMB server configuration by using the `vserver cifs show` command.

In the following example, the command output shows that a SMB server named `smb_server01` was created on SVM `svm1` in the workgroup
`workgroup01`:

```
`FSxIdabcde123456::>` `vserver cifs show -vserver svm1`

                                               `Vserver: svm1
 CIFS Server NetBIOS Name: SMB_SERVER01
 NetBIOS Domain/Workgroup Name: workgroup01
 Fully Qualified Domain Name: -
 Organizational Unit: -
 Default Site Used by LIFs Without Site Membership: -
 Workgroup Name: workgroup01
 Authentication Style: workgroup
 CIFS Server Administrative Status: up
 CIFS Server Description:
 List of NetBIOS Aliases: -`
```
