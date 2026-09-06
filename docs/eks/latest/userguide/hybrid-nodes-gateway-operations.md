

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Amazon EKS Hybrid Nodes gateway operations
<a name="hybrid-nodes-gateway-operations"></a>

This page covers day-2 operations for the Amazon EKS Hybrid Nodes gateway, including high availability, failover behavior, monitoring, scaling, and VXLAN tunnel lifecycle. For installation instructions, see [Get started with EKS Hybrid Nodes gateway](hybrid-nodes-gateway-getting-started.md).

## High availability and failover
<a name="hybrid-nodes-gateway-ha"></a>

The Hybrid Nodes gateway uses an active-standby model with Kubernetes Lease-based leader election. Two gateway pods run on separate EC2 nodes, enforced by pod anti-affinity. Both pods create a VXLAN interface at startup and run a node reconciler that maintains VTEP entries for all hybrid nodes. Only the leader pod manages VPC route tables and the `CiliumVTEPConfig` CRD. The standby pod is always ready to forward traffic within 3–5 seconds on failover because it already has a complete set of tunnel entries.

### Failover sequence
<a name="hybrid-nodes-gateway-failover-sequence"></a>

When the active gateway instance fails, the following sequence occurs:

1. The standby pod detects that the leader lease has expired.

1. The standby pod acquires the lease and becomes the new leader.

1. The new leader runs the leader setup sequence:
   + Updates VPC route table entries to point hybrid pod CIDRs to the new leader’s primary ENI.
   + Upserts the `CiliumVTEPConfig` custom resource with the new leader’s node IP and VXLAN MAC address.

1. Traffic resumes flowing through the new leader.

Because both pods maintain VXLAN interfaces and VTEP entries at all times, the new leader does not need to recreate the VXLAN interface or reprogram tunnel entries during failover. Only the VPC route table and `CiliumVTEPConfig` updates are required.

Expected failover time is approximately 3–5 seconds. During failover, traffic between the VPC and hybrid pods is interrupted.

### Availability Zone recommendation
<a name="hybrid-nodes-gateway-az-recommendation"></a>

Spread gateway nodes across two Availability Zones so that an AZ failure does not take out both the leader and standby. When using EKS Auto Mode, configure your `NodeClass` with subnet selectors across multiple AZs. For managed node groups or self-managed nodes, choose nodes in different AZs when labeling them.

**Note**  
Cross-AZ traffic between the gateway and other resources in the VPC incurs standard AWS cross-AZ data transfer charges.

### Leader election parameters
<a name="hybrid-nodes-gateway-leader-params"></a>

The default leader election parameters are tuned for fast failover:


| Parameter | Default | Description | 
| --- | --- | --- | 
|  `--leader-election-lease-duration`  |  `3s`  | How long a non-leader waits before attempting to acquire the lease after the leader stops renewing. | 
|  `--leader-election-renew-deadline`  |  `2s`  | How long the leader tries to renew the lease before giving up. | 
|  `--leader-election-retry-period`  |  `1s`  | How often candidates retry acquiring the lease. | 

Lowering these values reduces failover time but increases the risk of false failovers under network partitions. For most deployments, the defaults are appropriate. For more information, see [Amazon EKS Hybrid Nodes gateway configuration reference](hybrid-nodes-gateway-configuration.md).

## VPC route table management
<a name="hybrid-nodes-gateway-route-table-mgmt"></a>

The gateway manages VPC route table entries so that traffic destined for hybrid pod CIDRs reaches the active gateway instance.

### How routes are managed
<a name="hybrid-nodes-gateway-route-how"></a>

When a gateway pod becomes the leader, it creates or replaces routes in each configured VPC route table. Each route sets the destination CIDR to a hybrid pod CIDR and the target to the leader’s primary ENI. If a route already exists and points to the correct ENI, the gateway skips the update.

During failover, the new leader replaces the existing routes so they point to its own ENI. This is the mechanism that redirects VPC traffic to the new active gateway.

### Route table entry example
<a name="hybrid-nodes-gateway-route-example"></a>

After the gateway configures routes, your VPC route table contains entries similar to the following:


| Destination | Target | Status | 
| --- | --- | --- | 
|  `10.0.0.0/16`  | local | active | 
|  {{HYBRID\_POD\_CIDR}}  |  {{eni-LEADER\_ENI\_ID}}  | active | 

### IAM permissions
<a name="hybrid-nodes-gateway-route-iam"></a>

The gateway requires the following IAM actions to manage route tables:
+  `ec2:DescribeRouteTables` 
+  `ec2:CreateRoute` 
+  `ec2:ReplaceRoute` 
+  `ec2:DescribeInstances` 

Attach these permissions to the IAM role associated with the gateway nodes' instance profile, pod identity, or IRSA configuration.

## Monitoring
<a name="hybrid-nodes-gateway-monitoring"></a>

### Health and readiness endpoints
<a name="hybrid-nodes-gateway-health-endpoints"></a>

The gateway exposes health and readiness endpoints on port `8088`:


| Endpoint | Path | Description | 
| --- | --- | --- | 
| Health check |  `/healthz`  | Returns HTTP 200 when the gateway process is healthy. Used by the Kubernetes liveness probe. | 
| Readiness check |  `/readyz`  | Returns HTTP 200 when the gateway is ready to serve traffic. Used by the Kubernetes readiness probe. | 

You can query these endpoints manually for diagnostics by running a temporary debug container or by port-forwarding:

```
kubectl port-forward -n eks-hybrid-nodes-gateway {{POD_NAME}} 8088:8088 &
curl -s http://localhost:8088/healthz
curl -s http://localhost:8088/readyz
```

### Metrics endpoint
<a name="hybrid-nodes-gateway-metrics"></a>

The gateway exposes Prometheus-compatible metrics on port `10080` at the `/metrics` path. The following custom metrics are available in addition to the standard controller-runtime metrics.

 **Gateway info:** 


| Metric | Type | Description | 
| --- | --- | --- | 
|  `hybrid_gateway_info`  | Gauge | Static information about the gateway instance. Always 1. Labels: `node_ip`, `node_name`, `vxlan_interface`, `vpc_cidr`, `pod_cidr`. | 

 **Hybrid nodes:** 


| Metric | Type | Description | 
| --- | --- | --- | 
|  `hybrid_gateway_hybrid_nodes_configured`  | Gauge | Current number of hybrid nodes with VTEP entries configured. | 

 **VTEP operations:** 


| Metric | Type | Description | 
| --- | --- | --- | 
|  `hybrid_gateway_vtep_add_total`  | Counter | Total successful VTEP add operations. | 
|  `hybrid_gateway_vtep_add_errors_total`  | Counter | Total failed VTEP add operations. | 
|  `hybrid_gateway_vtep_remove_total`  | Counter | Total successful VTEP remove operations. | 
|  `hybrid_gateway_vtep_remove_errors_total`  | Counter | Total failed VTEP remove operations. | 

 **Leader election and route tables:** 


| Metric | Type | Description | 
| --- | --- | --- | 
|  `hybrid_gateway_leader_is_active`  | Gauge | 1 if this pod is the active leader, 0 if standby. | 
|  `hybrid_gateway_leader_setup_duration_seconds`  | Histogram | Duration of leader setup operations (route tables \+ CiliumVTEPConfig) in seconds. | 
|  `hybrid_gateway_aws_route_table_update_total`  | Counter | Total successful AWS route table update operations. | 
|  `hybrid_gateway_aws_route_table_update_errors_total`  | Counter | Total failed AWS route table update operations. | 
|  `hybrid_gateway_aws_route_table_update_duration_seconds`  | Histogram | Duration of AWS route table update operations in seconds. | 

 **Network statistics (collected on-demand per scrape):** 


| Metric | Type | Description | 
| --- | --- | --- | 
|  `hybrid_gateway_vxlan_rx_bytes_total`  | Gauge | Total bytes received on the VXLAN interface. | 
|  `hybrid_gateway_vxlan_tx_bytes_total`  | Gauge | Total bytes transmitted on the VXLAN interface. | 
|  `hybrid_gateway_vxlan_rx_packets_total`  | Gauge | Total packets received on the VXLAN interface. | 
|  `hybrid_gateway_vxlan_tx_packets_total`  | Gauge | Total packets transmitted on the VXLAN interface. | 
|  `hybrid_gateway_vxlan_rx_dropped_total`  | Gauge | Total packets dropped on receive by the VXLAN interface. | 
|  `hybrid_gateway_vxlan_tx_dropped_total`  | Gauge | Total packets dropped on transmit by the VXLAN interface. | 
|  `hybrid_gateway_vxlan_rx_errors_total`  | Gauge | Total receive errors on the VXLAN interface. | 
|  `hybrid_gateway_vxlan_tx_errors_total`  | Gauge | Total transmit errors on the VXLAN interface. | 
|  `hybrid_gateway_vxlan_interface_up`  | Gauge | 1 if the VXLAN interface is UP, 0 otherwise. | 
|  `hybrid_gateway_vxlan_fdb_entries`  | Gauge | Current number of FDB entries on the VXLAN interface. | 
|  `hybrid_gateway_vxlan_route_count`  | Gauge | Current number of routes via the VXLAN interface. | 
|  `hybrid_gateway_primary_nic_rx_bytes_total`  | Gauge | Total bytes received on the primary network interface. | 
|  `hybrid_gateway_primary_nic_tx_bytes_total`  | Gauge | Total bytes transmitted on the primary network interface. | 
|  `hybrid_gateway_primary_nic_rx_packets_total`  | Gauge | Total packets received on the primary network interface. | 
|  `hybrid_gateway_primary_nic_tx_packets_total`  | Gauge | Total packets transmitted on the primary network interface. | 
|  `hybrid_gateway_primary_nic_rx_dropped_total`  | Gauge | Total packets dropped on receive by the primary NIC. | 
|  `hybrid_gateway_primary_nic_tx_dropped_total`  | Gauge | Total packets dropped on transmit by the primary NIC. | 
|  `hybrid_gateway_primary_nic_rx_errors_total`  | Gauge | Total receive errors on the primary NIC. | 
|  `hybrid_gateway_primary_nic_tx_errors_total`  | Gauge | Total transmit errors on the primary NIC. | 
|  `hybrid_gateway_primary_nic_info`  | Gauge | Primary NIC name. Always 1. Labels: `interface_name`. | 

### CloudWatch Observability add-on
<a name="hybrid-nodes-gateway-cloudwatch"></a>

You can use the [Amazon CloudWatch Observability add-on](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-setup-EKS-addon.html) to collect gateway metrics and logs. Configure the add-on to scrape the gateway namespace (`eks-hybrid-nodes-gateway`) on port `10080`. For the correct configuration format, see the add-on documentation linked above.

## Scaling considerations
<a name="hybrid-nodes-gateway-scaling"></a>

The Hybrid Nodes gateway uses an active-standby model with leader election, so only one pod handles traffic at any given time. Horizontally scaling the gateway (by increasing the number of replicas) can improve availability by providing additional standby pods that are ready to take over during failover, but it does not improve performance or throughput because traffic is not distributed across replicas. To scale performance, scale vertically by choosing an EC2 instance type with sufficient network bandwidth for your traffic volume.

### Instance type guidance
<a name="hybrid-nodes-gateway-instance-guidance"></a>

Gateway throughput is limited by the EC2 instance network performance. Consider the following when selecting an instance type:
+  **Network bandwidth** — The gateway forwards all traffic between the VPC and hybrid pods. Choose an instance type whose network bandwidth meets your peak traffic requirements.
+  **Packets per second (PPS)** — VXLAN encapsulation adds overhead per packet. Workloads with many small packets (for example, microservices with high request rates) benefit from instance types with higher PPS limits.
+  **Number of hybrid nodes** — Each hybrid node adds a VXLAN tunnel endpoint that the gateway forwards traffic through. As the number of hybrid nodes scales, the aggregate traffic through the gateway grows. Select an instance type with sufficient network bandwidth to handle the peak cross-network traffic for your cluster.

### Recommended instance types
<a name="hybrid-nodes-gateway-instance-recommendations"></a>

 **Production (10–100 hybrid nodes, moderate traffic)** 

Suitable for standard production workloads with steady cross-network traffic.


| Instance type | vCPUs | Memory | Network | Notes | 
| --- | --- | --- | --- | --- | 
|  `c6i.xlarge`  | 4 | 8 GiB | Up to 12.5 Gbps | Good balance of cost and performance | 
|  `c6in.xlarge`  | 4 | 8 GiB | Up to 30 Gbps | Network-optimized; recommended for production | 
|  `c7i.xlarge`  | 4 | 8 GiB | Up to 12.5 Gbps | Latest generation compute-optimized | 
|  `m6i.xlarge`  | 4 | 16 GiB | Up to 12.5 Gbps | Suitable if co-locating other workloads on gateway nodes | 

 **High-throughput production (100\+ hybrid nodes, heavy traffic)** 

For environments with significant cross-network bandwidth requirements, such as data-intensive workloads or many concurrent connections.


| Instance type | vCPUs | Memory | Network | Notes | 
| --- | --- | --- | --- | --- | 
|  `c6in.2xlarge`  | 8 | 16 GiB | Up to 40 Gbps | Recommended for high-throughput production | 
|  `c5n.2xlarge`  | 8 | 21 GiB | Up to 25 Gbps | Previous-generation network-optimized, cost-effective | 
|  `c6in.4xlarge`  | 16 | 32 GiB | Up to 50 Gbps | Maximum throughput for very heavy workloads | 
|  `c5n.4xlarge`  | 16 | 42 GiB | Up to 25 Gbps | High vCPU count for extreme packet rates | 

Monitor network utilization using the gateway metrics (see [Metrics endpoint](#hybrid-nodes-gateway-metrics)) and adjust the instance type as needed.

## VXLAN tunnel lifecycle
<a name="hybrid-nodes-gateway-vxlan-lifecycle"></a>

The gateway automatically maintains VXLAN tunnels to hybrid nodes as they join or leave the cluster.

### How tunnels are managed
<a name="hybrid-nodes-gateway-tunnel-mgmt"></a>

A node controller watches `CiliumNode` objects in the cluster. The controller runs on every gateway pod (not just the leader) so that both the leader and standby have up-to-date tunnel state. When a `CiliumNode` event occurs, the controller checks whether the node is a hybrid node by looking for the `eks.amazonaws.com/compute-type: hybrid` label.

 **When a hybrid node joins the cluster:** 

1. The controller detects the new `CiliumNode` object.

1. It extracts the node’s internal IP address and pod CIDR from the `CiliumNode` spec.

1. It programs the following on the VXLAN interface:
   + A route for the node’s pod CIDR via the node’s IP through the VXLAN interface.
   + A static ARP entry mapping the node’s IP to a deterministic MAC address.
   + An FDB entry telling the VXLAN module to send encapsulated packets to the node’s IP.

 **When a hybrid node leaves the cluster:** 

1. The controller detects the `CiliumNode` deletion.

1. It removes the route, ARP entry, and FDB entry for that node from the VXLAN interface.

This lifecycle is fully automatic. You do not need to manually configure tunnels when adding or removing hybrid nodes.

## Next steps
<a name="hybrid-nodes-gateway-operations-next"></a>
+  [Amazon EKS Hybrid Nodes gateway configuration reference](hybrid-nodes-gateway-configuration.md) — Customize Helm values, CLI flags, and leader election parameters.
+  [Amazon EKS Hybrid Nodes gateway troubleshooting](hybrid-nodes-gateway-troubleshooting.md) — Diagnose and resolve common issues.
+  [Amazon EKS Hybrid Nodes gateway](hybrid-nodes-gateway-overview.md) — Return to the overview page.