# Resilience in Amazon Aurora DSQL

The AWS global infrastructure is built around AWS Regions and Availability Zones (AZ). AWS Regions provide multiple physically separated and isolated
Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and
operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly
available, fault tolerant, and scalable than traditional single or multiple data center infrastructures. Aurora DSQL is designed
so that you can take advantage of AWS Regional infrastructure while providing the highest database availability.
By default, single-Region clusters in Aurora DSQL have Multi-AZ availability, providing tolerance to major component failures
and infrastructure disruptions that might impact access to a full AZ. Multi-Region clusters provide all of the benefits
from Multi-AZ resiliency while still providing the strongly consistent database availability, even in cases in which AWS Region
is inaccessible to application clients.

For more information about AWS Regions and Availability Zones, see [AWS Global
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

In addition to the AWS global infrastructure, Aurora DSQL offers several features to help support your data resiliency and backup needs.

## Backup and restore

Aurora DSQL supports backup and restore with AWS Backup console. You can perform a full backup and
restore for your single-Region and multi-Region clusters. For more information, see
[Backup and restore for Amazon Aurora DSQL](backup-aurora-dsql.md "backup-aurora-dsql.md").

## Replication

By design, Aurora DSQL commits all write transactions to a distributed transaction log and
synchronously replicates all committed log data to user storage replicas in three AZs.
Multi-Region clusters provide full cross-Region replication capabilities between read
and write Regions.

A designated witness Region supports transaction log-only writes and doesn't consume
storage. Witness Regions don't have an endpoint. This means that witness Regions store
only encrypted transaction logs, require no administration or configuration, and aren't
accessible by users.

Aurora DSQL transaction logs and user storage are distributed with all data presented to
Aurora DSQL query processors as a single logical volume. Aurora DSQL automatically splits, merges,
and replicates data based on database primary key range and access patterns. Aurora DSQL
automatically scales read replicas, both up and down, based on read access
frequency.

Cluster storage replicas are distributed across a multi-tenant storage fleet. If a component or AZ becomes impaired,
Aurora DSQL automatically redirects access to surviving components and asynchronously repairs missing replicas. Once
Aurora DSQL fixes the impaired replicas, Aurora DSQL automatically adds them back to the storage quorum and makes them
available to your cluster.

## High availability

By default, single-Region and multi-Region clusters in Aurora DSQL are active-active, and you don't need to
manually provision, configure, or reconfigure any clusters. Aurora DSQL fully automates cluster recovery, which eliminates the need
for traditional primary-secondary failover operations. Replication is always synchronous and done in multiple AZs, so
there is no risk of data loss due to replication lag or failover to an asynchronous secondary database
during failure recovery.

Single-Region clusters provide a Multi-AZ redundant endpoint that automatically enables concurrent access with
strong data consistency across three AZs. This means that user storage replicas on any of these three AZs always
return the same result to one or more readers and are always available to receive writes. This strong consistency
and Multi-AZ resiliency is available across all Regions for Aurora DSQL multi-Region clusters. This means that
multi-Region clusters provide two strongly consistent Regional endpoints, so clients can read or write indiscriminately
to either Region with zero replication lag on commit.

Aurora DSQL provides 99.99% availability for single-Region clusters and 99.999% for multi-Region clusters.

## Fault injection testing

Amazon Aurora DSQL integrates with AWS Fault Injection Service (AWS FIS), a fully managed service for
running controlled fault injection experiments to improve an application's resilience.
Using AWS FIS, you can:

- Create experiment templates that define specific failure scenarios
- Inject failures (elevated cluster connection error rates) to validate application error handling and recovery mechanisms
- Test multi-Region application behavior to validate application traffic shift between AWS Regions when one AWS Region is experiencing high connection error rates

For example, in a multi-Region cluster spanning US East (N. Virginia) and US East (Ohio), you can run an experiment in US East (Ohio) to test failures there while US East (N. Virginia) continues normal operations. This controlled testing helps you identify and resolve potential issues before they affect production workloads.

See [Action targets](../../../fis/latest/userguide/action-sequence.md#action-targets "../../../fis/latest/userguide/action-sequence.md#action-targets") in the _AWS FIS user guide_ for a complete list of AWS FIS supported actions.

For information about Amazon Aurora DSQL actions available in AWS FIS, see [Aurora DSQL actions reference](../../../fis/latest/userguide/fis-actions-reference.md#dsql-actions-reference "../../../fis/latest/userguide/fis-actions-reference.md#dsql-actions-reference") in the _AWS FIS User Guide_.

To get started running fault injection experiments, see [Planning your AWS FIS
experiments](../../../fis/latest/userguide/getting-started-planning.md "../../../fis/latest/userguide/getting-started-planning.md") in the _AWS FIS User Guide_.
