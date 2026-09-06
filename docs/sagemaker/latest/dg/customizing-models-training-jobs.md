

# SageMaker AI Training Jobs
<a name="customizing-models-training-jobs"></a>

[Amazon SageMaker AI Training Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html) is a fully managed service that you can use to efficiently train AI/ML models at scale. With SageMaker AI Training Jobs, you can select and manage compute instances for model customization. You have full control over instance type and configuration. Jobs are ephemeral — instances are provisioned for the duration of training and released when complete. For more information about SageMaker AI Training Jobs, see [Train a Model with Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/train-model.html).

For a fully managed experience without instance selection, see [Serverless model customization](customize-model.md).

## Overview
<a name="training-jobs-overview"></a>

### Regional availability
<a name="training-jobs-regional"></a>

SageMaker AI Training Jobs is available in all SageMaker AI regions.

### Interfaces
<a name="training-jobs-interfaces"></a>

Recipes  
Run pre-configured training recipes using [SageMaker AI Recipes](https://github.com/aws/sagemaker-hyperpod-recipes). Recipes work with both SageMaker AI Training Jobs and [HyperPod](customizing-models-hyperpod.md), automating dataset loading, distributed training, and checkpoint management.

Python SDK V3 (ModelTrainer)  
Use the `ModelTrainer` class from the SageMaker AI Python SDK to submit training jobs programmatically with full control over instance selection and configuration.  

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

Studio (legacy models)  
For older models, use the model detail card → Train button in Studio. This flow allows instance selection and hyperparameter configuration.

### Supported techniques
<a name="training-jobs-supported-techniques"></a>
+ SFT, DPO, RLVR, RLAIF (via Recipes)
+ PPO (Amazon Nova models only)
+ CPT (Continued Pre-Training)

### Supported training types
<a name="training-jobs-supported-training-types"></a>
+ LoRA
+ FFT (Full Fine-Tuning)

## Getting started
<a name="training-jobs-getting-started"></a>

To get started with SageMaker AI Training Jobs using Recipes:

1. Clone the recipes repository: 

   ```
   git clone --recursive https://github.com/aws/sagemaker-hyperpod-recipes.git
   cd sagemaker-hyperpod-recipes
   pip3 install -r requirements.txt
   ```

1. Choose a recipe from `recipes_collection/recipes/fine-tuning/` for your model and technique.

1. Configure your training data path and hyperparameters in the recipe YAML file.

1. Launch the training job using the launcher script.

For detailed tutorials, see [SageMaker AI HyperPod recipes documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-recipes.html).