# Nova Forge SDK

The Nova Forge SDK is a comprehensive Python SDK for customizing Amazon Nova
models. The SDK provides a unified interface for training, evaluation, monitoring,
deployment, and inference of Amazon Nova models across different platforms including SageMaker AI
and Amazon Bedrock. Whether you're adapting models to domain-specific tasks or optimizing performance
for your use case, this SDK provides everything you need in one unified interface.

## Quick Links

Follow these steps to go from installation to your first training job:

- **[SDK Reference](https://github.com/aws/nova-forge-sdk/blob/main/docs/spec.md "https://github.com/aws/nova-forge-sdk/blob/main/docs/spec.md")** - Documentation and usage specification
- **[Quick Start Notebook](https://github.com/aws/nova-forge-sdk/blob/main/samples/nova_quickstart.ipynb "https://github.com/aws/nova-forge-sdk/blob/main/samples/nova_quickstart.ipynb")** – Interactive Python notebook for hands-on exploration

## Benefits

- One SDK for the entire model customization lifecycle—from data preparation to
  deployment and monitoring.
- Support for multiple training methods including continued pre-training (CPT), supervised fine-tuning (SFT), direct preference optimization (DPO),
  and reinforcement fine-tuning (RFT), both single-turn and multi-turn, with both LoRA and full-rank
  approaches.
- Built-in support for SageMaker Training Jobs, SageMaker HyperPod, and Amazon Bedrock, with automatic
  resource management.
- No more finding the right recipes or container URI for your training
  techniques.
- Bring your own training recipes or use the SDK's intelligent defaults with
  parameter overrides.
- The SDK validates your configuration against supported model and instance
  combinations and provides validation support, preventing errors before training starts.
- Integrated Amazon CloudWatch monitoring enables you to track training progress in
  real-time.
- Integrated MLFlow to track training experiments with SageMaker AI MLFlow tracking servers.

## Requirements

**Supported Python Versions**

Nova Forge SDK is tested on:

- Python 3.12

## Installation

To install this SDK, please follow below command.

```
pip install amzn-nova-forge
```

## Supported Models and Techniques

The SDK supports the following models and techniques within the Amazon Nova
family:

| Method                                         | Supported Models                                                                                                                                                                                          |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Continued Pre-training                         | [All Nova Models](../../../sagemaker/latest/dg/nova-model-recipes.md#nova-model-recipes-reference "../../../sagemaker/latest/dg/nova-model-recipes.md#nova-model-recipes-reference") (SMHP only)          |
| Supervised Fine-tuning LoRA                    | [All Nova Models](../../../sagemaker/latest/dg/nova-model-recipes.md#nova-model-recipes-reference "../../../sagemaker/latest/dg/nova-model-recipes.md#nova-model-recipes-reference")                      |
| Supervised Fine-tuning Full-Rank               | [All Nova Models](../../../sagemaker/latest/dg/nova-model-recipes.md#nova-model-recipes-reference "../../../sagemaker/latest/dg/nova-model-recipes.md#nova-model-recipes-reference") (SMHP and SMTJ only) |
| Direct Preference Optimization LoRA            | Nova 1.0 models (SMHP and SMTJ only)                                                                                                                                                                      |
| Direct Preference Optimization Full-Rank       | Nova 1.0 models (SMHP and SMTJ only)                                                                                                                                                                      |
| Reinforcement Fine-tuning LoRA                 | Nova Lite 2.0                                                                                                                                                                                             |
| Reinforcement Fine-tuning Full-Rank            | Nova Lite 2.0 (SMHP and SMTJ only)                                                                                                                                                                        |
| Multi-turn Reinforcement Fine-tuning LoRA      | Nova Lite 2.0                                                                                                                                                                                             |
| Multi-turn Reinforcement Fine-tuning Full-Rank | Nova Lite 2.0                                                                                                                                                                                             |

### Multi-turn Reinforcement Learning Output

A Restricted Model Package (RMP) is a SageMaker AI Model Package that wraps
proprietary model artifacts in platform-managed escrow storage. RMPs allow you
to authorize and control usage of these models through IAM policies without
granting direct access to the underlying artifacts. Model data cannot be
downloaded, exported, or viewed directly. It can only be used within authorized
AWS services. RMPs exist within Model Package Groups marked with
`StorageType: "Restricted"`.

When you train a model using multi-turn reinforcement learning (MTRL) on
SageMaker Training Jobs Serverless, the output is delivered as an RMP ARN within a
Model Package Group, rather than an S3 path. This differs from other training
methods (such as SFT, DPO, or RFT) where the output is an S3 path to the
model checkpoint.

To use MTRL, specify a `model_package_group_name` in the
runtime configuration to receive the training output. Once the job
completes, you can reference the output RMP ARN to evaluate the trained
model. Using an RMP as input to a subsequent training job — for example,
to chain MTRL runs into an iterative training workflow — is planned for
Q3 2026. For more information and code examples, see [Restricted Model Packages](nova-rmp.md "nova-rmp.md").

## Getting Started

###### Topics

- [1. Prepare Your Data](#nova-forge-sdk-prepare-data "#nova-forge-sdk-prepare-data")
- [2. Configure Your Infrastructure](#nova-forge-sdk-configure-infrastructure "#nova-forge-sdk-configure-infrastructure")
- [3. Train](#nova-forge-sdk-train "#nova-forge-sdk-train")
- [4. Monitor](#nova-forge-sdk-monitor "#nova-forge-sdk-monitor")
- [5. Evaluate](#nova-forge-sdk-evaluate "#nova-forge-sdk-evaluate")
- [6. Deploy](#nova-forge-sdk-deploy "#nova-forge-sdk-deploy")

### 1. Prepare Your Data

Load your dataset from local files or S3, and let the SDK handle the
transformation to the correct format for your chosen training method. Or, provide
formatted data and get started immediately.

```
from amzn_nova_forge.dataset.dataset_loader import JSONLDatasetLoader
from amzn_nova_forge.model.model_enums import Model, TrainingMethod, TransformMethod

loader = JSONLDatasetLoader()
loader.load("s3://your-bucket/training-data.jsonl")
loader.transform(
    method=TransformMethod.SCHEMA,
    training_method=TrainingMethod.SFT_LORA,
    model=Model.NOVA_LITE_2,
    column_mappings={"question": "input", "answer": "output"},
)
```

### 2. Configure Your Infrastructure

Choose your compute resources—the SDK validates configurations and ensures optimal
setup.

```
from amzn_nova_forge.manager.runtime_manager import BedrockRuntimeManager, SMTJRuntimeManager, SMTJServerlessRuntimeManager, SMHPRuntimeManager

# Bedrock
runtime = BedrockRuntimeManager(
    execution_role="arn:aws:iam::123456789012:role/ExampleRole"
)

# SageMaker Training Jobs
runtime = SMTJRuntimeManager(
    instance_type="ml.p5.48xlarge",
    instance_count=4
)

# SageMaker Training Jobs Serverless
runtime = SMTJServerlessRuntimeManager(
    model_package_group_name = "my-package"
)

# SageMaker HyperPod
runtime = SMHPRuntimeManager(
    instance_type="ml.p5.48xlarge",
    instance_count=4,
    cluster_name="my-hyperpod-cluster",
    namespace="kubeflow"
)
```

### 3. Train

Start training with just a few lines of code.

```
from amzn_nova_forge.trainer.forge_trainer import ForgeTrainer
from amzn_nova_forge.model.model_enums import Model, TrainingMethod
from amzn_nova_forge.core import ForgeConfig

trainer = ForgeTrainer(
    model=Model.NOVA_LITE_2,
    method=TrainingMethod.SFT_LORA,
    infra=runtime,
    training_data_s3_path="s3://your-bucket/sft/prepared-data.jsonl",  # Training data path
    config=ForgeConfig(
        output_s3_path="s3://your-bucket/output",
    ),
)

result = trainer.train(job_name="my-training-job")
```

### 4. Monitor

Track your training progress directly from the SDK.

```
from amzn_nova_forge.monitor.log_monitor import CloudWatchLogMonitor

# Monitor training logs
trainer.get_logs()

# Or monitor directly via CloudWatchLogMonitor
monitor = CloudWatchLogMonitor.from_job_result(result)
monitor.show_logs(limit=10)

# Check job status
result.get_job_status() # InProgress, Completed, Failed
```

### 5. Evaluate

Evaluate model performance with a variety of [built-in benchmarks](../../../sagemaker/latest/dg/nova-model-evaluation.md#nova-model-evaluation-benchmark "../../../sagemaker/latest/dg/nova-model-evaluation.md#nova-model-evaluation-benchmark"), or design your
own evaluations.

```
from amzn_nova_forge.evaluator import ForgeEvaluator
from amzn_nova_forge.recipe_config.eval_config import EvaluationTask

evaluator = ForgeEvaluator(
    model=Model.NOVA_LITE_2,
    infra=runtime,
    config=ForgeConfig(
        output_s3_path="s3://your-bucket/output",
    ),
    data_s3_path="s3://your-bucket/eval-data/data.jsonl"
)

# Evaluate on benchmark tasks
eval_result = evaluator.evaluate(
    job_name="model-eval",
    eval_task=EvaluationTask.MMLU,
    model_path=result.model_artifacts.checkpoint_s3_path
)
```

### 6. Deploy

Deploy your customized model to production with built-in support for Amazon
Bedrock or SageMaker.

```
from amzn_nova_forge.deployer import ForgeDeployer
from amzn_nova_forge.model.model_enums import DeployPlatform, Model

deployer = ForgeDeployer(
    region="us-east-1",
    model=Model.NOVA_LITE_2,
)

# Bedrock provisioned throughput
deployment = deployer.deploy(
    model_artifact_path=result.model_artifacts.checkpoint_s3_path,
    deploy_platform=DeployPlatform.BEDROCK_PT,
    unit_count=10
)

# Bedrock On-Demand
deployment = deployer.deploy(
    model_artifact_path=result.model_artifacts.checkpoint_s3_path,
    deploy_platform=DeployPlatform.BEDROCK_OD
)

# Sagemaker Real-time Inference
deployment = deployer.deploy(
    model_artifact_path=result.model_artifacts.checkpoint_s3_path,
    deploy_platform=DeployPlatform.SAGEMAKER,
    unit_count=10,
    sagemaker_instance_type="ml.p5.48xlarge",
    sagemaker_environment_variables={
        "CONTEXT_LENGTH": "12000",
        "MAX_CONCURRENCY": "16",
    }
)
```

## Key Capabilities

### On The Fly Recipe Creation

The SDK eliminates the need to search for the appropriate recipes or container URI
for specific techniques.

### Intelligent Data Processing

The SDK automatically transforms your data into the correct format for training.
Whether you're working with JSON, JSONL, or CSV files, the data loader handles the
conversion seamlessly. Data Loader supports text as well as multimodal data (images
and videos).

### Enterprise Infrastructure Support

The SDK works with both SageMaker Training Jobs and SageMaker HyperPod,
automatically managing:

- Instance type validation
- Recipe validation
- Dataset validation
- Job orchestration and monitoring

The SDK also supports SageMaker Training Jobs serverless and Bedrock customization.

### Comprehensive evaluation

Evaluate your customized models against [standard benchmarks](../../../sagemaker/latest/dg/nova-hp-evaluate.md "../../../sagemaker/latest/dg/nova-hp-evaluate.md") including:

- MMLU (Massive Multitask Language Understanding)
- BBH (Advanced Reasoning Tasks)
- GPQA (Graduate-Level Google-Proof Q&A)

Either use the benchmark defaults, or modify them to fit your needs:

- BYOM (Bring Your Own Metric)
- BYOD (Bring Your Own Dataset)

### Production Deployment

Deploy your models to Amazon Bedrock or SageMaker AI with options for:

- **Bedrock Provisioned Throughput** - Dedicated
  capacity for consistent performance
- **Bedrock On-Demand (only applicable to LoRA based customization)** - Pay-per-use pricing
- **SageMaker AI Real-time Inference** - Dedicated capacity for consistent performance

### Batch Inference

Run large-scale inference jobs efficiently:

- Process thousands of requests in parallel
- Automatic result aggregation
- Cost-effective batch processing

### Nova Forge

For Nova Forge subscribers, the SDK supports data mixing recipes.

## Learn More

Ready to start customizing Nova models with the Nova Forge SDK? Check out our
GitHub repository for detailed guides, API references, and additional examples: [https://github.com/aws/nova-forge-sdk](https://github.com/aws/nova-forge-sdk "https://github.com/aws/nova-forge-sdk")
