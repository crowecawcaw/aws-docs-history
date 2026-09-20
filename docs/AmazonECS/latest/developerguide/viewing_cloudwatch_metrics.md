

# Viewing Amazon ECS metrics
<a name="viewing_cloudwatch_metrics"></a>

After you have resources running in your cluster, you can view the metrics on the Amazon ECS and CloudWatch consoles. The Amazon ECS console provides a 24-hour maximum, minimum, and average view of your cluster and service metrics. The CloudWatch console provides a fine-grained and customizable display of your resources, as well as the number of running tasks in a service.

## Amazon ECS console
<a name="viewing_service_metrics"></a>

Amazon ECS service CPU and memory utilization metrics are available on the Amazon ECS console. The view provided for service metrics shows the average, minimum, and maximum values for the previous 24-hour period, with data points available in 5-minute intervals. For more information, see [Amazon ECS service utilization metrics](service_utilization.md).

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. Select the cluster that you want to view metrics for.

1. Determine the metrics to view.


<table>
<thead>
  <tr><th>To view metrics from</th><th>Steps</th><th></th></tr>
</thead>
<tbody>
  <tr><td>Clusters</td><td>On the cluster details page, choose the <b>Metrics</b> tab. There is also a link provided to the CloudWatch console to view your CloudWatch Container Insights metrics if you have those turned on.</td><td></td></tr>
  <tr><td>Services</td><td>On the cluster details page, on the <b>Services</b> tab, select the service. The metrics are then available on the <b>Health and metrics</b> tab.</td><td></td></tr>
</tbody>
</table>


## CloudWatch console
<a name="viewing_metrics_console"></a>

For Fargate, Amazon ECS service metrics can also be viewed on the CloudWatch console. The console provides the most detailed view of Amazon ECS metrics, and you can tailor the views to suit your needs. You can view the service utilization and service RUNNING task count.

For EC2 capacity providers, Amazon ECS cluster and service metrics can also be viewed on the CloudWatch console. The console provides the most detailed view of Amazon ECS metrics, and you can tailor the views to suit your needs. 

For information about how to view the metrics, see [View available metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.html) the *Amazon CloudWatch User Guide*.