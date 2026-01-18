**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Remove hybrid nodes

This topic describes how to delete hybrid nodes from your Amazon EKS cluster. You must delete your hybrid nodes with your choice of Kubernetes-compatible tooling such as [kubectl](https://kubernetes.io/docs/reference/kubectl/ "https://kubernetes.io/docs/reference/kubectl/"). Charges for hybrid nodes stop when the node object is removed from the Amazon EKS cluster. For more information on hybrid nodes pricing, see [Amazon EKS Pricing](https://aws.amazon.com/eks/pricing/ "https://aws.amazon.com/eks/pricing/").

###### Important

Removing nodes is disruptive to workloads running on the node. Before deleting hybrid nodes, we recommend that you first drain the node to move pods to another active node. For more information on draining nodes, see [Safely Drain a Node](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/ "https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/") in the Kubernetes documentation.

Run the kubectl steps below from your local machine or instance that you use to interact with the Amazon EKS cluster’s Kubernetes API endpoint. If you are using a specific `kubeconfig` file, use the `--kubeconfig` flag.

## Step 1: List your nodes

```
 kubectl get nodes
```

## Step 2: Drain your node

See [kubectl drain](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_drain/ "https://kubernetes.io/docs/reference/kubectl/generated/kubectl_drain/") in the Kubernetes documentation for more information on the `kubectl drain` command.

```
 kubectl drain --ignore-daemonsets <node-name>
```

## Step 3: Stop and uninstall hybrid nodes artifacts

You can use the Amazon EKS Hybrid Nodes CLI (`nodeadm`) to stop and remove the hybrid nodes artifacts from the host. You must run `nodeadm` with a user that has root/sudo privileges. By default, `nodeadm uninstall` will not proceed if there are pods remaining on the node. If you are using AWS Systems Manager (SSM) as your credentials provider, the `nodeadm uninstall` command deregisters the host as an AWS SSM managed instance. For more information, see [Hybrid nodes nodeadm reference](hybrid-nodes-nodeadm.md "hybrid-nodes-nodeadm.md").

```
 nodeadm uninstall
```

## Step 4: Delete your node from the cluster

With the hybrid nodes artifacts stopped and uninstalled, remove the node resource from your cluster.

```
 kubectl delete node <node-name>
```

## Step 5: Check for remaining artifacts

Depending on your choice of CNI, there may be artifacts remaining on your hybrid nodes after running the above steps. See [Configure CNI for hybrid nodes](hybrid-nodes-cni.md "hybrid-nodes-cni.md") for more information.
