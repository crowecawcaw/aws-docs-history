

# Retrieving SageMaker HyperPod cluster details
<a name="sagemaker-hyperpod-eks-operate-cli-command-cluster-details"></a>

Learn how to retrieve SageMaker HyperPod cluster details using the AWS CLI.

## Describe a cluster
<a name="sagemaker-hyperpod-eks-operate-cli-command-describe-cluster"></a>

Run [describe-cluster](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/describe-cluster.html) to check the status of the cluster. You can specify either the name or the ARN of the cluster.

```
aws sagemaker describe-cluster --cluster-name {{your-hyperpod-cluster}}
```

After the status of the cluster turns to **InService**, proceed to the next step. Using this API, you can also retrieve failure messages from running other HyperPod API operations.

## List details of cluster nodes
<a name="sagemaker-hyperpod-eks-operate-cli-command-list-cluster-nodes"></a>

Run [list-cluster-nodes](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/list-cluster-nodes.html) to check the key information of the cluster nodes.

```
aws sagemaker list-cluster-nodes --cluster-name {{your-hyperpod-cluster}}
```

This returns a response, and the `InstanceId` is what you need to use for logging (using `aws ssm`) into them.

## Describe details of a cluster node
<a name="sagemaker-hyperpod-eks-operate-cli-command-describe-cluster-node"></a>

Run [describe-cluster-node](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/describe-cluster-node.html) to retrieve details of a cluster node. You can get the cluster node ID from list-cluster-nodes output. You can specify either the name or the ARN of the cluster.

```
aws sagemaker describe-cluster-node \
    --cluster-name {{your-hyperpod-cluster}} \
    --node-id {{i-111222333444555aa}}
```

## List clusters
<a name="sagemaker-hyperpod-eks-operate-cli-command-list-clusters"></a>

Run [list-clusters](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/list-clusters.html) to list all clusters in your account.

```
aws sagemaker list-clusters
```

You can also add additional flags to filter the list of clusters down. To learn more about what this command runs at low level and additional flags for filtering, see the [ListClusters](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListClusters.html) API reference.