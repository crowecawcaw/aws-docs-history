# GitHub repositories

To launch a training job, you utilize files from two distinct GitHub
repositories:

- [SageMaker HyperPod recipes](https://github.com/aws/sagemaker-hyperpod-recipes "https://github.com/aws/sagemaker-hyperpod-recipes")
- [SageMaker HyperPod training adapter for NeMo](https://github.com/aws/sagemaker-hyperpod-training-adapter-for-nemo "https://github.com/aws/sagemaker-hyperpod-training-adapter-for-nemo")
  These repositories contain essential components for initiating, managing, and
  customizing Large Language Model (LLM) training processes. You use the scripts from
  the repositories to set up and run the training jobs for your LLMs.

## HyperPod recipe

repository

Use the [SageMaker HyperPod recipes](https://github.com/aws/sagemaker-hyperpod-recipes "https://github.com/aws/sagemaker-hyperpod-recipes") repository to get a recipe.

1. `main.py`: This file serves as the primary entry point for
   initiating the process of submitting a training job to either a cluster
   or a SageMaker training job.
2. `launcher_scripts`: This directory contains a collection of
   commonly used scripts designed to facilitate the training process for
   various Large Language Models (LLMs).
3. `recipes_collection`: This folder houses a compilation of
   pre-defined LLM recipes provided by the developers. Users can leverage
   these recipes in conjunction with their custom data to train LLM models
   tailored to their specific requirements.

You use the SageMaker HyperPod recipes to launch training or fine-tuning jobs.
Regardless of the cluster you're using, the process of submitting the job is the
same. For example, you can use the same script to submit a job to a Slurm or
Kubernetes cluster. The launcher dispatches a training job based on three
configuration files:

1. General Configuration (`config.yaml`): Includes common
   settings such as the default parameters or environment variables used in
   the training job.
2. Cluster Configuration (cluster): For training jobs using clusters
   only. If you're submitting a training job to a Kubernetes cluster, you
   might need to specify information such as volume, label, or restart
   policy. For Slurm clusters, you might need to specify the Slurm job
   name. All the parameters are related to the specific cluster that you're
   using.
3. Recipe (recipes): Recipes contain the settings for your training job,
   such as the model types, sharding degree, or dataset paths. For example,
   you can specify Llama as your training model and train it using model or
   data parallelism techniques like Fully Sharded Distributed Parallel
   (FSDP) across eight machines. You can also specify different checkpoint
   frequencies or paths for your training job.

After you've specified a recipe, you run the launcher script to specify an
end-to-end training job on a cluster based on the configurations through the
`main.py` entry point. For each recipe that you use, there are
accompanying shell scripts located in the launch_scripts folder. These examples
guide you through submitting and initiating training jobs. The following figure
illustrates how a SageMaker HyperPod recipe launcher submits a training job to a
cluster based on the preceding. Currently, the SageMaker HyperPod recipe launcher is
built on top of the Nvidia NeMo Framework Launcher. For more information, see
[NeMo Launcher Guide](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html "https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html").

![Diagram illustrating the HyperPod recipe launcher workflow. On the left, inside a dashed box, are three file icons labeled "Recipe", "config.yaml", and "slurm.yaml or k8s.yaml or sm_job.yaml (Cluster config)". An arrow points from this box to a central box labeled "HyperPod recipe Launcher". From this central box, another arrow points right to "Training Job", with "main.py" written above the arrow.](images/sagemaker-hyperpod-recipe-launcher.png)

## HyperPod recipe adapter repository

The SageMaker HyperPod training adapter is a training framework. You can use it to
manage the entire lifecycle of your training jobs. Use the adapter to distribute
the pre-training or fine-tuning of your models across multiple machines. The
adaptor uses different parallelism techniques to distribute the training. It
also handles the implementation and management of saving the checkpoints. For
more details, see [Advanced
settings](cluster-specific-configurations-advanced-settings.md "cluster-specific-configurations-advanced-settings.md").

Use the [SageMaker HyperPod recipe adapter repository](https://github.com/aws/sagemaker-hyperpod-training-adapter-for-nemo "https://github.com/aws/sagemaker-hyperpod-training-adapter-for-nemo") to use the recipe
adapter.

1. `src`: This directory contains the implementation of
   Large-scale Language Model (LLM) training, encompassing various features
   such as model parallelism, mixed-precision training, and checkpointing
   management.
2. `examples`: This folder provides a collection of examples
   demonstrating how to create an entry point for training an LLM model,
   serving as a practical guide for users.
