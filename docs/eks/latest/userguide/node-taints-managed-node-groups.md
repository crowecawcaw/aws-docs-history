

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Recipe: Prevent pods from being scheduled on specific nodes
<a name="node-taints-managed-node-groups"></a>

## Overview
<a name="_overview"></a>

Nodes with specialized processors, such as GPUs, can be more expensive to run than nodes on standard machines. To protect these nodes from workloads that don’t require special hardware, you can use Kubernetes taints. Taints mark nodes to repel pods that don’t have matching tolerations, ensuring only compatible workloads are scheduled. For more information, see [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) in the Kubernetes documentation.

Kubernetes node taints can be applied to new and existing managed node groups using the AWS Management Console or through the Amazon EKS API. This recipe shows how to apply taints to Amazon EKS managed node groups using the AWS CLI. For information on creating a node group with a taint using the AWS Management Console, see [Create a managed node group for your cluster](create-managed-node-group.md).

## Prerequisites
<a name="_prerequisites"></a>
+ An [existing Amazon EKS cluster](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html).
+  [AWS CLI installed and configured](https://docs.aws.amazon.com/eks/latest/userguide/setting-up.html) with appropriate permissions.

## Steps
<a name="_steps"></a>

### Step 1: Create a node group with taints
<a name="_step_1_create_a_node_group_with_taints"></a>

Use the `aws eks create-nodegroup` command to create a new managed node group with taints. This example applies a taint with key `dedicated`, value `gpuGroup`, and effect `NO_SCHEDULE`.

```
aws eks create-nodegroup \
 --cli-input-json '
{
  "clusterName": "my-cluster",
  "nodegroupName": "node-taints-example",
  "subnets": [
     "subnet-1234567890abcdef0",
     "subnet-abcdef01234567890",
     "subnet-021345abcdef67890"
   ],
  "nodeRole": "arn:aws:iam::111122223333:role/AmazonEKSNodeRole",
  "taints": [
     {
         "key": "dedicated",
         "value": "gpuGroup",
         "effect": "NO_SCHEDULE"
     }
   ]
}'
```

For more information and examples, see [taint](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#taint) in the Kubernetes reference documentation.

### Step 2: Update taints on an existing node group
<a name="_step_2_update_taints_on_an_existing_node_group"></a>

Use the [aws eks update-nodegroup-config](https://docs.aws.amazon.com/cli/latest/reference/eks/update-nodegroup-config.html) AWS CLI command to add, remove, or replace taints for managed node groups.

```
aws eks update-nodegroup-config \
  --cluster-name my-cluster \
  --nodegroup-name node-taints-example \
  --taints 'removeTaints=[{key=dedicated,value=gpuGroup,effect=NO_SCHEDULE}]'
```

## Notes
<a name="_notes"></a>
+ Taints can be updated after you create the node group using the `UpdateNodegroupConfig` API.
+ The taint key must begin with a letter or number. It can contain letters, numbers, hyphens (`-`), periods (`.`), and underscores (`_`). It can be up to 63 characters long.
+ Optionally, the taint key can begin with a DNS subdomain prefix and a single `/`. If it begins with a DNS subdomain prefix, it can be 253 characters long.
+ The value is optional and must begin with a letter or number. It can contain letters, numbers, hyphens (`-`), periods (`.`), and underscores (`_`). It can be up to 63 characters long.
+ When using Kubernetes directly or the AWS Management Console, the taint effect must be `NoSchedule`, `PreferNoSchedule`, or `NoExecute`. However, when using the AWS CLI or API, the taint effect must be `NO_SCHEDULE`, `PREFER_NO_SCHEDULE`, or `NO_EXECUTE`.
+ A maximum of 50 taints are allowed per node group.
+ If taints that were created using a managed node group are removed manually from a node, then Amazon EKS doesn’t add the taints back to the node. This is true even if the taints are specified in the managed node group configuration.