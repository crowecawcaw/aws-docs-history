

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Amazon EKS Hybrid Nodes gateway
<a name="hybrid-nodes-gateway-overview"></a>

The Amazon EKS Hybrid Nodes gateway automates networking between your Amazon EKS cluster VPC and Kubernetes pods running on [EKS Hybrid Nodes](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-overview.html). The gateway eliminates the need to make on-premises pod networks routable from the VPC or coordinate network infrastructure changes. It creates VXLAN tunnels between EC2-based gateway nodes in your VPC and Cilium-managed hybrid nodes in your on-premises environment, and it automatically maintains VPC route table entries so that traffic reaches the correct gateway instance.

## Use cases
<a name="hybrid-nodes-gateway-use-cases"></a>

The Hybrid Nodes gateway enables the following traffic flows between your VPC and on-premises environment:
+  **Control plane to webhook communication** — The Kubernetes API server can reach webhook endpoints running on hybrid nodes. Without the gateway, webhooks on hybrid nodes are unreachable from the control plane unless the pod CIDRs are made routable in the on-premises environment.
+  **Pod-to-pod traffic across cloud and on-premises** — Pods running on EC2 nodes in the VPC can communicate directly with pods running on hybrid nodes, and vice versa.
+  ** AWS service connectivity to hybrid pods** — AWS services such as Application Load Balancers, Network Load Balancers, and Amazon Managed Service for Prometheus can reach pods running on hybrid nodes.

## Architecture
<a name="hybrid-nodes-gateway-architecture"></a>

Two gateway pods run as a Deployment on labeled EC2 nodes. A Kubernetes Lease-based leader election determines which pod is active. Both pods create a VXLAN interface at startup and run a node reconciler that watches `CiliumNode` objects, so the standby is always ready to forward traffic within 3–5 seconds on failover. Only leader-specific actions (VPC route table updates and `CiliumVTEPConfig` management) transfer when leadership changes.

## How it works
<a name="hybrid-nodes-gateway-how-it-works"></a>

The Hybrid Nodes gateway uses four mechanisms to enable connectivity:

 **VXLAN tunneling** — The gateway creates a VXLAN interface (`hybrid_vxlan0`) with VNI 2 on UDP port 8472 (the Cilium default). It establishes a tunnel to each hybrid node by programming FDB entries, ARP entries, and routes on the VXLAN interface. A node controller watches `CiliumNode` objects and automatically adds or removes tunnels as hybrid nodes join or leave the cluster.

 **VPC route table management** — When the gateway becomes the leader, it creates or replaces routes in the specified VPC route tables. Each route points a hybrid pod CIDR to the leader’s primary ENI, so VPC traffic destined for hybrid pods is forwarded to the active gateway instance.

 **Cilium VTEP integration** — The gateway creates a `CiliumVTEPConfig` custom resource that tells Cilium agents on hybrid nodes where to send VPC-bound traffic. The config contains the leader’s node IP as the tunnel endpoint and the VXLAN interface MAC address. When hybrid pods send traffic to VPC addresses, Cilium encapsulates it in a VXLAN packet and sends it to the gateway.

 **Leader election** — The gateway uses Kubernetes Lease-based leader election with an active-standby model. Two gateway pods run on separate nodes enforced by pod anti-affinity. Both pods create a VXLAN interface at startup and run a node reconciler that maintains VTEP entries for all hybrid nodes. The leader performs VPC route table updates and Cilium VTEP configuration. If the leader fails, the standby detects the lease expiration, acquires the lease, and runs the leader setup sequence. Expected failover time is approximately 3–5 seconds.

## Deployment model
<a name="hybrid-nodes-gateway-deployment-model"></a>

The Hybrid Nodes gateway runs on EC2 instances in your VPC and is deployed using a Helm chart. The gateway supports the following deployment targets:
+  **EKS Auto Mode** — You create a `NodePool` and `NodeClass` that automatically provision gateway nodes with the correct labels, taints, and source/destination check configuration. This is the recommended configuration.
+  **EKS managed node groups** — You create a dedicated managed node group with the gateway label, taint, and source/destination check disabled, then set `autoMode.enabled=false` in the Helm values.

For all deployment targets, at least two nodes are recommended for high availability. For more information, see [Get started with EKS Hybrid Nodes gateway](hybrid-nodes-gateway-getting-started.md).

## Pricing
<a name="hybrid-nodes-gateway-pricing"></a>

There is no additional charge for the Amazon EKS Hybrid Nodes gateway, but you will be charged for the infrastructure costs for running the gateway, including the EC2 instances and EKS Auto Mode management fees if applicable. For more information, see [Amazon EKS pricing](https://aws.amazon.com/eks/pricing/).

## Region availability
<a name="hybrid-nodes-gateway-region-availability"></a>

The Amazon EKS Hybrid Nodes gateway is available in all AWS Regions where EKS Hybrid Nodes is available, except China Regions. For the current list of supported Regions, see [Amazon EKS Hybrid Nodes overview](hybrid-nodes-overview.md).

## Open source
<a name="hybrid-nodes-gateway-open-source"></a>

The Amazon EKS Hybrid Nodes gateway codebase is open source. You can view the source code, report issues, and contribute at the [GitHub repository](https://github.com/aws/eks-hybrid-nodes-gateway).

## Limitations and considerations
<a name="hybrid-nodes-gateway-limitations"></a>

Before deploying the Hybrid Nodes gateway, consider the following:
+  **No traffic encryption** — The VXLAN tunnels created by the gateway do not encrypt traffic. If you require encryption in transit between the VPC and your on-premises environment, use an encrypted transport such as AWS Direct Connect with MACsec or a VPN connection. For more information, see [Data protection in Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/data-protection.html).
+  **Single cluster** — Each gateway deployment serves a single EKS cluster. If you have multiple clusters with hybrid nodes, deploy a separate gateway for each cluster.
+  **Cilium VTEP required** — The gateway requires the EKS version of the Cilium CNI with VTEP support enabled on hybrid nodes. Other CNI plugins are not supported.

## Next steps
<a name="hybrid-nodes-gateway-next-steps"></a>
+  [Get started with EKS Hybrid Nodes gateway](hybrid-nodes-gateway-getting-started.md) 
+  [Amazon EKS Hybrid Nodes gateway configuration reference](hybrid-nodes-gateway-configuration.md) 
+  [Amazon EKS Hybrid Nodes gateway operations](hybrid-nodes-gateway-operations.md) 
+  [Amazon EKS Hybrid Nodes gateway troubleshooting](hybrid-nodes-gateway-troubleshooting.md) 