

# Amazon Managed Service for Apache Flink 2.2
<a name="flink-2-2"></a>

Amazon Managed Service for Apache Flink now supports Apache Flink version 2.2. This is the first major version upgrade for the service. This page covers the capabilities introduced in Flink 2.2, along with important considerations for upgrading from Flink 1.x.

**Note**  
Flink 2.2 introduces breaking changes that require careful planning. Review the full list of breaking changes and deprecations below and the [State compatibility guide for Flink 2.2 upgrades](state-compatibility.md) before upgrading from 1.x.

## What's new in Amazon Managed Service for Apache Flink 2.2
<a name="flink-2-2-whats-new"></a>

Amazon Managed Service for Apache Flink 2.2 introduces behavioral changes that may break existing applications upon upgrade. Review these carefully alongside the Flink API changes in the next section.

**Programmatic Configuration Handling**
+ MSF Flink 2.2 now reports an exception when customers attempt to modify configs not supported by MSF through `env.getConfig().set()` or similar APIs. See [Programmatic Flink configuration properties](programmatic-configuration.md).
+ Customers can still request to change certain configs through support tickets (see [Modifiable Settings](https://docs.aws.amazon.com/managed-flink/latest/java/reference-modifiable-settings.html))

**Metrics Removal**
+ The `fullRestarts` metric has been removed in Flink 2.2. Use the `numRestarts` metric instead.
+ The `bytesRequestedPerFetch` metric for KDS connector has been removed in Flink AWS connector version 6.0.0 (only connector version compatible with Flink 2.2).
+ The `uptime` and `downtime` metrics are both marked as deprecated in Flink 2.2 and will be removed soon. Replace `uptime` with the new metric `runningTime`. Replace `downtime` with one or more of `restartingTime`, `cancellingTime`, and `failingTime`.
+ See [Metrics and Dimensions page](https://docs.aws.amazon.com/managed-flink/latest/java/metrics-dimensions.html) for full list of supported metrics.

**Non-Credential IMDS Calls Blocked**
+ These allowed endpoints are used by the AWS SDK's **DefaultCredentialsProvider** (`/latest/meta-data/iam/security-credentials/`) and **DefaultAwsRegionProviderChain** (`/latest/dynamic/instance-identity/document`) to automatically configure credentials and region for your application.
+ Applications using AWS SDK functions that rely on non-credential IMDS calls (such as `EC2MetadataUtils.getInstanceId()`, `EC2MetadataUtils.getInstanceType()`, `EC2MetadataUtils.getLocalHostName()`, or `EC2MetadataUtils.getAvailabilityZone()`) will receive HTTP 4xx errors when attempting these calls.
+ If your application uses IMDS for instance metadata or other information outside the allowed paths, refactor your code to use environment variables or application configuration instead.

**Read-Only Root Filesystem**
+ To improve security, any dependency outside of `/tmp` which is the default flink working directory will result in: `java.io.FileNotFoundException: /{path}/{filename} (Read-only file system)`.
+ Filesystem dependencies can originate directly from your code or indirectly from libraries included in your dependencies. Override direct filesystem dependencies to `/tmp/` in your code. For indirect filesystem dependencies from libraries, use library configuration overrides to redirect filesystem operations to `/tmp/`.

## Breaking changes and deprecations
<a name="flink-2-2-breaking-changes"></a>

Below is a summary of breaking changes and deprecations introduced in Managed Service for Apache Flink 2.2. See [Apache Flink 2.0 Release Notes](https://nightlies.apache.org/flink/flink-docs-stable/release-notes/flink-2.0/) for full release notes of Apache Flink 2.0 that introduces these breaking changes.

**DataSet API Removed**
+ The legacy DataSet API for batch processing has been completely removed in Flink 2.0\+. All batch processing must now use the unified DataStream API.
+ Applications using the DataSet API must be migrated to DataStream API before upgrading. See [Apache Flink migration guide for DataSet to DataStream](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/dev/datastream/dataset_migration/) conversion

**Java 11 and Python 3.8 Removed**
+ Java 11 support completely removed; Java 17 is the default and recommended runtime.
+ Python 3.8 support removed; Python 3.12 is now the default.

**Legacy Connector Classes Removed**
+ The legacy `SourceFunction` and `SinkFunction` interfaces have been superseded by the new unified Source (FLIP-27) and Sink (FLIP-143) APIs, which provide better support for bounded/unbounded duality, improved checkpoint coordination, and a cleaner programming model.
+ For Kinesis Data Streams, use `KinesisStreamsSource` and `KinesisStreamsSink` from `flink-connector-aws-kinesis-streams:6.0.0-2.0`.

**Scala API removed**
+ The Flink Scala API has been removed. Flink's Java API is now the single supported API for JVM-based applications.
+ If your application is written in Scala, you can still use Flink's Java API from Scala code — the main change is that the Scala-specific wrappers and implicit conversions are no longer available. See [Upgrading Applications and Flink Versions](https://nightlies.apache.org/flink/flink-docs-release-2.0/docs/ops/upgrading/) for details on updating your Scala applications.

**State Compatibility Considerations**
+ Kryo serializer upgraded from version 2.24 to 5.6 may cause state compatibility issues.
+ POJOs with collections (`HashMap`, `ArrayList`, `HashSet`) may have state compatibility issues.
+ Avro and Protobuf serialization unaffected.
+ See [State compatibility guide for Flink 2.2 upgrades](state-compatibility.md) for detailed assessment to triage your application's risk level.

## Apache Flink 2.2 features supported
<a name="flink-2-2-supported-features"></a>

**Runtime and language support**



| Feature | Description | Documentation | 
| --- | --- | --- | 
| Java 17 Runtime | Java 17 is now the default and recommended runtime; Java 11 support removed. | [Java Compatibility](https://nightlies.apache.org/flink/flink-docs-stable/zh/docs/deployment/java_compatibility/) | 
| Python 3.12 Support | Python 3.12 now supported; Python 3.8 support removed. | [PyFlink Documentation](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/python/overview/) | 

**State management and performance**



| Feature | Description | Documentation | 
| --- | --- | --- | 
| RocksDB 8.10.0 | Improved I/O performance with RocksDB upgrade. | [State Backends](https://nightlies.apache.org/flink/flink-docs-release-2.0/docs/ops/state/state_backends/) | 
| Serialization Improvements | Dedicated serializers for Map, List, Set; Kryo upgraded from 2.24 to 5.6. | [Type Serialization](https://nightlies.apache.org/flink/flink-docs-release-2.0/docs/dev/datastream/fault-tolerance/serialization/types_serialization/) | 

**SQL and Table API features**



| Feature | Description | Documentation | 
| --- | --- | --- | 
| VARIANT Data Type | Native support for semi-structured data (JSON) without repeated string parsing. | [Data Types](https://nightlies.apache.org/flink/flink-docs-release-2.1/docs/dev/table/types/) | 
| Delta Join | Reduces state requirements for streaming joins by maintaining only the latest version of each key; requires customer-managed infrastructure (for example, Apache Fluss). | [Joins](https://nightlies.apache.org/flink/flink-docs-release-2.1/docs/dev/table/sql/queries/joins/) | 
| StreamingMultiJoinOperator | Executes multi-way joins as a single operator, eliminating intermediate materialization. | [FLIP-516](https://cwiki.apache.org/confluence/display/FLINK/FLIP-516) | 
| ProcessTableFunction (PTF) | Enables stateful, event-driven logic directly in SQL with per-key state and timers. | [User-Defined Functions](https://nightlies.apache.org/flink/flink-docs-release-2.1/docs/dev/table/functions/udfs/) | 
| ML\_PREDICT Function | Call registered ML models on streaming/batch tables directly from SQL. Requires customer to bundle a ModelProvider implementation (e.g., flink-model-openai). ModelProvider libraries are not shipped by Managed Service for Apache Flink. | [ML Predict](https://nightlies.apache.org/flink/flink-docs-release-2.1/docs/dev/table/sql/queries/model-inference/) | 
| Model DDL | Define ML models as first-class catalog objects using CREATE MODEL statements. | [CREATE Statements](https://nightlies.apache.org/flink/flink-docs-release-2.1/docs/dev/table/sql/create/#create-model) | 
| Vector Search | Flink SQL API supports searching vector databases. No open source VectorSearchTableSource implementation is currently available; customers must provide their own implementation. | [Flink SQL](https://nightlies.apache.org/flink/flink-docs-stable/release-notes/flink-2.2/#support-vector_search-in-flink-sql) | 

**DataStream API features**



| Feature | Description | Documentation | 
| --- | --- | --- | 
| FLIP-27 Source API | New unified source interface replacing legacy SourceFunction. | [Sources](https://nightlies.apache.org/flink/flink-docs-release-2.0/docs/dev/datastream/sources/) | 
| FLIP-143 Sink API | New unified sink interface replacing legacy SinkFunction. | [Sinks](https://nightlies.apache.org/flink/flink-docs-release-2.0/docs/dev/datastream/sinks/) | 
| Async Python DataStream | Non-blocking I/O operations in Python DataStream API using AsyncFunction. | [Async I/O](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/python/datastream/operators/async_io/) | 

## Connector availability
<a name="flink-2-2-connectors"></a>

When upgrading to Flink 2.2, you also need to update your connector dependencies to versions that are compatible with the Flink 2.2 runtime. Flink connectors are released independently from the Flink runtime, and not all connectors have a Flink 2.2-compatible release yet. The following table summarizes the availability of commonly used connectors in Amazon Managed Service for Apache Flink:


**Connector availability for Flink 2.2**  

| Connector | Flink 1.20 Version | Flink 2.0\+ Version | Notes | 
| --- | --- | --- | --- | 
| Apache Kafka | flink-connector-kafka 3.4.0-1.20 | flink-connector-kafka 4.0.0-2.0 | Recommended for Flink 2.2 | 
| Kinesis Data Streams (source) | flink-connector-kinesis 5.0.0-1.20 | flink-connector-aws-kinesis-streams 6.0.0-2.0 | Recommended for Flink 2.2 | 
| Kinesis Data Streams (sink) | flink-connector-aws-kinesis-streams 5.1.0-1.20 | flink-connector-aws-kinesis-streams 6.0.0-2.0 | Recommended for Flink 2.2 | 
| Amazon Data Firehose | flink-connector-aws-kinesis-firehose 5.1.0-1.20 | flink-connector-aws-kinesis-firehose 6.0.0-2.0 | Compatible with Flink 2.0 | 
| Amazon DynamoDB | flink-connector-dynamodb 5.1.0-1.20 | flink-connector-dynamodb 6.0.0-2.0 | Compatible with Flink 2.0 | 
| Amazon SQS | flink-connector-sqs 5.1.0-1.20 | flink-connector-sqs 6.0.0-2.0 | Compatible with Flink 2.0 | 
| FileSystem (S3, HDFS) | Bundled with Flink | Bundled with Flink | Built into the Flink distribution — always available | 
| JDBC | flink-connector-jdbc 3.3.0-1.20 | Not yet released for 2.x | No Flink 2.x-compatible release available | 
| OpenSearch | flink-connector-opensearch 1.2.0-1.19 | Not yet released for 2.x | No Flink 2.x-compatible release available | 
| Elasticsearch | Legacy connector only | Not yet released for 2.x | Consider migrating to the OpenSearch connector | 
| Amazon Managed Service for Prometheus | flink-connector-prometheus 1.0.0-1.20 | Not yet released for 2.x | No Flink 2.x-compatible release available | 
+ If your application depends on a connector that does not yet have a Flink 2.x release, you have two options: wait for the connector to release a compatible version, or evaluate whether you can replace it with an alternative (for example, using the JDBC catalog or a custom sink).
+ When updating connector versions, pay attention to artifact name changes — some connectors were renamed between major versions (for example, the Firehose connector changed from `flink-connector-aws-kinesis-firehose` to `flink-connector-aws-firehose` in some intermediate versions).
+ Always check the [Amazon Managed Service for Apache Flink connector documentation](https://docs.aws.amazon.com/managed-flink/latest/java/how-flink-connectors.html) for the exact artifact names and versions supported in your target runtime.

## Unsupported and experimental features
<a name="flink-2-2-unsupported"></a>

The following features are not supported in Amazon Managed Service for Apache Flink 2.2:
+ **Materialized Tables**: Continuously maintained, queryable table snapshots.
+ **Custom Telemetry Changes**: Custom metric reporters and telemetry configurations.
+ **ForSt State Backend**: Disaggregated state storage (experimental in open source).
+ **Java 21**: Experimental support in open source, not supported in Managed Service for Apache Flink.

## Known issues
<a name="flink-2-2-known-issues"></a>

**Amazon Managed Service for Apache Flink Studio**

Flink 2.2 in Amazon Managed Service for Apache Flink does not support Studio applications. For more information, see [Creating a Studio notebook](https://docs.aws.amazon.com/managed-flink/latest/java/how-zeppelin-creating.html).

**Kinesis Connector EFO**
+ Applications using the `KinesisStreamsSource` with EFO (Enhanced Fan-Out / SubscribeToShard) path introduced in connector v5.0.0 and v6.0.0 may fail when Kinesis streams undergo resharding. This is a known issue in the community. For more information, see [FLINK-37648](https://issues.apache.org/jira/browse/FLINK-37648).
+ Applications using the `KinesisStreamsSource` with EFO (Enhanced Fan-Out / SubscribeToShard) path introduced in connector v5.0.0 and v6.0.0 together with `KinesisStreamsSink` may experience deadlocks if the Flink application is under backpressure, resulting in a complete stop of data processing in one or more TaskManagers. A force stop operation and a start application operation are needed to recover the application. This is a sub-case of the known issue in the community. For more information, see [FLINK-34071](https://issues.apache.org/jira/browse/FLINK-34071).

## Upgrade experience
<a name="flink-2-2-upgrade"></a>

Amazon Managed Service for Apache Flink supports in-place version upgrades that preserve your application configuration, logs, metrics, tags, and—if state and binaries are compatible—your application state. For step-by-step instructions, see [Upgrading to Flink 2.2: Complete guide](flink-2-2-upgrade-guide.md).

For guidance on assessing state compatibility risk and handling incompatible state during upgrades, see [State compatibility guide for Flink 2.2 upgrades](state-compatibility.md).

## Next steps
<a name="flink-2-2-next-steps"></a>
+ New to Flink 2.2? For detailed Apache Flink 2.2 documentation, see [Apache Flink 2.2 Documentation](https://nightlies.apache.org/flink/flink-docs-release-2.2/).
+ Planning an upgrade? See [Upgrading to Flink 2.2: Complete guide](flink-2-2-upgrade-guide.md)
+ State compatibility concerns? See [State compatibility guide for Flink 2.2 upgrades](state-compatibility.md)

For questions or issues, see the [Troubleshoot Managed Service for Apache Flink](troubleshooting.md) or contact AWS Support.