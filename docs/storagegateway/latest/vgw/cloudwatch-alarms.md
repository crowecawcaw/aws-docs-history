# Understanding CloudWatch alarms

CloudWatch alarms monitor information about your gateway based on metrics and expressions.
You can add CloudWatch alarms for your gateway and view their statuses in the Storage Gateway console.
For more information about the metrics that are used to monitor Volume Gateway, see [Understanding gateway metrics](Main_monitoring-gateways-common.md#MonitoringGateways-common "Main_monitoring-gateways-common.md#MonitoringGateways-common") and [Understanding Volume Metrics](monitoring-volume-gateway.md#MonitoringVolumes-common "monitoring-volume-gateway.md#MonitoringVolumes-common"). For each alarm, you specify conditions that
will initiate its ALARM state. Alarm status indicators in the Storage Gateway console turn red
when in the ALARM state, making it easier for you to monitor status proactively. You can
configure alarms to invoke actions automatically based on sustained changes in state.
For more information about CloudWatch alarms, see [Using Amazon CloudWatch
alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the _Amazon CloudWatch User Guide_.

###### Note

If you don't have permission to view CloudWatch, you can't view the
alarms.

For each activated gateway, we recommend that you create the following CloudWatch
alarms:

- High IO wait: `IoWaitpercent` >= 20 for 3 datapoints in 15
  minutes
- Cache percent dirty: `CachePercentDirty` > 80 for 4 datapoints
  within 20 minutes
- Health notifications: `HealthNotifications` >= 1 for 1 datapoint
  within 5 minutes. When configuring this alarm, set **Missing data
  treatment** to **notBreaching**.

###### Note

You can set a health notification alarm only if the gateway had a previous
health notification in CloudWatch.
For gateways on VMware host platforms with HA mode activated, we also recommend this
additional CloudWatch alarm:

- Availability notifications: `AvailabilityNotifications` >= 1 for 1
  datapoint within 5 minutes. When configuring this alarm, set **Missing
  data treatment** to **notBreaching**.
  The following table describes the state of an alarm.

| State                 | Description                                                                                                                                                                                     |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **OK**                | The metric or expression is within the defined threshold.                                                                                                                                       |
| **Alarm**             | The metric or expression is outside of the defined threshold.                                                                                                                                   |
| **Insufficient data** | The alarm has just started, the metric is not available, or not enough data is available for the metric to determine the alarm state.                                                           |
| **None**              | No alarms are created for the gateway. To create a new alarm, see [Creating a custom CloudWatch alarm for your gateway](cloudwatch-alarms-create-alarm.md "cloudwatch-alarms-create-alarm.md"). |
| **Unavailable**       | The state of the alarm is unknown. Choose **Unavailable** to view error information in the **Monitoring** tab.                                                                                  |
