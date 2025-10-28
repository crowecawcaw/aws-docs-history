# Integrating with Amazon EKS cost monitoring

Amazon Managed Service for Prometheus integrates with Amazon Elastic Kubernetes Service (Amazon EKS) cost monitoring (with Kubecost) to perform
cost allocation calculations and provide insights into optimizing your Kubernetes
clusters. Using Amazon Managed Service for Prometheus with Kubecost, you can reliably scale your cost monitoring to
support larger clusters.

Integrating with Kubecost gives you granular visibility into your Amazon EKS cluster costs.
You can aggregate costs by the majority of Kubernetes contexts, from the container level
up to the cluster level, and even multi-cluster level. You can generate reports across
containers or clusters to track costs for show back or chargeback purposes.

The following give instructions for integrating with Kubecost in a single- or
multi-cluster scenario:

- **Single-cluster integration** – To learn how to
  integrate Amazon EKS cost monitoring with a single cluster, see the AWS
  blog post [Integrating
  Kubecost with Amazon Managed Service for Prometheus](https://aws.amazon.com/blogs/mt/integrating-kubecost-with-amazon-managed-service-for-prometheus/ "https://aws.amazon.com/blogs/mt/integrating-kubecost-with-amazon-managed-service-for-prometheus/").
- **Multi-cluster integration** – To learn how to
  integrate Amazon EKS cost monitoring with a multiple clusters, see the
  AWS blog post [Multi-cluster cost monitoring for Amazon EKS using Kubecost and Amazon Managed Service for Prometheus](https://aws.amazon.com/blogs/containers/multi-cluster-cost-monitoring-using-kubecost-with-amazon-eks-and-amazon-managed-service-for-prometheus/ "https://aws.amazon.com/blogs/containers/multi-cluster-cost-monitoring-using-kubecost-with-amazon-eks-and-amazon-managed-service-for-prometheus/").

###### Note

For more information about using Kubecost, see [Cost
monitoring](../../../eks/latest/userguide/cost-monitoring.md "../../../eks/latest/userguide/cost-monitoring.md") in the _Amazon EKS User Guide_.
