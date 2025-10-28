# Elastic Disaster Recovery network diagrams

The following are the network diagrams for AWS Elastic Disaster Recovery :

## General Architecture - On-Premises

to AWS

This diagram shows the general architecture of DRS protecting source servers
located in an on-premises environment.

![AWS Elastic Disaster Recovery architecture showing data flow from on-premises to AWS Cloud for replication and recovery.](images/drs-general-arc.png)

## On-Prem to AWS

This diagram shows the network architecture of DRS protecting source servers
located in an on-premises environment.

![Network architecture showing on-premises servers replicating to AWS Cloud via DRS, EC2, and S3 services.](images/drs-network-arc.png)

## AWS Cloud to AWS Cloud via VPN

This diagram shows the network architecture of DRS protecting source servers
located in an on-premises environment. Communication between the on-premise
environment and DRS is performed through a VPN connection.

![AWS Elastic Disaster Recovery architecture using VPN connection between on-premises and AWS Cloud regions.](images/drs-vpn-connection-communication.png)

## On-Prem to Outposts

This diagram shows the network architecture of DRS protecting source servers
located in an on-premises environment. The staging and recovery are both located on
AWS Outposts. [Find out more about protecting source servers using Outposts.](outposts.md "outposts.md")

![AWS Elastic Disaster Recovery architecture using AWS Outposts for staging and recovery in a separate data center.](images/drs-networkrequirements-outpost1.png)

## AWS to Outposts

This diagram shows the network architecture of DRS protecting source servers
located in AWS. The staging and recovery are both located on AWS Outposts. [Find out more
about protecting source servers using Outposts.](outposts.md "outposts.md")

![AWS Elastic Disaster Recovery architecture showing replication between main and recovery data centers using AWS Outposts.](images/drs-networkrequirements-outpost2.png)

## On-Premises to AWS Local

Zone

This diagram shows the network architecture of DRS protecting source servers located in an on-premises environment.
The staging area is located in an AWS Region and the and recovery is in an AWS Local Zone.

![Network architecture diagram showing DRS protecting on-premises servers with AWS Cloud staging and recovery areas.](images/On-premises-to-local-zones.png)

## AWS Local Zone to Region

This diagram shows the network architecture of DRS protecting source servers located in an AWS Local Zone.
The staging and recovery environment are both located in an AWS Region.

![AWS DRS architecture with source servers in Local Zone and staging/recovery in Region.](images/local-zone-to-region.png)

## AWS Local Zone to AWS Local Zone

This diagram shows the network architecture of DRS protecting source servers
located in an AWS Local Zone. The staging environment is located in an AWS
Region and the recovery environment is in another AWS Local Zone.

![Network architecture diagram of DRS protecting source servers in AWS Local Zones and Region.](images/local-zone-to-local-zone.png)

## AWS Failback to On-Prem

This diagram shows the network architecture of DRS performing Failback to an
on-premise environment after performing a recovery into AWS.

![AWS DRS failback replication architecture showing data flow between AWS Cloud and on-premises data center.](images/drs-failback-arc.png)
