# Enabling cloud write mode

Use the `volume modify` ONTAP CLI command to enable or disable cloud
write mode for an existing volume. For more information, see [`volume modify`](https://docs.netapp.com/us-en/ontap-cli-9131/volume-modify.html "https://docs.netapp.com/us-en/ontap-cli-9131/volume-modify.html") in the NetApp ONTAP Documentation
Center.

Prerequisites for setting cloud write mode are:

- The volume must be an existing volume. You can only enable the feature
  on an existing volume.
- The volume must be a read-write (RW) volume.
- The volume must have the **All** tiering
  policy. For more information about modifying a volume's tiering policy,
  see [Updating a tiering policy](modify-volume-tiering-policy.md "modify-volume-tiering-policy.md").
  Cloud write mode is helpful for cases like migrations, for example,
  where large amounts of data are transferred to a file system using the
  NFS protocol.

###### To set a volume's cloud write mode (ONTAP CLI)

1. To access the ONTAP CLI, establish an SSH session on the management port of the
   Amazon FSx for NetApp ONTAP file system or SVM by running the following command. Replace
   `management_endpoint_ip` with the IP address of the file system's
   management port.

```
`[~]$` `ssh fsxadmin@`management_endpoint_ip``
```

For more information, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 2. Enter the ONTAP CLI advanced mode using the following command.

```
`FSx::>` `set -privilege advanced`
`Warning: These advanced commands are potentially dangerous; use them only when
 directed to do so by NetApp personnel.
Do you want to continue? {y|n}:` `y`
```

3. Use the following command to set the volume’s cloud write mode,
   replacing the following values:
   - Replace `svm_name` with the name of the SVM that
     the volume is created on.
   - Replace `vol_name` with name of the volume for
     which you are setting cloud write mode.
   - Replace `vol_cw_mode` with either `true`
     to enable cloud write mode on the volume or `false` to disable it.

```
`FSx::>` `volume modify -vserver `svm_name` -volume `vol_name` -is-cloud-write-enabled `vol_cw_mode``
```

The system responds as follows for a successful request.

```
Volume modify successful on volume vol_name of Vserver svm_name.
```
