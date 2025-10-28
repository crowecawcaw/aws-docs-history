# Service-level agreements and SAP licenses

For a disaster recovery implementation, Service Level Agreements (SLA) are used to define how resilient your system is at avoiding loss of data and reducing downtime when your workload becomes unavailable due to a disaster event.

An SAP system disaster recovery approach requires replication of the application tier, database tier, and any file shares, such as NFS mounts. The following are some of the factors to consider for your disaster recovery implementation.

###### Topics

- [Recovery time objective (RTO)](#recovery-time "#recovery-time")
- [Recovery point objective (RPO)](#recovery-point "#recovery-point")
- [Recovery consistency objective (RCO)](#recovery-consistency "#recovery-consistency")
- [SAP licenses](#sap-licenses "#sap-licenses")

## Recovery time objective (RTO)

Recovery Time Objective (RTO) refers to how quickly can your application recover after an outage. In the event of a disaster, Elastic Disaster Recovery enables you to launch your replicated servers to a fully provisioned state at the target Region within minutes and continue operations. This automated approach supports a low RTO. It can be faster and more effective than a manual approach.

_Consideration_

As RTO is usually evaluated in the impact to business processes, other factors such as Domain Name System (DNS) propagation, environmental factors, including your disaster recovery team’s reaction time, your target environment’s storage architecture, operating system boot, and application startup times, influence this target value.

## Recovery point objective (RPO)

Elastic Disaster Recovery continuously replicates the changes to the disk at the block level asynchronously, to the target site. The RPO of Elastic Disaster Recovery is typically in the sub-second range. RPO can be influenced by external factors such as, the time taken by the source system to send changes to the staging area. This is further impacted by the volume of transactions on the source system. Other factors include network throughput and latency, source and replication server performance, etc. These factors should be measured to calculate the potential amount of data loss during a disaster recovery event.

_Consideration_

SAP workloads may from time to time may observe longer amounts of data loss than what is seen with a sub-second RPO due to how Elastic Disaster Recovery manages certain scenarios.

In the event of hard reboots, disk changes, and crashes, Elastic Disaster Recovery triggers a rescan of the disks. During the rescan, the Replication Agent does not replicate the changes of the source server to the target. This creates a lag between the two servers. If the primary system fails during this time, customers may experience a longer amount of data loss (measured in RPO) than expected.

The rescan time depends on multiple factors, and cannot be predicted without testing. A rescan may occur after a reboot of the source server. The rescan time will vary depending on the size of the source disks. The time depends on the performance of the disks (linear read), staging area disk performance, and the rate of write operations on the source server (which are sent in parallel with the rescan). The rescan is functioning normally as long as its moving forward, and is not "stuck".

SAP databases can have large disk sizes and high change rates. We recommend conducting tests to ensure that your SLA requirements are met in such events. Additionally, you must ensure that the primary and target databases are in sync during peak activity cycles.

## Recovery consistency objective (RCO)

Many disaster recovery solutions consider only RTO and RPO as SLAs for resiliency. You must also consider Recovery Consistency Objective (RCO) for your SAP workloads. RCO is a measurement for the consistency of distributed business data within interlinked systems. In a typical customer environment, SAP systems are tightly integrated and data is frequently exchanged between these systems, like SAP ECC or SAP S/4HANA, SAP BW or SAP BW/4HANA, SAP CRM, SAP SRM, SAP GTS etc. This group of tightly integrated systems is called a _system group_. In case of disaster recovery failover, you may have zero RCO requirement within the system group. This means that in case of disaster recovery failover, all of the databases within the SAP system group must be recovered to the same point-in-time.

_Consideration_

Elastic Disaster Recovery does not guarantee consistency across multiple source instances. If you have zero RCO requirement, you can use database native replication technology with point-in-time recovery or backtrack with secondary time travel.

For more information, see [SAP Note 434647 - Point-in-time recovery in an SAP system group](https://launchpad.support.sap.com/#/notes/434647 "https://launchpad.support.sap.com/#/notes/434647") (requires SAP portal access).

## SAP licenses

The SAP system is secured by a license using a hardware key. On AWS, the hardware key is based on your Amazon EC2 instance ID. Your Amazon EC2 instance must be launched before you can generate your SAP license. When you recover your SAP system in the disaster recovery site, the SAP license becomes invalid as the disaster recovery site is a new Amazon EC2 instance. The hardware key will no longer match. A temporary SAP license is created when the recovery instance is launched, and it is valid for 28 days. You do not need to create a new SAP license. If you need the disaster recovery instance to continue running after 28 days, you can request a new SAP license with the recovery Amazon EC2 instance ID.
