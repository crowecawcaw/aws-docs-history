

# Supervised fine-tuning (SFT) on Nova 2.0 on SageMaker Training Jobs
<a name="nova-sft-2-smtj"></a>

## Prerequisites
<a name="nova-model-training-jobs-prerequisites2"></a>

Before you start a training job, note the following.
+ Amazon S3 buckets to store your input data and output of training jobs. You can either use one bucket for both or separate buckets for each type of the data. Make sure your buckets are in the same AWS Region where you create all the other resources for training. For more information, see [Creating a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html).
+ An IAM role with permissions to run a training job. Make sure you attach an IAM policy with `AmazonSageMakerFullAccess`. For more information, see [How to use SageMaker AI execution roles](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html).
+ Base Amazon Nova recipes, see [Getting Amazon Nova recipes](nova-model-recipes.md#nova-model-get-recipes).

## What is SFT?
<a name="nova-2-what-is-sft"></a>

Supervised fine-tuning (SFT) trains a language model using labeled input-output pairs. The model learns from demonstration examples consisting of prompts and responses, refining its capabilities to align with specific tasks, instructions, or desired behaviors.

To determine whether SFT is a good fit for your use case, see [Supervised fine-tuning (SFT)](nova-fine-tune.md).

## Starting a training job
<a name="nova-2-starting-training"></a>

### Preparing your data
<a name="nova-2-data-preparation"></a>

For information about the data format, supported features, constraints, and best practices for preparing SFT training data, see [Preparing data for SFT on Amazon Nova 2](nova-data-prep-sft-2.md).

### Uploading your data
<a name="nova-2-uploading-data"></a>

Datasets should be uploaded to a bucket that can be accessed by SageMaker training jobs. For information about setting the right permissions, see [Prerequisites](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-model-general-prerequisites.html).

### Selecting hyperparameters and updating the recipe
<a name="nova-2-selecting-hyperparameters"></a>

The setup for Nova 2.0 is largely the same as for Nova 1.0. Once the input data has been uploaded to S3, use the recipe from [SageMaker HyperPod Recipes](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/fine-tuning/nova) on GitHub under the Fine tuning folder. For Nova 2.0 Lite, the following are some of the key hyperparameters that you can update based on the use case. The following is an example of the Nova 2.0 Lite SFT PEFT recipe. For the container image URI, use `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-TJ-SFT-V2-latest` to run an SFT fine-tuning job.

**Sample Input **

```
run:  
  name: {peft_recipe_job_name}  
  model_type: amazon.nova-2-lite-v1:0:256k  
  model_name_or_path: {peft_model_name_or_path}  
  data_s3_path: {train_dataset_s3_path} # SageMaker HyperPod (SMHP) only and not compatible with SageMaker Training jobs. Note replace my-bucket-name with your real bucket name for SMHP job  
  replicas: 4                      # Number of compute instances for training, allowed values are 4, 8, 16, 32  
  output_s3_path: ""               # Output artifact path (Hyperpod job-specific; not compatible with standard SageMaker Training jobs). Note replace my-bucket-name with your real bucket name for SMHP job  
  
training_config:  
  max_steps: 10                   # Maximum training steps. Minimal is 4.  
  save_steps: 10                      # How many training steps the checkpoint will be saved. Should be less than or equal to max_steps  
  save_top_k: 1                    # Keep top K best checkpoints. Note supported only for SageMaker HyperPod jobs. Minimal is 1.  
  max_length: 32768                # Sequence length (options: 8192, 16384, 32768 [default], 65536)  
  global_batch_size: 32            # Global batch size (options: 32, 64, 128)  
  reasoning_enabled: true          # If data has reasoningContent, set to true; otherwise False  
  
  lr_scheduler:  
    warmup_steps: 15               # Learning rate warmup steps. Recommend 15% of max_steps  
    min_lr: 1e-6                   # Minimum learning rate, must be between 0.0 and 1.0  
  
  optim_config:                    # Optimizer settings  
    lr: 1e-5                       # Learning rate, must be between 0.0 and 1.0  
    weight_decay: 0.0              # L2 regularization strength, must be between 0.0 and 1.0  
    adam_beta1: 0.9                # Exponential decay rate for first-moment estimates, must be between 0.0 and 1.0  
    adam_beta2: 0.95               # Exponential decay rate for second-moment estimates, must be between 0.0 and 1.0  
  
  peft:                            # Parameter-efficient fine-tuning (LoRA)  
    peft_scheme: "lora"            # Enable LoRA for PEFT  
    lora_tuning:  
      alpha: 64                    # Scaling factor for LoRA weights ( options: 32, 64, 96, 128, 160, 192),  
      lora_plus_lr_ratio: 64.0
```

The recipe also contains largely the same hyperparameters as Nova 1.0. The notable hyperparameters are:
+ `max_steps` – The number of steps you want to run the job for. Generally, for one epoch (one run through your entire dataset), the number of steps = number of data samples / global batch size. The larger the number of steps and the smaller your global batch size, the longer the job will take to run.
+ `reasoning_enabled` – Controls reasoning mode for your dataset. Options:
  + `true`: Enables reasoning mode (equivalent to high reasoning)
  + `false`: Disables reasoning mode

  Note: For SFT, there is no granular control over reasoning effort levels. Setting `reasoning_enabled: true` enables full reasoning capability.
+ `peft.peft_scheme` – Setting this to "lora" enables PEFT-based fine tuning. Setting it to null (no quotes) enables Full-Rank fine tuning.

### Start the training job
<a name="nova-2-start-job"></a>

```
from sagemaker.pytorch import PyTorch  
  
# define OutputDataConfig path  
if default_prefix:  
    output_path = f"s3://{bucket_name}/{default_prefix}/{sm_training_job_name}"  
else:  
    output_path = f"s3://{bucket_name}/{sm_training_job_name}"  

output_kms_key = "<KMS key arn to encrypt trained model in Amazon-owned S3 bucket>" # optional, leave blank for Amazon managed encryption
  
recipe_overrides = {  
    "run": {  
        "replicas": instance_count,  # Required  
        "output_s3_path": output_path  
    },  
}  
  
estimator = PyTorch(  
    output_path=output_path,  
    base_job_name=sm_training_job_name,  
    role=role,  
    disable_profiler=True,  
    debugger_hook_config=False,  
    instance_count=instance_count,  
    instance_type=instance_type,  
    training_recipe=training_recipe,  
    recipe_overrides=recipe_overrides,  
    max_run=432000,  
    sagemaker_session=sagemaker_session,  
    image_uri=image_uri,
    output_kms_key=output_kms_key,
    tags=[  
        {'Key': 'model_name_or_path', 'Value': model_name_or_path},  
    ]  
)  
  
print(f"\nsm_training_job_name:\n{sm_training_job_name}\n")  
print(f"output_path:\n{output_path}")
```

```
from sagemaker.inputs import TrainingInput  
  
train_input = TrainingInput(  
    s3_data=train_dataset_s3_path,  
    distribution="FullyReplicated",  
    s3_data_type="Converse",  
)  
  
estimator.fit(inputs={"validation": val_input}, wait=False)
```

**Note**  
Passing a validation dataset is not supported for supervised fine tuning of Nova 2.0 Lite.

To kick off the job:
+ Update the recipe with your dataset paths and hyperparameters
+ Execute the specified cells in the notebook to submit the training job

The notebook handles job submission and provides status tracking.