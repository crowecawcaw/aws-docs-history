# Monitoring Route 53 Resolver endpoints with Amazon CloudWatch

You can use Amazon CloudWatch to monitor the number of DNS queries that are forwarded by Route 53 Resolver
endpoints. Amazon CloudWatch collects and processes raw data into readable, near real-time
metrics. These statistics are recorded for a period of two weeks, so that you can access
historical information and gain a better perspective on how your resources are
performing. By default, metric data for Resolver endpoints is automatically sent to CloudWatch
at five-minute intervals. The five-minute interval is also the smallest interval at
which the metric data can be sent.

For more information about Resolver, see [What is Amazon Route 53 Resolver?](resolver.md "resolver.md"). For more information about CloudWatch, see
[What is Amazon CloudWatch?](../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md") in the _Amazon CloudWatch User Guide_.

## Metrics and dimensions for Route 53 Resolver

When you configure Resolver to forward DNS queries to your network or vice versa, Resolver starts to send
[metrics](monitoring-resolver-with-cloudwatch.md#cloudwatch-metrics-resolver "monitoring-resolver-with-cloudwatch.md#cloudwatch-metrics-resolver")
and
[dimensions](monitoring-resolver-with-cloudwatch.md#cloudwatch-dimensions-resolver "monitoring-resolver-with-cloudwatch.md#cloudwatch-dimensions-resolver")
once every five minutes to CloudWatch about the number of queries that are forwarded. You can use the following procedures
to view the metrics in the CloudWatch console or view them by using the AWS Command Line Interface (AWS CLI).

###### To view Resolver metrics using the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. On the navigation bar, choose the Region where you created the endpoint.
3. In the navigation pane, choose **Metrics**.
4. On the **All metrics** tab, choose **Route 53 Resolver**.
5. Choose **By Endpoint** to view query counts for a specified endpoint. Then choose the endpoints
   that you want to view the number of queries for.

Choose **Across All Endpoints** to view query counts for all inbound endpoints or for all outbound endpoints
that were created by the current AWS account. Then choose **InboundQueryVolume** or **OutboundQueryVolume**
to view the desired counts.

###### To view metrics using the AWS CLI

- At a command prompt, use the following command:

```
`aws cloudwatch list-metrics --namespace "AWS/Route53Resolver"`
```

###### Topics

- [CloudWatch metrics for Route 53 Resolver](#cloudwatch-metrics-resolver "#cloudwatch-metrics-resolver")
- [Dimensions for Route 53 Resolver metrics](#cloudwatch-dimensions-resolver "#cloudwatch-dimensions-resolver")

### CloudWatch metrics for Route 53 Resolver

`AWS/Route53Resolver` namespace includes metrics for Route 53 Resolver endpoints and for IP addresses.

###### Topics

- [Metrics for Resolver endpoints](#cloudwatch-metrics-resolver-endpoint "#cloudwatch-metrics-resolver-endpoint")
- [Metrics for Resolver IP addresses](#cloudwatch-metrics-resolver-ip-address "#cloudwatch-metrics-resolver-ip-address")

#### Metrics for Resolver endpoints

The `AWS/Route53Resolver` namespace includes the following metrics for Route 53 Resolver endpoints.

**EndpointHealthyENICount**
The number of elastic network interfaces in the `OPERATIONAL` status. This means
that the Amazon VPC network interfaces for the endpoint (specified by
`EndpointId`) are correctly configured and able
to pass inbound or outbound DNS queries between your network and
Resolver.

Valid statistics: Minimum, Maximum, Average

Units: Count

**EndpointUnhealthyENICount**
The number of elastic network interfaces in the `AUTO_RECOVERING` status.

This means that the resolver is trying to recover one or more of the Amazon VPC network
interfaces that are associated with the endpoint (specified by
`EndpointId`). During the recovery process, the
endpoint functions with limited capacity and is unable to process DNS queries until it's fully recovered.

Valid statistics: Minimum, Maximum, Average

Units: Count

**InboundQueryVolume**

For inbound endpoints, the number of DNS queries forwarded from your network to your VPCs through the endpoint
specified by `EndpointId`.

Valid statistics: Sum

Units: Count

**OutboundQueryVolume**

For outbound endpoints, the number of DNS queries forwarded from your VPCs to your network through the endpoint
specified by `EndpointId`.

Valid statistics: Sum

Units: Count

**OutboundQueryAggregateVolume**
For outbound endpoints, the total number of DNS queries forwarded from Amazon VPCs to your network,
including the following:

- The number of DNS queries forwarded from your VPCs to your network through the endpoint
  that is specified by `EndpointId`.
- When the current account shares Resolver rules with other accounts, queries from VPCs that are created
  by other accounts that are forwarded to your network through the endpoint that is specified by `EndpointId`.

Valid statistics: Sum

Units: Count

**ResolverEndpointCapacityStatus**

The capacity status of the Resolver endpoint. The metric indicates the current capacity
utilization state where: 0 = OK (Normal operating capacity), 1 =
Warning (At least one elastic network interface exceeds 50%
capacity utilization), and 2 = Critical (At least one elastic
network interface exceeds 75% capacity utilization).

The capacity status is determined by multiple factors
including query volume, query latency, DNS protocols, DNS packet
size, and connection tracking status.

Valid statistics: Maximum

Units: None

###### Note

In some cases, you might observe gaps in this metric. These gaps can
occur when your network interfaces undergo consecutive scheduled
maintenance or updates. After we return a network interface to service,
it takes at least 1 minute for our service to collect operational data
and publish this metric. These gaps do not indicate that your Resolver
endpoint is experiencing an outage. If you're configuring a CloudWatch Alarm
for this metric, we recommend the following:

- Set the alarm to "Treat missing data as ignore".

Or

- Configure an evaluation period of more than five minutes for the alarm
  threshold.
  These settings will help reduce false alarms during normal maintenance
  activities.

###### Best practices for Resolver endpoint capacity management

To address capacity issues, we generally recommend increasing the number of elastic
network interfaces for your Resolver endpoint. However, there are
important considerations for specific endpoint types:

For **inbound endpoints** the traffic load balancing is
customer-dependent. Therefore capacity warnings or critical alerts may
indicate a "hot spot" where a subset of elastic network interfaces is
disproportionately utilized.

- To identify potential load balancing issues, examine the [InboundQueryVolume](#cloudwatch-metrics-resolver-ip-address "#cloudwatch-metrics-resolver-ip-address") metrics for each elastic network
  interface individually.

For **outbound endpoints** the traffic is automatically
balanced across elastic network interfaces. Capacity issues may be due to
problems with the target name server, or because high-latency queries of
timeouts overwhelm the Resolver network interfaces.

- In these cases, simply increasing the elastic network interfaces might not be effective, and
  we recommend fixing the target name server.

#### Metrics for Resolver IP addresses

The `AWS/Route53Resolver` namespace includes the following metrics for each IP address that's associated
with a Resolver inbound or outbound endpoint. (When you specify an endpoint, Resolver creates an
Amazon VPC [elastic network interface](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md").)

**InboundQueryVolume**

For each IP address for your inbound endpoints, the number of DNS queries forwarded from your network
to the specified IP address. Each IP address is identified by the IP address ID. You can get this value
using the Route 53 console. On the page for the applicable endpoint, in the IP addresses section, see the
**IP address ID** column. You can also get the value programmatically using
[ListResolverEndpointIpAddresses](../APIReference/API_route53resolver_ListResolverEndpointIpAddresses.md "../APIReference/API_route53resolver_ListResolverEndpointIpAddresses.md").

Valid statistics: Sum

Units: Count

**OutboundQueryAggregateVolume**

For each IP address for your outbound endpoints, the total number of DNS queries forwarded from
Amazon VPCs to your network, including the following:

- The number of DNS queries forwarded from your VPCs to your network using the
  specified IP address.
- When the current account shares Resolver rules with other accounts, queries from VPCs
  that are created by other accounts that are forwarded to your network through using the
  specified IP address.

Each IP address is identified by the IP address ID. You can get this value using the Route 53 console.
On the page for the applicable endpoint, in the IP addresses section, see the **IP address ID** column.
You can also get the value programmatically using
[ListResolverEndpointIpAddresses](../APIReference/API_route53resolver_ListResolverEndpointIpAddresses.md "../APIReference/API_route53resolver_ListResolverEndpointIpAddresses.md").

Valid statistics: Sum

Units: Count

### Dimensions for Route 53 Resolver metrics

Route 53 Resolver metrics for inbound and outbound endpoints use the `AWS/Route53Resolver` namespace and provide metrics for
`EndpointId`. If you specify a value for the `EndpointId` dimension, CloudWatch returns the number of DNS queries
for the specified endpoint. If you don't specify `EndpointId`, CloudWatch returns the number of DNS queries for all
endpoints that were created by the current AWS account.

The `RniId` dimension is supported for
`OutboundQueryAggregateVolume` and
`InboundQueryVolume` metrics.
