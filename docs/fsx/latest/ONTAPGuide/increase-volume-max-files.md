# Updating the maximum number of files on a volume

FSx for ONTAP volumes can run out of file capacity when the number of available inodes, or file pointers, is exhausted.

###### To increase the maximum number of files on a volume (ONTAP CLI)

You use the `volume modify` ONTAP CLI command to increase the maximum number of files on a volume.
For more information, see [`volume modify`](https://docs.netapp.com/us-en/ontap-cli-9111/volume-modify.html "https://docs.netapp.com/us-en/ontap-cli-9111/volume-modify.html") in the NetApp ONTAP Documentation Center.

1. To access the ONTAP CLI, establish an SSH session on the management port of the
   Amazon FSx for NetApp ONTAP file system or SVM by running the following command. Replace
   `management_endpoint_ip` with the IP address of the file system's
   management port.

```
`[~]$` `ssh fsxadmin@`management_endpoint_ip``
```

For more information, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 2. Do one of the following, depending on your use case.
Replace `svm_name` and `vol_name` with your values.

    * To configure a volume to always have the maximum number of files (inodes) available, perform the following:



    	1. Enter advanced mode in the ONTAP CLI by using the following command.



    	```
    	`::>` set adv
    	```
    	2. After running this command, you'll see this output. Enter `y` to continue.



    	```
    	`Warning: These advanced commands are potentially dangerous; use them only when
    	directed to do so by NetApp personnel.
    	Do you want to continue? {y|n}:` `y`
    	```
    	3. Enter the following command to always use the maximum number of files on the volume:



    	```
    	`::>` volume modify -vserver `svm_name` -volume `vol_name` -files-set-maximum true
    	```
    * To manually specify the total number of files permitted on the volume, with ``max_number_files` =
     (current_size_of_volume) × (1 file ÷ 4 KiB)`, up to a maximum possible value of 2 billion, use the following command:



    ```
    `::>` volume modify -vserver `svm_name` -volume `vol_name` -files `max_number_files`
    ```
