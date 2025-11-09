# Monitor mirrored traffic using Amazon CloudWatch

You can monitor your mirrored traffic using Amazon CloudWatch, which collects information from
your network interface that is part of a traffic mirror session, and creates readable, near
real-time metrics. You can use this information to monitor and troubleshoot Traffic Mirroring.

For more information about Amazon CloudWatch, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md"). For more information,
see [CloudWatch metrics that
are available for your instances](../../../AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.md "../../../AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.md") in _Amazon EC2 User Guide_. For
more information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

## Traffic Mirroring metrics and dimensions

The following metrics are available for your mirrored traffic at the traffic mirror source:

| Metric                        | Description                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `NetworkMirrorIn`             | The number of bytes received on all network interfaces by the<br>instance that are mirrored.<br>The number reported is the number of bytes received during the<br>period. If you are using basic (five-minute) monitoring, you can<br>divide this number by 300 to find Bytes/second. If you have detailed<br>(one-minute) monitoring, divide it by 60.<br>Units: Bytes |
| `NetworkMirrorOut`            | The number of bytes sent out on all network interfaces by the<br>instance that are mirrored.<br>The number reported is the number of bytes sent during the period.<br>If you are using basic (five-minute) monitoring, you can divide this<br>number by 300 to find Bytes/second. If you have detailed<br>(one-minute) monitoring, divide it by 60.<br>Units: Bytes     |
| `NetworkPacketsMirrorIn`      | The number of packets received on all network interfaces by<br>the instance that are mirrored. This metric is available for basic<br>monitoring only.<br>Units: Count                                                                                                                                                                                                   |
| `NetworkPacketsMirrorOut`     | The number of packets sent out on all network interfaces by the<br>instance that are mirrored. This metric is available for basic<br>monitoring only.<br>Units: Count                                                                                                                                                                                                   |
| `NetworkSkipMirrorIn`         | The number of bytes received, that meet the traffic mirror filter<br>rules, that did not get mirrored because of production traffic<br>taking priority.<br>Units: Bytes                                                                                                                                                                                                 |
| `NetworkSkipMirrorOut`        | The number of bytes sent out, that meet the traffic mirror filter<br>rules, that did not get mirrored because of production traffic<br>taking priority.<br>Units: Bytes                                                                                                                                                                                                 |
| `NetworkPacketsSkipMirrorIn`  | The number of packets received, that meet the traffic mirror<br>filter rules, that did not get mirrored because of production<br>traffic taking priority. This metric is available for basic<br>monitoring only.<br>Units: Count                                                                                                                                        |
| `NetworkPacketsSkipMirrorOut` | The number of packets sent out, that meet the traffic mirror filter<br>rules, that did not get mirrored because of production traffic<br>taking priority. This metric is available for basic monitoring only.<br>Units: Count                                                                                                                                           |

To filter the metric data, use the following dimensions.

| Dimension              | Description                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AutoScalingGroupName` | This dimension filters the data you request for all instances in<br>a specified capacity group. An Auto Scaling group is a collection of<br>instances you define if you're using Auto Scaling. This dimension is<br>available only for Amazon EC2 metrics when the instances are in such an<br>Auto Scaling group. Available for instances with Detailed or Basic<br>Monitoring enabled.                             |
| `ImageId`              | This dimension filters the data you request for all instances running<br>this Amazon EC2 Amazon Machine Image (AMI). Available for instances with<br>Detailed Monitoring enabled.                                                                                                                                                                                                                                    |
| `InstanceId`           | This dimension filters the data you request for the identified<br>instance only. This helps you pinpoint an exact instance from which to<br>monitor data. Available for instances with Detailed or Basic Monitoring<br>enabled.                                                                                                                                                                                      |
| `InstanceType`         | This dimension filters the data you request for all instances running<br>with this specified instance type. This helps you categorize your data<br>by the type of instance running. For example, you might compare data<br>from an m1.small instance and an m1.large instance to determine which<br>has the better business value for your application. Available for<br>instances with Detailed Monitoring enabled. |

## View Traffic Mirroring CloudWatch metrics

You can view the metrics for Traffic Mirroring as follows.

###### To view metrics using the CloudWatch console

Metrics are grouped first by the service namespace, and then by the various
dimension combinations within each namespace.

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. Under **All metrics**, choose the
   **EC2** metric namespace.
4. To view the metrics, select the metric dimension.

###### To view metrics using the AWS CLI

At a command prompt, use the following command to list the metrics that are
available for Traffic Mirroring:

```
aws cloudwatch list-metrics --namespace "AWS/EC2"
```

The Traffic Mirroring metrics are included with the metrics for Amazon EC2.
