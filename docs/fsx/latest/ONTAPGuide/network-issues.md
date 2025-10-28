# Troubleshooting network issues

If you are experiencing network issues, you can use the procedures shown here to
diagnose the problem.

## You want to capture a packet trace

Packet tracing is the process of verifying the path of a packet through the layers to its
destination. You control the packet tracing process with the following NetApp ONTAP CLI
commands:

- **network tcpdump start** – Starts packet tracing
- **network tcpdump show** – Shows currently running packet traces
- **network tcpdump stop** – Stops a running packet trace

These commands are available to users who have the `fsxadmin` role on your file system.

###### To capture a packet trace from your file system

1. To SSH into the NetApp ONTAP CLI of your file system, follow the steps documented in the
   [Using the NetApp ONTAP CLI](managing-resources-ontap-apps.md#netapp-ontap-cli "managing-resources-ontap-apps.md#netapp-ontap-cli") section of the
   _Amazon FSx for NetApp ONTAP User Guide_.

```
`ssh fsxadmin@`file-system-management-endpoint-ip-address``
```

2. Enter the diagnostic privilege level in the ONTAP CLI by using the following command.

```
`::>` `set diag`
```

When prompted to continue, enter `y`.

```
Warning: These diagnostic commands are for use by NetApp personnel only.
Do you want to continue? {y|n}: y
```

3. Identify the location on your file system where you want to save your packet trace.
   The volume must be online and must be mounted in the namespace with a valid junction path.
   Use the following command to check for volumes that fulfill those criteria:

```
`::*>` `volume show -junction-path !- -fields junction-path`
`vserver volume junction-path
------- --------- -------------
fsx test_vol1 /test_vol1
fsx test_vol2 /test_vol2
fsx test_vol2 /test_vol3`
```

4. Start the trace with the minimum required arguments. Replace the following:
   - Replace `node_name` with the name of the node
     (for example, `FsxId01234567890abcdef-01`).
   - Replace `svm_name` with the name of your storage
     virtual machine (for example, `fsx`).
   - Replace `junction_path_name` with the name of the volume (for
     example, `test-vol1`).

```
`::*>` `debug network tcpdump start -node `node_name` -ipspace Default -pass-through "-i e0e -w /clus/`svm_name`/`junction_path_name`"`
`Info: Started network trace on interface "e0e"
Warning: Snapshots should be disabled on the tcpdump destination volume while packet traces are occurring. Use the
"volume modify -snapshot-policy none -vserver fsx -volume test_vol1" command to disable Snapshots on the
tcpdump destination volume.`
```

###### Important

Packet traces can only be captured on the `e0e` interface and in the `Default` IP space.
In FSx for ONTAP, all network traffic uses the `e0e` interface.

When using packet tracing, keep the following in mind:

    * When starting a packet trace, you must include the path to where you want to store the trace
     files, in this format: /clus/`svm_name`/`junction-path-name`
    * Optionally, provide the file name for the packet trace. If the filter\_name is not specified,
     it is automatically generated in the form: `node-name`\_`port-name`\_`yyyymmdd_hhmmss`.trc
    * If rolling traces are specified, the filter\_name is suffixed with a number that indicates
     the position in the rotation sequence.
    * The ONTAP CLI also accepts the following optional **-pass-through** arguments:



    ```
    -B, --buffer-size=<KiB>
    -c <number_of_packets>
    -C <file_size-mB>
    -F <filter_expression_filename>
    -G <rotate_seconds>
    --time-stamp-precision {micro|nano}
    -Q, --direction {in|out|inout}
    -s, --snapshot-length=<bytes>
    -U, --packet-buffered
    -W <rotate_file_count>
    <filter-expression>
    ```
    * For information about filter expressions, see
     [pcap-filter(7) man
     page](https://www.tcpdump.org/manpages/pcap-filter.7.html "https://www.tcpdump.org/manpages/pcap-filter.7.html").

5. View the traces in progress:

```
`::*>` `debug network tcpdump show`
`Node IPspace Port Filename
----------------------- -------- -------- --------
FsxId123456789abcdef-01 Default e0e /clus/fsx/test_vol1/FsxId123456789abcdef-01_e0e_20230605_181451.trc`
```

6. Stop the trace:

```
`::*>` `debug network tcpdump stop -node FsxId123456789abcdef-01 -ipspace Default -port e0e`
`Info: Stopped network trace on interface "e0e"`
```

7. Return to the admin privilege level:

```
`::*>` `set -priv admin`
`::>`
```

8. Access the packet traces.

Your packet traces are stored in the volume that you specified using
the **debug network tcpdump start** command, and can be accessed via
the NFS export or an SMB share that corresponds with that volume.

For more information about capturing packet traces, see
[How to use debug network dump in ONTAP 9.10+](https://kb.netapp.com/onprem/ontap/hardware/How_to_use_debug_tcpdump_in_ONTAP_9.10 "https://kb.netapp.com/onprem/ontap/hardware/How_to_use_debug_tcpdump_in_ONTAP_9.10") in the NetApp Knowledge Base.
