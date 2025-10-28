# Volume storage capacity

FSx for ONTAP volumes are virtual resources that you use for grouping data,
determining how data is stored, and determining the type of access to your data.
Volumes, like folders, don't consume file system storage capacity themselves. Only the
data that's stored in a volume consumes SSD storage and, depending on the [volume's tiering policy](#data-tiering-policy "#data-tiering-policy"), capacity pool storage.
You set a volume's size when you create it, and you can change its size later. You can
monitor and manage the storage capacity of your FSx for ONTAP volumes using the AWS Management Console,
AWS CLI and API, and the ONTAP CLI.

###### Topics

- [Volume data tiering](#volume-data-tiering "#volume-data-tiering")
- [Snapshots and volume storage capacity](#managing-snapshots "#managing-snapshots")
- [Volume file capacity](#managing-volume-file-capacity "#managing-volume-file-capacity")
- [Managing storage efficiencies](manage-vol-SE.md "manage-vol-SE.md")
- [Enabling autosizing](enable-volume-autosizing.md "enable-volume-autosizing.md")
- [Enabling cloud write mode](cloud-write-mode.md "cloud-write-mode.md")
- [Updating storage capacity](manage-volume-capacity.md "manage-volume-capacity.md")
- [Updating a tiering policy](modify-volume-tiering-policy.md "modify-volume-tiering-policy.md")
- [Updating the minimum cooling days](set-cooling-days.md "set-cooling-days.md")
- [Updating a volume's cloud retrieval policy](set-cloud-retrieval.md "set-cloud-retrieval.md")
- [Updating the maximum number of files on a volume](increase-volume-max-files.md "increase-volume-max-files.md")
- [Monitoring volume storage capacity](monitor-volume-storage-console.md "monitor-volume-storage-console.md")
- [Monitoring a volume's file capacity](view-volume-file-capacity.md "view-volume-file-capacity.md")

## Volume data tiering

An Amazon FSx for NetApp ONTAP file system has two storage tiers: primary storage and
capacity pool storage. Primary storage is provisioned, scalable, high-performance SSD
storage that’s purpose-built for the active portion of your data set. Capacity pool
storage is a fully elastic storage tier that can scale to petabytes in size and is
cost-optimized for infrequently accessed data.

The data on each volume is automatically tiered to the capacity pool storage tier based on the
volume's tiering policy, cooling period, and threshold settings. The following sections describe ONTAP volume
tiering policies and the thresholds used to determine when data is tiered to the capacity pool.

###### Note

FSx for ONTAP supports tiering data to the capacity pool on all SnapLock volumes, regardless of the SnapLock type.
For more information, see [How SnapLock works](how-snaplock-works.md "how-snaplock-works.md").

### Volume tiering policies

You determine how to use your FSx for ONTAP file system’s storage tiers by
choosing the tiering policy for each of volume on the file system. You choose the
tiering policy when you create a volume, and you can modify it at any time with
the Amazon FSx console, AWS CLI, API, or using [NetApp management tools](managing-resources-ontap-apps.md "managing-resources-ontap-apps.md"). You can
choose from one of the following policies that determine which data, if any, is
tiered to the capacity pool storage.

###### Note

Tiering can move your file data and snapshot data to the capacity pool tier. However,
file metadata always remains on the SSD tier. For more information, see
[How SSD storage is used](managing-storage-capacity.md#how-ssd-is-used "managing-storage-capacity.md#how-ssd-is-used").

- **Auto** – This policy moves all cold
  data—user data and snapshots—to the capacity pool tier. The cooling rate of
  data is determined by the policy's cooling period, which by default is 31
  days, and is configurable to values between 2–183 days. When the
  underlying cold data blocks are read randomly (as in typical file access),
  they are made hot and written to the primary storage tier. When cold data
  blocks are read sequentially (for example, by an antivirus scan), they
  remain cold and remain on the capacity pool storage tier. This is the
  default policy when creating a volume using the Amazon FSx console.
- **Snapshot Only** – This policy moves only
  snapshot data to the capacity pool storage tier. The rate at which snapshots
  are tiered to the capacity pool is determined by the policy's cooling
  period, which by default is set to 2 days, and is configurable to values
  between 2–183 days. When cold snapshot data are read, they are made
  hot and written to the primary storage tier. This is the default policy when
  creating a volume using the AWS CLI, Amazon FSx API, or the NetApp ONTAP
  CLI.
- **All** – This policy marks all user data and
  snapshot data as cold, and stores it in the capacity pool tier. When data
  blocks are read, they remain cold and are not written to the primary storage tier.
  When data is written to a volume with the **All** tiering policy,
  it is still initially written to the SSD storage tier, and is tiered to the capacity pool
  by a background process. If the **All** policy is applied to a volume that
  already contains data, the existing data is tiered from SSD to the capacity pool.
  Note that file metadata always remains on the SSD tier.
- **None** – This policy keeps all of your volume’s data on the primary storage tier,
  and prevents it from being moved to capacity pool storage. If you set a volume to this policy after it uses any other policy,
  existing data (including snapshots) in the volume that was in capacity pool storage is moved to SSD storage
  by a background process. This data migration only occurs when your SSD utilization is below 90% and the cloud retrieval
  policy is set to `promote` or `on-read`. This background process can be sped up by intentionally reading data.
  For more information, see [Cloud retrieval policies](#cloud-retrieval-policies "#cloud-retrieval-policies").

For more information about setting or modifying a volume's tiering policy, see
[Updating a tiering policy](modify-volume-tiering-policy.md "modify-volume-tiering-policy.md").

As a best practice, when migrating data that you plan to store long-term in capacity pool storage, we recommend
that you use the **Auto** tiering policy on your volume.
With **Auto** tiering, data is stored on the SSD storage tier for a minimum of 2 days (based on the volume's cooling period)
before it's moved to the capacity pool
tier. ONTAP runs post-process deduplication on data stored in the SSD storage tier periodically, automatically adjusting the
frequency based on the rate of data change in the volume—higher rates trigger post-process deduplication jobs more frequently.

By default, post-process compression is disabled in ONTAP due to the performance impact it can have on ongoing workloads on
the file system. You should evaluate the impact on your workload's performance before enabling post-process compression. To enable post-process
compression, assume the diagnostic privilege level in the ONTAP CLI and run the following command:

```
`::>` `volume efficiency inactive-data-compression modify -vserver `svm-name` -volume `vol-name` -is-enabled true`
```

ONTAP runs post-process compression for data that is retained on SSD storage for a minimum of 14 days. For workloads where
data is unlikely to be accessed after a shorter period, you can modify the post-process compression settings to run post-process compression sooner.
For example, to apply post-process compression savings to data that has not been accessed for 5 days, run the following ONTAP CLI command:

```
`::>` `volume efficiency inactive-data-compression modify -vserver `svm-name` -volume `vol-name` -threshold-days 5 -threshold-days-min 2 -threshold-days-max 14`
```

For more information about the command, see [volume efficiency inactive-data-compression modify](https://docs.netapp.com/us-en/ontap-cli-9141/volume-efficiency-inactive-data-compression-modify.html "https://docs.netapp.com/us-en/ontap-cli-9141/volume-efficiency-inactive-data-compression-modify.html")

By retaining data on SSD, you maximize the transfer speeds of volume backups that you create, as data transfer rates are higher for SSD storage.

### Tiering cooling period

A volume's tiering cooling period sets the amount of time that it takes
for data in the SSD tier to be marked as cold. The cooling period applies to the
`Auto` and `Snapshot-only` tiering policies. You can set
the cooling period to a value in the range of 2–183 days. For more
information about setting the cooling period, see [Updating the minimum cooling days](set-cooling-days.md "set-cooling-days.md").

Data is tiered 24–48 hours after its cooling period expires.
Tiering is a background process that consumes network resources, and has a lower
priority than client-facing requests. Tiering activities are throttled when there
are ongoing client-facing requests.

### Cloud retrieval policies

A volume's cloud retrieval policy sets the conditions that specify
when data that's read from the capacity pool tier is allowed to be promoted to the
SSD tier. When the cloud retrieval policy is set to anything other than
`Default`, this policy overrides the retrieval behavior of your
volume’s tiering policy. A volume can have one of the following cloud retrieval
policies:

- **Default** – This policy retrieves tiered data based on the volume's
  underlying tiering policy. This is the default cloud retrieval policy for all volumes.
- **Never** – This policy never retrieves tiered data, regardless of
  whether the reads are sequential or random. This is similar to setting the
  tiering policy of your volume to **All**, except that you
  can use it with other policies–**Auto**,
  **Snapshot-only**–to tier data according to the
  minimum cooling period instead of immediately.
- **On-read** – This policy retrieves tiered data for all client-driven
  data reads. This policy has no effect when using the
  **All** tiering policy.
- **Promote** – This policy marks all of a volume’s data that's in the
  capacity pool for retrieval to the SSD tier. The data is marked the next
  time the daily background tiering scanner runs. This policy is beneficial
  for applications that have cyclical workloads that run infrequently, but
  require SSD tier performance when they do run. This policy has no effect
  when using the **All** tiering policy.

For information on setting a volume's cloud retrieval policy, see [Updating a volume's cloud retrieval policy](set-cloud-retrieval.md "set-cloud-retrieval.md").

### Tiering thresholds

A file system's SSD storage capacity utilization determines how ONTAP manages the tiering
behavior for all of your volumes. Based on a file system's SSD storage capacity usage, the
following thresholds set the tiering behavior as described.
For information about how to monitor the capacity utilization
of a volume's SSD storage tier, see [Monitoring volume storage capacity](monitor-volume-storage-console.md "monitor-volume-storage-console.md").

###### Note

We recommend that you don't exceed 80% storage capacity utilization of your SSD storage tier.
For second-generation file systems, this recommendation applies to both the total average utilization across all of your
file system's aggregates and to the utilization of each individual aggregate. This ensures that tiering functions properly,
and provides overhead for new
data. If your SSD storage tier is consistently above 80% storage capacity
utilization, you can increase your SSD storage tier's capacity. For more
information, see [Updating file system SSD storage and IOPS](storage-capacity-and-IOPS.md#increase-primary-storage "storage-capacity-and-IOPS.md#increase-primary-storage").

FSx for ONTAP uses the following storage capacity thresholds to manage tiering on volumes:

- <=50% SSD storage tier utilization – At
  this threshold, the SSD storage tier is considered to be underutilized, and
  only volumes that are using the **All** tiering policy have
  data tiered to capacity pool storage. Volumes with **Auto**
  and **Snapshot-only** policies don't tier data at this
  threshold.
- > 50% SSD storage tier utilization – Volumes
  > with **Auto** and **Snapshot-only**
  > tiering policies tier data based on the tiering minimum cooling days
  > setting. The default setting is 31 days.
- > =90% SSD storage tier utilization –
  > At this threshold, Amazon FSx prioritizes preserving space in the SSD storage tier. Cold data from the
  > capacity pool tier is no longer moved into the SSD storage tier when read for volumes using
  > **Auto** and **Snapshot-only** policies.
- > =98% SSD storage tier utilization –
  > All tiering functionality stops when the SSD storage tier is at or above
  > 98% utilization. You can continue to read from storage tiers, but you
  > can't write to the tiers.

## Snapshots and volume storage capacity

A _snapshot_ is a read-only image of an Amazon FSx for NetApp ONTAP
volume at a point in time. Snapshots offer protection against accidental deletion or modification
of files in your volumes. With snapshots, your users can easily view and restore
individual files or folders from an earlier snapshot.

Snapshots are stored alongside your ﬁle system's data, and they consume
the ﬁle system's storage capacity. However, snapshots consume storage capacity only for
the portions of ﬁles that changed since the last snapshot. Snapshots
are not included in backups of your ﬁle system volumes.

Snapshots are enabled by default on your volumes, using the default
snapshot policy. Snapshots are stored in the `.snapshot` directory at the
root of a volume. You can manage volume storage capacity for snapshots in the
following ways:

- [Snapshot policies](snapshots-ontap.md#snapshot-policies "snapshots-ontap.md#snapshot-policies") – Select
  a built-in snapshot policy or choose a custom policy that you created in the ONTAP CLI or REST API.
- [Manually delete snapshots](manually-delete-snapshots.md "manually-delete-snapshots.md") – Reclaim
  storage capacity by deleting snapshots manually.
- [Create a snapshot autodelete policy](snapshot-autodelete-policy.md "snapshot-autodelete-policy.md") –
  Create a policy that deletes more snapshots than the default snapshot
  policy.
- [Turn off automatic snapshots](disable-snapshots.md "disable-snapshots.md") – Conserve
  storage capacity by turning off automatic snapshots.

For more information, see [Protecting your data with snapshots](snapshots-ontap.md "snapshots-ontap.md").

## Volume file capacity

Amazon FSx for NetApp ONTAP volumes have file pointers that are used to store file
metadata such as file name, last accessed time, permissions, size, and to serve as
pointers to data blocks. These file pointers are called inodes, and each volume has
a finite capacity for the number of inodes, which is called the volume file
capacity. When a volume runs low on or exhausts its available files (inodes), you
can't write additional data to that volume.

The number of file system objects—files, directories, Snapshot
copies—a volume can contain is determined by how many inodes it has. The
number of inodes in a volume increases commensurately with the volume's storage
capacity (and the number of volume constituents for FlexGroup volumes).
By default, FlexVol volumes (or FlexGroup constituents)
with a storage capacity of 648 GiB or more all
have the same number of inodes: 21,251,126. If you create a volume larger than
648 GiB and you want it to have more than 21,251,126 inodes, you must increase
the maximum number of inodes (files) manually. For more information about viewing the maximum number of files
for a volume, see [Monitoring a volume's file capacity](view-volume-file-capacity.md "view-volume-file-capacity.md").

The default number of inodes on a volume is 1 inode for every 32 KiB of volume storage capacity, up to a volume size of 648 GiB. For a 1 GiB volume:

Volume_size_in_bytes × (1 file ÷ inode_size_in_bytes) = maximum_number_of_files

1,073,741,824 bytes × (1 file ÷ 32,768 bytes) = 32,768 files

You can increase the maximum number of inodes that a volume can contain, up to a maximum of 1 inode for every
4 KiB of storage capacity. For a 1 GiB volume. this increases the maximum
number of inodes or files from 32,768 to 262,144:

1,073,741,824 bytes × (1 file ÷ 4096 bytes) = 262,144 files

An FSx for ONTAP volume can have a maximum of 2 billion inodes.

For information about changing the maximum number of files that a volume can store, see
[Updating the maximum number of files on a volume](increase-volume-max-files.md "increase-volume-max-files.md").
