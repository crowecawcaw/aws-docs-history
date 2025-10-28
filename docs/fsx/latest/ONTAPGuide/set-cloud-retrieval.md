# Updating a volume's cloud retrieval policy

Use the `volume modify` ONTAP CLI command to set the
cloud retrieval policy for an existing volume. For more information, see [`volume modify`](https://docs.netapp.com/us-en/ontap-cli-9111/volume-modify.html "https://docs.netapp.com/us-en/ontap-cli-9111/volume-modify.html") in the NetApp ONTAP Documentation
Center.

###### To set a volume's cloud retrieval policy (ONTAP CLI)

1. To access the ONTAP CLI, establish an SSH session on the management port of the
   Amazon FSx for NetApp ONTAP file system or SVM by running the following command. Replace
   `management_endpoint_ip` with the IP address of the file system's
   management port.

```
`[~]$` `ssh fsxadmin@`management_endpoint_ip``
```

For more information, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 2. Enter the ONTAP CLI advanced mode using the following command.

```
`FSx::>` `set adv`

`Warning: These advanced commands are potentially dangerous; use them only when
 directed to do so by NetApp personnel.
Do you want to continue? {y|n}:` `y`
```

3. Use the following command to set the volume’s cloud retrieval policy, replacing the following
   values:
   - Replace `svm_name` with the name of the SVM that
     the volume is created on.
   - Replace `vol_name` with name of the volume for which you
     are setting the cloud retrieval policy.
   - Replace `retrieval_policy` with the desired value,
     either `default`, `on-read`, `never`, or `promote`.

```
`FSx::>` `volume modify -vserver `svm_name` -volume `vol_name` -cloud-retrieval-policy `retrieval_policy``
```

The system responds as follows for a successful request.

```
Volume modify successful on volume vol_name of Vserver svm_name.
```
