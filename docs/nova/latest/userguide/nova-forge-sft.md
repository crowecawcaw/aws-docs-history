# Supervised Fine-Tuning

## Introduction

Supervised fine-tuning uses dataset with input-output pairs for the task of interest. In other words, you provide examples of prompts (questions, instructions, etc.) along with the correct or desired responses and continue training the model on these. The model's weights are adjusted to minimize a supervised loss, typically cross-entropy between its predictions and the target response tokens.

## When to use SFT?

SFT is best when you have a well-defined task with clear desired outputs. If you can explicitly say "Given X input, the correct/desired output is Y" and you can gather examples of such X-Y mappings, then supervised fine-tuning is a great choice. Some scenarios where SFT excels include:

- **Structured or complex classification tasks**: e.g. classifying internal documents or contracts into many custom categories. With SFT, the model can learn these specific categories far better than prompting alone.
- **Question-answering or transformation tasks with known answers**: e.g. fine-tuning a model to answer questions from a company's knowledge base, or to convert data between formats, where each input has a correct response.
- **Formatting and style consistency**: If you need the model to always respond in a certain format or tone, you can fine-tune on examples of the correct format/tone. For instance, training on prompt-response pairs that demonstrate a particular brand voice or style can teach the model with that style in its outputs. Instruction-following behavior is often initially taught via SFT on curated examples of good assistant behavior.

SFT is the most direct way to teach an LLM a new skill or behavior when you can specify what the right behavior looks like. It leverages the model's existing language understanding and focuses it on your task. Do not use SFT when the gap is knowledge rather than behavior; it will not make the model learn new facts, jargon, or recent events. In those cases, prefer continued pre-training on large in-domain corpora or retrieval-augmented generation to bring external knowledge at inference. When you can measure quality but cannot label a single right answer, reinforcement fine-tuning with verifiable rewards or an LLM-as-judge might be preferable to SFT.

Depending on task complexity and performance of the Nova model without tuning, plan for thousands to tens of thousands of demonstrations per task, with data quality, consistency, and diversity mattering more than raw volume.

## When to use parameter efficient and when full rank SFT?

Nova customization recipes enable you to perform parameter efficient, in particular LoRA, or full rank SFT. If you want a straightforward, cost-efficient model update, or have very little data, favor parameter-efficient methods so you train small adapters while leaving most of the backbone untouched (full rank SFT updates all model parameters).

## Data Mixing for SFT

Data mixing allows you to combine your custom training datasets with Nova's proprietary training data. This feature is available for both Nova 1.0 and Nova 2.0 models.

**Nova Proprietary Data Type**: Nova supports both text and multimodal SFT data types. It is organized into multiple data categories each containing a blend of tasks relevant for the corresponding category.

**Nova Proprietary Data Categories**: Text datasets includes several categories including: autonomous decision making, task completion, goal oriented datasets (agents), both reasoning and non-reasoning precise task execution datasets (reasoning-instruction-following, instruction-following), sequences demonstrating strategic thinking and step-by-step task breakdown (planning), responsible AI (rai), long-context, factuality, math, stem and many more. Similarly, multimodal datasets includes video, screenshot, charts and many more.

The data mixing feature allows you to blend your own fine-tuning training samples with samples from the Nova datasets used to fine-tune the Nova. This can prevent overfitting on your custom training and "catastrophic forgetting" of Nova capabilities, or help you build capabilities when training from a new pretrained checkpoint.

To mix in Nova data, you simply need to add a data_mixing block to your recipe YAML file, under the training_config section. Text and multi-modal data mixing blocks have different content, and data mixing blocks are somewhat different for Nova 1.0 and Nova 2.0. Please refer to corresponding recipes.

### Supported Models

- Nova 1.0 (Micro, Lite, Pro)
- Nova 2.0 Lite

### Supported Modality

- Text
- Multimodal

## YAML Configuration Examples

### Example Data Mixing Block for Nova 1.0 Text Mixing

```

## Run config
run:
  name: "my-lora-run"             # A descriptive name for your training job
  model_type: "amazon.nova-lite-v1:0:300k"  # Model variant specification, do not change
  model_name_or_path: "nova-lite/prod"      # Base model path, do not change
  replicas: 4                     # Number of compute instances for training, allowed values are 4, 8, 16
  data_s3_path: ""                # Customer data path
  output_s3_path: ""              # Output artifact path, Sagemaker Hyperpod job-specific configuration - not compatible with standard Sagemaker Training jobs

  ## MLFlow configs
  mlflow_tracking_uri: "" # Required for MLFlow
  mlflow_experiment_name: "my-lora-experiment" # Optional for MLFlow. Note: leave this field non-empty
  mlflow_run_name: "my-lora-run" # Optional for MLFlow. Note: leave this field non-empty

## Training specific configs
training_config:
  max_length: 32768               # Maximum context window size (tokens).
  global_batch_size: 64           # Global batch size, allowed values are 16, 32, 64

  trainer:
    max_epochs: 2                # Number of training epochs

  model:
    hidden_dropout: 0.0          # Dropout for hidden states, must be between 0.0 and 1.0
    attention_dropout: 0.0       # Dropout for attention weights, must be between 0.0 and 1.0
    ffn_dropout: 0.0             # Dropout for feed-forward networks, must be between 0.0 and 1.0

    optim:
      lr: 1e-5                 # Learning rate
      name: distributed_fused_adam  # Optimizer algorithm, do not change
      adam_w_mode: true        # Enable AdamW mode
      eps: 1e-06               # Epsilon for numerical stability
      weight_decay: 0.0        # L2 regularization strength, must be between 0.0 and 1.0
      betas:                   # Adam optimizer betas, must be between 0.0 and 1.0
        - 0.9
        - 0.999
      sched:
        warmup_steps: 10     # Learning rate warmup steps
        constant_steps: 0    # Steps at constant learning rate
        min_lr: 1e-6         # Minimum learning rate

    peft:
      peft_scheme: "lora"      # Enable LoRA for parameter-efficient fine-tuning
      lora_tuning:
        loraplus_lr_ratio: 8.0  # LoRA+ learning rate scaling factor, must be between 0.0 and 100.0
        alpha: 32            # Scaling factor for LoRA weights. Allowed values are 32, 64, 96, 128, 160 and 192
        adapter_dropout: 0.01  # Regularization for LoRA parameters. Must be between 0.0 and 1.0

data_mixing:
  dataset_catalog: sft_text       # Nova text dataset catalog
  sources:
    customer_data:
      percent: 50                 # Percent of overall mix to draw from customer data
    nova_data:                    # The remainder will be drawn from Nova data. The categories below must add to 100
      agents: 1                   # autonomous decision-making, task completion, goal-oriented behavior in AI systems
      chat: 51                    # Conversational exchanges demonstrating natural dialogue flow
      code: 8                     # Programming examples and solutions spanning multiple languages
      rai: 1                      # ethical AI principles, safety considerations, and responsible technology deployment
      instruction-following: 13   # precise task execution based on varying levels of user prompts and directives
      stem: 6                     # science, technology, engineering, and mathematics content
      planning: 2                 # sequences demonstrating strategic thinking and step-by-step task breakdown
      reasoning: 8                # logical problem-solving and analytical thinking demonstrations
      rag: 1                      # retrieval-augmented generation examples
      translation: 9              # language translation tasks

```

### Nova 2.0 Configuration Example

```

run:
  name: my-lora-sft-run
  model_type: amazon.nova-2-lite-v1:0:256k
  model_name_or_path: nova-lite-2/prod
  data_s3_path: s3://my-bucket-name/train.jsonl
  replicas: 4
  output_s3_path: s3://my-bucket-name/outputs/
  mlflow_tracking_uri: ""
  mlflow_experiment_name: "my-lora-sft-experiment"
  mlflow_run_name: "my-lora-sft-run"

training_config:
  max_steps: 100
  save_steps: 10
  save_top_k: 5
  max_length: 32768
  global_batch_size: 32
  reasoning_enabled: true
  lr_scheduler:
    warmup_steps: 15
    min_lr: 1e-6
  optim_config:
    lr: 1e-5
    weight_decay: 0.0
    adam_beta1: 0.9
    adam_beta2: 0.95
  peft:
    peft_scheme: "lora"
    lora_tuning:
      alpha: 64
      lora_plus_lr_ratio: 64.0

```

### Nova 2.0 Text Data Mixing

```

data_mixing:
  dataset_catalog: sft_1p5_text_chat
  sources:
    customer_data:
      percent: 50
    nova_data:
      agents: 1
      baseline: 10
      chat: 0.5
      code: 10
      factuality: 0.1
      identity: 1
      long-context: 1
      math: 2
      rai: 1
      instruction-following: 13
      stem: 0.5
      planning: 10
      reasoning-chat: 0.5
      reasoning-code: 0.5
      reasoning-factuality: 0.5
      reasoning-instruction-following: 45
      reasoning-math: 0.5
      reasoning-planning: 0.5
      reasoning-rag: 0.4
      reasoning-rai: 0.5
      reasoning-stem: 0.4
      rag: 1
      translation: 0.1

```

### Nova 1.0 Multimodal Data Mixing

```

data_mixing:
  dataset_catalog: sft_mm
  sources:
    customer_data:
      percent: 50
    nova_data:
      agents: 11
      docs: 17
      perception: 10
      rag: 4
      rai: 3
      reasoning: 10
      stem: 17
      text: 10
      video: 18

```

### Nova 2.0 Multimodal Data Mixing

```

data_mixing:
  dataset_catalog: sft_1p5_mm_chat
  sources:
    customer_data:
      percent: 50
    nova_data:
      charts: 1
      chat: 38
      code: 20
      docs: 3
      general: 2
      grounding: 1
      rag: 4
      screenshot: 4
      text: 8
      translation: 4
      video: 15

```

## Model Checkpoints

### Nova 1.0 Checkpoints

- **PRE-TRAINED** [`nova-<micro/lite/pro>/pretraining-text-partial`]: Checkpoint after constant learning rate stage of Nova pre-training where the model is trained on trillions of text tokens. [Outcome of Stage 1]
- **MID-TRAINED** [`nova-<micro/lite/pro>/pretraining-text-full`]: Text-only checkpoint after all stages of Nova pretraining and mid-training with trillions of text tokens. Use if you don't want the model to have seen any multi-modal data. [Outcome of Stage 3]
- **MID-TRAINED** [`nova-<lite/pro>/pretraining-mm-full`]: Checkpoint after all stages of Nova pretraining and mid-training, including multi-modal data, with trillions of tokens. [Outcome of Stage 3 with multimodal data]
- **FINAL** [`nova-<micro/lite/pro>/prod`]: Fully aligned final checkpoint that has gone through all pretraining and post training steps. [Outcome of Stage 4]

### Nova 2.0 Checkpoints

- **PRE-TRAINED** [`nova-lite-2/pretraining-text-RD`]: Checkpoint after constant learning rate and ramp-down stages where model is trained on trillions of tokens. [Outcome of Stage 2]
- **MID-TRAINED** [`nova-lite-2/pretraining-text-CE`]: Allows customers with intermediate volumes of unstructured data to introduce their data with a more conservative learning rate than pre-training, absorbing domain-specific knowledge while avoiding catastrophic forgetting. [Outcome of Stage 3]
- **FINAL** [`nova-lite-2/prod`]: Fully aligned final checkpoint that has gone through all pretraining and post training steps. [Outcome of Stage 4]

**Training Stages:**

- Stage 1: PT Ckpt, initial pre-training with constant learning rate
- Stage 2: PT Ckpt, learning rate ramp-down
- Stage 3: PT Ckpt, context extension training
- Stage 4: instruction-following alignment and safety training

## Training Approaches

| Training Approach Selection Guide                                                                            | Data Type    | Data Volume                  | Perform                             | With Checkpoint |
| ------------------------------------------------------------------------------------------------------------ | ------------ | ---------------------------- | ----------------------------------- | --------------- |
| Large-scale unstructured raw domain data (documents, logs, articles, code, etc.)                             | 1T+ Tokens   | Continued Pre-Training       | End of Constant Learning Rate (CLR) |
| Large-scale unstructured raw domain data                                                                     | 100B+ Tokens | Mid-Training                 | End of CLR                          |
| Smaller volumes of unstructured raw data; Structured reasoning traces / CoT data                             | 1B+ Tokens   | Mid-Training                 | Nova base model                     |
| Structured demonstrations (high-quality input-output pairs, curated task instructions, multi-turn dialogues) | 1K+ Examples | Supervised Fine-Tuning (SFT) | Nova base model                     |

## Pre-Requisites before you begin

- We assume that you've already setup an SMHP cluster with a restricted instance group (RIG) that has active capacity. If not please refer here to get your SMHP Cluster and RIG setup completed [[Docs Link](../../../sagemaker/latest/dg/nova-forge.md "../../../sagemaker/latest/dg/nova-forge.md"), [Workshop Link](https://catalog.us-east-1.prod.workshops.aws/workshops/dcac6f7a-3c61-4978-8344-7535526bf743/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/dcac6f7a-3c61-4978-8344-7535526bf743/en-US")]
- You will require **p5.48xlarge** EC2 instances to execute this recipe. The minimum number instances required to execute this recipe efficiently are as follows:
  - **Nova Lite 2.0 - 4 p5.48xlarge**
  - **Nova Lite 1.0 – 4 p5.48xlarge**
  - **Nova Micro 1.0 – 4 p5.48xlarge**
  - **Nova Pro 1.0 – 6 p5.48xlarge**

- Install the Forge Specific Sagemaker Hyperpod CLI using the provided instructions [here](https://catalog.us-east-1.prod.workshops.aws/workshops/dcac6f7a-3c61-4978-8344-7535526bf743/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/dcac6f7a-3c61-4978-8344-7535526bf743/en-US")
- Confirm that you can connect to your cluster using `hyperpod get-clusters`
  - Note that this command will list all SMHP clusters in your account

- Confirm that your training, and optionally validation data, is available in an S3 bucket that is accessible by the execution role of your SMHP cluster. For data preparation, refer to next section.
- Have setup completed. If you have not completed the setup, please follow below [guide](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md").
- **Verification**: After completing the setup, confirm you can successfully run below commands

```

aws sagemaker describe-cluster --cluster-name <cluster-name> --region <region>

hyperpod connect-cluster --cluster-name cluster-name

```

## A systematic Approach to Achieving Successful SFT

- **Data Preparation**: Follow established guidelines to create, clean, or reformat datasets into the required structure. Ensure that inputs, outputs, and auxiliary information (such as reasoning traces or metadata) are properly aligned and formatted.
- **Training Configuration**: Define how the model will be trained. When using Amazon SageMaker HyperPod, this configuration is written in a YAML recipe file that includes:
  - Data source paths (training and validation datasets)
  - Key hyperparameters (number of training steps, learning rate, batch size)
  - Optional components (distributed training parameters, etc)
  - Data Mixing setting (defines proportions of customer and Nova data categories)

- **Optimize SFT Hyper Parameters**: SFT recipe parameter values we recommend are are a great starting point and a robust choice. If you want to optimize them further for your use case do multiple SFT runs with different parameter combinations and pick the best one. You can select parameter combinations following Hyper-Parameter Optimization method of your choice. A simple approach is to vary the value of one parameter (default\*0.5, default, default\*2) while keeping other default value for other parameters, repeat this for each parameter you want to optimize, and iterate if needed. The most relevant parameters for LoRA are learning rate, alpha (scaling parameter), number of epochs to train and warmup steps; for full-rank it is mainly the learning rate, number of epochs, and warmup steps.

## Experiment Sequencing and Data Mixing

- If you have only SFT data (train/dev/test) for a set of tasks and care only about the test performance on these tasks
  - Do SFT without mixing on [FINAL] Nova checkpoint. Use the default SFT hyper-parameters and optionally optimize them for your use case. Monitor validation metrics and/or evaluate intermediate checkpoints for larger datasets.

- If you have only SFT data (train/dev/test) for a set of tasks and care about test performance on these tasks and general benchmarks in the domain of interest
  - Start by doing SFT with Nova data mixing on a pre-training checkpoint (PRE-TRAINED or MID-TRAINED checkpoint, not FINAL). Using an intermediate checkpoint allows the model to better integrate your custom data with Nova's proprietary data while maintaining strong general capabilities.
  - Run shorter SFT training runs with varying amount of Nova data in the mix (e.g., 10%, 25%, 50%, 75%) and Nova data category selections that complement your use case (e.g., pick instruction following category if you care about general instruction following ability). Monitor validation metrics and evaluate if mixing helps performance on general benchmarks. Select the training mix and checkpoint that leads to the best combination of performance on your task and general performance. Depending on the use case, both task and general performances can be further improved using reinforcement fine tuning (RFT).

## Prepare Dataset for SFT

**Nova 1.0**: Data prep is described at [https://docs.aws.amazon.com/sagemaker/latest/dg/nova-fine-tune.html](../../../sagemaker/latest/dg/nova-fine-tune.md "../../../sagemaker/latest/dg/nova-fine-tune.md")

**Nova 2.0**: Use Converse API format as for Nova 1.0 [https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-call.html](../../../bedrock/latest/userguide/conversation-inference-call.md "../../../bedrock/latest/userguide/conversation-inference-call.md"). Nova 2.0 data format can contain additional reasoning fields: [https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ReasoningContentBlock.html](../../../bedrock/latest/APIReference/API_runtime_ReasoningContentBlock.md "../../../bedrock/latest/APIReference/API_runtime_ReasoningContentBlock.md")

Reasoning content captures the model's intermediate thinking steps before generating a final answer. In the `assistant` turn, use the `reasoningContent` field to include reasoning traces. Use plain text for reasoning content, avoid markup tags like `<thinking>` and `</thinking>` unless specifically required by your task, and ensure reasoning content is clear and relevant to the problem-solving process.

## Responsible AI Toolkit and Content Moderation

**Content moderation settings**: Nova Forge customers have access to Customizable Content Moderation Settings (CCMS) for Nova Lite 1.0 and Pro 1.0 models. CCMS allows you to adjust content moderation controls to align with your specific business requirements while maintaining essential responsible AI safeguards. To determine if your business use case qualifies for CCMS, contact your Amazon Web Services account manager.

Nova Forge provides a Responsible AI toolkit that includes training data, evaluation benchmarks, and runtime controls to help you align your models with Nova's responsible AI guidelines.

**Training data**: The "RAI" category in data mixing contains cases and scenarios emphasizing responsible AI principles, safety considerations, and responsible technology deployment. Use these to align your models responsibly during continued pre-training.

**Evaluations**: Benchmark tasks are available to test your model's ability to detect and reject inappropriate, harmful, or incorrect content. Use these evaluations to measure the difference between base model performance and your custom model performance.

**Runtime controls**: By default, Nova's runtime controls moderate model responses during inference. To modify these controls for your specific business case, request Customizable Content Moderation Settings (CCMS) by contacting your Amazon Web Services account manager.

### Shared Responsibility for Safety

Safety is a shared responsibility between Amazon Web Services and our customers. Changing the base model or using continued pre-training to improve performance on a specific use case can impact safety, fairness, and other properties of the new model.

We use a robust adaptation method to minimize changes to the safety, fairness, and other protections built into our base models while minimizing impact on model performance for tasks the model was not customized for.

You are responsible for:

- End-to-end testing of their applications on datasets representative of their use cases
- Deciding if test results meet their specific expectations of safety, fairness, and other properties, as well as overall effectiveness

For more information, see the Amazon Web Services Responsible Use of AI Guide, Amazon Web Services Responsible AI Policy, AWS Acceptable Use Policy, and AWS Service Terms for the services you plan to use.

### Customizable Content Moderation Settings (CCMS)

CCMS allows you to adjust controls relevant to your business requirements while maintaining essential, non-configurable controls that ensure responsible use of AI.

These settings allow content generation through three available configurations:

- Security only
- Safety, sensitive content, and fairness combined
- All categories combined

The four content moderation categories are:

1. **Safety** – Covers dangerous activities, weapons, and controlled substances
2. **Sensitive content** – Includes profanity, nudity, and bullying
3. **Fairness** – Addresses bias and cultural considerations
4. **Security** – Involves cybercrime, malware, and malicious content

Regardless of your CCMS configuration, Amazon Nova enforces essential, non-configurable controls to ensure responsible use of AI, such as controls to prevent harm to children and preserve privacy.

#### Recommendations for Using CCMS

When using CCMS, we recommend using Continuous Pre Training (CPT) and starting from a pre-RAI alignment checkpoint (PRE-TRAINING-Early, PRE-TRAINING-Mid, or PRE-TRAINING-Final) rather than the GA/FINAL checkpoint. These checkpoints have not undergone safety training or been steered toward specific RAI behaviors, allowing you to customize them more efficiently to your content moderation requirements.

**Tip**: When using CCMS with data mixing, consider adjusting the "rai" category percentage in your nova_data configuration to align with your specific content moderation requirements.

#### Availability

CCMS is currently available for approved customers using:

- Nova Lite 1.0 and Pro 1.0 models
- Amazon Bedrock On-Demand inference
- The us-east-1 (N. Virginia) region

To enable CCMS for your Forge models, contact your Amazon Web Services account manager.

## Evaluation Methods

### Prerequisites

- Checkpoint S3 URI from your training job's `manifest.json` file (for trained models)
- Evaluation dataset uploaded to S3 in the correct format
- Output S3 path for evaluation results

**Out of the box benchmarks**: Use out of the box benchmarks to validate the performance on general tasks. For more details check here: [https://docs.aws.amazon.com/sagemaker/latest/dg/nova-hp-evaluate.html](../../../sagemaker/latest/dg/nova-hp-evaluate.md "../../../sagemaker/latest/dg/nova-hp-evaluate.md")

### Bring Your Own Data

You can also supply your custom data by formatting them in below format and then using below mentioned containers to get inference results along with log probabilities for calibrations if needed.

Create jsonl per task with the following structure:

```

{
  "metadata": "{key:4, category:'apple'}",
  "system": "arithmetic-patterns, please answer the following with no other words: ",
  "query": "What is the next number in this series? 1, 2, 4, 8, 16, ?",
  "response": "32"
}

```

Outputs generated during inference phase of the evaluation job will have following structure:

```

{
  "prompt": "[{'role': 'system', 'content': 'arithmetic-patterns, please answer the following with no other words: '}, {'role': 'user', 'content': 'What is the next number in this series? 1, 2, 4, 8, 16, ?'}]",
  "inference": "['32']",
  "gold": "32",
  "metadata": "{key:4, category:'apple'}"
}

```

**Field descriptions:**

- `prompt`: Formatted input sent to the model
- `inference`: Model's generated response
- `gold`: Expected correct answer from input dataset, response field from the input
- `metadata`: Optional metadata passed through from input

### Prepare Evaluation Config

Command to launch evaluation job. Use `"--override-parameters"` to modify any entry from the recipe.

```

hyperpod start-job -n kubeflow \
  --recipe evaluation/nova/nova_micro_p5_48xl_bring_your_own_dataset_eval \
  --override-parameters '{
    "instance_type": "p5.48xlarge",
    "container": "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-latest",
    "recipes.run.name": "<your-eval-job-name>",
    "recipes.run.model_name_or_path": "<checkpoint-s3-uri>",
    "recipes.run.output_s3_path": "s3://<your-bucket>/eval-results/",
    "recipes.run.data_s3_path": "s3://<your-bucket>/eval-data.jsonl"
  }'

```

## Best Practices

- **Prioritize data quality over volume**: High-quality, diverse, and representative training data is more valuable than large quantities of low-quality data.
- **Include reasoning-instruction-following category**: When using data mixing, include the "reasoning-instruction-following" category to maintain strong generic performance across tasks.
- **Use default learning rates**: Start with default learning rates (1e-5 for LoRA, 5e-6 for full-rank SFT) and adjust only if needed based on validation metrics.
- **Balance Nova data mixing**: Mix maximum 50% Nova data for optimal latency-performance balance. Higher percentages may improve general capabilities but can increase training time.
- **Monitor validation metrics**: Regularly evaluate intermediate checkpoints during training to detect overfitting or performance degradation early.
- **Test on representative datasets**: Ensure your evaluation datasets accurately represent your production use cases for meaningful performance assessment.

## Prepare Training Job Config

### Hyper Parameters

Full set of hyper-parameters other than data mixing:

```

## Run config
run:
  name: my-lora-sft-run
  model_type: amazon.nova-2-lite-v1:0:256k
  model_name_or_path: nova-lite-2/prod
  data_s3_path: s3://my-bucket-name/train.jsonl  # SageMaker Hyperpod (SMHP) only and not compatible with SageMaker Training jobs. Note replace my-bucket-name with your real bucket name for SMHP job
  replicas: 4                      # Number of compute instances for training, allowed values are 4, 8, 16, 32
  output_s3_path: s3://my-bucket-name/outputs/               # Output artifact path (Hyperpod job-specific; not compatible with standard SageMaker Training jobs). Note replace my-bucket-name with your real bucket name for SMHP job

  ## MLFlow configs
  mlflow_tracking_uri: "" # Required for MLFlow
  mlflow_experiment_name: "my-lora-sft-experiment" # Optional for MLFlow. Note: leave this field non-empty
  mlflow_run_name: "my-lora-sft-run" # Optional for MLFlow. Note: leave this field non-empty

training_config:
  max_steps: 100                   # Maximum training steps. Minimal is 4.
  save_steps: 10 # This parameter suggests after how many training steps the checkpoints will be saved. Should be less than or equal to max_steps(please override this value with a numerical value equal or less than max_steps value; min: 4)
  save_top_k: 5                    # Keep top K best checkpoints. Note supported only for SageMaker HyperPod jobs. Minimal is 1.
  max_length: 32768                # Sequence length (options: 8192, 16384, 32768 [default], 65536)
  global_batch_size: 32            # Golbal batch size (options: 32, 64, 128)
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
      lora_plus_lr_ratio: 64.0     # LoRA+ learning rate scaling factor (0.0–100.0)

```

The most relevant parameters for LoRA are learning rate, alpha (scaling parameter), number of epochs to train and warmup steps; for full-rank it is mainly the learning rate, number of epochs, and warmup steps. The recipes are pre-populated with the recommended defaults.

## Set Up Data Mixing Block

Add the data_mixing section to your recipe with the appropriate percentage distribution across dataset categories.

Below we describe each available Nova data category.

### Nova 1.0 Configuration with Data mixing

```

data_mixing:
  dataset_catalog: sft_text       # Nova text dataset catalog
  sources:
    customer_data:
      percent: 50                 # Percent of overall mix to draw from customer data
    nova_data:                    # The remainder will be drawn from Nova data. The categories below must add to 100
      agents: 1                   # autonomous decision-making, task completion, goal-oriented behavior in AI systems
      chat: 51                    # Conversational exchanges demonstrating natural dialogue flow
      code: 8                     # Programming examples and solutions spanning multiple languages
      rai: 1                      # ethical AI principles, safety considerations, and responsible technology deployment
      instruction-following: 13   # precise task execution based on varying levels of user prompts and directives
      stem: 6                     # Technical content covering science, technology, engineering, and mathematics
      planning: 2                 # Sequences demonstrating strategic thinking and step-by-step task breakdown
      reasoning: 8                # Logical deduction, critical thinking, and analytical problem-solving scenarios
      rag: 1                      # combining retrieved external knowledge with generated responses
      translation: 9              # Multi-language content pairs showing accurate translation

```

What do these categories mean?

| Nova 1.0 Text Data Categories | Category Name                                                                                                                       | Info detail |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| agents                        | Training data focused on autonomous decision-making, task completion, and goal-oriented behavior in AI systems                      |
| chat                          | Conversational exchanges demonstrating natural dialogue flow, context maintenance, and appropriate social interactions              |
| code                          | Programming examples and solutions spanning multiple languages, debugging scenarios, and software development best practices        |
| rai                           | Cases and scenarios emphasizing ethical AI principles, safety considerations, and responsible technology deployment                 |
| instruction-following         | Examples of precise task execution based on varying levels of user prompts and directives                                           |
| stem                          | Technical content covering science, technology, engineering, and mathematics, including problem-solving and theoretical concepts    |
| planning                      | Sequences demonstrating strategic thinking, step-by-step task breakdown, and efficient resource allocation                          |
| reasoning                     | Logical deduction, critical thinking, and analytical problem-solving scenarios with clear reasoning chains                          |
| rag                           | Examples of effectively combining retrieved external knowledge with generated responses to provide accurate, contextual information |
| translation                   | Multi-language content pairs showing accurate translation while preserving context, tone, and cultural nuances                      |

### Multimodal Data Mixing (Nova 1.0)

```

data_mixing:
  dataset_catalog: sft_mm        # Nova multi-modal dataset catalog
  sources:
    customer_data:
      percent: 50                 # Percent of overall mix to draw from customer data
    nova_data:                    # The remainder will be drawn from Nova data. The categories below must add to 100
      agents: 11                  # Combining visual and textual inputs
      docs: 17                    # Document-centric data combining text, images, layouts, and formatting
      perception: 10              # Visual-linguistic pairs t
      rag: 4                      # Combining retrieved external knowledge with generated responses
      rai: 3                      # Ethical AI principles, safety considerations, and responsible technology deployment
      reasoning: 10               # Logical analysis, problem-solving, and drawing conclusions
      stem: 17                    # Technical content pairing visual elements (diagrams, charts, equations) with text
      text: 10                    # A balanced pool of contextual text data create from the text-only SFT datasets
      video: 18                   # Video datasets

```

What do these categories mean?

| Nova 1.0 Multimodal Data Categories | Category Name                                                                                                                                                                                                  | Info detail |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| agents                              | Training pairs combining visual and textual inputs that demonstrate how AI systems should interpret, act upon, and interact with multi-sensory environmental information                                       |
| docs                                | Document-centric data combining text, images, layouts, and formatting to train models in understanding and processing various document types and structures to help with concepts like PDF content recognition |
| perception                          | Visual-linguistic pairs teaching models to accurately describe, interpret, and reason about images, videos, and other visual inputs in natural language                                                        |
| rag                                 | Multimodal retrieval examples showing how to effectively combine and reference visual and textual external knowledge to generate accurate, contextual responses                                                |
| reasoning                           | Cases combining visual and textual elements that demonstrate logical analysis, problem-solving, and drawing conclusions across multiple modalities                                                             |
| stem                                | Technical content pairing visual elements (diagrams, charts, equations) with text to teach scientific, mathematical, and technical concepts and problem-solving                                                |
| text                                | A balanced pool of contextual text data create from the text-only SFT Nova dataset categories in order to provide generalist abilities                                                                         |
| video                               | Motion-based visual content focused on temporal understanding and sequential visual-narrative comprehension                                                                                                    |

### Nova 2.0 Configuration with data mixing

```

data_mixing:
  dataset_catalog: sft_1p5_text_chat       # Nova text dataset catalog
  sources:
    customer_data:
      percent: 50                 # Percent of overall mix to draw from customer data
    nova_data:                    # The remainder will be drawn from Nova data. The categories below must add to 100
      agents: 1                   # autonomous decision-making, task completion, goal-oriented behavior in AI systems
      baseline: 10                 # [New in Nova 1.5]
      chat: 0.5                    # Conversational exchanges demonstrating natural dialogue flow
      code: 10                     # Programming examples and solutions spanning multiple languages
      factuality: 0.1               # [New in Nova 1.5]
      identity: 1                 # [New in Nova 1.5]
      long-context: 1             # [New in Nova 1.5]
      math: 2                     # [New in Nova 1.5]
      rai: 1                      # ethical AI principles, safety considerations, and responsible technology deployment
      instruction-following: 13   # precise task execution based on varying levels of user prompts and directives
      stem: 0.5                     # Technical content covering science, technology, engineering, and mathematics
      planning: 10                 # Sequences demonstrating strategic thinking and step-by-step task breakdown
      reasoning-chat: 0.5
      reasoning-code: 0.5
      reasoning-factuality: 0.5
      reasoning-instruction-following: 45
      reasoning-math: 0.5
      reasoning-planning: 0.5
      reasoning-rag: 0.4
      reasoning-rai: 0.5
      reasoning-stem: 0.4
      rag: 1                      # combining retrieved external knowledge with generated responses
      translation: 0.1

```

What do these categories mean?

| Nova 2.0 Text Data Categories   | Category Name                                                                                                                       | Info detail |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| agents                          | Training data focused on autonomous decision-making, task completion, and goal-oriented behavior in AI systems                      |
| baseline                        | Fundamental language data focused on general comprehension, basic communication, and core linguistic capabilities                   |
| chat                            | Conversational exchanges demonstrating natural dialogue flow, context maintenance, and appropriate social interactions              |
| code                            | Programming source code, documentation, and technical discussions from various programming languages and platforms.                 |
| factuality                      | Reference materials and verified information focused on accuracy, source validation, and truth assessment                           |
| identity                        | Personality frameworks and behavioral patterns focused on consistent character traits, values, and interaction styles               |
| long-context                    | Extended texts and complex narratives focused on maintaining coherence and relevance across lengthy exchanges                       |
| math                            | Mathematical content including textbooks, problems, solutions, and mathematical discussions.                                        |
| rai                             | Cases and scenarios emphasizing ethical AI principles, safety considerations, and responsible technology deployment                 |
| instruction-following           | Examples of precise task execution based on varying levels of user prompts and directives                                           |
| stem                            | Technical content covering science, technology, engineering, and mathematics, including problem-solving and theoretical concepts    |
| planning                        | Sequences demonstrating strategic thinking, step-by-step task breakdown, and efficient resource allocation                          |
| reasoning-chat                  | Analytical dialogue scenarios focused on logical discussion and structured conversation flows                                       |
| reasoning-code                  | Programming challenges and algorithmic problems focused on systematic solution development                                          |
| reasoning-factuality            | Information evaluation scenarios focused on critical assessment and verification processes                                          |
| reasoning-instruction-following | Complex task analysis focused on systematic interpretation and methodical execution                                                 |
| reasoning-math                  | Mathematical problem-solving scenarios focused on logical progression and solution strategies                                       |
| reasoning-planning              | Strategic decision-making scenarios focused on systematic approach to goal achievement                                              |
| reasoning-rag                   | Information retrieval and synthesis scenarios focused on contextual understanding and relevant application                          |
| reasoning-rai                   | Ethical decision-making scenarios focused on systematic evaluation of AI safety and fairness                                        |
| reasoning-stem                  | Scientific problem-solving scenarios focused on methodical analysis and solution development                                        |
| rag                             | Examples of effectively combining retrieved external knowledge with generated responses to provide accurate, contextual information |
| translation                     | Multi-language content pairs showing accurate translation while preserving context, tone, and cultural nuances                      |

### Multimodal Data Mixing (Nova 2.0)

```

data_mixing:
  dataset_catalog: sft_1p5_mm_chat       # Nova text dataset catalog
  sources:
    customer_data:
      percent: 50                 # Percent of overall mix to draw from customer data
    nova_data:                    # The remainder will be drawn from Nova data. The categories below must add to 100
      charts: 1
      chat: 38
      code: 20
      docs: 3
      general: 2
      grounding: 1
      rag: 4
      screenshot: 4
      text: 8
      translation: 4
      video: 15

```

Note: Nova 2.0 includes video data category support that is not available in Nova 1.0.

What do these categories mean?

| Nova 2.0 Multimodal Data Categories | Category Name                                                                                                                                                                                                  | Info detail |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| charts                              | Visual representations and descriptions of graphs, pie charts, bar charts, line plots, and other statistical visualizations to help the model understand and communicate quantitative information effectively  |
| chat                                | Conversational data paired with visual elements focused on contextual dialogue understanding and image-based interactions                                                                                      |
| code                                | Programming interfaces and development environments focused on visual code interpretation, IDE screenshots, and technical diagrams                                                                             |
| docs                                | Document-centric data combining text, images, layouts, and formatting to train models in understanding and processing various document types and structures to help with concepts like PDF content recognition |
| general                             | Diverse visual-textual content focused on broad comprehension of images, graphics, and accompanying descriptive text                                                                                           |
| grounding                           | Visual reference materials and labeled imagery focused on connecting language concepts to real-world visual representations                                                                                    |
| rag                                 | Multimodal retrieval examples showing how to effectively combine and reference visual and textual external knowledge to generate accurate, contextual responses                                                |
| screenshot                          | Application interface captures and digital display images focused on understanding software interfaces and digital interactions                                                                                |
| text                                | A balanced pool of contextual text data create from the text-only SFT Nova dataset categories in order to provide generalist abilities                                                                         |
| translation                         | Cross-language visual content focused on multilingual interpretation of text in images and cultural visual elements                                                                                            |
| video                               | Motion-based visual content focused on temporal understanding and sequential visual-narrative comprehension                                                                                                    |

## How to Launch a job

You can also refer to the README, if you only need to get the essential details to kick off first SFT run.

Container Information:

| Container Information and Launch Commands | Model       | Technique             | Subcategory                                                                                     | Image URI                                                                                                                                                                                                                                                                                                            | Hyperpod Launcher Command |
| ----------------------------------------- | ----------- | --------------------- | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| Nova 1.0                                  | Fine-tuning | SFT / PEFT            | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-latest               | hyperpod start-job \ -n kubeflow \ --recipe fine-tuning/nova/nova_1_0/nova_micro/SFT/nova_micro_1_0_p5_gpu_sft \ --override-parameters '{ "instance_type": "ml.p5.48xlarge", "container": "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-latest" }'                                     |
| Nova 1.0                                  | Fine-tuning | SFT with Data Mixing  | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:HP-SFT-DATAMIX                 | hyperpod start-job \ -n kubeflow \ --recipe fine-tuning/nova/forge/nova_1_0/nova_micro/SFT/nova_micro_1_0_p5_gpu_sft_text_with_datamix \ --override-parameters '{ "instance_type": "ml.p5.48xlarge", "container": "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:HP-SFT-DATAMIX" }'               |
| Nova 2.0                                  | Fine-tuning | SFT Text              | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-V2-latest            | hyperpod start-job \ -n kubeflow \ --recipe fine-tuning/nova/nova_2_0/nova_lite/SFT/nova_lite_2_0_p5_gpu_sft \ --override-parameters '{ "instance_type": "ml.p5.48xlarge", "container": "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-V2-latest" }'                                    |
| Nova 2.0                                  | Fine-tuning | SFT Text + Datamixing | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-V2-DATAMIXING-latest | hyperpod start-job \ -n kubeflow \ --recipe fine-tuning/nova/forge/nova_2_0/nova_lite/SFT/nova_lite_2_0_p5_gpu_sft_text_with_datamix \ --override-parameters '{ "instance_type": "ml.p5.48xlarge", "container": "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-V2-DATAMIXING-latest" }' |
| Nova 2.0                                  | Fine-tuning | SFT MM                | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-V2-latest            | hyperpod start-job \ -n kubeflow \ --recipe fine-tuning/nova/nova_2_0/nova_lite/SFT/nova_lite_2_0_p5_gpu_sft \ --override-parameters '{ "instance_type": "ml.p5.48xlarge", "container": "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-V2-latest" }'                                    |
| Nova 2.0                                  | Fine-tuning | SFT MM + Datamixing   | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-V2-DATAMIXING-latest | hyperpod start-job \ -n kubeflow \ --recipe fine-tuning/nova/forge/nova_2_0/nova_lite/SFT/nova_lite_2_0_p5_gpu_sft_mm_with_datamix \ --override-parameters '{ "instance_type": "ml.p5.48xlarge", "container": "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-V2-DATAMIXING-latest" }'   |

Once you're all setup, starting from the root of the sagemaker-hyperpod-cli repository, navigate to the default nova sft recipe folder

- cd /src/hyperpod_cli/sagemaker_hyperpod_recipes/recipes_collection/recipes/training/nova/
- Here you can choose whether you want to run nova 1 or nova 2 recipies based on the choice of base model.

For Nova 1.0 sft:

- If you would like to use a regular sft job , You should be able to see one recipe under this folder
  - cd /src/hyperpod_cli/sagemaker_hyperpod_recipes/recipes_collection/recipes/fine-tuning/nova_1_0/nova_lite/SFT and then you should be able to see one recipe under this folder called nova_lite_1_0_p5x8_gpu_sft.yaml

- If you would like to use datamixing sft Job, you can navigate to the sft Forge recipes folder
  - cd /src/hyperpod_cli/sagemaker_hyperpod_recipes/recipes_collection/recipes/fine-tuning/nova/forge/nova_1_0/nova_lite/SFT and you should be able to see one recipe under this folder called: nova_lite_1_0_p5x8_gpu_sft_with_datamix.yaml

- Edit the sections in the recipe required by the job such as name, data_s3_path, validation_s3_path, output_s3_path, and max_steps.Since we're performing sft, the notion of epochs doesn't apply here.

For Nova 2.0 sft:

- If you would like to use a regular sft job , You should be able to see one recipe under this folder
  - cd /src/hyperpod_cli/sagemaker_hyperpod_recipes/recipes_collection/recipes/fine-tuning/nova_2_0/nova_lite/SFT and then you should be able to see one recipe under this folder called nova_lite_2_0_p5x8_gpu_sft.yaml

- If you would like to use datamixing sft Job, you can navigate to the sft Forge recipes folder
  - cd /src/hyperpod_cli/sagemaker_hyperpod_recipes/recipes_collection/recipes/fine-tuning/nova/forge/nova_2_0/nova_lite/SFT and you should be able to see one recipe under this folder called: nova_lite_2_0_p5x8_gpu_sft_with_datamix.yaml

- Edit the sections in the recipe required by the job such as name, data_s3_path, validation_s3_path, output_s3_path, and max_steps. Since we're performing sft, the notion of epochs doesn't apply here.

The data mixing config will look the same, but with an extra data mixing section at the bottom similar to this

```

data_mixing:
  dataset_catalog: sft_text_lite
  sources:
    nova_data:   # percent inputs for Nova data must sum to 100%; use 0% if you want to exclude a data grouping
      agents: 20
      business-and-finance: 20
      scientific: 20
      code: 20
      factual-and-news: 20
      longform-text: 0
      health-and-medicine: 0
      humanities-and-education: 0
      legal: 0
      math: 0
      additional-languages: 0
      social-and-personal-interest: 0
      entertainment: 0
      reasoning: 0
      other: 0
      tables: 0
    customer_data: # percent input of customer data. 100 = use only customer data, 0 = use only the nova_data mix above
      percent: 25

```

There are two top-level categories of data here:

- nova_data : This is the actual data mixing and is sub-divided into even more categories. It is imperative that they sum up to 100%
  - A complete breakdown of these categories including token count can be found in below

- customer_data : This is your training data referred in the data_s3_path key at the top of your yaml. The percentage provided here determines what the resulting percentage will be for nova_data. For example, in the above percent selections, during training we'll use 25% of customer_data and 75% of nova_data of which 15% will be agents, 15% will be business-and-finance, 15% will be scientific, 15% will be code, and 15% will be factual-and-news

Tip: Run pip install -e . once again and you're ready to submit your job!

We'll be overriding a couple of parameters here to use data mixing:

```

hyperpod start-job \
 -n kubeflow \
 --recipe fine-tuning/nova/forge/nova_2_0/nova_lite/SFT/nova_lite_2_0_p5x8_gpu_sft_with_datamix \
 --override-parameters '{
 "instance_type": "ml.p5.48xlarge",
 "recipes.run.name": "nova-sft-datamixing",
 "container": "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-V2-Datamix",
 "recipes.run.data_s3_path": "s3://sft-data/sft_train_data.jsonl",
 "recipes.run.validation_data_s3_path": "s3://sft-data/sft_val_data.jsonl",
 "recipes.run.output_s3_path": "s3://sft-data/output/
 }'

```

Your output should contain a job name as follows:

```

⚡ MY Desktop ⚡ % hyperpod start-job \
 -n kubeflow \
 --recipe training/nova/forge/nova_2_0/nova_lite/sft/nova_lite_2_0_p5x8_gpu_pretrain_with_datamix \
 --override-parameters '{
 "instance_type": "ml.p5.48xlarge",
 "recipes.run.name": "nova-sft-datamixing",
 "container": "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-V2-Datamix",
 "recipes.run.data_s3_path": "s3://sft-data/sft_train_data.jsonl",
 "recipes.run.validation_data_s3_path": "3://sft-data/sft_val_data.jsonl",
 "recipes.run.output_s3_path": "3://sft-data/output/
 }'

```

Output would be like this:

```

Final command: python3 /local/home/my/Downloads/sagemaker-hyperpod-cli/src/hyperpod_cli/sagemaker_hyperpod_recipes/main.py recipes=training/nova/nova_micro_p5x8_gpu_pretrain cluster_type=k8s cluster=k8s base_results_dir=/local/home/niphaded/Downloads/sagemaker-hyperpod-cli/results cluster.pullPolicy="IfNotPresent" cluster.restartPolicy="OnFailure" cluster.namespace="kubeflow" instance_type="p5d.48xlarge" container="900867814919.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:sft-datamix-rig-final"
Prepared output directory at /local/home/my/Downloads/sagemaker-hyperpod-cli/results/my-sft-run-wzdyn/k8s_templates
Found credentials in shared credentials file: ~/.aws/credentials
Helm script created at /local/home/my/Downloads/sagemaker-hyperpod-cli/results/my-sft-run-wzdyn/niphaded-sft-run-wzdyn_launch.sh
Running Helm script: /local/home/my/Downloads/sagemaker-hyperpod-cli/results/my-sft-run-wzdyn/niphaded-sft-run-wzdyn_launch.sh

NAME: my-sft-run-wzdyn
LAST DEPLOYED: Tue Aug 26 16:21:06 2025
NAMESPACE: kubeflow
STATUS: deployed
REVISION: 1
TEST SUITE: None
Launcher successfully generated: /local/home/my/Downloads/sagemaker-hyperpod-cli/src/hyperpod_cli/sagemaker_hyperpod_recipes/launcher/nova/k8s_templates/SFT

{
 "Console URL": "https://us-east-1.console.aws.amazon.com/sagemaker/home?region=us-east-1#/cluster-management/hyperpod-eks-ga-0703"
}

```

You can view the status of your job using hyperpod list-pods -n kubeflow --job-name my-sft-run-wzdyn

```

hyperpod list-pods -n kubeflow --job-name my-sft-run-wzdyn
{
 "pods": [
  {
   "PodName": "my-sft-run-wzdyn-master-0",
   "Namespace": "kubeflow",
   "Status": "Pending",
   "CreationTime": "2025-08-26 16:21:06+00:00"
  },
  {
   "PodName": "my-sft-run-wzdyn-worker-0",
   "Namespace": "kubeflow",
   "Status": "Pending",
   "CreationTime": "2025-08-26 16:21:06+00:00"
  }
 ]
}

```

or directly use the kubectl command to find them.

For example,

```

kubectl get pods -o wide -w -n kubeflow | (head -n1 ; grep my-sft-run)

NAME                                                         READY   STATUS      RESTARTS   AGE     IP              NODE                           NOMINATED NODE   READINESS GATES
my-sft-run-5suc8-master-0                              0/1     Completed   0          3h23m   172.31.32.132   hyperpod-i-00b3d8a1bf25714e4   <none>           <none>
my-sft-run-5suc8-worker-0                              0/1     Completed   0          3h23m   172.31.44.196   hyperpod-i-0aa7ccfc2bd26b2a0   <none>           <none>
my-sft-run-5suc8-worker-1                              0/1     Completed   0          3h23m   172.31.46.84    hyperpod-i-026df6406a7b7e55c   <none>           <none>
my-sft-run-5suc8-worker-2                              0/1     Completed   0          3h23m   172.31.28.68    hyperpod-i-0802e850f903f28f1   <none>           <none>

```

Pro tip : Make sure to always use the -o wide flag since the EKS node on which the job runs will help you find your logs even faster in the AWS UI

## How to Monitor Job

You can view your logs one of three ways:

### a) Using CloudWatch

Your logs are available in your Amazon Web Services account that contains the hyperpod cluster under CloudWatch. To view them in your browser, navigate to the CloudWatch homepage in your account and search for your cluster name. For example, if your cluster were called my-hyperpod-rig the log group would have the prefix:

- Log group : /aws/sagemaker/Clusters/my-hyperpod-rig/{UUID}
- Once you're in the log group, you can find your specific log using the node instance ID such as - hyperpod-i-00b3d8a1bf25714e4.
  - i-00b3d8a1bf25714e4 here represents the hyperpod friendly machine name where your training job is running. Recall how in the previous command kubectl get pods -o wide -w -n kubeflow | (head -n1 ; grep my-cpt-run) output we captured a column called NODE.
  - The "master" node run was in this case running on hyperpod-i-00b3d8a1bf25714e4 and thus we'll use that string to select the log group to view. Select the one that says SagemakerHyperPodTrainingJob/rig-group/[NODE]

Your logs should look something like this:

### b) Using CloudWatch Insights

If you have your job name handy and don't wish to go through all the steps above, you can simply query all logs under /aws/sagemaker/Clusters/my-hyperpod-rig/{UUID} to find the individual log.

CPT

```

fields @timestamp, @message, @logStream, @log
| filter @message like /(?i)Starting CPT Job/
| sort @timestamp desc
| limit 100

```

For job completion replace Starting SFT Job with SFT Job completed

Then you can click through the results and pick the one that says "Epoch 0" since that will be your master node.

### C) Using the aws cli

You may choose to tail your logs using the . Before doing so, please check your aws cli version using aws --version. It is also recommended to use this utility script that helps in live log tracking in your terminal

for V1:

```

aws logs get-log-events \
 --log-group-name /aws/sagemaker/YourLogGroupName \
 --log-stream-name YourLogStream \
 --start-from-head | jq -r '.events[].message'

```

for V2:

```

aws logs tail /aws/sagemaker/YourLogGroupName \
  --log-stream-name YourLogStream \
 --since 10m \
 --follow

```

### D) Set up ML Flow:

You can track metrics via MLFlow.

Create an MLflow app

Using Studio UI: If you create a training job through the Studio UI, a default MLflow app is created automatically and selected by default under Advanced Options.

Using CLI: If you use the CLI, you must create an MLflow app and pass it as an input to the training job API request.

```

mlflow_app_name="<enter your MLflow app name>"
role_arn="<enter your role ARN>"
bucket_name="<enter your bucket name>"
region="<enter your region>"

mlflow_app_arn=$(aws sagemaker create-mlflow-app \
  --name $mlflow_app_name \
  --artifact-store-uri "s3://$bucket_name" \
  --role-arn $role_arn \
  --region $region)

```

Access the MLflow app

Using CLI: Create a presigned URL to access the MLflow app UI:

```

aws sagemaker create-presigned-mlflow-app-url \
  --arn $mlflow_app_arn \
  --region $region \
  --output text

```

Once ML Flow is setup, you can pass the URI in your recipe or use override when starting the job. One example of how to do that can be found in README.

## How to evaluate your model after SFT?

### Prerequisites

- Checkpoint S3 URI from your training job's manifest.json file (for trained models)
- Evaluation dataset uploaded to S3 in the correct format
- Output S3 path for evaluation results

Out of the box benchmarks: Use out of the box benchmarks to validate the performance on general tasks. For more details check here.

### Bring your own data:

You can also supply your custom data by formatting them in below format and then using below mentioned containers to get inference results along with log probabilities for calibrations if needed.

Crate jsonl per task with the following structure:

```

{
  "metadata": "{key:4, category:'apple'}",
  "system": "arithmetic-patterns, please answer the following with no other words: ",
  "query": "What is the next number in this series? 1, 2, 4, 8, 16, ?",
  "response": "32"
}

```

Outputs generated during inference phase of the evaluation job will have following structure:

```

{
  "prompt": "[{'role': 'system', 'content': 'arithmetic-patterns, please answer the following with no other words: '}, {'role': 'user', 'content': 'What is the next number in this series? 1, 2, 4, 8, 16, ?'}]",
  "inference": "['32']",
  "gold": "32",
  "metadata": "{key:4, category:'apple'}"
}

```

Field descriptions:

- prompt: Formatted input sent to the model
- inference: Model's generated response
- gold: Expected correct answer from input dataset, response field from the input
- metadata: Optional metadata passed through from input

### Prepare Evaluation Config

Command to launch evaluation job. Use "--override-parameters" to modify any entry from the recipe.

```

hyperpod start-job -n kubeflow \
  --recipe evaluation/nova/nova_micro_p5_48xl_bring_your_own_dataset_eval \
  --override-parameters '{
    "instance_type": "p5.48xlarge",
    "container": "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-latest",
    "recipes.run.name": "<your-eval-job-name>",
    "recipes.run.model_name_or_path": "<checkpoint-s3-uri>",
    "recipes.run.output_s3_path": "s3://<your-bucket>/eval-results/",
    "recipes.run.data_s3_path": "s3://<your-bucket>/eval-data.jsonl"
  }'

```

### Launch Your Evaluation Job

Job launching commands for different recipes with corresponding images.

| Evaluation Job Launch Commands | Model      | Technique | Subcategory                                                                         | Image URI                                                                                                                                                                                                                                                                            | Command |
| ------------------------------ | ---------- | --------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| Nova 1.0                       | Evaluation | Eval      | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-latest | hyperpod start-job \ -n kubeflow \ --recipe evaluation/nova/nova_1_0/nova_lite/nova_lite_2_0_p5_48xl_gpu_ft_eval \ --override-parameters '{ "instance_type": "ml.p5.48xlarge", "container": "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-latest" }' |
| Nova 2.0                       | Evaluation | Eval      | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-latest | hyperpod start-job -n kubeflow \ --recipe evaluation/nova/nova_2_0/nova_lite/nova_lite_2_0_p5_48xl_gpu_ft_eval \ --override-parameters '{ "instance_type": "ml.p5.48xlarge", "container": "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-latest" }'   |

## Lessons Learned and Tips

- The quality of the SFT dataset is critical. You should make every effort to filter out low-quality data. If you have a small subset of exceptionally high-quality data—in terms of both complexity and accuracy—you may consider placing it toward the end of training to help the model converge better.
- We leverage both text and multimodal (MM) datasets for data mixing. Our experiments with text dataset show that adding Nova's proprietary "reasoning-instruction-following" category significantly improves performance across generic benchmarks. We recommend including this category in your data mixing strategy if you care about generic benchmark that is regressed after you did SFT with your datasets.
- For MM datasets, our experiments indicate that incorporating over 20% of video categories into the mix is beneficial for maintaining generic benchmark performance.
- Further, SFT with data mixing is quite sensitive to learning rate so our finding suggests to fine-tune with the default learning rate i.e. 1e-5 for LoRA and 5e-6 for FR.
- Finally, there is a trade off between latency and performance if you mix Nova proprietary datasets so our findings suggest to mix 50% in max as a good balance.
