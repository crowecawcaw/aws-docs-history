

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Amazon EKS cluster lifecycle and configuration
<a name="clusters"></a>

This section provides in-depth guidance on the full lifecycle management of Kubernetes clusters and different ways to configure them. It covers cluster creation, monitoring cluster health, updating Kubernetes versions, and deleting clusters. It also includes advanced topics on how to configure endpoint access, enable/disable Windows support, set up private clusters, implement autoscaling, and how to enhance resilience with zonal shift for traffic redirection in multi-AZ setups.

**Topics**
+ [Create an Amazon EKS Auto Mode cluster](create-cluster-auto.md)
+ [Create an Amazon EKS cluster](create-cluster.md)
+ [Amazon EKS Provisioned Control Plane](eks-provisioned-control-plane.md)
+ [Advanced Kubernetes control plane configuration](control-plane-configuration.md)
+ [Prepare for Kubernetes version upgrades and troubleshoot misconfigurations with cluster insights](cluster-insights.md)
+ [Update existing cluster to new Kubernetes version](update-cluster.md)
+ [Roll back a cluster to a previous Kubernetes version](rollback-cluster.md)
+ [Delete a cluster](delete-cluster.md)
+ [Cluster API server endpoint](cluster-endpoint.md)
+ [Deploy Windows nodes on EKS clusters](windows-support.md)
+ [Disable Windows support](disable-windows-support.md)
+ [Deploy private clusters with limited internet access](private-clusters.md)
+ [Configuring control plane egress routing](control-plane-egress.md)
+ [Scale cluster compute with Karpenter and Cluster Autoscaler](autoscaling.md)
+ [Learn about Amazon Application Recovery Controller (ARC) zonal shift in Amazon EKS](zone-shift.md)
+ [Enable EKS zonal shift to avoid impaired Availability Zones](zone-shift-enable.md)