# Deploying a JEG pod to a node

group

JEG (Jupyter Enterprise Gateway) pod placement is a feature that allows you to deploy an
interactive endpoint on a specific node group. With this feature, you can configure settings
such as `instance type` for the interactive endpoint.

## Associating a JEG pod to a managed node

group

The following configuration property allows you to specify the name of a managed node
group on your Amazon EKS cluster where the JEG pod will be deployed.

```
//payload
--configuration-overrides '{
      "applicationConfiguration": [
            {
                "classification": "endpoint-configuration",
                "properties": {
                    "managed-nodegroup-name": `NodeGroupName`
                }
            }
        ]
    }'
```

A node group must have the Kubernetes label
`for-use-with-emr-containers-managed-endpoint-ng=`NodeGroupName``
attached to all nodes that are part of the node group. To list all nodes of a node group
that have this tag, use the following command:

```
kubectl get nodes --show-labels | grep for-use-with-emr-containers-managed-endpoint-ng=`NodeGroupName`
```

If the output of the command above doesn't return nodes that are part of your managed
node group, then there are no nodes in the node group that have the
`for-use-with-emr-containers-managed-endpoint-ng=`NodeGroupName``
Kubernetes label attached. In this case, follow the steps below to attach that label to
the nodes in your node group.

1. Use the following command to add the
   `for-use-with-emr-containers-managed-endpoint-ng=`NodeGroupName`Kubernetes label to all nodes in a managed node group`NodeGroupName``:

```
kubectl label nodes --selector eks:nodegroup-name=`NodeGroupName` for-use-with-emr-containers-managed-endpoint-ng=`NodeGroupName`
```

2. Verify that the nodes were labeled correctly using the following command:

```
kubectl get nodes --show-labels | grep for-use-with-emr-containers-managed-endpoint-ng=`NodeGroupName`
```

A managed node group must be associated with an Amazon EKS cluster’s security group, which
is usually the case if you created your cluster and managed node group using
`eksctl`. You can verify this in the AWS console using the following
steps.

1. Go to your cluster in the Amazon EKS console.
2. Go to the networking tab of your cluster and note down the cluster security
   group.
3. Go to the compute tab of your cluster and click on the managed node group
   name.
4. Under the **Details** tab of the managed node group,
   verify that the cluster security group that you noted previously is listed under
   **Security groups**.

If the managed node group is not attached to the Amazon EKS cluster security group, you
need to attach the
`for-use-with-emr-containers-managed-endpoint-sg=`ClusterName`/`NodeGroupName``
tag to the node group security group. Use the steps below to attach this tag.

1. Go to the Amazon EC2 console and click on security groups on the left navigation
   pane.
2. Select your managed node group’s security group by clicking the checkbox.
3. Under the **Tags** tab, add the tag
   `for-use-with-emr-containers-managed-endpoint-sg=`ClusterName`/`NodeGroupName``
   using the **Manage tags** button.

## Associating a JEG pod to a

self-managed node group

The following configuration property allows you to specify the name of a self-managed
or unmanaged node group on the Amazon EKS cluster where the JEG pod will be deployed.

```
//payload
--configuration-overrides '{
      "applicationConfiguration": [
            {
                "classification": "endpoint-configuration",
                "properties": {
                    "self-managed-nodegroup-name": `NodeGroupName`
                }
            }
        ]
    }'
```

The node group must have
`for-use-with-emr-containers-managed-endpoint-ng=`NodeGroupName``
Kubernetes label attached to all nodes that are part of the node group. To list all the
nodes of a node group that have this tag, use the following command:

```
kubectl get nodes --show-labels | grep for-use-with-emr-containers-managed-endpoint-ng=`NodeGroupName`
```

If the output of the command above doesn't return nodes that are part of your
self-managed node group, then there are no nodes in the node group that have the
`for-use-with-emr-containers-managed-endpoint-ng=`NodeGroupName``
Kubernetes label attached. In this case, follow the steps below to attach that label to
the nodes in your node group.

1. If you created the self-managed node group using `eksctl`, then use the
   following command to add the
   `for-use-with-emr-containers-managed-endpoint-ng=`NodeGroupName`Kubernetes label to all nodes in the self-managed node group`NodeGroupName`` at once.

```
kubectl label nodes --selector alpha.eksctl.io/nodegroup-name=`NodeGroupName` for-use-with-emr-containers-managed-endpoint-ng=`NodeGroupName`
```

If you didn’t use `eksctl` to create the self-managed node group, then
you will need to replace the selector in the above command to a different Kubernetes
label that is attached to all the nodes of the node group. 2. Use the following command to verify that the nodes were labeled correctly:

```
kubectl get nodes --show-labels | grep for-use-with-emr-containers-managed-endpoint-ng=`NodeGroupName`
```

The security group for the self-managed node group must have the
`for-use-with-emr-containers-managed-endpoint-sg=`ClusterName`/`NodeGroupName``
tag attached. Use the following steps to attach the tag to the security group from the
AWS Management Console.

1. Navigate to the Amazon EC2 console. Select **Security
   groups** on the left navigation pane.
2. Select the checkbox next to the security group for your self-managed node
   group.
3. Under the **Tags** tab, use the **Manage tags** button to add the tag
   `for-use-with-emr-containers-managed-endpoint-sg=`ClusterName`/`NodeGroupName`.
Replace `ClusterName`and`NodeGroupName`` with appropriate
   values.

## Associating a JEG pod to a

managed node group with On-Demand instances

You can also define additional labels, known as _Kubernetes label
selectors_, to specify additional constraints or restrictions to run an
interactive endpoint on a given node or node group. The following example shows how to use
On-Demand Amazon EC2 instances for a JEG pod.

```
--configuration-overrides '{
      "applicationConfiguration": [
            {
                "classification": "endpoint-configuration",
                "properties": {
                    "managed-nodegroup-name": `NodeGroupName`,
                    "node-labels": "eks.amazonaws.com/capacityType:ON_DEMAND"
                }
            }
        ]
    }'
```

###### Note

You can only use the `node-labels` property with
either with a `managed-nodegroup-name` or
`self-managed-nodegroup-name` property.
