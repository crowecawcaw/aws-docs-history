# Amazon EBS persistent block storage for Amazon EC2 instances

Amazon Elastic Block Store (Amazon EBS) provides scalable, high-performance block storage resources that can be used
with Amazon EC2 instances. With Amazon EBS, you can create and manage the following block storage
resources:

- Amazon EBS volumes — These are storage volumes that
  you attach to Amazon EC2 instances. After you attach a volume to an instance, you can use it
  in the same way you would use block storage. The instance can interact with the volume
  just as it would with a local drive.
- Amazon EBS snapshots — These are point-in-time backups of
  Amazon EBS volumes that persist independently from the volume itself. You can create snapshots
  to back up the data on your Amazon EBS volumes. You can then restore new volumes from those
  snapshots at any time.
  You can create and attach EBS volumes to an instance during launch, and you can create and
  attach EBS volumes to an instance at any time after launch. You can also increase the size or
  performance of your EBS volumes without detaching the volume or restarting your instance.

You can create EBS snapshots from an EBS volume at any time after creation. You can use
EBS snapshots to back up the data stored on your volumes. You can then use those snapshots
to instantly restore volumes, or to migrate data across AWS accounts, AWS Regions, or
Availability Zones. You can use Amazon Data Lifecycle Manager or AWS Backup to automate the creation, retention,
and deletion of your EBS snapshots.

A _managed EBS volume_ is managed by a service provider,
such as Amazon EKS Auto Mode. You can’t directly modify the settings of a managed EBS volume.
Managed EBS volumes are identified by a **true** value in the
**Managed** field. For more information, see [Amazon EC2 managed instances](amazon-ec2-managed-instances.md "amazon-ec2-managed-instances.md").

For more information about working with volumes and snapshots, see the [Amazon EBS User Guide](../../../ebs/latest/userguide/what-is-ebs.md "../../../ebs/latest/userguide/what-is-ebs.md").
