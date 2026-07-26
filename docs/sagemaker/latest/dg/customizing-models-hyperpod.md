# HyperPod

HyperPod runs model customization on persistent compute clusters that remain available
across multiple training jobs. HyperPod provides automatic fault detection and recovery,
making it ideal for large-scale and long-running training workloads.

For ephemeral training jobs, see [SageMaker AI Training Jobs](customizing-models-training-jobs.md "customizing-models-training-jobs.md"). For
fully managed serverless training, see [Serverless model customization](customize-model.md "customize-model.md").

For supported customization techniques and training types, see
[Customization techniques](customizing-models-techniques.md "customizing-models-techniques.md").

## Overview

### Regional availability

Available in all [HyperPod supported regions](sagemaker-hyperpod.md#sagemaker-hyperpod-available-regions "sagemaker-hyperpod.md#sagemaker-hyperpod-available-regions").

### Orchestration options

- **HyperPod with Amazon EKS** —
  Interfaces: Recipes, HP-CLI. Use Kubernetes-based workload orchestration with
  dynamic capacity management and containerized training jobs.
- **HyperPod with Slurm** —
  Interfaces: Recipes. Use Slurm-based job scheduling with head, login, and worker
  node configuration.

### Supported techniques and training types

HyperPod supports all customization techniques and training types. See
[Customization techniques](customizing-models-techniques.md "customizing-models-techniques.md") and
[Training types](customizing-models-training-types.md "customizing-models-training-types.md").

## Getting started

If this is your first time using HyperPod, see [Prerequisites for
using SageMaker AI HyperPod](sagemaker-hyperpod-prerequisites.md "sagemaker-hyperpod-prerequisites.md") to set up your cluster.

To run model customization on an existing HyperPod cluster:

1. Clone the recipes repository:

```
git clone --recursive https://github.com/aws/sagemaker-hyperpod-recipes.git
cd sagemaker-hyperpod-recipes
pip3 install -r requirements.txt
```

2. Choose a recipe from `recipes_collection/recipes/fine-tuning/`.
3. Configure cluster-specific settings (see [Cluster-specific
   configurations](cluster-specific-configurations.md "cluster-specific-configurations.md")).
4. Launch using the appropriate method:

   - **EKS:** Use the launcher script or HP-CLI
   - **Slurm:** Use the launcher script

For detailed tutorials and the full recipe catalog, see [SageMaker AI Recipes
documentation](sagemaker-hyperpod-recipes.md "sagemaker-hyperpod-recipes.md").

For more information about HyperPod, see [Amazon SageMaker AI HyperPod](sagemaker-hyperpod.md "sagemaker-hyperpod.md").
