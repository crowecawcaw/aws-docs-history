# Resilience in Amazon DocumentDB

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple
physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and
highly redundant networking. With Availability Zones, you can design and operate applications and databases that
automatically fail over between Availability Zones without interruption. Availability Zones are more highly
available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

An Amazon DocumentDB cluster can only be created in an Amazon VPC that has at least two subnets in at least two Availability
Zones. By distributing your cluster instances across at least two Availability Zones, Amazon DocumentDB helps ensure that
there are instances available in your cluster in the unlikely event of an Availability Zone failure. The cluster
volume for your Amazon DocumentDB cluster always spans three Availability Zones to provide durable storage with less
possibility of data loss.

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

In addition to the AWS global infrastructure, Amazon DocumentDB offers several features to help support your data
resiliency and backup needs.

**Fault-tolerant and self-healing storage**
Each 10 GB portion of your storage volume is replicated six ways, across three Availability
Zones. Amazon DocumentDB uses fault-tolerant storage that transparently handles the loss of up
to two copies of data without affecting database write availability, and up to three
copies without affecting read availability. Amazon DocumentDB storage is also self-healing;
data blocks and disks are continuously scanned for errors and replaced
automatically.

**Manual backups and restore**

Amazon DocumentDB provides the capability to create full backups of your cluster for
long-term retention and recovery. For more information, see [Backing up and restoring in Amazon DocumentDB](backup_restore.md "backup_restore.md").

**Point-in-time recovery**

Point-in-time recovery helps protect your Amazon DocumentDB clusters from accidental write or delete operations. With
point-in-time recovery, you don't have to worry about creating, maintaining, or scheduling on-demand backups.
For more information, see [Restoring to a point in time](backup_restore-point_in_time_recovery.md "backup_restore-point_in_time_recovery.md").
