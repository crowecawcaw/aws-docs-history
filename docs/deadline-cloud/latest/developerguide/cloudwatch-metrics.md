# CloudWatch metrics

Deadline Cloud sends metrics to Amazon CloudWatch. You can use the AWS Management Console, the AWS CLI, or an API to list
the metrics that Deadline Cloud sends to CloudWatch. By default, each data point covers the 1 minute that
follows the start time of activity. For information about how to view the available metrics
using the AWS Management Console or the AWS CLI, see [View
available metrics](../../../AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.md "../../../AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.md") in the _Amazon CloudWatch User Guide_.

## Customer-managed fleet metrics

The `AWS/DeadlineCloud` namespace contains the following metrics for your
customer-managed fleets:

| Metric                 | Description                                                                                                                                                                   | Unit  |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| `RecommendedFleetSize` | The number of workers that Deadline Cloud recommends that you use to process jobs. You<br>can use this metric to expand or contract the number of workers from your<br>fleet. | Count |
| `UnhealthyWorkerCount` | The number of workers assigned to process jobs that are not healthy.                                                                                                          | Count |

You can use the following dimensions to refine the customer-managed fleet
metrics:

| Dimension | Description                                                                        |
| --------- | ---------------------------------------------------------------------------------- |
| FarmId    | This dimension filters the data that you request to the specified<br>farm.         |
| FleetId   | This dimension filters the data that you request to the specified worker<br>fleet. |

## Licensing metrics

The `AWS/DeadlineCloud` namespace contains the following metrics for
licensing:

| Metric          | Description                            | Unit  |
| --------------- | -------------------------------------- | ----- |
| `LicensesInUse` | The number of license sessions in use. | Count |

You can use the following dimensions to refine the licensing metrics:

| Dimension         | Description                                                                                                                                                   |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| FleetId           | Use this dimension to filter the data to the specified service-managed<br>fleet. For customer-managed fleets, use the LicenseEndpointId dimension<br>instead. |
| LicenseEndpointId | Use this dimension to filter the data to the specified license endpoint.                                                                                      |
| Product           | Use this dimension to filter the data to the specified metered product.                                                                                       |

## Resource limit metrics

The `AWS/DeadlineCloud` namespace contains the following metrics for
resource limits:

| Metric         | Description                                                                                                                                                          | Unit  |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| `CurrentCount` | The number of resources modeled by this limit in use.                                                                                                                | Count |
| `MaxCount`     | The maximum number of resources modeled by this limit. If you set the<br>`maxCount` value to -1 using the API, Deadline Cloud doesn't emit the<br>`MaxCount` metric. | Count |

You can use the following dimensions to refine the concurrent limit metrics:

| Dimension | Description                                                                 |
| --------- | --------------------------------------------------------------------------- |
| FarmId    | This dimension filters the data that you request to the specified<br>farm.  |
| LimitId   | This dimension filters the data that you request to the specified<br>limit. |
