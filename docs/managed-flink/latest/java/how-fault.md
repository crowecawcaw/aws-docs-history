Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Implement fault tolerance in Managed Service for Apache Flink

Checkpointing is the method that is used for implementing fault tolerance in
Amazon Managed Service for Apache Flink. A _checkpoint_ is an up-to-date backup of a running
application that is used to recover immediately from an unexpected application disruption or failover.

For details on checkpointing in Apache Flink applications, see
[Checkpoints](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/ops/state/checkpoints/ "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/ops/state/checkpoints/") in the Apache Flink Documentation.

A _snapshot_ is a manually created and managed backup of application
state. Snapshots let you restore your application to a previous state by calling [`UpdateApplication`](../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md").
For more information, see [Manage application backups using snapshots](how-snapshots.md "how-snapshots.md").

If checkpointing is enabled for your application, then the service provides fault tolerance
by creating and loading backups of application data in the event of unexpected application
restarts. These unexpected application restarts could be caused by unexpected job restarts, instance failures, etc.
This gives the application the same semantics as failure-free execution during these restarts.

If snapshots are enabled for the application, and configured using the application's [ApplicationRestoreConfiguration](../../../managed-service-for-apache-flink/latest/apiv2/API_ApplicationRestoreConfiguration.md "../../../managed-service-for-apache-flink/latest/apiv2/API_ApplicationRestoreConfiguration.md"), then the service provides exactly-once
processing semantics during application updates, or during service-related scaling or maintenance.

## Configure checkpointing in Managed Service for Apache Flink

You can configure your application's checkpointing behavior. You can define whether it
persists the checkpointing state, how often it saves its state to checkpoints, and the
minimum interval between the end of one checkpoint operation and the beginning of
another.

You configure the following settings using the [`CreateApplication`](../../../managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.md") or [`UpdateApplication`](../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md") API operations:

- `CheckpointingEnabled` — Indicates whether checkpointing is
  enabled in the application.
- `CheckpointInterval` — Contains the time in milliseconds
  between checkpoint (persistence) operations.
- `ConfigurationType` — Set this value to `DEFAULT`
  to use the default checkpointing behavior. Set this value to `CUSTOM`
  to configure other values.

###### Note

The default checkpoint behavior is as follows:

    + **CheckpointingEnabled:** true
    + **CheckpointInterval:** 60000
    + **MinPauseBetweenCheckpoints:** 5000If **ConfigurationType** is set to `DEFAULT`, the preceding values will be used,

even if they are set to other values using either using the AWS Command Line Interface, or by setting the values in the application code.

###### Note

For Flink 1.15 onward, Managed Service for Apache Flink will use `stop-with-savepoint` during Automatic Snapshot Creation, that is, application update, scaling or stopping.

- `MinPauseBetweenCheckpoints` — The minimum time in
  milliseconds between the end of one checkpoint operation and the start of
  another. Setting this value prevents the application from checkpointing
  continuously when a checkpoint operation takes longer than the
  `CheckpointInterval`.

## Review checkpointing API examples

This section includes example requests for API actions for configuring checkpointing
for an application. For information about how to use a JSON file for input for an API
action, see [Managed Service for Apache Flink API example code](api-examples.md "api-examples.md").

### Configure checkpointing for a new

application

The following example request for the [`CreateApplication`](../../../managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.md") action configures checkpointing when you
are creating an application:

```
{
   "ApplicationName": "MyApplication",
   "RuntimeEnvironment":"FLINK-1_19",
   "ServiceExecutionRole":"arn:aws:iam::123456789123:role/myrole",
   "ApplicationConfiguration": {
      "ApplicationCodeConfiguration":{
      "CodeContent":{
        "S3ContentLocation":{
          "BucketARN":"arn:aws:s3:::amzn-s3-demo-bucket",
          "FileKey":"myflink.jar",
          "ObjectVersion":"AbCdEfGhIjKlMnOpQrStUvWxYz12345"
        }
      },
      "FlinkApplicationConfiguration": {
         "CheckpointConfiguration": {
            "CheckpointingEnabled": "true",
            "CheckpointInterval": 20000,
            "ConfigurationType": "CUSTOM",
            "MinPauseBetweenCheckpoints": 10000
         }
      }
}
```

### Disable checkpointing for a new

application

The following example request for the [`CreateApplication`](../../../managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.md") action disables checkpointing when you
are creating an application:

```
{
   "ApplicationName": "MyApplication",
   "RuntimeEnvironment":"FLINK-1_19",
   "ServiceExecutionRole":"arn:aws:iam::123456789123:role/myrole",
   "ApplicationConfiguration": {
      "ApplicationCodeConfiguration":{
      "CodeContent":{
        "S3ContentLocation":{
          "BucketARN":"arn:aws:s3:::amzn-s3-demo-bucket",
          "FileKey":"myflink.jar",
          "ObjectVersion":"AbCdEfGhIjKlMnOpQrStUvWxYz12345"
        }
      },
      "FlinkApplicationConfiguration": {
         "CheckpointConfiguration": {
            "CheckpointingEnabled": "false"
         }
      }
}
```

### Configure checkpointing for an

existing application

The following example request for the [`UpdateApplication`](../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md") action configures checkpointing for an
existing application:

```
{
   "ApplicationName": "MyApplication",
   "ApplicationConfigurationUpdate": {
      "FlinkApplicationConfigurationUpdate": {
         "CheckpointConfigurationUpdate": {
            "CheckpointingEnabledUpdate": true,
            "CheckpointIntervalUpdate": 20000,
            "ConfigurationTypeUpdate": "CUSTOM",
            "MinPauseBetweenCheckpointsUpdate": 10000
         }
      }
   }
}
```

### Disable checkpointing for an

existing application

The following example request for the [`UpdateApplication`](../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md") action disables checkpointing for an
existing application:

```
{
   "ApplicationName": "MyApplication",
   "ApplicationConfigurationUpdate": {
      "FlinkApplicationConfigurationUpdate": {
         "CheckpointConfigurationUpdate": {
            "CheckpointingEnabledUpdate": false,
            "CheckpointIntervalUpdate": 20000,
            "ConfigurationTypeUpdate": "CUSTOM",
            "MinPauseBetweenCheckpointsUpdate": 10000
         }
      }
   }
}
```
