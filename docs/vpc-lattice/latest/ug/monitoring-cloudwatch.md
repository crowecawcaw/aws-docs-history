# CloudWatch metrics for Amazon VPC Lattice

Amazon VPC Lattice sends data related to your target groups and services to Amazon CloudWatch, and
processes it into readable, near real-time metrics. These metrics are kept for 15 months, so
that you can access historical information and gain a better perspective on how your web
application or service is performing. You can also set alarms that watch for certain
thresholds and send notifications or take actions when those thresholds are met. For more
information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md").

Amazon VPC Lattice uses a service-linked role in your AWS account to send metrics to
Amazon CloudWatch. For more information, see [Using service-linked roles for Amazon VPC Lattice](using-service-linked-roles.md "using-service-linked-roles.md").

###### Contents

- [View Amazon CloudWatch metrics](#monitoring-cloudwatch-view "#monitoring-cloudwatch-view")
- [Target group metrics](#monitoring-cloudwatch-tg "#monitoring-cloudwatch-tg")
- [Service metrics](#monitoring-cloudwatch-service "#monitoring-cloudwatch-service")

## View Amazon CloudWatch metrics

You can view the Amazon CloudWatch metrics for your target groups and services using the CloudWatch console or AWS CLI.

###### To view metrics using the CloudWatch console

1. Open the Amazon CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. Select the `AWS/VpcLattice` namespace.
4. (Optional) To view a metric across all dimensions, enter its name in the search field.
5. (Optional) To filter by dimension, select one of the following:
   - To display only the metrics reported for your target groups, choose **Target groups**. To view the metrics for a single target group, enter its name in the search field.
   - To display only the metrics reported for your services, choose **Services**. To view the metrics for a single service, enter its name in the search field.

**To view metrics using the AWS CLI**

Use the following [CloudWatch list-metrics](../../../cli/latest/reference/cloudwatch/list-metrics.md "../../../cli/latest/reference/cloudwatch/list-metrics.md") AWS CLI command to list the available metrics:

`aws cloudwatch list-metrics --namespace AWS/VpcLattice`

For information about each of the metrics and their dimensions, see [Target group metrics](#monitoring-cloudwatch-tg "#monitoring-cloudwatch-tg") and
[Service metrics](#monitoring-cloudwatch-service "#monitoring-cloudwatch-service").

## Target group metrics

VPC Lattice automatically stores metrics related to target groups in the `AWS/VpcLattice`
[Amazon CloudWatch namespace](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Namespace "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Namespace"). For more information about target groups, see
[Target groups in VPC Lattice](target-groups.md "target-groups.md").

###### Dimensions

To filter the metrics for target groups, use the following dimensions:

- `AvailabilityZone`
- `TargetGroup`

| Metric                                                                              | Description                                                                                                                                                                                                                                                                                                             | TargetGroup Protocol |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| `TotalConnectionCount`                                                              | Total connections.<br>Reporting criteria<br>• Always reported (whether it's a zero or non-zero value)<br>from the time the resource receives traffic.<br>Reporting frequency<br>• Once a minute.<br>Statistics<br>• The most useful statistic is `Sum`.                                                                 | `HTTP, HTTPS, TCP`   |
| `ActiveConnectionCount`                                                             | Active connections.<br>Reporting criteria<br>• Always reported (whether it's a zero or non-zero value)<br>from the time the resource receives traffic.<br>Reporting frequency<br>• Once a minute.<br>Statistics<br>• The most useful statistic is `Sum`.                                                                | `HTTP, HTTPS, TCP`   |
| `ConnectionErrorCount`                                                              | Total connection failures.<br>Reporting criteria<br>• Always reported (whether it's a zero or non-zero value)<br>from the time the resource receives traffic.<br>Reporting frequency<br>• Once a minute.<br>Statistics<br>• The most useful statistic is `Sum`.                                                         | `HTTP, HTTPS, TCP`   |
| `HTTP1_ConnectionCount`                                                             | Total HTTP/1.1 connections.<br>Reporting criteria<br>• Always reported (whether it's a zero or non-zero value)<br>from the time the resource receives traffic.<br>Reporting frequency<br>• Once a minute.<br>Statistics<br>• The most useful statistic is `Sum`.                                                        | `HTTP, HTTPS`        |
| `HTTP2_ConnectionCount`                                                             | Total HTTP/2 connections.<br>Reporting criteria<br>• Always reported (whether it's a zero or non-zero value)<br>from the time the resource receives traffic.<br>Reporting frequency<br>• Once a minute.<br>Statistics<br>• The most useful statistic is `Sum`.                                                          | `HTTP, HTTPS`        |
| `ConnectionTimeoutCount`                                                            | Total connection connect timeouts.<br>Reporting criteria<br>• Always reported (whether it's a zero or non-zero value)<br>from the time the resource receives traffic.<br>Reporting frequency<br>• Once a minute.<br>Statistics<br>• The most useful statistic is `Sum`.                                                 | `HTTP, HTTPS, TCP`   |
| `TotalReceivedConnectionBytes`                                                      | Total received connection bytes.<br>Reporting criteria<br>• Always reported (whether it's a zero or non-zero value)<br>from the time the resource receives traffic.<br>Reporting frequency<br>• Once a minute.<br>Statistics<br>• The most useful statistic is `Sum`.                                                   | `HTTP, HTTPS, TCP`   |
| `TotalSentConnectionBytes`                                                          | Total sent connection bytes.<br>Reporting criteria<br>• Always reported (whether it's a zero or non-zero value)<br>from the time the resource receives traffic.<br>Reporting frequency<br>• Once a minute.<br>Statistics<br>• The most useful statistic is `Sum`.                                                       | `HTTP, HTTPS, TCP`   |
| `TotalRequestCount`                                                                 | Total requests.<br>Reporting criteria<br>• Always reported (whether it's a zero or non-zero value)<br>from the time the resource receives traffic.<br>Reporting frequency<br>• Once a minute.<br>Statistics<br>• The most useful statistic is `Sum`.                                                                    | `HTTP, HTTPS`        |
| `ActiveRequestCount`                                                                | Total active requests.<br>Reporting criteria<br>• Always reported (whether it's a zero or non-zero value)<br>from the time the resource receives traffic.<br>Reporting frequency<br>• Once a minute.<br>Statistics<br>• The most useful statistic is `Sum`.                                                             | `HTTP, HTTPS`        |
| `RequestTime`                                                                       | Request time to the last byte in milliseconds.<br>Reporting criteria<br>• Always reported (whether it's a zero or non-zero value)<br>from the time the resource receives traffic.<br>Reporting frequency<br>• Once a minute.<br>Statistics<br>• The most useful statistics are `Average` and<br>`pNN.NN` (percentiles). | `HTTP, HTTPS`        |
| `HTTPCode_2XX_Count, HTTPCode_3XX_Count, HTTPCode_4XX_Count,<br>HTTPCode_5XX_Count` | Aggregate HTTP response codes.<br>Reporting criteria<br>• Always reported (whether it's a zero or non-zero value)<br>from the time the resource receives traffic.<br>Reporting frequency<br>• Once a minute.<br>Statistics<br>• The most useful statistic is `Sum`.                                                     | `HTTP, HTTPS`        |
| `TLSConnectionErrorCount`                                                           | Total TLS connection errors not including failed certificate<br>verifications.<br>Reporting criteria<br>• Always reported (whether it's a zero or non-zero value)<br>from the time the resource receives traffic.<br>Reporting frequency<br>• Once a minute.<br>Statistics<br>• The most useful statistic is `Sum`.     | `HTTP, HTTPS, TCP`   |
| `TotalTLSConnectionHandshakeCount`                                                  | Total successful TLS connection handshakes.<br>Reporting criteria<br>• Always reported (whether it's a zero or non-zero value)<br>from the time the resource receives traffic.<br>Reporting frequency<br>• Once a minute.<br>Statistics<br>• The most useful statistic is `Sum`.                                        | `HTTP, HTTPS, TCP`   |

## Service metrics

VPC Lattice automatically stores metrics related to services in the `AWS/VpcLattice`
[Amazon CloudWatch namespace](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Namespace "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Namespace"). For more information about services, see
[Services in VPC Lattice](services.md "services.md").

###### Dimensions

To filter the metrics for target groups, use the following dimensions:

- `AvailabilityZone`
- `Service`

| Metric                                                                                          | Description                                                                                                                                                                                                                                                                                      |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `RequestTimeoutCount`                                                                           | Total requests that timed out waiting for a response.<br>Reporting criteria<br>• Always reported (whether it's a zero or nonzero value) from the time the resource receives traffic.<br>Reporting frequency<br>• Once a minute.<br>Statistics<br>• The most useful statistic is `Sum`.           |
| `TotalRequestCount`                                                                             | Total requests.<br>Reporting criteria<br>• Always reported (whether it's a zero or non-zero value) from the time the resource receives traffic.<br>Reporting frequency<br>• Once a minute.<br>Statistics<br>• The most useful statistic is `Sum`.                                                |
| `RequestTime`                                                                                   | Request time in milliseconds.<br>Reporting criteria<br>• Always reported (whether it's a zero or non-zero value) from the time the resource receives traffic.<br>Reporting frequency<br>• Once a minute.<br>Statistics<br>• The most useful statistics are `Average` and `pNN.NN` (percentiles). |
| `HTTPCode_2XX_Count`,<br>`HTTPCode_3XX_Count`,<br>`HTTPCode_4XX_Count`,<br>`HTTPCode_5XX_Count` | Aggregate HTTP response codes.<br>Reporting criteria<br>• Always reported (whether it's a zero or non-zero value) from the time the resource receives traffic.<br>Reporting frequency<br>• Once a minute.<br>Statistics<br>• The most useful statistic is `Sum`.                                 |
