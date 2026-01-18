**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Upgrade hybrid nodes for your cluster

The guidance for upgrading hybrid nodes is similar to self-managed Amazon EKS nodes that run in Amazon EC2. We recommend that you create new hybrid nodes on your target Kubernetes version, gracefully migrate your existing applications to the hybrid nodes on the new Kubernetes version, and remove the hybrid nodes on the old Kubernetes version from your cluster. Be sure to review the [Amazon EKS Best Practices](../best-practices/cluster-upgrades.md "../best-practices/cluster-upgrades.md") for upgrades before initiating an upgrade. Amazon EKS Hybrid Nodes have the same [Kubernetes version support](kubernetes-versions.md "kubernetes-versions.md") for Amazon EKS clusters with cloud nodes, including standard and extended support.

Amazon EKS Hybrid Nodes follow the same [version skew policy](https://kubernetes.io/releases/version-skew-policy/#supported-version-skew "https://kubernetes.io/releases/version-skew-policy/#supported-version-skew") for nodes as upstream Kubernetes. Amazon EKS Hybrid Nodes cannot be on a newer version than the Amazon EKS control plane, and hybrid nodes may be up to three Kubernetes minor versions older than the Amazon EKS control plane minor version.

If you do not have spare capacity to create new hybrid nodes on your target Kubernetes version for a cutover migration upgrade strategy, you can alternatively use the Amazon EKS Hybrid Nodes CLI (`nodeadm`) to upgrade the Kubernetes version of your hybrid nodes in-place.

###### Important

If you are upgrading your hybrid nodes in-place with `nodeadm`, there is downtime for the node during the process where the older version of the Kubernetes components are shut down and the new Kubernetes version components are installed and started.

## Prerequisites

Before upgrading, make sure you have completed the following prerequisites.

- The target Kubernetes version for your hybrid nodes upgrade must be equal to or less than the Amazon EKS control plane version.
- If you are following a cutover migration upgrade strategy, the new hybrid nodes you are installing on your target Kubernetes version must meet the [Prerequisite setup for hybrid nodes](hybrid-nodes-prereqs.md "hybrid-nodes-prereqs.md") requirements. This includes having IP addresses within the Remote Node Network CIDR you passed during Amazon EKS cluster creation.
- For both cutover migration and in-place upgrades, the hybrid nodes must have access to the [required domains](hybrid-nodes-networking.md#hybrid-nodes-networking-on-prem "hybrid-nodes-networking.md#hybrid-nodes-networking-on-prem") to pull the new versions of the hybrid nodes dependencies.
- You must have kubectl installed on your local machine or instance you are using to interact with your Amazon EKS Kubernetes API endpoint.
- The version of your CNI must support the Kubernetes version you are upgrading to. If it does not, upgrade your CNI version before upgrading your hybrid nodes. See [Configure CNI for hybrid nodes](hybrid-nodes-cni.md "hybrid-nodes-cni.md") for more information.

## Cutover migration (blue-green) upgrades

_Cutover migration upgrades_ refer to the process of creating new hybrid nodes on new hosts with your target Kubernetes version, gracefully migrating your existing applications to the new hybrid nodes on your target Kubernetes version, and removing the hybrid nodes on the old Kubernetes version from your cluster. This strategy is also called a blue-green migration.

1. Connect your new hosts as hybrid nodes following the [Connect hybrid nodes](hybrid-nodes-join.md "hybrid-nodes-join.md") steps. When running the `nodeadm install` command, use your target Kubernetes version.
2. Enable communication between the new hybrid nodes on the target Kubernetes version and your hybrid nodes on the old Kubernetes version. This configuration allows pods to communicate with each other while you are migrating your workload to the hybrid nodes on the target Kubernetes version.
3. Confirm your hybrid nodes on your target Kubernetes version successfully joined your cluster and have status Ready.
4. Use the following command to mark each of the nodes that you want to remove as unschedulable. This is so that new pods aren’t scheduled or rescheduled on the nodes that you are replacing. For more information, see [kubectl cordon](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_cordon/ "https://kubernetes.io/docs/reference/kubectl/generated/kubectl_cordon/") in the Kubernetes documentation. Replace `NODE_NAME` with the name of the hybrid nodes on the old Kubernetes version.

```
 kubectl cordon <replaceable>NODE_NAME</replaceable>
```

You can identify and cordon all of the nodes of a particular Kubernetes version (in this case, `1.28`) with the following code snippet.

```
 K8S_VERSION=1.28
for node in $(kubectl get nodes -o json | jq --arg K8S_VERSION "$K8S_VERSION" -r '.items[] | select(.status.nodeInfo.kubeletVersion | match("\($K8S_VERSION)")).metadata.name')
do
    echo "Cordoning $node"
    kubectl cordon $node
done
```

5. If your current deployment is running fewer than two CoreDNS replicas on your hybrid nodes, scale out the deployment to at least two replicas. We recommend that you run at least two CoreDNS replicas on hybrid nodes for resiliency during normal operations.

```
 kubectl scale deployments/coredns --replicas=2 -n kube-system
```

6. Drain each of the hybrid nodes on the old Kubernetes version that you want to remove from your cluster with the following command. For more information on draining nodes, see [Safely Drain a Node](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/ "https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/") in the Kubernetes documentation. Replace `NODE_NAME` with the name of the hybrid nodes on the old Kubernetes version.

```
 kubectl drain <replaceable>NODE_NAME</replaceable> --ignore-daemonsets --delete-emptydir-data
```

You can identify and drain all of the nodes of a particular Kubernetes version (in this case, `1.28`) with the following code snippet.

```
 K8S_VERSION=1.28
for node in $(kubectl get nodes -o json | jq --arg K8S_VERSION "$K8S_VERSION" -r '.items[] | select(.status.nodeInfo.kubeletVersion | match("\($K8S_VERSION)")).metadata.name')
do
    echo "Draining $node"
    kubectl drain $node --ignore-daemonsets --delete-emptydir-data
done
```

7. You can use `nodeadm` to stop and remove the hybrid nodes artifacts from the host. You must run `nodeadm` with a user that has root/sudo privileges. By default, `nodeadm uninstall` will not proceed if there are pods remaining on the node. For more information see [Hybrid nodes nodeadm reference](hybrid-nodes-nodeadm.md "hybrid-nodes-nodeadm.md").

```
 nodeadm uninstall
```

8. With the hybrid nodes artifacts stopped and uninstalled, remove the node resource from your cluster.

```
 kubectl delete node <replaceable>node-name</replaceable>
```

You can identify and delete all of the nodes of a particular Kubernetes version (in this case, `1.28`) with the following code snippet.

```
 K8S_VERSION=1.28
for node in $(kubectl get nodes -o json | jq --arg K8S_VERSION "$K8S_VERSION" -r '.items[] | select(.status.nodeInfo.kubeletVersion | match("\($K8S_VERSION)")).metadata.name')
do
    echo "Deleting $node"
    kubectl delete node $node
done
```

9. Depending on your choice of CNI, there may be artifacts remaining on your hybrid nodes after running the above steps. See [Configure CNI for hybrid nodes](hybrid-nodes-cni.md "hybrid-nodes-cni.md") for more information.

## In-place upgrades

The in-place upgrade process refers to using `nodeadm upgrade` to upgrade the Kubernetes version for hybrid nodes without using new physical or virtual hosts and a cutover migration strategy. The `nodeadm upgrade` process shuts down the existing older Kubernetes components running on the hybrid node, uninstalls the existing older Kubernetes components, installs the new target Kubernetes components, and starts the new target Kubernetes components. It is strongly recommend to upgrade one node at a time to minimize impact to applications running on the hybrid nodes. The duration of this process depends on your network bandwidth and latency.

1. Use the following command to mark the node you are upgrading as unschedulable. This is so that new pods aren’t scheduled or rescheduled on the node that you are upgrading. For more information, see [kubectl cordon](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_cordon/ "https://kubernetes.io/docs/reference/kubectl/generated/kubectl_cordon/") in the Kubernetes documentation. Replace `NODE_NAME` with the name of the hybrid node you are upgrading

```
 kubectl cordon NODE_NAME
```

2. Drain the node you are upgrading with the following command. For more information on draining nodes, see [Safely Drain a Node](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/ "https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/") in the Kubernetes documentation. Replace `NODE_NAME` with the name of the hybrid node you are upgrading.

```
 kubectl drain NODE_NAME --ignore-daemonsets --delete-emptydir-data
```

3. Run `nodeadm upgrade` on the hybrid node you are upgrading. You must run `nodeadm` with a user that has root/sudo privileges. The name of the node is preserved through upgrade for both AWS SSM and AWS IAM Roles Anywhere credential providers. You cannot change credentials providers during the upgrade process. See [Hybrid nodes nodeadm reference](hybrid-nodes-nodeadm.md "hybrid-nodes-nodeadm.md") for configuration values for `nodeConfig.yaml`. Replace `K8S_VERSION` with the target Kubernetes version you upgrading to.

```
 nodeadm upgrade K8S_VERSION -c file://nodeConfig.yaml
```

4. To allow pods to be scheduled on the node after you have upgraded, type the following. Replace `NODE_NAME` with the name of the node.

```
 kubectl uncordon NODE_NAME
```

5. Watch the status of your hybrid nodes and wait for your nodes to shutdown and restart on the new Kubernetes version with the Ready status.

```
 kubectl get nodes -o wide -w
```
