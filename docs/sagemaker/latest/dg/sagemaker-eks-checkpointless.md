# Checkpointless training in Amazon SageMaker HyperPod

Checkpointless training on Amazon SageMaker HyperPod enables faster recovery from training infrastructure
faults. The following documentation helps you get started with checkpointless training and
fine-tuning for NeMo-supported models.

Checkpointless training has the following pre-requisites:

- [Getting started with Amazon EKS support in
  SageMaker HyperPod](sagemaker-hyperpod-eks-prerequisites.md "sagemaker-hyperpod-eks-prerequisites.md")
- [Installing the training operator](sagemaker-eks-operator-install.md "sagemaker-eks-operator-install.md"). You must install v1.2.0 or above.

Checkpointless training on SageMaker HyperPod is built on top of the [NVIDIA NeMo Framework User Guide](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/exp_manager.html#experiment-manager "https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/exp_manager.html#experiment-manager"). You can run
checkpointless training with pre-created SageMaker HyperPod recipes. If you're familiar with NeMo,
the process of using the checkpointless training recipes is similar. With minor changes,
you can start training a model using checkpointless training features that enable you to
recover quickly from training faults.

The following HyperPod recipes are pre-configured with checkpointless training optimizations. You can
specify your data paths as part of the recipe and use the associated launch script to run training
(see the quick start guide below):

| Model   | Method                | Size | Nodes | Instance    | Accelerator | Recipe                                                                                                                                                                                                                                                                                                                              | Script                                                                                                                                                                                                                                                                                      | Tutorial                                                                                                                        |
| ------- | --------------------- | ---- | ----- | ----------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| GPT OSS | Full finetune example | 120b | 16    | p5.48xlarge | GPU H100    | [link](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/fine-tuning/gpt_oss/checkpointless_gpt_oss_120b_full_fine_tuning.yaml "https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/fine-tuning/gpt_oss/checkpointless_gpt_oss_120b_full_fine_tuning.yaml") | [link](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/launcher_scripts/gpt_oss/run_checkpointless_gpt_oss_120b_full_fine_tuning.sh "https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/launcher_scripts/gpt_oss/run_checkpointless_gpt_oss_120b_full_fine_tuning.sh") | [link](sagemaker-eks-checkpointless-recipes-finetune.md "sagemaker-eks-checkpointless-recipes-finetune.md")                     |
| GPT OSS | LoRA-example          | 120b | 2     | p5.48xlarge | GPU H100    | [link](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/fine-tuning/gpt_oss/checkpointless_gpt_oss_120b_lora.yaml "https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/fine-tuning/gpt_oss/checkpointless_gpt_oss_120b_lora.yaml")                         | [link](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/launcher_scripts/gpt_oss/run_checkpointless_gpt_oss_120b_lora.sh "https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/launcher_scripts/gpt_oss/run_checkpointless_gpt_oss_120b_lora.sh")                         | [link](sagemaker-eks-checkpointless-recipes-peft.md "sagemaker-eks-checkpointless-recipes-peft.md")                             |
| Llama3  | Pretrain example      | 70b  | 16    | p5.48xlarge | GPU H100    | [link](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/training/llama/checkpointless_llama3_70b_pretrain.yaml "https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/training/llama/checkpointless_llama3_70b_pretrain.yaml")                               | [link](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/launcher_scripts/llama/run_checkpointless_llama3_70b_pretrain.sh "https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/launcher_scripts/llama/run_checkpointless_llama3_70b_pretrain.sh")                         | [link](sagemaker-eks-checkpointless-recipes-pretraining-llama3.md "sagemaker-eks-checkpointless-recipes-pretraining-llama3.md") |
| Llama3  | LoRA-example          | 70b  | 2     | p5.48xlarge | GPU H100    | [link](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/fine-tuning/llama/checkpointless_llama3_70b_lora.yaml "https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/fine-tuning/llama/checkpointless_llama3_70b_lora.yaml")                                 | [link](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/launcher_scripts/llama/run_checkpointless_llama3_70b_lora.sh "https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/launcher_scripts/llama/run_checkpointless_llama3_70b_lora.sh")                                 | [link](sagemaker-eks-checkpointless-recipes-peft-llama.md "sagemaker-eks-checkpointless-recipes-peft-llama.md")                 |

The following quick-start guide provides tutorials for using checkpointless training recipes:

**Getting started examples**

- [Tutorials - Amazon SageMaker HyperPod Checkpointless Full Finetuning GPT OSS 120b](sagemaker-eks-checkpointless-recipes-finetune.md "sagemaker-eks-checkpointless-recipes-finetune.md")
- [Tutorials - Amazon SageMaker HyperPod Checkpointless PEFT-LoRA GPT OSS 120b](sagemaker-eks-checkpointless-recipes-peft.md "sagemaker-eks-checkpointless-recipes-peft.md")
- [Tutorials - Amazon SageMaker HyperPod Checkpointless Pretraining Llama 3 70b](sagemaker-eks-checkpointless-recipes-pretraining-llama3.md "sagemaker-eks-checkpointless-recipes-pretraining-llama3.md")
- [Tutorials - Amazon SageMaker HyperPod Checkpointless PEFT-LoRA Llama 3 70b](sagemaker-eks-checkpointless-recipes-peft-llama.md "sagemaker-eks-checkpointless-recipes-peft-llama.md")
  If you’d like to pre-train or fine-tune custom models, see [Tutorials - Amazon SageMaker HyperPod Checkpointless Pretraining or Finetuning Custom Models](sagemaker-eks-checkpointless-recipes-custom.md "sagemaker-eks-checkpointless-recipes-custom.md").

To learn more about incorporating specific checkpointless training components, [HyperPod checkpointless training features](sagemaker-eks-checkpointless-features.md "sagemaker-eks-checkpointless-features.md").
