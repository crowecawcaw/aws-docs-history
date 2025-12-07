# Understanding the recipe

parameters

###### Run configuration

The following is a general run configuration and an explanation of the parameters
involved.

```
run:
  name: eval_job_name
  model_type: amazon.nova-micro-v1:0:128k
  model_name_or_path: nova-micro/prod
  replicas: 1
  data_s3_path: ""
  output_s3_path: s3://output_path
```

- `name`: (Required) A descriptive name for your evaluation job. This helps
  identify your job in the AWS console.
- `model_type`: (Required) Specifies the Amazon Nova model variant to use. Do
  not manually modify this field. Options include:
  - `amazon.nova-micro-v1:0:128k`
  - `amazon.nova-lite-v1:0:300k`
  - `amazon.nova-pro-v1:0:300k`

- `model_name_or_path`: (Required) The path to the base model or S3 path
  for the post-trained checkpoint. Options include:
  - `nova-micro/prod`
  - `nova-lite/prod`
  - `nova-pro/prod`
  - (S3 path for the post-trained checkpoint) `s3://<escrow
bucket>/<job id>/outputs/checkpoints`

- `replicas`: (Required) The number of compute instances to use for
  distributed training. You must set this value to 1 because multi-node is not
  supported.
- `data_s3_path`: (Required) The S3 path to the input dataset. Leave this
  parameter empty unless you are using the _bring your own dataset_ or
  _LLM as a judge_ recipe.
- `output_s3_path`: (Required) The S3 path to store output evaluation
  artifacts. Note that the output S3 bucket must be created by the same account that is
  creating the job.
- `mlflow_tracking_uri`: (Optional) MLflow tracking server ARN for tracking MLFlow runs/experiments. Please ensure you have permission to access the tracking server from SageMaker AI execution role

###### Evaluation configuration

The following is a model evaluation configuration and an explanation of the parameters
involved.

```
evaluation:
  task: mmlu
  strategy: zs_cot
  subtask: mathematics
  metric: accuracy
```

- `task`: (Required) Specifies the evaluation benchmark or task to
  use.

Supported task list:

    + mmlu
    + mmlu\_pro
    + bbh
    + gpqa
    + math
    + strong\_reject
    + gen\_qa
    + ifeval
    + mmmu
    + llm\_judge
    + humaneval
    + mm\_llm\_judge

- `strategy`: (Required) Defines the evaluation approach:
  - zs_cot: Zero-shot Chain-of-Thought - An approach to prompt large language models
    that encourages step-by-step reasoning without requiring explicit examples.
  - zs: Zero-shot - An approach to solve a problem without any prior training
    examples.
  - gen_qa: A strategy specific for bring your own dataset recipes.
  - judge: A strategy specific for Amazon Nova LLM as Judge and mm_llm_judge.

- `subtask`: (Optional and Removable) Specifies a specific subtask for
  certain evaluation tasks. Remove this from your recipe if your task does not have any
  subtasks.
- `metric`: (Required) The evaluation metric to use.
  - accuracy: Percentage of correct answers
  - exact_match: (For `math` benchmark), returns the rate at which the
    input predicted strings exactly match their references.
  - deflection: (For `strong reject` benchmark), returns the relative
    deflection to the base model and the difference in significance metrics.
  - pass@1: (For `humaneval` benchmark) is a metric used to measures the
    percentage of cases where the model's highest confidence prediction matches the
    correct answer.
  - `all`: Returns the following metrics:
    - For `gen_qa` and bring your own dataset benchmark, return
      following metrics:
      - `rouge1`: Measures the overlap of unigrams (single words)
        between generated and reference text.
      - `rouge2`: Measures the overlap of bigrams (two consecutive
        words) between generated and reference text.
      - `rougeL`: Measures the longest common subsequence between
        texts, allowing for gaps in the matching.
      - `exact_match`: Binary score (0 or 1) indicating if the
        generated text matches the reference text exactly, character by
        character.
      - `quasi_exact_match`: Similar to exact match but more lenient,
        typically ignoring case, punctuation, and white space differences.
      - `f1_score`: Harmonic mean of precision and recall, measuring
        word overlap between predicted and reference answers.
      - `f1_score_quasi`: Similar to f1_score but with more lenient
        matching, using normalized text comparison that ignores minor
        differences.
      - `bleu`: Measures precision of n-gram matches between
        generated and reference text, commonly used in translation
        evaluation.

    - For `llm_judge` and `mm_llm_judge`, bring your own
      dataset benchmark, return following metrics:
      - `a_scores`: Number of wins for `response_A` across
        forward and backward evaluation passes.
      - `a_scores_stderr`: Standard error of `response_A
scores` across pairwise judgements.
      - `b_scores`: Number of wins for `response_B` across
        forward and backward evaluation passes.
      - `b_scores_stderr`: Standard error of `response_B
scores` across pairwise judgements.
      - `ties`: Number of judgements where `response_A`
        and `response_B` are evaluated as equal.
      - `ties_stderr`: Standard error of ties across pairwise
        judgements.
      - `inference_error`: Count of judgements that could not be
        properly evaluated.
      - `inference_error_stderr`: Standard error of inference errors
        across judgements.
      - `score`: Aggregate score based on wins from both forward and
        backward passes for `response_B`.
      - `score_stderr`: Standard error of the aggregate score across
        pairwise judgements.
      - `winrate`: the probability that response_B will be preferred
        over response_A calculated using Bradley-Terry probability.
      - `lower_rate`: Lower bound (2.5th percentile) of the estimated
        win rate from bootstrap sampling.

###### Inference configuration

The following is an inference configuration and an explanation of the parameters
involved. All parameters are optional.

```
inference:
  max_new_tokens: 200
  top_k: -1
  top_p: 1.0
  temperature: 0
  top_logprobs: 10
```

- `max_new_tokens`: The maximum number of tokens to generate. This must be
  an integer.
- `top_k`: The number of highest probability tokens to consider. This must
  be an integer.
- `top_p`: The cumulative probability threshold for token sampling. This
  must be a float between 0.0 and 1.0, inclusive.
- `temperature`: Randomness in token selection. Larger values introduce
  more randomness. Use 0 to make the results deterministic. This value must be a float
  with a minimum value of 0.
- `top_logprobs`: The number of top logprobs to be returned in the
  inference response. This value must be an integer from 0 to 20. Logprobs contain the
  considered output tokens and log probabilities of each output token returned in the
  message content.
  Note that for `humaneval`, we recommend the following inference
  configuration:

```
inference:
  top_k: 1
  max_new_tokens: 1600
  temperature: 0.0
```

###### MLFlow configuration

The following is an MLFlow configuration and an explanation of the parameters involved. All parameters are optional.

```
mlflow:
  experiment_name: "" # It organizes and group related ML runs
  run_name: "" # It is the identifier for a specific execution or training iteration within an experiment
```

- `experiment_name`: An experiment groups together runs and models for a specific task.
- `run_name`: Represent the training iteration within an experiment
