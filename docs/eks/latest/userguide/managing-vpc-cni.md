**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Assign IPs to Pods with the Amazon VPC CNI

###### Tip

With Amazon EKS Auto Mode, you don’t need to install or upgrade networking add-ons. Auto Mode includes pod networking and load balancing capabilities.

For more information, see [Automate cluster infrastructure with EKS Auto Mode](automode.md "automode.md").

The Amazon VPC CNI plugin for Kubernetes add-on is deployed on each Amazon EC2 node in your Amazon EKS cluster. The add-on creates [elastic network interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") and attaches them to your Amazon EC2 nodes. The add-on also assigns a private `IPv4` or `IPv6` address from your VPC to each Pod.

A version of the add-on is deployed with each Fargate node in your cluster, but you don’t update it on Fargate nodes. Other compatible CNI plugins are available for use on Amazon EKS clusters, but this is the only CNI plugin supported by Amazon EKS for nodes that run on AWS infrastructure. For more information about the other compatible CNI plugins, see [Alternate CNI plugins for Amazon EKS clusters](alternate-cni-plugins.md "alternate-cni-plugins.md"). The VPC CNI isn’t supported for use with hybrid nodes. For more information about your CNI options for hybrid nodes, see [Configure CNI for hybrid nodes](hybrid-nodes-cni.md "hybrid-nodes-cni.md").

The following table lists the latest available version of the Amazon EKS add-on type for each Kubernetes version.

## Amazon VPC CNI versions

| Kubernetes version | Amazon EKS type of VPC CNI version |
| ------------------ | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.34               | v1.20.4-eksbuild.1                 |
| 1.33               | v1.20.4-eksbuild.1                 |
| 1.32               | v1.20.4-eksbuild.1                 |
| 1.31               | v1.20.4-eksbuild.1                 |
| 1.30               | v1.20.4-eksbuild.1                 |
| 1.29               | v1.20.4-eksbuild.1                 |
| 1.28               | v1.20.4-eksbuild.1                 | ###### Important If you’re self-managing this add-on, the versions in the table might not be the same as the available self-managed versions. For more information about updating the self-managed type of this add-on, see [Update the Amazon VPC CNI (self-managed add-on)](vpc-add-on-self-managed-update.md "vpc-add-on-self-managed-update.md"). ###### Important To upgrade to VPC CNI v1.12.0 or later, you must upgrade to VPC CNI v1.7.0 first. We recommend that you update one minor version at a time. ## Considerations The following are considerations for using the feature. <br>• Versions are specified as `major-version.minor-version.patch-version-eksbuild.build-number`. <br>• Check version compatibility for each feature. Some features of each release of the Amazon VPC CNI plugin for Kubernetes require certain Kubernetes versions. When using different Amazon EKS features, if a specific version of the add-on is required, then it’s noted in the feature documentation. Unless you have a specific reason for running an earlier version, we recommend running the latest version. |
