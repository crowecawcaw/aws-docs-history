**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Monitor your cluster with the observability dashboard

The Amazon EKS console includes an observability dashboard that gives visibility into the performance of your cluster. The information it provides helps you to quickly detect, troubleshoot, and remediate issues. You can open the applicable section of the observability dashboard by choosing an item in the **Health and performance summary**. This summary is included in several places, including the **Observability** tab.

The observability dashboard is split into several tabs.

## Summary

The **Health and performance summary** lists the quantity of items in various categories. Each number acts as a hyperlink to a location in the observability dashboard with a list for that category.

## Cluster health

**Cluster health** provides important notifications to be aware of, some of which you may need to take action on as soon as possible. With this list, you can see descriptions and the affected resources. Cluster health includes two tables: **Health issues** and **Configuration insights**. To refresh the status of **Health issues**, choose the refresh button ( ↻ ). **Configuration insights** update automatically once every 24 hours and can’t be manually refreshed.

For more information about **Health issues**, see [Cluster health FAQs and error codes with resolution paths](troubleshooting.md#cluster-health-status "troubleshooting.md#cluster-health-status"). For more information about **Configuration insights**, see [Prepare for Kubernetes version upgrades and troubleshoot misconfigurations with cluster insights](cluster-insights.md "cluster-insights.md").

## Control plane monitoring

The **Control plane monitoring** tab is divided into three sections, each of which help you to monitor and troubleshoot your cluster’s control plane.

### Metrics

For clusters that are Kubernetes version `1.28` and above, the **Metrics** section shows graphs of several metrics gathered for various control plane components.

You can set the time period used by the X-axis of every graph by making selections at the top of the section. You can refresh data with the refresh button ( ↻ ). For each separate graph, the vertical ellipses button ( ⋮ ) opens a menu with options from CloudWatch.

These metrics and more are automatically available as basic monitoring metrics in CloudWatch under the `AWS/EKS` namespace. For more information, see [Basic monitoring and detailed monitoring](../../../AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-basic-detailed.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-basic-detailed.md") in the _Amazon CloudWatch User Guide_. To get more detailed metrics, visualization, and insights, see [Container Insights](../../../AmazonCloudWatch/latest/monitoring/ContainerInsights.md "../../../AmazonCloudWatch/latest/monitoring/ContainerInsights.md") in the _Amazon CloudWatch User Guide_. Or if you prefer Prometheus based monitoring, see [Monitor your cluster metrics with Prometheus](prometheus.md "prometheus.md").

The following table describes available metrics.

| Metric                               | Description                                                                                        |
| ------------------------------------ | -------------------------------------------------------------------------------------------------- |
| APIServer Requests                   | The requests per minute made to the API server.                                                    |
| APIServer Total Requests 4XX         | The count of API server requests per minute that had HTTP 4XX response codes (client-side errors). |
| APIServer Total Requests 5XX         | The count of API server requests per minute that had HTTP 5XX response codes (server-side errors). |
| APIServer Total Requests 429         | The count of API server requests per minute that had HTTP 429 response codes (too many requests).  |
| Storage size                         | The storage database (`etcd`) size.                                                                |
| Scheduler attempts                   | The number of attempts to schedule pods by results "unschedulable" "error", and "scheduled".       |
| Pending pods                         | The number of pending pods by queue type of "active", "backoff", "unschedulable", and "gated".     |
| API server request latency           | The latency for API server requests.                                                               |
| API server current inflight requests | The current in-flight requests for the API server.                                                 |
| Webhook requests                     | The webhook requests per minute.                                                                   |
| Webhook request rejections           | The count of webhook requests that were rejected.                                                  |
| Webhook request latency P99          | The 99th percentile latency of external, third-party webhook requests.                             |

### CloudWatch Log Insights

The **CloudWatch Log Insights** section shows various lists based on the control plane audit logs. The Amazon EKS control plane logs need to be turned on to use this feature, which you can do from the **View control plane logs in CloudWatch** section.

When enough time has passed to collect data, you can **Run all queries** or choose **Run query** for a single list at a time. An additional cost will incur from CloudWatch whenever you run queries. Choose the time period of results you want to view at the top of the section. If you want more advanced control for any query, you can choose **View in CloudWatch**. This will allow you to update a query in CloudWatch to fit your needs.

For more information, see [Analyzing log data with CloudWatch Logs Insights](../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md "../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md") in the Amazon CloudWatch Logs User Guide.

### View control plane logs in CloudWatch

Choose **Manage logging** to update the log types that are available. It takes several minutes for the logs to appear in CloudWatch Logs after you enable logging. When enough time has passed, choose any of the **View** links in this section to navigate to the applicable log.

For more information, see [Send control plane logs to CloudWatch Logs](control-plane-logs.md "control-plane-logs.md").

## Cluster insights

The **Upgrade insights** table both surfaces issues and recommends corrective actions, accelerating the validation process for upgrading to new Kubernetes versions. Amazon EKS automatically scans clusters against a list of potential Kubernetes version upgrade impacting issues. The **Upgrade insights** table lists the insight checks performed by Amazon EKS against this cluster, along with their associated statuses.

Amazon EKS maintains and periodically refreshes the list of insight checks to be performed based on evaluations of changes in the Kubernetes project as well as Amazon EKS service changes tied to new versions. The Amazon EKS console automatically refreshes the status of each insight, which can be seen in the last refresh time column.

For more information, see [Prepare for Kubernetes version upgrades and troubleshoot misconfigurations with cluster insights](cluster-insights.md "cluster-insights.md").

## Node health issues

The Amazon EKS node monitoring agent automatically reads node logs to detect health issues. Regardless of the auto repair setting, all node health issues are reported so that you can investigate as needed. If an issue type is listed without a description, you can read the description in its popover element.

When you refresh the page, any resolved issues will disappear from the list. If auto repair is enabled, you could temporarily see some health issues that will be resolved without action from you. Issues that are not supported by auto repair may require manual action from you depending on the type.

For node health issues to be reported, your cluster must use Amazon EKS Auto Mode or have the node monitoring agent add-on. For more information, see [Enable node auto repair and investigate node health issues](node-health.md "node-health.md").
