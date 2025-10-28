End of support notice: On May 31, 2026, AWS will end support for
AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama
resources. For more information, see [AWS Panorama end of support](panorama-end-of-support.md "panorama-end-of-support.md").

# Monitoring appliances and applications with Amazon CloudWatch

When an appliance is online, AWS Panorama sends metrics to Amazon CloudWatch. You can build graphs and dashboards with these
metrics in the CloudWatch console to monitor appliance activity, and set alarms that notify you when devices go offline or
applications encounter
errors.

###### To view metrics in the CloudWatch console

1. Open the [AWS Panorama
   console Metrics page](<https://console.aws.amazon.com/cloudwatch/home#metricsV2:graph=~();namespace=~'PanoramaDeviceMetrics> "https://console.aws.amazon.com/cloudwatch/home#metricsV2:graph=~();namespace=~'PanoramaDeviceMetrics") (`PanoramaDeviceMetrics` namespace).
2. Choose a dimension schema.
3. Choose metrics to add them to the graph.
4. To choose a different statistic and customize the graph, use the options on the **Graphed
   metrics** tab. By default, graphs use the `Average` statistic for all metrics.

###### Pricing

CloudWatch has an Always Free tier. Beyond the free tier threshold, CloudWatch charges for metrics, dashboards, alarms,
logs, and insights. For details, see [CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

For more information about CloudWatch, see the [_Amazon CloudWatch User Guide_](../../../AmazonCloudWatch/latest/DeveloperGuide.md "../../../AmazonCloudWatch/latest/DeveloperGuide.md").

###### Sections

- [Using device metrics](#monitoring-cloudwatch-device "#monitoring-cloudwatch-device")
- [Using application metrics](#monitoring-cloudwatch-application "#monitoring-cloudwatch-application")
- [Configuring alarms](#monitoring-cloudwatch-alarms "#monitoring-cloudwatch-alarms")

## Using device metrics

When an appliance is online, it sends metrics to Amazon CloudWatch. You can use these metrics to monitor device
activity and trigger an alarm if devices go offline.

- `DeviceActive` – Sent periodically when the device is active.

Dimensions – `DeviceId` and `DeviceName`.

View the `DeviceActive` metric with the `Average` statistic.

## Using application metrics

When an application encounters an error, it sends metrics to Amazon CloudWatch. You can use these metrics to trigger an
alarm if an application stops running.

- `ApplicationErrors` – The number of application errors recorded.

Dimensions – `ApplicationInstanceName` and `ApplicationInstanceId`.

View the application metrics with the `Sum` statistic.

## Configuring alarms

To get notifications when a metric exceeds a threshold, create an alarm. For example, you can create an alarm
that sends a notification when the sum of the `ApplicationErrors` metric stays at 1 for 20
minutes.

###### To create an alarm

1. Open the [Amazon CloudWatch console Alarms
   page](https://console.aws.amazon.com/cloudwatch/home#alarmsV2: "https://console.aws.amazon.com/cloudwatch/home#alarmsV2:").
2. Choose **Create alarm**.
3. Choose **Select metric** and locate a metric for your device, such as
   `ApplicationErrors` for
   `applicationInstance-gk75xmplqbqtenlnmz4ehiu7xa`,`my-application`.
4. Follow the instructions to configure a condition, action, and name for the alarm.

For detailed instructions, see [Create a CloudWatch alarm](../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md "../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md") in the
_Amazon CloudWatch User Guide_.
