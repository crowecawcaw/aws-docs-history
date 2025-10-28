# Migrating to Amazon FSx for Lustre using AWS DataSync

You can use AWS DataSync to transfer data between FSx for Lustre file systems. DataSync is a
data transfer service that simplifies, automates, and accelerates moving and replicating data
between self-managed storage systems and AWS storage services over the internet or
AWS Direct Connect. DataSync can transfer your file system data and metadata, such as ownership, timestamps,
and access permissions.

## How to migrate existing files to FSx for Lustre using

AWS DataSync

You can use DataSync with FSx for Lustre file systems to perform one-time data migrations,
periodically ingest data for distributed workloads, and schedule replication for data
protection and recovery. For information about specific transfer scenarios, see
[Where can I transfer my data with AWS DataSync?](../../../datasync/latest/userguide/working-with-locations.md "../../../datasync/latest/userguide/working-with-locations.md")
in the _AWS DataSync User Guide_.

### Prerequisites

To migrate data into your FSx for Lustre setup, you need a server and network that meet
the DataSync requirements. To learn more, see [Setting up with AWS DataSync](../../../datasync/latest/userguide/requirements.md "../../../datasync/latest/userguide/requirements.md")
in the _AWS DataSync User Guide_.

- You have created a destination FSx for Lustre file system. For more information,
  see [Step 1: Create your FSx for Lustre file system](getting-started.md#getting-started-step1 "getting-started.md#getting-started-step1").
- The source and destination file systems are connected in the same virtual private cloud (VPC).
  The source file system can be located on-premises or in another Amazon VPC, AWS account, or AWS Region, but it must be in a
  network peered with that of the destination file system using Amazon VPC Peering, Transit Gateway, AWS Direct Connect,
  or AWS VPN. For more information, see
  [What is VPC peering?](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md")
  in the _Amazon VPC Peering Guide_.

###### Note

DataSync can only transfer across AWS accounts to or from FSx for Lustre if the other transfer location is Amazon S3.

### Basic steps for migrating files using

DataSync

Transferring files from a source to a destination using DataSync involves the
following basic steps:

1. Download and deploy an agent in your environment and activate it (not required if
   transferring between AWS services).
2. Create a source and destination location.
3. Create a task.
4. Run the task to transfer files from the source to the destination.

For more information, see the following topics in the _AWS DataSync User Guide_:

- [Transferring between on-premises storage and AWS](../../../datasync/latest/userguide/how-datasync-transfer-works.md#onprem-aws "../../../datasync/latest/userguide/how-datasync-transfer-works.md#onprem-aws")
- [Configuring AWS DataSync transfers with Amazon FSx for Lustre](../../../datasync/latest/userguide/create-lustre-location.md "../../../datasync/latest/userguide/create-lustre-location.md").
- [Deploying your Amazon EC2 agent](../../../datasync/latest/userguide/deploy-agents.md#ec2-deploy-agent "../../../datasync/latest/userguide/deploy-agents.md#ec2-deploy-agent")
