**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Delete a cluster

When you’re done using an Amazon EKS cluster, you should delete the resources associated with it so that you don’t incur any unnecessary costs.

You can delete a cluster with `eksctl`, the AWS Management Console, or the AWS CLI.

## Considerations

- If you receive an error because the cluster creator has been removed, see [this article](https://aws.amazon.com/premiumsupport/knowledge-center/eks-api-server-unauthorized-error "https://aws.amazon.com/premiumsupport/knowledge-center/eks-api-server-unauthorized-error") to resolve.
- Amazon Managed Service for Prometheus resources are outside of the cluster lifecycle and need to be maintained independent of the cluster. When you delete your cluster, make sure to also delete any applicable scrapers to stop applicable costs. For more information, see [Find and delete scrapers](../../../prometheus/latest/userguide/AMP-collector-how-to.md#AMP-collector-list-delete "../../../prometheus/latest/userguide/AMP-collector-how-to.md#AMP-collector-list-delete") in the _Amazon Managed Service for Prometheus User Guide_.
- To remove a connected cluster, see [Deregister a Kubernetes cluster from the Amazon EKS console](deregister-connected-cluster.md "deregister-connected-cluster.md")
- Before you can delete a cluster, make sure deletion protection is diabled for your cluster.

### Considerations for EKS Auto Mode

- Any EKS Auto Mode Nodes will be deleted, including the EC2 managed instances
- All load balancers will be deleted

For more information, see [Disable EKS Auto Mode](auto-disable.md "auto-disable.md").

## Prerequisite steps

The following are steps that you must first perform before you can delete a cluster. These steps apply regardless of the method that you use to delete your cluster.

1. List all services running in your cluster.

```
kubectl get svc --all-namespaces
```

2. Delete any services that have an associated `EXTERNAL-IP` value. These services are fronted by an Elastic Load Balancing load balancer, and you must delete them in Kubernetes to allow the load balancer and associated resources to be properly released.
   Replace `service-name` with the name of each service listed as described.

```
kubectl delete svc service-name
```

3. Delete any ingress resources as well. If you don’t delete the ingress resources, the application load balancer remains even if you deleted the cluster. Replace `ingress-name` with the name of your ingress resources.

```
kubectl get ingress --all-namespaces
```

```
kubectl delete ing ingress-name
```

## Delete cluster (eksctl)

This procedure requires `eksctl` version `0.215.0` or later. You can check your version with the following command:

```
eksctl version
```

For instructions on how to install or upgrade `eksctl`, see [Installation](https://eksctl.io/installation "https://eksctl.io/installation") in the `eksctl` documentation.

1. Go through the [prerequisite steps](#prerequisite-steps "#prerequisite-steps"). After doing so, delete your cluster and its associated nodes with the following command, replacing `prod` with your cluster name.

```
eksctl delete cluster --name prod
```

Output:

```
[ℹ]  using region region-code
[ℹ]  deleting EKS cluster "prod"
[ℹ]  will delete stack "eksctl-prod-nodegroup-standard-nodes"
[ℹ]  waiting for stack "eksctl-prod-nodegroup-standard-nodes" to get deleted
[ℹ]  will delete stack "eksctl-prod-cluster"
[✔]  the following EKS cluster resource(s) for "prod" will be deleted: cluster. If in doubt, check CloudFormation console
```

## Delete cluster (AWS console)

1. Go through the [prerequisite steps](#prerequisite-steps "#prerequisite-steps"). After doing so, delete all node groups and Fargate profiles.
   1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
   2. In the left navigation pane, choose Amazon EKS **Clusters**, and then in the tabbed list of clusters, choose the name of the cluster that you want to delete.
   3. Choose the **Compute** tab and choose a node group to delete. Choose **Delete**, enter the name of the node group, and then choose **Delete**. Delete all node groups in the cluster.

   ###### Note

   The node groups listed are [managed node groups](managed-node-groups.md "managed-node-groups.md") only. 4. Choose a **Fargate Profile** to delete, select **Delete**, enter the name of the profile, and then choose **Delete**. Delete all Fargate profiles in the cluster.

2. Delete all [self-managed node AWS CloudFormation stacks](worker.md "worker.md").
   1. Open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
   2. Choose the node stack to delete, and then choose **Delete**.
   3. In the **Delete stack** confirmation dialog box, choose **Delete stack**. Delete all self-managed node stacks in the cluster.

3. Delete the cluster.
   1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
   2. choose the cluster to delete and choose **Delete**.
   3. On the delete cluster confirmation screen, choose **Delete**.

4. (Optional) Delete the VPC AWS CloudFormation stack.
   1. Open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
   2. Select the VPC stack to delete, and then choose **Delete**.
   3. In the **Delete stack** confirmation dialog box, choose **Delete stack**.

## Delete cluster (AWS CLI)

1. Go through the [prerequisite steps](#prerequisite-steps "#prerequisite-steps"). After doing so, delete all node groups and Fargate profiles.
   1. List the node groups in your cluster with the following command.

   ```
   aws eks list-nodegroups --cluster-name my-cluster
   ```

   ###### Note

   The node groups listed are [managed node groups](managed-node-groups.md "managed-node-groups.md") only. 2. Delete each node group with the following command. Delete all node groups in the cluster.

   ```
   aws eks delete-nodegroup --nodegroup-name my-nodegroup --cluster-name my-cluster
   ```

   3. List the Fargate profiles in your cluster with the following command.

   ```
   aws eks list-fargate-profiles --cluster-name my-cluster
   ```

   4. Delete each Fargate profile with the following command. Delete all Fargate profiles in the cluster.

   ```
   aws eks delete-fargate-profile --fargate-profile-name my-fargate-profile --cluster-name my-cluster
   ```

2. Delete all [self-managed node AWS CloudFormation stacks](worker.md "worker.md").
   1. List your available AWS CloudFormation stacks with the following command. Find the node template name in the resulting output.

   ```
   aws cloudformation list-stacks --query "StackSummaries[].StackName"
   ```

   2. Delete each node stack with the following command, replacing `node-stack` with your node stack name. Delete all self-managed node stacks in the cluster.

   ```
   aws cloudformation delete-stack --stack-name node-stack
   ```

3. Delete the cluster with the following command, replacing `my-cluster` with your cluster name.

```
aws eks delete-cluster --name my-cluster
```

4. (Optional) Delete the VPC AWS CloudFormation stack.
   1. List your available AWS CloudFormation stacks with the following command. Find the VPC template name in the resulting output.

   ```
   aws cloudformation list-stacks --query "StackSummaries[].StackName"
   ```

   2. Delete the VPC stack with the following command, replacing `my-vpc-stack` with your VPC stack name.

   ```
   aws cloudformation delete-stack --stack-name my-vpc-stack
   ```
