

# Managing SageMaker HyperPod Slurm clusters using the SageMaker console
<a name="sagemaker-hyperpod-operate-slurm-console-ui"></a>

The following topics provide guidance on how to manage SageMaker HyperPod through the console UI.

**Topics**
+ [Create a SageMaker HyperPod cluster](#sagemaker-hyperpod-operate-slurm-console-ui-create-cluster)
+ [Browse your SageMaker HyperPod clusters](#sagemaker-hyperpod-operate-slurm-console-ui-browse-clusters)
+ [View details of each SageMaker HyperPod cluster](#sagemaker-hyperpod-operate-slurm-console-ui-view-details-of-clusters)
+ [Edit a SageMaker HyperPod cluster](#sagemaker-hyperpod-operate-slurm-console-ui-edit-clusters)
+ [Delete a SageMaker HyperPod cluster](#sagemaker-hyperpod-operate-slurm-console-ui-delete-cluster)

## Create a SageMaker HyperPod cluster
<a name="sagemaker-hyperpod-operate-slurm-console-ui-create-cluster"></a>

See the instructions in [Getting started with SageMaker HyperPod using the SageMaker AI console](smcluster-getting-started-slurm-console.md) to create a new SageMaker HyperPod cluster through the SageMaker HyperPod console UI.

## Browse your SageMaker HyperPod clusters
<a name="sagemaker-hyperpod-operate-slurm-console-ui-browse-clusters"></a>

Under **Clusters** in the main pane of the SageMaker HyperPod console on the SageMaker HyperPod console main page, all created clusters should appear listed under the **Clusters** section, which provides a summary view of clusters, their ARNs, status, and creation time.

## View details of each SageMaker HyperPod cluster
<a name="sagemaker-hyperpod-operate-slurm-console-ui-view-details-of-clusters"></a>

Under **Clusters** on the console main page, the cluster **Names** are activated as links. Choose the cluster name link to see details of each cluster.

## Edit a SageMaker HyperPod cluster
<a name="sagemaker-hyperpod-operate-slurm-console-ui-edit-clusters"></a>

1. Under **Clusters** in the main pane of the SageMaker HyperPod console, choose the cluster you want to update.

1. Select your cluster, and choose **Edit**.

1. In the **Edit <your-cluster>** page, you can edit the configurations of existing instance groups, add more instance groups, delete instance groups, and change tags for the cluster. After making changes, choose **Submit**. 

   1. In the **Configure instance groups** section, you can add more instance groups by choosing **Create instance group**.

   1. In the **Configure instance groups** section, you can choose **Edit** to change its configuration or **Delete** to remove the instance group permanently.
**Important**  
When deleting an instance group, consider the following points:  
Your SageMaker HyperPod cluster must always maintain at least one instance group.
Ensure all critical data is backed up before removal
The removal process cannot be undone.
**Note**  
Deleting an instance group will terminate all compute resources associated with that group.

   1. In the **Tags** section, you can update tags for the cluster.

## Delete a SageMaker HyperPod cluster
<a name="sagemaker-hyperpod-operate-slurm-console-ui-delete-cluster"></a>

1. Under **Clusters** in the main pane of the SageMaker HyperPod console, choose the cluster you want to delete.

1. Select your cluster, and choose **Delete**.

1. In the pop-up window for cluster deletion, review the cluster information carefully to confirm that you chose the right cluster to delete.

1. After you reviewed the cluster information, choose **Yes, delete cluster**.

1. In the text field to confirm this deletion, type **delete**.

1. Choose **Delete** on the lower right corner of the pop-up window to finish sending the cluster deletion request.