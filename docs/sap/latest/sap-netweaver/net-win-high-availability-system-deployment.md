# High Availability System Deployment

High availability (HA) system: used for business-critical applications. With this option, all the services that are single points of failure are deployed across multiple Availability Zones for fault tolerance.

For SAP NetWeaver, the key single points of failure are:

- the central services (ASCS/SCS)
- the global and transport filesystems
  To protect against hardware failure of Amazon EC2 within an Availability Zone, you can enable EC2 instance recovery. See [Recover Your Instance](../../../AWSEC2/latest/UserGuide/ec2-instance-recover.md "../../../AWSEC2/latest/UserGuide/ec2-instance-recover.md") for more details on this feature. You can use scripts to start the SAP NetWeaver application automatically after instance recovery. You can further configure SAP application work processes to reconnect to your database after recovery. Consult the documentation for further restrictions. This option is not application aware and does not protect the application against Availability Zone failure, which makes it a good option for non-production systems. It also can be used for production systems but you might want to consider a Multi-AZ solution for this situation as well.

For HA solutions, it’s important to be aware of two concepts within a VPC: shared storage and the Overlay IP address.

## Shared Storage

EBS volumes are specific to a single Availability Zone and can only be attached to a single EC2 instance at a time. However, in distributed or HA deployments, shared storage is required for the global and transport filesystems. On AWS, this storage can be provided by building an NFS server or by using Amazon FSx. Amazon FSx provides shared file storage with full support for the SMB protocol, Windows NTFS, Active Directory integration, and Distributed File System (DFS).

If using such a solution in the context of a high availability installation, the shared storage solution you choose could introduce a single point of failure without appropriate protection. This can be protected against by:

- Clustering the NFS server providing the shared filesystem
- Clustering the host that is sharing the filesystems
- Using Amazon FSx. For workloads that require Multi-AZ redundancy to tolerate temporary AZ unavailability, you can [create multiple ﬁle systems in separate AZs](../../../fsx/latest/WindowsGuide/multi-az-deployments.md "../../../fsx/latest/WindowsGuide/multi-az-deployments.md"). Amazon FSx supports Microsoft’s Distributed File System (DFS) Replication and Namespaces. DFS Replication allows you to automatically replicate data between two file systems, and DFS Namespaces allows you to configure automatic failover.

## High availability

You can use a high availability (HA) clustering solution for autonomous failover of the central services across Availability Zones. There are multiple SAP-certified options for this clustering software on Windows [listed on the SAP website](https://wiki.scn.sap.com/wiki/display/SI/Certified+HA-Interface+Partners "https://wiki.scn.sap.com/wiki/display/SI/Certified+HA-Interface+Partners"), and it’s also possible to build and automate your own solution. HA solutions that have been tested and are known to work on AWS include:

- Veritas InfoScale:
  - [Veritas InfoScale for SAP on AWS](https://www.veritas.com/content/support/en_US/doc/infoscale_hadr_sap_netweaver_aws "https://www.veritas.com/content/support/en_US/doc/infoscale_hadr_sap_netweaver_aws")
  - [Veritas InfoScale for Windows compatibility list](https://www.veritas.com/content/support/en_US/doc/infoscale_scl_741_win "https://www.veritas.com/content/support/en_US/doc/infoscale_scl_741_win")

- SIOS:
  - [SIOS DataKeeper](https://us.sios.com/solutions/sap-high-availability/ "https://us.sios.com/solutions/sap-high-availability/") with Windows Server Failover Cluster (WSFC)
  - [SIOS DataKeeper Cluster Edition on AWS Quick Start](https://aws.amazon.com/quickstart/architecture/sios-datakeeper/ "https://aws.amazon.com/quickstart/architecture/sios-datakeeper/")
  - SAP on AWS Blog: [Implementing HA and DR for Microsoft SQL Server](https://aws.amazon.com/blogs/architecture/field-notes-implementing-ha-and-dr-for-microsoft-sql-server-using-always-on-failover-cluster-instance-and-sios-datakeeper/ "https://aws.amazon.com/blogs/architecture/field-notes-implementing-ha-and-dr-for-microsoft-sql-server-using-always-on-failover-cluster-instance-and-sios-datakeeper/")

- NEC ExpressCluster
- Windows Server Failover Cluster (WSFC) with native Windows and AWS services
  - SAP on AWS Blog: [How to setup SAP NetWeaver on Windows MSCS for SAP ASCS/ERS on AWS](https://aws.amazon.com/blogs/awsforsap/how-to-setup-sap-netweaver-on-windows-mscs-for-sap-ascs-ers-on-aws-using-amazon-fsx/ "https://aws.amazon.com/blogs/awsforsap/how-to-setup-sap-netweaver-on-windows-mscs-for-sap-ascs-ers-on-aws-using-amazon-fsx/")

###### Support and certification

SAP clustering software is supported by the cluster software vendors themselves, not by SAP. SAP only certifies the solution. Any custom-built solution is **not** certified and will need to be supported by the solution builder.

In this guide, we focus on the distributed installation type on Windows in AWS. More details on how to deploy and operate SIOS, Veritas, and WSFC clusters are available on their respective websites linked above. For effective use of WSFC, Windows Server 2016, or later, is required.

The key features to be aware of with the WSFC solution are:

- ASCS and a separate ERS instance set up within Windows Cluster Manager
- [Scale-Out File Server](https://docs.microsoft.com/en-us/windows-server/failover-clustering/sofs-overview "https://docs.microsoft.com/en-us/windows-server/failover-clustering/sofs-overview") is a feature that is designed to provide scale-out file shares that are continuously available for file-based server application storage
- Storage Spaces Direct uses standard servers with local-attached drives to create highly available, highly scalable software-defined storage. **This requires a minimum of Windows Server 2016 and NVMe storage (so nitro-generation EC2 instances are required).**
- Amazon FSx for Windows File Server

Also read the High Availability with Microsoft Failover Clustering section of the SAP NetWeaver installation guide.
