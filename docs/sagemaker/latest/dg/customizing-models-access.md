# How to access model customization

Amazon SageMaker AI provides multiple interfaces for model customization. The following table
summarizes your options — choose the interface that best fits your workflow and
level of control.

| Interface                          | Infrastructure                                                                                                                                                              | Best for                                     | Control level                                 |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | --------------------------------------------- |
| Studio UI                          | [Serverless](customize-model.md "customize-model.md")                                                                                                                       | Quick experimentation, no-code users         | Guided — select model, technique, upload data |
| Python SDK (`SFTTrainer`, etc.)    | [Serverless](customize-model.md "customize-model.md")                                                                                                                       | Reproducible pipelines, automation           | Programmatic — specify all params in code     |
| Python SDK (`ModelTrainer`)        | [SageMaker AI Training Jobs](customizing-models-training-jobs.md "customizing-models-training-jobs.md")                                                                     | Custom instances, advanced configs           | Full — choose instance type, count, image     |
| Recipes                            | [Training Jobs](customizing-models-training-jobs.md "customizing-models-training-jobs.md") +<br>[HyperPod](customizing-models-hyperpod.md "customizing-models-hyperpod.md") | Pre-configured best practices                | Recipe-driven — modify YAML config            |
| HP-CLI                             | [HyperPod](customizing-models-hyperpod.md "customizing-models-hyperpod.md") (EKS)                                                                                           | Kubernetes-native teams                      | Full — Kubernetes job submission              |
| Agent (Model customization skills) | [Serverless](customize-model.md "customize-model.md")                                                                                                                       | Natural language workflow, guided experience | Conversational — describe what you need       |

## Studio UI

The SageMaker AI Studio console provides visual workflows for model customization
without writing code.

**Customize with UI**

The primary entry point for serverless model customization. Walk through
a guided workflow:

1. Select a foundation model from the catalog
2. Choose a customization technique (SFT, DPO, RLVR, RLAIF)
3. Select a training type (LoRA or FFT)
4. Upload or specify your training dataset (S3 path)
5. Configure hyperparameters
6. Launch the training job

Monitor progress in real time with live metrics and logs.

**JumpStart model hub**
Browse and discover foundation models available for customization.
Filter by provider, task, or model size. From a model detail card, you can
launch customization directly.

**Agent-Guided experience**
Use Amazon SageMaker AI Skills for a conversational approach to model
customization. Describe what you want to achieve in natural language, and the
agent guides you through model selection, dataset preparation, and job
configuration. For more information, see [Model customization agent skills](model-customize-agent-skills.md "model-customize-agent-skills.md").

## Python SDK V3

Programmatic access for serverless and SageMaker AI Training Jobs workflows using the
[SageMaker AI Python SDK](https://sagemaker.readthedocs.io/en/stable/model_customization/index.html "https://sagemaker.readthedocs.io/en/stable/model_customization/index.html").

### Serverless trainers

Use technique-specific trainer classes for fully managed customization:

```
from sagemaker.modules.train import SFTTrainer, DPOTrainer, RLVRTrainer, RLAIFTrainer

# Example: Serverless SFT
trainer = SFTTrainer(
    model_id="meta-textgeneration-llama-3-1-8b-instruct",
    train_data="s3://my-bucket/train.jsonl",
    hyperparameters={
        "max_epochs": 3,
        "learning_rate": 5e-5,
        "lora_rank": 16,
    }
)
trainer.train()
```

### SageMaker AI Training Jobs

Use `ModelTrainer` for full control over instance selection:

```
from sagemaker.modules.train import ModelTrainer
from sagemaker.modules.configs import Compute, InputData

trainer = ModelTrainer(
    training_image="my-training-image",
    role="arn:aws:iam::123456789012:role/SageMakerRole",
    compute=Compute(instance_type="ml.p4d.24xlarge", instance_count=2)
)
trainer.train(input_data_config=[
    InputData(channel_name="training", data_source="s3://my-bucket/train")
])
```

## Recipes (Training Jobs + HyperPod)

Run pre-configured training recipes on
[SageMaker AI Training Jobs](customizing-models-training-jobs.md "customizing-models-training-jobs.md") or
[HyperPod](customizing-models-hyperpod.md "customizing-models-hyperpod.md") clusters. Recipes handle
distributed training configuration, dataset loading, and checkpoint management
automatically.

Recipes are available for all supported models and techniques. See [SageMaker AI
HyperPod recipes](sagemaker-hyperpod-recipes.md "sagemaker-hyperpod-recipes.md") for the full catalog.

```
git clone --recursive https://github.com/aws/sagemaker-hyperpod-recipes.git
cd sagemaker-hyperpod-recipes
pip3 install -r requirements.txt

# Launch a fine-tuning recipe
python3 launcher/launch.py --recipe recipes_collection/recipes/fine-tuning/llama/sft_lora.yaml
```

## HP-CLI

Command-line interface for submitting training jobs to HyperPod EKS clusters.
HP-CLI integrates with Kubernetes-based workload orchestration for containerized
training on persistent clusters.

For setup and usage, see [HyperPod with Amazon
EKS](sagemaker-hyperpod-eks.md "sagemaker-hyperpod-eks.md").
