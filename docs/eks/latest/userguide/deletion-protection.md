**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Protect EKS clusters from accidental deletion

Accidentally deleting an EKS cluster may impair Kubernetes cluster operations.

You can now protect EKS clusters from accidental deletion. If you enable deletion protection on a cluster, you must first disable deletion protection before you can delete the cluster.

The purpose of deletion protection is to prevent accidents. You should carefully restrict who is authorized to delete clusters.

If you try to delete an active cluster that has deletion protection turned on, you will receive a `InvalidRequestException` .

###### Important

If you enable deletion protection on a cluster, you must have **both** the UpdateClusterConfig and DeleteCluster IAM permissions to first remove the deletion protection, and finally delete the cluster.

###### Note

If the cluster state is creating, failed, or deleting, you can delete the cluster even if deletion protection is turned on.

## To enable deletion protection for an existing cluster

You can only run this on a cluster in the active status.

```
aws eks update-cluster-config --name <cluster-name> --region <aws-region> --deletion-protection
```

## To disable deletion protection for an existing cluster

```
aws eks update-cluster-config --name <cluster-name> --region <aws-region> --no-deletion-protection
```
