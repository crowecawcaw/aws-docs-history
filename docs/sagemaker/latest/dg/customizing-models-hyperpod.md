

# HyperPod
<a name="customizing-models-hyperpod"></a>

HyperPod runs model customization on persistent compute clusters that remain available across multiple training jobs. HyperPod provides automatic fault detection and recovery, making it ideal for large-scale and long-running training workloads.

For ephemeral training jobs, see [SageMaker AI Training Jobs](customizing-models-training-jobs.md). For fully managed serverless training, see [Serverless model customization](customize-model.md).

For supported customization techniques and training types, see [Customization techniques](customizing-models-techniques.md).

## Overview
<a name="hyperpod-customize-overview"></a>

### Regional availability
<a name="hyperpod-regional"></a>

Available in all [HyperPod supported regions](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html#sagemaker-hyperpod-available-regions).

### Orchestration options
<a name="hyperpod-orchestration"></a>
+ **HyperPod with Amazon EKS** — Interfaces: Recipes, HP-CLI. Use Kubernetes-based workload orchestration with dynamic capacity management and containerized training jobs.
+ **HyperPod with Slurm** — Interfaces: Recipes. Use Slurm-based job scheduling with head, login, and worker node configuration.

### Supported techniques and training types
<a name="hyperpod-supported-techniques-types"></a>

HyperPod supports all customization techniques and training types. See [Customization techniques](customizing-models-techniques.md) and [Training types](customizing-models-training-types.md).

## Getting started
<a name="hyperpod-customize-getting-started"></a>

If this is your first time using HyperPod, see [Prerequisites for using SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.html) to set up your cluster.

To run model customization on an existing HyperPod cluster:

1. Clone the recipes repository: 

   ```
   git clone --recursive https://github.com/aws/sagemaker-hyperpod-recipes.git
   cd sagemaker-hyperpod-recipes
   pip3 install -r requirements.txt
   ```

1. Choose a recipe from `recipes_collection/recipes/fine-tuning/`.

1. Configure cluster-specific settings (see [Cluster-specific configurations](https://docs.aws.amazon.com/sagemaker/latest/dg/cluster-specific-configurations.html)).

1. Launch using the appropriate method: 
   + **EKS:** Use the launcher script or HP-CLI
   + **Slurm:** Use the launcher script

For detailed tutorials and the full recipe catalog, see [SageMaker AI Recipes documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-recipes.html).

For more information about HyperPod, see [Amazon SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html).