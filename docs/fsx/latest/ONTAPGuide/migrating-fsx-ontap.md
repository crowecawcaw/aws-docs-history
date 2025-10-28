# Migrating to Amazon FSx for NetApp ONTAP

The following sections provide information on how to migrate your existing NetApp ONTAP file systems to Amazon FSx for NetApp ONTAP.

###### Note

If you plan to use the `All` tiering policy to migrate your data to the capacity pool tier, keep in mind that
file metadata is always stored on the SSD tier, and that all new user data is first written to the SSD tier. When data is written to
the SSD tier, the background tiering process will begin tiering your data to capacity pool storage, but the tiering process is not
immediate and consumes network resources. You need to size your SSD tier to account for file metadata (3-7% of the size of user data),
as a buffer for user data before it is tiered to capacity pool storage. We recommend that you do not exceed 80% utilization of your
SSD tier.

While migrating data, be sure to monitor your SSD tier using [CloudWatch File system metrics](file-system-metrics.md "file-system-metrics.md")
to ensure that it is not filling faster than the tiering process can move data to the capacity pool storage.

###### Topics

- [Migrating to FSx for ONTAP using NetApp SnapMirror](migrating-fsx-ontap-snapmirror.md "migrating-fsx-ontap-snapmirror.md")
- [Migrating to FSx for ONTAP using
  AWS DataSync](migrate-files-to-fsx-datasync.md "migrate-files-to-fsx-datasync.md")
