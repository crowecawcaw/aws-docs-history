Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Understanding CloudWatch alarms

CloudWatch alarms monitor information about your gateway based on metrics and expressions.
You can add CloudWatch alarms for your gateway and view their statuses in the Storage Gateway console.
For more information about the metrics that are used to monitor FSx File Gateway, see [Understanding gateway metrics](monitoring-file-gateway.md#understanding-file-gateway-metrics "monitoring-file-gateway.md#understanding-file-gateway-metrics") and [Understanding file system metrics](monitoring-file-gateway.md#monitoring-file-gateway-resources "monitoring-file-gateway.md#monitoring-file-gateway-resources"). For each alarm, you specify conditions
that will activate its ALARM state. Alarm status indicators in the Storage Gateway console turn
red when in the ALARM state, making it easier for you to monitor status proactively. You
can configure alarms to invoke actions automatically based on sustained changes in
state. For more information about CloudWatch alarms, see [Using Amazon CloudWatch
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
- Files failing upload: `FilesFailingUpload` >= 1 for 1 datapoint
  within 5 minutes
- File system error: `FileSystem-ERROR` >= 1 for 1 datapoint within 5
  minutes
- Health notifications: `HealthNotifications` >= 1 for 1 datapoints
  within 5 minutes. When configuring this alarm, set **Missing data
  treatment** to **notBreaching**.

###### Note

You can set a health notification alarm only if the gateway had a previous
health notification in CloudWatch.
For gateways on VMware host platforms that are part of a VMware High Availability
cluster, we also recommend this additional CloudWatch alarm:

- Availability notifications: `AvailabilityNotifications` >= 1 for 1
  datapoints within 5 minutes. When configuring this alarm, set **Missing
  data treatment** to **notBreaching**.
  The following table describes CloudWatch alarm states.

| State                 | Description                                                                                                                                                                                         |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **OK**                | The metric or expression is within the defined threshold.                                                                                                                                           |
| **Alarm**             | The metric or expression is outside of the defined<br>threshold.                                                                                                                                    |
| **Insufficient data** | The alarm has just started, the metric is not available, or not<br>enough data is available for the metric to determine the alarm<br>state.                                                         |
| **None**              | No alarms are created for the gateway. To create a new alarm, see<br>[Create a custom CloudWatch alarm for your<br>gateway](cloudwatch-alarms-create-alarm.md "cloudwatch-alarms-create-alarm.md"). |
| **Unavailable**       | The state of the alarm is unknown. Choose<br>**Unavailable\*<br>• to view error information in<br>the **Monitoring\*<br>• tab.                                                                      |
