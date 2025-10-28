**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Configure application networking, add-ons, and webhooks for hybrid nodes

After you create an EKS cluster for hybrid nodes, configure additional capabilities for application networking (CNI, BGP, Ingress, Load Balancing, Network Policies), add-ons, webhooks, and proxy settings. For the complete list of the EKS and community add-ons that are compatible with hybrid nodes, see [Configure add-ons for hybrid nodes](hybrid-nodes-add-ons.md "hybrid-nodes-add-ons.md").

**EKS cluster insights**
EKS includes insight checks for misconfigurations in your hybrid nodes setup that could impair functionality of your cluster or workloads. For more information on cluster insights, see [Prepare for Kubernetes version upgrades and troubleshoot misconfigurations with cluster insights](cluster-insights.md "cluster-insights.md").

The following lists the common capabilities and add-ons that you can use with hybrid nodes:

- **Container Networking Interface (CNI)**: AWS supports [Cilium](https://docs.cilium.io/en/stable/index.html "https://docs.cilium.io/en/stable/index.html") as the CNI for hybrid nodes. For more information, see [Configure CNI for hybrid nodes](hybrid-nodes-cni.md "hybrid-nodes-cni.md"). Note that the AWS VPC CNI can’t be used with hybrid nodes.
- **CoreDNS and `kube-proxy`**: CoreDNS and `kube-proxy` are installed automatically when hybrid nodes join the EKS cluster. These add-ons can be managed as EKS add-ons after cluster creation.
- **Ingress and Load Balancing**: You can use the AWS Load Balancer Controller and Application Load Balancer (ALB) or Network Load Balancer (NLB) with the target type `ip` for workloads running on hybrid nodes. AWS supports Cilium’s built-in Ingress, Gateway, and Kubernetes Service load balancing features for workloads running on hybrid nodes. For more information, see [Configure Kubernetes Ingress for hybrid nodes](hybrid-nodes-ingress.md "hybrid-nodes-ingress.md") and [Configure Services of type LoadBalancer for hybrid nodes](hybrid-nodes-load-balancing.md "hybrid-nodes-load-balancing.md").
- **Metrics**: You can use Amazon Managed Service for Prometheus (AMP) agent-less scrapers, AWS Distro for Open Telemetry (ADOT), and the Amazon CloudWatch Observability Agent with hybrid nodes. To use AMP agent-less scrapers for pod metrics on hybrid nodes, your pods must be accessible from the VPC that you use for the EKS cluster.
- **Logs**: You can enable EKS control plane logging for hybrid nodes-enabled clusters. You can use the ADOT EKS add-on and the Amazon CloudWatch Observability Agent EKS add-on for hybrid node and pod logging.
- **Pod Identities and IRSA**: You can use EKS Pod Identities and IAM Roles for Service Accounts (IRSA) with applications running on hybrid nodes to enable granular access for your pods running on hybrid nodes with other AWS services.
- **Webhooks**: If you are running webhooks, see [Configure webhooks for hybrid nodes](hybrid-nodes-webhooks.md "hybrid-nodes-webhooks.md") for considerations and steps to optionally run webhooks on cloud nodes if you cannot make your on-premises pod networks routable.
- **Proxy**: If you are using a proxy server in your on-premises environment for traffic leaving your data center or edge environment, you can configure your hybrid nodes and cluster to use your proxy server. For more information, see [Configure proxy for hybrid nodes](hybrid-nodes-proxy.md "hybrid-nodes-proxy.md").

###### Topics

- [Configure CNI for hybrid nodes](hybrid-nodes-cni.md "hybrid-nodes-cni.md")
- [Configure add-ons for hybrid nodes](hybrid-nodes-add-ons.md "hybrid-nodes-add-ons.md")
- [Configure webhooks for hybrid nodes](hybrid-nodes-webhooks.md "hybrid-nodes-webhooks.md")
- [Configure proxy for hybrid nodes](hybrid-nodes-proxy.md "hybrid-nodes-proxy.md")
- [Configure Cilium BGP for hybrid nodes](hybrid-nodes-cilium-bgp.md "hybrid-nodes-cilium-bgp.md")
- [Configure Kubernetes Ingress for hybrid nodes](hybrid-nodes-ingress.md "hybrid-nodes-ingress.md")
- [Configure Services of type LoadBalancer for hybrid nodes](hybrid-nodes-load-balancing.md "hybrid-nodes-load-balancing.md")
- [Configure Kubernetes Network Policies for hybrid nodes](hybrid-nodes-network-policies.md "hybrid-nodes-network-policies.md")
