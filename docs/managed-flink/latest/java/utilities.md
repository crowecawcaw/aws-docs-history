

# Use practical utilities for Managed Service for Apache Flink
<a name="utilities"></a>

The following utilities can make using the Managed Service for Apache Flink service easier to use:

**Topics**
+ [Snapshot manager](#snapshot-manager)
+ [Benchmarking](#benchmarking)

## Snapshot manager
<a name="snapshot-manager"></a>

 It's a best practice for Flink Applications to regularly initiate savepoints/snapshots to allow for more seamless failure recovery. Snapshot manager automates this task and offers the following benefits:
+ Creates an application snapshot (legacy) of a running Managed Service for Apache Flink application.
+ Counts the application snapshots (legacy) of the application.
+ Compares the count with the number of application snapshots (legacy) that you want to keep.
+ Deletes the oldest application snapshots (legacy) that exceed that number.

Snapshot manager uses the application snapshot (legacy) API actions, such as [`CreateApplicationSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateApplicationSnapshot.html). For an application in enhanced snapshot mode, `CreateApplicationSnapshot` returns `InvalidApplicationConfigurationException`, so Snapshot manager does not work. Managed Service for Apache Flink does not delete enhanced snapshots on a schedule. To remove enhanced snapshots that you no longer need, call `DeleteSnapshot`. If your application uses enhanced snapshot mode, manage its snapshots with the enhanced snapshot API actions, such as [`CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html). For more information, see [Create and manage enhanced snapshots](snapshots-manage.md).

For an example, see [Snapshot manager](https://github.com/aws-samples/amazon-kinesis-data-analytics-snapshot-manager-for-flink).

## Benchmarking
<a name="benchmarking"></a>

Managed Service for Apache Flink Flink Benchmarking Utility helps with capacity planning, integration testing, and benchmarking of Managed Service for Apache Flink for Apache Flink applications.

For an example, see [Benchmarking](https://github.com/aws-samples/amazon-kinesis-data-analytics-flink-benchmarking-utility)