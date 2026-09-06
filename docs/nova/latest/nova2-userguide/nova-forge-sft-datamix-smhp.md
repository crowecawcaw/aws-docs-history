

# Data mixing on SageMaker HyperPod
<a name="nova-forge-sft-datamix-smhp"></a>

## Introduction
<a name="introduction"></a>

Supervised fine-tuning (SFT) is a training approach that uses datasets containing input-output pairs. You provide examples of prompts along with the correct responses, and the model learns to produce similar outputs. The model's weights are adjusted to minimize a supervised loss, typically cross-entropy between its predictions and the target response tokens.

## When to use supervised fine-tuning
<a name="when-to-use-sft"></a>

SFT is best when you have a well-defined task with clear desired outputs. If you can explicitly say "Given X input, the correct/desired output is Y" and you can gather examples of such X-Y mappings, then supervised fine-tuning is a great choice. Some scenarios where SFT excels include:
+ **Structured or complex classification tasks** – For example, classifying internal documents or contracts into many custom categories. With SFT, the model can learn these specific categories far better than prompting alone.
+ **Question-answering or transformation tasks with known answers** – For example, fine-tuning a model to answer questions from a company's knowledge base, or to convert data between formats, where each input has a correct response.
+ **Formatting and style consistency**: If you need the model to always respond in a certain format or tone, you can fine-tune on examples of the correct format/tone. For instance, training on prompt-response pairs that demonstrate a particular brand voice or style can teach the model with that style in its outputs. Instruction-following behavior is often initially taught via SFT on curated examples of good assistant behavior.

SFT is the most direct way to teach an LLM a new skill or behavior when you can specify what the right behavior looks like. It leverages the model's existing language understanding and focuses it on your task. Do not use SFT when the gap is knowledge rather than behavior; it will not make the model learn new facts, jargon, or recent events. In those cases, prefer continued pre-training on large in-domain corpora or retrieval-augmented generation to bring external knowledge at inference. When you can measure quality but cannot label a single right answer, reinforcement fine-tuning with verifiable rewards or an LLM-as-judge might be preferable to SFT.

Depending on task complexity and performance of the Nova model without tuning, plan for thousands to tens of thousands of demonstrations per task, with data quality, consistency, and diversity mattering more than raw volume.

## Choosing between parameter-efficient and full-rank SFT
<a name="parameter-efficient-vs-full-rank"></a>

Nova customization recipes enable you to perform parameter efficient, in particular LoRA, or full rank SFT. If you want a straightforward, cost-efficient model update, or have very little data, favor parameter-efficient methods so you train small adapters while leaving most of the backbone untouched (full rank SFT updates all model parameters).

## Data mixing for SFT
<a name="data-mixing"></a>

With data mixing, you can combine your custom training datasets with Nova's proprietary training data. This feature is available for both Nova 1.0 and Nova 2.0 models.

**Nova Proprietary Data Type**: Nova supports both text and multimodal SFT data types. It is organized into multiple data categories each containing a blend of tasks relevant for the corresponding category.

**Nova Proprietary Data Categories**: Text datasets includes several categories including: autonomous decision making, task completion, goal oriented datasets (agents), both reasoning and non-reasoning precise task execution datasets (reasoning-instruction-following, instruction-following), sequences demonstrating strategic thinking and step-by-step task breakdown (planning), responsible AI (rai), long-context, factuality, math, stem and many more. Similarly, multimodal datasets includes video, screenshot, charts and many more.

The data mixing feature allows you to blend your own fine-tuning training samples with samples from the Nova datasets used to fine-tune the Nova. This can prevent overfitting on your custom training and "catastrophic forgetting" of Nova capabilities, or help you build capabilities when training from a new pretrained checkpoint.

To mix in Nova data, you simply need to add a data\_mixing block as a top-level section in your recipe YAML file (alongside run and training\_config). Text and multi-modal data mixing blocks have different content. Please refer to corresponding recipes.

### Supported models
<a name="supported-models"></a>
+ Nova 2.0 Lite

### Supported modality
<a name="supported-modality"></a>
+ Text
+ Multimodal

## YAML configuration examples
<a name="yaml-configuration-examples"></a>

### Nova 2.0 configuration example
<a name="nova-2-configuration"></a>

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

### Nova 2.0 text data mixing
<a name="nova-2-text-mixing"></a>

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

### Nova 2.0 multimodal data mixing
<a name="nova-2-multimodal-mixing"></a>

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

## Model checkpoints
<a name="model-checkpoints"></a>

### Nova 2.0 checkpoints
<a name="nova-2-checkpoints"></a>
+ **PRE-TRAINED** [`nova-lite-2/pretraining-text-RD`]: Checkpoint after constant learning rate and ramp-down stages where model is trained on trillions of tokens. [Outcome of Stage 2]
+ **MID-TRAINED** [`nova-lite-2/pretraining-text-CE`]: Allows customers with intermediate volumes of unstructured data to introduce their data with a more conservative learning rate than pre-training, absorbing domain-specific knowledge while avoiding catastrophic forgetting. [Outcome of Stage 3]
+ **FINAL** [`nova-lite-2/prod`]: Fully aligned final checkpoint that has gone through all pretraining and post training steps. [Outcome of Stage 4]

**Training Stages:**
+ Stage 1: PT Ckpt, initial pre-training with constant learning rate
+ Stage 2: PT Ckpt, learning rate ramp-down
+ Stage 3: PT Ckpt, context extension training
+ Stage 4: instruction-following alignment and safety training

## Training approaches
<a name="training-approaches"></a>


**Training approach selection guide**  

| Data Type | Data Volume | Perform | With Checkpoint | 
| --- | --- | --- | --- | 
| Large-scale unstructured raw domain data (documents, logs, articles, code, etc.) | 1T\+ Tokens | Continued Pre-Training | End of Constant Learning Rate (CLR) | 
| Large-scale unstructured raw domain data | 100B\+ Tokens | Mid-Training | End of CLR | 
| Smaller volumes of unstructured raw data; Structured reasoning traces / CoT data | 1B\+ Tokens | Mid-Training | Nova base model | 
| Structured demonstrations (high-quality input-output pairs, curated task instructions, multi-turn dialogues) | 1K\+ Examples | Supervised Fine-Tuning (SFT) | Nova base model | 

## Prerequisites
<a name="prerequisites"></a>
+ We assume that you've already set up an SageMaker HyperPod cluster with a restricted instance group (RIG) that has active capacity. If you have not completed this setup, see [Setting up Nova Forge with SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-forge.html) or the [Nova Forge HyperPod Setup Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/dcac6f7a-3c61-4978-8344-7535526bf743/en-US) to complete your cluster and RIG setup.
+ You will require **p5.48xlarge** EC2 instances to execute this recipe. The minimum number instances required to execute this recipe efficiently are as follows:
  + **Nova Lite 2.0 - 4 p5.48xlarge**
+ Install the Forge Specific SageMaker HyperPod CLI. For instructions, see the [Nova Forge HyperPod Setup Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/dcac6f7a-3c61-4978-8344-7535526bf743/en-US).
+ Confirm that you can connect to your cluster using `hyperpod get-clusters`
  + Note that this command will list all SageMaker HyperPod clusters in your account
+ Confirm that your training, and optionally validation data, is available in an S3 bucket that is accessible by the execution role of your SageMaker HyperPod cluster. For data preparation, refer to next section.
+ Have AWS CLI setup completed. If you have not completed the setup, please see [Getting started with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html).
+ **Verification**: After completing the setup, confirm you can successfully run the following commands

  ```
  aws sagemaker describe-cluster --cluster-name <cluster-name> --region <region>
  
  hyperpod connect-cluster --cluster-name cluster-name
  ```

## Systematic approach to successful SFT
<a name="systematic-approach"></a>
+ **Data Preparation**: Follow established guidelines to create, clean, or reformat datasets into the required structure. Ensure that inputs, outputs, and auxiliary information (such as reasoning traces or metadata) are properly aligned and formatted.
+ **Training Configuration**: Define how the model will be trained. When using Amazon SageMaker HyperPod, this configuration is written in a YAML recipe file that includes:
  + Data source paths (training and validation datasets)
  + Key hyperparameters (number of training steps, learning rate, batch size)
  + Optional components (distributed training parameters, etc)
  + Data Mixing setting (defines proportions of customer and Nova data categories)
+ **Optimize SFT Hyper Parameters**: SFT recipe parameter values we recommend are are a great starting point and a robust choice. If you want to optimize them further for your use case do multiple SFT runs with different parameter combinations and pick the best one. You can select parameter combinations following Hyper-Parameter Optimization method of your choice. A simple approach is to vary the value of one parameter (default\*0.5, default, default\*2) while keeping other default value for other parameters, repeat this for each parameter you want to optimize, and iterate if needed. The most relevant parameters for LoRA are learning rate, alpha (scaling parameter), number of epochs to train and warmup steps; for full-rank it is mainly the learning rate, number of epochs, and warmup steps.

## Experiment sequencing and data mixing
<a name="experiment-sequencing"></a>
+ If you have only SFT data (train/dev/test) for a set of tasks and care only about the test performance on these tasks
  + Do SFT without mixing on [FINAL] Nova checkpoint. Use the default SFT hyper-parameters and optionally optimize them for your use case. Monitor validation metrics and/or evaluate intermediate checkpoints for larger datasets.
+ If you have only SFT data (train/dev/test) for a set of tasks and care about test performance on these tasks and general benchmarks in the domain of interest
  + Start by doing SFT with Nova data mixing on a pre-training checkpoint (PRE-TRAINED or MID-TRAINED checkpoint, not FINAL). Using an intermediate checkpoint allows the model to better integrate your custom data with Nova's proprietary data while maintaining strong general capabilities.
  + Run shorter SFT training runs with varying amount of Nova data in the mix (e.g., 10%, 25%, 50%, 75%) and Nova data category selections that complement your use case (e.g., pick instruction following category if you care about general instruction following ability). Monitor validation metrics and evaluate if mixing helps performance on general benchmarks. Select the training mix and checkpoint that leads to the best combination of performance on your task and general performance. Depending on the use case, both task and general performances can be further improved using reinforcement fine tuning (RFT).

## Preparing datasets for SFT
<a name="dataset-preparation"></a>

**Nova 2.0**: Use the [Converse API format](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-call.html). Nova 2.0 data format can contain additional [reasoning fields](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ReasoningContentBlock.html).

Reasoning content captures the model's intermediate thinking steps before generating a final answer. In the `assistant` turn, use the `reasoningContent` field to include reasoning traces. Use plain text for reasoning content, avoid markup tags like `<thinking>` and `</thinking>` unless specifically required by your task, and ensure reasoning content is clear and relevant to the problem-solving process.

## Best practices
<a name="best-practices"></a>
+ **Prioritize data quality over volume**: High-quality, diverse, and representative training data is more valuable than large quantities of low-quality data.
+ **Include reasoning-instruction-following category**: When using data mixing, include the "reasoning-instruction-following" category to maintain strong generic performance across tasks.
+ **Use default learning rates**: Start with default learning rates (1e-5 for LoRA, 5e-6 for full-rank SFT) and adjust only if needed based on validation metrics.
+ **Balance Nova data mixing**: Mix maximum 50% Nova data for optimal latency-performance balance. Higher percentages may improve general capabilities but can increase training time.
+ **Monitor validation metrics**: Regularly evaluate intermediate checkpoints during training to detect overfitting or performance degradation early.
+ **Test on representative datasets**: Ensure your evaluation datasets accurately represent your production use cases for meaningful performance assessment.

## Preparing training job configuration
<a name="prepare-training-job-config"></a>

### Hyperparameters
<a name="hyper-parameters"></a>

Full set of hyper-parameters other than data mixing:

```
## Run config
run:
  name: my-lora-sft-run
  model_type: amazon.nova-2-lite-v1:0:256k
  model_name_or_path: nova-lite-2/prod
  data_s3_path: s3://my-bucket-name/train.jsonl  # SageMaker HyperPod (SMHP) only and not compatible with SageMaker Training jobs. Replace my-bucket-name with your actual bucket name
  replicas: 4                      # Number of compute instances for training, allowed values are 4, 8, 16, 32
  output_s3_path: s3://my-bucket-name/outputs/               # Output artifact path (Hyperpod job-specific; not compatible with standard SageMaker Training jobs). Replace my-bucket-name with your actual bucket name
  
  ## MLFlow configs
  mlflow_tracking_uri: "" # Required for MLFlow
  mlflow_experiment_name: "my-lora-sft-experiment" # Optional for MLFlow. Note: leave this field non-empty
  mlflow_run_name: "my-lora-sft-run" # Optional for MLFlow. Note: leave this field non-empty
  
training_config:
  max_steps: 100                   # Maximum training steps. Minimal is 4.
  save_steps: 10 # How often to save checkpoints (in training steps). Must be an even number and less than or equal to max_steps (min: 4)
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

## Setting up the data mixing block
<a name="set-up-data-mixing-block"></a>

Add the data\_mixing section to your recipe with the appropriate percentage distribution across dataset categories.

The following table describes each available Nova data category.

### Nova 2.0 configuration with data mixing
<a name="nova-2-config-data-mixing"></a>

```
data_mixing:
  dataset_catalog: sft_1p5_text_chat       # Nova text dataset catalog
  sources:
    customer_data:
      percent: 50                 # Percent of overall mix to draw from customer data
    nova_data:                    # The remainder will be drawn from Nova data. The following categories must add to 100
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

The following table describes each available Nova data category.


**Nova 2.0 text data categories**  

| Category Name | Info detail | 
| --- | --- | 
| agents | Agentic reasoning and task completion | 
| baseline | General language comprehension | 
| chat | Conversational fluency | 
| code | Code generation and understanding | 
| factuality | Factual accuracy and verification | 
| identity | Consistent identity and persona | 
| long-context | Long-context comprehension | 
| math | Mathematics | 
| rai | Responsible AI alignment | 
| instruction-following | Instruction following | 
| stem | STEM | 
| planning | Planning and task decomposition | 
| reasoning-chat | Conversational reasoning | 
| reasoning-code | Code reasoning | 
| reasoning-factuality | Factual reasoning and verification | 
| reasoning-instruction-following | Reasoning for complex instruction following | 
| reasoning-math | Mathematical reasoning | 
| reasoning-planning | Reasoning for planning and strategy | 
| reasoning-rag | Reasoning with retrieved context | 
| reasoning-rai | Responsible AI reasoning | 
| reasoning-stem | STEM reasoning | 
| rag | Retrieval-augmented generation | 
| translation | Multilingual comprehension and fluency | 

### Multimodal data mixing (Nova 2.0)
<a name="nova-2-mm-data-mixing"></a>

```
data_mixing:
  dataset_catalog: sft_1p5_mm_chat       # Nova multimodal dataset catalog
  sources:
    customer_data:
      percent: 50                 # Percent of overall mix to draw from customer data
    nova_data:                    # The remainder will be drawn from Nova data. The following categories must add to 100
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

The following table describes each available multimodal data category.


**Nova 2.0 multimodal data categories**  

| Category Name | Info detail | 
| --- | --- | 
| charts | Chart and data visualization understanding | 
| chat | Multimodal conversational fluency | 
| code | Visual code interpretation | 
| docs | Document understanding | 
| general | General visual comprehension | 
| grounding | Visual grounding | 
| rag | Multimodal retrieval-augmented generation | 
| screenshot | UI and screenshot understanding | 
| text | Text-based generalist abilities | 
| translation | Multilingual visual comprehension | 
| video | Video understanding | 

## Launching a job
<a name="launch-training-job"></a>

You can also refer to the README, if you only need to get the essential details to kick off first SFT run.

Container Information:


**Container information and launch commands**  

| Model | Technique | Subcategory | Image URI | Hyperpod Launcher Command | 
| --- | --- | --- | --- | --- | 
| Nova 2.0 | Fine-tuning | SFT Text (with or without data mixing) | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-V2-latest | hyperpod start-job \\ -n kubeflow \\ --recipe fine-tuning/nova/forge/nova\_2\_0/nova\_lite/SFT/nova\_lite\_2\_0\_p5\_gpu\_sft\_text\_with\_datamix \\ --override-parameters '{ "instance\_type": "ml.p5.48xlarge", "container": "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-V2-latest" }' | 
| Nova 2.0 | Fine-tuning | SFT MM (with or without data mixing) | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-V2-latest | hyperpod start-job \\ -n kubeflow \\ --recipe fine-tuning/nova/forge/nova\_2\_0/nova\_lite/SFT/nova\_lite\_2\_0\_p5\_gpu\_sft\_mm\_with\_datamix \\ --override-parameters '{ "instance\_type": "ml.p5.48xlarge", "container": "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-V2-latest" }' | 

Once you're all setup, starting from the root of the sagemaker-hyperpod-cli repository, navigate to the default nova sft recipe folder
+ cd /src/hyperpod\_cli/sagemaker\_hyperpod\_recipes/recipes\_collection/recipes/fine-tuning/nova/
+ Here you can choose whether you want to run nova 1 or nova 2 recipies based on the choice of base model.

For Nova 2.0 sft:
+ If you would like to use a regular sft job , You should be able to see one recipe under this folder
  + cd /src/hyperpod\_cli/sagemaker\_hyperpod\_recipes/recipes\_collection/recipes/fine-tuning/nova\_2\_0/nova\_lite/SFT and then you should be able to see one recipe under this folder called nova\_lite\_2\_0\_p5\_gpu\_sft.yaml
+ If you would like to use datamixing sft Job, you can navigate to the sft Forge recipes folder
  + cd /src/hyperpod\_cli/sagemaker\_hyperpod\_recipes/recipes\_collection/recipes/fine-tuning/nova/forge/nova\_2\_0/nova\_lite/SFT and you should be able to see one recipe under this folder called: nova\_lite\_2\_0\_p5\_gpu\_sft\_text\_with\_datamix.yaml
+ Edit the sections in the recipe required by the job such as name, data\_s3\_path, validation\_s3\_path, output\_s3\_path, and max\_steps. Since we're performing sft, the notion of epochs doesn't apply here.

The data mixing configuration file includes an additional `data_mixing` section, as shown in the following example.

```
data_mixing:
  dataset_catalog: sft_1p5_text_chat
  sources:
    customer_data:
      percent: 25
    nova_data:                    # The categories must add to 100
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

The data mixing configuration includes two top-level categories:
+ nova\_data : This is the actual data mixing and is sub-divided into even more categories. It is imperative that they sum up to 100%
+ customer\_data : This is your training data referenced in the `data_s3_path` key at the top of your YAML. The percentage provided here determines the resulting percentage for nova\_data. For example, with the preceding percent selections, during training the job uses 25% of customer\_data and 75% of nova\_data.

Tip: Run pip install -e . once again and you're ready to submit your job\!

The following command overrides parameters for data mixing:

```
hyperpod start-job \
 -n kubeflow \
 --recipe fine-tuning/nova/forge/nova_2_0/nova_lite/SFT/nova_lite_2_0_p5_gpu_sft_text_with_datamix \
 --override-parameters '{
 "instance_type": "ml.p5.48xlarge",
 "recipes.run.name": "nova-sft-datamixing",
 "container": "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-V2-latest",
 "recipes.run.data_s3_path": "s3://sft-data/sft_train_data.jsonl",
 "recipes.run.validation_data_s3_path": "s3://sft-data/sft_val_data.jsonl",
 "recipes.run.output_s3_path": "s3://sft-data/output/"
 }'
```

Your output should contain a job name as follows:

```
⚡ MY Desktop ⚡ % hyperpod start-job \
 -n kubeflow \
 --recipe fine-tuning/nova/forge/nova_2_0/nova_lite/SFT/nova_lite_2_0_p5_gpu_sft_text_with_datamix \
 --override-parameters '{
 "instance_type": "ml.p5.48xlarge",
 "recipes.run.name": "nova-sft-datamixing",
 "container": "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-V2-latest",
 "recipes.run.data_s3_path": "s3://sft-data/sft_train_data.jsonl",
 "recipes.run.validation_data_s3_path": "s3://sft-data/sft_val_data.jsonl",
 "recipes.run.output_s3_path": "s3://sft-data/output/"
 }'
```

Output would be like this:

```
Final command: python3 /local/home/my/Downloads/sagemaker-hyperpod-cli/src/hyperpod_cli/sagemaker_hyperpod_recipes/main.py recipes=fine-tuning/nova/forge/nova_2_0/nova_lite/SFT/nova_lite_2_0_p5_gpu_sft_text_with_datamix cluster_type=k8s cluster=k8s base_results_dir=/local/home/my/Downloads/sagemaker-hyperpod-cli/results cluster.pullPolicy="IfNotPresent" cluster.restartPolicy="OnFailure" cluster.namespace="kubeflow" instance_type="ml.p5.48xlarge" container="708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-V2-latest"
Prepared output directory at /local/home/my/Downloads/sagemaker-hyperpod-cli/results/my-sft-run-wzdyn/k8s_templates
Found credentials in shared credentials file: ~/.aws/credentials
Helm script created at /local/home/my/Downloads/sagemaker-hyperpod-cli/results/my-sft-run-wzdyn/my-sft-run-wzdyn_launch.sh
Running Helm script: /local/home/my/Downloads/sagemaker-hyperpod-cli/results/my-sft-run-wzdyn/my-sft-run-wzdyn_launch.sh

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

## Monitoring jobs
<a name="monitor-training-job"></a>

You can view your logs one of three ways:

### Using CloudWatch
<a name="using-cloudwatch"></a>

Your logs are available in your Amazon Web Services account that contains the hyperpod cluster under CloudWatch. To view them in your browser, navigate to the CloudWatch homepage in your account and search for your cluster name. For example, if your cluster were called my-hyperpod-rig the log group would have the prefix:
+ Log group : /aws/sagemaker/Clusters/my-hyperpod-rig/{UUID}
+ Once you're in the log group, you can find your specific log using the node instance ID such as - hyperpod-i-00b3d8a1bf25714e4.
  + i-00b3d8a1bf25714e4 here represents the hyperpod friendly machine name where your training job is running. Recall how in the previous command kubectl get pods -o wide -w -n kubeflow \| (head -n1 ; grep my-sft-run) output we captured a column called NODE.
  + The "master" node run was in this case running on hyperpod-i-00b3d8a1bf25714e4 and thus we'll use that string to select the log group to view. Select the one that says SagemakerHyperPodTrainingJob/rig-group/[NODE]

### Using CloudWatch Insights
<a name="using-cloudwatch-insights"></a>

If you have your job name handy, you can query all logs under /aws/sagemaker/Clusters/my-hyperpod-rig/{UUID} to find the individual log.

SFT

```
fields @timestamp, @message, @logStream, @log 
| filter @message like /(?i)Starting SFT Job/
| sort @timestamp desc 
| limit 100
```

For job completion replace Starting SFT Job with SFT Job completed

Then you can select from the results and pick the one that says "Epoch 0" since that will be your master node.

### Using the AWS CLI
<a name="using-aws-cli"></a>

You may choose to tail your logs using the AWS CLI. Before doing so, please check your AWS CLI version using `aws --version`. It is also recommended to use this utility script that helps in live log tracking in your terminal

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

### Setting up MLflow
<a name="setup-mlflow"></a>

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

After MLflow is set up, you can pass the URI in your recipe or use override when starting the job.

## Evaluating your model after SFT
<a name="evaluate-after-sft"></a>

### Prerequisites
<a name="eval-prerequisites"></a>
+ Checkpoint S3 URI from your training job's manifest.json file (for trained models)
+ Evaluation dataset uploaded to S3 in the correct format
+ Output S3 path for evaluation results

Out of the box benchmarks: Use out of the box benchmarks to validate the performance on general tasks. For more information, see [Evaluating Nova models on HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-hp-evaluate.html).

### Bring your own data
<a name="bring-your-own-eval-data"></a>

You can also supply your custom data by formatting them in the following format and then using the following containers to get inference results along with log probabilities for calibrations if needed.

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

Field descriptions:
+ prompt: Formatted input sent to the model
+ inference: Model's generated response
+ gold: Expected correct answer from input dataset, response field from the input
+ metadata: Optional metadata passed through from input

### Preparing evaluation configuration
<a name="prepare-eval-config"></a>

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

### Launching your evaluation job
<a name="launch-eval-job"></a>

Job launching commands for different recipes with corresponding images.


**Evaluation job launch commands**  

| Model | Technique | Subcategory | Image URI | Command | 
| --- | --- | --- | --- | --- | 
| Nova 2.0 | Evaluation | Eval | 708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-latest | hyperpod start-job -n kubeflow \\ --recipe evaluation/nova/nova\_2\_0/nova\_lite/nova\_lite\_2\_0\_p5\_48xl\_gpu\_ft\_eval \\ --override-parameters '{ "instance\_type": "ml.p5.48xlarge", "container": "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-latest" }' | 

## Lessons learned and tips
<a name="lessons-learned-tips"></a>
+ The quality of the SFT dataset is critical. You should make every effort to filter out low-quality data. If you have a small subset of exceptionally high-quality data—in terms of both complexity and accuracy—you may consider placing it toward the end of training to help the model converge better.
+ We leverage both text and multimodal (MM) datasets for data mixing. Our experiments with text dataset show that adding Nova's proprietary "reasoning-instruction-following" category significantly improves performance across generic benchmarks. We recommend including this category in your data mixing strategy if you care about generic benchmark that is regressed after you did SFT with your datasets.
+ For MM datasets, our experiments indicate that incorporating over 20% of video categories into the mix is beneficial for maintaining generic benchmark performance.
+ Further, SFT with data mixing is quite sensitive to learning rate so our finding suggests to fine-tune with the default learning rate i.e. 1e-5 for LoRA and 5e-6 for FR.
+ Finally, there is a trade off between latency and performance if you mix Nova proprietary datasets so our findings suggest to mix 50% in max as a good balance.