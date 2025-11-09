# Monitor Capacity Reservations usage with CloudWatch

metrics

With CloudWatch metrics, you can efficiently monitor your Capacity Reservations and identify unused capacity
by setting CloudWatch alarms to notify you when usage thresholds are met. This can help you
maintain a constant Capacity Reservation volume and achieve a higher level of utilization.

Capacity Reservations send metric data to CloudWatch every five minutes. Metrics are not supported for Capacity Reservations
that are active for less than five minutes.

For more information about viewing metrics in the CloudWatch console, see [Using Amazon CloudWatch Metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md"). For
more information about creating alarms, see [Creating Amazon CloudWatch Alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md").

###### Contents

- [Capacity Reservation usage metrics](#capacity-reservation-usage-metrics "#capacity-reservation-usage-metrics")
- [Capacity Reservation metric dimensions](#capacity-reservation-dimensions "#capacity-reservation-dimensions")
- [View CloudWatch metrics for
  Capacity Reservations](#viewing-capacity-reservation-metrics "#viewing-capacity-reservation-metrics")

## Capacity Reservation usage metrics

The `AWS/EC2CapacityReservations` namespace includes the following
usage metrics you can use to monitor and maintain on-demand capacity within
thresholds you specify for your reservation.

| Metric                   | Description                                                                                  |
| ------------------------ | -------------------------------------------------------------------------------------------- |
| `UsedInstanceCount`      | The number of instances that are currently in use.<br>Unit: Count                            |
| `AvailableInstanceCount` | The number of instances that are available.<br>Unit: Count                                   |
| `TotalInstanceCount`     | The total number of instances you have reserved.<br>Unit: Count                              |
| `InstanceUtilization`    | The percentage of reserved capacity instances that are<br>currently in use.<br>Unit: Percent |

## Capacity Reservation metric dimensions

You can use the following dimensions to refine the metrics listed in the previous
table within the selected Region and account.

| Dimension               | Description                                                                                                          |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------- |
| (No dimension)          | This dimension filters the specified metric for all Capacity<br>Reservations.                                        |
| `CapacityReservationId` | This dimension filters the specified metric for the identified<br>Capacity Reservation.                              |
| `InstanceType`          | This dimension filters the specified metric for the identified<br>instance type.                                     |
| `AvailabilityZone`      | This dimension filters the specified metric for the identified<br>Availability Zone.                                 |
| `InstanceMatchCriteria` | This dimension filters the specified metric for the identified<br>instance match criteria (`open` or<br>`targeted`). |
| `InstancePlatform`      | This dimension filters the specified metric data for the<br>identified platform.                                     |
| `Tenancy`               | This dimension filters the specified metric for the identified<br>tenancy.                                           |

## View CloudWatch metrics for

Capacity Reservations

Metrics are grouped first by the service namespace, and then by the supported
dimensions. You can use the following procedures to view the metrics for your Capacity Reservations.

###### To view Capacity Reservation metrics using the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. If necessary, change the Region. From the navigation bar, select the
   Region where your Capacity Reservation resides. For more information, see [Regions and Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").
3. In the navigation pane, choose **Metrics**.
4. For **All metrics**, choose **EC2 Capacity
   Reservations**.
5. Choose from the preceding metric dimensions **Across All Capacity
   Reservations**, **By Capacity Reservation**,
   **By Instance Type**, **By Availability
   Zone**, **By Platform**, **By Instance
   Match Criteria** or **By Tenancy** and metrics
   will be grouped by No dimension, `CapacityReservationId`,
   `InstanceType`, `AvailabilityZone`,
   `Platform`, `InstanceMatchCriteria`, and
   `Tenancy` respectively.
6. To sort the metrics, use the column heading. To graph a metric, select the
   checkbox next to the metric.

###### To view Capacity Reservation metrics using the AWS CLI

Use the following [list-metrics](../../../cli/latest/reference/cloudwatch/list-metrics.md "../../../cli/latest/reference/cloudwatch/list-metrics.md") command:

```
aws cloudwatch list-metrics --namespace "AWS/EC2CapacityReservations"
```
