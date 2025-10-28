# Migrating files to Amazon FSx for OpenZFS using AWS DataSync

We recommend using AWS DataSync to transfer data between FSx for OpenZFS file systems. DataSync is a
data transfer service that simplifies, automates, and accelerates moving and replicating data
between self-managed storage systems and AWS storage services over the internet or
AWS Direct Connect. DataSync can transfer your file system data and metadata, such as ownership, timestamps,
and access permissions.

You can use DataSync to transfer files between two FSx for OpenZFS file systems, and also move data to
a file system in a different AWS Region or AWS account. You can
also use DataSync with FSx for OpenZFS file systems for other tasks. For example, you can perform
one-time data migrations, periodically ingest data for distributed workloads, and schedule
replication for data protection and recovery.

In DataSync, a _location_ is an endpoint
for an FSx for OpenZFS file system. For information about specific transfer scenarios, see
[Working with
locations](../../../datasync/latest/userguide/working-with-locations.md "../../../datasync/latest/userguide/working-with-locations.md") in the _AWS DataSync User Guide_.

## Prerequisites

To migrate data into your FSx for OpenZFS setup, you need a server and network that meet
the DataSync requirements. To learn more, see [Requirements for DataSync](../../../datasync/latest/userguide/requirements.md "../../../datasync/latest/userguide/requirements.md")
in the _AWS DataSync User Guide_.

## Basic steps for migrating files using

DataSync

Transferring files from a source to a destination using DataSync involves the
following basic steps:

- Download and deploy an agent in your environment and activate it (not required if
  transferring between AWS services).
- Create a source and destination location.
- Create a task.
- Run the task to transfer files from the source to the destination.

For more information, see the following topics in the AWS DataSync User Guide:

- [Data transfer between self-managed storage and AWS](../../../datasync/latest/userguide/how-datasync-works.md#onprem-aws "../../../datasync/latest/userguide/how-datasync-works.md#onprem-aws")
- [Creating a location for Amazon FSx for OpenZFS](../../../datasync/latest/userguide/create-openzfs-location.md "../../../datasync/latest/userguide/create-openzfs-location.md")
- [Deploy your agent as an Amazon EC2 instance](../../../datasync/latest/userguide/deploy-agents.md#ec2-deploy-agent "../../../datasync/latest/userguide/deploy-agents.md#ec2-deploy-agent")
