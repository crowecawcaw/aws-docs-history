# Third-party block storage on

Outposts servers

With Outposts servers, you can leverage existing data you're stored on
third-party storage arrays. You can specify external block data volumes and external block boot
volumes for your EC2 instances on Outposts. Using this integration, you can use external block
data and boot volumes backed by third-party vendors such as, Dell PowerStore, HPE Alletra Storage
MP B10000, NetApp on-premises enterprise storage arrays, and Pure Storage FlashArray storage
systems.

###### Considerations

- Available on Outposts racks and Outposts 2U servers. Not available on Outposts 1U servers.
- Available in all AWS Regions where Outposts 2U servers are supported.
- Available at no extra charge.
- You are responsible for the configuration and day-to-day management of the storage array.
  You also create and manage the external block volumes on the storage array. If you have issues
  with the hardware, software, or connectivity for the storage array, contact the third-party
  storage vendor.

###### Note

The block volume stored on your external storage array contains the
operating system that will be booted into an EC2 instance on Outposts. Launching an AMI that is
backed by external storage arrays is not supported. To launch an AMI, the instance storage on the
Outposts server is used.

## External block data volumes

After you provision and configure block data volumes backed by a compatible third-party
storage system, you can attach the volumes to your EC2 instances when you launch them. If you
configure the volumes for multi-attach on the storage array, you can attach a volume to multiple
EC2 instances.

###### Key steps

- You are responsible for establishing connectivity between the Outpost subnets and the
  local network through the [local network
  interface](local-network-interface.md "local-network-interface.md").
- You use the management interface for the external storage array to create the volume.
  Then, you'll configure the initiator mapping by created a new Initiator Group and adding the
  iSCSI Qualified Name (IQN) of the target EC2 instance to this group. This associates the
  external block data volume with the EC2 instance.
- You add the external data volume when you launch the instance. You'll need the Initiator
  IQN, the target IP address, the port, and the IQN of the external storage array. For more
  information, see [Launch an instance on the
  Outpost](launch-instance.md#launch-instances "launch-instance.md#launch-instances").

For more information, see [Simplifying the use of third-party block storage with AWS Outposts](https://aws.amazon.com/blogs/compute/new-simplifying-the-use-of-third-party-block-storage-with-aws-outposts/ "https://aws.amazon.com/blogs/compute/new-simplifying-the-use-of-third-party-block-storage-with-aws-outposts/").

## External block boot volumes

Booting an EC2 instance on Outposts from external storage arrays provides a centralized,
cost-effective, and efficient solution for on-premises workloads that depend on third-party
storage. You can choose between the following options:

**iSCSI SAN boot**

Provides direct booting from the external storage array. Utilizes an AWS-provided iPXE
helper AMI so that the instances can boot from a network location. When iPXE is combined with
iSCSI, the EC2 instance treats the remote iSCSI target (the storage array) as a local disk.
All read and write operations from the operating system are performed on the external storage
array.

**iSCSI or NVMe-over-TCP LocalBoot**

Launches EC2 instances using a copy of the boot volume retrieved from the storage array,
leaving the original source image unmodified. We launch a helper instance using a LocalBoot
AMI. This helper instance copies the boot volume from the storage array to the instance store
of the EC2 instance, and acts as an iSCSI initiator or NVMe-over-TCP host. Finally, the EC2
instance reboots using the local instance store volume.

Because instance store is temporary storage, the boot volume is deleted when the EC2
instance is terminated. Therefore, this option is suitable for read-only boot volumes, such as
those used in virtual desktop infrastructure (VDI).

You can't boot EC2 Windows instances using NVMe-over-TCP LocalBoot. This is only
supported using EC2 Linux instances.

For more information, see [Deploying external boot volumes
for use with AWS Outposts](https://aws.amazon.com/blogs/compute/deploying-external-boot-volumes-with-aws-outposts/ "https://aws.amazon.com/blogs/compute/deploying-external-boot-volumes-with-aws-outposts/").
