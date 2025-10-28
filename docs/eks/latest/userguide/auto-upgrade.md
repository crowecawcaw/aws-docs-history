**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Update the Kubernetes Version of an EKS Auto Mode cluster

This topic explains how to update the Kubernetes version of your Auto Mode cluster. Auto Mode simplifies the version update process by handling the coordination of control plane updates with node replacements, while maintaining workload availability through pod disruption budgets.

When upgrading an Auto Mode cluster, many components that traditionally required manual updates are now managed as part of the service. Understanding the automated aspects of the upgrade process and your responsibilities helps ensure a smooth version transition for your cluster.

## Learn about updates with EKS Auto Mode

After you initiate a control plane upgrade, EKS Auto Mode will upgrade nodes in your cluster. As nodes expire, EKS Auto Mode will replace them with new nodes. The new nodes have the corresponding new Kubernetes version. EKS Auto Mode observes pod disruption budgets when upgrading nodes.

Additionally, you no longer need to update components like:

- Amazon VPC CNI
- AWS Load Balancer Controller
- CoreDNS
- `kube-proxy`
- Karpenter
- AWS EBS CSI driver

EKS Auto Mode replaces these components with service functionality.

You are still responsible for updating:

- Apps and workloads deployed to your cluster
- Self-managed add-ons and controllers
- Amazon EKS Add-ons
  - Learn how to [Update an Amazon EKS add-on](updating-an-add-on.md "updating-an-add-on.md")

Learn [Best Practices for Cluster Upgrades](../best-practices/cluster-upgrades.md "../best-practices/cluster-upgrades.md")

## Start Cluster Update

To start a cluster update, see [Update existing cluster to new Kubernetes version](update-cluster.md "update-cluster.md").
