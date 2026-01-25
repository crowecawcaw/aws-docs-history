**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Deregister a Kubernetes cluster from the Amazon EKS console

If you are finished using a connected cluster, you can deregister it. After it’s deregistered, the cluster is no longer visible in the Amazon EKS console.

You must have the following permissions to call the deregisterCluster API:

- `eks:DeregisterCluster`
- `ssm:DeleteActivation`
- `ssm:DeregisterManagedInstance`
  This process involves two steps: Deregistering the cluster with Amazon EKS and uninstalling the eks-connector agent in the cluster.

## Deregister the Kubernetes cluster

To deregister a cluster from Amazon EKS connector, you can use one of these tools:

- [AWS CLI](#awscli_deregister_cluster_connect "#awscli_deregister_cluster_connect")
- [AWS Management Console](#console_deregister_cluster_connect "#console_deregister_cluster_connect")
- [eksctl](#eksctl_deregister_cluster_connect "#eksctl_deregister_cluster_connect")

### AWS CLI

1. AWS CLI must be installed. To install or upgrade it, see [Installing the AWS CLI](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md").
2. Ensure the Amazon EKS Connector agent role was created.
3. Deregister the connected cluster.

```
aws eks deregister-cluster \
    --name my-cluster \
    --region region-code
```

### AWS Management Console

1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. Choose **Clusters**.
3. On the **Clusters** page, select the connected cluster and select **Deregister**.
4. Confirm that you want to deregister the cluster.

### `eksctl`

1. Install `eksctl` version `0.68` or later. To install or upgrade it, see [Get started with Amazon EKS – eksctl](getting-started-eksctl.md "getting-started-eksctl.md").
2. Ensure the Amazon EKS Connector agent role was created.
3. Deregister the connected cluster:

```
eksctl deregister cluster --name my-cluster
```

## Clean up the resources in your Kubernetes cluster

To uninstall the `eks-connector` agent, use one of the following tools:

- [helm](#helm_agent_cluster_deregister "#helm_agent_cluster_deregister")
- [yaml](#yaml_agent_cluster_deregister "#yaml_agent_cluster_deregister")

### helm

Run the following command to uninstall the agent.

```
helm -n eks-connector uninstall eks-connector
```

### yaml

1. Delete the Amazon EKS Connector YAML file from your Kubernetes cluster.

```
kubectl delete -f eks-connector.yaml
```

2. If you created `clusterrole` or `clusterrolebindings` for additional [IAM principals](../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal "../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal") to access the cluster, delete them from your Kubernetes cluster.
