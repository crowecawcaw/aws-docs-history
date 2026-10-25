

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Agentless replication overview
<a name="installing-vcenter-overview-mgn"></a>

**Important**  
Agentless replication is no longer available for new deployments. We recommend agent-based replication for all migrations. To learn more, see [Why we recommend agent-based replication](#why-agent-based).

## How agentless replication works
<a name="how-agentless-replication-works"></a>

Agentless snapshot-based replication allows you to replicate source servers on your vCenter environment into AWS without installing the AWS Replication Agent. 

In order to use agentless replication, you must dedicate at least one VM in your vCenter environment to host the MGN vCenter Client. The MGN vCenter Client is a software bundle distributed by MGN and is available for installation as a binary installer. The installation process installs services on the client VM which allow MGN to remotely discover your VMs that are suitable for agentless replication, and to perform data replication between your vCenter environment and AWS through the use of periodic snapshot shipping. 

Agentless snapshot based replication is divided into two main operations: discovery and replication: 

The discovery process involves periodically scanning your vCenter environment to detect source server VMs that are suitable for agentless replication, and adding these VMs to the MGN console. Once a source server has been added, you may choose to initiate agentless replication on the source VM using the MGN API or console. The discovery process also collects all of the necessary information from vCenter in order to perform an agentless conversion process once a migration job is launched. 

The replication process involves continuously starting and monitoring the “snapshot shipping processes” on the source server VM being replicated. A “snapshot shipping process” is a long running logical operation which consists of taking a VMware snapshot on the replicated VM, and launching an ephemeral replication agent process which uses VMware’s Changed Block Tracking (CBT) feature to identify changed volume data location, using Virtual Disk Development Kit (VDDK) to read the modified data, and sending the data from the source environment to the customer’s target AWS account. The first snapshot shipping process performs an “initial sync” which sends the entire disk contents of the replicating VM into AWS. Following snapshot shipping processes leverage CBT only to sync disk changes to the customer’s target AWS account. Each successful snapshot shipping process completes the replication operation by creating a group of consistent snapshots in the customer’s AWS account, which can then be used by the customer to launch test and cutover instances through the regular MGN mechanisms. 

These are the main system components of agentless replication:


+ MGN vCenter Client – A software bundle that is installed on a dedicated VM in your vCenter environment in order to facilitate agentless replication.
+ vCenter Replication Agent – A java agent that is based on the AWS Replication Agent, which replicates a single VM using VDDK and CBT as the data source instead of the MGN driver (that is used by the AWS Replication Agent)
+ MGN Service
+ MGN console 

**Note**  
Agentless replication does not work in IPv6-only source environments.

This diagram illustrates the high level interaction between the different agentless replication system components: 

![Architecture showing data flow from corporate data center through MGN Connector to staging area and migrated resources in AWS.](https://docs.aws.amazon.com/mgn/latest/ug/images/agentless-architecture.png)


## Prerequisites
<a name="installing-vcenter-prereques-mgn"></a>

1. Ensure that you have initialized AWS Transform MGN before installing the MGN vCenter Client.

## Why we recommend agent-based replication
<a name="why-agent-based"></a>

We recommend agent-based replication for all migrations. Agent-based replication installs the AWS Replication Agent in the guest operating system and performs continuous, block-level replication, keeping your source servers in sync with AWS in near real time. Because changes replicate as they occur rather than at scheduled snapshot intervals, there is no waiting for snapshots to sync. This keeps your recovery point low, reduces the data synchronized at cutover, and results in shorter launch times and more predictable cutover windows measured in minutes.

Agent-based replication also avoids creating VMware snapshots on your production datastores, so it does not affect source disk performance during the migration. It is supported for both VMware and non-VMware source environments, so you can use a single, consistent replication method across a mixed fleet. To install the agent across many source servers at scale, use the MGN connector instead of installing on each server manually.

Agentless replication is no longer available for new deployments. For new source servers, install the AWS Replication Agent, either manually or with the MGN connector, and adopt agent-based replication as your default method for new migration waves.