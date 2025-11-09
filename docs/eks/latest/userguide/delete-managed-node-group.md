**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Delete a managed node group from your cluster

This topic describes how you can delete an Amazon EKS managed node group. When you delete a managed node group, Amazon EKS first sets the minimum, maximum, and desired size of your Auto Scaling group to zero. This then causes your node group to scale down.

Before each instance is terminated, Amazon EKS sends a signal to drain that node. During the drain process, Kubernetes does the following for each pod on the node: runs any configured `preStop` lifecycle hooks, sends `SIGTERM` signals to the containers, then waits for the `terminationGracePeriodSeconds` for graceful shutdown. If the node hasn’t been drained after 5 minutes, Amazon EKS lets Auto Scaling continue the forced termination of the instance. After all instances have been terminated, the Auto Scaling group is deleted.

###### Important

If you delete a managed node group that uses a node IAM role that isn’t used by any other managed node group in the cluster, the role is removed from the `aws-auth`
`ConfigMap`. If any of the self-managed node groups in the cluster are using the same node IAM role, the self-managed nodes move to the `NotReady` status. Additionally, the cluster operation is also disrupted. To add a mapping for the role you’re using only for the self-managed node groups, see [Create access entries](creating-access-entries.md "creating-access-entries.md"), if your cluster’s platform version is at least minimum version listed in the prerequisites section of [Grant IAM users access to Kubernetes with EKS access entries](access-entries.md "access-entries.md"). If your platform version is earlier than the required minimum version for access entries, you can add the entry back to the `aws-auth`
`ConfigMap`. For more information, enter `eksctl create iamidentitymapping --help` in your terminal.

You can delete a managed node group with:

- [eksctl](#eksctl-delete-managed-nodegroup "#eksctl-delete-managed-nodegroup")
- [AWS Management Console](#console-delete-managed-nodegroup "#console-delete-managed-nodegroup")
- [AWS CLI](#awscli-delete-managed-nodegroup "#awscli-delete-managed-nodegroup")

## `eksctl`

**Delete a managed node group with `eksctl`**

Enter the following command. Replace every `<example value>` with your own values.

```
eksctl delete nodegroup \
  --cluster <my-cluster> \
  --name <my-mng> \
  --region <region-code>
```

For more options, see [Deleting and draining nodegroups](https://eksctl.io/usage/nodegroups/#deleting-and-draining-nodegroups "https://eksctl.io/usage/nodegroups/#deleting-and-draining-nodegroups") in the `eksctl` documentation.

## AWS Management Console

**Delete a managed node group with AWS Management Console**

1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. On the **Clusters** page, choose the cluster that contains the node group to delete.
3. On the selected cluster page, choose the **Compute** tab.
4. In the **Node groups** section, choose the node group to delete. Then choose **Delete**.
5. In the **Delete node group** confirmation dialog box, enter the name of the node group. Then choose **Delete**.

## AWS CLI

**Delete a managed node group with AWS CLI**

1. Enter the following command. Replace every `<example value>` with your own values.

```
aws eks delete-nodegroup \
  --cluster-name <my-cluster> \
  --nodegroup-name <my-mng> \
  --region <region-code>
```

2. If `cli_pager=` is set in the CLI config, use the arrow keys on your keyboard to scroll through the response output. Press the `q` key when you’re finished.

For more options, see the `delete-nodegroup` command in the _AWS CLI Command Reference_.
