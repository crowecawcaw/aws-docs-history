

# Use practical utilities for Managed Service for Apache Flink
<a name="utilities"></a>

The following utilities can make using the Managed Service for Apache Flink service easier to use:

**Topics**
+ [Snapshot manager](#snapshot-manager)
+ [Benchmarking](#benchmarking)

## Snapshot manager
<a name="snapshot-manager"></a>

 It's a best practice for Flink Applications to regularly initiate savepoints/snapshots to allow for more seamless failure recovery. Snapshot manager automates this task and offers the following benefits:
+ takes a new snapshot of a running Managed Service for Apache Flink for Apache Flink Application
+ gets a count of application snapshots
+ checks if the count is more than the required number of snapshots
+ deletes older snapshots that are older than the required number

For an example, see [Snapshot manager](https://github.com/aws-samples/amazon-kinesis-data-analytics-snapshot-manager-for-flink).

## Benchmarking
<a name="benchmarking"></a>

Managed Service for Apache Flink Flink Benchmarking Utility helps with capacity planning, integration testing, and benchmarking of Managed Service for Apache Flink for Apache Flink applications.

For an example, see [Benchmarking](https://github.com/aws-samples/amazon-kinesis-data-analytics-flink-benchmarking-utility)