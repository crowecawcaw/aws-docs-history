

# Amazon Managed Service for Apache Flink 2.3
<a name="flink-2-3"></a>

Managed Service for Apache Flink now supports Apache Flink version 2.3.0. This section introduces you to the key new features and changes introduced with Managed Service for Apache Flink support of Apache Flink 2.3.0.

**Note**  
If you are using an earlier supported version of Apache Flink and want to upgrade your existing applications to Apache Flink 2.3.0, you can do so using in-place Apache Flink version upgrades. For more information, see [Use in-place version upgrades for Apache Flink](how-in-place-version-upgrades.md). With in-place version upgrades, you retain application traceability against a single ARN across Apache Flink versions, including snapshots, logs, metrics, tags, Flink configurations, and more.

**Note**  
Upgrading from Flink 1.x to Flink 2.3 is a major version upgrade with breaking changes and state compatibility considerations. Before upgrading from 1.x, review [Breaking changes and deprecations](flink-2-2.md#flink-2-2-breaking-changes) and [State compatibility guide for Flink 2.2 upgrades](state-compatibility.md).

## Supported features
<a name="flink-2-3-supported-features"></a>

Apache Flink 2.3.0 introduces improvements in the SQL API, adaptive partition selection for skewed workloads, and the Flink dashboard.


**Supported features and related documentation**  

| Supported features | Description | Apache Flink documentation reference | 
| --- | --- | --- | 
| Improvements to SinkUpsertMaterializer and changelog disorder | Improves update ordering when writing CDC or changelog streams to upsert sinks. | [FLIP-558: Improvements to SinkUpsertMaterializer and changelog disorder](https://cwiki.apache.org/confluence/display/FLINK/FLIP-558) | 
| Application Management read APIs | New read-only endpoints for application-level observability. Write endpoints are disabled in Amazon Managed Service for Apache Flink. | [FLIP-549: Application Management](https://cwiki.apache.org/confluence/display/FLINK/FLIP-549), [FLIP-560: Application Management Capability Enhancement](https://cwiki.apache.org/confluence/x/5AAXG) | 
| Adaptive Partition Selection for StreamPartitioner | Opt-in throughput optimization for skewed `Rebalance` and `Rescale` partitioners. Disabled by default; enable with `taskmanager.network.adaptive-partitioner.enabled`. | [FLIP-339: Adaptive Partition Selection for StreamPartitioner](https://cwiki.apache.org/confluence/display/FLINK/FLIP-339) | 

**Note**  
You can opt into the following features by submitting a [support case](https://console.aws.amazon.com/support/home#/):


**Opt-in features and related documentation**  

| Opt-in features | Description | Apache Flink documentation reference | 
| --- | --- | --- | 
| Support checkpoint during recovery | This is disabled by default as it is an experimental feature in open source. You can request to enable it for your application using a support case. | [FLIP-547: Support checkpoint during recovery](https://cwiki.apache.org/confluence/display/FLINK/FLIP-547) | 

For the Apache Flink 2.3.0 release documentation, see [Apache Flink Documentation v2.3.0](https://nightlies.apache.org/flink/flink-docs-release-2.3/). For Flink 2.3 release notes, see [Release notes - Flink 2.3](https://nightlies.apache.org/flink/flink-docs-stable/release-notes/flink-2.3/).

## Changes in Amazon Managed Service for Apache Flink with Apache Flink 2.3
<a name="flink-2-3-changes"></a>

### Watermark alignment default preserved
<a name="flink-2-3-watermark-alignment"></a>

Apache Flink 2.3 changes the default behavior of watermark alignment to prevent backlogged jobs from consuming all downstream resources. In Amazon Managed Service for Apache Flink, the default value of `pipeline.watermark-alignment.max-drift` is set to `0` to preserve backward compatibility with earlier supported Apache Flink versions and protect your existing applications from a behavioral regression on upgrade. If you want the new fairness behavior, you can opt in by setting `pipeline.watermark-alignment.max-drift` programmatically in your application code. For more information, see [FLINK-37399: Watermark alignment prevents backlogged jobs from using all resources](https://issues.apache.org/jira/browse/FLINK-37399).

## Components
<a name="flink-2-3-components"></a>


**Components for Amazon Managed Service for Apache Flink 2.3**  

| Component | Version | 
| --- | --- | 
| Java | 17 (recommended) | 
| Python | 3.12 | 
| Kinesis Data Analytics Flink Runtime (aws-kinesisanalytics-runtime) | 1.2.0 | 
| Connectors | For information about available connectors, see [Apache Flink connectors](https://docs.aws.amazon.com/managed-flink/latest/java/how-flink-connectors.html). | 

## Unsupported and experimental features
<a name="flink-2-3-unsupported"></a>

The following Apache Flink 2.3 features are not supported in Amazon Managed Service for Apache Flink:
+ **Materialized Tables**: Continuously maintained, queryable table snapshots.
+ **Custom Telemetry Changes**: Custom metric reporters and telemetry configurations.
+ **Flink Native S3 FileSystem (FLIP-555)**: Native S3 File system implementation (experimental in open source)
+ **ForSt State Backend**: Disaggregated state storage (experimental in open source).
+ **Java 21**: Experimental support in open source, not supported in Managed Service for Apache Flink.

## Amazon Managed Service for Apache Flink Studio
<a name="flink-2-3-known-issues-studio"></a>

Flink 2.3 in Amazon Managed Service for Apache Flink does not support Studio applications. For more information, see [Creating a Studio notebook](https://docs.aws.amazon.com/managed-flink/latest/java/how-zeppelin-creating.html).