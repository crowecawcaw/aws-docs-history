Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Maintain best practices for Managed Service for Apache Flink

applications

This section contains information and recommendations for developing a stable, performant
Managed Service for Apache Flink applications.

###### Topics

- [Minimize the size of the uber JAR](#minimize-uber-JAR "#minimize-uber-JAR")
- [Fault tolerance: checkpoints and savepoints](#how-dev-bp-checkpoint "#how-dev-bp-checkpoint")
- [Unsupported connector versions](#how-dev-bp-connectors "#how-dev-bp-connectors")
- [Performance and parallelism](#how-dev-bp-performance "#how-dev-bp-performance")
- [Setting per-operator parallelism](#how-dev-bp-parallelism "#how-dev-bp-parallelism")
- [Logging](#how-dev-bp-logging "#how-dev-bp-logging")
- [Coding](#how-dev-bp-code "#how-dev-bp-code")
- [Managing credentials](#how-dev-bp-managing-credentials "#how-dev-bp-managing-credentials")
- [Reading from sources with few shards/partitions](#troubleshooting-few-shards-partitions "#troubleshooting-few-shards-partitions")
- [Studio notebook refresh interval](#notebook-refresh-rate "#notebook-refresh-rate")
- [Studio notebook optimum performance](#notebook-refresh-rate "#notebook-refresh-rate")
- [How watermark strategies and idle shards affect time windows](#notebook-watermarking "#notebook-watermarking")
- [Set a UUID for all operators](#best-practices-setting-operator-ids "#best-practices-setting-operator-ids")
- [Add
  ServiceResourceTransformer to the Maven shade plugin](#best-practices-service-resource-transformer "#best-practices-service-resource-transformer")

## Minimize the size of the uber JAR

Java/Scala application must be packaged in an uber (super/fat) JAR and include all the
additional required dependencies that are not already provided by the runtime. However,
the size of the uber JAR affects the application start and restart times and may cause
the JAR to exceed the limit of 512 MB.

To optimize the deployment time, your uber JAR should **not** include the following:

- **Any dependencies provided by the runtime** as
  illustrated in the following example. They should have `provided`
  scope in the POM file or `compileOnly` in your Gradle
  configuration.
- **Any dependencies used for testing only**, for
  example JUnit or Mockito. They should have `test` scope in the POM
  file or `testImplementation` in your Gradle configuration.
- **Any dependencies not actually used by your
  application**.
- **Any static data or metadata required by your
  application.** Static data should be loaded by the application at
  runtime, for example from a datastore or from Amazon S3.
- See this [POM example file](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/blob/main/java/GettingStarted/pom.xml "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/blob/main/java/GettingStarted/pom.xml") for details on the preceding configuration
  settings.

**Provided dependencies**

The Managed Service for Apache Flink runtime provides a number of dependencies. These dependencies should not be
included in the fat JAR and must have `provided` scope in the POM file or be
explicitly excluded in the `maven-shade-plugin` configuration. Any of these
dependencies included in the fat JAR is ignored at runtime, but increases the size of
the JAR adding overhead during the deployment.

Dependencies provided by the runtime, in runtime versions 1.18, 1.19, and 1.20:

- `org.apache.flink:flink-core`
- `org.apache.flink:flink-java`
- `org.apache.flink:flink-streaming-java`
- `org.apache.flink:flink-scala_2.12`
- `org.apache.flink:flink-table-runtime`
- `org.apache.flink:flink-table-planner-loader`
- `org.apache.flink:flink-json`
- `org.apache.flink:flink-connector-base`
- `org.apache.flink:flink-connector-files`
- `org.apache.flink:flink-clients`
- `org.apache.flink:flink-runtime-web`
- `org.apache.flink:flink-metrics-code`
- `org.apache.flink:flink-table-api-java`
- `org.apache.flink:flink-table-api-bridge-base`
- `org.apache.flink:flink-table-api-java-bridge`
- `org.apache.logging.log4j:log4j-slf4j-impl`
- `org.apache.logging.log4j:log4j-api`
- `org.apache.logging.log4j:log4j-core`
- `org.apache.logging.log4j:log4j-1.2-api`

Additionally, the runtime provides the library that is used to fetch application
runtime properties in Managed Service for Apache Flink,
`com.amazonaws:aws-kinesisanalytics-runtime:1.2.0`.

All dependencies provided by the runtime must use the following recommendations to
**not** include them in the uber JAR:

- In Maven (`pom.xml`) and SBT (`build.sbt`), use
  `provided` scope.
- In Gradle (`build.gradle`), use `compileOnly`
  configuration.

Any provided dependency accidentally included in the uber JAR will be ignored at
runtime because of Apache Flink's parent-first class loading. For more information, see
[parent-first-patterns](https://nightlies.apache.org/flink/flink-docs-master/docs/deployment/config/#classloader-parent-first-patterns-default "https://nightlies.apache.org/flink/flink-docs-master/docs/deployment/config/#classloader-parent-first-patterns-default") in the Apache Flink documentation.

**Connectors**

Most of the connectors, except the FileSystem connector, that are not included in the
runtime must be included in the POM file with the default scope
(`compile`).

**Other recommendations**

As a rule, your Apache Flink uber JAR provided to Managed Service for Apache Flink should contain the minimum
code required to run the application. Including dependencies that include the source
classes, test datasets, or bootstrapping state should not be included in this jar. If
static resources need to be pulled in at runtime, separate this concern into a resource
such as Amazon S3. Examples of this include state bootstraps or an inference model.

Take some time to consider your deep dependency tree and remove non-runtime
dependencies.

Although Managed Service for Apache Flink supports 512MB jar sizes, this should be seen as the exception to the
rule. Apache Flink currently supports ~104MB jar sizes through its default
configuration, and that should be the maximum target size of a jar needed.

## Fault tolerance: checkpoints and savepoints

Use checkpoints and savepoints to implement fault tolerance in your Managed Service for Apache Flink
application. Keep the following in mind when developing and maintaining your
application:

- We recommend that you keep checkpointing enabled for your application. Checkpointing provides
  fault tolerance for your application during scheduled maintenance, and also for
  unexpected failures due to service issues, application dependency failures, and
  other issues. For information about scheduled maintenance, see [Manage maintenance tasks for Managed Service for Apache Flink](maintenance.md "maintenance.md").
- Set [ApplicationSnapshotConfiguration::SnapshotsEnabled](../apiv2/API_ApplicationSnapshotConfiguration.md "../apiv2/API_ApplicationSnapshotConfiguration.md") to
  `false` during application development or troubleshooting. A snapshot
  is created during every application stop, which may cause issues if the
  application is in an unhealthy state or isn't performant. Set
  `SnapshotsEnabled` to `true` after the application is in
  production and is stable.

###### Note

We recommend that you set your application to create a snapshot several times a day to restart
properly with correct state data. The correct frequency for your snapshots
depends on your application's business logic. Taking frequent snapshots lets
you recover more recent data, but increases cost and requires more system
resources.

For information about monitoring application downtime, see
[Metrics and dimensions in Managed Service for Apache Flink](metrics-dimensions.md "metrics-dimensions.md").

For more information about implementing fault tolerance, see [Implement fault tolerance](how-fault.md "how-fault.md").

## Unsupported connector versions

From Apache Flink version 1.15 or later, Managed Service for Apache Flink automatically prevents
applications from starting or updating if they are using unsupported Kinesis connector
versions bundled into application JARs. When upgrading to Managed Service for Apache Flink version 1.15 or
later, make sure that you are using the most recent Kinesis connector. This is any version
equal to or newer than version 1.15.2. All other versions are not supported by
Managed Service for Apache Flink because they might cause consistency issues or failures with the **Stop with Savepoint** feature, preventing clean stop/update
operations. To learn more about connector compatibility in Amazon Managed Service for Apache Flink versions, see [Apache Flink connectors](how-flink-connectors.md "how-flink-connectors.md").

## Performance and parallelism

Your application can scale to meet any throughput level by tuning your application
parallelism, and avoiding performance pitfalls. Keep the following in mind when
developing and maintaining your application:

- Verify that all of your application sources and sinks are sufficiently provisioned
  and are not being throttled. If the sources and sinks are other AWS services, monitor those
  services using [CloudWatch](../../../cloudwatch.md "../../../cloudwatch.md").
- For applications with very high parallelism, check if the high levels of parallelism
  are applied to all operators in the application. By default, Apache Flink applies the same
  application parallelism for all operators in the application graph.
  This can lead to either provisioning issues on sources or sinks, or bottlenecks in operator
  data processing. You can change the parallelism of each operator in code with
  [setParallelism](https://nightlies.apache.org/flink/flink-docs-release-1.15/dev/parallel.html "https://nightlies.apache.org/flink/flink-docs-release-1.15/dev/parallel.html").
- Understand the meaning of the parallelism settings for the operators in your application.

If you change the parallelism for an operator, you may not be able to restore the application from
a snapshot created when the operator had a parallelism that is incompatible with the current settings.
For more information about setting operator parallelism, see
[Set maximum parallelism for operators explicitly](https://nightlies.apache.org/flink/flink-docs-release-1.15/ops/production_ready.html#set-maximum-parallelism-for-operators-explicitly "https://nightlies.apache.org/flink/flink-docs-release-1.15/ops/production_ready.html#set-maximum-parallelism-for-operators-explicitly").

For more information about implementing scaling, see [Implement application scaling](how-scaling.md "how-scaling.md").

## Setting per-operator parallelism

By default, all operators have the parallelism set at application level.
You can override the parallelism of a single operator using the DataStream API using `.setParallelism(x)`.
You can set an operator parallelism to any parallelism equal or lower than the application parallelism.

If possible, define the operator parallelism as a function of the application parallelism. This way, the operator parallelism will vary with the application parallelism. If you are using autoscaling, for example, all operators will vary their parallelism in the same proportion:

```
int appParallelism = env.getParallelism();
...
...ops.setParalleism(appParallelism/2);
```

In some cases, you may want to set the operator parallelism to a constant. For
example, setting the parallelism of a Kinesis Stream source to the number of shards. In
these cases, consider passing the operator parallelism as application configuration
parameter to change it without changing the code, for example to reshard the source
stream.

## Logging

You can monitor your application's performance and error conditions using CloudWatch Logs. Keep the following in mind when
configuring logging for your application:

- Enable CloudWatch logging for the application so that any runtime issues can be debugged.
- Do not create a log entry for every record being processed in the application. This causes
  severe bottlenecks during processing and might lead to backpressure in the
  processing of data.
- Create CloudWatch alarms to notify you when your application is not running properly. For more
  information, see [Use CloudWatch Alarms with Amazon Managed Service for Apache Flink](monitoring-metrics-alarms.md "monitoring-metrics-alarms.md")

For more information about implementing logging, see
.

## Coding

You can make your application performant and stable by using recommended programming practices.
Keep the following in mind when writing application code:

- Do not use `system.exit()` in your application code, in either your application's
  `main` method or in user-defined functions. If you want to shut down your application from
  within code, throw an exception derived from `Exception`
  or `RuntimeException`, containing a message about what went wrong with the application.

Note the following about how the service handles this exception:

    + If the exception is thrown from your application's `main` method, the
     service will wrap it in a `ProgramInvocationException` when the application
     transitions to the `RUNNING` status, and the job manager will fail to submit the job.
    + If the exception is thrown from a user-defined function, the job manager will
     fail the job and restart it, and details of the exception will be written to the exception log.

- Consider shading your application JAR file and its included dependencies. Shading is
  recommended when there are potential conflicts in package names between your
  application and the Apache Flink runtime. If a conflict occurs, your application
  logs may contain an exception of type
  `java.util.concurrent.ExecutionException`. For more information about
  shading your application JAR file, see [Apache Maven Shade
  Plugin](https://maven.apache.org/plugins/maven-shade-plugin/ "https://maven.apache.org/plugins/maven-shade-plugin/").

## Managing credentials

You should not bake any long-term credentials into production (or any other)
applications. Long-term credentials are likely checked into a version control system and
can easily get lost. Instead, you can associate a role to the Managed Service for Apache Flink application
and grant permissions to that role. The running Flink application can then select
temporary credentials with the respective permissions from the environment. In case
authentication is needed for a service that is not natively integrated with IAM, for
example, a database that requires a username and password for authentication, you should
consider storing secrets in [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/ "https://aws.amazon.com/secrets-manager/").

Many AWS native services support authentication:

- Kinesis Data Streams – [ProcessTaxiStream.java](hhttps://github.com/aws-samples/amazon-kinesis-data-analytics-taxi-consumer/blob/master/src/main/java/com/amazonaws/samples/kaja/taxi/consumer/ProcessTaxiStream.java#L90 "hhttps://github.com/aws-samples/amazon-kinesis-data-analytics-taxi-consumer/blob/master/src/main/java/com/amazonaws/samples/kaja/taxi/consumer/ProcessTaxiStream.java#L90")
- Amazon MSK – [https://github.com/aws/aws-msk-iam-auth/#using-the-amazon-msk-library-for-iam-authentication](https://github.com/aws/aws-msk-iam-auth/#using-the-amazon-msk-library-for-iam-authentication "https://github.com/aws/aws-msk-iam-auth/#using-the-amazon-msk-library-for-iam-authentication")
- Amazon Elasticsearch Service – [AmazonElasticsearchSink.java](https://github.com/aws-samples/amazon-kinesis-data-analytics-taxi-consumer/blob/master/src/main/java/com/amazonaws/samples/kaja/taxi/consumer/operators/AmazonElasticsearchSink.java "https://github.com/aws-samples/amazon-kinesis-data-analytics-taxi-consumer/blob/master/src/main/java/com/amazonaws/samples/kaja/taxi/consumer/operators/AmazonElasticsearchSink.java")
- Amazon S3 – works out of the box on Managed Service for Apache Flink

## Reading from sources with few shards/partitions

When reading from Apache Kafka or a Kinesis Data Stream, there may be a mismatch
between the parallelism of the stream (the number of partitions for Kafka and the number
of shards for Kinesis) and the parallelism of the application. With a naive design, the
parallelism of an application cannot scale beyond the parallelism of a stream: Each
subtask of a source operator can only read from 1 or more shards/partitions. That means
for a stream with only 2 shards and an application with a parallelism of 8, that only
two subtasks are actually consuming from the stream and 6 subtasks remain idle. This can
substantially limit the throughput of the application, in particular if the
deserialization is expensive and carried out by the source (which is the
default).

To mitigate this effect, you can either scale the stream. But that may not always be desirable or possible.
Alternatively, you can restructure the source so that it does not do any serialization and just passes on the `byte[]`.
You can then [rebalance](https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/datastream/overview/ "https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/datastream/overview/") the data to distribute it evenly across all tasks and then deserialize the data there.
In this way, you can leverage all subtasks for the deserialization and this potentially expensive operation is no longer bound by
the number of shards/partitions of the stream.

## Studio notebook refresh interval

If you change the paragraph result refresh interval, set it to a value that is at
least 1000 milliseconds.

## Studio notebook optimum performance

We tested with the following statement and got the optimal performance when
`events-per-second` multiplied by `number-of-keys` was under
25,000,000. This was for `events-per-second` under 150,000.

```
SELECT key, sum(value) FROM key-values GROUP BY key
```

## How watermark strategies and idle shards affect time windows

When reading events from Apache Kafka and Kinesis Data Streams, the source can set the event time based on attributes of the stream.
In case of Kinesis, the event time equals the approximate arrival time of events.
But setting event time at the source for events is not sufficient for a Flink application to use event time.
The source must also generate watermarks that propagate information about event time from the source to all other operators.
The [Flink documentation](https://nightlies.apache.org/flink/flink-docs-release-1.14/docs/concepts/time/ "https://nightlies.apache.org/flink/flink-docs-release-1.14/docs/concepts/time/")
has a good overview of how that process works.

By default, the timestamp of an event read from Kinesis is set to the approximate arrival time determined by Kinesis.
An additional prerequisite for event time to work in the application is a watermark strategy.

```
WatermarkStrategy<String> s = WatermarkStrategy
    .<String>forMonotonousTimestamps()
    .withIdleness(Duration.ofSeconds(...));
```

The watermark strategy is then applied to a `DataStream` with the
`assignTimestampsAndWatermarks` method. There are some useful built-in
strategies:

- `forMonotonousTimestamps()` will just use the event time
  (approximate arrival time) and periodically emit the maximum value as a
  watermark (for each specific subtask)
- `forBoundedOutOfOrderness(Duration.ofSeconds(...))` similar to the
  previous strategy, but will use the event time – duration for watermark
  generation.

From the [Flink documentation](https://nightlies.apache.org/flink/flink-docs-release-1.14/docs/concepts/time/ "https://nightlies.apache.org/flink/flink-docs-release-1.14/docs/concepts/time/"):

_Each parallel subtask of a source function usually generates its watermarks independently. These watermarks define the event time at that particular parallel source._

_As the watermarks flow through the streaming program, they advance the event time at the operators where they arrive. Whenever an operator advances its event time, it generates a new watermark downstream for its successor operators._

_Some operators consume multiple input streams; a union, for example, or operators following a keyBy(…) or partition(…) function. Such an operator’s current event time is the minimum of its input streams' event times. As its input streams update their event times, so does the operator._

That means, if a source subtask is consuming from an idle shard, downstream operators
do not receive new watermarks from that subtask and hence processing stalls for all
downstream operators that use time windows. To avoid this, customers can add the
`withIdleness` option to the watermark strategy. With that option, an
operator excludes the watermarks from idle upstream subtasks when computing the event
time of the operator. The idle subtask therefore no longer blocks the advancement of
event time in downstream operators.

Depending on the shard assigner you use, some workers might not be assigned any Kinesis shards. In that
case, these workers will manifest the idle source behavior even if all Kinesis shards continuously deliver
event data. You can mitigate this risk by using `uniformShardAssigner` with the source operator.
This makes sure that all source subtasks have shards to process as long as the number of workers is less or
equal to the number of active shards.

However, the idleness option with the build-in watermark strategies will not advance
the event time if no subtask is reading any event, that is there are no events in the
stream. This becomes particularly visible for test cases where a finite set of events is
read from the stream. As event time does not advance after the last event has been read,
the last window (containing the last event) will not close.

### Summary

- The `withIdleness` setting will not generate new watermarks in case a shard is
  idle. It will exclude the last watermark sent by idle subtasks from the min
  watermark calculation in downstream operators.
- With the build-in watermark strategies, the last open window will not close (unless new events
  that advance the watermark will be sent, but that creates a new window that
  then remains open).
- Even when the time is set by the Kinesis stream, late arriving events can still happen if one
  shard is consumed faster than others (for example during app initialization
  or when using `TRIM_HORIZON` where all existing shards are
  consumed in parallel ignoring their parent/child relationship).
- The `withIdleness` settings of the watermark strategy seem interrupt the Kinesis
  source-specific settings for idle shards
  `(ConsumerConfigConstants.SHARD_IDLE_INTERVAL_MILLIS`.

### Example

The following application is reading from a stream and creating session windows based on event time.

```
Properties consumerConfig = new Properties();
consumerConfig.put(AWSConfigConstants.AWS_REGION, "eu-west-1");
consumerConfig.put(ConsumerConfigConstants.STREAM_INITIAL_POSITION, "TRIM_HORIZON");

FlinkKinesisConsumer<String> consumer = new FlinkKinesisConsumer<>("...", new SimpleStringSchema(), consumerConfig);

WatermarkStrategy<String> s = WatermarkStrategy
    .<String>forMonotonousTimestamps()
    .withIdleness(Duration.ofSeconds(15));

env.addSource(consumer)
    .assignTimestampsAndWatermarks(s)
    .map(new MapFunction<String, Long>() {
        @Override
        public Long map(String s) throws Exception {
            return Long.parseLong(s);
        }
    })
    .keyBy(l -> 0l)
    .window(EventTimeSessionWindows.withGap(Time.seconds(10)))
    .process(new ProcessWindowFunction<Long, Object, Long, TimeWindow>() {
        @Override
        public void process(Long aLong, ProcessWindowFunction<Long, Object, Long, TimeWindow>.Context context, Iterable<Long>iterable, Collector<Object> collector) throws Exception {
            long count = StreamSupport.stream(iterable.spliterator(), false).count();
            long timestamp = context.currentWatermark();

            System.out.print("XXXXXXXXXXXXXX Window with " + count + " events");
            System.out.println("; Watermark: " + timestamp + ", " + Instant.ofEpochMilli(timestamp));


            for (Long l : iterable) {
                System.out.println(l);
            }
        }
    });
```

In the following example, 8 events are written to a 16 shard stream (the first 2 and the last event happen to land in the same shard).

```
$ aws kinesis put-record --stream-name hp-16 --partition-key 1 --data MQ==
$ aws kinesis put-record --stream-name hp-16 --partition-key 2 --data Mg==
$ aws kinesis put-record --stream-name hp-16 --partition-key 3 --data Mw==
$ date

{
    "ShardId": "shardId-000000000012",
    "SequenceNumber": "49627894338614655560500811028721934184977530127978070210"
}
{
    "ShardId": "shardId-000000000012",
    "SequenceNumber": "49627894338614655560500811028795678659974022576354623682"
}
{
    "ShardId": "shardId-000000000014",
    "SequenceNumber": "49627894338659257050897872275134360684221592378842022114"
}
Wed Mar 23 11:19:57 CET 2022

$ sleep 10
$ aws kinesis put-record --stream-name hp-16 --partition-key 4 --data NA==
$ aws kinesis put-record --stream-name hp-16 --partition-key 5 --data NQ==
$ date

{
    "ShardId": "shardId-000000000010",
    "SequenceNumber": "49627894338570054070103749783042116732419934393936642210"
}
{
    "ShardId": "shardId-000000000014",
    "SequenceNumber": "49627894338659257050897872275659034489934342334017700066"
}
Wed Mar 23 11:20:10 CET 2022

$ sleep 10
$ aws kinesis put-record --stream-name hp-16 --partition-key 6 --data Ng==
$ date

{
    "ShardId": "shardId-000000000001",
    "SequenceNumber": "49627894338369347363316974173886988345467035365375213586"
}
Wed Mar 23 11:20:22 CET 2022

$ sleep 10
$ aws kinesis put-record --stream-name hp-16 --partition-key 7 --data Nw==
$ date

{
    "ShardId": "shardId-000000000008",
    "SequenceNumber": "49627894338525452579706688535878947299195189349725503618"
}
Wed Mar 23 11:20:34 CET 2022

$ sleep 60
$ aws kinesis put-record --stream-name hp-16 --partition-key 8 --data OA==
$ date

{
    "ShardId": "shardId-000000000012",
    "SequenceNumber": "49627894338614655560500811029600823255837371928900796610"
}
Wed Mar 23 11:21:27 CET 2022
```

This input should result in 5 session windows: event 1,2,3; event 4,5; event 6; event 7; event 8. However, the program only yields the first 4 windows.

```
11:59:21,529 INFO  org.apache.flink.streaming.connectors.kinesis.FlinkKinesisConsumer [] - Subtask 5 will be seeded with initial shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000006,HashKeyRange: {StartingHashKey: 127605887595351923798765477786913079296,EndingHashKey: 148873535527910577765226390751398592511},SequenceNumberRange: {StartingSequenceNumber: 49627894338480851089309627289524549239292625588395704418,}}'}, starting state set as sequence number EARLIEST_SEQUENCE_NUM
11:59:21,530 INFO  org.apache.flink.streaming.connectors.kinesis.internals.KinesisDataFetcher [] - Subtask 5 will start consuming seeded shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000006,HashKeyRange: {StartingHashKey: 127605887595351923798765477786913079296,EndingHashKey: 148873535527910577765226390751398592511},SequenceNumberRange: {StartingSequenceNumber: 49627894338480851089309627289524549239292625588395704418,}}'} from sequence number EARLIEST_SEQUENCE_NUM with ShardConsumer 0
11:59:21,530 INFO  org.apache.flink.streaming.connectors.kinesis.FlinkKinesisConsumer [] - Subtask 6 will be seeded with initial shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000007,HashKeyRange: {StartingHashKey: 148873535527910577765226390751398592512,EndingHashKey: 170141183460469231731687303715884105727},SequenceNumberRange: {StartingSequenceNumber: 49627894338503151834508157912666084957565273949901684850,}}'}, starting state set as sequence number EARLIEST_SEQUENCE_NUM
11:59:21,530 INFO  org.apache.flink.streaming.connectors.kinesis.FlinkKinesisConsumer [] - Subtask 6 will be seeded with initial shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000010,HashKeyRange: {StartingHashKey: 212676479325586539664609129644855132160,EndingHashKey: 233944127258145193631070042609340645375},SequenceNumberRange: {StartingSequenceNumber: 49627894338570054070103749782090692112383219034419626146,}}'}, starting state set as sequence number EARLIEST_SEQUENCE_NUM
11:59:21,530 INFO  org.apache.flink.streaming.connectors.kinesis.internals.KinesisDataFetcher [] - Subtask 6 will start consuming seeded shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000007,HashKeyRange: {StartingHashKey: 148873535527910577765226390751398592512,EndingHashKey: 170141183460469231731687303715884105727},SequenceNumberRange: {StartingSequenceNumber: 49627894338503151834508157912666084957565273949901684850,}}'} from sequence number EARLIEST_SEQUENCE_NUM with ShardConsumer 0
11:59:21,531 INFO  org.apache.flink.streaming.connectors.kinesis.FlinkKinesisConsumer [] - Subtask 4 will be seeded with initial shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000005,HashKeyRange: {StartingHashKey: 106338239662793269832304564822427566080,EndingHashKey: 127605887595351923798765477786913079295},SequenceNumberRange: {StartingSequenceNumber: 49627894338458550344111096666383013521019977226889723986,}}'}, starting state set as sequence number EARLIEST_SEQUENCE_NUM
11:59:21,532 INFO  org.apache.flink.streaming.connectors.kinesis.internals.KinesisDataFetcher [] - Subtask 4 will start consuming seeded shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000005,HashKeyRange: {StartingHashKey: 106338239662793269832304564822427566080,EndingHashKey: 127605887595351923798765477786913079295},SequenceNumberRange: {StartingSequenceNumber: 49627894338458550344111096666383013521019977226889723986,}}'} from sequence number EARLIEST_SEQUENCE_NUM with ShardConsumer 0
11:59:21,532 INFO  org.apache.flink.streaming.connectors.kinesis.FlinkKinesisConsumer [] - Subtask 3 will be seeded with initial shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000004,HashKeyRange: {StartingHashKey: 85070591730234615865843651857942052864,EndingHashKey: 106338239662793269832304564822427566079},SequenceNumberRange: {StartingSequenceNumber: 49627894338436249598912566043241477802747328865383743554,}}'}, starting state set as sequence number EARLIEST_SEQUENCE_NUM
11:59:21,532 INFO  org.apache.flink.streaming.connectors.kinesis.FlinkKinesisConsumer [] - Subtask 2 will be seeded with initial shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000003,HashKeyRange: {StartingHashKey: 63802943797675961899382738893456539648,EndingHashKey: 85070591730234615865843651857942052863},SequenceNumberRange: {StartingSequenceNumber: 49627894338413948853714035420099942084474680503877763122,}}'}, starting state set as sequence number EARLIEST_SEQUENCE_NUM
11:59:21,532 INFO  org.apache.flink.streaming.connectors.kinesis.FlinkKinesisConsumer [] - Subtask 3 will be seeded with initial shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000015,HashKeyRange: {StartingHashKey: 319014718988379809496913694467282698240,EndingHashKey: 340282366920938463463374607431768211455},SequenceNumberRange: {StartingSequenceNumber: 49627894338681557796096402897798370703746460841949528306,}}'}, starting state set as sequence number EARLIEST_SEQUENCE_NUM
11:59:21,532 INFO  org.apache.flink.streaming.connectors.kinesis.FlinkKinesisConsumer [] - Subtask 2 will be seeded with initial shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000014,HashKeyRange: {StartingHashKey: 297747071055821155530452781502797185024,EndingHashKey: 319014718988379809496913694467282698239},SequenceNumberRange: {StartingSequenceNumber: 49627894338659257050897872274656834985473812480443547874,}}'}, starting state set as sequence number EARLIEST_SEQUENCE_NUM
11:59:21,532 INFO  org.apache.flink.streaming.connectors.kinesis.internals.KinesisDataFetcher [] - Subtask 3 will start consuming seeded shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000004,HashKeyRange: {StartingHashKey: 85070591730234615865843651857942052864,EndingHashKey: 106338239662793269832304564822427566079},SequenceNumberRange: {StartingSequenceNumber: 49627894338436249598912566043241477802747328865383743554,}}'} from sequence number EARLIEST_SEQUENCE_NUM with ShardConsumer 0
11:59:21,532 INFO  org.apache.flink.streaming.connectors.kinesis.internals.KinesisDataFetcher [] - Subtask 2 will start consuming seeded shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000003,HashKeyRange: {StartingHashKey: 63802943797675961899382738893456539648,EndingHashKey: 85070591730234615865843651857942052863},SequenceNumberRange: {StartingSequenceNumber: 49627894338413948853714035420099942084474680503877763122,}}'} from sequence number EARLIEST_SEQUENCE_NUM with ShardConsumer 0
11:59:21,532 INFO  org.apache.flink.streaming.connectors.kinesis.FlinkKinesisConsumer [] - Subtask 0 will be seeded with initial shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000001,HashKeyRange: {StartingHashKey: 21267647932558653966460912964485513216,EndingHashKey: 42535295865117307932921825928971026431},SequenceNumberRange: {StartingSequenceNumber: 49627894338369347363316974173816870647929383780865802258,}}'}, starting state set as sequence number EARLIEST_SEQUENCE_NUM
11:59:21,532 INFO  org.apache.flink.streaming.connectors.kinesis.FlinkKinesisConsumer [] - Subtask 0 will be seeded with initial shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000009,HashKeyRange: {StartingHashKey: 191408831393027885698148216680369618944,EndingHashKey: 212676479325586539664609129644855132159},SequenceNumberRange: {StartingSequenceNumber: 49627894338547753324905219158949156394110570672913645714,}}'}, starting state set as sequence number EARLIEST_SEQUENCE_NUM
11:59:21,532 INFO  org.apache.flink.streaming.connectors.kinesis.FlinkKinesisConsumer [] - Subtask 7 will be seeded with initial shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000000,HashKeyRange: {StartingHashKey: 0,EndingHashKey: 21267647932558653966460912964485513215},SequenceNumberRange: {StartingSequenceNumber: 49627894338347046618118443550675334929656735419359821826,}}'}, starting state set as sequence number EARLIEST_SEQUENCE_NUM
11:59:21,533 INFO  org.apache.flink.streaming.connectors.kinesis.FlinkKinesisConsumer [] - Subtask 0 will be seeded with initial shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000012,HashKeyRange: {StartingHashKey: 255211775190703847597530955573826158592,EndingHashKey: 276479423123262501563991868538311671807},SequenceNumberRange: {StartingSequenceNumber: 49627894338614655560500811028373763548928515757431587010,}}'}, starting state set as sequence number EARLIEST_SEQUENCE_NUM
11:59:21,533 INFO  org.apache.flink.streaming.connectors.kinesis.FlinkKinesisConsumer [] - Subtask 7 will be seeded with initial shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000008,HashKeyRange: {StartingHashKey: 170141183460469231731687303715884105728,EndingHashKey: 191408831393027885698148216680369618943},SequenceNumberRange: {StartingSequenceNumber: 49627894338525452579706688535807620675837922311407665282,}}'}, starting state set as sequence number EARLIEST_SEQUENCE_NUM
11:59:21,533 INFO  org.apache.flink.streaming.connectors.kinesis.internals.KinesisDataFetcher [] - Subtask 0 will start consuming seeded shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000001,HashKeyRange: {StartingHashKey: 21267647932558653966460912964485513216,EndingHashKey: 42535295865117307932921825928971026431},SequenceNumberRange: {StartingSequenceNumber: 49627894338369347363316974173816870647929383780865802258,}}'} from sequence number EARLIEST_SEQUENCE_NUM with ShardConsumer 0
11:59:21,533 INFO  org.apache.flink.streaming.connectors.kinesis.FlinkKinesisConsumer [] - Subtask 7 will be seeded with initial shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000011,HashKeyRange: {StartingHashKey: 233944127258145193631070042609340645376,EndingHashKey: 255211775190703847597530955573826158591},SequenceNumberRange: {StartingSequenceNumber: 49627894338592354815302280405232227830655867395925606578,}}'}, starting state set as sequence number EARLIEST_SEQUENCE_NUM
11:59:21,533 INFO  org.apache.flink.streaming.connectors.kinesis.internals.KinesisDataFetcher [] - Subtask 7 will start consuming seeded shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000000,HashKeyRange: {StartingHashKey: 0,EndingHashKey: 21267647932558653966460912964485513215},SequenceNumberRange: {StartingSequenceNumber: 49627894338347046618118443550675334929656735419359821826,}}'} from sequence number EARLIEST_SEQUENCE_NUM with ShardConsumer 0
11:59:21,568 INFO  org.apache.flink.streaming.connectors.kinesis.FlinkKinesisConsumer [] - Subtask 1 will be seeded with initial shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000002,HashKeyRange: {StartingHashKey: 42535295865117307932921825928971026432,EndingHashKey: 63802943797675961899382738893456539647},SequenceNumberRange: {StartingSequenceNumber: 49627894338391648108515504796958406366202032142371782690,}}'}, starting state set as sequence number EARLIEST_SEQUENCE_NUM
11:59:21,568 INFO  org.apache.flink.streaming.connectors.kinesis.FlinkKinesisConsumer [] - Subtask 1 will be seeded with initial shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000013,HashKeyRange: {StartingHashKey: 276479423123262501563991868538311671808,EndingHashKey: 297747071055821155530452781502797185023},SequenceNumberRange: {StartingSequenceNumber: 49627894338636956305699341651515299267201164118937567442,}}'}, starting state set as sequence number EARLIEST_SEQUENCE_NUM
11:59:21,568 INFO  org.apache.flink.streaming.connectors.kinesis.internals.KinesisDataFetcher [] - Subtask 1 will start consuming seeded shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000002,HashKeyRange: {StartingHashKey: 42535295865117307932921825928971026432,EndingHashKey: 63802943797675961899382738893456539647},SequenceNumberRange: {StartingSequenceNumber: 49627894338391648108515504796958406366202032142371782690,}}'} from sequence number EARLIEST_SEQUENCE_NUM with ShardConsumer 0
11:59:23,209 INFO  org.apache.flink.streaming.connectors.kinesis.internals.KinesisDataFetcher [] - Subtask 0 will start consuming seeded shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000009,HashKeyRange: {StartingHashKey: 191408831393027885698148216680369618944,EndingHashKey: 212676479325586539664609129644855132159},SequenceNumberRange: {StartingSequenceNumber: 49627894338547753324905219158949156394110570672913645714,}}'} from sequence number EARLIEST_SEQUENCE_NUM with ShardConsumer 1
11:59:23,244 INFO  org.apache.flink.streaming.connectors.kinesis.internals.KinesisDataFetcher [] - Subtask 6 will start consuming seeded shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000010,HashKeyRange: {StartingHashKey: 212676479325586539664609129644855132160,EndingHashKey: 233944127258145193631070042609340645375},SequenceNumberRange: {StartingSequenceNumber: 49627894338570054070103749782090692112383219034419626146,}}'} from sequence number EARLIEST_SEQUENCE_NUM with ShardConsumer 1
event: 6; timestamp: 1648030822428, 2022-03-23T10:20:22.428Z
11:59:23,377 INFO  org.apache.flink.streaming.connectors.kinesis.internals.KinesisDataFetcher [] - Subtask 3 will start consuming seeded shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000015,HashKeyRange: {StartingHashKey: 319014718988379809496913694467282698240,EndingHashKey: 340282366920938463463374607431768211455},SequenceNumberRange: {StartingSequenceNumber: 49627894338681557796096402897798370703746460841949528306,}}'} from sequence number EARLIEST_SEQUENCE_NUM with ShardConsumer 1
11:59:23,405 INFO  org.apache.flink.streaming.connectors.kinesis.internals.KinesisDataFetcher [] - Subtask 2 will start consuming seeded shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000014,HashKeyRange: {StartingHashKey: 297747071055821155530452781502797185024,EndingHashKey: 319014718988379809496913694467282698239},SequenceNumberRange: {StartingSequenceNumber: 49627894338659257050897872274656834985473812480443547874,}}'} from sequence number EARLIEST_SEQUENCE_NUM with ShardConsumer 1
11:59:23,581 INFO  org.apache.flink.streaming.connectors.kinesis.internals.KinesisDataFetcher [] - Subtask 7 will start consuming seeded shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000008,HashKeyRange: {StartingHashKey: 170141183460469231731687303715884105728,EndingHashKey: 191408831393027885698148216680369618943},SequenceNumberRange: {StartingSequenceNumber: 49627894338525452579706688535807620675837922311407665282,}}'} from sequence number EARLIEST_SEQUENCE_NUM with ShardConsumer 1
11:59:23,586 INFO  org.apache.flink.streaming.connectors.kinesis.internals.KinesisDataFetcher [] - Subtask 1 will start consuming seeded shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000013,HashKeyRange: {StartingHashKey: 276479423123262501563991868538311671808,EndingHashKey: 297747071055821155530452781502797185023},SequenceNumberRange: {StartingSequenceNumber: 49627894338636956305699341651515299267201164118937567442,}}'} from sequence number EARLIEST_SEQUENCE_NUM with ShardConsumer 1
11:59:24,790 INFO  org.apache.flink.streaming.connectors.kinesis.internals.KinesisDataFetcher [] - Subtask 0 will start consuming seeded shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000012,HashKeyRange: {StartingHashKey: 255211775190703847597530955573826158592,EndingHashKey: 276479423123262501563991868538311671807},SequenceNumberRange: {StartingSequenceNumber: 49627894338614655560500811028373763548928515757431587010,}}'} from sequence number EARLIEST_SEQUENCE_NUM with ShardConsumer 2
event: 4; timestamp: 1648030809282, 2022-03-23T10:20:09.282Z
event: 3; timestamp: 1648030797697, 2022-03-23T10:19:57.697Z
event: 5; timestamp: 1648030810871, 2022-03-23T10:20:10.871Z
11:59:24,907 INFO  org.apache.flink.streaming.connectors.kinesis.internals.KinesisDataFetcher [] - Subtask 7 will start consuming seeded shard StreamShardHandle{streamName='hp-16', shard='{ShardId: shardId-000000000011,HashKeyRange: {StartingHashKey: 233944127258145193631070042609340645376,EndingHashKey: 255211775190703847597530955573826158591},SequenceNumberRange: {StartingSequenceNumber: 49627894338592354815302280405232227830655867395925606578,}}'} from sequence number EARLIEST_SEQUENCE_NUM with ShardConsumer 2
event: 7; timestamp: 1648030834105, 2022-03-23T10:20:34.105Z
event: 1; timestamp: 1648030794441, 2022-03-23T10:19:54.441Z
event: 2; timestamp: 1648030796122, 2022-03-23T10:19:56.122Z
event: 8; timestamp: 1648030887171, 2022-03-23T10:21:27.171Z
XXXXXXXXXXXXXX Window with 3 events; Watermark: 1648030809281, 2022-03-23T10:20:09.281Z
3
1
2
XXXXXXXXXXXXXX Window with 2 events; Watermark: 1648030834104, 2022-03-23T10:20:34.104Z
4
5
XXXXXXXXXXXXXX Window with 1 events; Watermark: 1648030834104, 2022-03-23T10:20:34.104Z
6
XXXXXXXXXXXXXX Window with 1 events; Watermark: 1648030887170, 2022-03-23T10:21:27.170Z
7
```

The output is only showing 4 windows (missing the last window containing event 8).
This is due to event time and the watermark strategy. The last window cannot close
because the pre-built watermark strategies the time never advances beyond the time
of the last event that has been read from the stream. But for the window to close,
time needs to advance more than 10 seconds after the last event. In this case, the
last watermark is 2022-03-23T10:21:27.170Z, but for the session window to close, a
watermark 10s and 1ms later is required.

If the `withIdleness` option is removed from the watermark strategy, no
session window will ever close, because the “global watermark” of the window
operator cannot advance.

When the Flink application starts (or if there is data skew), some shards might be
consumed faster than others. This can cause some watermarks to be emitted too early
from a subtask (the subtask might emit the watermark based on the content of one
shard without having consumed from the other shards it’s subscribed to). Ways to
mitigate are different watermarking strategies that add a safety buffer
`(forBoundedOutOfOrderness(Duration.ofSeconds(30))` or explicitly
allow late arriving events `(allowedLateness(Time.minutes(5))`.

## Set a UUID for all operators

When Managed Service for Apache Flink starts a Flink job for an application with a snapshot, the Flink job
can fail to start due to certain issues. One of them is _operator ID
mismatch_. Flink expects explicit, consistent operator IDs for Flink job
graph operators. If not set explicitly, Flink generates an ID for the operators. This is
because Flink uses these operator IDs to uniquely identify the operators in a job graph
and uses them to store the state of each operator in a savepoint.

The _operator ID mismatch_ issue happens when Flink does not find a
1:1 mapping between the operator IDs of a job graph and the operator IDs defined in a
savepoint. This happens when explicit consistent operator IDs are not set and Flink
generates operator IDs that may not be consistent with every job graph creation. The
likelihood of applications running into this issue is high during maintenance runs. To
avoid this, we recommend customers set UUID for all operators in the Flink code. For
more information, see the topic _Set a UUID for all operators_ under
[Production
readiness](production-readiness.md "production-readiness.md").

## Add

ServiceResourceTransformer to the Maven shade plugin

Flink uses Java’s [Service Provider
Interfaces (SPI)](https://docs.oracle.com/javase/tutorial/sound/SPI-intro.html "https://docs.oracle.com/javase/tutorial/sound/SPI-intro.html") to load components such as connectors and formats. Multiple
Flink dependencies using SPI [may cause clashes in the uber-jar](https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/table/overview/#transform-table-connectorformat-resources "https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/table/overview/#transform-table-connectorformat-resources") and unexpected application behaviors. We
recommend that you add the [ServiceResourceTransformer](https://maven.apache.org/plugins/maven-shade-plugin/examples/resource-transformers.html "https://maven.apache.org/plugins/maven-shade-plugin/examples/resource-transformers.html") of the Maven shade plugin, defined in the
pom.xml.

```
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-shade-plugin</artifactId>
                <executions>
                    <execution>
                        <id>shade</id>
                        <phase>package</phase>
                        <goals>
                            <goal>shade</goal>
                        </goals>
                        <configuration>
                            <transformers combine.children="append">
                                <!-- The service transformer is needed to merge META-INF/services files -->
                                <transformer implementation="org.apache.maven.plugins.shade.resource.ServicesResourceTransformer"/>
                                <!-- ... -->
                            </transformers>
                        </configuration>
                    </execution>
                </executions>
        </plugin>
```
