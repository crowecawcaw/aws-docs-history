# Quick Start setup for Container Insights on Amazon EKS and Kubernetes

###### Important

If you are installing Container Insights on an Amazon EKS cluster, we recommend that
you use the Amazon CloudWatch Observability EKS add-on for the installation, instead of using
the instructions in this section. Additionally, to retrieve accelerated computing
networks, you must use the Amazon CloudWatch Observability EKS add-on. For more information and
instructions, see [Quick start with the Amazon CloudWatch Observability EKS add-on](Container-Insights-setup-EKS-addon.md "Container-Insights-setup-EKS-addon.md").

To complete the setup of Container Insights, you can follow the quick start
instructions in this section. If you are installing in an Amazon EKS cluster and you use the
instructions in this section on or after November 6, 2023, you install Container
Insights with enhanced observability for Amazon EKS in the cluster.

###### Important

Before completing the steps in this section, you must have verified the
prerequisites including IAM permissions. For more information, see [Verifying prerequisites for Container Insights in CloudWatch](Container-Insights-prerequisites.md "Container-Insights-prerequisites.md").

Alternatively, you can instead follow the instructions in the following two
sections, [Setting up the CloudWatch agent to collect cluster metrics](Container-Insights-setup-metrics.md "Container-Insights-setup-metrics.md") and [Send logs to CloudWatch Logs](Container-Insights-EKS-logs.md "Container-Insights-EKS-logs.md").
Those sections provide more configuration details on how the CloudWatch agent works with Amazon EKS
and Kubernetes, but require you to perform more installation steps.

With the original version of Container Insights, metrics collected and logs ingested
are charged as custom metrics. With Container Insights with enhanced observability for
Amazon EKS, Container Insights metrics and logs are charged per observation instead of being
charged per metric stored or log ingested. For more information about CloudWatch pricing, see
[Amazon CloudWatch
Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

###### Note

Amazon has now launched Fluent Bit as the default log solution for Container
Insights with significant performance gains. We recommend that you use Fluent Bit
instead of Fluentd.

## Quick Start with the CloudWatch agent operator and Fluent Bit

There are two configurations for Fluent Bit: an optimized version and a version
that provides an experience more similar to Fluentd. The Quick Start configuration
uses the optimized version. For more details about the Fluentd-compatible
configuration, see [Set up Fluent Bit as a DaemonSet to send logs to CloudWatch Logs](Container-Insights-setup-logs-FluentBit.md "Container-Insights-setup-logs-FluentBit.md").

The CloudWatch agent operator is an additional container that gets installed to an Amazon EKS
cluster. It is modeled after the OpenTelemetry Operator for Kubernetes. The operator
manages the lifecycle of Kubernetes resources in a cluster. It installs the CloudWatch
Agent, DCGM Exporter (NVIDIA), and the AWS Neuron Monitor on an Amazon EKS cluster and
manages them. Fluent Bit and the CloudWatch Agent for Windows are installed directly to an
Amazon EKS cluster without the operator managing them.

For a more secure and feature-rich certificate authority solution, the CloudWatch agent
operator requires cert-manager, a widely-adopted solution for TLS certificate
management in Kubernetes. Using cert-manager simplifies the process of obtaining,
renewing, managing and using these certificates. It ensures that certificates are
valid and up to date, and attempts to renew certificates at a configured time before
expiry. cert-manager also facilitates issuing certificates from a variety of supported
sources, including AWS Certificate Manager Private Certificate Authority.

###### To deploy Container Insights using the quick start

1. Install cert-manager if it is not already installed in the cluster. For more
   information, see [cert-manager Installation](https://cert-manager.io/docs/installation/ "https://cert-manager.io/docs/installation/").
2. Install the custom resource definitions (CRD) by entering the following
   commmand.

```
curl https://raw.githubusercontent.com/aws-samples/amazon-cloudwatch-container-insights/main/k8s-quickstart/cwagent-custom-resource-definitions.yaml | kubectl apply --server-side -f -
```

3. Install the operator by entering the following command. Replace
   `my-cluster-name` with the name of your Amazon EKS or
   Kubernetes cluster, and replace `my-cluster-region` with
   the name of the Region where the logs are published. We recommend that you use the
   same Region where your cluster is deployed to reduce the AWS outbound data
   transfer costs.

```
ClusterName=`my-cluster-name`
RegionName=`my-cluster-region`
curl https://raw.githubusercontent.com/aws-samples/amazon-cloudwatch-container-insights/main/k8s-quickstart/cwagent-operator-rendered.yaml | sed 's/{{cluster_name}}/'${ClusterName}'/g;s/{{region_name}}/'${RegionName}'/g' | kubectl apply -f -
```

For example, to deploy Container Insights on the cluster named
`MyCluster` and publish the logs and metrics to US West (Oregon),
enter the following command.

```
ClusterName='MyCluster'
RegionName='us-west-2'
curl https://raw.githubusercontent.com/aws-samples/amazon-cloudwatch-container-insights/main/k8s-quickstart/cwagent-operator-rendered.yaml | sed 's/{{cluster_name}}/'${ClusterName}'/g;s/{{region_name}}/'${RegionName}'/g' | kubectl apply -f -
```

**Migrating from Container Insights**

If you already have Container Insights configured in an Amazon EKS cluster and you want
to migrate to Container Insights with enhanced observability for Amazon EKS, see [Upgrading to Container Insights with enhanced observability for Amazon EKS in CloudWatch](Container-Insights-upgrade-enhanced.md "Container-Insights-upgrade-enhanced.md")

**Deleting Container Insights**

If you want to remove Container Insights after using the quick start setup, enter
the following commands.

```
ClusterName=`my-cluster-name`
RegionName=`my-cluster-region`
curl https://raw.githubusercontent.com/aws-samples/amazon-cloudwatch-container-insights/main/k8s-quickstart/cwagent-operator-rendered.yaml | sed 's/{{cluster_name}}/'${ClusterName}'/g;s/{{region_name}}/'${RegionName}'/g' | kubectl delete -f -
curl https://raw.githubusercontent.com/aws-samples/amazon-cloudwatch-container-insights/main/k8s-quickstart/cwagent-custom-resource-definitions.yaml | kubectl delete -f -
```
