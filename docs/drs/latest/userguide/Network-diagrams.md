

# Elastic Disaster Recovery network diagrams
<a name="Network-diagrams"></a>

AWS Elastic Disaster Recovery supports the following source infrastructure types:
+ **On-premises to AWS** – Protect physical or virtual servers in your data center by replicating to an AWS Region.
+ **AWS to AWS (cross-Region)** – Protect Amazon EC2 instances by replicating from one AWS Region to another. Cross-Region replication is recommended for disaster recovery to help protect against Region-level events.
+ **AWS to AWS (cross-Availability Zone)** – Replicate Amazon EC2 instances to a different Availability Zone within the same AWS Region. For comprehensive disaster recovery protection, we recommend cross-Region replication.
+ **VMware to AWS** – Protect VMware vSphere environments, including both on-premises vSphere and VMware Cloud on AWS. See [Disaster recovery for VMware Cloud on AWS using AWS Elastic Disaster Recovery](https://aws.amazon.com/blogs/storage/disaster-recovery-for-vmware-cloud-on-aws-using-aws-elastic-disaster-recovery/).
+ **Other clouds to AWS** – Protect workloads running on other cloud providers such as Microsoft Azure or Google Cloud. See [Building a disaster recovery site on AWS for workloads on Microsoft Azure](https://aws.amazon.com/blogs/storage/building-a-disaster-recovery-site-on-aws-for-workloads-on-microsoft-azure/).
+ **AWS to on-premises (failback)** – After a disaster recovery event, fail back from AWS to your original source environment.

The following are the network diagrams for AWS Elastic Disaster Recovery :

## General Architecture - On-Premises to AWS
<a name="Network-diagrams-onprem-general"></a>

 This diagram shows the general architecture of DRS protecting source servers located in an on-premises environment. 

![AWS Elastic Disaster Recovery architecture showing data flow from on-premises to AWS Cloud for replication and recovery.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-general-arc.png)




## On-Prem to AWS
<a name="Network-diagrams-onprem-network"></a>

 This diagram shows the network architecture of DRS protecting source servers located in an on-premises environment. 

![Network architecture showing on-premises servers replicating to AWS Cloud via DRS, EC2, and S3 services.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-network-arc.png)






## AWS Cloud to AWS Cloud via VPC Peering
<a name="Network-diagrams-aws-vpc-peering"></a>

This diagram shows the network architecture of AWS DRS protecting source servers located in an AWS VPC. Data replication between the source VPC and the target staging area, along with communication with the AWS DRS service, flows through a VPC peering connection.

![](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-vpc-peering-communication.png)






## On-Prem to Outposts
<a name="Network-diagrams-onprem-outpost"></a>

 This diagram shows the network architecture of DRS protecting source servers located in an on-premises environment. The staging and recovery are both located on AWS Outposts. [Find out more about protecting source servers using Outposts.](https://docs.aws.amazon.com/drs/latest/userguide/outposts.html) 

![AWS Elastic Disaster Recovery architecture using AWS Outposts for staging and recovery in a separate data center.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-networkrequirements-outpost1.png)






## AWS to Outposts
<a name="Network-diagrams-aws-outpost"></a>

 This diagram shows the network architecture of DRS protecting source servers located in AWS. The staging and recovery are both located on AWS Outposts. [Find out more about protecting source servers using Outposts.](https://docs.aws.amazon.com/drs/latest/userguide/outposts.html) 

![AWS Elastic Disaster Recovery architecture showing replication between main and recovery data centers using AWS Outposts.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-networkrequirements-outpost2.png)






## On-Premises to AWS Local Zone
<a name="Network-diagrams-On-premises-to-local-zones"></a>

 This diagram shows the network architecture of DRS protecting source servers located in an on-premises environment. The staging area is located in an AWS Region and the recovery is in an AWS Local Zone.

![Network architecture diagram showing DRS protecting on-premises servers with AWS Cloud staging and recovery areas.](http://docs.aws.amazon.com/drs/latest/userguide/images/On-premises-to-local-zones.png)




## AWS Local Zone to Region
<a name="Network-diagrams-local-zone-to-region"></a>

 This diagram shows the network architecture of DRS protecting source servers located in an AWS Local Zone. The staging and recovery environment are both located in an AWS Region.

![AWS DRS architecture with source servers in Local Zone and staging/recovery in Region.](http://docs.aws.amazon.com/drs/latest/userguide/images/local-zone-to-region.png)




## AWS Local Zone to AWS Local Zone
<a name="Network-diagrams-local-zone-to-local-zone"></a>

 This diagram shows the network architecture of DRS protecting source servers located in an AWS Local Zone. The staging environment is located in an AWS Region and the recovery environment is in another AWS Local Zone.

![Network architecture diagram of DRS protecting source servers in AWS Local Zones and Region.](http://docs.aws.amazon.com/drs/latest/userguide/images/local-zone-to-local-zone.png)




## AWS Failback to On-Prem
<a name="Network-diagrams-onprem-failback"></a>

 This diagram shows the network architecture of DRS performing Failback to an on-premises environment after performing a recovery into AWS. 

![AWS DRS failback replication architecture showing data flow between AWS Cloud and on-premises data center.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-failback-arc.png)


