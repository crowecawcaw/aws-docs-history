NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Change staging disk type

You can change the EBS volume disk type for each disk or for a group of disks.

To change the EBS volume disk type, select the circle to the left of each disk name and
choose **Change staging disk type**.

On the **Change staging disk type** dialog, select the type
of EBS volume to use for the disk or group of disks.

Select the **AUTO** option if you want AWS Application Migration Service to
automatically select the most cost-effective EBS volume disk type for each disk based on the
disk size and type based on the option you defined in the **Replication
settings** (either the default **Lower cost, Throughput Optimized
HDD (st1)** option or the **Faster, General Purpose SSD
(gp3)** option).

AWS Application Migration Service uses a single replication server per 15 source disks. Selecting the **AUTO** option ensures that the fewest number of replication servers
are used, resulting in increased cost savings.

###### Note

AWS Application Migration Service always uses EBS magnetic volumes for disks that are under 500 GiB in size
when the **AUTO** option is selected.

If you do not want AWS Application Migration Service to automatically select a disk, you can select a disk
manually. Select the disk type from the**EBS volume type** menu.

###### Note

When replicating into an AZ, ensure that the AZ supports the staging disk type chosen.

For certain disks, you can configure the amount of IOPS to be allocated per GB of disk
space under **IOPS**. You can allocate up to 50 IOPS per GB.
64,000 IOPS are available for Nitro-based instances. Other instances are guaranteed up to
32,000 IOPS. The maximum IOPS per instance is 80,000.

Choose **Change** to confirm the change.

For **General Purpose SSD (gp3)** disks, you'll also be able
to set the **Throughput**. General Purpose SSD (gp3) volumes have
a baseline performance of 125 MiB/s. You can provision additional throughput of 0.25 MiB/s per
provisioned IOPS up to a maximum of 1,000 MiB/s (at 4,000 IOPS or higher).

Choose **Change** to confirm the change.
