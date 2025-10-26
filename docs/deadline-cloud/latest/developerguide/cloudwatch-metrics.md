# CloudWatch metrics

Deadline Cloud sends metrics to Amazon CloudWatch. You can use the AWS Management Console, the AWS CLI, or an API to list
 the metrics that Deadline Cloud sends to CloudWatch. By default, each data point covers the 1 minute that
 follows the start time of activity. For information about how to view the available metrics
 using the AWS Management Console or the AWS CLI, see [View
 available metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.html "https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.html") in the *Amazon CloudWatch User Guide*.


## Customer-managed fleet metrics


The `AWS/DeadlineCloud` namespace contains the following metrics for your
 customer-managed fleets:




| Metric | Description | Unit |
| --- | --- | --- |
| `RecommendedFleetSize` | The number of workers that Deadline Cloud recommends that you use to process jobs. You can use this metric to expand or contract the number of workers from your fleet. | Count |
| `UnhealthyWorkerCount` | The number of workers assigned to process jobs that are not healthy. | Count | You can use the following dimensions to refine the customer-managed fleet metrics:
| Dimension | Description | | --- | --- |
| FarmId | This dimension filters the data that you request to the specified farm. | | FleetId | This dimension filters the data that you request to the specified worker fleet. | ## Resource limit metrics The `AWS/DeadlineCloud` namespace contains the following metrics for resource limits:
| Metric | Description | Unit |
| --- | --- | --- |
| `CurrentCount` | The number of resources modeled by this limit in use. | Count |
| `MaxCount` | The maximum number of resources modeled by this limit. If you set the `maxCount` value to -1 using the API, Deadline Cloud doesn't emit the `MaxCount` metric. | Count | You can use the following dimensions to refine the concurrent limit metrics:
| Dimension | Description | | --- | --- |
| FarmId | This dimension filters the data that you request to the specified farm. | | LimitId | This dimension filters the data that you request to the specified limit. |
