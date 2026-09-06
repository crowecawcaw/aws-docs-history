

# Virtual interface Rate Limiters
<a name="vif-rate-limiters"></a>

Use virtual interface (VIF) Rate Limiters to set a maximum bandwidth allocation for individual VIFs on a Direct Connect Dedicated connection. Rate Limiters help prevent network congestion caused by unexpected traffic spikes on a VIF, which can potentially consume all available bandwidth and impact workloads on other VIFs sharing the same dedicated connection. This feature is only supported on Dedicated connections. Hosted connections are always rate-limited to the purchased capacity.

## How VIF Rate Limiters work
<a name="vif-rate-limiters-how-it-works"></a>

A Dedicated connection supports multiple private, transit, and public VIFs (see [Direct Connect quotas](limits.md) for current details). By default, all VIFs on a connection can utilize 100% of the underlying connection's capacity. This means that a workload on one VIF can unexpectedly increase its utilization, causing congestion, packet loss, and potential disruption to workloads on other VIFs on that connection. This situation is commonly referred to as a "noisy neighbor" congestion event.

When you apply a Rate Limiter to a VIF, you set a maximum bandwidth that the VIF can use. If traffic on the rate-limited VIF exceeds the configured capacity, excess packets are dropped by the Direct Connect edge devices, preventing that VIF from consuming bandwidth needed by other VIFs on the same connection.

**Rate Limiters and traffic direction**  
Rate Limiters operate both on traffic leaving AWS to on-premises, and coming from on-premises into AWS. However, customer physical connections can terminate on the same device that applies the Rate Limiter policy or a different device. Direct Connect uses different device configurations to offer the service globally. The difference in devices will result in different behavior for Rate Limiters depending on the direction of your traffic.
+ **Traffic leaving AWS (Egress):** For egress traffic, VIFs are always provisioned on the same device that applies the Rate Limiter. Your applications can send traffic to on-premises in excess of a VIF's set bandwidth and the device will apply the Rate Limiter, dropping traffic down to your set bandwidth. This will protect all VIFs on the connection.
+ **Traffic coming into AWS (Ingress):** For traffic flowing from on-premises to AWS, your VIFs may be provisioned on a different upstream device than the device that terminates your physical connection. Therefore, your on-premises applications could potentially send traffic in excess of a VIF's set bandwidth, and congest the physical port before the Rate Limiters are applied. We recommend that you consider applying policers on your on-premises device to mitigate unexpected congestion events before traffic leaves your network towards AWS.

## Prerequisites and limitations
<a name="vif-rate-limiters-prerequisites"></a>
+ Rate Limiters are supported only on **Dedicated connections**. They are not supported on hosted connections.
+ You can apply Rate Limiters to VIFs of any type: private, public, and transit.
+ Each dedicated connection supports up to **10 rate limiters**. You can request a limit increase through AWS Service Quotas.
+ Hosted connections are automatically rate-limited to their purchased bandwidth. VIFs created on hosted connections cannot exceed the hosted connection's purchased speed.

## Available bandwidth options
<a name="vif-rate-limiters-bandwidth-options"></a>

The available bandwidth options depend on the speed of your underlying dedicated connection or link aggregation group (LAG). Rate Limiters are fully supported on VIFs created on link aggregation groups (LAGs). When you use a LAG, the feature is aware of the LAG's combined capacity and offers higher bandwidth options than would be available on a single connection.

For example:
+ On a 1 Gbps Dedicated connection, you can set Rate Limiters between 50 Mbps and 1 Gbps.
+ On a LAG combining 2×1 Gbps connections, you can set Rate Limiters between 50 Mbps and 2 Gbps.

## Rate Limiters and oversubscription
<a name="vif-rate-limiters-oversubscription"></a>

Rate Limiters are a static bandwidth allocation at the VIF level. They do not track actual utilization of other VIFs on the same Dedicated connection. You can allocate bandwidth to your VIFs in excess of the underlying connection's capacity (oversubscription).

VIFs without a Rate Limiter applied are considered **Unlimited** and can use up to 100% of the connection or LAG's capacity. Unlimited VIFs can congest other VIFs on the same connection, but rate-limited VIFs cannot exceed their allocated bandwidth.

You can use this behavior to establish a priority hierarchy between your VIFs. For example, you can leave a critical workload's VIF as Unlimited while applying Rate Limiters to non-critical workloads, ensuring that non-critical VIFs cannot congest the critical one.

Use the **Rate Limiters** tab in the Connection/LAG view to get a summary view of all VIFs on the connection and their bandwidth allocation. The **Rate Limiters** tab also shows the connection's current level of oversubscription. This is calculated as the allocated bandwidth across all VIFs over the underlying connection's maximum capacity. Unlimited VIFs are counted as 100% of the capacity. This allows you to quickly understand which VIFs can potentially congest others.

## Monitoring with CloudWatch
<a name="vif-rate-limiters-monitoring"></a>

When you apply a Rate Limiter to a VIF, the following metrics are published to CloudWatch. You can use these metrics to create CloudWatch alarms.

### Policed packets and bytes metrics
<a name="vif-rate-limiters-policed-metrics"></a>

These metrics report the amount of traffic dropped by the Rate Limiter when a VIF exceeds its allocated bandwidth.


| Metric | Description | 
| --- | --- | 
| VirtualInterfacePolicedPpsIngress | The number of packets per second traveling from your on-premises network to AWS that were dropped by the Rate Limiter when exceeding the allocated bandwidth. | 
| VirtualInterfacePolicedPpsEgress | The number of packets per second traveling from AWS to your on-premises network that were dropped by the Rate Limiter when exceeding the allocated bandwidth. | 
| VirtualInterfacePolicedBpsIngress | The number of bytes per second traveling from your on-premises network to AWS that were dropped by the Rate Limiter when exceeding the allocated bandwidth. | 
| VirtualInterfacePolicedBpsEgress | The number of bytes per second traveling from AWS to your on-premises network that were dropped by the Rate Limiter when exceeding the allocated bandwidth. | 

### Utilization metrics
<a name="vif-rate-limiters-utilization-metrics"></a>

These metrics report the percentage utilization of a rate-limited VIF relative to its configured bandwidth. This metric is derived automatically, and does not require you to apply CloudWatch Math.

**Note**  
When you change a VIF's allocated bandwidth, you might see a step change in the percentage utilization of the VIF, depending on the traffic going through when you make the change. For example, if you have a VIF configured to be rate-limited at 1 Gbps and that VIF had a constant 500 Mbps of egress traffic, you will see `VirtualInterfaceUtilizationEgress` at 50% utilization. If you increase that VIF's allocation to 2 Gbps, that utilization will drop to 25% as soon as the change is provisioned and the utilization metric is recalculated using the new configured capacity for that VIF.


| Metric | Description | 
| --- | --- | 
| VirtualInterfaceUtilizationIngress | Percentage utilization of the VIF based on its configured bandwidth, for traffic traveling from your on-premises network to AWS. | 
| VirtualInterfaceUtilizationEgress | Percentage utilization of the VIF based on its configured bandwidth, for traffic traveling from AWS to your on-premises network. | 

**Note**  
The utilization metric reports traffic *before* rate limiting is applied. During congestion, you may see utilization above 100% in the direction where traffic exceeds the VIF's bandwidth. At the same time, the corresponding `PolicedPps` and `PolicedBps` metrics report the amount of traffic dropped. This behavior helps you:  
Understand the total volume of traffic being received, which is useful when you are actively remediating a congestion event by shutting down traffic sources.
Determine by how much your application exceeded the bandwidth allocation, helping you decide whether to adjust the VIF's bandwidth setting.

## Configuring a Rate Limiter
<a name="vif-rate-limiters-configure"></a>

Rate Limiters can be configured on a VIF when it is created (in the Additional Settings section of the Create virtual interface view), or on an existing VIF.

**To apply or remove a Rate Limiter from an existing virtual interface (Console)**

1. Open the Direct Connect console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Connections**.

1. Select the Dedicated connection that contains the VIF you want to rate-limit.

1. Choose the **Rate Limiters** tab to view the current rate limiter allocations for the connection.

1. Select the virtual interface you want to configure.

1. Choose **Edit**.

1. For **Bandwidth**, select a bandwidth value from the available options. To remove a Rate Limiter, select **Unlimited**.

1. Choose **Edit virtual interface** to save changes.