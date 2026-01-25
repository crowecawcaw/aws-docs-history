**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Configure add-ons for hybrid nodes

This page describes considerations for running AWS add-ons and community add-ons on Amazon EKS Hybrid Nodes. To learn more about Amazon EKS add-ons and the processes for creating, upgrading, and removing add-ons from your cluster, see [Amazon EKS add-ons](eks-add-ons.md "eks-add-ons.md"). Unless otherwise noted on this page, the processes for creating, upgrading, and removing Amazon EKS add-ons is the same for Amazon EKS clusters with hybrid nodes as it is for Amazon EKS clusters with nodes running in AWS Cloud. Only the add-ons included on this page have been validated for compatibility with Amazon EKS Hybrid Nodes.

The following AWS add-ons are compatible with Amazon EKS Hybrid Nodes.

| AWS add-on                              | Compatible add-on versions                                                                               |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| kube-proxy                              | v1.25.14-eksbuild.2 and above                                                                            |
| CoreDNS                                 | v1.9.3-eksbuild.7 and above                                                                              |
| AWS Distro for OpenTelemetry (ADOT)     | v0.102.1-eksbuild.2 and above                                                                            |
| CloudWatch Observability agent          | v2.2.1-eksbuild.1 and above                                                                              |
| EKS Pod Identity Agent                  | • v1.3.3-eksbuild.1 and above, except for Bottlerocket<br>• v1.3.7-eksbuild.2 and above for Bottlerocket |
| Node monitoring agent                   | v1.2.0-eksbuild.1 and above                                                                              |
| CSI snapshot controller                 | v8.1.0-eksbuild.1 and above                                                                              |
| AWS Private CA Connector for Kubernetes | v1.6.0-eksbuild.1 and above                                                                              |

The following community add-ons are compatible with Amazon EKS Hybrid Nodes. To learn more about community add-ons, see [Community add-ons](community-addons.md "community-addons.md").

| Community add-on          | Compatible add-on versions   |
| ------------------------- | ---------------------------- |
| Kubernetes Metrics Server | v0.7.2-eksbuild.1 and above  |
| cert-manager              | v1.17.2-eksbuild.1 and above |
| Prometheus Node Exporter  | v1.9.1-eksbuild.2 and above  |
| kube-state-metrics        | v2.15.0-eksbuild.4 and above |
| External DNS              | v0.19.0-eksbuild.1 and above |

In addition to the Amazon EKS add-ons in the tables above, the [Amazon Managed Service for Prometheus Collector](prometheus.md "prometheus.md"), and the [AWS Load Balancer Controller](aws-load-balancer-controller.md "aws-load-balancer-controller.md") for [application ingress](alb-ingress.md "alb-ingress.md") (HTTP) and [load balancing](network-load-balancing.md "network-load-balancing.md") (TCP/UDP) are compatible with hybrid nodes.

There are AWS add-ons and community add-ons that aren’t compatible with Amazon EKS Hybrid Nodes. The latest versions of these add-ons have an anti-affinity rule for the default `eks.amazonaws.com/compute-type: hybrid` label applied to hybrid nodes. This prevents them from running on hybrid nodes when deployed in your clusters. If you have clusters with both hybrid nodes and nodes running in AWS Cloud, you can deploy these add-ons in your cluster to nodes running in AWS Cloud. The Amazon VPC CNI is not compatible with hybrid nodes, and Cilium and Calico are supported as the Container Networking Interfaces (CNIs) for Amazon EKS Hybrid Nodes. See [Configure CNI for hybrid nodes](hybrid-nodes-cni.md "hybrid-nodes-cni.md") for more information.

## AWS add-ons

The sections that follow describe differences between running compatible AWS add-ons on hybrid nodes compared to other Amazon EKS compute types.

## kube-proxy and CoreDNS

EKS installs kube-proxy and CoreDNS as self-managed add-ons by default when you create an EKS cluster with the AWS API and AWS SDKs, including from the AWS CLI. You can overwrite these add-ons with Amazon EKS add-ons after cluster creation. Reference the EKS documentation for details on [Manage kube-proxy in Amazon EKS clusters](managing-kube-proxy.md "managing-kube-proxy.md") and [Manage CoreDNS for DNS in Amazon EKS clusters](managing-coredns.md "managing-coredns.md"). If you are running a mixed mode cluster with both hybrid nodes and nodes in AWS Cloud, AWS recommends to have at least one CoreDNS replica on hybrid nodes and at least one CoreDNS replica on your nodes in AWS Cloud. See [Configure CoreDNS replicas](hybrid-nodes-webhooks.md#hybrid-nodes-mixed-coredns "hybrid-nodes-webhooks.md#hybrid-nodes-mixed-coredns") for configuration steps.

## CloudWatch Observability agent

The CloudWatch Observability agent operator uses [webhooks](https://kubernetes.io/docs/reference/access-authn-authz/webhook/ "https://kubernetes.io/docs/reference/access-authn-authz/webhook/"). If you run the operator on hybrid nodes, your on-premises pod CIDR must be routable on your on-premises network and you must configure your EKS cluster with your remote pod network. For more information, see [Configure webhooks for hybrid nodes](hybrid-nodes-webhooks.md "hybrid-nodes-webhooks.md").

Node-level metrics are not available for hybrid nodes because [CloudWatch Container Insights](../../../AmazonCloudWatch/latest/monitoring/ContainerInsights.md "../../../AmazonCloudWatch/latest/monitoring/ContainerInsights.md") depends on the availability of [Instance Metadata Service](../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md "../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md") (IMDS) for node-level metrics. Cluster, workload, pod, and container-level metrics are available for hybrid nodes.

After installing the add-on by following the steps described in [Install the CloudWatch agent with the Amazon CloudWatch Observability](../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Observability-EKS-addon.md "../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Observability-EKS-addon.md"), the add-on manifest must be updated before the agent can run successfully on hybrid nodes. Edit the `amazoncloudwatchagents` resource on the cluster to add the `RUN_WITH_IRSA` environment variable as shown below.

```
kubectl edit amazoncloudwatchagents -n amazon-cloudwatch cloudwatch-agent
```

```
apiVersion: v1
items:
- apiVersion: cloudwatch.aws.amazon.com/v1alpha1
  kind: AmazonCloudWatchAgent
  metadata:
    ...
    name: cloudwatch-agent
    namespace: amazon-cloudwatch
    ...
  spec:
    ...
    env:
    - name: RUN_WITH_IRSA # <-- Add this
      value: "True" # <-- Add this
    - name: K8S_NODE_NAME
      valueFrom:
        fieldRef:
          fieldPath: spec.nodeName
          ...
```

## Amazon Managed Prometheus managed collector for hybrid nodes

An Amazon Managed Service for Prometheus (AMP) managed collector consists of a scraper that discovers and collects metrics from the resources in an Amazon EKS cluster. AMP manages the scraper for you, removing the need to manage any instances, agents, or scrapers yourself.

You can use AMP managed collectors without any additional configuration specific to hybrid nodes. However the metric endpoints for your applications on the hybrid nodes must be reachable from the VPC, including routes from the VPC to remote pod network CIDRs and the ports open in your on-premises firewall. Additionally, your cluster must have [private cluster endpoint access](cluster-endpoint.md "cluster-endpoint.md").

Follow the steps in [Using an AWS managed collector](../../../prometheus/latest/userguide/AMP-collector-how-to.md "../../../prometheus/latest/userguide/AMP-collector-how-to.md") in the Amazon Managed Service for Prometheus User Guide.

## AWS Distro for OpenTelemetry (ADOT)

You can use the AWS Distro for OpenTelemetry (ADOT) add-on to collect metrics, logs, and tracing data from your applications running on hybrid nodes. ADOT uses admission [webhooks](https://kubernetes.io/docs/reference/access-authn-authz/webhook/ "https://kubernetes.io/docs/reference/access-authn-authz/webhook/") to mutate and validate the Collector Custom Resource requests. If you run the ADOT operator on hybrid nodes, your on-premises pod CIDR must be routable on your on-premises network and you must configure your EKS cluster with your remote pod network. For more information, see [Configure webhooks for hybrid nodes](hybrid-nodes-webhooks.md "hybrid-nodes-webhooks.md").

Follow the steps in [Getting Started with AWS Distro for OpenTelemetry using EKS Add-Ons](https://aws-otel.github.io/docs/getting-started/adot-eks-add-on "https://aws-otel.github.io/docs/getting-started/adot-eks-add-on") in the _AWS Distro for OpenTelemetry_ documentation.

## AWS Load Balancer Controller

You can use the [AWS Load Balancer Controller](aws-load-balancer-controller.md "aws-load-balancer-controller.md") and Application Load Balancer (ALB) or Network Load Balancer (NLB) with the target type `ip` for workloads on hybrid nodes The IP target(s) used with the ALB or NLB must be routable from AWS. The AWS Load Balancer controller also uses [webhooks](https://kubernetes.io/docs/reference/access-authn-authz/webhook/ "https://kubernetes.io/docs/reference/access-authn-authz/webhook/"). If you run the AWS Load Balancer Controller operator on hybrid nodes, your on-premises pod CIDR must be routable on your on-premises network and you must configure your EKS cluster with your remote pod network. For more information, see [Configure webhooks for hybrid nodes](hybrid-nodes-webhooks.md "hybrid-nodes-webhooks.md").

To install the AWS Load Balancer Controller, follow the steps at [AWS Application Load Balancer](hybrid-nodes-ingress.md#hybrid-nodes-ingress-alb "hybrid-nodes-ingress.md#hybrid-nodes-ingress-alb") or [AWS Network Load Balancer](hybrid-nodes-load-balancing.md#hybrid-nodes-service-lb-nlb "hybrid-nodes-load-balancing.md#hybrid-nodes-service-lb-nlb").

For ingress with ALB, you must specify the annotations below. See [Route application and HTTP traffic with Application Load Balancers](alb-ingress.md "alb-ingress.md") for more information.

```
alb.ingress.kubernetes.io/target-type: ip
```

For load balancing with NLB, you must specify the annotations below. See [Route TCP and UDP traffic with Network Load Balancers](network-load-balancing.md "network-load-balancing.md") for more information.

```
service.beta.kubernetes.io/aws-load-balancer-type: "external"
service.beta.kubernetes.io/aws-load-balancer-nlb-target-type: "ip"
```

## EKS Pod Identity Agent

###### Note

To successfully deploy the EKS Pod Identity Agent add-on on hybrid nodes running Bottlerocket, ensure your Bottlerocket version is at least v1.39.0. The Pod Identity Agent is not supported on earlier Bottlerocket versions in hybrid node environments.

The original Amazon EKS Pod Identity Agent DaemonSet relies on the availability of EC2 IMDS on the node to obtain the required AWS credentials. As IMDS isn’t available on hybrid nodes, starting with version 1.3.3-eksbuild.1, the Pod Identity Agent add-on optionally deploys a DaemonSet that mounts the required credentials. Hybrid nodes running Bottlerocket require a different method to mount the credentials, and starting in version 1.3.7-eksbuild.2, the Pod Identity Agent add-on optionally deploys a DaemonSet that specifically targets Bottlerocket hybrid nodes. The following sections describe the process for enabling the optional DaemonSets.

### Ubuntu/RHEL/AL2023

1. To use the Pod Identity agent on Ubuntu/RHEL/Al2023 hybrid nodes, set `enableCredentialsFile: true` in the hybrid section of `nodeadm` config as shown below:

```
apiVersion: node.eks.aws/v1alpha1
kind: NodeConfig
spec:
    hybrid:
        enableCredentialsFile: true # <-- Add this
```

This will configure `nodeadm` to create a credentials file to be configured on the node under `/eks-hybrid/.aws/credentials`, which will be used by `eks-pod-identity-agent` pods. This credentials file will contain temporary AWS credentials that will be refreshed periodically. 2. After you update the `nodeadm` config on _each_ node, run the following `nodeadm init` command with your `nodeConfig.yaml` to join your hybrid nodes to your Amazon EKS cluster. If your nodes have joined the cluster previous, still run the `nodeadm init` command again.

```
nodeadm init -c file://nodeConfig.yaml
```

3. Install `eks-pod-identity-agent` with support for hybrid nodes enabled, by using either the AWS CLI or AWS Management Console.
   1. AWS CLI: From the machine that you’re using to administer the cluster, run the following command to install `eks-pod-identity-agent` with support for hybrid nodes enabled. Replace `my-cluster` with the name of your cluster.

   ```
   aws eks create-addon \
       --cluster-name my-cluster \
       --addon-name eks-pod-identity-agent \
       --configuration-values '{"daemonsets":{"hybrid":{"create": true}}}'
   ```

   2. AWS Management Console: If you are installing the Pod Identity Agent add-on through the AWS console, add the following to the optional configuration to deploy the DaemonSet that targets hybrid nodes.

   ```
   {"daemonsets":{"hybrid":{"create": true}}}
   ```

### Bottlerocket

1. To use the Pod Identity agent on Bottlerocket hybrid nodes, add the `--enable-credentials-file=true` flag to the command used for the Bottlerocket bootstrap container user data, as described in [Connect hybrid nodes with Bottlerocket](hybrid-nodes-bottlerocket.md "hybrid-nodes-bottlerocket.md").
   1. If you are using the SSM credential provider, your command should look like this:

   ```
   eks-hybrid-ssm-setup --activation-id=<activation-id> --activation-code=<activation-code> --region=<region> --enable-credentials-file=true
   ```

   2. If you are using the IAM Roles Anywhere credential provider, your command should look like this:

   ```
   eks-hybrid-iam-ra-setup --certificate=<certificate> --key=<private-key> --enable-credentials-file=true
   ```

   This will configure the bootstrap script to create a credentials file on the node under `/var/eks-hybrid/.aws/credentials`, which will be used by `eks-pod-identity-agent` pods. This credentials file will contain temporary AWS credentials that will be refreshed periodically.

2. Install `eks-pod-identity-agent` with support for Bottlerocket hybrid nodes enabled, by using either the AWS CLI or AWS Management Console.
   1. AWS CLI: From the machine that you’re using to administer the cluster, run the following command to install `eks-pod-identity-agent` with support for Bottlerocket hybrid nodes enabled. Replace `my-cluster` with the name of your cluster.

   ```
   aws eks create-addon \
       --cluster-name my-cluster \
       --addon-name eks-pod-identity-agent \
       --configuration-values '{"daemonsets":{"hybrid-bottlerocket":{"create": true}}}'
   ```

   2. AWS Management Console: If you are installing the Pod Identity Agent add-on through the AWS console, add the following to the optional configuration to deploy the DaemonSet that targets Bottlerocket hybrid nodes.

   ```
   {"daemonsets":{"hybrid-bottlerocket":{"create": true}}}
   ```

## CSI snapshot controller

Starting with version `v8.1.0-eksbuild.2`, the [CSI snapshot controller add-on](csi-snapshot-controller.md "csi-snapshot-controller.md") applies a soft anti-affinity rule for hybrid nodes, preferring the controller `deployment` to run on EC2 in the same AWS Region as the Amazon EKS control plane. Co-locating the `deployment` in the same AWS Region as the Amazon EKS control plane improves latency.

## Community add-ons

The sections that follow describe differences between running compatible community add-ons on hybrid nodes compared to other Amazon EKS compute types.

## Kubernetes Metrics Server

The control plane needs to reach Metrics Server’s pod IP (or node IP if hostNetwork is enabled). Therefore, unless you run Metrics Server in hostNetwork mode, you must configure a remote pod network when creating your Amazon EKS cluster, and you must make your pod IP addresses routable. Implementing Border Gateway Protocol (BGP) with the CNI is one common way to make your pod IP addresses routable.

## cert-manager

`cert-manager` uses [webhooks](https://kubernetes.io/docs/reference/access-authn-authz/webhook/ "https://kubernetes.io/docs/reference/access-authn-authz/webhook/"). If you run `cert-manager` on hybrid nodes, your on-premises pod CIDR must be routable on your on-premises network and you must configure your EKS cluster with your remote pod network. For more information, see [Configure webhooks for hybrid nodes](hybrid-nodes-webhooks.md "hybrid-nodes-webhooks.md").
