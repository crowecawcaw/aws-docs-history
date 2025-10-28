# SageMaker HyperPod recipes

Amazon SageMaker HyperPod recipes are pre-configured training stacks provided by AWS to help you
quickly start training and fine-tuning publicly available foundation models (FMs) from
various model families such as Llama, Mistral, Mixtral, or DeepSeek. Recipes automate the
end-to-end training loop, including loading datasets, applying distributed training
techniques, and managing checkpoints for faster recovery from faults.

SageMaker HyperPod recipes are particularly beneficial for users who may not have deep machine
learning expertise, as they abstract away much of the complexity involved in training large
models.

You can run recipes within SageMaker HyperPod or as SageMaker training jobs.

The following tables are maintained in the SageMaker HyperPod GitHub repository and provide the
most up-to-date information on the models supported for pre-training and fine-tuning, their
respective recipes and launch scripts, supported instance types, and more.

- For the most current list of supported models, recipes, and launch scripts for
  pre-training, see the [pre-training table](https://github.com/aws/sagemaker-hyperpod-recipes?tab=readme-ov-file#pre-training "https://github.com/aws/sagemaker-hyperpod-recipes?tab=readme-ov-file#pre-training").
- For the most current list of supported models, recipes, and launch scripts for
  fine-tuning, see the [fine-tuning table](https://github.com/aws/sagemaker-hyperpod-recipes?tab=readme-ov-file#fine-tuning "https://github.com/aws/sagemaker-hyperpod-recipes?tab=readme-ov-file#fine-tuning").
  For SageMaker HyperPod users, the automation of end-to-end training workflows comes from the
  integration of the training adapter with SageMaker HyperPod recipes. The training adapter is built
  on the [NVIDIA NeMo framework](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html "https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html") and the [Neuronx Distributed Training package](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/libraries/neuronx-distributed/index.html "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/libraries/neuronx-distributed/index.html"). If you're familiar with using NeMo, the
  process of using the training adapter is the same. The training adapter runs the recipe on
  your cluster.

![Diagram showing SageMaker HyperPod recipe workflow. A "Recipe" icon at the top feeds into a "HyperPod recipe launcher" box. This box connects to a larger section labeled "Cluster: Slurm, K8s, ..." containing three GPU icons with associated recipe files. The bottom of the cluster section is labeled "Train with HyperPod Training Adapter".](images/sagemaker-hyperpod-recipes-overview.png)
You can also train your own model by defining your own custom recipe.

To get started with a tutorial, see [Tutorials](sagemaker-hyperpod-recipes-tutorials.md "sagemaker-hyperpod-recipes-tutorials.md").

###### Topics

- [Tutorials](sagemaker-hyperpod-recipes-tutorials.md "sagemaker-hyperpod-recipes-tutorials.md")
- [Default configurations](default-configurations.md "default-configurations.md")
- [Cluster-specific
  configurations](cluster-specific-configurations.md "cluster-specific-configurations.md")
- [Considerations](cluster-specific-configurations-special-considerations.md "cluster-specific-configurations-special-considerations.md")
- [Advanced
  settings](cluster-specific-configurations-advanced-settings.md "cluster-specific-configurations-advanced-settings.md")
- [Appendix](appendix.md "appendix.md")
