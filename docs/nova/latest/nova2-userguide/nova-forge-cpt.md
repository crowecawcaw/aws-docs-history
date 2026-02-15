# Continued Pre-Training and Mid-Training

###### Note

Detailed documentation is provided once subscribed

Nova Forge CPT offers advanced capabilities beyond standard CPT, including access to
intermediate checkpoints and data mixing with Nova's pre-training corpus. These features
enable more efficient domain adaptation and better preservation of the model's general
capabilities.

## What are intermediate checkpoints and

why are they needed?

Intermediate checkpoints are snapshots of the Amazon Nova model saved at different
stages of the pre-training, before the model reaches its final production-ready
state. During model development, Amazon Nova undergoes multiple training phases: initial
pre-training with constant learning rate, learning rate ramp-down, context extension
training, and finally instruction-following alignment and safety training. For CPT,
intermediate checkpoints are often preferable to the final Prod checkpoint because
they are more plastic and receptive to domain adaptation. The Prod checkpoint has
undergone extensive instruction-following alignment and safety training, which
optimizes the model for general conversational use but can make it resistant to
learning new domain-specific patterns during CPT. In contrast, Partially and Fully
pre-trained text only checkpoints retain the model's pre-training characteristics.
They haven't been heavily steered toward specific behaviors, making them more
efficient starting points for domain adaptation. When performing large-scale CPT
(>10B tokens), starting from intermediate checkpoints typically results in faster
convergence, better training stability, and more effective domain knowledge
acquisition. However, for small-scale CPT (<10B tokens), or when
instruction-following capabilities need to be preserved, the Prod checkpoint may be
more appropriate as it allows domain adaptation while maintaining the model's
conversational abilities.

Multiple intermediate checkpoints are necessary for CPT because they offer
different levels of model plasticity that affect how efficiently the model can
absorb new domain knowledge. The final Prod checkpoint has undergone extensive
instruction-following alignment and safety training, which optimizes it for general
conversational use but makes it resistant to learning new domain-specific patterns.
In other words, It has been hardened through post-training. In contrast, earlier
checkpoints retain the model's pre-training characteristics and haven't been heavily
steered toward specific behaviors, making them more plastic and receptive to domain
adaptation.

To achieve the best training efficiency, multiple intermediate checkpoints are
provided.

## What checkpoints are available?

###### Nova 2.0

There are three Amazon Nova Lite 2.0 checkpoints.

- PRE-TRAINED - [`nova-lite-2/pretraining-text-RD`]: This is the
  checkpoint after the constant learning rate and ramp-down stages of Amazon Nova
  pre-training where the model is trained on trillions of tokens.
- MID-TRAINED - [`nova-lite-2/pretraining-text-CE`]: This
  checkpoint allows intermediate volumes of unstructured data to be introduced
  with a more conservative learning rate than pre-training, absorbing
  domain-specific knowledge while avoiding catastrophic forgetting.
- POST-TRAINED - [`nova-lite-2/prod`]: This is the fully aligned final
  checkpoint of the model that has gone through all the pertaining and post
  training steps.

The following table elaborates on the different conditions for pre- and
mid-training.

| Data Type                                                                                                       | Perform                         | With Checkpoint |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------- | --------------- |
| Large-scale unstructured raw domain data (documents, logs,<br>articles, code, etc.)                             | Continued Pre-Training          | Pre-Trained     |
| Large-scale unstructured raw domain data (documents, logs,<br>articles, code, etc.)                             | Mid-Training                    | Pre-Trained     |
| Smaller volumes of unstructured raw data. Structured reasoning<br>traces / CoT data                             | Mid-Training                    | Mid-Trained     |
| Structured demonstrations (high-quality input-output pairs,<br>curated task instructions, multi-turn dialogues) | Full Fine-Tuning                | Mid-Trained     |
| Structured demonstrations (high-quality input-output pairs,<br>curated task instructions, multi-turn dialogues) | Parameter Efficient Fine-Tuning | Post-Trained    |

## Which checkpoint to use?

Partially pre-trained text only and fully pre-trained text only checkpoints
typically converge faster and require fewer training steps for domain adaptation.
However, they have no instruction tuning and would need to undergo post training
steps to be able to perform useful tasks and follow instructions. GA checkpoint may
require more steps to adapt but provides safer starting point for small-scale
experiments and will maintain some of it post training capabilities even after CPT
training.

In general, with large training datasets (>10B tokens), start from partially
pre-trained text only or fully pre-trained text only checkpoints for more efficient
and stable training, as the model's knowledge base will be substantially modified.
With small datasets (<10B tokens), use the GA checkpoint to preserve
instruction-following capabilities while adapting to the domain.

## How to use data mixing for Nova 2.0?

When performing CPT with a new domain data, it is highly beneficial to mix the new
data with some of the data used previously in the pre-training stage of the model.
Mixing old data with new domain data solves two problems:

- Forgetting control: Prevents catastrophic forgetting by preserving
  existing skills and knowledge of the model. Without data mixing, training
  exclusively on narrow domain data causes the model to overwrite general
  capabilities. For example, a model trained only on legal documents might
  lose its ability to code or do math. Mixing the general domain datasets
  preserves these general skills while acquiring the new domain.
- Optimization stability: Maintains training stability by anchoring the
  model's internal representations. During CPT, the model's learned features
  are modified and data mixing provides gradients from diverse sources that
  guide this adaptation smoothly. Without it, training on narrow distributions
  can cause gradient instability, where the model's representations shift too
  drastically, leading to training divergence, loss spikes, or collapse of
  existing capabilities. This is the stability-plasticity tradeoff: the model
  should be plastic enough to learn new domain knowledge, but stable enough
  not to break what it already knows.

###### Nova CPT Data Mixing Capabilities

Access to Amazon Nova pre-training data and checkpoints is one of the core
offerings of the Amazon Nova CPT customization. Amazon Nova CPT customization enables easy
mixing of domain data with Amazon Nova's pre-training corpus. Further, the sampling
ratio of the specific Amazon Nova data categories (e.g., code, math, reasoning, etc)
can be changed and their proportions controlled to complement domain data. This
allows reinforcement of capabilities that align with the use case while adapting
the model to the specific domain.

###### Finding the Optimal Mixing Ratio

The optimal ratio of Amazon Nova data versus domain data depends on the dataset's
domain, complexity, size, quality, and the importance of maintaining general
capabilities. This ratio must be discovered through experimentation. An
experiment framework to decide on how much Amazon Nova data to mix is as
follows.

Select a representative subset of domain data (e.g., 5B tokens) and keep this
constant across all experimental runs.

Run small-scale CPT experiments varying only the amount of Amazon Nova data mixed
in:

- No mixing: 100% domain → 5B domain only (total 5B)
- Light mixing: 90% domain → 5B domain + ~0.56B Amazon Nova (total ~5.56B)
- Medium mixing: 70% domain → 5B domain + ~2.14B Amazon Nova (total
  ~7.14B)
- Heavy mixing: 50% domain → 5B domain + 5B Amazon Nova (total 10B)

Evaluate each checkpoint on in domain and general domain benchmarks. Also evaluate
the starting checkpoint (Amazon Nova checkpoint before any training).

- Does customer-domain performance stay roughly constant across runs? It
  usually should, since each run saw the same number of domain tokens. If
  domain performance improves with more mixing, Amazon Nova data provides useful
  regularization.
- Do general benchmark scores improve as mixing is increased?
  - Expected behavior is that the general capabilities should improve
    monotonically as more Amazon Nova data is added.
  - Measure multiple general benchmarks: MMLU (general knowledge),
    HumanEval (coding), GSM8K (math), or specific benchmarks of
    interest.

- Select the mixing ratio that maintains domain performance while delivering
  acceptable general capabilities for the use cases. Factor in the additional
  cost of training with more data mixing.

Once the optimal mixing ratio has been identified, run full-scale CPT using the
complete domain dataset with the selected mixing ratio.

## Dissecting the Data Mixing Categories

Below we dissect each available category in Data Mixing, for you to make best decision of what data categories makes most sense to be represented in your overall data mixture.

### How to Enable Data Mixing

Add the `data_mixing` section to your recipe with the appropriate percentage distribution across dataset categories. The `nova_data` percentages must sum to 100.

#### Nova 2.0 Configuration with data mixing

```

# Note:
# This recipe can run on p5.48xlarge

# Run config
display_name: "Nova Lite Pretrain on P5 GPU"
versions: ["2.0"]
instance_types: ["ml.p5.48xlarge"]

run:
  name: "my-cpt-run"     # A descriptive name for your training job
  model_type: "amazon.nova-2-lite-v1:0:256k" # Model variant specification, do not change
  model_name_or_path: "nova-lite-2/prod" # Base model path, do not change
  replicas: 8       # Number of compute instances for training, allowed values are 4, 8, 16, 32
  data_s3_path: ""       # Customer data paths
  validation_data_s3_path: ""        # Customer validation data paths
  output_s3_path: ""   # Output artifact path, Sagemaker Hyperpod job-specific configuration - not compatible with standard Sagemaker Training jobs

## Training specific configs
training_config:
  task_type: cpt
  max_length: 8192              # Maximum context window size (tokens)
  global_batch_size: 64        # Global batch size, allowed values are 32, 64, 128, 256.

  trainer:
    max_steps: 10               # The number of training steps to run total
    val_check_interval: 10      # The number of steps between running validation
    limit_val_batches: 2        # Batches of the validation set to use each trigger

  model:
    hidden_dropout: 0.0           # Dropout for hidden states, must be between 0.0 and 1.0
    attention_dropout: 0.0        # Dropout for attention weights, must be between 0.0 and 1.0

  optim:
    optimizer: adam
    lr: 1e-5                      # Learning rate
    name: distributed_fused_adam  # Optimizer algorithm, do not change
    adam_w_mode: true             # Enable AdamW mode
    eps: 1e-06                    # Epsilon for numerical stability
    weight_decay: 0.0             # L2 regularization strength, must be between 0.0 and 1.0
    adam_beta1: 0.9               # Beta1 for Adam optimizer
    adam_beta2: 0.95              # Beta2 for Adam optimizer
    sched:
      warmup_steps: 10            # Learning rate warmup steps
      constant_steps: 0           # Steps at constant learning rate
      min_lr: 1e-6                # Minimum learning rate, must be lower than lr

data_mixing:
  dataset_catalog: cpt_text_lite
  sources:
    nova_data:   # percent inputs for Nova data must sum to 100%; use 0% if you want to exclude a data grouping
      agents: 20
      business-and-finance: 4
      scientific: 10
      code: 5
      factual-and-news: 5
      longform-text: 6
      health-and-medicine: 1
      humanities-and-education: 1
      legal: 1
      math: 9
      additional-languages: 15
      social-and-personal-interest: 11
      entertainment: 0.5
      reasoning: 10
      other: 0.5
      tables: 1
    customer_data: # percent input of customer data. 100 = use only customer data, 0 = use only the nova_data mix above
      percent: 25

```

**What do these categories mean**

**Note**: Nova 2.0 includes additional reasoning-specific categories (e.g., `reasoning-code`, `reasoning-math`, `reasoning-instruction-following`) that are not available in Nova 1.0.

Summary of Categories and Info Labels:

| Category Name                     | Info detail                                                                                                                         |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `agents`                          | Training data focused on autonomous decision-making, task completion, and goal-oriented behavior in AI systems                      |
| `baseline`                        | Fundamental language data focused on general comprehension, basic communication, and core linguistic capabilities                   |
| `chat`                            | Conversational exchanges demonstrating natural dialogue flow, context maintenance, and appropriate social interactions              |
| `code`                            | Programming source code, documentation, and technical discussions from various programming languages and platforms.                 |
| `factuality`                      | Reference materials and verified information focused on accuracy, source validation, and truth assessment                           |
| `identity`                        | Personality frameworks and behavioral patterns focused on consistent character traits, values, and interaction styles               |
| `long-context`                    | Extended texts and complex narratives focused on maintaining coherence and relevance across lengthy exchanges                       |
| `math`                            | Mathematical content including textbooks, problems, solutions, and mathematical discussions.                                        |
| `rai`                             | Cases and scenarios emphasizing ethical AI principles, safety considerations, and responsible technology deployment                 |
| `instruction-following`           | Examples of precise task execution based on varying levels of user prompts and directives                                           |
| `stem`                            | Technical content covering science, technology, engineering, and mathematics, including problem-solving and theoretical concepts    |
| `planning`                        | Sequences demonstrating strategic thinking, step-by-step task breakdown, and efficient resource allocation                          |
| `reasoning-chat`                  | Analytical dialogue scenarios focused on logical discussion and structured conversation flows                                       |
| `reasoning-code`                  | Programming challenges and algorithmic problems focused on systematic solution development                                          |
| `reasoning-factuality`            | Information evaluation scenarios focused on critical assessment and verification processes                                          |
| `reasoning-instruction-following` | Complex task analysis focused on systematic interpretation and methodical execution                                                 |
| `reasoning-math`                  | Mathematical problem-solving scenarios focused on logical progression and solution strategies                                       |
| `reasoning-planning`              | Strategic decision-making scenarios focused on systematic approach to goal achievement                                              |
| `reasoning-rag`                   | Information retrieval and synthesis scenarios focused on contextual understanding and relevant application                          |
| `reasoning-rai`                   | Ethical decision-making scenarios focused on systematic evaluation of AI safety and fairness                                        |
| `reasoning-stem`                  | Scientific problem-solving scenarios focused on methodical analysis and solution development                                        |
| `rag`                             | Examples of effectively combining retrieved external knowledge with generated responses to provide accurate, contextual information |
| `translation`                     | Multi-language content pairs showing accurate translation while preserving context, tone, and cultural nuances                      |

#### Parameter Guide

- **dataset_catalog:** The only value is cpt_text_lite for now, until we enable the multimodal training.
- **nova_data:** Percentage of the individual categories of Nova data when mixed in. They should add up to 1.0.
- **customer_data**: the percentage of customer's data mixed into the Nova data.

The total number of tokens used in training can be calculated from `max_length` \* `global_batch_size` \* `max_steps`

###### Limitations

Current CPT only supports text data and does not support any customer multi-modal
datasets.
