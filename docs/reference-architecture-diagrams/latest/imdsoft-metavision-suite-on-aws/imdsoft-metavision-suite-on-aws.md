

# iMDSoft MetaVision Suite on AWS
<a name="imdsoft-metavision-suite-on-aws"></a>

Publication date: **November 28, 2022 ([Diagram history](#diagram-history))**

This architecture helps you deploy MetaVision Suite on AWS. MetaVision Suite by iMDSoft is a clinical information system designed to support the delivery of care in adult, neonatal, and pediatric intensive care units (ICU) with [MetaVision ICU](https://imd-soft.com/metavision/icu/), as well as anesthesia and operation theatres with [MetaVision OR](https://imd-soft.com/metavision/anesthesia/).

**Note**  
This architecture is provided for reference only, and is to be used accordingly. Actual deployment architecture will depend upon the availability of services, end customer requirements, solution features, and sizing. 

## iMDSoft MetaVision Suite on AWS Diagram
<a name="diagram1"></a>

![Reference architecture diagram showing how you can use AWS to deply MetaVision Suite.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/imdsoft-metavision-suite-on-aws/images/imdsoft-metavision-suite-on-aws.png)


1. Hospital users access MetaVision Suite using Citrix client workstations. Bedside devices communicate through a serial server with the MetaVision Integration Engine (MVIE) instance on AWS. The Emergency Data Access Workstations (EDA) provide a disaster capability in case of loss of connectivity. 

1. Hospital sites use redundant **AWS Direct Connect** connections to access AWS. Data is encrypted in transit with TLS. 

1. MetaVision Application Server is deployed on **Amazon Elastic Compute Cloud** (Amazon EC2) instances with Citrix across multiple Availability Zones (AZs). 

1. The MVIE is a communication server responsible for connectivity to hospital devices as well as other clinical and administration systems. MVIE server is hosted on **Amazon EC2** **Windows Server** instances across multiple Availability Zones, and is set up as a Windows Server Failover Cluster (WSFC) for high availability. 

1. The MetaVision Database stores data from medical devices, hospital systems and data entered by clinicians. It uses SQL Server deployed on **Amazon EC2** instances. [SQL Server Always On Failover Cluster Instances (FCIs)](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-hadr.html) are configured across Availability Zones to achieve high availability. 

1. A standalone SQL Server replica on **Amazon EC2** serves reporting requirements as well as data synchronization with EDA workstations. 

1. **Amazon FSx for Windows File Server** file shares provide shared storage for the SQL Server instances, as well as file-share witness for the Failover Cluster Instances (FCIs). 

1. Transactional replication is used to synchronize the on-premises EDA workstations continuously. 

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | November 28, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.