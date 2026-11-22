

# CloudWatch metrics for Amazon VPC Lattice

Amazon VPC Lattice sends data related to your target groups, services, and VPC resources to Amazon CloudWatch, and processes it into readable, near real-time metrics. These metrics are kept for 15 months, so that you can access historical information and gain a better perspective on how your web application or service is performing. You can also set alarms that watch for certain thresholds and send notifications or take actions when those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).

Amazon VPC Lattice uses a service-linked role in your AWS account to send metrics to Amazon CloudWatch. For more information, see [Using service-linked roles for Amazon VPC Lattice](using-service-linked-roles.md).

**Topics**
+ [View Amazon CloudWatch metrics](#monitoring-cloudwatch-view)
+ [Target group metrics](#monitoring-cloudwatch-tg)
+ [Service metrics](#monitoring-cloudwatch-service)
+ [Resource gateway and resource configuration metrics](#resource-gateway-resource-configuration-metrics)
+ [Resource consumer metrics](#resource-consumer-metrics)

## View Amazon CloudWatch metrics
<a name="monitoring-cloudwatch-view"></a>

You can view the Amazon CloudWatch metrics for your target groups, services, resource gateways, resource configurations, and resource consumers using the CloudWatch console or AWS CLI.

**To view metrics using the CloudWatch console**

1. Open the Amazon CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Metrics**.

1. Select the `AWS/VpcLattice` namespace.

1. (Optional) To view a metric across all dimensions, enter its name in the search field.

1. (Optional) To filter by dimension, select one of the following:
   + To display only the metrics reported for your target groups, choose **Target groups**. To view the metrics for a single target group, enter its name in the search field.
   + To display only the metrics reported for your services, choose **Services**. To view the metrics for a single service, enter its name in the search field.
   + To display only the metrics reported for your resource gateways, choose **Resource Gateway Id**. To view the metrics for a single resource gateway, enter its ID in the search field.
   + To display only the metrics reported for your resource configurations, choose **Resource Configuration Id**. To view the metrics for a single resource configuration, enter its ID in the search field.
   + To display only the metrics reported for your resource endpoints, service-network endpoints, or service network VPC associations, choose **VPC Endpoint Id** or **Service Network VPC Association Id**.

**To view metrics using the AWS CLI**

Use the following [CloudWatch list-metrics](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/list-metrics.html) AWS CLI command to list the available metrics:

`aws cloudwatch list-metrics --namespace AWS/VpcLattice`

For information about each of the metrics and their dimensions, see [Target group metrics](#monitoring-cloudwatch-tg), [Service metrics](#monitoring-cloudwatch-service), [Resource gateway and resource configuration metrics](#resource-gateway-resource-configuration-metrics), and [Resource consumer metrics](#resource-consumer-metrics).

## Target group metrics
<a name="monitoring-cloudwatch-tg"></a>

VPC Lattice automatically stores metrics related to target groups in the `AWS/VpcLattice` [Amazon CloudWatch namespace](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace). For more information about target groups, see [Target groups in VPC Lattice](target-groups.md).

**Dimensions**

To filter the metrics for target groups, use the following dimensions:
+ `AvailabilityZone`
+ `TargetGroup`


| Metric | Description | TargetGroup Protocol | 
| --- | --- | --- | 
|  TotalConnectionCount  | This metric reports the total number of connections.<br />This metric has the following reporting criteria:+  VPC Lattice reports this metric from the time the resource receives traffic, whether the value is zero or non-zero. <br />This metric has the following reporting frequency:+  VPC Lattice reports this metric once a minute. <br />The following statistics are available for this metric:+  The most useful statistic is `Sum`.  |  HTTP, HTTPS, TCP  | 
|  ActiveConnectionCount  | This metric reports the number of active connections.<br />This metric has the following reporting criteria:+  VPC Lattice reports this metric from the time the resource receives traffic, whether the value is zero or non-zero. <br />This metric has the following reporting frequency:+  VPC Lattice reports this metric once a minute. <br />The following statistics are available for this metric:+  The most useful statistic is `Sum`.  |  HTTP, HTTPS, TCP  | 
|  ConnectionErrorCount  | This metric reports the total number of connection failures.<br />This metric has the following reporting criteria:+  VPC Lattice reports this metric from the time the resource receives traffic, whether the value is zero or non-zero. <br />This metric has the following reporting frequency:+  VPC Lattice reports this metric once a minute. <br />The following statistics are available for this metric:+  The most useful statistic is `Sum`.  |  HTTP, HTTPS, TCP  | 
|  HTTP1\_ConnectionCount  | This metric reports the total number of HTTP/1.1 connections.<br />This metric has the following reporting criteria:+  VPC Lattice reports this metric from the time the resource receives traffic, whether the value is zero or non-zero. <br />This metric has the following reporting frequency:+  VPC Lattice reports this metric once a minute. <br />The following statistics are available for this metric:+  The most useful statistic is `Sum`.  |  HTTP, HTTPS  | 
|  HTTP2\_ConnectionCount  | This metric reports the total number of HTTP/2 connections.<br />This metric has the following reporting criteria:+  VPC Lattice reports this metric from the time the resource receives traffic, whether the value is zero or non-zero. <br />This metric has the following reporting frequency:+  VPC Lattice reports this metric once a minute. <br />The following statistics are available for this metric:+  The most useful statistic is `Sum`.  |  HTTP, HTTPS  | 
|  ConnectionTimeoutCount  | This metric reports the total number of connection connect timeouts.<br />This metric has the following reporting criteria:+  VPC Lattice reports this metric from the time the resource receives traffic, whether the value is zero or non-zero. <br />This metric has the following reporting frequency:+  VPC Lattice reports this metric once a minute. <br />The following statistics are available for this metric:+  The most useful statistic is `Sum`.  |  HTTP, HTTPS, TCP  | 
|  TotalReceivedConnectionBytes  | This metric reports the total number of received connection bytes.<br />This metric has the following reporting criteria:+  VPC Lattice reports this metric from the time the resource receives traffic, whether the value is zero or non-zero. <br />This metric has the following reporting frequency:+  VPC Lattice reports this metric once a minute. <br />The following statistics are available for this metric:+  The most useful statistic is `Sum`.  |  HTTP, HTTPS, TCP  | 
|  TotalSentConnectionBytes  | This metric reports the total number of sent connection bytes.<br />This metric has the following reporting criteria:+  VPC Lattice reports this metric from the time the resource receives traffic, whether the value is zero or non-zero. <br />This metric has the following reporting frequency:+  VPC Lattice reports this metric once a minute. <br />The following statistics are available for this metric:+  The most useful statistic is `Sum`.  |  HTTP, HTTPS, TCP  | 
|  TotalRequestCount  | This metric reports the total number of requests.<br />This metric has the following reporting criteria:+  VPC Lattice reports this metric from the time the resource receives traffic, whether the value is zero or non-zero. <br />This metric has the following reporting frequency:+  VPC Lattice reports this metric once a minute. <br />The following statistics are available for this metric:+  The most useful statistic is `Sum`.  |  HTTP, HTTPS  | 
|  ActiveRequestCount  | This metric reports the total number of active requests.<br />This metric has the following reporting criteria:+  VPC Lattice reports this metric from the time the resource receives traffic, whether the value is zero or non-zero. <br />This metric has the following reporting frequency:+  VPC Lattice reports this metric once a minute. <br />The following statistics are available for this metric:+  The most useful statistic is `Sum`.  |  HTTP, HTTPS  | 
|  RequestTime  | This metric reports the request time to the last byte, in milliseconds.<br />This metric has the following reporting criteria:+  VPC Lattice reports this metric from the time the resource receives traffic, whether the value is zero or non-zero. <br />This metric has the following reporting frequency:+  VPC Lattice reports this metric once a minute. <br />The following statistics are available for this metric:+  The most useful statistics are `Average` and `pNN.NN` (percentiles).  |  HTTP, HTTPS  | 
|  HTTPCode\_2XX\_Count, HTTPCode\_3XX\_Count, HTTPCode\_4XX\_Count, HTTPCode\_5XX\_Count  | This metric reports aggregate HTTP response codes.<br />This metric has the following reporting criteria:+  VPC Lattice reports this metric from the time the resource receives traffic, whether the value is zero or non-zero. <br />This metric has the following reporting frequency:+  VPC Lattice reports this metric once a minute. <br />The following statistics are available for this metric:+  The most useful statistic is `Sum`.  |  HTTP, HTTPS  | 
|  TLSConnectionErrorCount  | This metric reports the total number of TLS connection errors, not including failed certificate verifications.<br />This metric has the following reporting criteria:+  VPC Lattice reports this metric from the time the resource receives traffic, whether the value is zero or non-zero. <br />This metric has the following reporting frequency:+  VPC Lattice reports this metric once a minute. <br />The following statistics are available for this metric:+  The most useful statistic is `Sum`.  |  HTTP, HTTPS, TCP  | 
|  TotalTLSConnectionHandshakeCount  | This metric reports the total number of successful TLS connection handshakes.<br />This metric has the following reporting criteria:+  VPC Lattice reports this metric from the time the resource receives traffic, whether the value is zero or non-zero. <br />This metric has the following reporting frequency:+  VPC Lattice reports this metric once a minute. <br />The following statistics are available for this metric:+  The most useful statistic is `Sum`.  |  HTTP, HTTPS, TCP  | 

## Service metrics
<a name="monitoring-cloudwatch-service"></a>

VPC Lattice automatically stores metrics related to services in the `AWS/VpcLattice` [Amazon CloudWatch namespace](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace). For more information about services, see [Services in VPC Lattice](services.md).

**Dimensions**

To filter the metrics for services, use the following dimensions:
+ `AvailabilityZone`
+ `Service`


| Metric | Description | 
| --- | --- | 
|  RequestTimeoutCount  | This metric reports the total number of requests that timed out waiting for a response.<br />This metric has the following reporting criteria:+  VPC Lattice reports this metric from the time the resource receives traffic, whether the value is zero or non-zero. <br />This metric has the following reporting frequency:+  VPC Lattice reports this metric once a minute. <br />The following statistics are available for this metric:+  The most useful statistic is `Sum`.  | 
|  TotalRequestCount  | This metric reports the total number of requests.<br />This metric has the following reporting criteria:+  VPC Lattice reports this metric from the time the resource receives traffic, whether the value is zero or non-zero. <br />This metric has the following reporting frequency:+  VPC Lattice reports this metric once a minute. <br />The following statistics are available for this metric:+  The most useful statistic is `Sum`.  | 
|  RequestTime  | This metric reports the request time, in milliseconds.<br />This metric has the following reporting criteria:+  VPC Lattice reports this metric from the time the resource receives traffic, whether the value is zero or non-zero. <br />This metric has the following reporting frequency:+  VPC Lattice reports this metric once a minute. <br />The following statistics are available for this metric:+  The most useful statistics are `Average` and `pNN.NN` (percentiles).  | 
|  HTTPCode\_2XX\_Count, HTTPCode\_3XX\_Count, HTTPCode\_4XX\_Count, HTTPCode\_5XX\_Count  | This metric reports aggregate HTTP response codes.<br />This metric has the following reporting criteria:+  VPC Lattice reports this metric from the time the resource receives traffic, whether the value is zero or non-zero. <br />This metric has the following reporting frequency:+  VPC Lattice reports this metric once a minute. <br />The following statistics are available for this metric:+  The most useful statistic is `Sum`.  | 
|  HTTPCode\_VpcLattice\_400\_Count, HTTPCode\_VpcLattice\_403\_Count, HTTPCode\_VpcLattice\_404\_Count, HTTPCode\_VpcLattice\_429\_Count, HTTPCode\_VpcLattice\_500\_Count, HTTPCode\_VpcLattice\_502\_Count, HTTPCode\_VpcLattice\_504\_Count  | This metric reports granular HTTP response codes.<br />This metric has the following reporting criteria:+  VPC Lattice reports this metric from the time the resource receives traffic, whether the value is zero or non-zero. <br />This metric has the following reporting frequency:+  VPC Lattice reports this metric once a minute. <br />The following statistics are available for this metric:+  The most useful statistic is `Sum`.  | 

## Resource gateway and resource configuration metrics
<a name="resource-gateway-resource-configuration-metrics"></a>

VPC Lattice automatically publishes metrics for your resource gateways and resource configurations to the `AWS/VpcLattice` Amazon CloudWatch namespace. These metrics are published only to the account that owns the resource gateway. If the resource gateway is in a shared VPC subnet, the participant account that owns the resource gateway receives these metrics, not the VPC owner. Service network owners don't receive these metrics. Metrics are published for all resource configuration types: single, group, child, ARN, and CIDR. For more information, see [Resource gateways](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-gateway.html) and [Resource configurations](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-configuration.html).

**Dimensions**


| Dimension | Description | 
| --- | --- | 
| Resource Gateway Id | Filters the metric data by resource gateway. | 
| Resource Configuration Id | Filters the metric data by resource configuration. For a group resource configuration, the group's metrics are the sum of the metrics of its child resource configurations. Each child resource configuration also has its own metrics, under its own resource configuration ID. | 
| Service Network Resource Association Id | Filters the metric data by the association between the resource configuration and a service network. Includes traffic from clients that access the resource through a service network VPC association or a service-network VPC endpoint. | 
| VPC Endpoint Association Id | Filters the metric data by the association between the resource configuration and a VPC endpoint. Includes traffic from clients that access the resource through a resource VPC endpoint or a service-network VPC endpoint. | 
| AvailabilityZone | Filters the metric data by Availability Zone. | 

The metrics are available only for the following dimension sets. You can't combine dimensions from different sets. For example, you can't filter by both `Service Network Resource Association Id` and `Resource Gateway Id`.


| Dimension set | Use it to | 
| --- | --- | 
| `Resource Gateway Id`<br />`Resource Gateway Id, AvailabilityZone` | View all traffic through a resource gateway, overall or per Availability Zone. | 
| `Resource Configuration Id`<br />`Resource Configuration Id, AvailabilityZone` | View all traffic to a resource configuration, overall or per Availability Zone. | 
| `Service Network Resource Association Id`<br />`Service Network Resource Association Id, AvailabilityZone` | View traffic to a resource configuration from clients that connect through a service network. | 
| `VPC Endpoint Association Id`<br />`VPC Endpoint Association Id, AvailabilityZone` | View traffic to a resource configuration from clients that connect through a VPC endpoint. | 

**Metrics**


| Metric | Description | Unit | 
| --- | --- | --- | 
| BytesProcessed | The number of bytes processed through the resource gateway to and from your resources, aggregated in both directions.<br />Reporting criteria: VPC Lattice reports this metric only for one-minute periods in which there is traffic.<br />Reporting frequency: once a minute.<br />Statistics: The most useful statistic is `Sum`. | Bytes | 
| PacketsDropped | The number of packets dropped by the resource gateway. Increasing values could indicate that the resource is unhealthy or unreachable from the resource gateway.<br />Reporting criteria: VPC Lattice reports this metric only for one-minute periods in which there is traffic.<br />Reporting frequency: once a minute.<br />Statistics: The most useful statistic is `Sum`. | Count | 
| NewFlows | The number of new flows (connections) established to your resources through the resource gateway during the one-minute period.<br />Reporting criteria: VPC Lattice reports this metric only for one-minute periods in which there is traffic.<br />Reporting frequency: once a minute.<br />Statistics: The most useful statistic is `Sum`. | Count | 
| ActiveFlows | The number of flows currently established to your resources through the resource gateway, including idle flows that are still tracked.<br />Reporting criteria: VPC Lattice reports this metric only for one-minute periods in which there is traffic.<br />Reporting frequency: once a minute.<br />Statistics: The most useful statistics are `Average` and `Maximum`. | Count | 
| PortAllocationErrors | The number of connections that the resource gateway could not establish because it could not allocate a source port. Increasing values usually mean that the resource gateway needs more IPv4 addresses per ENI or more Availability Zones. You can't change either on an existing resource gateway, so create a resource gateway with the settings you need and re-create your resource configurations on it.<br />Reporting criteria: VPC Lattice reports this metric only for one-minute periods in which there is traffic.<br />Reporting frequency: once a minute.<br />Statistics: The most useful statistic is `Sum`. | Count | 

## Resource consumer metrics
<a name="resource-consumer-metrics"></a>

VPC Lattice automatically publishes metrics for clients that access VPC resources to the `AWS/VpcLattice` Amazon CloudWatch namespace. These metrics are published only to the account that owns the resource VPC endpoint, service-network VPC endpoint, or service network VPC association. Service network owners don't receive these metrics. Metrics are published for all resource configuration types. For more information, see [Access a resource through a resource VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/use-resource-endpoint.html) and [Manage the associations for a VPC Lattice service network](service-network-associations.md).

**Dimensions**


| Dimension | Description | 
| --- | --- | 
| VPC Endpoint Id | Filters the metric data by resource VPC endpoint or service-network VPC endpoint. | 
| Service Network VPC Association Id | Filters the metric data by service network VPC association. | 
| AvailabilityZone | Filters the metric data by Availability Zone. | 

The metrics are available only for the following dimension sets. You can't combine dimensions from different sets.


| How the client accesses the resource | Dimension sets | 
| --- | --- | 
| Resource VPC endpoint or service-network VPC endpoint | `VPC Endpoint Id`<br />`VPC Endpoint Id, AvailabilityZone` | 
| Service network VPC association | `Service Network VPC Association Id`<br />`Service Network VPC Association Id, AvailabilityZone` | 

**Metrics**


| Metric | Description | Unit | 
| --- | --- | --- | 
| BytesProcessed | The number of bytes processed between clients and the resource, aggregated in both directions.<br />Reporting criteria: VPC Lattice reports this metric only for one-minute periods in which there is traffic.<br />Reporting frequency: once a minute.<br />Statistics: The most useful statistic is `Sum`. | Bytes | 
| PacketsDropped | The number of packets dropped on the path to the resource. Increasing values could indicate a connectivity issue between the client and the resource.<br />Reporting criteria: VPC Lattice reports this metric only for one-minute periods in which there is traffic.<br />Reporting frequency: once a minute.<br />Statistics: The most useful statistic is `Sum`. | Count | 
| NewFlows | The number of new flows (connections) established with the resource during the one-minute period.<br />Reporting criteria: VPC Lattice reports this metric only for one-minute periods in which there is traffic.<br />Reporting frequency: once a minute.<br />Statistics: The most useful statistic is `Sum`. | Count | 
| ActiveFlows | The number of flows currently established with the resource, including idle flows that are still tracked.<br />Reporting criteria: VPC Lattice reports this metric only for one-minute periods in which there is traffic.<br />Reporting frequency: once a minute.<br />Statistics: The most useful statistics are `Average` and `Maximum`. | Count | 