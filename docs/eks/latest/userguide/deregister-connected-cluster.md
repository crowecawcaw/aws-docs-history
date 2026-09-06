

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Deregister a Kubernetes cluster from the Amazon EKS console
<a name="deregister-connected-cluster"></a>

If you are finished using a connected cluster, you can deregister it. After it’s deregistered, the cluster is no longer visible in the Amazon EKS console.

You must have the following permissions to call the deregisterCluster API:
+  `eks:DeregisterCluster` 
+  `ssm:DeleteActivation` 
+  `ssm:DeregisterManagedInstance` 

This process involves two steps: Deregistering the cluster with Amazon EKS and uninstalling the eks-connector agent in the cluster.

## Deregister the Kubernetes cluster
<a name="deregister-connected-cluster-eks"></a>

To deregister a cluster from Amazon EKS Connector, you can use one of these tools:
+  [AWS CLI](#awscli_deregister_cluster_connect) 
+  [AWS Management Console](#console_deregister_cluster_connect) 
+  [`eksctl`](#eksctl_deregister_cluster_connect) 

### AWS CLI
<a name="awscli_deregister_cluster_connect"></a>

1.  AWS CLI must be installed. To install or upgrade it, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html).

1. Ensure the Amazon EKS Connector agent role was created.

1. Deregister the connected cluster.

   ```
   aws eks deregister-cluster \
       --name my-cluster \
       --region region-code
   ```

### AWS Management Console
<a name="console_deregister_cluster_connect"></a>

1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters).

1. Choose **Clusters**.

1. On the **Clusters** page, select the connected cluster and select **Deregister**.

1. Confirm that you want to deregister the cluster.

### `eksctl`
<a name="eksctl_deregister_cluster_connect"></a>

1. Install `eksctl` version `0.68` or later. To install or upgrade it, see [Get started with Amazon EKS – `eksctl`](getting-started-eksctl.md).

1. Ensure the Amazon EKS Connector agent role was created.

1. Deregister the connected cluster:

   ```
   eksctl deregister cluster --name my-cluster
   ```

## Clean up the resources in your Kubernetes cluster
<a name="deregister-connected-cluster-k8s"></a>

To uninstall the `eks-connector` agent, use one of the following tools:
+  [Helm](#helm_agent_cluster_deregister) 
+  [YAML](#yaml_agent_cluster_deregister) 

### Helm
<a name="helm_agent_cluster_deregister"></a>

Run the following command to uninstall the agent.

```
helm -n eks-connector uninstall eks-connector
```

### YAML
<a name="yaml_agent_cluster_deregister"></a>

1. Delete the Amazon EKS Connector YAML file from your Kubernetes cluster.

   ```
   kubectl delete -f eks-connector.yaml
   ```

1. If you created `clusterrole` or `clusterrolebindings` for additional [IAM principals](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html#iam-term-principal) to access the cluster, delete them from your Kubernetes cluster.