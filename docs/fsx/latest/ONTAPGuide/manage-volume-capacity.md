# Updating storage capacity

You can manage volume storage capacity by manually increasing or decreasing volume size using the AWS Management Console, AWS CLI and API,
and the ONTAP CLI. You can also enable volume autosizing so that the volume size automatically grows or shrinks
when it reaches certain used storage capacity thresholds. You use the ONTAP CLI to manage volume autosizing.

###### To change a volume's storage capacity (console)

- You can increase or decrease a volume's storage capacity using the Amazon FSx console, AWS CLI, and API.
  For more information, see [Updating volumes](updating-volumes.md "updating-volumes.md").
  You can also use the ONTAP CLI to modify a volume's storage capacity using the
  [`volume modify`](https://docs.netapp.com/us-en/ontap-cli-9111/volume-modify.html "https://docs.netapp.com/us-en/ontap-cli-9111/volume-modify.html") command.

###### To modify a volume's size (ONTAP CLI)

1. To access the ONTAP CLI, establish an SSH session on the management port of the
   Amazon FSx for NetApp ONTAP file system or SVM by running the following command. Replace
   `management_endpoint_ip` with the IP address of the file system's
   management port.

```
`[~]$` `ssh fsxadmin@`management_endpoint_ip``
```

For more information, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 2. Use the **volume modify** ONTAP CLI command to modify a volume's storage capacity. Run the following command,
using your data in place of the following values:

    * Replace ``svm_name`` with the name of the storage virtual
     machine (SVM) that the volume is created on.
    * Replace ``vol_name`` with name of the volume that you want
     to re-size.
    * Replace ``vol_size`` with the new size of the volume in
     the format
     ```integer````[KB|MB|GB|TB|PB]`;
     for example, `100GB` to increase the volume size to 100 gigabytes.

```
`::>` `volume modify -vserver `svm_name` -volume `vol_name` -size `vol_size``
```
