# Block storage (Disks)

## What can I do with Lightsail block

storage?

Lightsail block storage provides additional storage volumes (called "attached disks"
in Lightsail) that you can attach to your Lightsail instance, similar to an individual
hard drive. Attached disks are useful for applications or software that need to separate out
specific data from their core service and to protect application data in case of a failure
or other issue with your instance and system disk. Attached disks offers consistent
performance and low latency needed for applications or software that frequently access their
stored data.

Lightsail block storage disks use solid-state drives (SSD). This type of block storage
balances a low price and good performance and is intended to support the vast majority of
workloads that run on Lightsail. For customers with applications that require sustained
IOPS performance, high amounts of throughput per disk, or that are running large databases
like MongoDB, Cassandra, etc., we recommend using Amazon EC2 with GP2 or Provisioned IOPS SSD
storage instead of Lightsail.

## How are attached

disks different than the storage included in my Lightsail plan?

The system disk included with your Lightsail plan is your instance's root device. If
you terminate your instance, the system disk will be deleted as well. If you experience an
instance failure, the system disk could be impacted. You also cannot detach your system disk
or back it up separately from your instance. Data stored on an attached disk persists
independently of the instance. Attached disks can be detached and moved between instances.
They can be backed up independently from an instance by creating a manual snapshot of the
disk. To protect your data, we recommend that you use your Lightsail instance's system
disk only for temporary data. For data requiring a higher level of durability, we recommend
using attached disks and regularly backing up your disk using disk or instance snapshots.

## How large can I make my attached

disk?

Each attached disk can be up to 16 TB, and the total amount of attached block storage in
a Lightsail account must not exceed 20 TB.

## How many disks can I attach per Lightsail

instance?

You can attach up to 15 disks to a Lightsail instance.

## Can I attach a disk to more

than one instance?

No, disks can only be attached to one instance at a time.

## Does my disk need to be

attached to an instance?

No, you can choose not to attach a disk to an instance. The disk will remain in your
account in an unattached state. There is no difference in price if your disk is not attached
to an instance.

## Can I increase the size of my

attached disk?

Yes, you can increase the size of a disk by taking a disk snapshot and then creating a
new, larger disk from that snapshot.

## Does Lightsail block storage offer

encryption?

Yes, to help keep your data secure, all Lightsail attached disks and disk snapshots
are encrypted at rest by default, using keys that Lightsail manages on your behalf.
Lightsail also provides encryption of data as it moves between Lightsail instances and
attached disks.

## What availability can I expect from

Lightsail block storage?

Lightsail block storage is designed to be highly available and reliable. Each attached
disk is automatically replicated within its Availability Zone to protect you from component
failure. Lightsail block storage disks are designed for 99.99% availability. Lightsail
also supports disk snapshots to allow regular backups of your data.

## How do I back up my attached disk?

You can back up your disk by creating a manual snapshot of the disk. You can also back
up your entire instance and any attached disks by creating a manual snapshot of the
instance, or by enabling automatic snapshots for the instance with the disk attached. Disks
attached to instances are included in instance manual and automatic snapshots.
