# Monitoring your graphs

Amazon Neptune and Amazon CloudWatch are integrated so that you can gather and analyze performance metrics. You can
monitor these metrics using the CloudWatch console, the AWS Command Line Interface (AWS CLI), or the CloudWatch API.

CloudWatch also lets you set alarms so that you can be notified if a metric value breaches a threshold that you specify.
You can even set up CloudWatch events to take corrective action if a breach occurs. For more information about using CloudWatch
and alarms, see the [CloudWatch documentation](../../../cloudwatch.md "../../../cloudwatch.md").

## Viewing CloudWatch data

AWS console

To view CloudWatch data for a Neptune Analytics graph from the AWS console:

1. Sign in to the [AWS management console](https://console.aws.amazon.com//cloudwatch/ "https://console.aws.amazon.com//cloudwatch/")
   and open the CloudWatch console.
2. In the navigation pane, choose **Metrics**.
3. In the **All Metrics** pane, choose Neptune , and then choose Neptune Analytics.
4. In the upper pane, scroll down to view the full list of metrics for your graph. The available
   Neptune Analytics metric options appear in the **Viewing** list.

To select or deselect an individual metric, in the results pane, select the check box next to the
resource name and metric. Graphs showing the metrics for the selected items appear at the bottom
of the console. To learn more about CloudWatch graphs, see
[Graph metrics](../../../AmazonCloudWatch/latest/DeveloperGuide/graph_metrics.md "../../../AmazonCloudWatch/latest/DeveloperGuide/graph_metrics.md") in the Amazon CloudWatch user guide.

AWS CLI

To view CloudWatch data for a Neptune cluster using the AWS CLI:

1. Install the AWS CLI. For information on installing the CLI, see
   the [AWS
   Command Line Interface](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md") user guide.
2. Use the AWS CLI to fetch information. The relevant CloudWatch parameters for Neptune are listed in
   [Neptune CloudWatch metrics](../../../neptune/latest/userguide/cw-metrics.md "../../../neptune/latest/userguide/cw-metrics.md").

The following example retrieves the `GraphSizeBytes` CloudWatch metric for the example graph
`g-d3iivkv6i6`.

```
aws cloudwatch get-metric-statistics \                                                                                                            ──(Mon,Aug19)─┘
    --namespace AWS/Neptune   --metric-name GraphSizeBytes \
    --dimensions Name="GraphIdentifier",Value=g-d3iivkv6i6 \
    --start-time 2024-08-17T00:00:00Z --end-time 2024-08-18T00:00:00Z \
    --period 60 --statistics=Average --region=us-east-1
```

API

CloudWatch also supports a query action so that you can request information programmatically. For more
information, see the
[CloudWatch Query API](../../../AmazonCloudWatch/latest/DeveloperGuide/Using_Query_API.md "../../../AmazonCloudWatch/latest/DeveloperGuide/Using_Query_API.md") documentation and
[Amazon CloudWatch API Reference](../../../AmazonCloudWatch/latest/APIReference.md "../../../AmazonCloudWatch/latest/APIReference.md").
When a CloudWatch action requires a parameter that is specific to Neptune monitoring, such as `MetricName`,
use the values listed in
[Neptune CloudWatch Metrics](../../../neptune/latest/userguide/cw-metrics.md "../../../neptune/latest/userguide/cw-metrics.md").
The following example shows a low-level CloudWatch request, using the following parameters:

1. Statistics.member.1 = Average
2. Dimensions.member.1 = "GraphIdentifier"=g-d3iivkv6i6
3. Namespace = AWS/Neptune
4. StartTime = 2024-08-17T00:00:00Z
5. EndTime = 2024-08-17T00:00:00Z
6. Period = 60
7. MetricName = GraphSizeBytes

```
aws cloudwatch get-metric-statistics \                                                                                                            ──(Mon,Aug19)─┘
    --namespace AWS/Neptune   --metric-name GraphSizeBytes \
    --dimensions Name="GraphIdentifier",Value=g-d3iivkv6i6 \
    --start-time 2024-08-17T00:00:00Z --end-time 2024-08-18T00:00:00Z \
    --period 60 --statistics=Average --region=us-east-1
```

## Neptune CloudWatch metrics

The following table lists the CloudWatch metrics that Neptune Analytics supports:

| Name                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NumOpenCypherRequestsPerSec     | Number of Open Cypher requests/sec made to the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| NumOpenCypherClientErrorsPerSec | Number of Open Cypher requests/sec resulting into client side failures(4xx).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| NumOpenCypherServerErrorsPerSec | Number of OpenCypher requests/sec resulting into internal failures(5xx).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| NumQueuedRequestsPerSec         | Number of requests/sec accepted by the server and pending execution. A non zero metric<br>value indicates the graph is running queries at full capacity and a scale up is needed<br>to avoid a throughput drop.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| NumThrottledRequestsPerSec      | Number of requests/sec throttled by the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| GraphSizeBytes                  | Aggregated storage volume used for graph indexes, dictionary and vector index(es).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| CPUUtilization                  | System CPU usage by percentage. A continuous period of high(close to 100) CPU Utilization<br>metric is not alone indicative of an issue, but validates a potential need to scale up if<br>other metrics are also exhibiting stress.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| NumEdges                        | Number of edges in the graph.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| NumEdgeProperties               | Number of properties across all edges in the graph.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| NumVertexProperties             | Number of properties across all vertices in the graph. Note that Neptune Analytics models LPG<br>labels as vertex properties, so this includes the LPG labels.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| NumVectors                      | Number of vectors present in the Vector Search Index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| GraphStorageUsagePercent        | Percentage storage quota usage of the graph at the current configured m-NCU. This<br>metric can be used to resize your graph as you add or remove data. If this metric<br>reaches close to 100 and the graph expects addition of more data, the queries will<br>run out of memory. It is recommended to scale up your graph in such cases. More<br>information on optimally resizing your graph is available in<br>[this blog entry](https://aws.amazon.com/blogs/database/introducing-smaller-capacity-units-for-amazon-neptune-analytics-up-to-75-cheaper-to-get-started-with-graph-analytics-workloads/ "https://aws.amazon.com/blogs/database/introducing-smaller-capacity-units-for-amazon-neptune-analytics-up-to-75-cheaper-to-get-started-with-graph-analytics-workloads/") . |
