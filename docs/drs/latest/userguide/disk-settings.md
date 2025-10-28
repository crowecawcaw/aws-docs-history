# AWS DRS disk settings

The **Disk settings** tab shows a list of all of the disks on
the source server and information for each disk:

- **Disk name**
- **Staging disk type** – The corresponding Amazon EBS volume
  disk type that is being used for the disk.
- **Replicated storage** – The amount of storage that has been
  replicated from the disk to the Replication Server.
- **Total storage** – The total storage capacity of the
  disk.
- **Status** – shows the status of each disk, values can be
  either **Normal**, **Normal with
  marketplace license**, **Error** (with error
  description). Normal with marketplace license means that the server has at least one
  marketplace license associated with this volume. Volumes with marketplace licenses pose
  some limitations on launch: the target region and the selected instance type must
  support this license. If launching into a different account, the marketplace product
  must be subscribed to in that account as well or the launch fails. The state is set to
  Error if there is a problem with the volume, such as not having permissions to read the
  marketplace license details if the server is owned by a different AWS account. The value
  can also be empty if the status is not known at this time.

## Change staging disk type

You can change the EBS volume disk type for each disk or for a group of disks. To change
the EBS volume disk type:

1. Select the circle to the left of each disk name and choose **Change
   staging disk type**.
2. On the **Change staging disk type** dialog, select the type
   of EBS volume to use for the disk or group of disks.
3. Select the **AUTO** option if your volume's size is greater than 125 GiB and you want AWS Elastic Disaster Recovery to automatically
   select the most cost-effective EBS volume disk type for each
   disk based on the disk size and type based on the option you defined in the **Replication settings** (either the default **Lower cost, Throughput Optimized HDD (st1)** option or the **Faster, General Purpose SSD (gp2) or (gp3)** s option).

AWS Elastic Disaster Recovery uses a single Replication Server per 15 source disks. Selecting the **Auto** option ensures that the fewest number of replication servers
are used, resulting in increased cost savings.

###### Note

AWS Elastic Disaster Recovery always uses EBS magnetic volumes for disks that are under 125 GiB in size when
you choose the **Auto** option.

If you do not want AWS Elastic Disaster Recovery to automatically select a disk, you can
select a disk manually. Select the disk type from the **EBS volume
type** menu.

For certain disks, you can configure the amount of IOPS to be allocated per GB of disk
space under **IOPS**. You can allocate up to 50 IOPS per GB.
64,000 IOPS are available for Nitro-based instances. Other instances are guaranteed up to
32,000 IOPS. The maximum IOPS per instance is 80,000.

Choose **Change** to confirm the change.
