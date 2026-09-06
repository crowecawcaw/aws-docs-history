

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Configure CNI for the Hybrid Nodes gateway
<a name="hybrid-nodes-gateway-cni"></a>

The Amazon EKS Hybrid Nodes gateway requires specific Cilium configuration to enable VXLAN-based connectivity between your VPC and hybrid nodes. You must enable Cilium VTEP (VXLAN Tunnel Endpoint) support and disable the L7 proxy.

## Prerequisites
<a name="hybrid-nodes-gateway-cni-prereqs"></a>
+ Cilium is already installed on your hybrid nodes. For installation instructions, see [Configure CNI for hybrid nodes](hybrid-nodes-cni.md).

**Note**  
Cilium VTEP is only supported on the following minimum EKS Cilium versions:  
Cilium 1.17.13-1 or later
Cilium 1.18.8-1 or later
Cilium 1.19.2-1 or later
If you are running an older version, upgrade Cilium before enabling VTEP. For upgrade instructions, see [Configure CNI for hybrid nodes](hybrid-nodes-cni.md).

## Enable VTEP and disable L7 proxy
<a name="hybrid-nodes-gateway-cni-configure"></a>

Set the Cilium version and run the `helm upgrade` command to enable VTEP and disable the L7 proxy on your existing Cilium installation. You can find the latest available patch version at [Amazon ECR Public: eks/cilium/cilium](https://gallery.ecr.aws/eks/cilium/cilium).

```
helm upgrade cilium oci://public.ecr.aws/eks/cilium/cilium \
  --version {{CILIUM_VERSION}} \
  --namespace kube-system \
  --reuse-values \
  --set vtep.enabled=true \
  --set l7Proxy=false
```

After the upgrade completes, restart the Cilium DaemonSet to apply the new configuration:

```
kubectl rollout restart daemonset/cilium -n kube-system
kubectl rollout status daemonset/cilium -n kube-system
```

## Required settings
<a name="hybrid-nodes-gateway-cni-settings"></a>


| Setting | Value | Description | 
| --- | --- | --- | 
|  `vtep.enabled`  |  `true`  | Enables Cilium’s VXLAN Tunnel Endpoint support. This allows Cilium agents on hybrid nodes to encapsulate VPC-bound traffic and send it to the gateway. | 
|  `l7Proxy`  |  `false`  | Disables Cilium’s L7 proxy. This is required for VTEP to function correctly. If L7 proxy is enabled, VTEP traffic may be intercepted and dropped. | 

## Verify the configuration
<a name="hybrid-nodes-gateway-cni-verify"></a>

After upgrading Cilium, verify that VTEP is enabled and the L7 proxy is disabled:

```
kubectl get configmap cilium-config -n kube-system -o yaml | grep -E "enable-vtep|enable-l7-proxy"
```

You should see output similar to:

```
enable-l7-proxy: "false"
enable-vtep: "true"
```

## Configure VPC CNI for hybrid pod traffic
<a name="hybrid-nodes-gateway-cni-vpc-cni"></a>

By default, the AWS VPC CNI applies source NAT (SNAT) to all pod traffic leaving the node. To ensure that Kubernetes ClusterIP services with hybrid pod endpoints work correctly from cloud nodes, exclude the hybrid pod CIDRs from SNAT. This allows kube-proxy DNAT’d traffic to use VPC routing correctly.

Set the `AWS_VPC_K8S_CNI_EXCLUDE_SNAT_CIDRS` environment variable on the `aws-node` DaemonSet to your hybrid pod CIDR(s):

```
kubectl set env daemonset aws-node -n kube-system \
  AWS_VPC_K8S_CNI_EXCLUDE_SNAT_CIDRS={{POD_CIDRS}}
```

Replace the value with your actual hybrid pod CIDRs (comma-separated if multiple).

This setting adds the hybrid pod CIDRs to the VPC CNI’s ip rules so that traffic destined for hybrid pods is routed through the main routing table, which contains the VPC route to the gateway ENI.

**Note**  
This step is required for ClusterIP service traffic from cloud pods to hybrid pod endpoints. Direct pod-to-pod connectivity by IP address works without this setting.

## Next steps
<a name="hybrid-nodes-gateway-cni-next"></a>

After configuring Cilium and VPC CNI, proceed to install the Hybrid Nodes gateway. See [Get started with EKS Hybrid Nodes gateway](hybrid-nodes-gateway-getting-started.md).