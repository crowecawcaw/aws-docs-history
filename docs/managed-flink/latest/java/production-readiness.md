Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Achieve production readiness for your Managed Service for Apache Flink

applications

This is a collection of important aspects of running production applications on Managed Service for Apache Flink. It's not an exhaustive list, but rather the
bare minimum of what you should pay attention to before putting an application into production.

## Load-test your applications

Some problems with applications only manifest under heavy load. We have seen cases
where applications seemed healthy, yet an operational event substantially amplified the
load on the application. This can happen completely independent of the application
itself. If the data source or the data sink is unavailable for a couple of hours, the
Flink application cannot make progress. When that issue is fixed, there is a backlog of
unprocessed data that has accumulated, which can completely exhaust the available
resources. The load can then amplify bugs or performance issues that had not emerged
before.

It is therefore essential that you run proper load tests for production
applications. Questions that should be answered during those load tests include:

- Is the application stable under sustained high load?
- Can the application still take a savepoint under peak load?
- How long does it take to process a backlog of 1 hour? And how long for 24 hours (depending on the max retention of the data in the stream)?
- Does the throughput of the application increase when the application is scaled?

When consuming from a data stream, these scenarios can be simulated by producing into
the stream for some time. Then start the application and have it consume data from the
beginning of time. For example, use a start position of `TRIM_HORIZON` in the
case of a Kinesis data stream.

## Define Max parallelism

The max parallelism defines the maximum parallelism a stateful application can scale to. This is defined when the state is first created and there is no way of scaling the operator beyond this maximum without discarding the state.

Max parallelism is set when the state is first created.

By default, Max parallelism is set to:

- 128, if parallelism <= 128
- `MIN(nextPowerOfTwo(parallelism + (parallelism / 2)), 2^15)`: if parallelism > 128

If you are planning to scale your application > 128 parallelism, you should explicitly
define the Max parallelism.

You can define Max parallelism at level of application, with
`env.setMaxParallelism(x)` or single operator. Unless differently
specified, all operators inherit the Max parallelism of the application.

For more information, see [Setting the Maximum Parallelism](https://nightlies.apache.org/flink/flink-docs-release-1.18/docs/dev/datastream/execution/parallel/#setting-the-maximum-parallelism "https://nightlies.apache.org/flink/flink-docs-release-1.18/docs/dev/datastream/execution/parallel/#setting-the-maximum-parallelism") in the Apache Flink Documentation.

## Set a UUID for all operators

A UUID is used in the operation in which Flink maps a savepoint back to an individual operator. Setting a specific UUID for each operator gives a stable mapping for the savepoint process to restore.

```
.map(...).uid("my-map-function")
```

For more information, see [Production Readiness Checklist](https://nightlies.apache.org/flink/flink-docs-release-1.18/docs/ops/production_ready/ "https://nightlies.apache.org/flink/flink-docs-release-1.18/docs/ops/production_ready/").
