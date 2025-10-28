# Enabling autosizing

Volume autosizing so that the volume will automatically grow to a specified size
when it reaches a used space threshold. You can do this for FlexVol volume types (the default volume type for
FSx for ONTAP) using the [`volume autosize`](https://docs.netapp.com/us-en/ontap-cli-9111/volume-autosize.html "https://docs.netapp.com/us-en/ontap-cli-9111/volume-autosize.html") ONTAP CLI command.

###### To enable volume autosizing (ONTAP CLI)

1. To access the ONTAP CLI, establish an SSH session on the management port of the
   Amazon FSx for NetApp ONTAP file system or SVM by running the following command. Replace
   `management_endpoint_ip` with the IP address of the file system's
   management port.

```
`[~]$` `ssh fsxadmin@`management_endpoint_ip``
```

For more information, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 2. Use the `volume autosize` command as shown, replacing the following values:

    * Replace ``svm_name`` with the name of the SVM that
     the volume is created on.
    * Replace ``vol_name`` with name of the volume that you
     want to resize.
    * Replace ``grow_threshold`` with a used space percentage value (such
     as `90`) at which the volume will automatically increase in size (up to the
     ``max_size`` value).
    * Replace ``max_size`` with the maximum size that the volume
     can grow to. Use the format ```integer````[KB|MB|GB|TB|PB]`;
     for example, `300TB`. The maximum size is 300 TB. The default is 120% of the volume size.
    * Replace `min_size` with the minimum size that the volume will shrink to. Use the same format
     as for `max_size`.
    * Replace `shrink_threshold` with the used space percentage at which the volume will automatically shrink in size.

```
`::>` `volume autosize -vserver `svm_name` -volume `vol_name` -mode grow_shrink -grow-threshold-percent `grow_threshold` -maximum-size `max_size` -shrink-threshold-percent `shrink_threshold` -minimum-size `min_size``
```

3. To show the current autosize setting, run the following command. Replace `svm_name` and `vol_name` with your information.

```
`::>` `volume autosize -vserver `svm_name` -volume `vol_name``
```
