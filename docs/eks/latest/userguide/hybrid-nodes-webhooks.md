**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Configure webhooks for hybrid nodes

This page details considerations for running webhooks with hybrid nodes. Webhooks are used in Kubernetes applications and open source projects, such as the AWS Load Balancer Controller and CloudWatch Observability Agent, to perform mutating and validation capabilities at runtime.

**Routable pod networks**

If you are able to make your on-premises pod CIDR routable on your on-premises network, you can run webhooks on hybrid nodes. There are several techniques you can use to make your on-premises pod CIDR routable on your on-premises network including Border Gateway Protocol (BGP), static routes, or other custom routing solutions. BGP is the recommended solution as it is more scalable and easier to manage than alternative solutions that require custom or manual route configuration. AWS supports the BGP capabilities of Cilium and Calico for advertising pod CIDRs, see [Configure CNI for hybrid nodes](hybrid-nodes-cni.md "hybrid-nodes-cni.md") and [Routable remote Pod CIDRs](hybrid-nodes-concepts-kubernetes.md#hybrid-nodes-concepts-k8s-pod-cidrs "hybrid-nodes-concepts-kubernetes.md#hybrid-nodes-concepts-k8s-pod-cidrs") for more information.

**Unroutable pod networks**

If you _cannot_ make your on-premises pod CIDR routable on your on-premises network and need to run webhooks, we recommend that you run all webhooks on cloud nodes in the same EKS cluster as your hybrid nodes.

## Considerations for mixed mode clusters

_Mixed mode clusters_ are defined as EKS clusters that have both hybrid nodes and nodes running in AWS Cloud. When running a mixed mode cluster, consider the following recommendations:

- Run the VPC CNI on nodes in AWS Cloud and either Cilium or Calico on hybrid nodes. Cilium and Calico are not supported by AWS when running on nodes in AWS Cloud.
- Configure webhooks to run on nodes in AWS Cloud. See [Configure webhooks for add-ons](#hybrid-nodes-webhooks-add-ons "#hybrid-nodes-webhooks-add-ons") for how to configure the webhooks for AWS and community add-ons.
- If your applications require pods running on nodes in AWS Cloud to directly communicate with pods running on hybrid nodes ("east-west communication"), and you are using the VPC CNI on nodes in AWS Cloud, and Cilium or Calico on hybrid nodes, then your on-premises pod CIDR must be routable on your on-premises network.
- Run at least one replica of CoreDNS on nodes in AWS Cloud and at least one replica of CoreDNS on hybrid nodes.
- Configure Service Traffic Distribution to keep Service traffic local to the zone it is originating from. For more information on Service Traffic Distribution, see [Configure Service Traffic Distribution](#hybrid-nodes-mixed-service-traffic-distribution "#hybrid-nodes-mixed-service-traffic-distribution").
- If you are using AWS Application Load Balancers (ALB) or Network Load Balancers (NLB) for workload traffic running on hybrid nodes, then the IP target(s) used with the ALB or NLB must be routable from AWS.
- The Metrics Server add-on requires connectivity from the EKS control plane to the Metrics Server pod IP address. If you are running the Metrics Server add-on on hybrid nodes, then your on-premises pod CIDR must be routable on your on-premises network.
- To collect metrics for hybrid nodes using Amazon Managed Service for Prometheus (AMP) managed collectors, your on-premises pod CIDR must be routable on your on-premises network. Or, you can use the AMP managed collector for EKS control plane metrics and resources running in AWS Cloud, and the AWS Distro for OpenTelemetry (ADOT) add-on to collect metrics for hybrid nodes.

## Configure mixed mode clusters

To view the mutating and validating webhooks running on your cluster, you can view the **Extensions** resource type in the **Resources** panel of the EKS console for your cluster, or you can use the following commands. EKS also reports webhook metrics in the cluster observability dashboard, see [Monitor your cluster with the observability dashboard](observability-dashboard.md "observability-dashboard.md") for more information.

```
kubectl get mutatingwebhookconfigurations
```

```
kubectl get validatingwebhookconfigurations
```

### Configure Service Traffic Distribution

When running mixed mode clusters, we recommend that you use [_Service Traffic Distribution_](https://kubernetes.io/docs/reference/networking/virtual-ips/#traffic-distribution "https://kubernetes.io/docs/reference/networking/virtual-ips/#traffic-distribution") to keep Service traffic local to the zone it is originating from. Service Traffic Distribution (available for Kubernetes versions 1.31 and later in EKS) is the recommended solution over [Topology Aware Routing](https://kubernetes.io/docs/concepts/services-networking/topology-aware-routing/ "https://kubernetes.io/docs/concepts/services-networking/topology-aware-routing/") because it is more predictable. With Service Traffic Distribution, healthy endpoints in the zone will receive all of the traffic for that zone. With Topology Aware Routing, each service must meet several conditions in that zone to apply the custom routing, otherwise it routes traffic evenly to all endpoints.

If you are using Cilium as your CNI, you must run the CNI with the `enable-service-topology` set to `true` to enable Service Traffic Distribution. You can pass this configuration with the Helm install flag `--set loadBalancer.serviceTopology=true` or you can update an existing installation with the Cilium CLI command `cilium config set enable-service-topology true`. The Cilium agent running on each node must be restarted after updating the configuration for an existing installation.

An example of how to configure Service Traffic Distribution for the CoreDNS Service is shown in the following section, and we recommend that you enable the same for all Services in your cluster to avoid unintended cross-environment traffic.

### Configure CoreDNS replicas

If you are running a mixed mode cluster with both hybrid nodes and nodes in AWS Cloud, we recommend that you have at least one CoreDNS replica on hybrid nodes and at least one CoreDNS replica on your nodes in AWS Cloud. To prevent latency and network issues in a mixed mode cluster setup, you can configure the CoreDNS Service to prefer the closest CoreDNS replica with [Service Traffic Distribution](https://kubernetes.io/docs/reference/networking/virtual-ips/#traffic-distribution "https://kubernetes.io/docs/reference/networking/virtual-ips/#traffic-distribution").

_Service Traffic Distribution_ (available for Kubernetes versions 1.31 and later in EKS) is the recommended solution over [Topology Aware Routing](https://kubernetes.io/docs/concepts/services-networking/topology-aware-routing/ "https://kubernetes.io/docs/concepts/services-networking/topology-aware-routing/") because it is more predictable. In Service Traffic Distribution, healthy endpoints in the zone will receive all of the traffic for that zone. In Topology Aware Routing, each service must meet several conditions in that zone to apply the custom routing, otherwise it routes traffic evenly to all endpoints. The following steps configure Service Traffic Distribution.

If you are using Cilium as your CNI, you must run the CNI with the `enable-service-topology` set to `true` to enable Service Traffic Distribution. You can pass this configuration with the Helm install flag `--set loadBalancer.serviceTopology=true` or you can update an existing installation with the Cilium CLI command `cilium config set enable-service-topology true`. The Cilium agent running on each node must be restarted after updating the configuration for an existing installation.

1. Add a topology zone label for each of your hybrid nodes, for example `topology.kubernetes.io/zone: onprem`. Or, you can set the label at the `nodeadm init` phase by specifying the label in your `nodeadm` configuration, see [Node Config for customizing kubelet (Optional)](hybrid-nodes-nodeadm.md#hybrid-nodes-nodeadm-kubelet "hybrid-nodes-nodeadm.md#hybrid-nodes-nodeadm-kubelet"). Note, nodes running in AWS Cloud automatically get a topology zone label applied to them that corresponds to the availability zone (AZ) of the node.

```
kubectl label node `hybrid-node-name` topology.kubernetes.io/zone=`zone`

```

2. Add `podAntiAffinity` to the CoreDNS deployment with the topology zone key. Or, you can configure the CoreDNS deployment during installation with EKS add-ons.

```
kubectl edit deployment coredns -n kube-system
```

```
spec:
  template:
    spec:
      affinity:
       ...
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - podAffinityTerm:
              labelSelector:
                matchExpressions:
                - key: k8s-app
                  operator: In
                  values:
                  - kube-dns
              topologyKey: kubernetes.io/hostname
            weight: 100
          - podAffinityTerm:
              labelSelector:
                matchExpressions:
                - key: k8s-app
                  operator: In
                  values:
                  - kube-dns
              topologyKey: topology.kubernetes.io/zone
            weight: 50
      ...
```

3. Add the setting `trafficDistribution: PreferClose` to the `kube-dns` Service configuration to enable Service Traffic Distribution.

```
kubectl patch svc kube-dns -n kube-system --type=merge -p '{
  "spec": {
    "trafficDistribution": "PreferClose"
  }
}'
```

4. You can confirm that Service Traffic Distribution is enabled by viewing the endpoint slices for the `kube-dns` Service. Your endpoint slices must show the `hints` for your topology zone labels, which confirms that Service Traffic Distribution is enabled. If you do not see the `hints` for each endpoint address, then Service Traffic Distribution is not enabled.

```
kubectl get endpointslice -A | grep "kube-dns"
```

```
kubectl get endpointslice [.replaceable]`kube-dns-<id>`  -n kube-system -o yaml
```

```
addressType: IPv4
apiVersion: discovery.k8s.io/v1
endpoints:
- addresses:
  - <your-hybrid-node-pod-ip>
  hints:
    forZones:
    - name: onprem
  nodeName: <your-hybrid-node-name>
  zone: onprem
- addresses:
  - <your-cloud-node-pod-ip>
  hints:
    forZones:
    - name: us-west-2a
  nodeName: <your-cloud-node-name>
  zone: us-west-2a
```

### Configure webhooks for add-ons

The following add-ons use webhooks and are supported for use with hybrid nodes.

- AWS Load Balancer Controller
- CloudWatch Observability Agent
- AWS Distro for OpenTelemetry (ADOT)
- `cert-manager`

See the following sections for configuring the webhooks used by these add-ons to run on nodes in AWS Cloud.

#### AWS Load Balancer Controller

To use the AWS Load Balancer Controller in a mixed mode cluster setup, you must run the controller on nodes in AWS Cloud. To do so, add the following to your Helm values configuration or specify the values by using EKS add-on configuration.

```
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
      - matchExpressions:
        - key: eks.amazonaws.com/compute-type
          operator: NotIn
          values:
          - hybrid
```

#### CloudWatch Observability Agent

The CloudWatch Observability Agent add-on has a Kubernetes Operator that uses webhooks. To run the operator on nodes in AWS Cloud in a mixed mode cluster setup, edit the CloudWatch Observability Agent operator configuration. You can’t configure the operator affinity during installation with Helm and EKS add-ons (see [containers-roadmap issue #2431](https://github.com/aws/containers-roadmap/issues/2431 "https://github.com/aws/containers-roadmap/issues/2431")).

```
kubectl edit -n amazon-cloudwatch deployment amazon-cloudwatch-observability-controller-manager
```

```
spec:
  ...
  template:
    ...
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: eks.amazonaws.com/compute-type
                operator: NotIn
                values:
                - hybrid
```

#### AWS Distro for OpenTelemetry (ADOT)

The AWS Distro for OpenTelemetry (ADOT) add-on has a Kubernetes Operator that uses webhooks. To run the operator on nodes in AWS Cloud in a mixed mode cluster setup, add the following to your Helm values configuration or specify the values by using EKS add-on configuration.

```
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
      - matchExpressions:
        - key: eks.amazonaws.com/compute-type
          operator: NotIn
          values:
          - hybrid
```

If your pod CIDR is not routable on your on-premises network, then the ADOT collector must run on hybrid nodes to scrape the metrics from your hybrid nodes and the workloads running on them. To do so, edit the Custom Resource Definition (CRD).

```
kubectl -n opentelemetry-operator-system edit opentelemetrycollectors.opentelemetry.io adot-col-prom-metrics
```

```
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: eks.amazonaws.com/compute-type
            operator: In
            values:
            - hybrid
```

You can configure the ADOT collector to only scrape metrics from hybrid nodes and the resources running on hybrid nodes by adding the following `relabel_configs` to each `scrape_configs` in the ADOT collector CRD configuration.

```
relabel_configs:
  - action: keep
    regex: hybrid
    source_labels:
    - __meta_kubernetes_node_label_eks_amazonaws_com_compute_type
```

The ADOT add-on has a prerequisite requirement to install `cert-manager` for the TLS certificates used by the ADOT operator webhook. `cert-manager` also runs webhooks and you can configure it to run on nodes in AWS Cloud with the following Helm values configuration.

```
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
      - matchExpressions:
        - key: eks.amazonaws.com/compute-type
          operator: NotIn
          values:
          - hybrid
webhook:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: eks.amazonaws.com/compute-type
            operator: NotIn
            values:
            - hybrid
cainjector:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: eks.amazonaws.com/compute-type
            operator: NotIn
            values:
            - hybrid
startupapicheck:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: eks.amazonaws.com/compute-type
            operator: NotIn
            values:
            - hybrid
```

#### `cert-manager`

The `cert-manager` add-on runs webhooks and you can configure it to run on nodes in AWS Cloud with the following Helm values configuration.

```
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
      - matchExpressions:
        - key: eks.amazonaws.com/compute-type
          operator: NotIn
          values:
          - hybrid
webhook:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: eks.amazonaws.com/compute-type
            operator: NotIn
            values:
            - hybrid
cainjector:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: eks.amazonaws.com/compute-type
            operator: NotIn
            values:
            - hybrid
startupapicheck:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: eks.amazonaws.com/compute-type
            operator: NotIn
            values:
            - hybrid
```
