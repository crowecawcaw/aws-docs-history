# Viewing App Runner service metrics reported to CloudWatch

Amazon CloudWatch monitors your Amazon Web Services (AWS) resources and the applications you run on AWS in
real time. You can use CloudWatch to collect and track metrics, which are variables you can measure
for your resources and applications. You can also use it to create alarms that watch metrics.
When a certain threshold is reached, CloudWatch sends notifications, or automatically makes changes to
the monitored resources. For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

AWS App Runner collects a variety of metrics that provide you with greater visibility into the
usage, performance, and availability of your App Runner services. Some metrics track individual
instances that run your web service, whereas others are at the overall service level. The
following sections list App Runner metrics and show you how to view them in the App Runner console.

## App Runner metrics

App Runner collects the following metrics relating to your service and publishes them to CloudWatch in
the `AWS/AppRunner` namespace.

###### Note

Prior to August 23, 2023, the **CPU utilization** and **Memory utilization** metrics were based on vCPU units and
megabytes of memory utilized, instead of _percent utilization_, as calculated today. If your application ran on App Runner
before this date, and you choose to go back to view metrics for this date on either the App Runner or the CloudWatch console, you'll see a display of the metrics in
both units and will also see some irregularities as a result.

###### Important

You'll need to update any CloudWatch alarms that are based on the _CPU utilization_ and _Memory utilization_ metric
values prior to August 23, 2023. Update the alarms to trigger based on percentage utilization rather than vCPU or megabytes. For more information, see
the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

Instance level metrics are collected for each instance
(scaling unit) individually.

| **What's measured?** | **Metric**          | **Description**                                                                                                                    |
| -------------------- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| CPU utilization      | `CPUUtilization`    | The percentage of average CPU usage during one-minute periods out of the total<br>CPU usage reserved by the service configuration. |
| Memory utilization   | `MemoryUtilization` | The percentage of average memory usage during one-minute periods out of the<br>total memory reserved by the service configuration. |

Service level metrics are collected for the entire
service.

| **What's measured?** | **Metric**                                                           | **Description**                                                                                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CPU utilization      | `CPUUtilization`                                                     | The percentage of aggregated CPU usage across all instances during one minute<br>periods out of the total CPU usage reserved by the service configuration.                                                                                                                   |
| Memory utilization   | `MemoryUtilization`                                                  | The percentage of aggregated memory usage across all instances during one minute<br>periods out of the total memory reserved by the service configuration.                                                                                                                   |
| Concurrency          | `Concurrency`                                                        | The approximate number of concurrent requests being handled by the<br>service.                                                                                                                                                                                               |
| HTTP request count   | `Requests`                                                           | The number of HTTP requests that the service received.                                                                                                                                                                                                                       |
| HTTP status counts   | `2xxStatusResponses`<br>`4xxStatusResponses`<br>`5xxStatusResponses` | The number of HTTP requests that returned each response status, grouped by<br>category (2XX, 4XX, 5XX).                                                                                                                                                                      |
| HTTP request latency | `RequestLatency`                                                     | The time, in milliseconds, that it took your web service to process HTTP<br>requests.                                                                                                                                                                                        |
| Instance counts      | `ActiveInstances`                                                    | The number of instances that are processing HTTP requests for your<br>service.<br>Note If the `ActiveInstances` metric displays zero, it means that there<br>are no requests for the service. It does not indicate that the number of instances<br>for your service is zero. |

## Viewing App Runner metrics in the console

The App Runner console graphically displays the metrics that App Runner collects for your service and
provides more ways to explore them.

###### Note

At this time, the console displays only service metrics. To view instance metrics, use
the CloudWatch console.

###### To view logs for your service

1. Open the [App Runner console](https://console.aws.amazon.com/apprunner "https://console.aws.amazon.com/apprunner"), and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Services**, and then choose your App Runner service.

The console displays the service dashboard with a **Service overview**.

![App Runner service dashboard page showing Activity list](images/console-dashboard.png) 3. On the service dashboard page, choose the **Metrics** tab.

The console displays a set of metrics graphs.

![The Metrics tab on the App Runner service dashboard page](images/service-dashboad-metrics.png) 4. Choose a duration (for example, **12h**) to scope metrics graphs to
the recent period of that duration. 5. Choose **Add to dashboard** at the top of one of the graph sections,
or use the menu on any graph, to add the relevant metrics to a dashboard in the CloudWatch
console for further investigation.
