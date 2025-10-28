**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Manage networking add-ons for Amazon EKS clusters

Several networking add-ons are available for your Amazon EKS cluster.

## Built-in add-ons

###### Note

**When you create an EKS cluster:**

- **Using the AWS Console**: The built-in add-ons (like CoreDNS, kube-proxy, etc.) are automatically installed as Amazon EKS Add-ons. These can be easily configured and updated through the AWS Console, CLI, or SDKs.
- **Using other methods** (CLI, SDKs, etc.): The same built-in add-ons are installed as self-managed versions that run as regular Kubernetes deployments. These require manual configuration and updates since they can’t be managed through AWS tools.
  We recommend using Amazon EKS Add-ons rather than self-managed versions to simplify add-on management and enable centralized configuration and updates through AWS services.

**Amazon VPC CNI plugin for Kubernetes**

This CNI add-on creates elastic network interfaces and attaches them to your Amazon EC2 nodes. The add-on also assigns a private `IPv4` or `IPv6` address from your VPC to each Pod and service. This add-on is installed, by default, on your cluster. For more information, see [Assign IPs to Pods with the Amazon VPC CNI](managing-vpc-cni.md "managing-vpc-cni.md"). If you are using hybrid nodes, the VPC CNI is still installed by default but it is prevented from running on your hybrid nodes with an anti-affinity rule. For more information about your CNI options for hybrid nodes, see [Configure CNI for hybrid nodes](hybrid-nodes-cni.md "hybrid-nodes-cni.md").

**CoreDNS**

CoreDNS is a flexible, extensible DNS server that can serve as the Kubernetes cluster DNS. CoreDNS provides name resolution for all Pods in the cluster. This add-on is installed, by default, on your cluster. For more information, see [Manage CoreDNS for DNS in Amazon EKS clusters](managing-coredns.md "managing-coredns.md").

**`kube-proxy`**

This add-on maintains network rules on your Amazon EC2 nodes and enables network communication to your Pods. This add-on is installed, by default, on your cluster. For more information, see [Manage kube-proxy in Amazon EKS clusters](managing-kube-proxy.md "managing-kube-proxy.md").

## Optional AWS networking add-ons

**AWS Load Balancer Controller**

When you deploy Kubernetes service objects of type `loadbalancer`, the controller creates AWS Network Load Balancers . When you create Kubernetes ingress objects, the controller creates AWS Application Load Balancers. We recommend using this controller to provision Network Load Balancers, rather than using the [legacy Cloud Provider](https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/service/annotations/#legacy-cloud-provider "https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/service/annotations/#legacy-cloud-provider") controller built-in to Kubernetes. For more information, see the [AWS Load Balancer Controller](https://kubernetes-sigs.github.io/aws-load-balancer-controller "https://kubernetes-sigs.github.io/aws-load-balancer-controller") documentation.

**AWS Gateway API Controller**

This controller lets you connect services across multiple Kubernetes clusters using the [Kubernetes gateway API](https://gateway-api.sigs.k8s.io/ "https://gateway-api.sigs.k8s.io/"). The controller connects Kubernetes services running on Amazon EC2 instances, containers, and serverless functions by using the [Amazon VPC Lattice](../../../vpc-lattice/latest/ug/what-is-vpc-service-network.md "../../../vpc-lattice/latest/ug/what-is-vpc-service-network.md") service. For more information, see the [AWS Gateway API Controller](https://www.gateway-api-controller.eks.aws.dev/ "https://www.gateway-api-controller.eks.aws.dev/") documentation.

For more information about add-ons, see [Amazon EKS add-ons](eks-add-ons.md "eks-add-ons.md").
