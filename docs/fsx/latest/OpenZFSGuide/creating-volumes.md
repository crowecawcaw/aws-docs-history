# Creating an Amazon FSx for OpenZFS volume

This section provides information on the volume properties that you can configure, as well as instructions on how to create a volume using the Amazon FSx console, the AWS CLI, and the
Amazon FSx API.

###### Topics

- [Creating a volume](#how-to-create-volumes "#how-to-create-volumes")
- [Configurable volume properties](#volume-properties "#volume-properties")

## Creating a volume

You can create new volumes, or create a volume from an existing volume snapshot using the Amazon FSx console, the AWS CLI, or the Amazon FSx API.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. In the left navigation pane, choose **File systems**, and then choose the
   FSx for OpenZFS file system that you want to create a volume for.
3. Choose the **Volumes** tab.
4. Choose **Create volume**.

The **Create volume** dialog box appears. 5. In the **File system** field, choose the file
system to create the volume on. 6. In the **Parent volume ID** field, choose the ID
of the parent volume, which can be the root volume or another volume. 7. In the **Volume name** field, provide a name for the volume.
You can use a maximum of 203 alphanumeric characters, plus the underscore (\_)
special character. The name must be unique among all the volume names on
the same parent volume on the same file system. 8. For **Storage capacity quota - optional**, you can set a quota that
will be the maximum storage size for the volume. This quota cannot be larger than
the parent volume quota. To set no quota and allow this volume to consume any available
capacity in your file system, set this property to `-1`. 9. For **Storage capacity reservation - optional**, you can enter the
reservation for the volume. This reserves dedicated space on the file system storage
pool, meaning the space available to all other volumes is reduced by the amount specified.
It cannot be set to a value that's greater than the parent volume quota or the remaining
reservation space on the file system storage. To set no reservation and allow this volume to consume any available
capacity in your file system, set this property to `0` or `-1`. 10. For **Data compression type**, choose the type of compression
to use for your volume, either **Zstandard**, **LZ4**,
or **No compression**. Zstandard compression provides more data compression
and higher read throughput than LZ4 compression. LZ4 compression provides less compression
and higher write throughput performance than Zstandard compression. For more information about the
storage and performance benefits of the volume data compression options,
see [Data compression](performance.md#perf-data-compression "performance.md#perf-data-compression"). 11. For **Copy tags to snapshots**, enable or disable the option
to copy tags on the root volume to snapshots. 12. For **NFS exports**, there is a default client configuration setting
which you can modify or remove. Client configurations define which clients can access
the volume and their permissions.

To provide additional client configurations:

    1. In the **Client addresses** field, specify which
     clients can access the volume. Enter an asterisk (`*`) for
     any client, a specific IP address, or a CIDR range of IP addresses.
    2. In the **NFS options** field, enter a
     comma-delimited set of exports options. For example, enter `rw`
     to allow read and write permissions to the volume.
    3. Choose **Add client configuration**.
    4. Repeat the procedure to add another client configuration.For more information, see [NFS exports](#nfs-exports "#nfs-exports").

13. For **Record size**, choose whether to use the
    default suggested record size of 128 KiB, or to set a **User-configured** suggested record
    size for the volume. Generally, workloads that write in fixed small or large
    record sizes may benefit from setting a custom record size, like database workloads
    (small record size) or media streaming workloads (large record size). We recommend using
    the default setting for the majority of use cases. For more information about the
    record size setting, see [Configurable volume properties](#volume-properties "#volume-properties").
14. For **User and group quotas**, you can set a storage quota for
    a user or group:
    1.  For **Quota type**, choose `USER` or
        `GROUP`.
    2.  For **User or group ID**, choose a number that is
        the ID of the user or group.
    3.  For **Usage quota**, choose a number that is
        the storage quota of the user or group.
    4.  Choose **Add quota**.
    5.  Repeat the procedure to add a quota for another user or group.

15. To create a volume from an existing volume snapshot, use **Source snapshot ID - optional**, to specify the
    ID of a snapshot from which to create a volume. Then choose a **Source snapshot copy strategy**
    option for the type of volume you're creating:
    - **Clone** creates a clone volume. The snapshot
      will provide the seed content for the volume.
    - **Full copy** creates a volume that will
      contain data copied from the snapshot.

16. Choose **Confirm** to create the volume.
    You can monitor the progress on the **File
    systems** detail page, in the **Status**
    column of the **Volumes** pane. The volume is ready for use
    when its status is **Created**.

- To create an FSx for OpenZFS volume, use the
  [create-volume](../../../cli/latest/reference/fsx/create-volume.md "../../../cli/latest/reference/fsx/create-volume.md")
  CLI command (or the equivalent [CreateVolume](../APIReference/API_CreateVolume.md "../APIReference/API_CreateVolume.md") API operation). The following example creates a new volume by cloning an existing snapshot.

```
`aws fsx create-volume \
 --name vol2 \
 --volume-type OPENZFS \
 --tags Key=creator,Value=Liu \
 --open-zfs-configuration '{
 "CopyTagsToSnapshots": true,
 "DataCompressionType": "LZ4",
 "NfsExports": [
 {
 "ClientConfigurations": [
 {
 "Clients": "*",
 "Options": [ "rw","root_squash","crossmnt" ]
 }
 ]
 }
 ],
 "OriginSnapshot": {
 "CopyStrategy": "CLONE",
 "SnapshotARN": "arn:aws:fsx:us-east-2:111122223333:snapshot/fsvol-0123456789abcdef0/fsvolsnap-1234567890abcdef0"
 },
 "ParentVolumeId": "fsvol-abcdef01234567890",
 "ReadOnly": false,
 "RecordSizeKiB": 128,
 "StorageCapacityQuotaGiB": 10000,
 "StorageCapacityReservationGiB": -1,
 "UserAndGroupQuotas": [
 {
 "Id": 1004,
 "StorageCapacityQuotaGiB": 2000,
 "Type": "GROUP"
 }
 ]
 }'`
```

After successfully creating the volume, Amazon FSx returns its description in
JSON format.

## Configurable volume properties

When you create a volume, you can configure the following properties to customize and control the storage aspects of the volume.

- **Volume name** provides a name for the volume. Please
  ensure that the specified name does not conflict with an existing file or directory on the parent volume.
- **Data compression type** reduces the storage capacity that
  your data consumes and can also help increase your effective throughput. You can choose
  either **Zstandard**, **LZ4**,
  or **No compression**. Zstandard compression
  provides a higher level of data compression and higher read throughput performance than LZ4 compression.
  LZ4 compression provides a lower level of compression and higher write throughput performance than Zstandard compression.
  For more information about the storage and performance benefits of the volume data compression options,
  see [Data compression](performance.md#perf-data-compression "performance.md#perf-data-compression").
- **Storage capacity quota** sets a volume quota, which is
  the maximum storage size for the volume. A volume quota limits the amount of storage space
  that the volume can consume to the configured amount, but does not guarantee the space will be available.
  To guarantee quota space, you must also set **Storage capacity reservation**.

By setting quotas without setting a **Storage capacity reservation**,
you can create space-efficient _thin-provisioned_ volumes where capacity
is allocated only as storage is being consumed. With thin-provisioned volumes, you can assign quotas
that are collectively larger than the existing capacity of the file system or
quota of a parent volume. If your file system is nearing capacity or a parent
volume is nearing its quota, note that your users or applications may not be
able to write in a child volume even though the volume has not reached its
quota limit.

- **Storage capacity reservation** guarantees a specified
  amount of storage space to always be available for the volume. The reservation
  reserves a configured amount of storage space from the parent volume. Only the volume
  with the reservation can use that storage space, regardless of the volume quotas
  that other volumes may have. Note that unlike volume quotas, you can't reserve
  an amount of storage space that doesn't exist in its immediate parent. Set a
  reservation if an application must have a certain amount of storage space or it
  will fail.
- **Record size** sets the suggested block size for a volume
  in a ZFS dataset. Choose whether to use the default record size of 128 KiB,
  or to set a custom record size for the volume. We recommend using the default
  setting for the majority of use cases.
  For more information about the record size setting, see
  [ZFS record size](performance.md#record-size-performance "performance.md#record-size-performance").
  Generally, workloads that write in fixed small or large
  record sizes may benefit from setting a custom record size, like database workloads
  (small record size) or media streaming workloads (large record size). See the
  OpenZFS documentation for more information about
  [Dataset record size](https://openzfs.github.io/openzfs-docs/Performance%20and%20Tuning/Workload%20Tuning.html#dataset-recordsize "https://openzfs.github.io/openzfs-docs/Performance%20and%20Tuning/Workload%20Tuning.html#dataset-recordsize") and ZFS datasets.
- **NFS exports** use NFS-level export policies to
  define how the file system should be exported over the NFS protocol. The NFS
  exports setting defines which clients can access the volume and what permissions
  they have. For more information,
  see [NFS exports](#nfs-exports "#nfs-exports").
- **User and group quotas** configures
  individual user and/or group quotas for volumes, which sets a limit on the amount
  of storage space they can consume on the volume. To determine quota usage, add up the total size of files
  owned by the user or group specified in the quota. Only data in the volume on which the quota is applied counts
  toward the user or group's volume quota utilization. Other files and directories that exist only in snapshots or
  child volumes do not count toward quota usage.
- **Source snapshot ID** specifies a snapshot from which to
  create a volume. Then use **Source snapshot copy strategy**
  to specify the type of volume to create:

      + **Clone** creates a clone volume. A clone volume
       is a writable copy that is initialized with the same
       data as the snapshot from which it was created. Because clone volumes
       reference the data from the snapshot, clone volumes are created
       almost instantly, and initially consume no additional capacity. They only
       consume the capacity required for the incremental changes made to the
       source snapshot, providing an easy way to support multiple users or
       applications in parallel from a shared dataset. However, a clone volume
       maintains a dependency on its source snapshot, so you cannot delete this
       source snapshot while the clone volume is in use.
      + **Full copy** creates a full-copy volume.
       A full-copy volume is a writable copy that is initialized with the same
       data as the snapshot from which it was created. Unlike a clone volume,
       it does not maintain any dependency on its source snapshot. Because a
       full-copy volume requires copying all of the source snapshot data to a
       new volume, creation time will depend on the size of the source snapshot.
       While this data is being copied, your full-copy volume will be read only.
       Once a full-copy volume is created, it is identical to a standard
       FSx for OpenZFS volume. Files in the source snapshot will maintain their original
       record size regardless of the record size of the destination volume. Files will
       be compressed according to the compression property on the destination volume.

  For more information on snapshots, see
  [Protecting your data with snapshots](snapshots-openzfs.md "snapshots-openzfs.md").

### NFS exports

NFS exports are NFS-level export policies that configure which clients can
access the volume and the options that are available. Each volume has its own NFS
exports setting, so a client may be able to mount one volume on the file system
but not a different volume.

When creating a volume from the console, you provide the NFS exports information
in an array of client configurations, each of which has **Client addresses**
and **NFS options** fields.

The **Client addresses** field specifies which hosts can mount over the NFS
protocol and contains one of these settings:

- `*` is a wildcard that means anyone who can route to the
  file server can mount it.
- The IP address of a client's computer (such as `10.0.0.1`)
  that means a client from that specific IP address can mount the file system.
- A CIDR block range (such as `192.0.2.0/24`) that means any
  client from that address range can mount the file system.

###### Note

If an IP address is permitted to mount a parent volume, it is also automatically
permitted to mount any of the child volumes.

The **NFS options** field lists a set of exports options available on the volume.
Following are descriptions of the most common NFS options. For a more comprehensive list of exports options, see
the [exports(5) - Linux man page](https://linux.die.net/man/5/exports "https://linux.die.net/man/5/exports")
on the `die.net` web site.

- `rw` allows both read and write requests on this NFS volume from the
  specified Client addresses.
- `ro` allows only read requests on this NFS volume. The specified Client
  addresses can't write to the volume.
- `crossmnt` allows clients to inherit access to any child volumes within this
  volume (if configured along with the `no_subtree_check` option, which is included by default).
  This option is required to provide file-level access to your snapshots in the
  `.zfs/snapshot` directory of each volume.
- `all_squash` maps all User IDs (UIDs) and group IDs (GIDs) to the anonymous user.
- `root_squash` maps requests from UID/GID 0 to the anonymous UID/GID.
  It prevents remote root user from having superuser (root) privileges on remote NFS-mounted volumes.
  `root_squash` is the default unless overridden by `all_squash`
  or `no_root_squash`.
- `no_root_squash` turns off root squashing.
- `anonuid` and `anongid` explicitly set the UID and GID of the anonymous account. Valid values are 0 - 2147483647, inclusive.
- `sync` replies to client requests only after the changes have been committed
  to stable storage (that is, disk drives). `sync` is the default unless overridden
  by `async`
- `async` replies to client requests (such as write requests) after the
  changes have been committed to memory, but before any changes made by that request have been
  committed to stable storage (that is, disk drives). This setting can improve performance for
  latency-intensive or IOPS-intensive workloads. For more information,
  see [Performance for Amazon FSx for OpenZFS](performance.md "performance.md").

###### Warning

Use of the `async` option can cause data to be lost or corrupted if a write request
is acknowledged but the server crashes before the write request is fully written to disk.

When you create a volume, the default for **Client addresses** is an asterisk
(`*`) and the default for **NFS options** is `rw,crossmnt`.
