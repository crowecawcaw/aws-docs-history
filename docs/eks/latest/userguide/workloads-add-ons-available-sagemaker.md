

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Amazon SageMaker add-ons

Amazon SageMaker AI publishes Amazon EKS add-ons for clusters that orchestrate an Amazon SageMaker HyperPod cluster. When you create a HyperPod cluster with Amazon EKS orchestration, HyperPod adds its nodes to your Amazon EKS cluster, and these add-ons build on those nodes and on the HyperPod cluster itself. They add task governance, observability, training job recovery, model deployment, and interactive development environments.

Except for Amazon SageMaker Spaces, these add-ons need an existing HyperPod cluster. Each one depends on HyperPod nodes in the cluster, the HyperPod Amazon Machine Image (AMI), or the Amazon Resource Name (ARN) of the HyperPod cluster. They aren’t supported on Amazon EKS clusters without HyperPod, such as clusters whose nodes are only Amazon EC2 instances, EKS Auto Mode nodes, Fargate, or hybrid nodes. Spaces runs on HyperPod nodes and on Amazon EC2 nodes. For add-ons that run on any Amazon EKS cluster, see [AWS add-ons](workloads-add-ons-available-eks.md).

You install these add-ons the same way as other Amazon EKS add-ons. For more information, see [Create an Amazon EKS add-on](creating-an-add-on.md). You can also install several of them from the HyperPod cluster page in the SageMaker AI console. To create a HyperPod cluster, see [Orchestrating SageMaker HyperPod clusters with Amazon EKS](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks.html) in the *Amazon SageMaker AI Developer Guide*.


| Description | Learn more | Compatible compute types | 
| --- | --- | --- | 
| Set task priorities, compute allocation for each team, and how teams lend and borrow idle compute |  [Amazon SageMaker HyperPod task governance](#addons-hyperpod)  | HyperPod | 
| Collect cluster, GPU, and training job metrics into Amazon Managed Service for Prometheus |  [Amazon SageMaker HyperPod observability](#addons-hyperpod-observability)  | HyperPod | 
| Recover distributed training jobs from faults and hangs without restarting the whole job |  [Amazon SageMaker HyperPod training operator](#addons-hyperpod-training-operator)  | HyperPod | 
| Deploy, scale, and monitor models for inference |  [Amazon SageMaker HyperPod inference operator](#addons-hyperpod-inference-operator)  | HyperPod | 
| Create and manage JupyterLab and Code Editor applications for interactive ML workloads |  [Amazon SageMaker Spaces](#add-ons-amazon-sagemaker-spaces)  | HyperPod, EC2 | 

## Amazon SageMaker HyperPod task governance
<a name="addons-hyperpod"></a>

SageMaker HyperPod task governance manages how teams and projects share the compute in your Amazon EKS cluster. Administrators can set:
+ Priority levels for tasks
+ Compute allocation for each team
+ How each team lends and borrows idle compute
+ Whether a team preempts its own tasks

Task governance also shows cluster capacity in real time, including compute availability and usage, team allocation and utilization, and task run and wait times.

The Amazon EKS add-on name is `amazon-sagemaker-hyperpod-taskgovernance`.

### Prerequisites
<a name="_prerequisites"></a>
+ A HyperPod cluster with Amazon EKS orchestration, with at least one HyperPod node in the Amazon EKS cluster before you install the add-on.
+ Kubernetes version 1.30 or later.

For more information, see [Task governance setup](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance-setup-task-governance.html) in the *Amazon SageMaker AI Developer Guide*.

### Required IAM permissions
<a name="_required_iam_permissions"></a>

This add-on doesn’t require any permissions.

### Additional information
<a name="_additional_information"></a>

To learn more about the add-on, see [SageMaker HyperPod task governance](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance.html).

## Amazon SageMaker HyperPod observability
<a name="addons-hyperpod-observability"></a>

The Amazon SageMaker HyperPod observability add-on deploys and manages monitoring components on your HyperPod cluster, including node exporter, DCGM exporter, kube-state-metrics, and EFA exporter. It forwards metrics to an Amazon Managed Service for Prometheus workspace that you choose, and exposes an OTLP endpoint for custom metrics and events from your training jobs.

The add-on also scrapes metrics from the HyperPod task governance add-on, the HyperPod training operator, Kubeflow, and KEDA. You can view the metrics in Amazon Managed Grafana dashboards to see cluster health, resource utilization, and training job performance.

The Amazon EKS add-on name is `amazon-sagemaker-hyperpod-observability`.

### Prerequisites
<a name="_prerequisites_2"></a>
+ A HyperPod cluster with Amazon EKS orchestration, with at least one node before you install the add-on.

For more information, see [Setting up the SageMaker HyperPod observability add-on](https://docs.aws.amazon.com/sagemaker/latest/dg/hyperpod-observability-addon-setup.html) in the *Amazon SageMaker AI Developer Guide*.

### Required IAM permissions
<a name="_required_iam_permissions_2"></a>

This add-on uses the IAM roles for service accounts capability of Amazon EKS. For more information, see [IAM roles for service accounts](iam-roles-for-service-accounts.md). The following managed policies are required:
+  `AmazonPrometheusRemoteWriteAccess` - for remote writing metrics from the cluster to Amazon Managed Service for Prometheus
+  `CloudWatchAgentServerPolicy` - for remote writing the logs from the cluster to CloudWatch

### Additional information
<a name="_additional_information_2"></a>

To learn more about the add-on and its capabilities, see [SageMaker HyperPod observability](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-cluster-observability-cluster.html).

## Amazon SageMaker HyperPod training operator
<a name="addons-hyperpod-training-operator"></a>

The Amazon SageMaker HyperPod training operator manages distributed training jobs across large GPU clusters. It detects faults and hung jobs and recovers at the process level, so a failure restarts only the affected processes instead of the whole job.

The operator works with HyperPod health monitoring and observability, and monitors training metrics such as loss spikes and throughput degradation. You define recovery policies in YAML, without code changes, to recover jobs that reach an unrecoverable state.

The Amazon EKS add-on name is `amazon-sagemaker-hyperpod-training-operator`.

### Prerequisites
<a name="_prerequisites_3"></a>
+ A HyperPod cluster with Amazon EKS orchestration that runs the latest HyperPod AMI release. To update the AMI, use the `UpdateClusterSoftware` API.
+ If you install the add-on with Amazon EKS, the HyperPod cluster must have the tag `SageMaker` with the value `true`. Otherwise, the installation fails.

For more information, see [Using the HyperPod training operator](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-eks-operator.html) in the *Amazon SageMaker AI Developer Guide*.

### Required IAM permissions
<a name="_required_iam_permissions_3"></a>

This add-on requires IAM permissions, and uses EKS Pod Identity.

 AWS suggests the `AmazonSageMakerHyperPodTrainingOperatorAccess` [managed policy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerHyperPodTrainingOperatorAccess.html).

For more information, see [Installing the training operator](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-eks-operator-install.html#sagemaker-eks-operator-install-operator) in the *Amazon SageMaker AI Developer Guide*.

### Additional information
<a name="_additional_information_3"></a>

To learn more about the add-on, see [SageMaker HyperPod training operator](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-eks-operator.html).

## Amazon SageMaker HyperPod inference operator
<a name="addons-hyperpod-inference-operator"></a>

The Amazon SageMaker HyperPod inference operator deploys, scales, and monitors generative AI models on the same HyperPod compute that you use for training.

You can deploy models with `kubectl`, the Python SDK, Amazon SageMaker Studio, or the HyperPod CLI. The operator scales deployments automatically based on demand, and tracks metrics such as time to first token, latency, and GPU utilization.

The Amazon EKS add-on name is `amazon-sagemaker-hyperpod-inference`.

### Installation methods
<a name="_installation_methods"></a>

You can install this add-on using one of the following methods:
+  **SageMaker AI console**: Creates the IAM roles, Amazon S3 buckets, and dependency add-ons for you, or reuses ones that you already have.
+  **Amazon EKS console or AWS CLI**: Requires you to install the dependency add-ons listed in the following prerequisites before you install the inference operator.

### Prerequisites
<a name="_prerequisites_4"></a>

The inference operator requires a HyperPod cluster with Amazon EKS orchestration. When you install the add-on, you provide the ARN of the HyperPod cluster in the `hyperpodClusterArn` configuration value.

Before installing the inference operator add-on via the EKS Add-ons Console or CLI, ensure the following dependencies are installed.

Required EKS add-ons:
+ Amazon S3 Mountpoint CSI Driver (minimum version: v1.14.1-eksbuild.1)
+ Metrics Server (minimum version: v0.7.2-eksbuild.4)
+ Amazon FSx CSI Driver (minimum version: v1.6.0-eksbuild.1)
+ Cert Manager (minimum version: v1.18.2-eksbuild.2)

For detailed installation instructions for each dependency, see [Installing the inference operator](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-setup.html).

### Required IAM permissions
<a name="_required_iam_permissions_4"></a>

This add-on requires IAM permissions, and uses OIDC/IRSA.

The following managed policies are recommended as they provide the minimum scoped permissions:
+  `AmazonSageMakerHyperPodInferenceAccess` - provides admin privileges required for setting up the inference operator
+  `AmazonSageMakerHyperPodGatedModelAccess` - provides SageMaker HyperPod access to gated models in SageMaker Jumpstart (e.g., Meta Llama, GPT-Neo)

For more information, see [Installing the inference operator](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-setup.html).

### Additional information
<a name="_additional_information_4"></a>

To learn more about the Amazon SageMaker HyperPod inference operator, see [SageMaker HyperPod inference operator](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment.html).

For troubleshooting information, see [Troubleshooting SageMaker HyperPod model deployment](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-ts.html).

## Amazon SageMaker Spaces
<a name="add-ons-amazon-sagemaker-spaces"></a>

With the Amazon SageMaker Spaces add-on, you can run IDEs and notebooks on Amazon EKS clusters, on HyperPod nodes or on Amazon EC2 nodes. Administrators can use EKS Console to install the add-on on their cluster, and define default space configurations such as images, compute resources, local storage for notebook settings (additional storage to be attached to their spaces), file systems, and initialization scripts.

AI developers can use kubectl to create, update, and delete spaces. They have the flexibility to use default configurations provided by admins or customize settings. AI developers can access their spaces on EKS or HyperPod-EKS using their local VS Code IDEs, and/or their web browser that hosts their JupyterLab or CodeEditor IDE on custom DNS domain configured by their admins. They can also use kubernetes’ port forwarding feature to access spaces in their web browsers.

The Amazon EKS add-on name is `amazon-sagemaker-spaces`.

### Required IAM permissions
<a name="_required_iam_permissions_5"></a>

This add-on requires IAM permissions. For more information about the required IAM setup, see [IAM permissions setup](https://docs.aws.amazon.com/sagemaker/latest/dg/permission-setup.html) in the *Amazon SageMaker AI Developer Guide*.

### Additional information
<a name="_additional_information_5"></a>

To learn more about the add-on and its capabilities, see [SageMaker AI notebooks on HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-cluster-ide.html) in the *Amazon SageMaker AI Developer Guide*.