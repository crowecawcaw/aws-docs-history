# Updating your volume's snapshot reserve

You can change the amount of snapshot reserve on a volume using the NetApp ONTAP CLI or API,
described in the following procedure.

1. To access the ONTAP CLI, establish an SSH session on the management port of the
   Amazon FSx for NetApp ONTAP file system or SVM by running the following command. Replace
   `management_endpoint_ip` with the IP address of the file system's
   management port.

```
`[~]$` `ssh fsxadmin@`management_endpoint_ip``
```

For more information, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 2. Use the
[`volume modify`](https://docs.netapp.com/us-en/ontap-cli-9141/volume-modify.html "https://docs.netapp.com/us-en/ontap-cli-9141/volume-modify.html")
ONTAP ClI command to change the percent of disk space used for the Snapshot copy reserve.
Replace the following placeholder values with your data:

    * ``svm_name`` — use your SVM's name.
    * ``vol_name`` — use your volume's name.
    * ``percent`` — the percent of disk space you want
     to reserve for Snapshot copies.

```
`::>` `volume modify -vserver `svm_name` -volume `vol_name` -percent-snapshot-space `percent``
```

The following example changes the snapshot reserve for vol1 to 25% of the volume's storage capacity.

```
`::>` volume modify -vserver vs0 -volume vol1 -percent-snapshot-space 25
```
