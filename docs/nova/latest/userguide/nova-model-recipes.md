# Amazon Nova recipes

You can get an Amazon Nova recipe from the [recipes](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes "https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes") repository. An Amazon Nova recipe is a [YAML](https://yaml.org/ "https://yaml.org/") configuration file that provides details to
SageMaker on how to run your model customization job. It provides the base model name, sets
training hyperparameters, defines optimization settings, and includes any additional
options required to fine-tune or train the model successfully.

You can also access Amazon Nova recipes through Amazon SageMaker Studio and by navigating
to the model hub, selecting AWS, and browsing Amazon Nova models to find
their associated recipes. Both Amazon SageMaker Studio and provide sample notebooks
for each recipe, which include all the necessary steps to modify the recipes and run
customization jobs using SageMaker training jobs or SageMaker HyperPod environments.

To access the recipes pages in Amazon SageMaker Studio, the execution role must have the
following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::*model-customization-recipes*"
 ]
 }
 ]
}`

```

To execute the sample notebooks on SageMaker training jobs and , use one of the
following SageMaker distribution image versions: `2.7.1+`, `2.8.0+`, `3.2.1+`, `3.3.0+`. This applies
to both Amazon SageMaker Studio and .

###### Topics

- [Getting Amazon Nova recipes](#nova-model-get-recipes "#nova-model-get-recipes")
- [Getting Amazon Nova Forge recipes](#nova-model-get-forge-recipes "#nova-model-get-forge-recipes")
- [Available models and algorithms](#nova-model-algorithm "#nova-model-algorithm")
- [Amazon Nova Lite](#nova-model-recipes-reference-novalite "#nova-model-recipes-reference-novalite")
- [Amazon Nova Micro](#nova-model-recipes-reference-novamicro "#nova-model-recipes-reference-novamicro")
- [Amazon Nova Pro](#nova-model-recipes-reference-novapro "#nova-model-recipes-reference-novapro")

## Getting Amazon Nova recipes

To get a base Amazon Nova recipe, clone the [recipes](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes "https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes") repository by running the following
command.

```
git clone https://github.com/aws/sagemaker-hyperpod-recipes.git
```

The base recipes are available at [`recipes_collection/recipes/`](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/ "https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/").

```
cd recipes_collection/recipes/
```

The Amazon Nova customization recipes are in the following folders.

| Recipe type                                             | Folder                                                                                                                                                                                                                                |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SFT (Full-rank and PEFT), PPO, DPO (Full-rank and PEFT) | [fine-tuning/nova](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/fine-tuning/nova "https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/fine-tuning/nova") |
| Evaluation                                              | [evaluation/nova](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/evaluation/nova "https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/evaluation/nova")    |
| CPT                                                     | [training/nova](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/training "https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/training")                    |

## Getting Amazon Nova Forge recipes

To access specialized Amazon Nova Forge recipes for jobs, please [set up your access to Amazon Nova Forge](nova-forge-access.md "nova-forge-access.md") and then follow [this workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/dcac6f7a-3c61-4978-8344-7535526bf743/en-US/02-smhp-rig/03-nova-forge "https://catalog.us-east-1.prod.workshops.aws/workshops/dcac6f7a-3c61-4978-8344-7535526bf743/en-US/02-smhp-rig/03-nova-forge") to set up the Forge version of the CLI. For SageMaker Training Jobs, the AWS Console and Nova Customization SDK will automatically access Forge recipes.

## Available models and algorithms

The following table summarizes the availability of customization for Amazon Nova models
and supported algorithms using SageMaker.

| Model name           | Model ID                     | Fine-tuning | Notes                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------- | ---------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon Nova Lite 2.0 | amazon.nova-2-lite-v1:0:256k | Yes         | • SFT - Accepts either text and/or image or text and/or video as the<br>input and produces text as output. A single job can't combine text,<br>image, and video in the same run.<br>• DPO - Accepts text and image as the input and produces text as<br>output.<br>• RFT - Accepts text and image as input for single-turn conversations and produces text as output. Improved reward optimization capabilities. |

## Amazon Nova Lite

The table below lists detailed information of the Amazon Nova Lite recipes reference.

| Model     | Category/Sub-category           | Technique                             | Recipe Name                                                                                                                            | Image URI (Training Jobs)                                                             | Image URI (SageMaker HyperPod)                                                           | Compute Instance                                                                                                   |
| --------- | ------------------------------- | ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Nova Lite | Training/Fine-tuning            | Supervised Fine-Tuning (LoRA)         | `nova_lite_1_0_g5_g6_12x_gpu_lora_sft.yaml`<br>`nova_lite_1_0_g5_g6_48x_gpu_lora_sft.yaml`<br>`nova_lite_1_0_p5_p4d_gpu_lora_sft.yaml` | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-TJ-SFT-latest`   | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-latest`      | `ml.p5.48xlarge`, `ml.p5en.48xlarge`,<br>`ml.g5.12xlarge`, `ml.g6.12xlarge`,<br>`ml.g5.48xlarge`, `ml.g6.48xlarge` |
| Nova Lite | Training/Fine-tuning            | Supervised Fine-Tuning (Full)         | `nova_lite_1_0_p5_p4d_gpu_sft.yaml`                                                                                                    | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-TJ-SFT-latest`   | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-latest`      | `ml.p5.48xlarge`, `ml.p5en.48xlarge`                                                                               |
| Nova Lite | Training/Fine-tuning            | Direct Preference Optimization (Full) | `nova_lite_1_0_p5_p4d_gpu_dpo.yaml`                                                                                                    | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-TJ-DPO-latest`   | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-DPO-latest`      | `ml.p5.48xlarge`, `ml.p5en.48xlarge`                                                                               |
| Nova Lite | Training/Fine-tuning            | Direct Preference Optimization (LoRA) | `nova_lite_1_0_p5_p4d_gpu_lora_dpo.yaml`<br>`nova_lite_1_0_g5_g6_48x_gpu_lora_dpo.yaml`                                                | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-TJ-DPO-latest`   | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-DPO-latest`      | `ml.p5.48xlarge`, `ml.p5en.48xlarge`,<br>`ml.g5.48xlarge`, `ml.g6.48xlarge`                                        |
| Nova Lite | Training/Reinforcement learning | Reinforcement Fine-Tuning (RFT)       | `nova_lite_1_0_p5_gpu_ppo.yaml`                                                                                                        | n/a                                                                                   | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SMHP-PPO-TRAIN-latest` | `ml.p5.48xlarge`, `ml.p5en.48xlarge`                                                                               |
| Nova Lite | Training/Continued Pre-Training | Continued Pre-Training (base model)   | `nova_lite_gpu_p5x16_pretrain.yaml`                                                                                                    | n/a                                                                                   | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:HP-CPT-latest`         | `ml.p5.48xlarge`                                                                                                   |
| Nova Lite | Evaluation/Evaluate             | Standard text benchmarks              | `nova_lite_p5_48xl_general_text_benchmark_eval.yaml`                                                                                   | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-TJ-Eval-latest` | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-latest`    | `ml.p5.48xlarge`                                                                                                   |
| Nova Lite | Evaluation/Evaluate             | Custom dataset evaluation             | `nova_lite_p5_48xl_bring_your_own_dataset_eval.yaml`                                                                                   | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-TJ-Eval-latest` | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-latest`    | `ml.p5.48xlarge`                                                                                                   |
| Nova Lite | Evaluation/Evaluate             | Multi-modal benchmarks                | `nova_lite_p5_48_general_multi_modal_benchmark_eval.yaml`                                                                              | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-TJ-Eval-latest` | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-latest`    | `ml.p5.48xlarge`                                                                                                   |
| Nova Lite | Evaluation/Evaluate             | LLM as a Judge                        | `nova_lite_p5_48xl_llm_judge_eval.yaml`                                                                                                | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-TJ-Eval-latest` | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-latest`    | `ml.p5.48xlarge`                                                                                                   |

## Amazon Nova Micro

The table below lists detailed information of the Amazon Nova Micro recipes reference.

| Model      | Category/Sub-category           | Technique                                 | Recipe Name                                                                                                                               | Image URI (Training Jobs)                                                             | Image URI (SageMaker HyperPod)                                                           | Compute Instance                                                                                                                      |
| ---------- | ------------------------------- | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Nova Micro | Training/Fine-tuning            | Supervised Fine-Tuning (LoRA)             | `nova_micro_1_0_p5_p4d_gpu_lora_sft.yaml`<br>`nova_micro_1_0_g5_g6_12x_gpu_lora_sft.yaml`<br>`nova_micro_1_0_g5_g6_48x_gpu_lora_sft.yaml` | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-TJ-SFT-latest`   | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-latest`      | `ml.p5.48xlarge`, `ml.p5en.48xlarge`, `ml.p4d.24xlarge`,<br>`ml.g5.12xlarge`, `ml.g6.12xlarge`,<br>`ml.g5.48xlarge`, `ml.g6.48xlarge` |
| Nova Micro | Training/Fine-tuning            | Supervised Fine-Tuning (Full)             | `nova_micro_1_0_p5_p4d_gpu_sft.yaml`<br>`nova_micro_1_0_g5_g6_48x_gpu_sft.yaml`                                                           | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-TJ-SFT-latest`   | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-latest`      | `ml.p5.48xlarge`, `ml.p5en.48xlarge`, `ml.p4d.24xlarge`,<br>`ml.g5.48xlarge`, `ml.g6.48xlarge`                                        |
| Nova Micro | Training/Fine-tuning            | Direct Preference Optimization (LoRA)     | `nova_micro_1_0_g5_g6_12x_gpu_lora_dpo.yaml`<br>`nova_micro_1_0_g5_g6_48x_gpu_lora_dpo.yaml`<br>`nova_micro_1_0_p5_p4d_gpu_lora_dpo.yaml` | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-TJ-DPO-latest`   | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-DPO-latest`      | `ml.p5.48xlarge`, `ml.p5en.48xlarge`, `ml.p4d.24xlarge`,<br>`ml.g5.12xlarge`, `ml.g6.12xlarge`,<br>`ml.g5.48xlarge`, `ml.g6.48xlarge` |
| Nova Micro | Training/Fine-tuning            | Direct Preference Optimization (Full)     | `nova_micro_1_0_p5_p4d_gpu_dpo.yaml`                                                                                                      | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-TJ-DPO-latest`   | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-DPO-latest`      | `ml.p5.48xlarge`, `ml.p5en.48xlarge`, `ml.p4d.24xlarge`                                                                               |
| Nova Micro | Training/Reinforcement learning | Reinforcement Fine-Tuning (RFT)           | `nova_micro_1_0_p5_gpu_ppo.yaml`                                                                                                          | n/a                                                                                   | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SMHP-PPO-TRAIN-latest` | `ml.p5.48xlarge`, `ml.p5en.48xlarge`                                                                                                  |
| Nova Micro | Training/Continued Pre-Training | Continued Pre-Training (Base Model)       | `nova_micro_gpu_p5x8_pretrain.yaml`                                                                                                       | n/a                                                                                   | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:HP-CPT-latest`         | `ml.p5.48xlarge`                                                                                                                      |
| Nova Micro | Evaluation/Evaluate             | General text benchmark                    | `nova_micro_p5_48xl_general_text_benchmark_eval.yaml`                                                                                     | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-TJ-Eval-latest` | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-latest`    | `ml.p5.48xlarge`                                                                                                                      |
| Nova Micro | Evaluation/Evaluate             | Bring your own dataset (gen_qa) benchmark | `nova_micro_p5_48xl_bring_your_own_dataset_eval.yaml`                                                                                     | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-TJ-Eval-latest` | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-latest`    | `ml.p5.48xlarge`                                                                                                                      |
| Nova Micro | Evaluation/Evaluate             | LLM as a Judge                            | `nova_micro_p5_48xl_llm_judge_eval.yaml`                                                                                                  | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-TJ-Eval-latest` | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-latest`    | `ml.p5.48xlarge`                                                                                                                      |

## Amazon Nova Pro

The table below lists detailed information of the Amazon Nova Pro recipes reference.

| Model    | Category/Sub-category           | Technique                             | Recipe Name                                                | Image URI (Training Jobs)                                                             | Image URI (SageMaker HyperPod)                                                             | Compute Instance                                        |
| -------- | ------------------------------- | ------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------- |
| Nova Pro | Training/Fine-tuning            | Supervised Fine-Tuning (LoRA)         | `nova_pro_1_0_p5_p4d_gpu_lora_sft.yaml`                    | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-TJ-SFT-latest`   | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-latest`        | `ml.p5.48xlarge`, `ml.p5en.48xlarge`, `ml.p4d.24xlarge` |
| Nova Pro | Training/Fine-tuning            | Supervised Fine-Tuning (Full)         | `nova_pro_1_0_p5_p4d_gpu_sft.yaml`                         | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-TJ-SFT-latest`   | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-latest`        | `ml.p5.48xlarge`, `ml.p5en.48xlarge`                    |
| Nova Pro | Training/Fine-tuning            | Direct Preference Optimization (Full) | `nova_pro_1_0_p5_gpu_dpo.yaml`                             | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-TJ-DPO-latest`   | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-DPO-latest`        | `ml.p5.48xlarge`, `ml.p5en.48xlarge`                    |
| Nova Pro | Training/Fine-tuning            | Direct Preference Optimization (LoRA) | `nova_pro_1_0_p5_p4d_gpu_lora_dpo.yaml`                    | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-TJ-DPO-latest`   | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-DPO-latest`        | `ml.p5.48xlarge`, `ml.p5en.48xlarge`, `ml.p4d.24xlarge` |
| Nova Pro | Training/Reinforcement learning | Reinforcement Fine-Tuning (RFT)       | `nova_pro_1_0_p5_gpu_ppo.yaml`                             | n/a                                                                                   | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SMHP-PPO-TRAIN-latest`   | `ml.p5.48xlarge`, `ml.p5en.48xlarge`                    |
| Nova Pro | Training/Continued Pre-Training | Continued Pre-Training (Base Model)   | `nova_pro_gpu_p5x24_pretrain.yaml`                         | n/a                                                                                   | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:HP-CPT-latest`           | `ml.p5.48xlarge`                                        |
| Nova Pro | Training/Data augmentation      | Model distillation for post-training  | `nova_pro_r5_cpu_distill.yaml`                             | n/a                                                                                   | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-distillation-repo:SM-TJ-DISTILL-LATEST` | `ml.r5.24xlarge`                                        |
| Nova Pro | Evaluation/Evaluate             | Standard text benchmarks              | `nova_pro_p5_48xl_general_text_benchmark_eval.yaml`        | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-TJ-Eval-latest` | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-latest`      | `ml.p5.48xlarge`                                        |
| Nova Pro | Evaluation/Evaluate             | Custom dataset evaluation             | `nova_pro_p5_48xl_bring_your_own_dataset_eval.yaml`        | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-TJ-Eval-latest` | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-latest`      | `ml.p5.48xlarge`                                        |
| Nova Pro | Evaluation/Evaluate             | Multi-modal benchmarks                | `nova_pro_p5_48xl_general_multi_modal_benchmark_eval.yaml` | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-TJ-Eval-latest` | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-latest`      | `ml.p5.48xlarge`                                        |
| Nova Pro | Evaluation/Evaluate             | LLM as a Judge                        | `nova_pro_p5_48xl_llm_judge_eval.yaml`                     | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-TJ-Eval-latest` | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-latest`      | `ml.p5.48xlarge`                                        |
