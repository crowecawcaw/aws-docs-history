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

For a list and details about past jobs, use the [`sacct`](https://slurm.schedmd.com/sacct.html "https://slurm.schedmd.com/sacct.html") command from the Slurm
documentation in JupyterLab or a Code Editor terminal. The `sacct` command shows _historical information_ about jobs that have _finished_ or are _complete_ in the system. It
provides accounting information, including job resources usage like memory and exit status.

By default, all Studio users can view, manage, and interact with all available
Slurm tasks. To restrict the viewable tasks to Studio users, see [Restrict task view in Studio for Slurm clusters](sagemaker-hyperpod-studio-setup-slurm.md#sagemaker-hyperpod-studio-setup-slurm-restrict-tasks-view "sagemaker-hyperpod-studio-setup-slurm.md#sagemaker-hyperpod-studio-setup-slurm-restrict-tasks-view").

For Amazon EKS clusters
For Amazon EKS clusters, kubeflow (PyTorch, MPI, TensorFlow) tasks are shown in the table.
PyTorch tasks are shown by default. You can sort for PyTorch, MPI, and TensorFlow under
**Task type**. The information that is shown for each task includes the
task name, status, namespace, priority class, and creation time.

By default, all users can view jobs across all namespaces. To restrict the viewable
Kubernetes namespaces available to Studio users, see [Restrict task view in Studio for EKS clusters](sagemaker-hyperpod-studio-setup-eks.md#sagemaker-hyperpod-studio-setup-eks-restrict-tasks-view "sagemaker-hyperpod-studio-setup-eks.md#sagemaker-hyperpod-studio-setup-eks-restrict-tasks-view"). If a user cannot
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

## IDE and Notebooks

Amazon SageMaker HyperPod provides a view of the development spaces running on your cluster. Spaces
are self-contained environments for running JupyterLab or Code Editor IDEs directly on your
HyperPod EKS cluster. You can create, configure, start, stop, and open spaces directly
from Studio.

In Amazon SageMaker Studio, navigate to one of your clusters in **HyperPod
clusters** (under **Compute**) and choose the **IDE and
Notebooks** tab.

Key capabilities available through Studio include:

- Create spaces with configurable compute, storage, and image settings through a guided
  form.
- View all spaces in a searchable table showing name, application type, status, access
  type, storage, GPU, and vCPU allocations.
- Start and stop spaces with a single click to manage compute costs.
- Open spaces directly in the browser (JupyterLab or Code Editor) or connect through a
  Remote IDE. For more information, see [Remote access using SSH over SSM](vscode-access.md "vscode-access.md").
- Delete spaces that are no longer needed.
- Select namespaces to organize spaces by team with resource quotas and governance
  settings.
- Apply templates for consistent space configurations across teams.

For information on creating a domain, see [Guide to getting set up with Amazon SageMaker AI](gs.md "gs.md").

### Prerequisites

- Install the HyperPod add-on on your cluster. For more information, see
  [Install SageMaker AI Spaces Add-on](operator-install.md "operator-install.md").
- Set up your cluster to be used in Studio. For more information, see
  [Setting up an Amazon EKS cluster in Studio](sagemaker-hyperpod-studio-setup-eks.md "sagemaker-hyperpod-studio-setup-eks.md").
- To enable private spaces among users with the same execution role, you must ensure the
  `ExecutionRoleSessionNameMode` flag is set to `USER_IDENTITY`. With
  the HyperPod Spaces feature, the username used inside the space is automatically
  derived from the Studio authentication context, allowing users to have a consistent
  identity across Studio and HyperPod Spaces without requiring additional
  sign-in.

For Studio domains configured in IAM authentication mode, the Spaces username is
derived from the IAM role session name. This corresponds to the IAM session used to
launch Studio, either through the AWS Management Console or through a presigned
Studio URL. For Studio domains configured in IAM Identity Center authentication mode, the Spaces
username is the sanitized authenticated IAM Identity Center username.

This is set by default for new domains
and can be overridden for older domains. This setting can also be overridden for each user
profile. For more information, see
[Execution role session name mode](execution-roles-and-spaces.md#sagemaker-execution-role-session-name "execution-roles-and-spaces.md#sagemaker-execution-role-session-name").

### How it works

Once the add-on is installed and access is configured, navigate to your
HyperPod cluster in Studio and select the **IDE and Notebooks**
tab to see the spaces management interface.

#### Creating a space

To create a new space, choose **Create space**. The creation form
allows you to configure the following:

- **Namespace**: Select your team namespace with resource
  quotas and governance settings. This determines your available compute allocation.
- **Space settings:**

  - **Template**: Select a pre-configured template (for
    example, JupyterLab or Code Editor) to apply default settings.
  - **Compute**: Choose between GPU and CPU configurations
    with fine-grained control over GPUs, vCPUs, and memory.
  - **GPU partition**: If fractional GPU is enabled, you
    can choose a partition to use for your workspace.
  - **Image**: Select from available container images or
    custom images configured by your administrator.
  - **EBS space storage**: Configure persistent storage
    for your notebooks and data.

- **Task governance**: When enabled for the namespace,
  spaces integrate with HyperPod task governance for resource management and priority
  scheduling. For more information, see [Task governance for Interactive Spaces on HyperPod](task-governance.md "task-governance.md").

#### Managing spaces

The spaces table provides a consolidated view of all your environments, including
status and resource allocations.

From the **Actions** column, you can:

- Stop a running space to release compute resources while preserving your data on EBS
  storage.
- Open the space in your browser to launch the JupyterLab or Code Editor web
  interface.
- Connect using a Remote IDE. For more information, see
  [Remote access using SSH over SSM](vscode-access.md "vscode-access.md").

#### Connecting to your space

Spaces support two connection methods:

**Web UI access**

Choose **Open** from the spaces table to launch the IDE directly in
your browser. This opens a fully functional JupyterLab or Code Editor interface hosted on
your HyperPod cluster. No local software installation is required beyond a web
browser. This is ideal for quick iterations, notebook-based exploration, and collaborative
work. To enable Web UI access on your cluster, see [Web browser access](browser-access.md "browser-access.md").

**Remote IDE connection**

Choose **Open in Remote IDE** from the spaces table to connect your
local IDE to the space running on HyperPod. This provides a secure connection
without requiring you to manage SSH keys or expose port 22. You get the full power of your
local development environment while running code on HyperPod cluster compute. For
more information, see [Remote access using SSH over SSM](vscode-access.md "vscode-access.md").

## Details

Amazon SageMaker HyperPod provides a view of your cluster metadata details. The following paragraph
provides information on how to get your HyperPod cluster details.

In Amazon SageMaker Studio, you can navigate to one of your clusters in **HyperPod
clusters** (under **Compute**) and view the
**Details** on your cluster. This includes the tags, logs, and
metadata.
