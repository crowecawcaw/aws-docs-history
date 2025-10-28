**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Amazon EKS cluster lifecycle and configuration

This section provides in-depth guidance on the full lifecycle management of Kubernetes clusters and different ways to configure them. It covers cluster creation, monitoring cluster health, updating Kubernetes versions, and deleting clusters. It also includes advanced topics on how to configure endpoint access, enable/disable Windows support, set up private clusters, implement autoscaling, and how to enhance resilience with zonal shift for traffic redirection in multi-AZ setups.

###### Topics

- [Create an Amazon EKS Auto Mode cluster](create-cluster-auto.md "create-cluster-auto.md")
- [Create an Amazon EKS cluster](create-cluster.md "create-cluster.md")
- [Prepare for Kubernetes version upgrades and troubleshoot misconfigurations with cluster insights](cluster-insights.md "cluster-insights.md")
- [Update existing cluster to new Kubernetes version](update-cluster.md "update-cluster.md")
- [Delete a cluster](delete-cluster.md "delete-cluster.md")
- [Cluster API server endpoint](cluster-endpoint.md "cluster-endpoint.md")
- [Deploy Windows nodes on EKS clusters](windows-support.md "windows-support.md")
- [Disable Windows support](disable-windows-support.md "disable-windows-support.md")
- [Deploy private clusters with limited internet access](private-clusters.md "private-clusters.md")
- [Scale cluster compute with Karpenter and Cluster Autoscaler](autoscaling.md "autoscaling.md")
- [Learn about Amazon Application Recovery Controller (ARC) zonal shift in Amazon EKS](zone-shift.md "zone-shift.md")
- [Enable EKS zonal shift to avoid impaired Availability Zones](zone-shift-enable.md "zone-shift-enable.md")
