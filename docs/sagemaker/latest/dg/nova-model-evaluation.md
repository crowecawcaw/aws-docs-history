# Evaluating your SageMaker AI-trained model

The purpose of the evaluation process is to assess trained-model performance against
benchmarks or custom dataset. The evaluation process typically involves steps to create
evaluation recipe pointing to the trained model, specify evaluation datasets and
metrics, submit a separate job for the evaluation, and evaluate against standard
benchmarks or custom data. The evaluation process will output performance metrics stored
in your Amazon S3 bucket.

###### Note

The evaluation process described in this topic is an offline process. The model is
tested against fixed benchmarks with predefined answers, rather than being assessed
in real-time or through live user interactions. For real-time evaluation, you can
test the model after it has been deployed to Amazon Bedrock by calling [Amazon Bedrock](../../../bedrock/latest/userguide/import-with-create-custom-model.md "../../../bedrock/latest/userguide/import-with-create-custom-model.md") Runtime APIs.

###### Topics

- [Prerequisites](#nova-model-evaluation-prerequisites "#nova-model-evaluation-prerequisites")
- [Available benchmark tasks](#nova-model-evaluation-benchmark "#nova-model-evaluation-benchmark")
- [Evaluation specific
  configurations](#nova-model-evaluation-config "#nova-model-evaluation-config")
- [Running evaluation training
  jobs](#nova-model-evaluation-notebook "#nova-model-evaluation-notebook")
- [Assessing and analyzing evaluation
  results](#nova-model-evaluation-assess "#nova-model-evaluation-assess")
- [Evaluation best practices and
  troubleshooting](#nova-model-evaluation-best-practices "#nova-model-evaluation-best-practices")
- [Available subtasks](#nova-model-evaluation-subtasks "#nova-model-evaluation-subtasks")
- [Rubric Based Judge](nova-rubric-judge-evaluation.md "nova-rubric-judge-evaluation.md")
- [Reasoning model evaluation](nova-reasoning-model-evaluation.md "nova-reasoning-model-evaluation.md")
- [RFT evaluation](nova-rft-evaluation.md "nova-rft-evaluation.md")
- [Implementing reward functions](nova-implementing-reward-functions.md "nova-implementing-reward-functions.md")
- [Running evaluations and interpreting results](nova-running-evaluations.md "nova-running-evaluations.md")

## Prerequisites

Before you start a evaluation training job, note the following.

- A SageMaker AI-trained Amazon Nova model which you want to evaluate its
  performance.
- Base Amazon Nova recipe for evaluation. For more information, see [Getting Amazon Nova recipes](nova-model-recipes.md#nova-model-get-recipes "nova-model-recipes.md#nova-model-get-recipes").

## Available benchmark tasks

A sample code package is available that demonstrates how to calculate benchmark
metrics using the SageMaker model evaluation feature for Amazon Nova. To access the code
packages, see [sample-Nova-lighteval-custom-task](https://github.com/aws-samples/sample-Nova-lighteval-custom-task/ "https://github.com/aws-samples/sample-Nova-lighteval-custom-task/").

Here is a list of available industry standard benchmarks supported. You can
specify the following benchmarks in the `eval_task` parameter.

**Available benchmarks for model evaluation**

| Benchmark           | Modality            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Metrics     | Strategy | Subtask available |
| ------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | -------- | ----------------- |
| mmlu                | Text                | Multi-task Language Understanding – Tests knowledge across 57<br>subjects.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | accuracy    | zs_cot   | Yes               |
| mmlu_pro            | Text                | MMLU – Professional Subset – Focuses on professional domains<br>such as law, medicine, accounting, and engineering.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | accuracy    | zs_cot   | No                |
| bbh                 | Text                | Advanced Reasoning Tasks – A collection of challenging<br>problems that test higher-level cognitive and problem-solving<br>skills.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | accuracy    | fs_cot   | Yes               |
| gpqa                | Text                | General Physics Question Answering – Assesses comprehension of<br>physics concepts and related problem-solving abilities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | accuracy    | zs_cot   | No                |
| math                | Text                | Mathematical Problem Solving – Measures mathematical reasoning<br>across topics including algebra, calculus, and word<br>problems.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | exact_match | zs_cot   | Yes               |
| strong_reject       | Text                | Quality-Control Task – Tests the model’s ability to detect and<br>reject inappropriate, harmful, or incorrect content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | deflection  | zs       | Yes               |
| ifeval              | Text                | Instruction-Following Evaluation – Gauges how accurately a<br>model follows given instructions and completes tasks to<br>specification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                | accuracy    | zs       | No                |
| gen_qa              | Multi-Modal (image) | Custom Dataset Evaluation – Lets you supply your own dataset<br>for benchmarking, comparing model outputs to reference answers<br>with metrics such as ROUGE and BLEU. `gen_qa`<br>supports image inference for Amazon Nova Lite or Amazon Nova Pro<br>based models. Also supports Bring-Your-Own Metrics lambda. (For<br>RFT evaluation, please use RFT eval recipe)                                                                                                                                                                                                                                  | all         | gen_qa   | No                |
| llm_judge           | Text                | LLM-as-a-Judge Preference Comparison – Uses a Nova Judge model<br>to determine preference between paired responses (B compared<br>with A) for your prompts, calculating the probability of B being<br>preferred over A.                                                                                                                                                                                                                                                                                                                                                                                | all         | judge    | No                |
| mm_llm_judge        | Multi-Modal (image) | This new benchmark behaves the same as the text-based<br>`llm_judge`above. The only difference is that it<br>supports image inference.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | all         | judge    | No                |
| rubric_llm_judge    | Text                | Rubric Judge is an enhanced LLM-as-a-judge evaluation model<br>built on Nova 2.0 Lite. Unlike the [original judge model](https://aws.amazon.com/blogs/machine-learning/evaluating-generative-ai-models-with-amazon-nova-llm-as-a-judge-on-amazon-sagemaker-ai/ "https://aws.amazon.com/blogs/machine-learning/evaluating-generative-ai-models-with-amazon-nova-llm-as-a-judge-on-amazon-sagemaker-ai/") that only provides preference<br>verdicts, Rubric Judge dynamically generates custom evaluation<br>criteria tailored to each prompt and assigns granular scores<br>across multiple dimensions. | all         | judge    | No                |
| aime_2024           | Text                | AIME 2024<br>• American Invitational Mathematics Examination<br>problems testing advanced mathematical reasoning and<br>problem-solving                                                                                                                                                                                                                                                                                                                                                                                                                                                                | exact_match | zs_cot   | No                |
| calendar_scheduling | Text                | Natural Plan<br>• Calendar Scheduling task testing planning<br>abilities for scheduling meetings across multiple days and<br>people                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | exact_match | fs       | No                |
| humaneval           | Text                | HumanEval<br>• A benchmark dataset designed to evaluate the code<br>generation capabilities of large language models                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | pass@1      | zs       | No                |

## Evaluation specific

configurations

Below is a breakdown of the key components in the recipe and guidance on how to
modify them for your use cases.

### Understanding and

modifying your recipes

**General run configuration**

```
run:
  name: eval_job_name
  model_type: amazon.nova-2-lite-v1:0:256k
  model_name_or_path: nova-lite-2/prod # or s3://escrow_bucket/model_location
  replicas: 1
  data_s3_path: ""
  mlflow_tracking_uri: ""
  mlflow_experiment_name : ""
  mlflow_run_name : ""
```

- `name`: A descriptive name for your evaluation job.
- `model_type`: Specifies the Nova model variant to use. Do
  not manually modify this field. Options include:
  - amazon.nova-micro-v1:0:128k
  - amazon.nova-lite-v1:0:300k
  - amazon.nova-pro-v1:0:300k
  - amazon.nova-2-lite-v1:0:256k

- `model_name_or_path`: The path to the base model or s3 path
  for post trained checkpoint. Options include:
  - nova-micro/prod
  - nova-lite/prod
  - nova-pro/prod
  - nova-lite-2/prod
  - S3 path for post trained checkpoint path
    (`s3:customer-escrow-111122223333-smtj-<unique_id>/<training_run_name>`)

  ###### Note

  **Evaluate post-trained
  model**

  To evaluate a post-trained model after a Nova SFT training
  job, follow these steps after running a successful training
  job. At the end of the training logs, you will see the log
  message "Training is complete". You will also find a
  `manifest.json` file in your output bucket
  containing the location of your checkpoint. This file will
  be located within an `output.tar.gz` file at your
  output S3 location. To proceed with evaluation, use this
  checkpoint by setting it as the value for
  `run.model_name_or_path` in your recipe
  configuration.

- `replica`: The number of compute instances to use for
  distributed inference (running inference across multiple nodes). Set
  `replica` > 1 to enable multi-node inference, which
  accelerates evaluation. If both `instance_count` and
  `replica` are specified, `instance_count`
  takes precedence. Note that multiple replicas only apply to SageMaker
  training jobs, not SageMaker HyperPod.
- `data_s3_path`: The input dataset Amazon S3 path. This field is
  required but should always left empty.
- `mlflow_tracking_uri`: (Optional) The location of the MLflow tracking server (only needed on SMHP)
- `mlflow_experiment_name`: (Optional) Name of the experiment to group related ML runs together
- `mlflow_run_name`: (Optional) Custom name for a specific training run within an experiment

**Evaluation configuration**

```
evaluation:
  task: mmlu
  strategy: zs_cot
  subtask: abstract_algebra
  metric: accuracy
```

- `task`: Specifies the evaluation benchmark or task to use.
  Supported task includes:
  - `mmlu`
  - `mmlu_pro`
  - `bbh`
  - `gpqa`
  - `math`
  - `strong_reject`
  - `gen_qa`
  - `ifeval`
  - `llm_judge`
  - `mm_llm_judge`
  - `rubric_llm_judge`
  - `aime_2024`
  - `calendar_scheduling`
  - `humaneval`

- `strategy`: Defines the evaluation approach.
  - `zs_cot`: Zero-shot Chain of Thought - an approach
    to prompt large language models that encourages step-by-step
    reasoning without requiring explicit examples.
  - `fs_cot`: Few-shot Chain of Thought - an approach
    that provides a few examples of step-by-step reasoning before
    asking the model to solve a new problem.
  - `zs`: Zero-shot - an approach to solve a problem
    without any prior training examples.
  - `gen_qa`: Strategy specific for bring your own
    dataset.
  - `judge`: Strategy specific for Nova LLM as Judge
    and `mm_llm_judge`.

- `subtask`: Optional. Specific components of the evaluation
  task. For a complete list of available subtasks, see [Available subtasks](#nova-model-evaluation-subtasks "#nova-model-evaluation-subtasks").
  - Check supported subtasks in Available benchmarks tasks.
  - Should remove this field if there are no subtasks
    benchmarks.

- `metric`: The evaluation metric to use.
  - `accuracy`: Percentage of correct answers.
  - `exact_match`: For math benchmark, returns the rate
    at which the input predicted strings exactly match their
    references.
  - `deflection`: For strong reject benchmark, returns
    relative deflection to base model and difference significance
    metrics.
  - `all`:

  For `gen_qa`, bring your own dataset benchmark,
  return following metrics:

      - `rouge1`: Measures overlap of unigrams
       (single words) between generated and reference
       text.
      - `rouge2`: Measures overlap of bigrams (two
       consecutive words) between generated and reference
       text.
      - `rougeL`: Measures longest common
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
      - `f1_score_quasi`: Similar to f1\_score but
       with more lenient matching, using normalized text
       comparison that ignores minor differences.
      - `bleu`: Measures precision of n-gram
       matches between generated and reference text, commonly
       used in translation evaluation.

  For `llm_judge` and `mm_llm_judge`,
  bring your own dataset benchmark, return following
  metrics:

      - `a_scores`: Number of wins for
       `response_A` across forward and backward
       evaluation passes.
      - `a_scores_stderr`: Standard error of
       `response_A_scores` across pairwise
       judgements.
      - `b_scores`: Measures Number of wins for
       `response_B` across forward and backward
       evaluation passes.
      - `a_scores_stderr`: Standard error of
       `response_B_scores` across pairwise
       judgements.
      - `ties`: Number of judgements where
       `response_A` and `response_B`
       are evaluated as equal.
      - `ties_stderr`: Standard error of
       `ties` across pairwise judgements.
      - `inference_error`: Count of judgements that
       could not be properly evaluated.
      - `score`: Aggregate score based on wins from
       both forward and backward passes for
       `response_B`.
      - `score_stderr`: Aggregate score based on
       wins from both forward and backward passes for
       `response_B`.
      - `inference_error_stderr`: Standard error of
       the aggregate score across pairwise judgements.
      - `winrate`: The probability that
       `response_B` will be preferred over
       `response_A` calculated using
       Bradley-Terry probability.
      - `lower_rate`: Lower bound (2.5th
       percentile) of the estimated win rate from bootstrap
       sampling.
      - `upper_rate`: Upper bound (97.5th
       percentile) of the estimated win rate from bootstrap
       sampling.

**Inference configuration (optional)**

```
inference:
  max_new_tokens: 2048
  top_k: -1
  top_p: 1.0
  temperature: 0
  top_logprobs: 10
  reasoning_effort: null  # options: low/high to enable reasoning or null to disable reasoning
```

- `max_new_tokens`: Maximum number of tokens to generate.
  Must be an integer. (Unavailable for LLM Judge)
- `top_k`: Number of the highest probability tokens to
  consider. Must be an integer.
- `top_p`: Cumulative probability threshold for token
  sampling. Must be a float between 1.0 to 0.0.
- `temperature`: Randomness in token selection (higher = more
  random), keep 0 to make the result deterministic. Float type, minimal
  value is 0.
- `top_logprobs`: The number of top logprobs to be returned
  in the inference response. This value must be an integer from 0 to 20.
  Logprobs contain the considered output tokens and log probabilities of
  each output token returned in the message content.
- `reasoning_effort`: controls the reasoning behavior for
  reasoning-capable models. Set `reasoning_effort` only when
  `model_type` specifies a reasoning-capable model (currently `amazon.nova-2-lite-v1:0:256k`).
  Available options are null (default value if not set; disables reasoning), low, or high.

### Evaluation recipe

examples

Amazon Nova provides four different types of evaluation recipes. All recipes are
available in [Amazon SageMaker HyperPod recipes GitHub repository](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection "https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection").

###### Evaluation recipes

These recipes enable you to evaluate the fundamental capabilities of
Amazon Nova models across a comprehensive suite of text-only benchmarks.

Recipe format:
`xxx_general_text_benchmark_eval.yaml`.

These recipes enable you to bring your own dataset for benchmarking
and compare model outputs to reference answers using different types of
metrics.

Recipe format: `xxx_
 bring_your_own_dataset_eval.yaml`.

**Bring your own dataset
requirements**

File format:

- Single `gen_qa.jsonl` file containing evaluation
  examples. The file name should be exact
  `gen_qa.jsonl`.
- Your must upload your dataset to an S3 location where SageMaker
  training jobs can access.
- The file must follow the required schema format for general
  Q&A dataset.
  Schema format requirements - Each line in the `.jsonl` file
  must be a JSON object with the following fields.

- Required fields.

`query`: String containing the question or
instruction that needs an answer.

`response`: String containing the expected model
output.

- Optional fields.

`system`: String containing the system prompt that
sets the behavior, role, or personality of the AI model before
it processes the query.

`images`: Array containing a list of objects with
data attributes (Base64 encoded image strings).

`metadata`: String containing metadata associated
with the entry for tagging purposes.
**Example entry**

```
{
"system":"You are an English major with top marks in class who likes to give minimal word responses: ",
   "query":"What is the symbol that ends the sentence as a question",
   "response":"?"
}{
"system":"You are a pattern analysis specialist who provides succinct answers: ",
   "query":"What is the next number in this series? 1, 2, 4, 8, 16, ?",
   "response":"32"
}{
"system":"You have great attention to detail and follow instructions accurately: ",
   "query":"Repeat only the last two words of the following: I ate a hamburger today and it was kind of dry",
   "response":"of dry"
}{
"system": "Image inference: ",
  "query": "What is the number in the image? Please just use one English word to answer.",
  "response": "two",
  "images": [
    {
      "data": "data:image/png;Base64,iVBORw0KGgoA ..."
    }
  ]
}
```

To use your custom dataset, modify your evaluation recipe by adding
the following required fields without changing the existing
configuration:

```
evaluation:
  task: gen_qa
  strategy: gen_qa
  metric: all
```

**Limitations**

- Only one `.jsonl` file is allowed per
  evaluation.
- The file must strictly follow the defined schema.

##### Bring your own

metrics

You can bring your own metrics to fully customize your model
evaluation workflow with custom preprocessing, postprocessing, and
metrics capabilities. Preprocessing allows you to process input data
before sending it to the inference server, and postprocessing allows
you to customize metrics calculation and return custom metrics based
on your needs.

Follow these steps to bring your own metrics with custom
evaluation SDK.

1. If you haven't done so, [create an
   AWS Lambda function](../../../lambda/latest/dg/getting-started.md "../../../lambda/latest/dg/getting-started.md") in your AWS account
   first.
2. Download the pre-built
   `nova-custom-eval-layer.zip` file from the
   [GitHub repository](https://github.com/aws/nova-custom-eval-sdk/releases "https://github.com/aws/nova-custom-eval-sdk/releases"). You can use this open-source
   Nova custom evaluation SDK to validate input and output
   payloads for your custom function and provide a unified
   interface for integrating with Nova's bring your own metrics
   evaluation during training.
3. Upload the custom Lambda layer using the following
   command:

```
aws lambda publish-layer-version \
    --layer-name nova-custom-eval-layer \
    --zip-file fileb://nova-custom-eval-layer.zip \
    --compatible-runtimes python3.12 python3.11 python3.10 python3.9
```

4. Add this layer as a custom layer to your Lambda function,
   along with the required AWS layer:
   `AWSLambdaPowertoolsPythonV3-python312-arm64`
   (required for `pydantic` dependency).
5. Update your Lambda code using the provided example,
   modifying the code as needed. This example code creates a
   Lambda function for Nova's custom evaluation with
   preprocessing and postprocessing steps for model
   evaluation.

```
from nova_custom_evaluation_sdk.processors.decorators import preprocess, postprocess
from nova_custom_evaluation_sdk.lambda_handler import build_lambda_handler

@preprocess
def preprocessor(event: dict, context) -> dict:
    data = event.get('data', {})
    return {
        "statusCode": 200,
        "body": {
            "system": data.get("system"),
            "prompt": data.get("prompt", ""),
            "gold": data.get("gold", "")
        }
    }

@postprocess
def postprocessor(event: dict, context) -> dict:
    # data is already validated and extracted from event
    data = event.get('data', [])
    inference_output = data.get('inference_output', '')
    gold = data.get('gold', '')

    metrics = []
    inverted_accuracy = 0 if inference_output.lower() == gold.lower() else 1.0
    metrics.append({
        "metric": "inverted_accuracy_custom",
        "value": accuracy
    })

    # Add more metrics here

    return {
        "statusCode": 200,
        "body": metrics
    }

# Build Lambda handler
lambda_handler = build_lambda_handler(
    preprocessor=preprocessor,
    postprocessor=postprocessor
)
```

6. Grant Lambda access to the evaluation job. Ensure the
   execution role specified for the evaluation job includes a
   policy the invoke your Lambda function. Here is an example
   policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "LambdaAccess",
 "Effect": "Allow",
 "Action": [
 "lambda:InvokeFunction"
 ],
 "Resource": "arn:aws:lambda:us-east-1:111122223333:function:ExampleFunction",
 "Condition": {
 "StringLike": {
 "aws:PrincipalArn": "arn:aws:iam::111122223333:role/service-role/AmazonSageMaker-ExecutionRole-ARN"
 }
 }
 },
 {
 "Sid": "DenyNonAWSEventSourcesForLambda",
 "Effect": "Deny",
 "Action": [
 "lambda:InvokeFunction"
 ],
 "Resource": "arn:aws:lambda:us-east-1:111122223333:function:ExampleFunction",
 "Condition": {
 "Null": {
 "lambda:EventSourceToken": false
 }
 }
 }
 ]
}`

```

7. Review the Lambda payload schema. The following table lists
   the Lambda request and response schema. You can validate your
   schema using the Nova custom evaluation SDK.

|               | Lambda Request Payload                                                                                                                                      | Lambda Response Payload                                                                                                                                                                                                          |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Preprocessor  | `<br>{<br>"process_type": "preprocess",<br>"data": {<br>"system": "You are a helpful assistant",<br>"prompt": "What is 2+2?",<br>"gold": "4"<br>}<br>}<br>` | `<br>{<br>"statusCode": 200,<br>"body": {<br>"system": "You are a helpful assistant that can substitute<br>• for addition",<br>"prompt": "What is 2*2?",<br>"gold": "4"<br>}<br>}<br>`                                           |
| Postprocessor | `<br>{<br>"process_type": "postprocess",<br>"data":  {<br>"prompt": "What is 2+2?",<br>"inference_output": "2+2=4",<br>"gold": "4"<br>}<br>}<br>`           | `<br>{<br>"statusCode": 200,<br>"body": [<br>{"metric": "accuracy", "value": 1.0},<br>{"metric": "f1_score", "value": 1.0},<br>{"metric": "exact_match", "value": 1},<br>{"metric": "length_ratio", "value": 0.8}<br>]<br>}<br>` |

8. Modify the recipe file. Here is an example.

```
processor:
  lambda_arn: arn:aws:lambda:us-east-1:111122223333:function:name
  lambda_type: "custom_metrics"
  preprocessing:
    enabled: true
  postprocessing:
    enabled: true
  aggregation: average
```

    * `lambda-arn`: The Amazon Resource Name
     (ARN) for your Lambda function that handles
     preprocessing and postprocessing.
    * `lambda_type`: "custom\_metrics" or "rft".
    * `preprocessing`: Whether to enable
     custom pre-processing operations.
    * `postprocessing`: Whether to enable
     custom post-processing operations.
    * `aggregation`: Built-in aggregation
     function (valid options: min, max, average,
     sum).

**Limitations**

- Bring your own metrics only applies to text input
  datasets.
- Multi-modal input datasets are not supported.
- The preprocessing step does not process the metadata
  field.

Nova LLM Judge is a model evaluation feature that enables you to
compare the quality of responses from one model against a baseline
model's responses using a custom dataset. It accepts a dataset
containing prompts, baseline responses, and challenger responses, then
uses a Nova Judge model to provide a win rate metric based on [Bradley-Terry](https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model "https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model") probability through pairwise comparisons.
Recipe format: `xxx_llm_judge_eval.yaml`.

**Nova LLM dataset requirements**

File format:

- Single `llm_judge.jsonl` file containing evaluation
  examples. The file name should be exact
  `llm_judge.jsonl`.
- Your must upload your dataset to an S3 location where SageMaker
  training jobs can access.
- The file must follow the required schema format for the
  `llm_judge` dataset.
- The input dataset should ensure all records are under 12 k
  context length.
  Schema format - Each line in the `.jsonl` file must be a
  JSON object with the following fields.

- Required fields.

`prompt`: String containing the prompt for the
generated response.

`response_A`: String containing the baseline
response.

`response_B`: String containing the alternative
response be compared with baseline response.
Example entry

```
{
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
}
```

To use your custom dataset, modify your evaluation recipe with the
following required fields, don't change any of the content:

```
evaluation:
  task: llm_judge
  strategy: judge
  metric: all
```

**Limitations**

- Only one `.jsonl` file is allowed per
  evaluation.
- The file must strictly follow the defined schema.
- Nova Judge models are the same across micro / lite / pro
  specifications.
- Custom judge models are not currently supported.

##### Nova LLM as a

Judge for multi-modal (image) benchmark recipes

Nova LLM Judge for multi-modal (image), short for Nova MM_LLM
Judge, is a model evaluation feature that enables you to compare the
quality of responses from one model against a baseline model's
responses using a custom dataset. It accepts a dataset containing
prompts, baseline responses, and challenger responses, and images in
thte form of Base64-encoded string, then uses a Nova Judge model to
provide a win rate metric based on [Bradley-Terry](https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model "https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model") probability through pairwise comparisons.
Recipe format: `xxx_mm_llm_judge_eval.yaml`.

**Nova LLM dataset
requirements**

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

Schema format - Each line in the `.jsonl` file must be
a JSON object with the following fields.

- Required fields.

`prompt`: String containing the prompt for the
generated response.

`images`: Array containing a list of objects
with data attributes (values are Base64-encoded image
strings).

`response_A`: String containing the baseline
response.

`response_B`: String containing the alternative
response be compared with baseline response.

Example entry

For readability, the following example includes new lines and
indentation, but in the actual dataset, each record should be on a
single line.

```
{
  "prompt": "What is in the image?",
  "images": [
    {
      "data": "data:image/jpeg;Base64,/9j/2wBDAAQDAwQDAwQEAwQFBAQFBgo..."
    }
  ],
  "response_A": "a dog.",
  "response_B": "a cat.",
}
{
  "prompt": "How many animals are in each of the images?",
  "images": [
    {
      "data": "data:image/jpeg;Base64,/9j/2wBDAAQDAwQDAwQEAwQFBAQFBgo..."
    },
    {
      "data": "data:image/jpeg;Base64,/DKEafe3gihn..."
    }
  ],
  "response_A": "The first image contains one cat and the second image contains one dog",
  "response_B": "The first image has one aminal and the second has one animal"
}
```

To use your custom dataset, modify your evaluation recipe with the
following required fields, don't change any of the content:

```
evaluation:
  task: mm_llm_judge
  strategy: judge
  metric: all
```

**Limitations**

- Only one `.jsonl` file is allowed per
  evaluation.
- The file must strictly follow the defined schema.
- Nova MM Judge models only support image reference.
- Nova MM Judge models are the same across Amazon Nova Micro,
  Amazon Nova Lite, and Amazon Nova Pro specifications.
- Custom judge models are not currently supported.
- Amazon S3 image URI is not supported.
- The input dataset should ensure all records are under 12 k
  context length, excluding images attribute.

## Running evaluation training

jobs

Start a training job using the following sample Jupyter notebook. Please refer to
below notebook as example to run the evaluation training job. For more information,
see [Use a SageMaker AI estimator to run a training job](docker-containers-adapt-your-own-private-registry-estimator.md "docker-containers-adapt-your-own-private-registry-estimator.md").

### Reference tables

Before running the notebook, refer to the following reference tables to select
image URI and instance configurations.

**Selecting image URI**

| Recipe               | Image URI                                                                                |
| -------------------- | ---------------------------------------------------------------------------------------- |
| Evaluation image URI | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-TJ-Eval-V2-latest` |

**Selecting instance type and count**

| Model             | Job type             | Instance type | Recommended instance count | Allowed instance count |
| ----------------- | -------------------- | ------------- | -------------------------- | ---------------------- |
| Amazon Nova Micro | Evaluation (SFT/DPO) | g5.12xlarge   | 1                          | 1<br>• 16              |
| Amazon Nova Lite  | Evaluation (SFT/DPO) | g5.12xlarge   | 1                          | 1<br>• 16              |
| Amazon Nova Pro   | Evaluation (SFT/DPO) | p5.48xlarge   | 1                          | 1<br>• 16              |

### Sample notebook

The following sample notebook demonstrates how to run an evaluation training
job.

```
# install python SDK

# Do not use sagemaker v3, as sagemaker v3 introduced breaking changes

!pip install sagemaker==2.254.1

import os
import sagemaker,boto3
from sagemaker.inputs import TrainingInput
from sagemaker.pytorch import PyTorch

sagemaker_session = sagemaker.Session()
role = sagemaker.get_execution_role()

# Download recipe from https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/evaluation/nova to local
# Assume the file name be `recipe.yaml`

# Populate parameters
# input_s3_uri = "`s3://<path>/input/`" # (Optional) Only used for multi-modal dataset or bring your own dataset s3 location
output_s3_uri= "`s3://<path>/output/`" # Output data s3 location, a zip containing metrics json and tensorboard metrics files will be stored to this location
instance_type = "`instance_type`"  # ml.g5.16xlarge as example
instance_count = 1 # The number of instances for inference (set `instance_count` > 1 for multi-node inference to accelerate evaluation)
job_name = "`your job name`"
recipe_path = "`recipe path`" # ./recipe.yaml as example
image_uri = "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-TJ-Eval-V2-latest" # Do not change

# (Optional) To bring your own dataset and LLM judge for evaluation
# evalInput = TrainingInput(
# s3_data=input_s3_uri,
# distribution='FullyReplicated',
# s3_data_type='S3Prefix'
#)

estimator = PyTorch(
    output_path=output_s3_uri,
    base_job_name=job_name,
    role=role,
    instance_type=instance_type,
    instance_count=instance_count,
    training_recipe=recipe_path,
    sagemaker_session=sagemaker_session,
    image_uri=image_uri
)
estimator.fit()

# If input dataset exist, pass in inputs
# estimator.fit(inputs={"train": evalInput})
```

## Assessing and analyzing evaluation

results

After your evaluation job completes successfully, you can assess and analyze the
results using the following steps.

###### To assess and analyze the results, following these steps.

1. Understand the output location structure. Results are stored in your
   specified Amazon S3 output location as a compressed file:

```
s3:`//your-bucket/output/benchmark-name/`
└── job_name/
    └── output/
        └── output.tar.gz
```

2. Download the `output.tar.gz` file from your bucket. Extract the
   contents to reveal.

```
run_name/
├── eval_results/
|   └── results_[timestamp].json
│   └── inference_output.jsonl (only present for gen_qa)
|   └── details/
|         └── model/
|              └── <execution-date-time>/
|                    └──details_<task_name>_#_<datetime>.parquet
└── tensorboard_results/
    └── eval/
        └── events.out.tfevents.[timestamp]
```

    * `results_[timestamp].json` - Output metrics JSON
     file
    * `details_<task_name>_#_<datetime>.parquet` -
     Inference output file (except for `strong_reject`)
    * `events.out.tfevents.[timestamp]` - TensorBoard output
     file
    * `inference_output.jsonl` - Cleaned inference output
     file (only for `gen_qa` tasks)

3.  View results in TensorBoard. To visualize your evaluation metrics:
    1. Upload the extracted folder to an S3 bucket
    2. Navigate to SageMaker TensorBoard
    3. Select your "S3 folders"
    4. Add the S3 folder path
    5. Wait for synchronization to complete

4.  Analyze inference outputs. All evaluation tasks, except
    `llm_judge` and `strong_reject`, will have the
    following fields for analysis in the inference output.

        * `full_prompt` - The full user prompt sent to the model
         used for the evaluation task.
        * `gold` - The field that contains the correct answer(s)
         as specified by the dataset.
        * `metrics` - The field that contains the metrics
         evaluated on the individual inference. Values that require
         aggregation would not have a value on the individual inference
         outputs.
        * `predictions` - The field that contains a list of the
         model’s output for the given prompt.
        * `pred_logits` - The field that contains the considered
         output tokens and log probabilities of each output token returned in
         the message content.

    By looking at these fields, you can determine the cause for metric
    differences and understand the behavior of the customized models.

For `llm_judge`, the inference output file contains the
following fields under the metrics field per pair of evaluations.

    * `forward_output` - Judge's raw preferences when
     evaluating in order (response\_A, response\_B).
    * `backward_output` - Judge's raw preferences when
     evaluating in reverse order (response\_B, response\_A).
    * `Pairwise metrics` - Metrics that are calculated per
     pair of forward and backward evaluation including
     `a_scores`, `b_scores`, `ties`,
     `inference-score` and `score`.


    ###### Note

    Aggregate metrics like `winrate` are only available
     in the summary results files, not per individual
     judgement.

For `gen_qa`, the `inference_output.jsonl` file
contains the following fields for each JSON object:

    * prompt - The final prompt submitted to the model
    * inference - The raw inference output from the model
    * gold - The target response from the input dataset
    * metadata - The metadata string from the input dataset if
     provided

## Evaluation best practices and

troubleshooting

### Best practices

The following lists some best practices for the evaluation process.

- Keep your output paths organized by model and benchmark type.
- Maintain consistent naming conventions for easy tracking.
- Save extracted results in a secure location.
- Monitor TensorBoard sync status for successful data loading.

### Troubleshooting

You can use CloudWatch log group `/aws/sagemaker/TrainingJobs` for
training job error logs.

#### Engine core Failure

**Issue**:

If you are seeing:

```
RuntimeError: Engine core initialization failed.
```

**Cause**:

Although this is a general error that can have multiple causes, it
typically occurs when there is a mismatch between the model checkpoint
you're trying to load and the model type specified. E.g. you want to
evaluate a fine-tuned Nova 2.0 lite model checkpoint but the model type you
provide is 1.0 model type. e.g. `amazon.nova-micro-v1:0:128k`

The correct mapping should be

```
model_type: amazon.nova-2-lite-v1:0:256k
model_name_or_path: nova-lite-2/prod # or s3://escrow_bucket/model_location
```

**Prevention**:

Double check the `model_name_or_path` is mapped to the right `model_type` before submitting the evaluation job.

## Available subtasks

The following lists available subtasks for model evaluation across multiple
domains including MMLU (Massive Multitask Language Understanding), BBH (Big Bench
Hard), and MATH. These subtasks allow you to assess your model's performance on
specific capabilities and knowledge areas.

**MMLU**

```
MMLU_SUBTASKS = [
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
]
```

**BBH**

```
BBH_SUBTASKS = [
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
]
```

**Math**

```
MATH_SUBTASKS = [
    "algebra",
    "counting_and_probability",
    "geometry",
    "intermediate_algebra",
    "number_theory",
    "prealgebra",
    "precalculus",
```

Evaluate your customized Nova models using various evaluation methods and
metrics.

###### In this section:

- [Rubric Based Judge](nova-rubric-judge-evaluation.md "nova-rubric-judge-evaluation.md")
- [Reasoning model evaluation](nova-reasoning-model-evaluation.md "nova-reasoning-model-evaluation.md")
- [RFT evaluation](nova-rft-evaluation.md "nova-rft-evaluation.md")
- [Implementing reward functions](nova-implementing-reward-functions.md "nova-implementing-reward-functions.md")
- [Running evaluations and interpreting results](nova-running-evaluations.md "nova-running-evaluations.md")
