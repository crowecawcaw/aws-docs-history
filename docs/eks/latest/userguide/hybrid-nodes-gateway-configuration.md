

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Amazon EKS Hybrid Nodes gateway configuration reference
<a name="hybrid-nodes-gateway-configuration"></a>

This page documents all configurable parameters for the Amazon EKS Hybrid Nodes gateway. For installation instructions, see [Get started with EKS Hybrid Nodes gateway](hybrid-nodes-gateway-getting-started.md). For an overview of the gateway, see [Amazon EKS Hybrid Nodes gateway](hybrid-nodes-gateway-overview.md).

## Helm chart values
<a name="hybrid-nodes-gateway-helm-values"></a>

The following table lists all values in the `eks-hybrid-nodes-gateway` Helm chart. You can set these values using `--set` flags or a custom `values.yaml` file during `helm install` or `helm upgrade`.


| Value | Type | Default | Required | Description | 
| --- | --- | --- | --- | --- | 
|  `image.repository`  | string |  `public.ecr.aws/eks/eks-hybrid-nodes-gateway`  | No | Container image repository for the gateway image. Defaults to the public Amazon ECR registry. | 
|  `image.tag`  | string | Chart `appVersion`  | No | Image tag. Defaults to the `appVersion` defined in `Chart.yaml`. | 
|  `image.pullPolicy`  | string |  `IfNotPresent`  | No | Image pull policy. Valid values: `Always`, `IfNotPresent`, `Never`. | 
|  `replicas`  | integer |  `2`  | No | Number of gateway pod replicas. Two replicas is the recommended configuration for high availability in production environments. | 
|  `nodeLabel`  | string |  `hybrid-gateway-node`  | No | Node label key used to select gateway nodes. Nodes must have this label set to `"true"`. | 
|  `vpcCIDR`  | string |  `""`  | Yes | VPC CIDR block used for Cilium VTEP configuration. Example: `10.0.0.0/16`. | 
|  `podCIDRs`  | string |  `""`  | Yes | Comma-separated list of pod CIDRs used by Cilium on hybrid nodes. Example: `10.85.0.0/16,10.86.0.0/16`. | 
|  `routeTableIDs`  | string |  `""`  | Yes | Comma-separated list of VPC route table IDs to program with hybrid pod routes. Example: `rtb-0123456789abcdef0,rtb-0123456789abcdef1`. | 
|  `autoMode.enabled`  | boolean |  `true`  | No | Enable EKS Auto Mode integration. When `true`, the chart adds an `eks.amazonaws.com/compute-type: auto` node selector and uses a zero-downtime rolling update strategy. Set to `false` for managed node groups or self-managed nodes. | 

### Example install commands
<a name="hybrid-nodes-gateway-install-examples"></a>

 **EKS Auto Mode** (default):

```
helm install eks-hybrid-nodes-gateway oci://public.ecr.aws/eks/eks-hybrid-nodes-gateway \
  --version 1.0.0 \
  --namespace eks-hybrid-nodes-gateway \
  --create-namespace \
  --set vpcCIDR={{VPC_CIDR}} \
  --set podCIDRs={{POD_CIDRS}} \
  --set routeTableIDs={{ROUTE_TABLE_IDS}}
```

 **Managed node groups or self-managed nodes**:

```
helm install eks-hybrid-nodes-gateway oci://public.ecr.aws/eks/eks-hybrid-nodes-gateway \
  --version 1.0.0 \
  --namespace eks-hybrid-nodes-gateway \
  --create-namespace \
  --set autoMode.enabled=false \
  --set vpcCIDR={{VPC_CIDR}} \
  --set podCIDRs={{POD_CIDRS}} \
  --set routeTableIDs={{ROUTE_TABLE_IDS}}
```

## Auto Mode vs. managed node group configuration
<a name="hybrid-nodes-gateway-auto-vs-mng"></a>

The `autoMode.enabled` Helm value controls two behaviors in the Deployment template:


| Behavior |  `autoMode.enabled=true` (default) |  `autoMode.enabled=false`  | 
| --- | --- | --- | 
|  **Node selector**  | Adds `eks.amazonaws.com/compute-type: auto` in addition to the gateway node label. | Uses only the gateway node label (`hybrid-gateway-node: "true"`). | 
|  **Rolling update strategy**  |  `maxSurge: 1`, `maxUnavailable: 0` — ensures zero downtime during upgrades by starting a new pod before terminating the old one. |  `maxSurge: 0`, `maxUnavailable: 1` — terminates the old pod before starting a new one, because node capacity is pre-provisioned. | 

When using EKS Auto Mode, you must create a `NodePool` and `NodeClass` before installing the Helm chart. The NodePool provisions EC2 instances with the correct labels, taints, and source/destination check configuration. For the required YAML, see [Get started with EKS Hybrid Nodes gateway](hybrid-nodes-gateway-getting-started.md). When using managed node groups or self-managed nodes, you must provision and label the nodes yourself before installing the chart.

For all deployment targets, the Deployment uses `hostNetwork: true` and requires the `NET_ADMIN` capability. Pod anti-affinity ensures that the two gateway pods run on separate nodes.

## Leader election tuning
<a name="hybrid-nodes-gateway-leader-tuning"></a>

The gateway uses Kubernetes Lease-based leader election to maintain an active-standby model. The default parameters are tuned for fast failover:


| Parameter | Default | Description | 
| --- | --- | --- | 
|  `--leader-election-lease-duration`  |  `3s`  | How long a non-leader waits after the last observed lease renewal before trying to acquire the lease. Lower values detect leader failure faster but increase the risk of false failovers during transient network issues. | 
|  `--leader-election-renew-deadline`  |  `2s`  | Maximum time the active leader spends trying to renew the lease before giving up leadership. Must be less than the lease duration. | 
|  `--leader-election-retry-period`  |  `1s`  | How frequently candidates retry acquiring or renewing the lease. | 

With the default values, the expected failover time when the active gateway fails is approximately 3–5 seconds. This includes the time for the standby to detect the lease expiration, acquire the lease, and run the leader setup sequence (VPC route table updates and Cilium VTEP configuration).

### When to adjust leader election parameters
<a name="hybrid-nodes-gateway-leader-tuning-guidance"></a>
+  **Increase lease duration** if you observe frequent leader transitions caused by transient network latency between gateway pods and the Kubernetes API server.
+  **Decrease lease duration** if you need faster failover detection and your network between gateway nodes and the API server is reliable and low-latency.
+  **Increase retry period** to reduce API server load from leader election in large clusters.

**Note**  
The `--leader-election-renew-deadline` must always be less than `--leader-election-lease-duration`. If the renew deadline exceeds the lease duration, the leader may lose the lease before it can renew.

## Related topics
<a name="hybrid-nodes-gateway-configuration-related"></a>
+  [Amazon EKS Hybrid Nodes gateway](hybrid-nodes-gateway-overview.md) 
+  [Get started with EKS Hybrid Nodes gateway](hybrid-nodes-gateway-getting-started.md) 
+  [Amazon EKS Hybrid Nodes gateway operations](hybrid-nodes-gateway-operations.md) 
+  [Amazon EKS Hybrid Nodes gateway troubleshooting](hybrid-nodes-gateway-troubleshooting.md) 