# CPT on Nova 2.0

Amazon Nova Lite 2.0 is a reasoning model trained on larger and more diverse datasets
than Nova Lite 1.0. Despite being a larger model, Nova Lite 2.0 delivers faster inference
than Nova Lite 1.0 while offering enhanced reasoning capabilities, longer context lengths,
and improved multilingual performance.

CPT on Nova 2.0 allows you to extend these advanced capabilities with your
domain-specific data, enabling the model to develop deep expertise in specialized areas
while maintaining its superior reasoning and analytical abilities.

The following is a sample recipe for CPT. You can find this recipe and others in the [recipes](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/training/nova "https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/training/nova") repository.

```
# Note:
# This recipe can run on p5.48xlarge
# Run config
run:
  name: "my-cpt-run"                           # A descriptive name for your training job
  model_type: "amazon.nova-2-lite-v1:0:256k"   # Model variant specification, do not change
  model_name_or_path: "nova-lite-2/prod"        # Base model path, do not change
  replicas: 8                                   # Number of compute instances for training, allowed values are 4, 8, 16, 32
  data_s3_path: ""                              # Customer data paths
  validation_data_s3_path: ""                   # Customer validation data paths
  output_s3_path: ""                            # Output artifact path,  job-specific configuration - not compatible with standard SageMaker Training Jobs
  mlflow_tracking_uri: ""                       # Required for MLFlow
  mlflow_experiment_name: "my-cpt-experiment"   # Optional for MLFlow. Note: leave this field non-empty
  mlflow_run_name: "my-cpt-run"                 # Optional for MLFlow. Note: leave this field non-empty

## Training specific configs
training_config:
  task_type: cpt
  max_length: 8192                              # Maximum context window size (tokens)
  global_batch_size: 256                        # Global batch size, allowed values are 32, 64, 128, 256.

  trainer:
    max_steps: 10                               # The number of training steps to run total
    val_check_interval: 10                      # The number of steps between running validation. Integer count or float percentage
    limit_val_batches: 2                        # Batches of the validation set to use each trigger

  model:
    hidden_dropout: 0.0                         # Dropout for hidden states, must be between 0.0 and 1.0
    attention_dropout: 0.0                      # Dropout for attention weights, must be between 0.0 and 1.0

  optim:
    optimizer: adam
    lr: 1e-5                                    # Learning rate
    name: distributed_fused_adam                # Optimizer algorithm, do not change
    adam_w_mode: true                           # Enable AdamW mode
    eps: 1e-06                                  # Epsilon for numerical stability
    weight_decay: 0.0                           # L2 regularization strength, must be between 0.0 and 1.0
    adam_beta1: 0.9                             # Beta1 for Adam optimizer
    adam_beta2: 0.95                            # Beta2 for Adam optimizer
    sched:
      warmup_steps: 10                          # Learning rate warmup steps
      constant_steps: 0                         # Steps at constant learning rate
      min_lr: 1e-6                              # Minimum learning rate, must be lower than lr
```

## Data preparation for CPT on 2.0

###### Data format requirements

Training and validation datasets must be JSONL files following the format shown below,
where each line contains a JSON object representing a conversation with the required
fields and structure. Here is an example:

```
{"text": "AWS stands for Amazon Web Services"}
{"text": "Amazon SageMaker is a fully managed machine learning service"}
{"text": "Amazon Bedrock is a fully managed service for foundation models"}
```

Text entries should contain naturally flowing, high-quality content that represents
the target domain.

Test that the data is capable of being converted into [Arrow format](https://huggingface.co/docs/datasets/en/about_arrow "https://huggingface.co/docs/datasets/en/about_arrow"). Use the
python script below to help with it. Ensure the `datasets==2.18.0` version at
minimum is used:

```
from datasets import load_dataset, load_from_disk
from pathlib import Path

input_path = Path("<Your jsonl file>")
output_path = Path("<Your output directory>")

dataset = load_dataset("json", data_files=str(input_path), split="train")
dataset.save_to_disk(str(output_path), max_shard_size="1GB")

try:
  test_dataset = datasets.load_from_disk(output_dir)
  print(f"Dataset loaded successfully ✅! Contains {len(test_dataset)} samples")
except Exception as e:
  print(e)
```

It should print the same number of lines that were in the JSONL file.

When using datamixing, run the first job with `max_steps=2`. This will help
create optimizations in the cluster for data access and validate that all the datamixes
are available.

###### How to prepare data for CPT

Training data is the most crucial determining factor for the success of continuous
pre-training. While CPT data is often described as "unlabeled," the reality is far more
nuanced. How data is structured, formatted, and presented determines whether the model
will acquire the knowledge and skills required for the business use case.

### Preparing structured business datasets

for CPT

This is a common challenge for companies and organizations building foundation
models specialized in their domain. Most businesses possess rich repositories of
structured data: product catalogs, user profiles, transaction logs, form submissions,
API calls, and operational metadata. At first glance, this looks very different from
the unstructured web text typically used in standard pre-training.

To effectively learn from structured business data, think carefully about
downstream tasks and design the data presentation to force the model to learn the
right predictive relationships.

To unlock the full potential of continuous pre-training, consider:

- What tasks the model should perform at inference time
- What information is present in the raw data
- How to structure that data so the model learns to extract and manipulate the
  information correctly

Simply dumping structured data into training won't teach the model to reason about
it. Actively shape the data presentation to guide what the model learns.

In the following sections, there is literature review demonstrating the importance
of data augmentation and provide examples augmentation strategies for structured
business data that will give useful ideas on how to treat and organize business
dataset for CPT.

###### Structured data for CPT in the literature

CPT can pack domain facts into the model but often fails to make those facts
retrievable and manipulable when inputs or tasks shift. Controlled experiments show
that without diverse augmentation during pretraining, models memorize facts in
brittle ways that remain hard to extract even after later instruction tuning, and
they recommend injecting instruction like signals early in training. For semi
structured data, randomized serialization and other augmentations reduce schema
overfitting, which is why CPT should be interleaved with instruction style tasks
rather than run first and IFT later. Finance focused work further finds that jointly
mixing CPT and instruction data at batch time improves generalization and reduces
forgetting versus the sequential recipe. Qwen technical report converges on the same
pattern by integrating high quality instruction data into pretraining itself, which
boosts in context learning and preserves instruction following while acquiring new
domain knowledge.

Data augmentation for semi structured corpora is a key lever. Synthetic graph aware
CPT expands small domain sets into entity linked corpora that explicitly teach
relationships and compounds with retrieval at inference time. Joint CPT plus
instruction mixing outperforms sequential pipelines in finance and balancing domain
with general data lowers degradation on general skills. Very large scale domain CPT
can also retain broad ability and even allow trade offs through model merging, yet
still points to instruction tuning as an essential next step, reinforcing the value of
introducing instruction signals during CPT.

###### Injecting diversity through randomization and shuffling

A general strategy that helps to teach model effectively from the structured and
semi structured datasets is to shuffle the order of fields in the datasets, and even
randomly drop out some keys.

Shuffling the fields forces the model to read what each value means instead of
where it appears and learn the relationships between all the fields. For example, in
case of an video game posted on amazon store, when "Title," "Platform," "Price,"
"Condition," and "Edition" arrive in different permutations, the model can't rely on
"the third slot is platform"; it must bind labels to values and learn the bilateral
relationships among attributes: title ⇄ platform, platform ⇄ price, condition ⇄ price.
So it can, for example, infer a likely platform from a game name and an observed
price, or estimate a plausible price range given a title and platform.

Randomly dropping keys during serialization acts like feature dropout: it prevents
co-adaptation on any one field and forces the model to recover missing information
from the remaining evidence. If "Platform" is absent, the model must pick it up from
the title string or compatibility text; if "Price" is hidden, it has to triangulate
from platform, edition, and condition. This builds symmetry (A→B and B→A), robustness
to messy real-world listings, and schema invariance when fields are missing, renamed,
or reordered.

An shopping-style example makes it concrete. Serialize the same item multiple
ways—"Title: 'Elden Ring' | Platform: PlayStation 5 | Condition: Used—Like New |
Price: $34.99" and a permutation like "Price: $34.99 | Title: 'Elden Ring' |
Condition: Used—Like New | Platform: PlayStation 5"—and on some passes drop "Platform"
while leaving "Compatible with PS5" in the description. Train complementary objectives
such as predicting platform from {title, price} and predicting a price bucket from
{title, platform}. Because order and even presence of keys vary, the only stable
strategy is to learn the true relationships between attributes rather than memorize a
template.

### The way data is presented

matters

LLMs learn by predicting the next token from what they have already seen. So the
order of fields and events shown during training decides what the model can learn. If
the training format matches the real task, the loss lands on the exact decision
tokens. If fields are tossed together without structure, the model learns shortcuts or
memorizes popularity and then fails when asked to choose among options.

Show the situation first, then the options, then the decision. If the model should
also learn about outcomes or explanations, put them after the decision.

### Packing samples for CPT

###### What is packing?

It simply means to fill each sequence window in the training data with multiple
whole examples so the window is dense with real tokens, not padding.

###### Why it matters

During training a maximum context length is set, for example 8,192 tokens.
Batches are shaped to [batch size × context length]. If a training example is
shorter than the context length, the remaining positions are padded. Padding still
runs through attention and MLP kernels even if loss is masked, so compute is paid
for tokens that carry no learning signal.

###### How to do packing?

To pack multiple samples, concatenate multiple training samples with a `[DOC]` separator in between (note the space before and after the [DOC] )
such that the full length of the samples are under the desired context
length.

An example packed document would look like this:

```
{"text": "training sample 1 [DOC] training sample 2 [DOC] training sample 3"}
```

### CPT Tuning Parameters

The parameters that are available for fine-tuning with CPT include:

###### Run Configuration

- **name**: A descriptive name for your training job. This helps identify your job in the AWS Management Console.
- **model_type**: The Amazon Nova model variant to use. The available options are `amazon.nova-2-lite-v1:0:256k`.
- **model_name_or_path**: The path to the base model to use for your training. The available options are `nova-lite-2/prod`, or the S3 path for the post-training checkpoint (`s3://customer-escrow-bucket-unique_id/training_run_name`).
- **replicas**: The number of compute instances to use for distributed training. Available values vary based on the model you choose. Amazon Nova Lite 2.0 supports 4, 8, 16, or 32 replicas.
- **data_s3_path**: The S3 location of the training dataset, which is a JSONL file. This file must reside in the same AWS account and Region as the cluster. All of the S3 locations provided must be in the same account and Region.
- **validation_data_s3_path**: (Optional) The S3 location of the validation dataset, which is a JSONL file. This file must reside in the same account and region as the cluster. All of the S3 locations provided must be in the same account and Region.
- **output_s3_path**: The S3 location where the manifest and TensorBoard logs are stored. All of the S3 locations provided must be in the same AWS account and AWS Region.
- **mlflow_tracking_uri**: The ARN of the MLFlow App to use for MLFlow logging
- **mlflow_experiment_name**: MLFlow experiment name
- **mlflow_run_name**: MLFlow run name

###### Training Configuration

- **max_length**: The maximum sequence length in tokens. This determines the context window size for training. The maximum supported value are 8192 tokens for CPT.

Longer sequences will improve training efficiencies at the cost of increased memory requirements. We recommend that you match the max_length parameter to your data distribution.

- **global_batch_size**: The total number of training samples processed together in one forward or backward pass across all devices and workers.

This value multiplies the per-device batch size and number of devices. It affects the stability of training and throughput. We recommend that you start with a batch size that fits comfortably within your memory and scale up from there. For domain-specific data, larger batches might over-smooth gradients.

###### Trainer Settings

- **max_steps**: The number of training steps to run. Each step will train the model with `global_batch_size` no. of elements

###### Model Settings

- **hidden_dropout**: The probability of dropping hidden state outputs. Increase this value by approximately 0.0-0.2 to reduce overfitting on smaller datasets. Valid values are between 0-1, inclusive.
- **attention_dropout**: The probability of dropping attention weights. This parameter can help with generalization. Valid values are between 0-1, inclusive.

###### Optimizer Configuration

- **lr**: The learning rate, which controls the step size during optimization. We recommend values between 1e-6-1e-4 for good performance. Valid values are between 0-1, inclusive.
- **name**: The optimizer algorithm. Currently, only `distributed_fused_adam` is supported.
- **weight_decay**: The L2 regularization strength. Higher values (between 0.01-0.1) increase regularization.
- **warmup_steps**: The number of steps to gradually increase learning rate. This improves training stability. Valid values are between 1-20, inclusive.
- **min_lr**: The minimum learning rate at the end of decay. Valid values are between 0-1, inclusive, but must be less than learning rate.
