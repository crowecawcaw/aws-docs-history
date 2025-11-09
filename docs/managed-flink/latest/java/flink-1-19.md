Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Amazon Managed Service for Apache Flink 1.19

Managed Service for Apache Flink now supports Apache Flink version 1.19.1. This section introduces you to
the key new features and changes introduced with Managed Service for Apache Flink support of Apache Flink
1.19.1.

###### Note

If you are using an earlier supported version of Apache Flink and want to upgrade
your existing applications to Apache Flink 1.19.1, you can do so using in-place
Apache Flink version upgrades. For more information, see [Use in-place version upgrades for Apache
Flink](how-in-place-version-upgrades.md "how-in-place-version-upgrades.md"). With in-place version upgrades,
you retain application traceability against a single ARN across Apache Flink
versions, including snapshots, logs, metrics, tags, Flink configurations, and more.

## Supported features

Apache Flink 1.19.1 introduces improvements in the SQL API, such as named
parameters, custom source parallelism, and different state TTLs for various Flink
operators.

| Supported features and related documentation                           | Supported features                                                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                | Apache Flink documentation reference |
| ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------ |
| SQL API: Support Configuring Different State TTLs using SQL<br>Hint    | Users can now configure state TTL on stream regular joins and group<br>aggregate.                                                                                                                                                                                                            | [FLIP-373: Configuring Different State TTLs using SQL Hint](https://cwiki.apache.org/confluence/display/FLINK/FLIP-373%3A+Support+Configuring+Different+State+TTLs+using+SQL+Hint "https://cwiki.apache.org/confluence/display/FLINK/FLIP-373%3A+Support+Configuring+Different+State+TTLs+using+SQL+Hint")                                                                                 |
| SQL API: Support named parameters for functions and call<br>procedures | Users can now use named parameters in functions, rather than relying<br>on the order of parameters.                                                                                                                                                                                          | [FLIP-378: Support named parameters for functions and call procedures](https://cwiki.apache.org/confluence/display/FLINK/FLIP-387%3A+Support+named+parameters+for+functions+and+call+procedures "https://cwiki.apache.org/confluence/display/FLINK/FLIP-387%3A+Support+named+parameters+for+functions+and+call+procedures")                                                                |
| SQL API: Setting parallelism for SQL sources                           | Users can now specify parallelism for SQL sources.                                                                                                                                                                                                                                           | [FLIP-367: Support Setting Parallelism for Table/SQL Sources](https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=263429150 "https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=263429150")                                                                                                                                                                     |
| SQL API: Support Session Window TVF                                    | Users can now use session window Table-Valued Functions.                                                                                                                                                                                                                                     | [FLINK-24024: Support session Window TVF](https://issues.apache.org/jira/browse/FLINK-24024 "https://issues.apache.org/jira/browse/FLINK-24024")                                                                                                                                                                                                                                           |
| SQL API: Window TVF Aggregation Supports Changelog Inputs              | Users can now perform window aggregation on changelog inputs.                                                                                                                                                                                                                                | [FLINK-20281: Window aggregation supports changelog stream input](https://issues.apache.org/jira/browse/FLINK-20281 "https://issues.apache.org/jira/browse/FLINK-20281")                                                                                                                                                                                                                   |
| Support Python 3.11                                                    | Flink now supports Python 3.11, which is 10-60% faster compared to<br>Python 3.10. For more information, see [What's New in Python 3.11](https://docs.python.org/3/whatsnew/3.11.html#summary-release-highlights "https://docs.python.org/3/whatsnew/3.11.html#summary-release-highlights"). | [FLINK-33030: Add python 3.11 support](https://issues.apache.org/jira/browse/FLINK-33030 "https://issues.apache.org/jira/browse/FLINK-33030")                                                                                                                                                                                                                                              |
| Provide metrics for TwoPhaseCommitting sink                            | Users can view statistics around the status of committers in two<br>phase committing sinks.                                                                                                                                                                                                  | [FLIP-371: Provide initialization context for Committer creation in TwoPhaseCommittingSink](https://cwiki.apache.org/confluence/display/FLINK/FLIP-371%3A+Provide+initialization+context+for+Committer+creation+in+TwoPhaseCommittingSink "https://cwiki.apache.org/confluence/display/FLINK/FLIP-371%3A+Provide+initialization+context+for+Committer+creation+in+TwoPhaseCommittingSink") |
| Trace Reporters for job restart and checkpointing                      | Users can now monitor traces around checkpoint duration and recvery<br>trends. In Amazon Managed Service for Apache Flink, we enable Slf4j trace reporters by default, so<br>users can monitor checkpoint and job traces through application<br>CloudWatch Logs.                             | [FLIP-384: Introduce TraceReporter and use it to create checkpointing and recovery traces](https://cwiki.apache.org/confluence/display/FLINK/FLIP-384%3A+Introduce+TraceReporter+and+use+it+to+create+checkpointing+and+recovery+traces "https://cwiki.apache.org/confluence/display/FLINK/FLIP-384%3A+Introduce+TraceReporter+and+use+it+to+create+checkpointing+and+recovery+traces")    |

###### Note

You can opt into the following features by submitting a [support
case](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/"):

| Opt-in features and related documentation                                        | Opt-in features                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                          | Apache Flink documentation reference |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------ |
| Support using larger checkpointing interval when source is<br>processing backlog | This is an opt-in feature, because users must tune the<br>configuration for their specific job requirements.                                                                                                               | [FLIP-309: Support using larger checkpointing interval when source is processing backlog](https://cwiki.apache.org/confluence/display/FLINK/FLIP-309%3A+Support+using+larger+checkpointing+interval+when+source+is+processing+backlog "https://cwiki.apache.org/confluence/display/FLINK/FLIP-309%3A+Support+using+larger+checkpointing+interval+when+source+is+processing+backlog") |
| Redirect System.out and System.err to Java logs                                  | This is an opt-in feature. On Amazon Managed Service for Apache Flink, the default behavior is<br>to ignore output from System.out and System.err because best<br>practice in production is to use the native Java logger. | [FLIP-390: Support System out and err to be redirected to LOG or discarded](https://cwiki.apache.org/confluence/display/FLINK/FLIP-390%3A+Support+System+out+and+err+to+be+redirected+to+LOG+or+discarded "https://cwiki.apache.org/confluence/display/FLINK/FLIP-390%3A+Support+System+out+and+err+to+be+redirected+to+LOG+or+discarded")                                           |

For the Apache Flink 1.19.1 release documentation, see [Apache Flink Documentation v1.19.1](https://nightlies.apache.org/flink/flink-docs-stable/ "https://nightlies.apache.org/flink/flink-docs-stable/").

## Changes in Amazon Managed Service for Apache Flink 1.19.1

**Logging Trace Reporter enabled by default**

Apache Flink 1.19.1 introduced checkpoint and recovery traces, enabling users to
better debug checkpoint and job recovery issues. In Amazon Managed Service for Apache Flink, these traces are
logged into the CloudWatch log stream, allowing users to break down the time spent on job
initialization, and record the historical size of checkpoints.

**Default restart strategy is now
exponential-delay**

In Apache Flink 1.19.1, there are significant improvements to the
exponential-delay restart strategy. In Amazon Managed Service for Apache Flink from Flink 1.19.1 onwards, Flink
jobs use the exponential-delay restart strategy by default. This means that user
jobs will recover quicker from transient errors, but will not overload external
systems if job restarts persist.

**Backported bug fixes**

Amazon Managed Service for Apache Flink backports fixes from the Flink community for critical issues. This means
that the runtime differs from the Apache Flink 1.19.1 release. Following is a list
of bug fixes that we have backported:

| Backported bug fixes                                                                                                 | Apache Flink JIRA link                                                                                                 | Description |
| -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------- |
| [FLINK-35531](https://issues.apache.org/jira/browse/FLINK-35531 "https://issues.apache.org/jira/browse/FLINK-35531") | This fix addresses the performance regression introduced in<br>1.17.0 that causes slower writes to HDFS.               |
| [FLINK-35157](https://issues.apache.org/jira/browse/FLINK-35157 "https://issues.apache.org/jira/browse/FLINK-35157") | This fix addresses the issue of stuck Flink jobs when sources<br>with watermark alignment encounter finished subtasks. |
| [FLINK-34252](https://issues.apache.org/jira/browse/FLINK-34252 "https://issues.apache.org/jira/browse/FLINK-34252") | This fix addresses the issue in watermark generation that results in an erroneous IDLE watermark state.                |
| [FLINK-34252](https://issues.apache.org/jira/browse/FLINK-34252 "https://issues.apache.org/jira/browse/FLINK-34252") | This fix addresses the performance regression during watermark generation by reducing system calls.                    |
| [FLINK-33936](https://issues.apache.org/jira/browse/FLINK-33936 "https://issues.apache.org/jira/browse/FLINK-33936") | This fix addresses the issue with duplicate records during mini-batch aggregation on Table API.                        |
| [FLINK-35498](https://issues.apache.org/jira/browse/FLINK-35498 "https://issues.apache.org/jira/browse/FLINK-35498") | This fix addresses the issue with argument name conflicts when defining named parameters in Table API UDFs.            |
| [FLINK-33192](https://issues.apache.org/jira/browse/FLINK-33192 "https://issues.apache.org/jira/browse/FLINK-33192") | This fix addresses the issue of a state memory leak in window operators due to improper timer cleanup.                 |
| [FLINK-35069](https://issues.apache.org/jira/browse/FLINK-35069 "https://issues.apache.org/jira/browse/FLINK-35069") | This fix addresses the issue when a Flink job gets stuck triggering a timer at the end of a window.                    |
| [FLINK-35832](https://issues.apache.org/jira/browse/FLINK-35832 "https://issues.apache.org/jira/browse/FLINK-35832") | This fix addresses the issue when IFNULL returns incorrect results.                                                    |
| [FLINK-35886](https://issues.apache.org/jira/browse/FLINK-35886 "https://issues.apache.org/jira/browse/FLINK-35886") | This fix addresses the issue when backpressured tasks are considered as idle.                                          |

## Components

| Component                                                                                                                                     | Version                                                                                                                                                                                                                                            |
| --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Java                                                                                                                                          | 11 (recommended)                                                                                                                                                                                                                                   |
| Python                                                                                                                                        | 3.11                                                                                                                                                                                                                                               |
| Kinesis Data Analytics Flink Runtime (aws-kinesisanalytics-runtime)                                                                           | 1.2.0                                                                                                                                                                                                                                              |
| Connectors                                                                                                                                    | For information about available connectors, see [Apache<br>Flink connectors](how-flink-connectors.md "how-flink-connectors.md").                                                                                                                   |
| [Apache Beam (Beam applications only)](https://aws.amazon.com/developer/language/python/ "https://aws.amazon.com/developer/language/python/") | From version 2.61.0. For more information, see [Flink Version Compatibility](https://beam.apache.org/documentation/runners/flink/#flink-version-compatibility "https://beam.apache.org/documentation/runners/flink/#flink-version-compatibility"). |

## Known issues

**Amazon Managed Service for Apache Flink Studio**

Studio uses Apache Zeppelin notebooks to provide a single-interface development
experience for developing, debugging code, and running Apache Flink stream
processing applications. An upgrade is required to Zeppelin’s Flink Interpreter to
enable support of Flink 1.19. This work is scheduled with the Zeppelin community and
we will update these notes when it is complete. You can continue to use Flink 1.15
with Amazon Managed Service for Apache Flink Studio. For more information, see [Creating a Studio
notebook](how-zeppelin-creating.md "how-zeppelin-creating.md").
