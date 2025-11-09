# Evaluating your trained model

An evaluation recipe is a YAML configuration file that defines how your Amazon Nova model
evaluation job is executed. With this recipe, you can assess the performance of a base or
trained model against common benchmarks or your own custom datasets. Metrics can be stored
in Amazon S3 or TensorBoard. The evaluation provides quantitative metrics that help you assess
model performance across various tasks to determine if further customization is
needed.

Model evaluation is an offline process, where models are tested against fixed benchmarks
with predefined answers. They are not assessed in real-time or against live user
interactions. For real-time evaluations, you can evaluate the model after it is deployed to
Amazon Bedrock by calling the Amazon Bedrock runtime APIs.

###### Topics

- [Available benchmark
  tasks](#customize-fine-tune-evaluate-available-tasks "#customize-fine-tune-evaluate-available-tasks")
- [Understanding the
  recipe parameters](#customize-fine-tune-evaluate-understand-modify "#customize-fine-tune-evaluate-understand-modify")
- [Evaluation recipe
  examples](#customize-fine-tune-evaluate-recipe-examples "#customize-fine-tune-evaluate-recipe-examples")
- [Starting an evaluation
  job](#customize-fine-tune-evaluate-start-job "#customize-fine-tune-evaluate-start-job")
- [Accessing and analyzing
  evaluation results](#customize-fine-tune-evaluate-access-results "#customize-fine-tune-evaluate-access-results")

## Available benchmark

tasks

A sample code package is available that demonstrates how to calculate benchmark metrics using the SageMaker AI model evaluation feature for Amazon Nova. To access the code packages, see [sample-Nova-lighteval-custom-task](https://github.com/aws-samples/sample-Nova-lighteval-custom-task/ "https://github.com/aws-samples/sample-Nova-lighteval-custom-task/").

Here is a list of the supported, available industry standard benchmarks. You can specify
the following benchmarks in the `eval_task` parameter:

| Benchmark     | Modality            | Description                                                                                                                                                                                                          | Metrics     | Strategy | Subtask Available |
| ------------- | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------- | ----------------- |
| mmlu          | Text                | Multi-task Language Understanding – Tests knowledge across 57<br>subjects.                                                                                                                                           | accuracy    | zs_cot   | Yes               |
| mmlu_pro      | Text                | MMLU – Professional Subset – Focuses on professional domains such as<br>law, medicine, accounting, and engineering.                                                                                                  | accuracy    | zs_cot   | No                |
| bbh           | Text                | Advanced Reasoning Tasks – A collection of challenging problems that<br>test higher-level cognitive and problem-solving skills.                                                                                      | accuracy    | zs_cot   | Yes               |
| gpqa          | Text                | General Physics Question Answering – Assesses comprehension of physics<br>concepts and related problem-solving abilities.                                                                                            | accuracy    | zs_cot   | No                |
| math          | Text                | Mathematical Problem Solving – Measures mathematical reasoning across<br>topics including algebra, calculus, and word problems.                                                                                      | exact_match | zs_cot   | Yes               |
| strong_reject | Text                | Quality-Control Task – Tests the model’s ability to detect and reject<br>inappropriate, harmful, or incorrect content.                                                                                               | deflection  | zs       | Yes               |
| IFEval        | Text                | Instruction-Following Evaluation – Gauges how accurately a model<br>follows given instructions and completes tasks to<br>specification.                                                                              | accuracy    | zs       | No                |
| gen_qa        | Text                | Custom Dataset Evaluation – Lets you bring your own dataset for<br>benchmarking, comparing model outputs to reference answers with metrics<br>such as ROUGE and BLEU.                                                | all         | gen_qa   | No                |
| mmmu          | Multi-modal         | Massive Multidiscipline Multimodal Understanding (MMMU) –<br>College-level benchmark comprising multiple-choice and open-ended<br>questions from 30 disciplines.                                                     | accuracy    | zs_cot   | Yes               |
| llm_judge     | Text                | LLM-as-a-Judge Preference Comparison – Uses a Nova Judge model to<br>determine preference between paired responses (B compared with A) for your prompts,<br>calculating the probability of B being preferred over A. | all         | judge    | No                |
| humaneval     | Text                | HumanEval<br>• A benchmark dataset designed to evaluate the code<br>generation capabilities of large language models                                                                                                 | pass@1      | zs       | No                |
| mm_llm_judge  | Multi-modal (image) | This new benchmark behaves the same as the text-based `llm_judge` above.<br>The only difference is that it supports image inference.                                                                                 | all         | judge    | No                |

The following `mmlu` subtasks are available:

```
`MMLU_SUBTASKS = [
 "abstract_algebra",
 "anatomy",
 "astronomy",
 "business_ethics",
 "clinical_knowledge",
 "college_biology",
 "college_chemistry",
 "college_computer_science",
 "college_mathematics",
 "college_medicine",
 "college_physics",
 "computer_security",
 "conceptual_physics",
 "econometrics",
 "electrical_engineering",
 "elementary_mathematics",
 "formal_logic",
 "global_facts",
 "high_school_biology",
 "high_school_chemistry",
 "high_school_computer_science",
 "high_school_european_history",
 "high_school_geography",
 "high_school_government_and_politics",
 "high_school_macroeconomics",
 "high_school_mathematics",
 "high_school_microeconomics",
 "high_school_physics",
 "high_school_psychology",
 "high_school_statistics",
 "high_school_us_history",
 "high_school_world_history",
 "human_aging",
 "human_sexuality",
 "international_law",
 "jurisprudence",
 "logical_fallacies",
 "machine_learning",
 "management",
 "marketing",
 "medical_genetics",
 "miscellaneous",
 "moral_disputes",
 "moral_scenarios",
 "nutrition",
 "philosophy",
 "prehistory",
 "professional_accounting",
 "professional_law",
 "professional_medicine",
 "professional_psychology",
 "public_relations",
 "security_studies",
 "sociology",
 "us_foreign_policy",
 "virology",
 "world_religions"
]`
```

The following `bbh` subtasks are available:

```
`BBH_SUBTASKS = [
 "boolean_expressions",
 "causal_judgement",
 "date_understanding",
 "disambiguation_qa",
 "dyck_languages",
 "formal_fallacies",
 "geometric_shapes",
 "hyperbaton",
 "logical_deduction_five_objects",
 "logical_deduction_seven_objects",
 "logical_deduction_three_objects",
 "movie_recommendation",
 "multistep_arithmetic_two",
 "navigate",
 "object_counting",
 "penguins_in_a_table",
 "reasoning_about_colored_objects",
 "ruin_names",
 "salient_translation_error_detection",
 "snarks",
 "sports_understanding",
 "temporal_sequences",
 "tracking_shuffled_objects_five_objects",
 "tracking_shuffled_objects_seven_objects",
 "tracking_shuffled_objects_three_objects",
 "web_of_lies",
 "word_sorting"
]`
```

The following `math` subtasks are available:

```
`MATH_SUBTASKS = [
 "algebra",
 "counting_and_probability",
 "geometry",
 "intermediate_algebra",
 "number_theory",
 "prealgebra",
 "precalculus",
]`
```

## Understanding the

recipe parameters

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

- `name`: (Required) A descriptive name for your evaluation job. This
  helps identify your job in the AWS console.
- `model_type`: (Required) Specifies the Amazon Nova model variant to
  use. Do not manually modify this field. Options include:
  - `amazon.nova-micro-v1:0:128k`
  - `amazon.nova-lite-v1:0:300k`
  - `amazon.nova-pro-v1:0:300k`

- `model_name_or_path`: (Required) The path to the base model or S3
  path for the post-trained checkpoint. Options include:
  - `nova-micro/prod`
  - `nova-lite/prod`
  - `nova-pro/prod`
  - (S3 path for the post-trained checkpoint)
    `s3://<escrow bucket>/<job id>/outputs/checkpoints`

- `replicas`: (Required) The number of compute instances to use for
  distributed training. You must set this value to 1 because multi-node is not
  supported.
- `data_s3_path`: (Required) The S3 path to the input dataset. Leave
  this parameter empty unless you are using the _bring your own
  dataset_ or _LLM as a judge_ recipe.
- `output_s3_path`: (Required) The S3 path to store output evaluation
  artifacts. Note that the output S3 bucket must be created by the same account
  that is creating the job.

###### Evaluation configuration

The following is a model evaluation configuration and an explanation of the
parameters involved.

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
  - zs_cot: Zero-shot Chain-of-Thought - An approach to prompt large
    language models that encourages step-by-step reasoning without requiring
    explicit examples.
  - zs: Zero-shot - An approach to solve a problem without any prior
    training examples.
  - gen_qa: A strategy specific for bring your own dataset recipes.
  - judge: A strategy specific for Amazon Nova LLM as Judge and
    mm_llm_judge.

- `subtask`: (Optional and Removable) Specifies a specific subtask
  for certain evaluation tasks. Remove this from your recipe if your task does not
  have any subtasks.
- `metric`: (Required) The evaluation metric to use.
  - accuracy: Percentage of correct answers
  - exact_match: (For `math` benchmark), returns the rate at
    which the input predicted strings exactly match their references.
  - deflection: (For `strong reject` benchmark), returns the
    relative deflection to the base model and the difference in significance
    metrics.
  - pass@1: (For `humaneval` benchmark) is a metric used to
    measures the percentage of cases where the model's highest confidence
    prediction matches the correct answer.
  - `all`: Returns the following metrics:
    - For `gen_qa` and bring your own dataset benchmark,
      return following metrics:
      - `rouge1`: Measures the overlap of unigrams
        (single words) between generated and reference
        text.
      - `rouge2`: Measures the overlap of bigrams
        (two consecutive words) between generated and reference
        text.
      - `rougeL`: Measures the longest common
        subsequence between texts, allowing for gaps in the
        matching.
      - `exact_match`: Binary score (0 or 1)
        indicating if the generated text matches the reference
        text exactly, character by character.
      - `quasi_exact_match`: Similar to exact match
        but more lenient, typically ignoring case, punctuation,
        and white space differences.
      - `f1_score`: Harmonic mean of precision and
        recall, measuring word overlap between predicted and
        reference answers.
      - `f1_score_quasi`: Similar to f1_score but
        with more lenient matching, using normalized text
        comparison that ignores minor differences.
      - `bleu`: Measures precision of n-gram
        matches between generated and reference text, commonly
        used in translation evaluation.

    - For `llm_judge` and `mm_llm_judge`, bring your own
      dataset benchmark, return following metrics:
      - `a_scores`: Number of wins for
        `response_A` across forward and backward
        evaluation passes.
      - `a_scores_stderr`: Standard error of
        `response_A scores` across pairwise
        judgements.
      - `b_scores`: Number of wins for
        `response_B` across forward and backward
        evaluation passes.
      - `b_scores_stderr`: Standard error of
        `response_B scores` across pairwise
        judgements.
      - `ties`: Number of judgements where
        `response_A` and `response_B`
        are evaluated as equal.
      - `ties_stderr`: Standard error of ties
        across pairwise judgements.
      - `inference_error`: Count of judgements that
        could not be properly evaluated.
      - `inference_error_stderr`: Standard error of
        inference errors across judgements.
      - `score`: Aggregate score based on wins from
        both forward and backward passes for
        `response_B`.
      - `score_stderr`: Standard error of the
        aggregate score across pairwise judgements.
      - `winrate`: the probability that response_B
        will be preferred over response_A calculated using
        Bradley-Terry probability.
      - `lower_rate`: Lower bound (2.5th
        percentile) of the estimated win rate from bootstrap
        sampling.

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

- `max_new_tokens`: The maximum number of tokens to generate. This
  must be an integer.
- `top_k`: The number of highest probability tokens to consider. This
  must be an integer.
- `top_p`: The cumulative probability threshold for token sampling.
  This must be a float between 0.0 and 1.0, inclusive.
- `temperature`: Randomness in token selection. Larger values
  introduce more randomness. Use 0 to make the results deterministic. This value
  must be a float with a minimum value of 0.
- `top_logprobs`: The number of top logprobs to be returned in the
  inference response. This value must be an integer from 0 to 20. Logprobs
  contain the considered output tokens and log probabilities of each output
  token returned in the message content.

Note that for `humaneval`, we recommend the following inference
configuration:

```
inference:
  top_k: 1
  max_new_tokens: 1600
  temperature: 0.0
```

## Evaluation recipe

examples

Amazon Nova provides four types of evaluation recipes, which are available in the HyperPod recipes GitHub repository.

These recipes enable you to evaluate the fundamental capabilities of Amazon Nova models
across a comprehensive suite of text-only benchmarks. They are provided in the format
`xxx_general_text_benchmark_eval.yaml`.

These recipes enable you to evaluate the fundamental capabilities of Amazon Nova models
across a comprehensive suite of multi-modality benchmarks. They are provided in the
format `xxx_general_multi_modal_benchmark_eval.yaml`.

These recipes enable you to bring your own dataset for benchmarking and compare
model outputs to reference answers using different types of metrics. They are
provided in the format `xxx_bring_your_own_dataset_eval.yaml`.

The following are the bring your own dataset requirements:

- File format requirements
  - You must include a single `gen_qa.jsonl` file containing
    evaluation examples.
  - Your dataset must be uploaded to an S3 location where SageMaker AI training
    job can access it.
  - The file must follow the required schema format for a general Q&A
    dataset.

- Schema format requirements - Each line in the JSONL file must be a JSON object
  with the following fields:

      + `query`: (Required) String containing the question or
       instruction that needs an answer
      + `response`: (Required) String containing the expected model
       output
      + `system`: (Optional) String containing the system prompt
       that sets the behavior, role, or personality of the AI model before it
       processes the query
      + `metadata`: (Optional) String containing metadata
       associated with the entry for tagging purposes.

  Here is a bring your own data set example entry

```
`{
 "system":"You are a english major with top marks in class who likes to give minimal word responses: ",
 "query":"What is the symbol that ends the sentence as a question",
 "response":"?"
}
{
 "system":"You are a pattern analysis specialist that provides succinct answers: ",
 "query":"What is the next number in this series? 1, 2, 4, 8, 16, ?",
 "response":"32"
}
{
 "system":"You have great attention to detail that follows instructions accurately: ",
 "query":"Repeat only the last two words of the following: I ate a hamburger today and it was kind of dry",
 "response":"of dry"
}`
```

To use your custom dataset, modify your evaluation recipe with the following required
fields, do not change any of the content:

```
`evaluation:
 task: gen_qa
 strategy: gen_qa
 metric: all`
```

The following limitations apply:

- Only one JSONL file is allowed per evaluation.
- The file must strictly follow the defined schema.
- Context length limit: For each sample in the dataset, the context length
  (including system + query prompts) should be less than 3.5k.

Amazon Nova LLM as a Judge is a model evaluation feature that enables customers to
compare the quality of responses from one model to a baseline model response on a
custom dataset. It takes in a dataset with prompts, baseline responses, and
challenger responses, and uses a Nova Judge model to provide a winrate metric based
on [Bradley-Terry probability](https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model "https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model") with pairwise comparisons.

The recipes are provided in the format `xxx_llm_judge_eval.yaml`.

The following are the LLM as a Judge requirements:

- File format requirements
  - Include a single `llm_judge.jsonl` file containing
    evaluation examples. The file name must be
    `llm_judge.jsonl`.
  - Your dataset must be uploaded to an S3 location that [SageMaker AI HyperPod RIG](nova-hp-cluster.md "nova-hp-cluster.md") can access.
  - The file must follow the required schema format for the
    `llm_judge.jsonl` dataset.
  - The input dataset should ensure all records are under 12k context
    length.

- Schema format requirements - Each line in the JSONL file must be a JSON object
  with the following fields:

      + `prompt`: (Required) A string containing the prompt for the
       generated response.
      + `response_A`: A string containing the baseline
       response.
      + `response_B`: A string containing the alternative response
       be compared with baseline response.

  Here is an LLM as a judge example entry

```
`{
"prompt": "What is the most effective way to combat climate change?",
"response_A": "The most effective way to combat climate change is through a combination of transitioning to renewable energy sources and implementing strict carbon pricing policies. This creates economic incentives for businesses to reduce emissions while promoting clean energy adoption.",
"response_B": "We should focus on renewable energy. Solar and wind power are good. People should drive electric cars. Companies need to pollute less."
}
{
"prompt": "Explain how a computer's CPU works",
"response_A": "CPU is like brain of computer. It does math and makes computer work fast. Has lots of tiny parts inside.",
"response_B": "A CPU (Central Processing Unit) functions through a fetch-execute cycle, where instructions are retrieved from memory, decoded, and executed through its arithmetic logic unit (ALU). It coordinates with cache memory and registers to process data efficiently using binary operations."
}
{
"prompt": "How does photosynthesis work?",
"response_A": "Plants do photosynthesis to make food. They use sunlight and water. It happens in leaves.",
"response_B": "Photosynthesis is a complex biochemical process where plants convert light energy into chemical energy. They utilize chlorophyll to absorb sunlight, combining CO2 and water to produce glucose and oxygen through a series of chemical reactions in chloroplasts."
}`
```

To use your custom dataset, modify your evaluation recipe with the following required
fields, don't change any of the content:

```
`evaluation:
 task: llm_judge
 strategy: judge
 metric: all`
```

The following limitations apply:

- Only one JSONL file is allowed per evaluation.
- The file must strictly follow the defined schema.
- Amazon Nova Judge models are the same across all model family specifications (that
  is, Lite, Micro, and Pro).
- Custom judge models are not supported at this time.
- Context length limit: For each sample in the dataset, the context length
  (including system + query prompts) should be less than 7k.

Nova LLM Judge for multi-modal (image), short for Nova MM_LLM Judge, is a model
evaluation feature that enables you to compare the quality of responses from
one model against a baseline model's responses using a custom dataset. It
accepts a dataset containing prompts, baseline responses, and challenger
responses, and images in the form of Base64-encoded string, then uses a Nova
Judge model to provide a win rate metric based on [Bradley-Terry](https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model "https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model") probability through pairwise comparisons. Recipe
format: `xxx_mm_llm_judge _eval.yaml`.

**Nova LLM dataset requirements**

File format:

- Single `mm_llm_judge.jsonl` file containing
  evaluation examples. The file name must be exactly
  `llm_judge.jsonl`.
- Your must upload your dataset to an S3 location where SageMaker
  training jobs can access it.
- The file must follow the required schema format for the
  `mm_llm_judge` dataset.
- The input dataset should ensure all records are under 12 k
  context length, excluding the image's attribute.
  Schema format - Each line in the `.jsonl` file must be a JSON
  object with the following fields.

- Required fields.

`prompt`: String containing the prompt for the
generated response.

`images`: Array containing a list of objects with data
attributes (values are Base64-encoded image strings).

`response_A`: String containing the baseline
response.

`response_B`: String containing the alternative response be
compared with baseline response.
Example entry

For readability, the following example includes new lines and
indentation, but in the actual dataset, each record should be on a
single line.

```
{
  "prompt": "what is in the image?",
  "images": [
    {
      "data": "data:image/jpeg;Base64,/9j/2wBDAAQDAwQDAwQEAwQFBAQFBgo..."
    }
  ],
  "response_A": "a dog.",
  "response_B": "a cat.",
}
{
  "prompt": "how many animals in echo of the images?",
  "images": [
    {
      "data": "data:image/jpeg;Base64,/9j/2wBDAAQDAwQDAwQEAwQFBAQFBgo..."
    },
    {
      "data": "data:image/jpeg;Base64,/DKEafe3gihn..."
    }
  ],
  "response_A": "The first image contains one cat and the second image contains one dog",
  "response_B": "The first image has one aminal and the second has one animal",
}
```

To use your custom dataset, modify your evaluation recipe with the following
required fields, don't change any of the content:

```
evaluation:
  task: mm_llm_judge
  strategy: judge
  metric: all
```

**Limitations**

- Only one `.jsonl` file is allowed per evaluation.
- The file must strictly follow the defined schema.
- Nova MM Judge models only support image reference.
- Nova MM Judge models are the same across Amazon Nova Micro, Amazon Nova Lite, and Amazon Nova Pro
  specifications.
- Custom judge models are not currently supported.
- Amazon S3 image URI is not supported.
- The input dataset should ensure all records are under 12 k context length, excluding images attribute.

## Starting an evaluation

job

The following provides a suggested evaluation instance type and model type
configuration:

```
# Install Dependencies (Helm - https://helm.sh/docs/intro/install/)
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
rm -f ./get_helm.sh

# Install the HyperPod CLI
git clone --recurse-submodules https://github.com/aws/sagemaker-hyperpod-cli.git
git checkout -b release_v2
cd sagemaker-hyperpod-cli
pip install .

# Verify the installation
hyperpod --help

# Connect to a HyperPod Cluster
hyperpod connect-cluster --cluster-name `cluster-name`


# Submit the Job using the recipe for eval
# Namespace by default should be kubeflow
hyperpod start-job [--namespace `namespace`] --recipe evaluation/nova/nova_micro_p5_48xl_general_text_benchmark_eval --override-parameters \
'{
    "instance_type":"p5d.48xlarge",
    "container": "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-latest",
    "recipes.run.name": `custom-run-name`,
    "recipes.run.model_type": `model_type`,
    "recipes.run.model_name_or_path" " `model name or finetune checkpoint s3uri`,
    "recipes.run.data_s3_path": `s3 for input data only for genqa and llm_judge, must be full S3 path that include filename`,
}'

# List jobs
hyperpod list-jobs [--namespace `namespace`] [--all-namespaces]

# Getting Job details
hyperpod get-job --job-name `job-name` [--namespace `namespace`] [--verbose]

# Listing Pods
hyperpod list-pods --job-name `job-name` --namespace `namespace`

# Cancel Job
hyperpod cancel-job --job-name `job-name` [--namespace `namespace`]
```

You should also be able to view the job status through Amazon EKS cluster console.

## Accessing and analyzing

evaluation results

After your evaluation job completes successfully, you can access and analyze the
results using the information in this section. Based on the `output_s3_path`
(such as `s3://output_path/`) defined in the recipe, the output structure is
the following:

```
job_name/
├── eval-result/
│    └── results_[timestamp].json
│    └── inference_output.jsonl (only present for gen_qa)
│    └── details/
│        └── model/
│            └── execution-date-time/
│                └──details_task_name_#_datetime.parquet
└── tensorboard-results/
    └── eval/
        └── events.out.tfevents.[timestamp]
```

Metrics results are stored in the specified S3 output location
`s3://output_path/job_name/eval-result/result-timestamp.json`.

Tensorboard results are stored in the S3 path
`s3://output_path/job_name/eval-tensorboard-result/eval/event.out.tfevents.epoch+ip`.

All inference outputs, except for `llm_judge` and
`strong_reject`, are stored in the S3 path:
`s3://output_path/job_name/eval-result/details/model/taskname.parquet`.

For `gen_qa`, the `inference_output.jsonl` file contains the
following fields for each JSON object:

- prompt - The final prompt submitted to the
  model
- inference - The raw inference output from the
  model
- gold - The target response from the input dataset
- metadata - The metadata string from the input dataset if provided

To visualize your evaluation metrics in Tensorboard, complete the following
steps:

1. Navigate to SageMaker AI Tensorboard.
2. Select **S3 folders**.
3. Add your S3 folder path, for example
   `s3://output_path/job-name/eval-tensorboard-result/eval`.
4. Wait for synchronization to complete.

The time series, scalars, and text visualizations are available.

We recommend the following best practices:

- Keep your output paths organized by model and benchmark type.
- Maintain consistent naming conventions for easy tracking.
- Save extracted results in a secure location.
- Monitor TensorBoard sync status for successful data loading.

You can find HyperPod job error logs in the CloudWatch log group
`/aws/sagemaker/Clusters/cluster-id`.
