

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Extend Amazon EKS capabilities with open source projects
<a name="related-projects"></a>

These open-source projects extend the functionality of Kubernetes clusters running on or outside of AWS, including clusters managed by Amazon EKS.

## Support for software deployed to EKS
<a name="oss-scope"></a>

When reviewing the Amazon EKS docs, you’ll encounter references to various open-source tools and software throughout our procedures and examples. These tools include the [Kubernetes Metrics Server](https://github.com/kubernetes-sigs/metrics-server) and [Cert Manager.](https://cert-manager.io/) 

Please note that any third-party or open-source software you choose to deploy falls outside the scope of your AWS Support Agreements. A benefit of using Kubernetes is the active open source community. We recommend working directly with the relevant open-source communities and project maintainers to establish appropriate support channels for such components. For more information, see the [graduated and incubating projects](https://www.cncf.io/projects/) associated with the Cloud Native Computing Foundation (CNCF).

The Kubernetes ecosystem includes numerous projects and components that come with different levels of community support, response times, and intended use cases. When implementing these technologies alongside EKS, ensure you understand the support matrix for each component.

 AWS maintains the open-source components we integrate into the EKS control plane. This includes our comprehensive security pipeline covering build verification, vulnerability scanning, validation testing, and patch management for all container images and binaries we distribute. For example, AWS is responsible for the [Kubernetes API Server](https://kubernetes.io/docs/concepts/architecture/#kube-apiserver). The Kubernetes API server is covered by [Amazon EKS Service Level Agreement](https://aws.amazon.com/eks/sla/). You can use your [Amazon Web Services Support Plan](https://aws.amazon.com/premiumsupport/plans/) to resolve issues with the Kubernetes API server, or get general guidance.

You need to carefully review the support offered for various Amazon EKS Add-ons. AWS add-ons are the only type of Amazon EKS add-on that are fully supported by AWS. AWS Marketplace add-ons are primarily supported by AWS Partners. Community add-ons receive basic lifecycle support from AWS. For more information, see [add-on Support.](eks-add-ons.md#addon-support) 

Every EKS add-on, irrespective of the type, receives basic lifecycle support from EKS including Marketplace add-ons. Basic lifecycle support includes installing and uninstalling the add-on. For more information on the types of Amazon EKS Add-ons available and the associated levels of support, see [Scope of Support for Amazon EKS add-ons.](eks-add-ons.md#addon-support) To view add-ons fully supported by AWS, see [Amazon Web Services add-ons.](workloads-add-ons-available-eks.md) 
+ For more information about our security practices and support boundaries, see [Security in Amazon EKS.](security.md) 
+ For more information about community and AWS marketplace add-ons available through Amazon EKS Add-ons, see [EKS Add-ons Support](eks-add-ons.md#addon-support).

## Management tools
<a name="related-management-tools"></a>

Related management tools for Amazon EKS and Kubernetes clusters.

### eksctl
<a name="related-eksctl"></a>

 `eksctl` is a simple CLI tool for creating clusters on Amazon EKS.
+  [Project URL](https://eksctl.io/) 
+  [Project documentation](https://eksctl.io/) 
+  AWS open source blog: [eksctl: Amazon EKS cluster with one command](https://aws.amazon.com/blogs/opensource/eksctl-eks-cluster-one-command) 

### AWS Controllers for Kubernetes
<a name="related-aws-controllers"></a>

With AWS Controllers for Kubernetes, you can create and manage AWS resources directly from your Kubernetes cluster.

Available in [EKS Capabilities](ack.md).
+  [Project URL](https://aws-controllers-k8s.github.io/docs/) 
+  AWS open source blog: [AWS service operator for Kubernetes now available](https://aws.amazon.com/blogs/opensource/aws-service-operator-kubernetes-available) 

### kro (Kube Resource Orchestrator)
<a name="related-kro"></a>

kro enables you to create custom Kubernetes APIs that compose multiple resources into higher-level abstractions. Platform teams can define reusable patterns with guardrails, while application teams use simple, high-level APIs to provision and manage resources.

Available in [EKS Capabilities](kro.md).
+  [Project URL](https://kro.run/) 
+  [Project documentation](https://kro.run/docs/) 

### Argo CD
<a name="related-argocd"></a>

Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes. It continuously monitors your Git repositories and automatically syncs changes to your clusters.

Available in [EKS Capabilities](argocd.md).
+  [Project URL](https://argo-cd.readthedocs.io/) 
+  [Project documentation](https://argo-cd.readthedocs.io/en/stable/) 

### Flux CD
<a name="related-flux-cd"></a>

Flux is a tool that you can use to manage your cluster configuration using Git. It uses an operator in the cluster to trigger deployments inside of Kubernetes. For more information about operators, see [OperatorHub.io](https://operatorhub.io/) on GitHub.
+  [Project URL](https://fluxcd.io/) 
+  [Project documentation](https://docs.fluxcd.io/) 

### CDK for Kubernetes
<a name="related-cdk"></a>

With the CDK for Kubernetes (cdk8s), you can define Kubernetes apps and components using familiar programming languages. cdk8s apps synthesize into standard Kubernetes manifests, which can be applied to any Kubernetes cluster.
+  [Project URL](https://cdk8s.io/) 
+  [Project documentation](https://cdk8s.io/docs/latest/) 
+  AWS containers blog: [Introducing cdk8s\+: Intent-driven APIs for Kubernetes objects](https://aws.amazon.com/blogs/containers/introducing-cdk8s-intent-driven-apis-for-kubernetes-objects) 

## Networking
<a name="related-networking"></a>

Related networking projects for Amazon EKS and Kubernetes clusters.

### Amazon VPC CNI plugin for Kubernetes
<a name="related-vpc-cni-k8s"></a>

Amazon EKS supports native VPC networking through the Amazon VPC CNI plugin for Kubernetes. The plugin assigns an IP address from your VPC to each Pod.
+  [Project URL](https://github.com/aws/amazon-vpc-cni-k8s) 
+  [Project documentation](https://github.com/aws/amazon-vpc-cni-k8s/blob/master/README.md) 

### AWS Load Balancer Controller for Kubernetes
<a name="related-alb-ingress-controller"></a>

The AWS Load Balancer Controller helps manage AWS Elastic Load Balancers for a Kubernetes cluster. It satisfies Kubernetes Ingress resources by provisioning AWS Application Load Balancers. It satisfies Kubernetes service resources by provisioning AWS Network Load Balancers.
+  [Project URL](https://github.com/kubernetes-sigs/aws-load-balancer-controller) 
+  [Project documentation](https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/) 

### ExternalDNS
<a name="related-externaldns"></a>

ExternalDNS synchronizes exposed Kubernetes services and ingresses with DNS providers including Amazon Route 53 and AWS Service Discovery.
+  [Project URL](https://github.com/kubernetes-incubator/external-dns) 
+  [Project documentation](https://github.com/kubernetes-incubator/external-dns/blob/master/docs/tutorials/aws.md) 

## Machine learning
<a name="related-machine-learning"></a>

Related machine learning projects for Amazon EKS and Kubernetes clusters.

### Kubeflow
<a name="related-kubeflow"></a>

A machine learning toolkit for Kubernetes.
+  [Project URL](https://www.kubeflow.org/) 
+  [Project documentation](https://www.kubeflow.org/docs/) 
+  AWS open source blog: [Kubeflow on Amazon EKS](https://aws.amazon.com/blogs/opensource/kubeflow-amazon-eks) 

## Auto Scaling
<a name="related-auto-scaling"></a>

Related auto scaling projects for Amazon EKS and Kubernetes clusters.

### Cluster autoscaler
<a name="related-cluster-autoscaler"></a>

Cluster Autoscaler is a tool that automatically adjusts the size of the Kubernetes cluster based on CPU and memory pressure.
+  [Project URL](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler) 
+  [Project documentation](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/cloudprovider/aws/README.md) 
+ Amazon EKS workshop: [Cluster Autoscaler](https://www.eksworkshop.com/docs/autoscaling/compute/cluster-autoscaler/) 

### Karpenter
<a name="related-karpenter"></a>

Karpenter is a Kubernetes Node Autoscaler built for flexibility, performance, and simplicity.
+  [Project URL](https://github.com/kubernetes-sigs/karpenter) 
+  [Project documentation](https://karpenter.sh/) 
+ Amazon EKS workshop: [Karpenter](https://www.eksworkshop.com/docs/fundamentals/compute/karpenter/) 

### Escalator
<a name="related-escalator"></a>

Escalator is a batch or job optimized horizontal autoscaler for Kubernetes.
+  [Project URL](https://github.com/atlassian/escalator) 
+  [Project documentation](https://github.com/atlassian/escalator/blob/master/docs/README.md) 

## Monitoring
<a name="related-monitoring"></a>

Related monitoring projects for Amazon EKS and Kubernetes clusters.

### Prometheus
<a name="related-prometheus"></a>

Prometheus is an open-source systems monitoring and alerting toolkit.
+  [Project URL](https://prometheus.io/) 
+  [Project documentation](https://prometheus.io/docs/introduction/overview/) 
+ Amazon EKS workshop: [https://eksworkshop.com/intermediate/240_monitoring/](https://eksworkshop.com/intermediate/240_monitoring/) 

## Continuous integration / continuous deployment
<a name="related-cicd"></a>

Related imperative CI/CD projects for Amazon EKS and Kubernetes clusters.

### Jenkins X
<a name="related-jenkinsx"></a>

CI/CD solution for modern cloud applications on Amazon EKS and Kubernetes clusters.
+  [Project URL](https://jenkins-x.io/) 
+  [Project documentation](https://jenkins-x.io/docs/) 