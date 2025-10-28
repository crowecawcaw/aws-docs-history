Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# I/O bound operators

It's best to avoid dependencies to external systems on the data path. It's often much more performant to keep a
reference data set in state rather than querying an external system to enrich individual events.
However, sometimes there are dependencies that cannot be easily moved to state, e.g., if you want to enrich events with a machine learning model
that is hosted on Amazon Sagemaker.

Operators that are interfacing with external systems over the network can become a bottleneck and cause backpressure.
It is highly recommended to use [AsyncIO](https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/datastream/operators/asyncio/ "https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/datastream/operators/asyncio/") to implement the functionality,
to reduce the wait time for individual calls and avoid the entire application slowing down.

Moreover, for applications with I/O bound operators it can also make sense to increase the [ParallelismPerKPU](../apiv2/API_ParallelismConfiguration.md "../apiv2/API_ParallelismConfiguration.md") setting of the Managed Service for Apache Flink application.
This configuration describes the number of parallel subtasks an application can perform per Kinesis Processing Unit (KPU).
By increasing the value from the default of 1 to, say, 4, the application leverages the same resources (and has the same cost)
but can scale to 4 times the parallelism. This works well for I/O bound applications, but it causes additional overhead for applications that are not I/O bound.
