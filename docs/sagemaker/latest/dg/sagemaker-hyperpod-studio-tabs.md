# HyperPod tabs in Studio

In Amazon SageMaker Studio you can navigate to one of your clusters in **HyperPod
clusters** (under **Compute**) and view your list of clusters. The
displayed clusters contain information like tasks, hardware metrics, settings, and metadata
details. This visibility can help your team identify the right candidate for your pre-training or
finetuning workloads. The following sections provide information on each type of
information.

## Tasks

Amazon SageMaker HyperPod provides a view of your cluster tasks. Tasks are operations or jobs that
are sent to the cluster. These can be machine learning operations, like training, running
experiments, or inference. The following section provides information on your HyperPod
cluster tasks.

In Amazon SageMaker Studio, you can navigate to one of your clusters in **HyperPod
clusters** (under **Compute**) and view the
**Tasks** information on your cluster. If you are having any issues with
viewing tasks, see [Troubleshooting](sagemaker-hyperpod-studio-troubleshoot.md "sagemaker-hyperpod-studio-troubleshoot.md").

The task table includes:

For Slurm clusters
For Slurm clusters, the tasks currently in the Slurm job scheduler queue are shown in
the table. The information shown for each task includes the task name, status, job ID,
partition, run time, nodes, created by, and actions.

For a list and details about past jobs, use the [`sacct`](https://slurm.schedmd.com/sacct.html "https://slurm.schedmd.com/sacct.html") command in JupyterLab
or a Code Editor terminal. The `sacct` command is used to view _historical information_ about jobs that have _finished_ or are _complete_ in the system. It
provides accounting information, including job resources usage like memory and exit status.

By default, all Studio users can view, manage, and interact with all available
Slurm tasks. To restrict the viewable tasks to Studio users, see [Restrict task view
in Studio for Slurm clusters](sagemaker-hyperpod-studio-setup-slurm.md#sagemaker-hyperpod-studio-setup-slurm-restrict-tasks-view "sagemaker-hyperpod-studio-setup-slurm.md#sagemaker-hyperpod-studio-setup-slurm-restrict-tasks-view").

For Amazon EKS clusters
For Amazon EKS clusters, kubeflow (PyTorch, MPI, TensorFlow) tasks are shown in the table.
PyTorch tasks are shown by default. You can sort for PyTorch, MPI, and TensorFlow under
**Task type**. The information that is shown for each task includes the
task name, status, namespace, priority class, and creation time.

By default, all users can view jobs across all namespaces. To restrict the viewable
Kubernetes namespaces available to Studio users, see [Restrict task view in
Studio for EKS clusters](sagemaker-hyperpod-studio-setup-eks.md#sagemaker-hyperpod-studio-setup-eks-restrict-tasks-view "sagemaker-hyperpod-studio-setup-eks.md#sagemaker-hyperpod-studio-setup-eks-restrict-tasks-view"). If a user cannot
view the tasks and is asked to provide a namespace, they need to get that information from
the administrator.

## Metrics

Amazon SageMaker HyperPod provides a view of your Slurm or Amazon EKS cluster utilization metrics. The
following provides information on your HyperPod cluster metrics.

You will need to install the Amazon EKS add-on to view the following metrics. For more
information, see [Install the
Amazon CloudWatch Observability EKS add-on](../../../AmazonCloudWatch/latest/monitoring/Container-Insights-setup-EKS-addon.md "../../../AmazonCloudWatch/latest/monitoring/Container-Insights-setup-EKS-addon.md").

In Amazon SageMaker Studio, you can navigate to one of your clusters in **HyperPod
clusters** (under **Compute**) and view the
**Metrics** details on your cluster. Metrics provides a comprehensive view of
cluster utilization metrics, including hardware, team, and task metrics. This includes compute
availability and usage, team allocation and utilization, and task run and wait time information.

## Settings

Amazon SageMaker HyperPod provides a view of your cluster settings. The following provides
information on your HyperPod cluster settings.

In Amazon SageMaker Studio you can navigate to one of your clusters in **HyperPod
clusters** (under **Compute**) and view the
**Settings** information on your cluster. The information includes the
following:

- **Instances** details, including instance ID, status, instance type, and
  instance group
- **Instance groups** details, including instance group name, type,
  counts, and compute information
- **Orchestration** details, including the orchestrator, version, and
  certification authority
- **Cluster resiliency** details
- **Security** details, including subnets and security groups

## Details

Amazon SageMaker HyperPod provides a view of your cluster metadata details. The following paragraph
provides information on how to get your HyperPod cluster details.

In Amazon SageMaker Studio, you can navigate to one of your clusters in **HyperPod
clusters** (under **Compute**) and view the
**Details** on your cluster. This includes the tags, logs, and
metadata.
