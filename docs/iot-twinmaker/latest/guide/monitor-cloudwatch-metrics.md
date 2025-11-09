# Monitoring AWS IoT TwinMaker with Amazon CloudWatch metrics

You can monitor AWS IoT TwinMaker by using CloudWatch, which collects raw data and processes it into
readable, near real-time metrics. These statistics are kept for 15 months, so that you
can access historical information and gain a better perspective on how your web
application or service is performing. You can also set alarms that watch for certain
thresholds, and send notifications or take actions when those thresholds are met. For
more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

AWS IoT TwinMaker publishes the metrics and dimensions listed in the following sections to the
`AWS/IoTTwinMaker` namespace.

###### Tip

AWS IoT TwinMaker publishes metrics on a one minute interval. When you view these metrics in
graphs in the CloudWatch console, we recommend that you choose a
**Period** of **1 minute** to see the highest
available resolution of your metric data.

###### Contents

- [Metrics](monitor-cloudwatch-metrics.md#gateway-metrics "monitor-cloudwatch-metrics.md#gateway-metrics")

## Metrics

AWS IoT TwinMaker publishes the following metrics.

| Metrics                        | Metric                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `ComponentTypeCreationFailure` | This metric reports whether the component type creation is<br>successful.<br>The metric is published when a component type is in<br>`CREATING` state. This happens when a<br>component type is created with the required properties in the<br>schema initializer and these properties are instantiated with<br>default values.<br>The metric value can be either `0` for success or<br>`1` for failure.<br>**Dimensions**: ComponentTypeId, WorkspaceId.<br>**Units**: Count |
| `ComponentTypeUpdateFailure`   | This metric reports whether the component type update is<br>successful.<br>The metric is published when a component type is in<br>`UPDATING` state. This happens when a component<br>type is updated with the required properties in the schema<br>initializer and these properties are instantiated with default<br>values.<br>The metric value can be either `0` for success or<br>`1` for failure.<br>**Dimensions**: ComponentTypeId, WorkspaceId.<br>**Units**: Count   |
| `EntityCreationFailure`        | This metric reports whether the entity creation is<br>successful. The metric is published when an entity is in<br>`CREATING` state. This happens when an entity is created with a component.<br>The metric value can be either `0` for success or<br>`1` for failure.<br>**Dimensions**: EntityName, EntityId, WorkspaceId.<br>**Units**: Count                                                                                                                              |
| `EntityUpdateFailure`          | This metric reports whether the entity update is<br>successful. The metric is published when an entity is in<br>`UPDATING` state. This happens when an entity is updated.<br>The metric value can be either `0` for success or<br>`1` for failure.<br>**Dimensions**: EntityName, EntityId, WorkspaceId.<br>**Units**: Count                                                                                                                                                 |
| `EntityDeletionFailure`        | This metric reports whether the entity deletion is<br>successful. The metric is published when an entity is in<br>`DELETING` state. This happens when an entity is deleted.<br>The metric value can be either `0` for success or<br>`1` for failure.<br>**Dimensions**: EntityName, EntityId, WorkspaceId.<br>**Units**: Count                                                                                                                                               |

###### Tip

All metrics are published to the `AWS/IoTTwinMaker` namespace.
