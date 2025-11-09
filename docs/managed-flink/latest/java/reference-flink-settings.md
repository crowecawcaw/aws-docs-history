Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Apache Flink settings

Managed Service for Apache Flink is an implementation of the Apache Flink framework. Managed Service for Apache Flink uses the
default values described in this section. Some of these values can be set by the Managed Service for Apache Flink
applications in code, and others cannot be changed.

Use the links in this section to learn more about Apache flink settings and which ones are
modifiable.

###### This topic contains the following sections:

- [Apache Flink configuration](#apache-flink-configuration "#apache-flink-configuration")
- [State backend](#reference-defaults-state-backend "#reference-defaults-state-backend")
- [Checkpointing](#reference-defaults-checkpoint "#reference-defaults-checkpoint")
- [Savepointing](#reference-defaults-savepoint "#reference-defaults-savepoint")
- [Heap sizes](#reference-defaults-heap "#reference-defaults-heap")
- [Buffer debloating](#reference-defaults-buffer-debloating "#reference-defaults-buffer-debloating")
- [Modifiable Flink configuration properties](reference-modifiable-settings.md "reference-modifiable-settings.md")
- [View configured Flink properties](viewing-modifiable-settings.md "viewing-modifiable-settings.md")

## Apache Flink configuration

Managed Service for Apache Flink provides a default Flink configuration consisting of Apache
Flink-recommended values for most properties and a few based on common application
profiles. For more information about Flink configuration, see [Configuration](https://nightlies.apache.org/flink/flink-docs-master/docs/deployment/config/ "https://nightlies.apache.org/flink/flink-docs-master/docs/deployment/config/"). Service-provided default configuration works for most
applications. However, to tweak Flink configuration properties to improve performance
for certain applications with high parallelism, high memory and state usage, or enable
new debugging features in Apache Flink, you can change certain properties by requesting
a support case. For more information, see [AWS Support
Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/"). You can check the current configuration for your application using
the [Apache Flink Dashboard](how-dashboard.md "how-dashboard.md").

## State backend

Managed Service for Apache Flink stores transient data in a state backend. Managed Service for Apache Flink uses the **RocksDBStateBackend**. Calling `setStateBackend` to set a different backend has no effect.

We enable the following features on the state backend:

- Incremental state backend snapshots
- Asynchronous state backend snapshots
- Local recovery of checkpoints

For more information about state backends, see [State Backends](https://nightlies.apache.org/flink/flink-docs-release-1.19/ops/state/state_backends.html "https://nightlies.apache.org/flink/flink-docs-release-1.19/ops/state/state_backends.html")
in the Apache Flink Documentation.

## Checkpointing

Managed Service for Apache Flink uses a default checkpoint configuration with the following values.
Some of these values can be changed using [CheckpointConfiguration](../apiv2/API_CheckpointConfiguration.md "../apiv2/API_CheckpointConfiguration.md"). You must set
`CheckpointConfiguration.ConfigurationType` to `CUSTOM` for
Managed Service for Apache Flink to use modified checkpointing values.

| Setting                           | Can be modified? | How                                                                                                                                                                                                                                                                                                                                                               | Default Value                                                                |
| --------------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| CheckpointingEnabled              | Modifiable       | [Create Application](../apiv2/API_CreateApplication.md "../apiv2/API_CreateApplication.md")<br>[Update Application](../apiv2/API_UpdateApplication.md "../apiv2/API_UpdateApplication.md")<br>[AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/AWS_KinesisAnalyticsV2.md "../../../AWSCloudFormation/latest/UserGuide/AWS_KinesisAnalyticsV2.md") | True                                                                         |
| CheckpointInterval                | Modifiable       | [Create Application](../apiv2/API_CreateApplication.md "../apiv2/API_CreateApplication.md")<br>[Update Application](../apiv2/API_UpdateApplication.md "../apiv2/API_UpdateApplication.md")<br>[AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/AWS_KinesisAnalyticsV2.md "../../../AWSCloudFormation/latest/UserGuide/AWS_KinesisAnalyticsV2.md") | 60000                                                                        |
| MinPauseBetweenCheckpoints        | Modifiable       | [Create Application](../apiv2/API_CreateApplication.md "../apiv2/API_CreateApplication.md")<br>[Update Application](../apiv2/API_UpdateApplication.md "../apiv2/API_UpdateApplication.md")<br>[AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/AWS_KinesisAnalyticsV2.md "../../../AWSCloudFormation/latest/UserGuide/AWS_KinesisAnalyticsV2.md") | 5000                                                                         |
| Unaligned checkpoints             | Modifiable       | [Support case](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/")                                                                                                                                                                                                                                                     | False                                                                        |
| Number of Concurrent Checkpoints  | Not Modifiable   | N/A                                                                                                                                                                                                                                                                                                                                                               | 1                                                                            |
| Checkpointing Mode                | Not Modifiable   | N/A                                                                                                                                                                                                                                                                                                                                                               | Exactly Once                                                                 |
| Checkpoint Retention Policy       | Not Modifiable   | N/A                                                                                                                                                                                                                                                                                                                                                               | On Failure                                                                   |
| Checkpoint Timeout                | Not Modifiable   | N/A                                                                                                                                                                                                                                                                                                                                                               | 60 minutes                                                                   |
| Max Checkpoints Retained          | Not Modifiable   | N/A                                                                                                                                                                                                                                                                                                                                                               | 1                                                                            |
| Checkpoint and Savepoint Location | Not Modifiable   | N/A                                                                                                                                                                                                                                                                                                                                                               | We store durable checkpoint and savepoint data to a service-owned S3 bucket. |

## Savepointing

By default, when restoring from a savepoint, the resume operation will try to map all state of the savepoint back to the program you are restoring with. If you dropped an operator,
by default, restoring from a savepoint that has data that corresponds to the missing operator will fail. You can allow the operation
to succeed by setting the _AllowNonRestoredState_ parameter of the application's
[FlinkRunConfiguration](../apiv2/API_FlinkRunConfiguration.md "../apiv2/API_FlinkRunConfiguration.md") to `true`. This will
allow the resume operation to skip state that cannot be mapped to the new program.

For more information, see [Allowing Non-Restored State](https://nightlies.apache.org/flink/flink-docs-release-1.15/ops/state/savepoints.html#allowing-non-restored-state "https://nightlies.apache.org/flink/flink-docs-release-1.15/ops/state/savepoints.html#allowing-non-restored-state") in the [Apache Flink documentation](https://nightlies.apache.org/flink/flink-docs-release-1.15/ "https://nightlies.apache.org/flink/flink-docs-release-1.15/").

## Heap sizes

Managed Service for Apache Flink allocates each KPU 3 GiB of JVM heap, and reserves 1 GiB for native code allocations. For information about increasing your application capacity, see [Implement application scaling in Managed Service for Apache Flink](how-scaling.md "how-scaling.md").

For more information about JVM heap sizes, see [Configuration](https://nightlies.apache.org/flink/flink-docs-release-1.15/ops/config.html "https://nightlies.apache.org/flink/flink-docs-release-1.15/ops/config.html") in the
[Apache Flink documentation](https://nightlies.apache.org/flink/flink-docs-release-1.15/ "https://nightlies.apache.org/flink/flink-docs-release-1.15/").

## Buffer debloating

Buffer debloating can help applications with high backpressure. If your application experiences failed checkpoints/savepoints, enabling this feature could be useful.
To do this, request a [support case](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

For more information, see [The Buffer Debloating Mechanism](https://nightlies.apache.org/flink/flink-docs-release-1.15/docs/deployment/memory/network_mem_tuning/#the-buffer-debloating-mechanism "https://nightlies.apache.org/flink/flink-docs-release-1.15/docs/deployment/memory/network_mem_tuning/#the-buffer-debloating-mechanism") in the
[Apache Flink documentation](https://nightlies.apache.org/flink/flink-docs-release-1.15/ "https://nightlies.apache.org/flink/flink-docs-release-1.15/").
