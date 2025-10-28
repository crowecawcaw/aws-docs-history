# Implementing disaster recovery on AWS cloud for SAP workloads

Using Elastic Disaster Recovery to implement a disaster recovery solution for SAP workloads on AWS follows different considerations for different parts of a typical SAP workload, such as S/4HANA deployment. The following sections provide guidance on the differences in how to design, implement, and manage Elastic Disaster Recovery when used for the application and the database layers.

###### Topics

- [SAP application layer](#application-layer "#application-layer")
- [SAP database layer](#database-layer "#database-layer")

## SAP application layer

We recommend using AWS Elastic Disaster Recovery to protect your SAP application servers, such as SAP ASCS/SCS, PAS, AAS etc. Elastic Disaster Recovery supports the SAP application layer based on SAP NetWeaver, ABAP foundation, and stand-alone applications like TREX, content servers, and so on. You can use Elastic Disaster Recovery for Amazon EBS backed storages, such as SAP instance binaries, local files stored on an Amazon EBS volume.

The application layer also contains shared file systems, such as SAP mount, transport, and interface directories. These file systems usually need to be managed separately. For more information, see [Shared storage resiliency](file-systems-storage.md "file-systems-storage.md").

To setup, install Elastic Disaster Recovery agent on the application servers. Create an IAM user with required permissions. Provide Elastic Disaster Recovery agent with the user information to establish a connection with Elastic Disaster Recovery APIs. Once the agent is configured, it engages in an authentication handshake with the TLS 1.3-encrypted Elastic Disaster Recovery API endpoint. The service produces identically sized Amazon EBS volumes in the staging area subnet, for each source volume that is duplicated, for data synchronization. The type of Amazon EBS volumes can be configured in the replication server settings. Replication starts after the staging area subnet resources are generated and the agent is installed. The data is transported with encryption from the source servers to the replication server directly. The service automatically manages the subnet resources for the staging area, scaling them up or down based on the concurrent replication of the source servers and disks.

## SAP database layer

AWS Elastic Disaster Recovery is fully supported as disaster recovery solution for SAP applications running on any database, and for SAP applications running on SAP HANA database in scale-up configuration. It is not supported for replication of multi-node SAP databases, such as SAP HANA scale-out cluster.

The data in an SAP system is stored in a database. This data includes master data, transactional data, and ABAP artifacts. You must consider your business RPO and RTO requirements when evaluation Elastic Disaster Recovery for a disaster recovery solution. The service is not application aware but works at the operating system layer by replicating the attached storage to the target staging environment. Based on your RTO and RPO requirements, you can select Elastic Disaster Recovery or database native replication methods, such as SAP HANA System Replication (HSR) for SAP HANA.

The following are the important considerations to choose your database replication method.

###### Topics

- [Network bandwidth](#network-bandwidth "#network-bandwidth")
- [RPO](#rpo "#rpo")
- [Change rate](#change-rate "#change-rate")
- [RTO](#rto "#rto")
- [Cost](#cost "#cost")
- [RCO](#rco "#rco")
- [Storage limits](#storage-limits "#storage-limits")

### Network bandwidth

AWS Elastic Disaster Recovery works at the operating system layer, with block level replication of attached storage devices. Depending on the change rate at the source, you may need higher network bandwidth to stay current with replication. Database aware technologies such as SAP HSR require lesser network bandwidth, enabling faster replications for systems with high rate of change.

### RPO

Elastic Disaster Recovery supports sub-second RPO. For SAP workloads, ensure that your network can support peaks in change rate. If your RPO is very small, we recommend testing database native replication methods along with Elastic Disaster Recovery.

Actions that lead to significant changes to the data of your database cause delays data replication on staging area. It can include a partial or full recovery of a backup to protected volumes for a database on source server. The changes made to your storage volumes are much higher than your usual change rates on source server. Data restored from backup to protected volumes on the source server is treated as changed blocks and is replicated by Elastic Disaster Recovery. The replication servers need additional time to receive and write this larger amount of changed data from the source system. This can impact your business RPO.

It is recommended to manage actions, such as recovery from backups, at less critical workload times. This way, longer RPO values won’t impact your workload. You can track the amount of changed data still waiting to be replicated with Elastic Disaster Recovery. For more information, see [Recovery dashboard](../../../drs/latest/userguide/recovery-dashboard.md "../../../drs/latest/userguide/recovery-dashboard.md").

### Change rate

For databases with high change rates, you can meet the performance requirements with sufficiently performing networks, along with the storage and compute configuration of the replication server. If these changes are insufficient to meet the business performance requirements, you can choose database native replication methods to optimize your RPO.

### RTO

With Elastic Disaster Recovery, the target disaster recovery environment is provisioned once the disaster recovery event is triggered. The total time depends on the size of your database, and the chosen Point-in-Time (PiT). You must test your disaster recovery scenario before implementation on production environments.

### Cost

As Elastic Disaster Recovery is not using a warm or hot standby approach, the compute costs are minimized for your disaster recovery environment as compared to many other disaster recovery options. For more information, see [AWS Elastic Disaster Recovery pricing](https://aws.amazon.com/disaster-recovery/pricing/ "https://aws.amazon.com/disaster-recovery/pricing/"). With database native replication methods, costs can increase with the compute resources in the disaster recovery area.

### RCO

If you have multiple tightly coupled systems, then you need to use database native replication methods.

### Storage limits

In most cases, the available Amazon EBS volume types are sufficient to address any storage capacity and performance needs. Depending on the source environment architecture, in some cases, the storage volume on the recovery instance exceeds the capacity and/or performance limits of individual Amazon EBS volumes. This can happen in a non-AWS to AWS disaster recovery implementation with `data` and `log` volumes attached to high workload database servers. For more information, see [Amazon EBS volume types](https://docs.aws.amazon.comAWSEC2/latest/UserGuide/ebs-volume-types.html "https://docs.aws.amazon.comAWSEC2/latest/UserGuide/ebs-volume-types.html").

When migrating servers to AWS, such storage volumes must be refactored to a new storage architecture, for instance, creating striped volume sets. Striped volume sets are defined and maintained using logical volume manager tools in your recovery instance’s operating system. For more information, see [RAID configuration on Linux](https://docs.aws.amazon.comAWSEC2/latest/UserGuide/raid-config.html "https://docs.aws.amazon.comAWSEC2/latest/UserGuide/raid-config.html"). These volume sets will span two or more Amazon EBS volumes, up to the total needed to meet the required volume size and performance. The storage volume data is then copied to the new striped volume set. While it may be possible to automate this process through Elastic Disaster Recovery post-launch scripts or alarm events which trigger code through Amazon EventBridge event rules, the additional steps can cause longer recovery time.

In these cases, implementing a hybrid disaster recovery solution is suitable. Most of the servers are managed by Elastic Disaster Recovery and select servers (with storage performance considerations) use alternative disaster recovery approaches, such as native database replication technologies. The storage architecture refactoring is done when the standby replication server is set up during the initial disaster recovery environment implementation. As the replication now happens at an application level, the disaster recovery server is able to write to a storage architecture that is different from what is on the source server.
