# SAP on AWS cost estimation

_Last updated: May 2023_

AWS offers pay-as-you-go pricing. You only pay for the services you use, for as long as you use them. There are no long-term contracts or complex licensing requirements. For more information, see [AWS Pricing](https://aws.amazon.com/pricing "https://aws.amazon.com/pricing") and [https://calculator.aws/#/](https://calculator.aws/#/ "https://calculator.aws/#/").

The following is an overview of the pricing characteristics of AWS services that are frequently used for the deployment and operation of SAP systems on AWS.

###### Topics

- [AWS Region](#aws-region-pricing "#aws-region-pricing")
- [Compute](#compute-pricing "#compute-pricing")
- [Storage](#storage-pricing "#storage-pricing")
- [Network](#network-pricing "#network-pricing")
- [Automation](#automation "#automation")
- [Backup, restore, and recovery](#backup "#backup")
- [Migration](#migration "#migration")
- [Monitoring](#monitoring "#monitoring")
- [Operating System licenses](#os-licenses "#os-licenses")
- [AWS Marketplace](#marketplace "#marketplace")
- [AWS Support](#aws-support-pricing "#aws-support-pricing")

## AWS Region

AWS service pricing varies between different AWS Regions. You must select the Region in which you want to deploy your SAP system to begin creating an estimate. For more information, see [Regions and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/").

## Compute

[Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.comAWSEC2/latest/UserGuide/concepts.html "https://docs.aws.amazon.comAWSEC2/latest/UserGuide/concepts.html") provides a wide selection of instance types that provide varying combinations of CPU, memory, storage, I/O, and networking capabilities. Each running instance is charged by the hour. For more information, see [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/").

Amazon EC2 offers multiple purchasing options that give you flexibility to optimize your costs. For more information, see [Instance purchasing options](https://docs.aws.amazon.comAWSEC2/latest/UserGuide/instance-purchasing-options.html "https://docs.aws.amazon.comAWSEC2/latest/UserGuide/instance-purchasing-options.html").

## Storage

The following AWS services are flexible, cost-effective, and easy-to-use data storage options available for your SAP systems. Each option has a unique combination of performance and durability. For more information, see [Cloud storage on AWS](https://aws.amazon.com/products/storage/ "https://aws.amazon.com/products/storage/").

###### Topics

- [Amazon EBS](#ebs "#ebs")
- [Amazon EFS](#efs "#efs")
- [Amazon FSx for Windows File Server](#fsx "#fsx")
- [Amazon FSx for NetApp ONTAP](#fsx-ontap "#fsx-ontap")
- [Amazon S3](#s3 "#s3")

### Amazon EBS

[Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.comAWSEC2/latest/UserGuide/AmazonEBS.html "https://docs.aws.amazon.comAWSEC2/latest/UserGuide/AmazonEBS.html") provides persistent, block-level storage volumes for Amazon EC2 instances. Each Amazon EC2 instance that runs an SAP environment requires one or more Amazon EBS volumes to store system components, such as operating system, SAP software, SAP database data and log files, and local backup storage.

With Amazon Elastic Block Store, you only pay for what you provision. For more information, see [Amazon EBS pricing](https://aws.amazon.com/ebs/pricing/ "https://aws.amazon.com/ebs/pricing/").

**Amazon EBS snapshots**

Amazon EBS snapshots are point-in-time copies of your block data stored in Amazon EBS volumes. Amazon EBS snapshots in the Standard tier are stored incrementally, which means you are billed only for the changed blocks stored. Amazon EBS snapshots in the Archive tier are full copies of your block data, which means you are billed for all the blocks stored and not just the changed blocks.

You can also enable a Recycle Bin feature to protect against accidental deletion. Amazon EBS snapshots in the recycle bin are billed at the same rate.

Another feature of Amazon EBS snapshots which is applicable to SAP workloads is the Fast Snapshot Restore (FSR). This feature enables you to promptly restore fully provisioned Amazon EBS volumes from snapshots, regardless of the size of the volume or snapshot. FSR is charged in Data Services Unit-Hours (DSU-Hours) for each snapshot and each Availability Zone in which it is enabled. DSUs mean that you are billed per minute with a one-hour minimum.

Amazon EBS snapshots can be used for both root and binary volumes of your SAP system as well as database volumes.

### Amazon EFS

[Amazon Elastic File System (Amazon EFS)](../../../efs/latest/ug/whatisefs.md "../../../efs/latest/ug/whatisefs.md") provides serverless file storage. You can share file data without provisioning or managing storage capacity and performance. Amazon EFS is built to scale on demand to petabytes without disrupting applications, growing and shrinking automatically as you add and remove files. You can create and configure file systems quickly and easily.

Amazon EFS stores every object across multiple Availability Zones, making it highly available. It supports the Network File System version 4 (NFSv4.1 and NFSv4.0) protocol. It is certified for SAP file shares, and it can also be used for storing data files in your SAP landscape.

With Amazon EFS, you pay only for the storage used by your file system, and there is no minimum fee or setup cost. For more information, see [Amazon EFS pricing](https://aws.amazon.com/efs/pricing/ "https://aws.amazon.com/efs/pricing/").

### Amazon FSx for Windows File Server

[Amazon FSx for Windows File Server](../../../fsx/latest/WindowsGuide/what-is.md "../../../fsx/latest/WindowsGuide/what-is.md") provides fully managed Microsoft Windows file servers, backed by a fully native Windows file system. It has support for Windows file system features and for the industry-standard Server Message Block (SMB) protocol to access file storage over a network.

FSx for Windows File Server is certified for SAP workloads on AWS, and can also be used for Windows based data file sharing in your SAP landscape.

With FSx for Windows File Server, you only pay for the resources you use, and there is no minimum fee or setup cost. For more information, see [Amazon FSx for Windows File Server pricing](https://aws.amazon.com/fsx/windows/pricing/ "https://aws.amazon.com/fsx/windows/pricing/").

### Amazon FSx for NetApp ONTAP

[Amazon FSx for NetApp ONTAP](../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md "../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md") is a fully managed service that provides highly reliable, scalable, high-performing, and feature-rich file storage built on NetApp’s popular ONTAP file system.

FSx for ONTAP is certified for SAP workloads on AWS.

You are billed for the file systems you use, based on the following categories.

- SSD storage capacity (per gigabtye-month, or GB-month)
- SSD IOPS that you provision above three IOPS/GB (per IOPS-month)
- Throughput capacity (per megabytes per second [MBps]-month)
- Capacity pool storage consumption (per GB-month)
- Capacity pool requests (per read and write)
- Backup storage consumption (per GB-month)

For more information, see [Amazon FSx for NetApp ONTAP pricing](https://aws.amazon.com/fsx/netapp-ontap/pricing/ "https://aws.amazon.com/fsx/netapp-ontap/pricing/").

### Amazon S3

[Amazon Simple Storage Service (Amazon S3)](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md") is an object storage service that offers industry-leading scalability, data availability, security, and performance. You can use Amazon S3 to stage media, store backups, and archive data. Amazon S3 offers a range of storage classes designed for different use cases.

Amazon S3 charges you only for what you actually use, with no hidden fees and no overage charges. This model gives you a variable-cost service that can grow with your business while giving you the cost advantages of AWS infrastructure. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing "https://aws.amazon.com/s3/pricing").

## Network

AWS offers multiple strong and secure networking services.

###### Topics

- [Amazon VPC](#vpc "#vpc")
- [AWS Site-to-Site VPN](#vpn "#vpn")
- [AWS Direct Connect](#direct-connect "#direct-connect")
- [Elastic Load Balancing](#elb "#elb")
- [Data transfer pricing](#data-transfer "#data-transfer")

### Amazon VPC

With [Amazon Virtual Private Cloud (Amazon VPC)](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md"), you can launch AWS resources in a logically isolated virtual network that you’ve defined. This virtual network closely resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

There’s no additional charge for using Amazon VPC. There are charges for some components, such as NAT gateways, IP Address Manager, traffic mirroring, Reachability Analyzer, and Network Access Analyzer. For more information, see [Amazon VPC pricing](https://aws.amazon.com/vpc/pricing/ "https://aws.amazon.com/vpc/pricing/").

Use the following options for a secure connection between your on-premises network and Amazon VPC.

- [AWS Transit Gateway](../../../vpc/latest/tgw/what-is-transit-gateway.md "../../../vpc/latest/tgw/what-is-transit-gateway.md") is a network transit hub that you can use to interconnect your virtual private clouds (VPCs) and on-premises networks. As your cloud infrastructure expands globally, inter-Region peering connects transit gateways together using the AWS Global Infrastructure. Your data is automatically encrypted and never travels over the public internet.

You are charged hourly for each attachment on a transit gateway, and you are charged for the amount of traffic processed on the transit gateway. For more information, see [AWS Transit Gateway pricing](https://aws.amazon.com/transit-gateway/pricing/ "https://aws.amazon.com/transit-gateway/pricing/").

- [NAT gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") is a Network Address Translation (NAT) service. You can use a NAT gateway so that instances in a private subnet can connect to services outside your VPC but external services cannot initiate a connection with those instances.

When you provision a NAT gateway, you are charged for each hour that your NAT gateway is available and each Gigabyte of data that it processes. For more information, see [Amazon VPC pricing](https://aws.amazon.com/vpc/pricing/ "https://aws.amazon.com/vpc/pricing/").

- [AWS PrivateLink](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md") is a highly available, scalable technology that you can use to privately connect your VPC to services as if they were in your VPC. You do not need to use an internet gateway, NAT device, public IP address, AWS Direct Connect connection, or AWS Site-to-Site VPN connection to allow communication with the service from your private subnets. Therefore, you control the specific API endpoints, sites, and services that are reachable from your VPC.

For information about the pricing for VPC endpoints, see [AWS PrivateLink pricing](https://aws.amazon.com/privatelink/pricing/ "https://aws.amazon.com/privatelink/pricing/").

### AWS Site-to-Site VPN

By default, instances that you launch into an Amazon VPC can’t communicate with your own (remote) network. You can enable access to your remote network from your VPC by creating an [AWS Site-to-Site VPN](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md") (Site-to-Site VPN) connection, and configuring routing to pass traffic through the connection.

You are charged for each VPN connection hour that your VPN connection is provisioned and available. For more information, see [AWS Site-to-Site VPN and Accelerated Site-to-Site VPN Connection pricing](https://aws.amazon.com/vpn/pricing/#AWS_Site-to-Site_VPN_and_Accelerated_Site-to-Site_VPN_Connection_Pricing "https://aws.amazon.com/vpn/pricing/#AWS_Site-to-Site_VPN_and_Accelerated_Site-to-Site_VPN_Connection_Pricing").

You are charged for data transfer out from Amazon EC2 to the internet. For more information, see [Data Transfer](https://aws.amazon.com/ec2/pricing/on-demand "https://aws.amazon.com/ec2/pricing/on-demand").

When you create an accelerated VPN connection, we create and manage two accelerators on your behalf. You are charged an hourly rate and data transfer costs for each accelerator. For more information, see [AWS Global Accelerator pricing](https://aws.amazon.com/global-accelerator/pricing/ "https://aws.amazon.com/global-accelerator/pricing/").

### AWS Direct Connect

[AWS Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") links your internal network to an AWS Direct Connect location over a standard Ethernet fiber-optic cable. One end of the cable is connected to your router, the other to an AWS Direct Connect router. With this connection, you can create virtual interfaces directly to public AWS services (for example, to Amazon S3 or Amazon VPC), bypassing internet service providers in your network path. An AWS Direct Connect location provides access to AWS in the Region with which it is associated. You can use a single connection in a public Region or AWS GovCloud (US) to access public AWS services in all other public Regions.

AWS Direct Connect has two billing elements: port hours and outbound data transfer. For more information, see [AWS Direct Connect pricing](https://aws.amazon.com/directconnect/pricing/ "https://aws.amazon.com/directconnect/pricing/").

### Elastic Load Balancing

[Elastic Load Balancing](../../../elasticloadbalancing/latest/userguide/what-is-load-balancing.md "../../../elasticloadbalancing/latest/userguide/what-is-load-balancing.md") automatically distributes your incoming traffic across multiple targets, such as Amazon EC2 instances, containers, and IP addresses, in one or more Availability Zones. It monitors the health of its registered targets, and routes traffic only to the healthy targets. Elastic Load Balancing scales your load balancer capacity automatically in response to changes in incoming traffic.

Use Elastic Load Balancing for setting up highly available SAP environments on AWS.

With your load balancer, you pay only for what you use. For more information, see [Elastic Load Balancing pricing](https://aws.amazon.com/elasticloadbalancing/pricing/ "https://aws.amazon.com/elasticloadbalancing/pricing/").

### Data transfer pricing

Data transfer pricing varies based on the architecture pattern and use case. It only amounts to a small percentage of the overall cost of SAP workloads on AWS, 1-5%.

The following table summarizes the common data transfer scenarios that can apply to your SAP landscape.

| Scenario                                     | Architecture                  | Data transfer cost | Pricing guidance                                                                                                                                                        | Other costs                                                                                                                                                                  |
| -------------------------------------------- | ----------------------------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inbound to AWS                               | All                           | No                 |                                                                                                                                                                         |                                                                                                                                                                              |
| Outbound from AWS to Internet                | All                           | Yes                | Based on the services used                                                                                                                                              |                                                                                                                                                                              |
| Services in the same AWS Region              | Internet gateway              | No                 |                                                                                                                                                                         |                                                                                                                                                                              |
| Services in the same AWS Region              | NAT gateway                   | No                 |                                                                                                                                                                         | Per GB processing charge, see [Amazon VPC pricing](https://aws.amazon.com/vpc/pricing/ "https://aws.amazon.com/vpc/pricing/")                                                |
| Services in the same AWS Region              | AWS PrivateLink/ VPC endpoint | No                 |                                                                                                                                                                         | See [AWS PrivateLink pricing](https://aws.amazon.com/privatelink/pricing/ "https://aws.amazon.com/privatelink/pricing/")                                                     |
| Services in different AWS Regions            | All                           | Yes                | Per GB charge for inter-Region data transfer, see [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/")                       |                                                                                                                                                                              |
| Components in same Availability Zone         | All                           | No                 |                                                                                                                                                                         |                                                                                                                                                                              |
| Components in different Availability Zones   | AWS Transit Gateway           | No                 |                                                                                                                                                                         | AWS Transit Gateway processing charges, see [AWS Transit Gateway pricing](https://aws.amazon.com/transit-gateway/pricing/ "https://aws.amazon.com/transit-gateway/pricing/") |
| Components in different Availability Zones   | Amazon VPC peering            | Yes                | Per GB charge for inter-Region data transfer, see [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/")                       |                                                                                                                                                                              |
| Components in different AWS Regions          | AWS Transit Gateway           | Yes                | Per GB charge for inter-Region data transfer, see [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/")                       | AWS Transit Gateway processing charges                                                                                                                                       |
| Components in different AWS Regions          | Amazon VPC peering            | Yes                | Per GB charge for inter-Region data transfer, see [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/")                       |                                                                                                                                                                              |
| Transfer to on-premises or corporate network | AWS VPN                       | Yes                | Per GB charge for data transfer out, see [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/")                                | AWS VPN and AWS Transit Gateway charges                                                                                                                                      |
| Transfer to on-premises or corporate network | AWS Direct Connect            | Yes                | Per GB charge for data transfer out based on location and provider, see [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/") | AWS Direct Connect and AWS Transit Gateway charges                                                                                                                           |

## Automation

With AWS Systems Manager for SAP, you can backup and restore SAP HANA databases on Amazon EC2 with AWS Backup.

AWS Systems Manager for SAP is available to you at no additional cost. You only pay for the AWS resources that you provision to manage and operate your SAP environments.

## Backup, restore, and recovery

With these services, you can quickly and effectively backup, restore, and recovery your SAP workloads.

###### Topics

- [AWS Backint Agent for SAP HANA](#backint "#backint")
- [AWS Elastic Disaster Recovery](#disaster-recovery "#disaster-recovery")
- [Amazon EBS snapshots](#snapshots "#snapshots")

### AWS Backint Agent for SAP HANA

[AWS Backint Agent for SAP HANA (AWS Backint agent)](../sap-hana/aws-backint-agent-sap-hana.md "../sap-hana/aws-backint-agent-sap-hana.md") is an SAP-certified backup and restore application for SAP HANA workloads running on Amazon EC2 instances in the cloud. AWS Backint agent runs as a standalone application that integrates with your existing workflows to back up your SAP HANA database to Amazon S3 and AWS Backup.

AWS Backint agent is a free service. You pay for only the underlying AWS services that you use, for example Amazon S3 or AWS Backup. See the following references for more information.

- [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/")
- [AWS Backup pricing](https://aws.amazon.com/backup/pricing/ "https://aws.amazon.com/backup/pricing/")

### AWS Elastic Disaster Recovery

[AWS Elastic Disaster Recovery (Elastic Disaster Recovery)](../../../drs/latest/userguide/what-is-drs.md "../../../drs/latest/userguide/what-is-drs.md") minimizes downtime and data loss with fast, reliable recovery of on-premises and cloud-based applications using affordable storage, minimal compute, and point-in-time recovery.

You only pay for the servers you are actively replicating to AWS. For more information, see [AWS Elastic Disaster Recovery pricing](https://aws.amazon.com/disaster-recovery/pricing/ "https://aws.amazon.com/disaster-recovery/pricing/").

### Amazon EBS snapshots

See the [Amazon EBS](#ebs "#ebs") section.

## Migration

The following services enable you to quickly move application and files.

###### Topics

- [Migration Hub Orchestrator](#orchestrator "#orchestrator")
- [AWS DataSync](#datasync "#datasync")

### Migration Hub Orchestrator

[AWS Migration Hub Orchestrator](../../../migrationhub-orchestrator/latest/userguide/what-is-migrationhub-orchestrator.md "../../../migrationhub-orchestrator/latest/userguide/what-is-migrationhub-orchestrator.md") simplifies and automates the migration of servers and enterprise applications to AWS. It provides a single location to run and track your migrations.

AWS Migration Hub Orchestrator is available to you at no additional cost. You only pay for the AWS resources that you provision for migrations.

### AWS DataSync

[AWS DataSync](../../../datasync/latest/userguide/what-is-datasync.md "../../../datasync/latest/userguide/what-is-datasync.md") is an online data movement and discovery service that simplifies data migration and helps you quickly, easily, and securely move your file or object data to, from, and between AWS storage services.

You pay only for the amount of data that you migrate based on a flat, per-gigabyte fee according to your AWS Region. For more information, see [AWS DataSync pricing](https://aws.amazon.com/datasync/pricing/ "https://aws.amazon.com/datasync/pricing/").

## Monitoring

With the use of following services, you can monitor your SAP workloads on AWS.

###### Topics

- [AWS Data Provider](#data-provider "#data-provider")
- [Amazon CloudWatch Application Insights for SAP HANA](#application-insights "#application-insights")
- [Amazon CloudWatch](#cloudwatch "#cloudwatch")
- [AWS CloudTrail](#cloudtrail "#cloudtrail")
- [VPC Flow Logs](#flow-logs "#flow-logs")

### AWS Data Provider

AWS Data Provider for SAP is a tool that collects performance-related data from AWS services. It makes this data available to SAP applications to help monitor and improve the performance of business transactions.

For information about costs, see [AWS Data Provider for SAP pricing](data-provider-intro.md#data-provider-pricing "data-provider-intro.md#data-provider-pricing").

### Amazon CloudWatch Application Insights for SAP HANA

[Amazon CloudWatch Application Insights](../../../AmazonCloudWatch/latest/monitoring/appinsights-what-is.md "../../../AmazonCloudWatch/latest/monitoring/appinsights-what-is.md") helps you monitor your applications that use Amazon EC2 instances along with other application resources.

CloudWatch Application Insights sets up recommended metrics and logs for selected application resources using CloudWatch metrics, Logs, and Events for notifications on detected problems. These features are charged to your AWS account according to [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/"). For more information, see [CloudWatch Application Insights pricing](../../../AmazonCloudWatch/latest/monitoring/appinsights-what-is.md#appinsights-pricing "../../../AmazonCloudWatch/latest/monitoring/appinsights-what-is.md#appinsights-pricing").

### Amazon CloudWatch

[Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") monitors your resources and applications running on AWS in real time. You can collect and track metrics for your resources and applications.

For information about CloudWatch pricing, refer the following resources.

- [CloudWatch billing and cost](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_billing.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_billing.md")
- [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/")

### AWS CloudTrail

[AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") is an AWS service that helps you enable operational and risk auditing, governance, and compliance of your AWS account. Actions taken by a user, role, or an AWS service are recorded as events in CloudTrail.

CloudTrail is charged pay per usage with no minimum fee. For more information, see [AWS CloudTrail pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

### VPC Flow Logs

[VPC Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md") is a feature that enables you to capture information about the IP traffic going to and from network interfaces in your VPC.

Data ingestion and archival charges for vended logs apply when you publish flow logs. For more information about pricing when publishing vended logs, open [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/"), select **Logs** > **Vended Logs**.

## Operating System licenses

You can bring your own licenses for the operating system of your choice or purchase from [AWS Marketplace](https://aws.amazon.com/marketplace/search "https://aws.amazon.com/marketplace/search").

###### Topics

- [Red Hat](#redhat "#redhat")
- [SUSE](#suse "#suse")
- [Windows](#windows "#windows")
- [Oracle Enterprise Linux](#oel "#oel")

### Red Hat

Red Hat offers two Linux distributions to run SAP workloads. For more details, you can check Red Hat documentation – [Overview of the Red Hat Enterprise Linux (RHEL) for SAP Solutions subscription](https://access.redhat.com/solutions/3082481 "https://access.redhat.com/solutions/3082481").

You can avail these options from [AWS Marketplace](https://aws.amazon.com/marketplace/search "https://aws.amazon.com/marketplace/search") or [Red Hat Cloud Access](https://www.redhat.com/en/technologies/cloud-computing/cloud-access "https://www.redhat.com/en/technologies/cloud-computing/cloud-access"). When you purchase Red Hat operating systems from AWS, your Support plan includes operating system support.

If you want to launch an Amazon EC2 instance with RHEL for SAP Applications, then you must have a subscription for the Red Hat Cloud Access program. With RHEL 8, RHEL for SAP Solutions or RHEL for SAP Applications is required for running SAP applications in production environments.

[RHEL for SAP Solutions on AWS Marketplace](https://aws.amazon.com/marketplace/search/results?searchTerms=rhel+for+sap+solutions "https://aws.amazon.com/marketplace/search/results?searchTerms=rhel+for+sap+solutions") is available at an hourly rate or as an annual commitment. RHEL for SAP Solutions is designed specifically to run SAP workloads. It includes a longer lifecycle support with Extended Update Support (E4S) that provides support on specific minor releases for four years from general availability. It also provides all the necessary packages for configuring the Pacemaker based cluster, ensuring reliability and availability of critical production services.

###### Note

AWS Marketplace pricing displays the software cost for RHEL. The additional cost of RHEL is included in Amazon EC2 pricing.

### SUSE

SUSE offers two Linux distributions to run SAP workloads – SUSE Linux Enterprise Server (SLES) and SUSE Linux Enterprise Server for SAP Applications (SLES for SAP)

You can avail these options from [AWS Marketplace](https://aws.amazon.com/marketplace/search "https://aws.amazon.com/marketplace/search") or from SUSE. When you purchase SUSE operating systems from AWS, your Support plan includes operating system support.

When you bring your own subscription, the support for Amazon EC2 is based on your SUSE purchasing agreement.

SLES for Amazon EC2 is available at an hourly rate or as an annual commitment. RHEL for SAP Solutions is designed specifically to run SAP workloads. It includes a longer lifecycle support with Extended Update Support (E4S) that provides support on specific minor releases for four years from general availability. It also provides all the necessary packages for configuring the Pacemaker based cluster, ensuring reliability and availability of critical production services.

[SLES for SAP on AWS Marketplace](https://aws.amazon.com/marketplace/search/results?searchTerms=rhel+for+sap+solutions "https://aws.amazon.com/marketplace/search/results?searchTerms=rhel+for+sap+solutions") is available at an hourly rate or as an annual commitment. The price of the SLES subscription is included with your Amazon EC2 instance cost, and is based on the vCPUs of the Amazon EC2 instance. SLES for SAP is designed specifically to run SAP workloads. It includes a longer lifecycle support with Extended Service Pack Overlap Support that provides 4.5 years of total support. SLES for SAP also offers software components and service offerings like SAP HANA high availability resource agents and cluster connector.

###### Note

SLES for SAP pricing is the cost of the software and there is not an additional cost for SLES.

### Windows

Windows server on Amazon EC2 can be availed at a flat, hourly rate with no commitment (On-Demand) or through a one-time payment (Savings Plan or Reserved Instances). There is no difference in cost in terms of a Windows operating system with either of these options. You can also bring your own licence. For more information, see [Microsoft Licensing on AWS](https://aws.amazon.com/windows/resources/licensing/ "https://aws.amazon.com/windows/resources/licensing/").

### Oracle Enterprise Linux

SAP requires you to have Oracle Linux Premier Support subscription to use Oracle Enterprise Linux operating system. For additional information, review the following resources from Oracle and SAP.

- [Oracle Store](https://shop.oracle.com/apex/f?p=700:1:::::: "https://shop.oracle.com/apex/f?p=700:1::::::")
- [SAP Note 2069760 - Oracle Linux 7.x SAP Installation and Upgrade](https://launchpad.support.sap.com/#/notes/2069760 "https://launchpad.support.sap.com/#/notes/2069760") (requires SAP portal access)

## AWS Marketplace

[AWS Marketplace](../../../marketplace/latest/userguide/what-is-marketplace.md "../../../marketplace/latest/userguide/what-is-marketplace.md") is a curated digital catalog that customers can use to find, buy, deploy, and manage third-party software, data, and services to build solutions and run their businesses.

In AWS Marketplace, products can be free to use or can have associated charges. For more information, see [Product pricing](../../../marketplace/latest/userguide/pricing.md "../../../marketplace/latest/userguide/pricing.md").

## AWS Support

[AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/") offers different levels of support. For more information, see [AWS Support Plan Pricing](https://aws.amazon.com/premiumsupport/pricing/ "https://aws.amazon.com/premiumsupport/pricing/").

SAP requires you to have at least a Business level of support when running SAP workloads on AWS. To learn more about the SAP prerequisite, see [SAP Note 1656250 - SAP on AWS: Support Prerequisites](https://launchpad.support.sap.com/#/notes/1656250 "https://launchpad.support.sap.com/#/notes/1656250") (requires SAP portal access).
