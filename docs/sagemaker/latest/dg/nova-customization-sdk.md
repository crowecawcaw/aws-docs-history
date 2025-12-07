# Nova Customization SDK

The Nova Customization SDK is a comprehensive Python SDK for customizing Amazon Nova
models. The SDK provides a unified interface for training, evaluation, monitoring,
deployment, and inference of Amazon Nova models across different platforms including SageMaker AI
and Amazon Bedrock. Whether you're adapting models to domain-specific tasks or optimizing performance
for your use case, this SDK provides everything you need in one unified interface.

## Benefits

- Unified experience

One SDK for the entire model customization lifecycle—from data preparation to
deployment and monitoring.

- Flexible training options

Support for multiple training methods including supervised fine-tuning (SFT)
and reinforcement fine-tuning (RFT), with both LoRA and full-rank
approaches.

- Enterprise-ready infrastructure

Built-in support for SageMaker AI Training Jobs and SageMaker HyperPod, with automatic
resource management.

- On-the-fly recipe creation

No more finding the right recipes or container URI for your training
techniques.

- Custom recipe support

Bring your own training recipes or use the SDK's intelligent defaults with
parameter overrides.

- Automatic validation

The SDK validates your configuration against supported model and instance
combinations, preventing errors before training starts.

- Complete observability

Integrated Amazon CloudWatch monitoring enables you to track training progress in
real-time.

## Requirements

The SDK requires at least Python 3.12.

## Installation

To install this SDK, please follow below command.

```
pip install amzn-nova-customization-sdk
```

## Supported Models and

Techniques

The SDK supports the following models and techniques within the Amazon Nova
family:

| Method                              | Supported Models |
| ----------------------------------- | ---------------- |
| Supervised Fine-tuning LoRA         | All Nova Models  |
| Supervised Fine-tuning Full-Rank    | All Nova Models  |
| Reinforcement Fine-tuning LoRA      | Nova Lite 2.0    |
| Reinforcement Fine-tuning Full-Rank | Nova Lite 2.0    |

## Getting Started

###### Topics

- [1. Prepare Your Data](#nova-customization-sdk-prepare-data "#nova-customization-sdk-prepare-data")
- [2. Configure Your
  Infrastructure](#nova-customization-sdk-configure-infrastructure "#nova-customization-sdk-configure-infrastructure")
- [3. Train](#nova-customization-sdk-train "#nova-customization-sdk-train")
- [4. Monitor](#nova-customization-sdk-monitor "#nova-customization-sdk-monitor")
- [5. Evaluate](#nova-customization-sdk-evaluate "#nova-customization-sdk-evaluate")
- [6. Deploy](#nova-customization-sdk-deploy "#nova-customization-sdk-deploy")

### 1. Prepare Your Data

Load your dataset from local files or S3, and let the SDK handle the
transformation to the correct format for your chosen training method. Or, provide
formatted data and get started immediately.

```
from amzn_nova_customization_sdk.dataset import JSONLDatasetLoader
from amzn_nova_customization_sdk.model.model_enums import Model, TrainingMethod

loader = JSONLDatasetLoader(question="input", answer="output")
loader.load("s3://your-bucket/training-data.jsonl")
loader.transform(method=TrainingMethod.SFT_LORA, model=Model.NOVA_LITE)
```

### 2. Configure Your

Infrastructure

Choose your compute resources—the SDK validates configurations and ensures optimal
setup.

```
from amzn_nova_customization_sdk.manager import SMTJRuntimeManager, SMHPRuntimeManager

# SageMaker Training Jobs
runtime = SMTJRuntimeManager(
    instance_type="ml.p5.48xlarge",
    instance_count=4
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
from amzn_nova_customization_sdk.model import NovaModelCustomizer
from amzn_nova_customization_sdk.model.model_enums import Model, TrainingMethod

customizer = NovaModelCustomizer(
    model=Model.NOVA_LITE_2,
    method=TrainingMethod.SFT_LORA,
    infra=runtime,
    data_s3_path="s3://your-bucket/prepared-data.jsonl"
)

result = customizer.train(job_name="my-training-job")
```

### 4. Monitor

Track your training progress directly from the SDK.

```
from amzn_nova_customization_sdk.monitor.log_monitor import CloudWatchLogMonitor

# Monitor training logs
customizer.get_logs()

# Or monitor directly via CloudWatchLogMonitor
monitor = CloudWatchLogMonitor.from_job_result(result)
monitor.show_logs(limit=10)

# Check job status
result.get_job_status() # InProgress, Completed, Failed
```

### 5. Evaluate

Evaluate model performance with a variety of [built-in benchmarks](nova-model-evaluation.md#nova-model-evaluation-benchmark "nova-model-evaluation.md#nova-model-evaluation-benchmark"), or design your
own evaluations.

```
from amzn_nova_customization_sdk.recipe_config.eval_config import EvaluationTask

# Evaluate on benchmark tasks
eval_result = customizer.evaluate(
    job_name="model-eval",
    eval_task=EvaluationTask.MMLU,
    model_path=result.model_artifacts.checkpoint_s3_path
)
```

### 6. Deploy

Deploy your customized model to production with built-in support for Amazon
Bedrock.

```
from amzn_nova_customization_sdk.model.model_enums import DeployPlatform

# Bedrock provisioned throughput
deployment = customizer.deploy(
    model_artifact_path=result.model_artifacts.checkpoint_s3_path,
    deploy_platform=DeployPlatform.BEDROCK_PT,
    pt_units=10
)

# Bedrock On-Demand
deployment = customizer.deploy(
    model_artifact_path=result.model_artifacts.checkpoint_s3_path,
    deploy_platform=DeployPlatform.BEDROCK_OD,
    pt_units=10
)
```

## Key Capabilities

### On The Fly Recipe

Creation

The SDK eliminates the need to search for the appropriate recipes or container URI
for specific techniques.

### Intelligent Data

Processing

The SDK automatically transforms your data into the correct format for training.
Whether you're working with JSON, JSONL, or CSV files, the data loader handles the
conversion seamlessly. Data Loader supports text as well as multimodal data (images
and videos).

### Enterprise

Infrastructure Support

The SDK works with both SageMaker Training Jobs and SageMaker HyperPod,
automatically managing:

- Instance type validation
- Recipe validation
- Job orchestration and monitoring

### Comprehensive evaluation

Evaluate your customized models against [standard benchmarks](nova-hp-evaluate.md "nova-hp-evaluate.md") including:

- MMLU (Massive Multitask Language Understanding)
- BBH (Advanced Reasoning Tasks)
- GPQA (Graduate-Level Google-Proof Q&A)

Either use the benchmark defaults, or modify them to fit your needs:

- BYOM (Bring Your Own Metric)
- BYOD (Bring Your Own Dataset)

### Production Deployment

Deploy your models to Amazon Bedrock with options for:

- **Provisioned Throughput** - Dedicated
  capacity for consistent performance
- **On-Demand** - Pay-per-use pricing

### Batch Inference

Run large-scale inference jobs efficiently:

- Process thousands of requests in parallel
- Automatic result aggregation
- Cost-effective batch processing

## Learn More

Ready to start customizing Nova models with the Nova Customization SDK? Check out our
GitHub repository for detailed guides, API references, and additional examples: [https://github.com/aws-samples/sample-nova-customization-sdk/](https://github.com/aws-samples/sample-nova-customization-sdk/ "https://github.com/aws-samples/sample-nova-customization-sdk/")
