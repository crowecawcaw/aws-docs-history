# Core concepts

Below is a high-level overview of the Core Concepts that are incorporated in Elastic Disaster Recovery. We recommend readers to also familiarize themselves with core AWS functionality such as [Amazon Identity and Access Management](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/")
(IAM), [Networking Essentials](https://aws.amazon.com/getting-started/aws-networking-essentials/ "https://aws.amazon.com/getting-started/aws-networking-essentials/"), [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/ "https://aws.amazon.com/ec2/") (EC2); and general disaster recovery concepts.

_The main goal of disaster recovery (DR) is to help your business prepare and recover from unexpected events in an acceptable amount of time. This means you need to determine which applications deliver the core functionality required for your business to be available, and define the appropriate recovery time objective (RTO) and recovery point objective (RPO) required for these applications._

## Region

AWS has the concept of a Region, which is a physical location where we cluster data centers around the world. We call each group of logical data centers an Availability Zone (AZ). Each AWS Region consists of a minimum of
three, isolated, and physically separate AZs within a geographic area. Unlike other cloud providers, who often define a Region as a single data center, the multiple AZ design of every AWS Region offers advantages for
customers. Each AZ has independent power, cooling, and physical security and is connected through redundant, ultra-low-latency networks. AWS customers focused on high availability can design their applications to run in multiple AZs to achieve even greater fault-tolerance. AWS
infrastructure Regions meet the highest levels of security, compliance, and data protection.

## Availability Zone (AZ)

An Availability Zone (AZ) is one or more discrete data centers with redundant power, networking, and connectivity in an AWS Region. AZs give customers the ability to operate production applications and databases that are more highly available, fault tolerant, and scalable than would be possible from a single data center. All AZs in an AWS Region are interconnected with high-bandwidth, low-latency networking, over fully redundant, dedicated metro fiber providing high-throughput, low-latency
networking between AZs. All traffic between AZs is encrypted. The network performance is sufficient to accomplish synchronous replication between AZs. AZs make partitioning applications for high availability
easy. If an application is partitioned across AZs, companies are better isolated and protected from issues such as power outages, lightning strikes, tornadoes, earthquakes, and more. AZs are physically separated
by a meaningful distance, many kilometers, from any other AZ, although all are within 100 km (60 miles) of each other.

## Recovery Point Objective (RPO)

RPO is defined by how much data loss your application can tolerate, and determines what is considered an acceptable loss of data between the last recovery point and the interruption of service.

## Recovery Time Objective (RTO)

Defined by the organization, RTO is the maximum acceptable time between the interruption of service and restoration of service. This determines what is considered an acceptable time window when service is unavailable after a disaster.

## Source server

The Source server refers to the instance or server that you want to protect and recover in the event of a disaster. Elastic Disaster Recovery can be used to recover Amazon EC2 instances (referred to as Recovery Instances on Elastic Disaster Recovery) in a different Availability Zone within the same Region, or a different AWS Region.
Elastic Disaster Recovery can also protect applications hosted on physical infrastructure, VMware vSphere, Microsoft Hyper-V, and cloud infrastructure from other cloud providers.

## Recovery subnet

The Recovery subnet is the virtual network segment hosted within an
Availability Zone and hosts the recovered Source Servers in the event of
a disaster.

## AWS Replication Agent

The AWS Replication Agent is a lightweight software package. It must be installed on each source EC2 instance that you want to protect using Elastic Disaster Recovery. The agent performs two main tasks:

1. Initial
   block-level replication of disks by copying the state of the disk on the source server and transmitting this data to the staging environment where this data is persisted on Elastic Block Storage (EBS) volumes that
   logically map to the source disks.
2. Real-time monitoring and replication of all block-level changes once the agent has completed the initial synchronization process.

## Staging area subnet

In the selected AWS account and Region, the subnet selected to host the Replication Server is referred to as the Staging area subnet. The Elastic Disaster Recovery service utilizes low-cost compute and storage hosted on the Staging Area subnet to keep the data in sync with the
source environment. Replication resources consist of Replication Servers, Staging volumes, and EBS snapshots.

## Replication server

The Replication Server is responsible for receiving and storing the replicated data from the Source Server. The Replication Server is an EC2 instance to which Staging EBS Volumes are attached. The AWS Replication Agent sends data from the Source Server to the Replication Server during
the initial synchronization process or when blocks change on the Source Server. Replication Servers will take snapshots of the staging EBS Volumes attached to them.

## Point in time snapshots (PiT snapshots)

These are periodic backups taken by the Replication Server at specific intervals to capture the state of the Source Server and its data. The intervals are:

1. Once every 10 minutes for the last hour.
2. Once an hour for the last 24 hours.
3. Once a day for the last 7 days (unless a different retention period is configured, 1-365 days).

These PiT snapshots are used during recovery or recovery drill to recover the source server to a particular point in time.

## Conversion Server

The Conversion Server is a component that makes all the necessary modifications to allow the target instance to boot and run, including pre- and post-boot scripts. The conversion server is launched within the staging area subnet and managed by the Elastic Disaster Recovery
service. Conversion Servers are ephemeral resources and will only last for minutes in order to complete the conversion process.

## Drills

Drills refer to scheduled or ad-hoc tests performed to validate the effectiveness of your disaster recovery plan. Elastic Disaster Recovery allows you to conduct drills to simulate recovery scenarios without impacting the production environment or replication state.

## Recovery instance

During an actual recovery, a recovery instance is provisioned in the recovery subnet. The recovery instance is an EC2 instance and a fully functional copy of the source server that allows you to recover operations in the selected Region.

## Drill Instance

A Drill Instance is an instance that has been launched using Elastic Disaster Recovery for the purpose of a drill or `test.` The goal of launching a drill instance is to test and validate your disaster recovery plan before an actual disaster. This instance is meant to be launched while your source server remains active. You may choose
to activate this instance for production use by shutting down the source server and redirecting traffic to this instance.

## Failover

Failover is the process of initiating a recovery in Elastic Disaster Recovery, launching an EC2 instance, and restoring your data based on the PiT snapshot selected to an EBS volume. This process would include failing over to a new Region, launching the recovery instance, and
validating the application is ready to receive traffic. Additional steps are often required to prepare the recovery environment for a failover and these are often documented and executed as part of a DR runbook.

## Failback

Failback is the process of returning to normal operations at your source site. This includes replicating data back to the source Region, bringing the source servers back online, and redirecting user traffic back to these machines (redirection of traffic, as well as other configuration operations, are handled outside of the AWS Elastic Disaster Recovery service)
