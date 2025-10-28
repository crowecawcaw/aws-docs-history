# Creating an iSCSI LUN

This process describes how to create an iSCSI LUN on an Amazon FSx for NetApp ONTAP file system using the NetApp ONTAP CLI **lun create** command.
For more information, see [**lun create**](https://docs.netapp.com/us-en/ontap-cli-9111/lun-create.html "https://docs.netapp.com/us-en/ontap-cli-9111/lun-create.html")
in the NetApp ONTAP Documentation Center.

###### Note

The iSCSI protocol isn't supported for file systems with more than six HA pairs.

This process assumes you already have a volume created on your file
system. For more information, see
[Creating volumes](creating-volumes.md "creating-volumes.md").

1. To access the ONTAP CLI, establish an SSH session on the management port of the
   Amazon FSx for NetApp ONTAP file system or SVM by running the following command. Replace
   `management_endpoint_ip` with the IP address of the file system's
   management port.

```
`[~]$` `ssh fsxadmin@`management_endpoint_ip``
```

For more information, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 2. Create a LUN using the **lun create** NetApp CLI command, replacing the following values:

    * **``svm_name``** - The name of the storage virtual
     machine (SVM) providing the iSCSI target. The host uses this value to reach the LUN.
    * **``vol_name``** - The name of
     the volume hosting the LUN.
    * **``lun_name``** -
     The name you want to assign to the LUN.
    * **``size``** - The
     size, in bytes, of the LUN. The maximum size LUN you can create is 128 TB.

     ###### Note

    We recommend that you use a volume at least 5% larger than your LUN
     size. This margin leaves space for volume snapshots.
    * **``ostype``** - The
     operating system of the host, either `windows_2008` or
     `linux`. Use `windows_2008` for all versions
     of Windows; this ensures the LUN has proper block offset for the
     operating system and optimizes performance.

###### Note

We recommend enabling space allocation on your LUN. With space
allocation enabled, ONTAP can inform your host when the LUN is
out of capacity and can reclaim space as you delete data from the
LUN.

For more information, see [`lun create`](https://docs.netapp.com/us-en/ontap-cli-9121/lun-create.html "https://docs.netapp.com/us-en/ontap-cli-9121/lun-create.html")
in the NetApp ONTAP CLI documentation.

```
`>` lun create -vserver `svm_name` -path /vol/`vol_name`/`lun_name` -size `size` -ostype `ostype` -space-allocation enabled
```

```
`Created a LUN of size 10g (10737418240)`
```

3. Confirm the LUN is created, online, and mapped.

```
`>` lun show
```

The system responds with the following output:

```
`Vserver Path State Mapped Type Size
--------- ------------------------------- ------- -------- ------------ --------
`svm_name`
 /vol/`vol_name`/`lun_name` online unmapped windows_2008 10GB`
```

## Next steps

Now that you have created an iSCSI LUN, the next step in the process of using an iSCSI LUN
as block storage is to map the LUN to an `igroup`. For more information, see
[Provisioning iSCSI for Linux](mount-iscsi-luns-linux.md "mount-iscsi-luns-linux.md") or
[Provisioning iSCSI for Windows](mount-iscsi-windows.md "mount-iscsi-windows.md").
