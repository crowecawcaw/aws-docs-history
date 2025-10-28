# Clusters

This chapter covers creating and configuring EKS clusters using eksctl. It also includes add-ons and EKS Auto Mode.

## Topics:

- [EKS Access Entries](access-entries.md "access-entries.md")
  - Simplify Kubernetes RBAC management by replacing aws-auth ConfigMap with EKS access entries
  - Migrate existing IAM identity mappings from aws-auth ConfigMap to access entries
  - Configure cluster authentication modes and control cluster creator admin permissions

- [Default add-on updates](addon-upgrade.md "addon-upgrade.md")
  - Keep clusters secure by updating default EKS add-ons on older clusters

- [Addons](addons.md "addons.md")
  - Automate routine tasks for installing, updating, and removing add-ons.
  - Amazon EKS Add-ons include AWS add-ons, open source community add-ons, and marketplace add-ons.

- [EKS Auto Mode](auto-mode.md "auto-mode.md")
  - Reduce operational overhead by letting AWS manage your EKS infrastructure
  - Configure custom node pools instead of default general-purpose and system pools
  - Convert existing EKS clusters to use Auto Mode

- [CloudWatch logging](cloudwatch-cluster-logging.md "cloudwatch-cluster-logging.md")
  - Troubleshoot cluster issues by enabling logs for specific EKS control plane components
  - Configure log retention periods for EKS cluster logs
  - Modify existing cluster logging settings using eksctl commands

- [Cluster upgrades](cluster-upgrade.md "cluster-upgrade.md")
  - Maintain security and stability by safely upgrading EKS control plane versions
  - Roll out upgrades across nodegroups by replacing old groups with new ones
  - Update default cluster add-ons

- [Creating and managing clusters](creating-and-managing-clusters.md "creating-and-managing-clusters.md")
  - Start quickly with basic EKS clusters using default managed nodegroups
  - Create customized clusters using config files with specific configurations
  - Deploy clusters in existing VPCs with private networking and custom IAM policies

- [Customizing kubelet configuration](customizing-the-kubelet.md "customizing-the-kubelet.md")
  - Prevent node resource starvation by configuring kubelet and system daemon reservations
  - Customize eviction thresholds for memory and filesystem availability
  - Enable or disable specific kubelet feature gates across node groups

- [Registering non-EKS clusters with EKS Connector](eks-connector.md "eks-connector.md")
  - Centralize management of hybrid Kubernetes deployments through EKS Console
  - Configure IAM roles and permissions for external cluster access
  - Remove external clusters and cleanup associated AWS resources

- [EKS Fully-Private Cluster](eks-private-cluster.md "eks-private-cluster.md")
  - Meet security requirements with fully-private EKS clusters having no outbound internet access
  - Configure private access to AWS services through VPC endpoints
  - Create and manage private nodegroups with explicit networking settings

- [Karpenter Support](eksctl-karpenter.md "eksctl-karpenter.md")
  - Automate node provisioning
  - Create custom Karpenter provisioner configurations
  - Set up Karpenter with spot instance interruption handling

- [Enabling Access for Amazon EMR](emr-access.md "emr-access.md")
  - Create IAM identity mapping between EMR and EKS cluster

- [EKS Fargate Support](fargate.md "fargate.md")
  - Define custom Fargate profiles for pod scheduling
  - Manage Fargate profiles through creation and configuration updates

- [Non eksctl-created clusters](unowned-clusters.md "unowned-clusters.md")
  - Standardize management of clusters created outside eksctl
  - Use eksctl commands on existing non-eksctl clusters

- [Support for Zonal Shift in EKS clusters](zonal-shift.md "zonal-shift.md")
  - Improve application availability by enabling rapid zone failover capabilities
  - Configure zonal shift on new EKS cluster deployments
  - Enable zonal shift features on existing EKS clusters
