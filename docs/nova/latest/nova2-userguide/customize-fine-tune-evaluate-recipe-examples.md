# Evaluation recipe

examples

Amazon Nova provides four types of evaluation recipes, which are available in the
SageMaker AI HyperPod recipes GitHub repository.

These recipes enable you to evaluate the fundamental capabilities of Amazon Nova models
across a comprehensive suite of text-only benchmarks. They are provided in the format
`xxx_general_text_benchmark_eval.yaml`.

These recipes enable you to bring your own dataset for benchmarking and compare
model outputs to reference answers using different types of metrics. They are provided
in the format `xxx_bring_your_own_dataset_eval.yaml`.

The following are the bring your own dataset requirements:

- File format requirements
  - You must include a single `gen_qa.jsonl` file containing
    evaluation examples.
  - Your dataset must be uploaded to an S3 location where SageMaker AI training job can
    access it.
  - The file must follow the required schema format for a general Q&A
    dataset.

- Schema format requirements - Each line in the JSONL file must be a JSON object
  with the following fields:

      + `query`: (Required) String containing the question or instruction
       that needs an answer
      + `response`: (Required) String containing the expected model
       output
      + `system`: (Optional) String containing the system prompt that
       sets the behavior, role, or personality of the AI model before it processes the
       query
      + `metadata`: (Optional) String containing metadata associated with
       the entry for tagging purposes.

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

To use your custom dataset, modify your evaluation recipe with the following
required fields, do not change any of the content:

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
  compare the quality of responses from one model to a baseline model response on a custom
  dataset. It takes in a dataset with prompts, baseline responses, and challenger
  responses, and uses a Amazon Nova Judge model to provide a winrate metric based on [Bradley-Terry
  probability](https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model "https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model") with pairwise comparisons.

The recipes are provided in the format `xxx_llm_judge_eval.yaml`.

The following are the LLM as a Judge requirements:

- File format requirements
  - Include a single `llm_judge.jsonl` file containing evaluation
    examples. The file name must be `llm_judge.jsonl`.
  - Your dataset must be uploaded to an S3 location that [SageMaker AI
    SageMaker AI Hyperpod RIG](../../../sagemaker/latest/dg/nova-hp-cluster.md "../../../sagemaker/latest/dg/nova-hp-cluster.md") can access.
  - The file must follow the required schema format for the
    `llm_judge.jsonl` dataset.
  - The input dataset should ensure all records are under 12k context
    length.

- Schema format requirements - Each line in the JSONL file must be a JSON object
  with the following fields:

      + `prompt`: (Required) A string containing the prompt for the
       generated response.
      + `response_A`: A string containing the baseline response.
      + `response_B`: A string containing the alternative response be
       compared with baseline response.

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

To use your custom dataset, modify your evaluation recipe with the following
required fields, don't change any of the content:

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
  Nova LLM Judge for multi-modal (image), short for Amazon Nova MM_LLM Judge, is a model
  evaluation feature that enables you to compare the quality of responses from one model
  against a baseline model's responses using a custom dataset. It accepts a dataset
  containing prompts, baseline responses, and challenger responses, and images in the form
  of Base64-encoded string, then uses a Amazon Nova Judge model to provide a win rate metric
  based on [Bradley-Terry](https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model "https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model") probability through pairwise comparisons. Recipe format:
  `xxx_mm_llm_judge _eval.yaml`.

**Nova LLM dataset requirements**

File format:

- Single `mm_llm_judge.jsonl` file containing evaluation examples. The
  file name must be exactly `llm_judge.jsonl`.
- Your must upload your dataset to an S3 location where SageMaker AI training jobs can
  access it.
- The file must follow the required schema format for the
  `mm_llm_judge` dataset.
- The input dataset should ensure all records are under 12 k context length,
  excluding the image's attribute.
  Schema format - Each line in the `.jsonl` file must be a JSON object with
  the following fields.

- Required fields.

`prompt`: String containing the prompt for the generated
response.

`images`: Array containing a list of objects with data attributes
(values are Base64-encoded image strings).

`response_A`: String containing the baseline response.

`response_B`: String containing the alternative response be compared
with baseline response.
Example entry

For readability, the following example includes new lines and indentation, but in
the actual dataset, each record should be on a single line.

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
- Nova MM Judge models are the same across Amazon Nova Lite
  specifications.
- Custom judge models are not currently supported.
- Amazon S3 image URI is not supported.
- The input dataset should ensure all records are under 12 k context length,
  excluding images attribute.
  Rubric Judge is an enhanced LLM-as-a-judge evaluation model built on Amazon Nova 2.0 Lite.
  Unlike the [original judge model](https://aws.amazon.com/blogs/machine-learning/evaluating-generative-ai-models-with-amazon-nova-llm-as-a-judge-on-amazon-sagemaker-ai/ "https://aws.amazon.com/blogs/machine-learning/evaluating-generative-ai-models-with-amazon-nova-llm-as-a-judge-on-amazon-sagemaker-ai/") that only provides preference verdicts (A>B, B>A, or
  tie), Rubric Judge dynamically generates custom evaluation criteria tailored to each prompt
  and assigns granular scores across multiple dimensions.

Key capabilities:

- **Dynamic criteria generation**: Automatically creates
  relevant evaluation dimensions based on the input prompt
- **Weighted scoring**: Assigns importance weights to
  each criterion to reflect their relative significance
- **Granular assessment**: Provides detailed scores on a
  binary (true/false) or scale (1-5) basis for each criterion
- **Quality metrics**: Calculates continuous quality
  scores (0-1 scale) that quantify the magnitude of differences between responses
  Example criterion generated by the model:

```
price_validation:
  description: "The response includes validation to ensure price is a positive value."
  type: "scale"
  weight: 0.3
```

The model evaluates both responses against all generated criteria, then uses these
criterion-level scores to inform its final preference decision.

###### Topics

- [Recipe configuration](#nova-hp-evaluate-rubric-judge-recipe "#nova-hp-evaluate-rubric-judge-recipe")
- [Input dataset format](#nova-hp-evaluate-rubric-judge-input "#nova-hp-evaluate-rubric-judge-input")
- [Evaluation output](#nova-hp-evaluate-rubric-judge-output "#nova-hp-evaluate-rubric-judge-output")
- [Reasoning model support](#nova-hp-evaluate-rubric-judge-reasoning "#nova-hp-evaluate-rubric-judge-reasoning")

### Recipe configuration

###### Rubric Judge recipe

Enable Rubric Judge by setting `task: rubric_llm_judge` in your
recipe:

```
run:
  name: nova-eval-job-name                              # [MODIFIABLE] Unique identifier for your evaluation job
  model_type: amazon.nova-2-lite-v1:0:256k              # [FIXED] Rubric Judge model type
  model_name_or_path: "nova-lite-2/prod"                # [FIXED] Path to model checkpoint or identifier
  replicas: 1                                           # [MODIFIABLE] Number of replicas for SageMaker Training job
  data_s3_path: ""                                      # [FIXED] Leave empty for SageMaker Training job
  output_s3_path: ""                                    # [FIXED] Leave empty for SageMaker Training job

evaluation:
  task: rubric_llm_judge                                # [FIXED] Evaluation task - enables Rubric Judge
  strategy: judge                                       # [FIXED] Evaluation strategy
  metric: all                                           # [FIXED] Metric calculation method

inference:
  max_new_tokens: 12000                                 # [MODIFIABLE] Maximum tokens to generate
  top_k: -1                                             # [MODIFIABLE] Top-k sampling parameter
  top_p: 1.0                                            # [MODIFIABLE] Nucleus sampling parameter
  temperature: 0                                        # [MODIFIABLE] Sampling temperature (0 = deterministic)
```

###### Original LLM as a Judge recipe (for comparison)

The original judge model uses `task: llm_judge`:

```
run:
  name: eval-job-name                                   # [MODIFIABLE] Unique identifier for your evaluation job
  model_type: amazon.nova-micro-v1:0:128k               # [FIXED] Model type
  model_name_or_path: "nova-micro/prod"                 # [FIXED] Path to model checkpoint or identifier
  replicas: 1                                           # [MODIFIABLE] Number of replicas for SageMaker Training job
  data_s3_path: ""                                      # [FIXED] Leave empty for SageMaker Training job
  output_s3_path: ""                                    # [FIXED] Leave empty for SageMaker Training job

evaluation:
  task: llm_judge                                       # [FIXED] Original judge task
  strategy: judge                                       # [FIXED] Evaluation strategy
  metric: all                                           # [FIXED] Metric calculation method

inference:
  max_new_tokens: 12000                                 # [MODIFIABLE] Maximum tokens to generate
  top_k: -1                                             # [MODIFIABLE] Top-k sampling parameter
  top_p: 1.0                                            # [MODIFIABLE] Nucleus sampling parameter
  temperature: 0                                        # [MODIFIABLE] Sampling temperature (0 = deterministic)
```

### Input dataset format

The input dataset format is identical to the [original judge model](https://aws.amazon.com/blogs/machine-learning/evaluating-generative-ai-models-with-amazon-nova-llm-as-a-judge-on-amazon-sagemaker-ai/ "https://aws.amazon.com/blogs/machine-learning/evaluating-generative-ai-models-with-amazon-nova-llm-as-a-judge-on-amazon-sagemaker-ai/"):

**Required fields:**

- `prompt`: String containing the input prompt and instructions
- `response_A`: String containing the baseline model output
- `response_B`: String containing the customized model output

**Example dataset (JSONL format):**

```
{"prompt": "What is the most effective way to combat climate change?", "response_A": "The most effective way to combat climate change is through a combination of transitioning to renewable energy sources and implementing strict carbon pricing policies. This creates economic incentives for businesses to reduce emissions while promoting clean energy adoption.", "response_B": "We should focus on renewable energy. Solar and wind power are good. People should drive electric cars. Companies need to pollute less."}
{"prompt": "Explain how a computer's CPU works", "response_A": "CPU is like brain of computer. It does math and makes computer work fast. Has lots of tiny parts inside.", "response_B": "A CPU (Central Processing Unit) functions through a fetch-execute cycle, where instructions are retrieved from memory, decoded, and executed through its arithmetic logic unit (ALU). It coordinates with cache memory and registers to process data efficiently using binary operations."}
{"prompt": "How does photosynthesis work?", "response_A": "Plants do photosynthesis to make food. They use sunlight and water. It happens in leaves.", "response_B": "Photosynthesis is a complex biochemical process where plants convert light energy into chemical energy. They utilize chlorophyll to absorb sunlight, combining CO2 and water to produce glucose and oxygen through a series of chemical reactions in chloroplasts."}
```

**Format requirements:**

- Each entry must be a single-line JSON object
- Separate entries with newlines
- Follow the exact field naming as shown in examples

### Evaluation output

###### Output structure

Rubric Judge produces enhanced evaluation metrics compared to the original judge
model:

```
{
  "config_general": {
    "lighteval_sha": "string",
    "num_fewshot_seeds": "int",
    "max_samples": "int | null",
    "job_id": "int",
    "start_time": "float",
    "end_time": "float",
    "total_evaluation_time_secondes": "string",
    "model_name": "string",
    "model_sha": "string",
    "model_dtype": "string | null",
    "model_size": "string"
  },
  "results": {
    "custom|rubric_llm_judge_judge|0": {
      "a_scores": "float",
      "a_scores_stderr": "float",
      "b_scores": "float",
      "b_scores_stderr": "float",
      "ties": "float",
      "ties_stderr": "float",
      "inference_error": "float",
      "inference_error_stderr": "float",
      "score": "float",
      "score_stderr": "float",
      "weighted_score_A": "float",
      "weighted_score_A_stderr": "float",
      "weighted_score_B": "float",
      "weighted_score_B_stderr": "float",
      "score_margin": "float",
      "score_margin_stderr": "float",
      "winrate": "float",
      "lower_rate": "float",
      "upper_rate": "float"
    }
  },
  "versions": {
    "custom|rubric_llm_judge_judge|0": "int"
  }
}
```

###### New metrics in Rubric Judge

The following six metrics are unique to Rubric Judge and provide granular quality
assessment:

| Metric                  | Description                                                                                                                                                                                                     |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| weighted_score_A        | Average normalized quality score for response_A across all model-generated<br>evaluation criteria. Scores are weighted by criterion importance and normalized to<br>0-1 scale (higher = better quality)         |
| weighted_score_A_stderr | Standard error of the mean for weighted_score_A, indicating statistical<br>uncertainty                                                                                                                          |
| weighted_score_B        | Average normalized quality score for response_B across all model-generated<br>evaluation criteria. Scores are weighted by criterion importance and normalized to<br>0-1 scale (higher = better quality)         |
| weighted_score_B_stderr | Standard error of the mean for weighted_score_B, indicating statistical<br>uncertainty                                                                                                                          |
| score_margin            | Difference between weighted scores (calculated as weighted_score_A -<br>weighted_score_B). Range: -1.0 to 1.0. Positive = response_A is better; negative =<br>response_B is better; near zero = similar quality |
| score_margin_stderr     | Standard error of the mean for score_margin, indicating uncertainty in the<br>quality difference measurement                                                                                                    |

###### Understanding weighted score metrics

**Purpose**: Weighted scores provide continuous quality
measurements that complement binary preference verdicts, enabling deeper insights into
model performance.

**Key differences from original judge**:

- **Original judge**: Only outputs discrete preferences
  (A>B, B>A, A=B)
- **Rubric Judge**: Outputs both preferences AND
  continuous quality scores (0-1 scale) based on custom criteria

**Interpreting score_margin**:

- `score_margin = -0.128`: Response_B scored 12.8 percentage points
  higher than response_A
- `|score_margin| < 0.1`: Narrow quality difference (close
  decision)
- `|score_margin| > 0.2`: Clear quality difference (confident
  decision)

**Use cases**:

- **Model improvement**: Identify specific areas where
  your model underperforms
- **Quality quantification**: Measure the magnitude of
  performance gaps, not just win/loss ratios
- **Confidence assessment**: Distinguish between close
  decisions and clear quality differences

###### Important

Final verdicts are still based on the judge model's explicit preference labels to
preserve holistic reasoning and ensure proper position bias mitigation through
forward/backward evaluation. Weighted scores serve as observability tools, not as
replacements for the primary verdict.

###### Calculation methodology

Weighted scores are computed through the following process:

- **Extract criterion data**: Parse the judge's YAML
  output to extract criterion scores and weights
- **Normalize scores**:
  - Scale-type criteria (1-5): Normalize to 0-1 by calculating `(score - 1) /
4`
  - Binary criteria (true/false): Convert to 1.0/0.0

- **Apply weights**: Multiply each normalized score by
  its criterion weight
- **Aggregate**: Sum all weighted scores for each
  response
- **Calculate margin**: Compute `score_margin =
weighted_score_A - weighted_score_B`

**Example**: If response_A has a weighted sum of 0.65 and
response_B has 0.78, the `score_margin` would be -0.13, indicating response_B
is 13 percentage points higher in quality across all weighted criteria.

### Reasoning model support

Reasoning model support enables evaluation with reasoning-capable Amazon Nova models that
perform explicit internal reasoning before generating final responses. This feature uses
API-level control via the `reasoning_effort` parameter to dynamically enable or
disable reasoning functionality, potentially improving response quality for complex
analytical tasks.

**Supported models**:

- amazon.nova-2-lite-v1:0:256k

###### Recipe configuration

Enable reasoning by adding the `reasoning_effort` parameter to the
`inference` section of your recipe:

```
run:
  name: eval-job-name                                    # [MODIFIABLE] Unique identifier for your evaluation job
  model_type: amazon.nova-2-lite-v1:0:256k               # [FIXED] Must be a reasoning-supported model
  model_name_or_path: nova-lite-2/prod                   # [FIXED] Path to model checkpoint or identifier
  replicas: 1                                            # [MODIFIABLE] Number of replicas for SageMaker Training job
  data_s3_path: ""                                       # [MODIFIABLE] Leave empty for SageMaker Training job; optional for SageMaker  SageMaker AI Hyperpod  job
  output_s3_path: ""                                     # [MODIFIABLE] Output path for SageMaker  SageMaker AI Hyperpod  job (not compatible with SageMaker Training jobs)

evaluation:
  task: mmlu                                             # [MODIFIABLE] Evaluation task
  strategy: generate                                     # [MODIFIABLE] Evaluation strategy
  metric: all                                            # [MODIFIABLE] Metric calculation method

inference:
  reasoning_effort: high                                 # [MODIFIABLE] Enables reasoning mode; options: low/medium/high or null to disable
  max_new_tokens: 200                                    # [MODIFIABLE] Maximum tokens to generate
  top_k: 50                                              # [MODIFIABLE] Top-k sampling parameter
  top_p: 1.0                                             # [MODIFIABLE] Nucleus sampling parameter
  temperature: 0                                         # [MODIFIABLE] Sampling temperature (0 = deterministic)
```

###### Using the reasoning_effort parameter

The `reasoning_effort` parameter controls the reasoning behavior for
reasoning-capable models.

**Prerequisites**:

- **Model compatibility**: Set
  `reasoning_effort` only when `model_type` specifies a
  reasoning-capable model (currently `amazon.nova-2-lite-v1:0:256k`)
- **Error handling**: Using
  `reasoning_effort` with unsupported models will fail with
  `ConfigValidationError: "Reasoning mode is enabled but model '{model_type}'
does not support reasoning. Please use a reasoning-capable model or disable
reasoning mode."`

**Available options**:

| Option         | Behavior                              | Token Limit                          | Use Case                                                                    |
| -------------- | ------------------------------------- | ------------------------------------ | --------------------------------------------------------------------------- |
| null (default) | Disables reasoning mode               | N/A                                  | Standard evaluation without reasoning overhead                              |
| low            | Enables reasoning with constraints    | 4,000 tokens for internal reasoning  | Scenarios requiring concise reasoning; optimizes for speed and<br>cost      |
| high           | Enables reasoning without constraints | No token limit on internal reasoning | Complex problems requiring extensive analysis and step-by-step<br>reasoning |

###### When to enable reasoning

**Use reasoning mode (`low`, `medium`, or
`high`) for**:

- Complex problem-solving tasks (mathematics, logic puzzles, coding)
- Multi-step analytical questions requiring intermediate reasoning
- Tasks where detailed explanations or step-by-step thinking improve accuracy
- Scenarios where response quality is prioritized over speed

**Use non-reasoning mode (omit parameter) for**:

- Simple Q&A or factual queries
- Creative writing tasks
- When faster response times are critical
- Performance benchmarking where reasoning overhead should be excluded
- Cost optimization when reasoning doesn't improve task performance

###### Troubleshooting

**Error: "Reasoning mode is enabled but model does not support
reasoning"**

**Cause**: The `reasoning_effort` parameter is
set to a non-null value, but the specified `model_type` doesn't support
reasoning.

**Resolution**:

- Verify your model type is `amazon.nova-2-lite-v1:0:256k`
- If using a different model, either switch to a reasoning-capable model or remove
  the `reasoning_effort` parameter from your recipe
