

# Update a connector
<a name="mkc-update-connector"></a>

This procedure describes how to update the configuration of an existing MSK Connect connector using the AWS Management Console.

**Updating connector configuration using the AWS Management Console**

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/](https://console.aws.amazon.com/msk/).

1. In the left pane, under **MSK Connect**, choose **Connectors**.

1. Select an existing connector.

1. Choose **Edit connector configuration**.

1. Update the connector configuration. You can't override `connector.class` using UpdateConnector. The following example shows an example configuration for the Confluent Amazon S3 Sink connector. 

   ```
   connector.class=io.confluent.connect.s3.S3SinkConnector
   tasks.max=2
   topics=my-example-topic
   s3.region=us-east-1
   s3.bucket.name=amzn-s3-demo-bucket
   flush.size=1
   storage.class=io.confluent.connect.s3.storage.S3Storage
   format.class=io.confluent.connect.s3.format.json.JsonFormat
   partitioner.class=io.confluent.connect.storage.partitioner.DefaultPartitioner
   key.converter=org.apache.kafka.connect.storage.StringConverter
   value.converter=org.apache.kafka.connect.storage.StringConverter
   schema.compatibility=NONE
   ```

1. Choose **Submit**.

1. You can then monitor the current state of the operation in the **Operations** tab of the connector. 

Use the `skipHealthValidation` parameter to control whether Amazon MSK Connect runs connector-level and task-level health checks after it applies your update. If you set it to `true`, Amazon MSK Connect skips those checks. If you set it to `false` or omit it, the checks run.

Every update to a connector that is in the `PAUSED` state requires `skipHealthValidation` to be `true`, because Amazon MSK Connect cannot validate the health of a connector that is not processing records. For more information, see [Pause and resume a connector](mkc-pause-resume-connector.md).

To use the MSK Connect API to update the configuration of a connector, see [UpdateConnector](https://docs.aws.amazon.com/MSKC/latest/mskc/API_UpdateConnector.html).

## Update worker settings
<a name="mkc-update-connector-worker-settings"></a>

You can update a connector's custom plugin and worker configuration without deleting and recreating the connector. For example, you can move the connector to a new version of your plugin code, or change how its workers are configured. To do this, update the connector's worker settings. The worker settings comprise the connector's custom plugin, its worker configuration, and its capacity. You can change one or more of them in a single update:
+ Update the custom plugin. For example, to run a new version of your connector code, create a custom plugin that contains the new code, and then update the connector to use that plugin. The plugin must be in the `ACTIVE` state and in the same AWS account and Region as the connector. A connector uses exactly one plugin.
+ Update the worker configuration. Switch the connector to a different custom worker configuration, or return it to the default worker configuration that Amazon MSK Connect provides. For example, to change a worker property, create a worker configuration that contains the new value, and then update the connector to use that worker configuration. The worker configuration must be in the same AWS account and Region as the connector. For more information about worker configurations, see [Understand MSK Connect workers](msk-connect-workers.md).
+ Update the capacity. Choose new provisioned or autoscaled capacity for the connector. For more information about capacity, see [Understand connector capacity](msk-connect-capacity.md).

When you change the plugin or the worker configuration, Amazon MSK Connect starts a new set of workers with the new settings, moves the connector's tasks to the new workers, and then removes the previous workers.

Update the connector configuration and the worker settings in separate requests. In a worker settings update, specify at least one value that differs from the connector's current worker settings.

Before you update worker settings, make sure that the following prerequisites are met:
+ The connector is in the `RUNNING` or `PAUSED` state.
  + An update to a connector that is in the `PAUSED` state requires you to skip health validation, because Amazon MSK Connect cannot validate the health of a connector that is not processing records. We recommend that you resume a paused connector before updating it, so that health validation and automatic rollback apply to the update. For more information about health validation, see [Health validation and rollback](#mkc-update-connector-health-validation).
+ No other lifecycle operation is running on the connector.
+ You have the connector's current version if you use the AWS Command Line Interface (AWS CLI) or the MSK Connect API. `DescribeConnector` returns it in `currentVersion`. Each update changes the version, so get it again before you submit another update.

**Updating worker settings using the AWS Management Console**

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/](https://console.aws.amazon.com/msk/).

1. In the left pane, under **MSK Connect**, choose **Connectors**.

1. In the list of connectors, select the connector that you want to update, choose **Actions**, and then choose **Edit worker settings**.

1. Change the settings that you want to update:
   + To change the plugin, under **Choose custom plugin**, choose a custom plugin.
   + To return to the default worker configuration, under **Worker configuration**, choose **MSK default configuration**.
   + To use a custom worker configuration, under **Worker configuration**, choose **Custom configuration**, and then choose a worker configuration.
   + To change the capacity, edit the capacity settings.

1. (Optional) Select **Skip health validation and rollback**. An update to a connector that is in the `PAUSED` state requires this option.

1. Choose **Save changes**.

### Updating worker settings using the AWS CLI
<a name="mkc-update-connector-worker-settings-cli"></a>

Run the following AWS CLI command to get the connector's current version. In this command and the commands that follow, replace the placeholder values, such as {{connector\_arn}}, with your own values.

```
aws kafkaconnect describe-connector \
   --connector-arn {{connector_arn}} \
   --query currentVersion \
   --output text
```

To switch the connector to a different custom plugin, run the following AWS CLI command. Specify exactly one plugin:

```
aws kafkaconnect update-connector \
   --connector-arn {{connector_arn}} \
   --current-version {{current_version}} \
   --plugins customPlugin={customPluginArn={{custom_plugin_arn}},revision=1}
```

To switch the connector to a different custom worker configuration, run the following AWS CLI command:

```
aws kafkaconnect update-connector \
   --connector-arn {{connector_arn}} \
   --current-version {{current_version}} \
   --worker-configuration workerConfigurationArn={{worker_configuration_arn}},revision=1
```

To return the connector to the default worker configuration, run the following AWS CLI command. Use the `--use-default-worker-configuration` option without `--worker-configuration`:

```
aws kafkaconnect update-connector \
   --connector-arn {{connector_arn}} \
   --current-version {{current_version}} \
   --use-default-worker-configuration
```

You can combine the `--capacity` option, the `--plugins` option, and one of the worker configuration options in the same command. To skip health validation, add the `--skip-health-validation` option.

### Tracking the update
<a name="mkc-update-connector-worker-settings-track"></a>

The update is asynchronous. When you submit it, you receive a connector operation Amazon Resource Name (ARN). While the update runs, the connector is in the `UPDATING` state. In the console, you can monitor the operation in the **Operations** tab of the connector.

To track the update with the AWS CLI, run the following command with the `connectorOperationArn` that the `update-connector` command returned. The response reports the operation state. Its `originWorkerSetting` and `targetWorkerSetting` fields show the worker settings before and after the update:

```
aws kafkaconnect describe-connector-operation \
   --connector-operation-arn {{operation_arn}}
```

A worker settings update has the operation type `UPDATE_WORKER_SETTING`. The following states describe its progress:

`UPDATE_IN_PROGRESS`  
Amazon MSK Connect accepted the update and is applying it. The connector is in the `UPDATING` state.

`UPDATE_COMPLETE`  
The connector runs with the new worker settings. It has returned to the state that it was in before the update, `RUNNING` or `PAUSED`.

`UPDATE_FAILED`  
The update did not take effect. The connector keeps its previous worker settings and returns to the state that it was in before the update. Depending on where the update failed, Amazon MSK Connect either did not start it or rolled it back. The `errorInfo` field reports the cause. For more information about why an update fails, see [Worker settings update reaches `UPDATE_FAILED` state](msk-connect-troubleshooting.md#mkc-update-failed-causes).

### Health validation and rollback
<a name="mkc-update-connector-health-validation"></a>

After the tasks move, Amazon MSK Connect validates the connector's health on the new workers. The update fails if the connector does not become healthy, for example if tasks are failing that were not failing before the update, or if fewer tasks are running than before the update. When this validation fails, Amazon MSK Connect automatically rolls the update back. It restores the previous workers and removes the new workers, and the connector keeps its previous worker settings. The operation reaches the `UPDATE_FAILED` state.

If you skip health validation, Amazon MSK Connect does not validate the connector's health on the new workers and does not roll the update back. The update stays in effect even when the connector or its tasks are unhealthy on the new workers.

### Considerations
<a name="mkc-update-connector-considerations"></a>

Consider the following when you update worker settings:
+ During a plugin or worker configuration update, the previous workers and the new workers exist at the same time. Each worker uses one IP address from your subnets. Make sure that the subnets have enough free IP addresses for the new workers.
+ During a plugin or worker configuration update, tasks stop processing records while they move to the new workers. The connector's committed offsets are stored in Kafka topics on your cluster, and the update does not affect them. After the update, the tasks continue from the offsets that they last committed.
+ Make sure that the new plugin contains the connector class that your connector configuration specifies. Also make sure that the new worker configuration is compatible with your connector. If the connector can't start on the new workers, health validation fails and Amazon MSK Connect rolls back the update.
+ A connector uses exactly one plugin. To use more than one plugin, create a single custom plugin from a ZIP file that bundles the plugins together.
+ In a request, specify either a custom worker configuration or the default worker configuration, not both.
+ Wait for an update to complete before you perform other lifecycle operations on the connector, such as restart, pause, resume, or delete.
+ Use `DescribeConnectorOperation` with the returned `connectorOperationArn` to track whether the operation is in progress, complete, or failed.