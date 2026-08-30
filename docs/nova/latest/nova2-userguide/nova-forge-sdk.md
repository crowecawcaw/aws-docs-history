# Customizing with SageMaker Python SDK

The SageMaker Python SDK v3 introduces a modern, modular API for training,
fine-tuning, deploying, and managing models on SageMaker. The SDK supports multiple training
methods including continued pre-training (CPT), supervised fine-tuning (SFT), direct
preference optimization (DPO), reinforcement fine-tuning (RFT), and multi-turn
reinforcement learning (MTRL). You can run training jobs on SageMaker Training Jobs and
SageMaker HyperPod.

## Quick Links

Follow these steps to go from installation to your first training job:

- [SDK Reference](https://sagemaker.readthedocs.io "https://sagemaker.readthedocs.io") on the Read the Docs website for SageMaker Python SDK
- [Quick Start Notebook on GitHub](https://github.com/aws/sagemaker-python-sdk/blob/master/v3-examples/model-customization-examples/serverless/serverless_e2e_example.ipynb "https://github.com/aws/sagemaker-python-sdk/blob/master/v3-examples/model-customization-examples/serverless/serverless_e2e_example.ipynb") – Interactive Python notebook for hands-on exploration

## Benefits

- A modular SDK for the entire model customization lifecycle from
  training to deployment and monitoring.
- Multi-platform support for SageMaker Training Jobs and SageMaker HyperPod,
  with automatic resource management and infrastructure configuration.
- No more finding the right recipes or container URI for your training
  techniques.
- Bring your own training recipes or use the defaults with parameter overrides.
- The SDK validates your configuration against supported model and instance
  combinations, preventing errors before training starts.
- Support for multiple training methods including continued pre-training (CPT),
  supervised fine-tuning (SFT), direct preference optimization (DPO),
  reinforcement fine-tuning (RFT), and multi-turn reinforcement learning (MTRL),
  with both LoRA and full-rank approaches.
- Integrated Amazon CloudWatch monitoring enables you to track training progress in
  real-time.
- Integrated MLflow to track training experiments with SageMaker AI MLflow tracking servers.

## Requirements

**Supported Python Versions**

The SageMaker Python SDK supports Python 3.10 and later.

## Installation

To install the SageMaker Python SDK, run the following command:

```
pip install "sagemaker>=3.19.0"
```

## Supported Models and Techniques

The SDK supports the following models and techniques within the Amazon Nova
family:

| Method                                         | Supported Models                                                                                                                                                                         |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Continued Pre-training                         | [All Nova Models](../nova/latest/nova2-userguide/nova-model-recipes.md#nova-model-get-recipes "../nova/latest/nova2-userguide/nova-model-recipes.md#nova-model-get-recipes") (SMHP only) |
| Supervised Fine-tuning LoRA                    | [All Nova Models](../nova/latest/nova2-userguide/nova-model-recipes.md#nova-model-get-recipes "../nova/latest/nova2-userguide/nova-model-recipes.md#nova-model-get-recipes")             |
| Supervised Fine-tuning Full-Rank               | [All Nova Models](../nova/latest/nova2-userguide/nova-model-recipes.md#nova-model-get-recipes "../nova/latest/nova2-userguide/nova-model-recipes.md#nova-model-get-recipes")             |
| Direct Preference Optimization LoRA            | Nova 1.0 models                                                                                                                                                                          |
| Direct Preference Optimization Full-Rank       | Nova 1.0 models                                                                                                                                                                          |
| Reinforcement Fine-tuning LoRA                 | Nova Lite 2.0                                                                                                                                                                            |
| Reinforcement Fine-tuning Full-Rank            | Nova Lite 2.0                                                                                                                                                                            |
| Multi-turn Reinforcement Fine-tuning LoRA      | Nova Lite 2.0                                                                                                                                                                            |
| Multi-turn Reinforcement Fine-tuning Full-Rank | Nova Lite 2.0                                                                                                                                                                            |

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

To use MTRL, use the `MultiTurnRLTrainer` class. When
training on SageMaker Training Jobs Serverless, you can optionally specify an
`output_model_package_group` to control where the output RMP is
registered. If omitted, the SDK auto-creates a Model Package Group for you.
For more information and code examples, see [Restricted Model Packages](nova-rmp.md "nova-rmp.md").

## Getting Started

###### Topics

- [1. Configure Your Infrastructure](#nova-forge-sdk-configure-infrastructure "#nova-forge-sdk-configure-infrastructure")
- [2. Train](#nova-forge-sdk-train "#nova-forge-sdk-train")
- [3. Monitor](#nova-forge-sdk-monitor "#nova-forge-sdk-monitor")
- [4. Evaluate](#nova-forge-sdk-evaluate "#nova-forge-sdk-evaluate")
- [5. Deploy](#nova-forge-sdk-deploy "#nova-forge-sdk-deploy")

### 1. Configure Your Infrastructure

The SDK supports three compute platforms. Pass the appropriate configuration
to the `compute` parameter of your trainer.

**SageMaker HyperPod**

```
from sagemaker.core.training.configs import HyperPodCompute

compute = HyperPodCompute(
    cluster_name="my-hyperpod-cluster",
    instance_type="ml.p5.48xlarge",
    node_count=4,
)
```

**SageMaker Training Jobs (Serverful)**

```
from sagemaker.core.training.configs import TrainingJobCompute

compute = TrainingJobCompute(
    instance_type="ml.p5.48xlarge",
    instance_count=2,
)
```

**SageMaker Training Jobs (Serverless)**

Fully managed and no compute configuration required. Omit the
`compute` parameter and the SDK uses serverless by default:

```
# No compute parameter needed as serverless is the default
trainer = SFTTrainer(
    model="nova-textgeneration-lite-v2",
    training_dataset="s3://my-bucket/sft-data.jsonl",
    s3_output_path="s3://my-bucket/output/",
)
```

### 2. Train

Start supervised fine-tuning with the `SFTTrainer` class. Provide
your model, compute configuration, training dataset, and output path.

```
from sagemaker.train import SFTTrainer
from sagemaker.core.training.configs import HyperPodCompute

compute = HyperPodCompute(
    cluster_name="my-hyperpod-cluster",
    instance_type="ml.p5.48xlarge",
    node_count=4,
)

trainer = SFTTrainer(
    model="nova-textgeneration-lite-v2",
    compute=compute,
    training_dataset="s3://my-bucket/sft-data.jsonl",
    s3_output_path="s3://my-bucket/output/",
)

job = trainer.train(wait=False)
```

The SDK also provides `CPTTrainer` for continued pre-training,
`DPOTrainer` for direct preference optimization,
`RLVRTrainer` for reinforcement fine-tuning, and
`MultiTurnRLTrainer` for multi-turn reinforcement learning. Each
follows the same pattern: provide a model, compute configuration, training
dataset, and output path.

### 3. Monitor

Track your training progress directly from the SDK. Use
`stream_logs()` to stream Amazon CloudWatch logs in real-time, or
`show_metrics()` to plot training metrics such as loss and
learning rate after job completion.

```
# Stream CloudWatch logs in real-time (blocks until job completes)
trainer.stream_logs(poll=5)

# Or stream only the last N lines
trainer.stream_logs(tail_lines=50)

# Plot training metrics (training_loss, lr, reward_score)
df = trainer.show_metrics()
```

### 4. Evaluate

Evaluate your trained model against built-in benchmark tasks using the
`BenchMarkEvaluator` class. Supported benchmarks include MMLU
(Massive Multitask Language Understanding), BBH (Advanced Reasoning Tasks),
and GPQA (Graduate-Level Google-Proof Q&A). For other evaluation options,
see [Evaluators](#nova-forge-sdk-evaluation "#nova-forge-sdk-evaluation").

```
from sagemaker.train.evaluate import BenchMarkEvaluator, get_benchmarks

# Get the trained model s3 path from the completed training job
s3_path = job.model_artifacts.s3_model_artifacts

Benchmark = get_benchmarks()

evaluator = BenchMarkEvaluator(
    benchmark=Benchmark.MMLU,
    model=s3_path,
    s3_output_path="s3://my-bucket/eval-output/",
)

execution = evaluator.evaluate()
```

### 5. Deploy

After training, deploy your customized model to production. With the
SageMaker Python SDK, you can deploy to SageMaker Real-time Inference
endpoints and Amazon Bedrock On-Demand. Choose the deployment option that best fits
your latency, throughput, and cost requirements.

**SageMaker Real-time Inference**

Deploy to a SageMaker Real-time Inference endpoint for full control over
instance types, scaling policies, and endpoint configuration. Use
`ModelBuilder` to create and deploy an SageMaker endpoint:

```
from sagemaker.serve import ModelBuilder

# Get the trained model checkpoint path
s3_path = job.model_artifacts.s3_model_artifacts

# Deploy to SageMaker Real-time Inference endpoint
builder = ModelBuilder(
    model=s3_path,
    instance_type="ml.p5.48xlarge",
    env_vars={
        "CONTEXT_LENGTH": "8000",
        "MAX_CONCURRENCY": "2",
    },
)

builder.build().deploy()  # Build the model and deploy to an endpoint
```

**Bedrock On-Demand**

On-Demand inference provides pay-per-use pricing without provisioned
capacity. This option is applicable to LoRA-based customizations.
Use On-Demand when you have variable or unpredictable traffic patterns:

```
from sagemaker.serve import BedrockModelBuilder

# Deploy with Bedrock On-Demand
builder = BedrockModelBuilder(
    model=s3_path,
    throughput_type="on-demand",
)

deployment = builder.deploy()
```

## Key Capabilities

### Recipe Override Precedence

The SageMaker Python SDK uses a layered configuration system for training
recipes. When you launch a training job, parameters are resolved in the
following order of precedence (highest to lowest):

1. **Parameter overrides** – Values passed
   directly via the `overrides` dictionary in the trainer
   constructor. These take the highest priority and override any
   conflicting value from the recipe YAML or Hub defaults.
2. **Recipe YAML** – A recipe YAML file
   you supply (either an S3 path or a local file). This defines the
   full training configuration but can be selectively overridden by
   the `overrides` dictionary.
3. **Hub defaults** – The default recipe
   automatically resolved from the SageMaker Model Hub based on your
   model and training method. These provide sensible starting
   configurations when no custom recipe or overrides are specified.

For example, to override the maximum training steps and learning rate
while using Hub defaults for all other parameters:

```
from sagemaker.train import SFTTrainer
from sagemaker.core.training.configs import HyperPodCompute

compute = HyperPodCompute(
    cluster_name="my-hyperpod-cluster",
    instance_type="ml.p5.48xlarge",
    node_count=2,
)

trainer = SFTTrainer(
    model="nova-textgeneration-lite-v2",
    training_dataset="s3://my-bucket/sft-data.jsonl",
    s3_output_path="s3://my-bucket/output/",
    base_job_name="my-sft-training-job",
    overrides={
        "training_config.trainer.max_epochs": 1,
        "training_config.model.optim.lr": 1e-5,
    },
)

job = trainer.train(wait=False)
```

In this example, `max_epochs` and `optim.lr` are set
explicitly via overrides. All other training parameters (batch size, warmup
steps, model-parallel and so on) fall through to the Hub default recipe
for the `nova-textgeneration-lite-v2` model.

### Enterprise Infrastructure Support

The SDK supports multiple compute platforms, automatically managing
infrastructure configuration, validation, and job orchestration:

- **SageMaker Training Jobs** – Fully managed
  training with automatic instance provisioning and teardown. Supports
  both on-demand and serverless modes.
- **SageMaker HyperPod** – Persistent clusters
  for large-scale distributed training with built-in fault tolerance
  and automatic node recovery.

Across all platforms, the SDK validates instance types, recipe configurations,
and dataset formats before submitting jobs, preventing errors early in the
workflow.

### Comprehensive evaluation

Evaluate your customized models against [standard benchmarks](nova-model-evaluation.md "nova-model-evaluation.md"). The SDK
provides the following evaluators:

- `BenchMarkEvaluator` – Run standardized performance
  benchmarks such as MMLU, BBH, and GPQA
- `LLMAsJudgeEvaluator` – Use large language models to
  assess model outputs
- `InspectAIEvaluator` – Run InspectAI or custom benchmark tasks
- `CustomScorerEvaluator` – Apply custom defined
  evaluator functions
- `MultiTurnRLEvaluator` – Evaluate multi-turn agent
  models with rollout-based metrics

### Production Deployment

With the SageMaker Python SDK, you can deploy your customized models
using multiple deployment options:

- **SageMaker Real-time Inference** – Full
  control over instance types, scaling policies, and endpoint
  configuration for custom hosting requirements.
- **Bedrock On-Demand** – Pay-per-use
  pricing without provisioned capacity. Applicable to LoRA-based
  customizations.

Use `ModelBuilder` or `BedrockModelBuilder` classes to deploy trained models.

### Data Mixing

###### Note

Data mixing is available exclusively for Nova Forge subscribers.

The SageMaker Python SDK provides the
`DataMixingConfig` class to configure data mixing.

Use `DataMixingConfig` with your trainer to
specify the percentage of customer data and the distribution across
Nova data categories:

```
from sagemaker.train import SFTTrainer
from sagemaker.train.data_mixing_config import DataMixingConfig
from sagemaker.core.training.configs import HyperPodCompute

data_mixing = DataMixingConfig(
    customer_data_percent=70.0,
    nova_data_percentages={
        "code": 40.0,
        "reasoning": 30.0,
        "instruction-following": 30.0,
    },
)

trainer = SFTTrainer(
    model="nova-textgeneration-lite-v2",
    compute=HyperPodCompute(
        cluster_name="my-cluster",
        instance_type="ml.p5.48xlarge",
        node_count=4,
    ),
    training_dataset="s3://my-bucket/sft-data.jsonl",
    s3_output_path="s3://my-bucket/output/",
    data_mixing_config=data_mixing,
)

job = trainer.train(wait=False)
```

## Learn More

Ready to start customizing Nova models with the SageMaker Python SDK? For
detailed guides, API references, and additional examples, see [sagemaker-python-sdk](https://github.com/aws/sagemaker-python-sdk "https://github.com/aws/sagemaker-python-sdk") on GitHub.
