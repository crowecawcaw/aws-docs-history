# Shared storage resiliency

File systems on an SAP server can be created on block type storage, for instance, on locally attached disks or Enterprise Storage Area Network (SAN) devices, or may be based on shared file systems such as SMB or NFS shared volumes from servers or Network Attached Storage (NAS) devices.

As Elastic Disaster Recovery is a block level replication service, it only replicates the disks if they are represented as block storage devices. Other tools and processes must be used to provide resiliency for shared file systems. To address these requirements, we recommend using the fully managed shared storage services of AWS that are easy and cost-effective to launch, run, and scale feature-rich, high performance, and resilient file systems in the cloud. The choice of your file system depends on the operating system of your disaster recovery scenario.

- Linux – [Amazon Elastic File System](https://aws.amazon.com/efs/ "https://aws.amazon.com/efs/") (Amazon EFS)
- Microsoft Windows Server – [Amazon FSx for Windows File Server](https://aws.amazon.com/fsx/windows/ "https://aws.amazon.com/fsx/windows/") (Amazon FSx)
- Mixed – Amazon FSx for Windows File Server or [Amazon FSx for NetApp ONTAP](https://aws.amazon.com/fsx/netapp-ontap/ "https://aws.amazon.com/fsx/netapp-ontap/") (FSx for ONTAP)
  The following sections provide guidance on file systems based on your disaster recovery scenario.

###### Topics

- [AWS In-Region disaster recovery](#file-systems-same-region "#file-systems-same-region")
- [AWS Cross-Region disaster recovery](#file-systems-different-regions "#file-systems-different-regions")
- [Outside of AWS to AWS disaster recovery](#file-systems-other-aws "#file-systems-other-aws")

## AWS In-Region disaster recovery

When using managed services such as Amazon EFS, FSx for ONTAP or FSx for Windows File Server to host your shared file systems, the built-in resiliency offered through their multi-Availability Zone design means that your shared storage is already disaster recovery ready. For further resiliency, ensure that your shared storage is backed up regularly, to protect against potential data corruption.

If you are sharing a file system using NFS or SMB protocols directly from one of your Amazon EC2 instances, you may not need additional steps if it is on Amazon EBS and attached to a server with the Replication Agent. This ensures replication via Elastic Disaster Recovery. If the shared file system is hosted on another Amazon EC2 instance along with other content that is not part of your SAP workload, use OS native tools like `rsync` to manage the replication of this file system to the recovery area.

You can also use AWS DataSync to provide selective replication. It can be scheduled to run once an hour at minimum, and replicate these files to the target storage in the recovery area. You must have an additional agent installed on an Amazon EC2 instance that has access to the file system. For more information, see [How AWS DataSync works](../../../datasync/latest/userguide/create-task.md#configure-scheduling-queueing "../../../datasync/latest/userguide/create-task.md#configure-scheduling-queueing").

## AWS Cross-Region disaster recovery

To support cross-Region disaster recovery, another shared file system must be available in the second Region. The data from the primary shared file system must be replicated on the shared file system in the second Region. Your implementation will differ based on your choice of AWS service.

- Amazon Elastic File System – Amazon EFS native replication can support cross-Region replication within a single AWS account.
- Amazon FSx for Windows File Server – You can also use AWS DataSync to replicate data between your primary to secondary shared storage. For more information, see [How AWS DataSync works](../../../datasync/latest/userguide/create-task.md#configure-scheduling-queueing "../../../datasync/latest/userguide/create-task.md#configure-scheduling-queueing").
- Amazon FSx for NetApp ONTAP – You can use NetApp SnapMirror to copy your files between FSx for ONTAP file systems on your source and target instances, as frequently as every 5 minutes, to maintain a current copy of your shared file systems. For more information, see [Scheduled replication using NetApp SnapMirror](../../../fsx/latest/ONTAPGuide/scheduled-replication.md "../../../fsx/latest/ONTAPGuide/scheduled-replication.md").

## Outside of AWS to AWS disaster recovery

Depending on your source area design for shared storage, you must consider replicating these files on your disaster recovery instance in AWS. We recommend using [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/"). It can copy data to and from services, such as NFS and SMB shares, along with file systems using Amazon EFS, FSx for Windows File Server, and FSx for ONTAP.

In certain scenarios, you can consider using other options to protect your source area SAP shared file systems, such as if the following is being used on your source environment.

- FSx for ONTAP – You can use NetApp SnapMirror to copy your files between FSx for ONTAP file systems on your source and target instances, as frequently as every 5 minutes, to maintain a current copy of your shared file systems. For more information, see [Scheduled replication using NetApp SnapMirror](../../../fsx/latest/ONTAPGuide/scheduled-replication.md "../../../fsx/latest/ONTAPGuide/scheduled-replication.md").
- Local storage – Elastic Disaster Recovery will replicate it to your disaster recovery environment on AWS, if Replication Agent can be configured on the source server hosting the local storage.
