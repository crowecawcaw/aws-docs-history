**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Extend Amazon EKS capabilities with open source projects

These open-source projects extend the functionality of Kubernetes clusters running on or outside of AWS, including clusters managed by Amazon EKS.

## Support for software deployed to EKS

When reviewing the Amazon EKS docs, you’ll encounter references to various open-source tools and software throughout our procedures and examples. These tools include the [Kubernetes Metrics Server](https://github.com/kubernetes-sigs/metrics-server "https://github.com/kubernetes-sigs/metrics-server") and [Cert Manager.](https://cert-manager.io/ "https://cert-manager.io/")

Please note that any third-party or open-source software you choose to deploy falls outside the scope of your AWS Support Agreements. A benefit of using Kubernetes is the active open source community. We recommend working directly with the relevant open-source communities and project maintainers to establish appropriate support channels for such components. For more information, see the [graduated and incubating projects](https://www.cncf.io/projects/ "https://www.cncf.io/projects/") associated with the Cloud Native Computing Foundation (CNCF).

The Kubernetes ecosystem includes numerous projects and components that come with different levels of community support, response times, and intended use cases. When implementing these technologies alongside EKS, ensure you understand the support matrix for each component.

AWS maintains the open-source components we integrate into the EKS control plane. This includes our comprehensive security pipeline covering build verification, vulnerability scanning, validation testing, and patch management for all container images and binaries we distribute. For example, AWS is responsible for the [Kubernetes API Server](https://kubernetes.io/docs/concepts/architecture/#kube-apiserver "https://kubernetes.io/docs/concepts/architecture/#kube-apiserver"). The Kubernetes API server is covered by [Amazon EKS Service Level Agreement](https://aws.amazon.com/eks/sla/ "https://aws.amazon.com/eks/sla/"). You can use your [Amazon Web Services Support Plan](https://aws.amazon.com/premiumsupport/plans/ "https://aws.amazon.com/premiumsupport/plans/") to resolve issues with the Kubernetes API server, or get general guidance.

You need to carefully review the support offered for various Amazon EKS Add-ons. AWS add-ons are the only type of Amazon EKS add-on that are fully supported by AWS. AWS Marketplace add-ons are primarily supported by AWS Partners. Community add-ons receive basic lifecycle support from AWS. For more information, see [add-on Support.](eks-add-ons.md#addon-support "eks-add-ons.md#addon-support")

Every EKS add-ons, irrespective of the type, receives basic lifecycle support from EKS including Marketplace add-ons. Basic lifecycle support includes installing and uninstalling the add-on. For more information on the types of Amazon EKS Add-ons available and the associated levels of support, see [Scope of Support for Amazon EKS add-ons.](eks-add-ons.md#addon-support "eks-add-ons.md#addon-support") To view add-ons fully supported by AWS, see [Amazon Web Services add-ons.](workloads-add-ons-available-eks.md "workloads-add-ons-available-eks.md")

- For more information about our security practices and support boundaries, see [Security in Amazon EKS.](security.md "security.md")
- For more information about community and AWS marketplace add-ons available through Amazon EKS Add-ons, see [EKS Add-ons Support](eks-add-ons.md#addon-support "eks-add-ons.md#addon-support").

## Management tools

Related management tools for Amazon EKS and Kubernetes clusters.

### eksctl

`eksctl` is a simple CLI tool for creating clusters on Amazon EKS.

- [Project URL](https://eksctl.io/ "https://eksctl.io/")
- [Project documentation](https://eksctl.io/ "https://eksctl.io/")
- AWS open source blog: [eksctl: Amazon EKS cluster with one command](https://aws.amazon.com/blogs/opensource/eksctl-eks-cluster-one-command "https://aws.amazon.com/blogs/opensource/eksctl-eks-cluster-one-command")

### AWS controllers for Kubernetes

With AWS Controllers for Kubernetes, you can create and manage AWS resources directly from your Kubernetes cluster.

- [Project URL](https://github.com/aws-controllers-k8s/ "https://github.com/aws-controllers-k8s/")
- AWS open source blog: [AWS service operator for Kubernetes now available](https://aws.amazon.com/blogs/opensource/aws-service-operator-kubernetes-available "https://aws.amazon.com/blogs/opensource/aws-service-operator-kubernetes-available")

### Flux CD

Flux is a tool that you can use to manage your cluster configuration using Git. It uses an operator in the cluster to trigger deployments inside of Kubernetes. For more information about operators, see [OperatorHub.io](https://operatorhub.io/ "https://operatorhub.io/") on GitHub.

- [Project URL](https://fluxcd.io/ "https://fluxcd.io/")
- [Project documentation](https://docs.fluxcd.io/ "https://docs.fluxcd.io/")

### CDK for Kubernetes

With the CDK for Kubernetes (cdk8s), you can define Kubernetes apps and components using familiar programming languages. cdk8s apps synthesize into standard Kubernetes manifests, which can be applied to any Kubernetes cluster.

- [Project URL](https://cdk8s.io/ "https://cdk8s.io/")
- [Project documentation](https://cdk8s.io/docs/latest/ "https://cdk8s.io/docs/latest/")
- AWS containers blog: [Introducing cdk8s+: Intent-driven APIs for Kubernetes objects](https://aws.amazon.com/blogs/containers/introducing-cdk8s-intent-driven-apis-for-kubernetes-objects "https://aws.amazon.com/blogs/containers/introducing-cdk8s-intent-driven-apis-for-kubernetes-objects")

## Networking

Related networking projects for Amazon EKS and Kubernetes clusters.

### Amazon VPC CNI plugin for Kubernetes

Amazon EKS supports native VPC networking through the Amazon VPC CNI plugin for Kubernetes. The plugin assigns an IP address from your VPC to each Pod.

- [Project URL](https://github.com/aws/amazon-vpc-cni-k8s "https://github.com/aws/amazon-vpc-cni-k8s")
- [Project documentation](https://github.com/aws/amazon-vpc-cni-k8s/blob/master/README.md "https://github.com/aws/amazon-vpc-cni-k8s/blob/master/README.md")

### AWS Load Balancer Controller for Kubernetes

The AWS Load Balancer Controller helps manage AWS Elastic Load Balancers for a Kubernetes cluster. It satisfies Kubernetes Ingress resources by provisioning AWS Application Load Balancers. It satisfies Kubernetes service resources by provisioning AWS Network Load Balancers.

- [Project URL](https://github.com/kubernetes-sigs/aws-load-balancer-controller "https://github.com/kubernetes-sigs/aws-load-balancer-controller")
- [Project documentation](https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/ "https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/")

### ExternalDNS

ExternalDNS synchronizes exposed Kubernetes services and ingresses with DNS providers including Amazon Route 53 and AWS Service Discovery.

- [Project URL](https://github.com/kubernetes-incubator/external-dns "https://github.com/kubernetes-incubator/external-dns")
- [Project documentation](https://github.com/kubernetes-incubator/external-dns/blob/master/docs/tutorials/aws.md "https://github.com/kubernetes-incubator/external-dns/blob/master/docs/tutorials/aws.md")

## Machine learning

Related machine learning projects for Amazon EKS and Kubernetes clusters.

### Kubeflow

A machine learning toolkit for Kubernetes.

- [Project URL](https://www.kubeflow.org/ "https://www.kubeflow.org/")
- [Project documentation](https://www.kubeflow.org/docs/ "https://www.kubeflow.org/docs/")
- AWS open source blog: [Kubeflow on Amazon EKS](https://aws.amazon.com/blogs/opensource/kubeflow-amazon-eks "https://aws.amazon.com/blogs/opensource/kubeflow-amazon-eks")

## Auto Scaling

Related auto scaling projects for Amazon EKS and Kubernetes clusters.

### Cluster autoscaler

Cluster Autoscaler is a tool that automatically adjusts the size of the Kubernetes cluster based on CPU and memory pressure.

- [Project URL](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler "https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler")
- [Project documentation](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/cloudprovider/aws/README.md "https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/cloudprovider/aws/README.md")
- Amazon EKS workshop: [Cluster Autoscaler](https://www.eksworkshop.com/docs/autoscaling/compute/cluster-autoscaler/ "https://www.eksworkshop.com/docs/autoscaling/compute/cluster-autoscaler/")

### Karpenter

Karpenter is a Kubernetes Node Autoscaler built for flexibility, performance, and simplicity.

- [Project URL](https://github.com/kubernetes-sigs/karpenter "https://github.com/kubernetes-sigs/karpenter")
- [Project documentation](https://karpenter.sh/ "https://karpenter.sh/")
- Amazon EKS workshop: [Karpenter](https://www.eksworkshop.com/docs/autoscaling/compute/karpenter/ "https://www.eksworkshop.com/docs/autoscaling/compute/karpenter/")

### Escalator

Escalator is a batch or job optimized horizontal autoscaler for Kubernetes.

- [Project URL](https://github.com/atlassian/escalator "https://github.com/atlassian/escalator")
- [Project documentation](https://github.com/atlassian/escalator/blob/master/docs/README.md "https://github.com/atlassian/escalator/blob/master/docs/README.md")

## Monitoring

Related monitoring projects for Amazon EKS and Kubernetes clusters.

### Prometheus

Prometheus is an open-source systems monitoring and alerting toolkit.

- [Project URL](https://prometheus.io/ "https://prometheus.io/")
- [Project documentation](https://prometheus.io/docs/introduction/overview/ "https://prometheus.io/docs/introduction/overview/")
- Amazon EKS workshop: [https://eksworkshop.com/intermediate/240_monitoring/](https://eksworkshop.com/intermediate/240_monitoring/ "https://eksworkshop.com/intermediate/240_monitoring/")

## Continuous integration / continuous deployment

Related CI/CD projects for Amazon EKS and Kubernetes clusters.

### Jenkins X

CI/CD solution for modern cloud applications on Amazon EKS and Kubernetes clusters.

- [Project URL](https://jenkins-x.io/ "https://jenkins-x.io/")
- [Project documentation](https://jenkins-x.io/docs/ "https://jenkins-x.io/docs/")
