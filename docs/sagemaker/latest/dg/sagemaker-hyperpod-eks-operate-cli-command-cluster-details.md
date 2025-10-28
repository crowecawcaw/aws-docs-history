# Retrieving SageMaker HyperPod cluster details

Learn how to retrieve SageMaker HyperPod cluster details using the AWS CLI.

## Describe a cluster

Run [describe-cluster](../../../cli/latest/reference/sagemaker/describe-cluster.md "../../../cli/latest/reference/sagemaker/describe-cluster.md") to check the status of the cluster. You can
specify either the name or the ARN of the cluster.

```
aws sagemaker describe-cluster --cluster-name `your-hyperpod-cluster`
```

After the status of the cluster turns to `InService`,
proceed to the next step. Using this API, you can also retrieve failure messages
from running other HyperPod API operations.

## List details of cluster nodes

Run [list-cluster-nodes](../../../cli/latest/reference/sagemaker/list-cluster-nodes.md "../../../cli/latest/reference/sagemaker/list-cluster-nodes.md") to check the key information of the cluster
nodes.

```
aws sagemaker list-cluster-nodes --cluster-name `your-hyperpod-cluster`
```

This returns a response, and the `InstanceId` is what you need to
use for logging (using `aws ssm`) into them.

## Describe details of a cluster node

Run [describe-cluster-node](../../../cli/latest/reference/sagemaker/describe-cluster-node.md "../../../cli/latest/reference/sagemaker/describe-cluster-node.md") to retrieve details of a cluster node. You
can get the cluster node ID from list-cluster-nodes output. You can specify
either the name or the ARN of the cluster.

```
aws sagemaker describe-cluster-node \
    --cluster-name `your-hyperpod-cluster` \
    --node-id `i-111222333444555aa`
```

## List

clusters

Run [list-clusters](../../../cli/latest/reference/sagemaker/list-clusters.md "../../../cli/latest/reference/sagemaker/list-clusters.md") to list all clusters in your account.

```
aws sagemaker list-clusters
```

You can also add additional flags to filter the list of clusters down. To
learn more about what this command runs at low level and additional flags for
filtering, see the [ListClusters](../APIReference/API_ListClusters.md "../APIReference/API_ListClusters.md") API reference.
