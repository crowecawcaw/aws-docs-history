# CloudWatch metrics for your Classic Load Balancer

ELB publishes data points to Amazon CloudWatch for your load balancers and your back-end instances.
CloudWatch enables you to retrieve statistics about those data points as an ordered set of
time-series data, known as _metrics_. Think of a metric as a variable
to monitor, and the data points as the values of that variable over time. For example, you
can monitor the total number of healthy EC2 instances for a load balancer over a specified
time period. Each data point has an associated time stamp and an optional unit of measurement.

You can use metrics to verify that your system is performing as expected. For example, you
can create a CloudWatch alarm to monitor a specified metric and initiate an action (such
as sending a notification to an email address) if the metric goes outside what you
consider an acceptable range.

ELB reports metrics to CloudWatch only when requests are flowing through the load balancer.
If there are requests flowing through the load balancer, ELB measures and sends its metrics in 60-second intervals.
If there are no requests flowing through the load balancer or no data for a metric, the metric is not reported.

For more information about Amazon CloudWatch, see the _[Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md")_.

###### Contents

- [Classic Load Balancer metrics](#loadbalancing-metrics-clb "#loadbalancing-metrics-clb")
- [Metric dimensions for Classic Load Balancers](#load-balancer-metric-dimensions-clb "#load-balancer-metric-dimensions-clb")
- [Statistics for Classic Load Balancer metrics](#measure-stats "#measure-stats")
- [View CloudWatch metrics for your load balancer](#ViewingDataUsingCloudWatch "#ViewingDataUsingCloudWatch")

## Classic Load Balancer metrics

The `AWS/ELB` namespace includes the following metrics.

| Metric                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BackendConnectionErrors`                                                                               | The number of connections that were not successfully<br>established between the load balancer and the registered instances. Because<br>the load balancer retries the connection when there are errors, this count can<br>exceed the request rate. Note that this count also includes any connection errors<br>related to health checks.<br>**Reporting criteria**: There is a nonzero value<br>**Statistics**: The most useful statistic is `Sum`.<br>Note that `Average`, `Minimum`, and `Maximum` are reported per load balancer node and are not<br>typically useful. However, the difference between the minimum and maximum (or peak to average or<br>average to trough) might be useful to determine whether a load balancer node is an outlier.<br>**Example**: Suppose that your load balancer has 2 instances in us-west-2a and 2 instances in us-west-2b,<br>and that attempts to connect to 1 instance in us-west-2a result in back-end connection errors. The sum for us-west-2a<br>includes these connection errors, while the sum for us-west-2b does not include them. Therefore, the sum for<br>the load balancer equals the sum for us-west-2a.                                                    |
| `DesyncMitigationMode_NonCompliant_Request_Count`                                                       | [HTTP listener] The number of requests that do not comply with RFC 7230.<br>**Reporting criteria**: There is a nonzero value<br>**Statistics**: The most useful statistic is `Sum`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `HealthyHostCount`                                                                                      | The number of healthy instances registered with your load balancer.<br>A newly registered instance is considered healthy after it passes the first health check.<br>If cross-zone load balancing is enabled, the number of healthy instances for the `LoadBalancerName` dimension<br>is calculated across all Availability Zones. Otherwise, it is calculated per Availability Zone.<br>**Reporting criteria**: There are registered instances<br>**Statistics**: The most useful statistics are `Average` and `Maximum`.<br>These statistics are determined by the load balancer nodes. Note that some load balancer nodes might determine that an instance is<br>unhealthy for a brief period while other nodes determine that it is healthy.<br>**Example**: Suppose that your load balancer has 2 instances in us-west-2a<br>and 2 instances in us-west-2b, us-west-2a has 1 unhealthy instance, and us-west-2b has no unhealthy instances.<br>With the `AvailabilityZone` dimension, there is an average of 1 healthy and 1 unhealthy instance in us-west-2a,<br>and an average of 2 healthy and 0 unhealthy instances in us-west-2b.                                                                          |
| `HTTPCode_Backend_2XX`,<br>`HTTPCode_Backend_3XX`,<br>`HTTPCode_Backend_4XX`,<br>`HTTPCode_Backend_5XX` | [HTTP listener] The number of HTTP response codes generated by registered instances.<br>This count does not include any response codes generated by the load balancer.<br>**Reporting criteria**: There is a nonzero value<br>**Statistics**: The most useful statistic is `Sum`.<br>Note that `Minimum`, `Maximum`, and `Average` are all 1.<br>**Example**: Suppose that your load balancer has 2 instances in us-west-2a and 2 instances in us-west-2b,<br>and that requests sent to 1 instance in us-west-2a result in HTTP 500 responses. The sum for us-west-2a includes these error responses,<br>while the sum for us-west-2b does not include them. Therefore, the sum for the load balancer equals the sum for us-west-2a.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `HTTPCode_ELB_4XX`                                                                                      | [HTTP listener] The number of HTTP 4XX client error codes generated by the load balancer.<br>Client errors are generated when a request is malformed or incomplete.<br>**Reporting criteria**: There is a nonzero value<br>**Statistics**: The most useful statistic is `Sum`.<br>Note that `Minimum`, `Maximum`, and `Average` are all 1.<br>**Example**: Suppose that your load balancer has us-west-2a and us-west-2b enabled,<br>and that client requests include a malformed request URL. As a result, client errors would likely increase<br>in all Availability Zones. The sum for the load balancer is the sum of the values for the Availability Zones.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `HTTPCode_ELB_5XX`                                                                                      | [HTTP listener] The number of HTTP 5XX server error codes generated by the load balancer.<br>This count does not include any response codes generated by the registered instances.<br>The metric is reported if there are no healthy instances registered to the load balancer,<br>or if the request rate exceeds the capacity of the instances (spillover) or the load balancer.<br>**Reporting criteria**: There is a nonzero value<br>**Statistics**: The most useful statistic is `Sum`.<br>Note that `Minimum`, `Maximum`, and `Average` are all 1.<br>**Example**: Suppose that your load balancer has us-west-2a and us-west-2b enabled, and<br>that instances in us-west-2a are experiencing high latency and are slow to respond to requests. As a result,<br>the surge queue for the load balancer nodes in us-west-2a fills and clients receive a 503 error.<br>If us-west-2b continues to respond normally, the sum for the load balancer equals the sum for us-west-2a.                                                                                                                                                                                                                                |
| `Latency`                                                                                               | [HTTP listener] The total time elapsed, in seconds, from the time the load balancer<br>sent the request to a registered instance until the instance started to send the response headers.<br>[TCP listener] The total time elapsed, in seconds, for the load balancer to successfully<br>establish a connection to a registered instance.<br>**Reporting criteria**: There is a nonzero value<br>**Statistics**: The most useful statistic is `Average`.<br>Use `Maximum` to determine whether some requests are taking substantially longer than the average.<br>Note that `Minimum` is typically not useful.<br>**Example**: Suppose that your load balancer has 2 instances in us-west-2a and 2 instances in us-west-2b,<br>and that requests sent to 1 instance in us-west-2a have a higher latency. The average for us-west-2a has a higher value than<br>the average for us-west-2b.                                                                                                                                                                                                                                                                                                                          |
| `RequestCount`                                                                                          | The number of requests completed or connections made during the specified interval (1 or 5 minutes).<br>[HTTP listener] The number of requests received and routed, including HTTP error responses from the registered instances.<br>[TCP listener] The number of connections made to the registered instances.<br>**Reporting criteria**: There is a nonzero value<br>**Statistics**: The most useful statistic is `Sum`.<br>Note that `Minimum`, `Maximum`, and `Average` all return 1.<br>**Example**: Suppose that your load balancer has 2 instances in us-west-2a<br>and 2 instances in us-west-2b, and that 100 requests are sent to the load balancer. There are 60 requests sent to us-west-2a,<br>with each instance receiving 30 requests, and 40 requests sent to us-west-2b, with each instance receiving 20 requests.<br>With the `AvailabilityZone` dimension, there is a sum of 60 requests in us-west-2a and 40 requests in us-west-2b.<br>With the `LoadBalancerName` dimension, there is a sum of 100 requests.                                                                                                                                                                                  |
| `SpilloverCount`                                                                                        | The total number of requests that were rejected because the surge queue is full.<br>[HTTP listener] The load balancer returns an HTTP 503 error code.<br>[TCP listener] The load balancer closes the connection.<br>**Reporting criteria**: There is a nonzero value<br>**Statistics**: The most useful statistic is `Sum`.<br>Note that `Average`, `Minimum`, and `Maximum` are reported per load balancer node<br>and are not typically useful.<br>**Example**: Suppose that your load balancer has us-west-2a and us-west-2b enabled, and<br>that instances in us-west-2a are experiencing high latency and are slow to respond to requests. As a result,<br>the surge queue for the load balancer node in us-west-2a fills, resulting in spillover.<br>If us-west-2b continues to respond normally, the sum for the load balancer will be the same<br>as the sum for us-west-2a.                                                                                                                                                                                                                                                                                                                                |
| `SurgeQueueLength`                                                                                      | The total number of requests (HTTP listener) or connections (TCP listener) that are pending routing to a healthy instance.<br>The maximum size of the queue is 1,024. Additional requests or connections are rejected when the queue is full.<br>For more information, see `SpilloverCount`.<br>**Reporting criteria**: There is a nonzero value.<br>**Statistics**: The most useful statistic is `Maximum`, because it represents the peak<br>of queued requests. The `Average` statistic can be useful in combination with `Minimum` and<br>`Maximum` to determine the range of queued requests. Note that `Sum` is not useful.<br>**Example**: Suppose that your load balancer has us-west-2a and us-west-2b enabled, and<br>that instances in us-west-2a are experiencing high latency and are slow to respond to requests. As a result, the<br>surge queue for the load balancer nodes in us-west-2a fills, with clients likely experiencing increased response times.<br>If this continues, the load balancer will likely have spillovers (see the `SpilloverCount` metric).<br>If us-west-2b continues to respond normally, the `max` for the load balancer will be the same as the<br>`max` for us-west-2a. |
| `UnHealthyHostCount`                                                                                    | The number of unhealthy instances registered with your load balancer.<br>An instance is considered unhealthy after it exceeds the unhealthy threshold configured for health checks.<br>An unhealthy instance is considered healthy again after it meets the healthy threshold configured for health checks.<br>**Reporting criteria**: There are registered instances<br>**Statistics**: The most useful statistics are `Average` and `Minimum`.<br>These statistics are determined by the load balancer nodes. Note that some load balancer nodes might determine that an instance is<br>unhealthy for a brief period while other nodes determine that it is healthy.<br>**Example**: See `HealthyHostCount`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

The following metrics enable you to estimate your costs if you migrate a Classic Load Balancer to an Application Load Balancer. These metrics are intended for informational
use only, not for use with CloudWatch alarms. Note that if your Classic Load Balancer has multiple listeners, these metrics are aggregated across the listeners.

These estimates are based on a load balancer with one default rule and a certificate that is 2K in size. If you use a certificate that is 4K or
greater in size, we recommend that you estimate your costs as follows: create an Application Load Balancer based on your Classic Load Balancer using the migration tool and monitor the
`ConsumedLCUs` metric for the Application Load Balancer. For more information, see [Migrate your Classic Load Balancer](../userguide/migrate-classic-load-balancer.md "../userguide/migrate-classic-load-balancer.md")
in the _Elastic Load Balancing User Guide_.

| Metric                              | Description                                                                                                                                                                                                                                                                                                     |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `EstimatedALBActiveConnectionCount` | The estimated number of concurrent TCP connections active from clients to the load balancer and from the load balancer to targets.                                                                                                                                                                              |
| `EstimatedALBConsumedLCUs`          | The estimated number of load balancer capacity units (LCU) used by an Application Load Balancer. You pay for the number of LCUs that you use per hour.<br>For more information, see [ELB Pricing](https://aws.amazon.com/elasticloadbalancing/pricing/ "https://aws.amazon.com/elasticloadbalancing/pricing/"). |
| `EstimatedALBNewConnectionCount`    | The estimated number of new TCP connections established from clients to the load balancer and from the load balancer to targets.                                                                                                                                                                                |
| `EstimatedProcessedBytes`           | The estimated number of bytes processed by an Application Load Balancer.                                                                                                                                                                                                                                        |

## Metric dimensions for Classic Load Balancers

To filter the metrics for your Classic Load Balancer, use the following dimensions.

| Dimension          | Description                                                 |
| ------------------ | ----------------------------------------------------------- |
| `AvailabilityZone` | Filters the metric data by the specified Availability Zone. |
| `LoadBalancerName` | Filters the metric data by the specified load balancer.     |

## Statistics for Classic Load Balancer metrics

CloudWatch provides statistics based on the metric data points published by ELB.
Statistics are metric data aggregations over specified period of time.
When you request statistics, the returned data stream is identified by the metric name and dimension.
A dimension is a name/value pair that uniquely identifies a metric. For example, you can
request statistics for all the healthy EC2 instances behind a load balancer launched in
a specific Availability Zone.

The `Minimum` and `Maximum` statistics reflect the minimum and maximum reported by the individual load balancer nodes.
For example, suppose there are 2 load balancer nodes. One node has `HealthyHostCount` with a `Minimum` of 2,
a `Maximum` of 10, and an `Average` of 6, while the other node has `HealthyHostCount` with a
`Minimum` of 1, a `Maximum` of 5, and an `Average` of 3. Therefore, the load balancer has a
`Minimum` of 1, a `Maximum` of 10, and an `Average` of about 4.

The `Sum` statistic is the aggregate value across all load balancer nodes.
Because metrics include multiple reports per period, `Sum` is only applicable to metrics that are aggregated
across all load balancer nodes, such as `RequestCount`, `HTTPCode_ELB_XXX`,
`HTTPCode_Backend_XXX`, `BackendConnectionErrors`, and `SpilloverCount`.

The `SampleCount` statistic is the number of samples measured. Because metrics are gathered based on sampling intervals and
events, this statistic is typically not useful. For example, with `HealthyHostCount`, `SampleCount` is based
on the number of samples that each load balancer node reports, not the number of healthy hosts.

A percentile indicates the relative standing of a value in a data set. You can specify any percentile, using up to two decimal places
(for example, p95.45). For example, the 95th percentile means that 95 percent of the data is below this value and 5 percent is above.
Percentiles are often used to isolate anomalies. For example, suppose that an application serves the majority of requests from a cache
in 1-2 ms, but in 100-200 ms if the cache is empty. The maximum reflects the slowest case, around 200 ms. The average doesn't indicate
the distribution of the data. Percentiles provide a more meaningful view of the application's performance. By using the 99th percentile as
an Amazon EC2 Auto Scaling trigger or a CloudWatch alarm, you can target that no more than 1 percent of requests take longer than 2 ms to process.

## View CloudWatch metrics for your load balancer

You can view the CloudWatch metrics for your load balancers using the Amazon EC2 console. These
metrics are displayed as monitoring graphs. The monitoring graphs show data points if the
load balancer is active and receiving requests.

Alternatively, you can view metrics for your load balancer using the CloudWatch console.

###### To view metrics using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose
   **Load Balancers**.
3. Choose the name of the load balancer to open its detail page.
4. Choose the **Monitoring** tab.
5. To get a larger view of a single metric, hover over its graph then choose the `Maximize` icon.
   The following metrics are available:
   - Healthy Hosts — `HealthyHostCount`
   - Unhealthy Hosts — `UnHealthyHostCount`
   - Average Latency — `Latency`
   - Requests — `RequestCount`
   - Backend Connection Errors — `BackendConnectionErrors`
   - Surge Queue Length — `SurgeQueueLength`
   - Spillover Count — `SpilloverCount`
   - HTTP 2XXs — `HTTPCode_Backend_2XX`
   - HTTP 3XXs — `HTTPCode_Backend_3XX`
   - HTTP 4XXs — `HTTPCode_Backend_4XX`
   - HTTP 5XXs — `HTTPCode_Backend_5XX`
   - ELB HTTP 4XXs — `HTTPCode_ELB_4XX`
   - ELB HTTP 5XXs — `HTTPCode_ELB_5XX`
   - Estimated processed bytes — `EstimatedProcessedBytes`
   - Estimated ALB consumed LCUs — `EstimatedALBConsumedLCUs`
   - Estimated ALB active connection count — `EstimatedALBActiveConnectionCount`
   - Estimated ALB new connection count — `EstimatedALBNewConnectionCount`

###### To view metrics using the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. Select the **ELB** namespace.
4. Do one of the following:
   - Select a metric dimension to view metrics by load balancer, by Availability Zone, or
     across all load balancers.
   - To view a metric across all dimensions, type its name in the search field.
   - To view the metrics for a single load balancer, type its name
     in the search field.
   - To view the metrics for a single Availability Zone, type its name
     in the search field.
