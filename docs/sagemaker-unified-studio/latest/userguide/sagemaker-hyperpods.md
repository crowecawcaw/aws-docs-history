# HyperPod clusters

Use Amazon SageMaker AI HyperPod to help you provision resilient compute clusters for running model
training or fine-tuning workloads. Amazon SageMaker AI HyperPod integrates with Slurm or Amazon EKS for
orchestration.

You can create HyperPod clusters using the Amazon SageMaker AI Hyperpod console UI or SageMaker AI Studio. For
more information, see [Orchestrating SageMaker AI HyperPod clusters with Slurm](../../../sagemaker/latest/dg/sagemaker-hyperpod-slurm.md "../../../sagemaker/latest/dg/sagemaker-hyperpod-slurm.md") or [Orchestrating SageMaker AI HyperPod clusters with Amazon EKS](../../../sagemaker/latest/dg/sagemaker-hyperpod-eks.md "../../../sagemaker/latest/dg/sagemaker-hyperpod-eks.md") in the _Amazon SageMaker AI Developer Guide_.

In Amazon SageMaker Unified Studio, you can launch machine learning workloads on Amazon SageMaker AI HyperPod clusters. You
can also view details about the HyperPod clusters.

###### Topics

- [Connect to a HyperPod cluster](#sagemaker-hyperpods-add-connection "#sagemaker-hyperpods-add-connection")
- [View the HyperPod clusters](#sagemaker-hyperpods-view "#sagemaker-hyperpods-view")
- [View details about a HyperPod
  cluster](#sagemaker-hyperpods-view-details "#sagemaker-hyperpods-view-details")
- [HyperPod task governance](#sagemaker-hyperpods-task-gov "#sagemaker-hyperpods-task-gov")
- [Open the HyperPod in JupyterLab](#sagemaker-hyperpods-jupyterlab "#sagemaker-hyperpods-jupyterlab")

## Connect to a HyperPod cluster

To use a HyperPod cluster in Amazon SageMaker Unified Studio, you create a connection to the cluster by
following these steps:

1. Sign in to Amazon SageMaker Unified Studio using the link that your administrator gave you.
2. From the **Build** drop-down menu, choose **HyperPod**. The compute page displays the
   HyperPod clusters for your project.
3. Choose **Add compute**.
4. In the **Add compute** form, configure the following fields:
   1. For **Connection name**, enter a name for this connection.
   2. For **HuperPod cluster name**, enter the name of the HyperPod cluster.
   3. For **Access role ARN**, enter the IAM role that the project needs to assume.
   4. For **Account ID**, enter the AWS account where the runtime role exists.
   5. For **AWS Region**, enter the Region where the HyperPod cluster was
      created.

## View the HyperPod clusters

To view the HyperPod clusters in your project, follow these steps:

1. Sign in to Amazon SageMaker Unified Studio using the link that your administrator gave you.
2. From the **Build** drop-down menu, choose **HyperPods**.

The portal opens the **HyperPod clusters** tab of the **Compute** page.
The HyperPod clusters table provides a summary view of each cluster, including the ARN, status, and creation time.

## View details about a HyperPod

cluster

To view the details page for a HyperPod cluster, choose the HyperPod from the table of
HyperPod clusters. The page displays tabs for tasks, metrics, settings, and metadata
details.

For more information about HyperPod cluster details that you can view in Amazon SageMaker Unified Studio,
see [HyperPod tabs in Studio](../../../sagemaker/latest/dg/sagemaker-hyperpod-studio-tabs.md "../../../sagemaker/latest/dg/sagemaker-hyperpod-studio-tabs.md") in the _Amazon SageMaker AI Developer Guide_.

## HyperPod task governance

For Amazon EKS clusters, you can use HyperPod task governance to streamline resource allocation
and utilization of compute resources in the cluster.

HyperPod task governance provides a comprehensive dashboard view of your Amazon EKS
cluster utilization metrics, including hardware, team, and task metrics.

For more information about the HyperPod dashboard view, see [Dashboard](../../../sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance-metrics.md "../../../sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance-metrics.md") in the _Amazon SageMaker AI Developer Guide_.

## Open the HyperPod in JupyterLab

To open your HyperPod in JupyterLab, follow these steps:

1. From the cluster details page, choose **Open in JupyterLab**.

The **Starting space** page opens and the space initialization starts.

After the JupyterLab space is ready, it opens the HyperPod sample notebook. 2. The HyperPod sample notebook shows the end-to-end flow of how to use the HyperPod cluster,
including sample commands for:

    * Connecting to the cluster
    * Submitting jobs to the cluster.
    * Viewing job status or cluster status.
