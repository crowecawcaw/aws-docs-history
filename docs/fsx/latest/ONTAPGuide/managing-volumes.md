# Managing FSx for ONTAP volumes

Each storage virtual machine (SVM) on an FSx for ONTAP file system can have one or
more _volumes_. A volume is an isolated data container for
files, directories, or iSCSI logical units of storage (LUNs). Volumes are _thin provisioned_, meaning that they consume storage
capacity only for the data stored in them.

You can access a volume from Linux, Windows, or macOS clients over the Network File
System (NFS) protocol, the Server Message Block (SMB) protocol, or over the Internet
Small Computer Systems Interface (iSCSI) protocol by creating an iSCSI LUN (shared block
storage). FSx for ONTAP also supports multi-protocol access (concurrent NFS and SMB access) to the same volume.

You can create volumes by using the AWS Management Console, AWS CLI, the Amazon FSx API, or NetApp Console.
You can also use your file system’s or SVM’s administrative endpoint to create,
update, and delete volumes by using the NetApp ONTAP CLI or REST API.

###### Note

You can create 500 volumes per HA pair, up to 1,000 volumes across all HA pairs. FlexGroup constituent volumes
count toward this limit. By default, there are eight constituent volumes per aggregate, per FlexGroup.

When you create a volume, you define the following properties:

- Volume style – The [volume style](#volume-styles "#volume-styles") can be either FlexVol or FlexGroup.
- Volume name – The name of the volume.
- Volume type – The [volume type](#volume-types "#volume-types") can be either Read-Write (RW)
  or Data protection (DP). DP volumes are read-only and used as the destination
  in a NetApp SnapMirror or SnapVault relationship.
- Volume size – This is the maximum amount of data that the volume can store, regardless
  of the storage tier.
- Junction path – This is the location in the SVM's namespace where the volume gets
  mounted.
- Storage efficiency – [Storage
  efficiency](managing-storage-capacity.md#storage-efficiency "managing-storage-capacity.md#storage-efficiency") features, including data compaction, compression, and deduplication provide
  typical storage savings of 65% for general-purpose file sharing workloads.
- Volume [security style](#volume-security-style "#volume-security-style") (Unix or NTFS)
  – Determines what type of permissions are used for data
  access on the volume when authorizing users.
- Data tiering – The [tiering policy](volume-storage-capacity.md#volume-data-tiering "volume-storage-capacity.md#volume-data-tiering") defines which data is stored
  in the cost-effective capacity pool tier.
- [Tiering policy cooling period](volume-storage-capacity.md#tiering-cooling-period "volume-storage-capacity.md#tiering-cooling-period") – Defines when data is marked
  cold and moved to capacity pool storage.
- Snapshot policy – [Snapshot policies](snapshots-ontap.md#snapshot-policies "snapshots-ontap.md#snapshot-policies") define how the system
  creates snapshots for a volume. You can choose from three predefined policies or use a custom policy.
  that you have created using the ONTAP CLI or REST API.
- [Copy tags to backups](tag-resources.md#copying-tags-to-backups "tag-resources.md#copying-tags-to-backups") – Amazon FSx will automatically copy any tags from your volumes to
  backups using this option. You can set this option using the AWS CLI or Amazon FSx API.

###### Topics

- [Volume styles](#volume-styles "#volume-styles")
- [Volume types](#volume-types "#volume-types")
- [Volume security style](#volume-security-style "#volume-security-style")
- [Creating volumes](creating-volumes.md "creating-volumes.md")
- [Updating volumes](updating-volumes.md "updating-volumes.md")
- [Moving volumes between aggregates](moving-fg-volumes.md "moving-fg-volumes.md")
- [Monitoring volumes](viewing-volumes.md "viewing-volumes.md")
- [Deleting volumes](deleting-volumes.md "deleting-volumes.md")

## Volume styles

FSx for ONTAP offers two styles of volumes that you can use for different
purposes. You can create either FlexVol or FlexGroup volumes using the
Amazon FSx console, the AWS CLI, and the Amazon FSx API.

- FlexVol volumes offer the simplest experience for file systems
  with one high-availability (HA) pair, so they are the default volume style for
  first-generation file systems and second-generation file systems with one HA
  pair. The minimum size of a FlexVol volume is 20 mebibytes (MiB),
  and the maximum size is 314,572,800 MiB.
- FlexGroup volumes are comprised of multiple constituent
  FlexVol volumes, which allows them to deliver higher
  performance and storage scalability than FlexVol volumes for file
  systems with multiple HA pairs. FlexGroup volumes are the default
  volume style for second-generation file systems with more than one HA pair. The
  minimum size of a FlexGroup volume is 100 gibibytes (GiB) per
  constituent, and the maximum size is 20 pebibytes (PiB).

You can convert a volume with the FlexVol style to the FlexGroup style with the ONTAP CLI, which creates a FlexGroup with a single constituent.
However, we recommend that you use AWS DataSync to move data between a FlexVol volume and a new FlexGroup volume to ensure that the data is evenly distributed across the
FlexGroup's constituents. For more information, see [FlexGroup constituents](#constituents "#constituents").

###### Note

If you want to use the ONTAP CLI to convert a FlexVol volume to a FlexGroup volume, make sure that you delete any backups
of the FlexVol volume before converting it. ONTAP doesn't automatically rebalance data as part of the conversion, so the data might be imbalanced
across the FlexGroup constituents.

### FlexGroup constituents

A FlexGroup volume is made up of constituents, which are FlexVol volumes. By default, FSx for ONTAP assigns eight constituents
to a FlexGroup volume per HA pair.

When you create your FlexGroup volume, the size of it is divided
evenly among its constituents. For example, if you create an 800 gigabyte (GB)
FlexGroup volume with eight constituents, each constituent is 100
GB in size. A FlexGroup volume can be between 100 GB and 20 PiB in
size, but the total size depends on the size of the constituents. Each constituent
has a minimum size of 100 GB and a maximum size of 300 TiB. For example, a
FlexGroup volume with eight constituents has a minimum size of
800 GB and a maximum size of 20 PiB.

ONTAP distributes data at the file-level across the constituents. You can store up to two billion files in each constituent on your FlexGroup volume.

When you update the size of your FlexGroup volume, the new size is
evenly distributed among its existing constituents.

You can also add more constituents to your FlexGroup volume using the
ONTAP CLI or REST API. However, we recommend that you only do so if you need
additional storage capacity and all of your constituents are already at their maximum size (300 TiB per constituent).
Adding constituents can lead to an imbalance of data and I/O across the constituents. Until the constituents are
balanced, it's possible that the write throughput might be 5–10% lower
than a balanced FlexGroup volume. When new data is written to the
FlexGroup volume, ONTAP prioritizes distributing it among the new
constituents until the constituents are balanced. If you do add new constituents, we recommend choosing
an even number and not exceeding eight per aggregate.

###### Note

If you add new constituents, your existing snapshots become partial snapshots; therefore, they can't be used to fully restore your FlexGroup volume to a prior state.
The previous snapshots can't offer a complete point-in-time image of your FlexGroup volume because the new constituents didn't exist yet. However, the partial snapshots can be used to
restore individual files and directories, to create a new volume, or to replicate with SnapMirror.

## Volume types

FSx for ONTAP offers two types of volumes that you can create using the
Amazon FSx console, the AWS CLI, and the Amazon FSx API.

- Read-write (RW) volumes are used in most cases. As their name indicates, they are
  read-writable.
- Data protection (DP) volumes are read-only volumes that you use as the destination of a
  NetApp SnapMirror or SnapVault relationship. You should use DP volumes when
  you want to [migrate](migrating-fsx-ontap-snapmirror.md "migrating-fsx-ontap-snapmirror.md") or
  [protect](scheduled-replication.md "scheduled-replication.md") a single volume’s
  data.

FlexVol and FlexGroup volumes can be either RW or DP.

###### Note

You can't update a volume's type after the volume is created.

## Volume security style

When creating an FSx for ONTAP volume, you can choose from two security styles: Unix
and NTFS. Each security style has a different effect on how permissions are handled for
data. You must understand the different effects to ensure that you select the
appropriate security style for your purposes.

It is important to understand that security styles do not determine what client types
can or cannot access data. Security styles only determine the type of permissions FSx for ONTAP
uses to control data access and what client type can modify these permissions.

The two factors that you use to determine the security style for a volume are the type of
administrators that manage the file system and the type of users or services that
access the data on the volume.

When creating a volume in the Amazon FSx console, CLI, and API, the security style
is automatically set to the root volume's security style. You can modify a volume's
security style using the AWS CLI or API. You can modify this setting after the volume
is created. See [Updating volumes](updating-volumes.md "updating-volumes.md") for more information.

When you configure the security style on a volume, consider the needs of your
environment to ensure that you select the best security style in order to avoid
issues with managing permissions. Keep in mind that security style doesn't determine which client types can access data.
Security style determines the permissions that are used to allow data access and the client types that can modify those
permissions.
Following are considerations that can help you decide which security style to choose for a
volume:

- **Unix (Linux)** – Choose this security style if
  the file system is managed by a Unix administrator, the majority of users
  are NFS clients, and an application accessing the data uses a Unix user as
  the service account. Only Linux clients can modify permissions with the Unix
  security style, and the type of permissions used on files and directories
  are mode-bits or NFS v4.x ACLs.
- **NTFS** – Choose this security style if the file
  system is managed by a Windows administrator, the majority of users are SMB
  clients, and an application accessing the data uses a Windows user as the
  service account. If any Windows access is required to a volume, we recommend
  that you use the NTFS security style. Only Windows clients can modify
  permissions with NTFS security style, and the types of permissions used on
  file and directories is NTFS ACLs.
