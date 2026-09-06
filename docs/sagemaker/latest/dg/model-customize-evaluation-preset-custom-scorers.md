

# Evaluate with Preset and Custom Scorers
<a name="model-customize-evaluation-preset-custom-scorers"></a>

When using the Custom Scorer evaluation type, SageMaker Evaluation supports two built-in scorers (also referred to as "reward functions") Prime Math and Prime Code taken from the [volcengine/verl](https://github.com/volcengine/verl) RL training library, or your own custom scorer implemented as a Lambda Function.

## Built-in Scorers
<a name="model-customize-evaluation-builtin-scorers"></a>

**Prime Math**

The prime math scorer expects a custom JSONL dataset of entries containing a math question as the prompt/query and the correct answer as ground truth. The dataset can be any of the supported formats mentioned in [Supported Dataset Formats for Bring-Your-Own-Dataset (BYOD) Tasks](model-customize-evaluation-dataset-formats.md).

Example dataset entry (expanded for clarity):

```
{
    "system":"You are a math expert: ",
    "query":"How many vertical asymptotes does the graph of $y=\\frac{2}{x^2+x-6}$ have?",
    "response":"2" # Ground truth aka correct answer
}
```

**Prime Code**

The prime code scorer expects a custom JSONL dataset of entries containing a coding problem and test cases specified in the `metadata` field. Structure the test cases with the expected function name for each entry, sample inputs, and expected outputs.

Example dataset entry (expanded for clarity):

```
{
    "system":"\\nWhen tackling complex reasoning tasks, you have access to the following actions. Use them as needed to progress through your thought process.\\n\\n[ASSESS]\\n\\n[ADVANCE]\\n\\n[VERIFY]\\n\\n[SIMPLIFY]\\n\\n[SYNTHESIZE]\\n\\n[PIVOT]\\n\\n[OUTPUT]\\n\\nYou should strictly follow the format below:\\n\\n[ACTION NAME]\\n\\n# Your action step 1\\n\\n# Your action step 2\\n\\n# Your action step 3\\n\\n...\\n\\nNext action: [NEXT ACTION NAME]\\n\\n",
    "query":"A number N is called a factorial number if it is the factorial of a positive integer. For example, the first few factorial numbers are 1, 2, 6, 24, 120,\\nGiven a number N, the task is to return the list/vector of the factorial numbers smaller than or equal to N.\\nExample 1:\\nInput: N = 3\\nOutput: 1 2\\nExplanation: The first factorial number is \\n1 which is less than equal to N. The second \\nnumber is 2 which is less than equal to N,\\nbut the third factorial number is 6 which \\nis greater than N. So we print only 1 and 2.\\nExample 2:\\nInput: N = 6\\nOutput: 1 2 6\\nExplanation: The first three factorial \\nnumbers are less than equal to N but \\nthe fourth factorial number 24 is \\ngreater than N. So we print only first \\nthree factorial numbers.\\nYour Task:  \\nYou don't need to read input or print anything. Your task is to complete the function factorialNumbers() which takes an integer N as an input parameter and return the list/vector of the factorial numbers smaller than or equal to N.\\nExpected Time Complexity: O(K), Where K is the number of factorial numbers.\\nExpected Auxiliary Space: O(1)\\nConstraints:\\n1<=N<=10^{18}\\n\\nWrite Python code to solve the problem. Present the code in \\n```python\\nYour code\\n```\\nat the end.",
    "response": "", # Dummy string for ground truth. Provide a value if you want NLP metrics like ROUGE, BLEU, and F1.
    ### Define test cases in metadata field
    "metadata": {
        "fn_name": "factorialNumbers",
        "inputs": ["5"],
        "outputs": ["[1, 2]"]
    }
}
```

## Custom Scorers (Bring Your Own Metrics)
<a name="model-customize-evaluation-custom-scorers-byom"></a>

Fully customize your model evaluation workflow with custom post-processing logic which allows you to compute custom metrics tailored to your needs. You must implement your custom scorer as an AWS Lambda function that accepts model responses and returns reward scores.

### Sample Lambda Input Payload
<a name="model-customize-evaluation-custom-scorers-lambda-input"></a>

The payload your custom scorer AWS Lambda function receives mirrors the format of your evaluation dataset. SageMaker AI detects your dataset format and sends each sample to your Lambda in the corresponding shape, with the model's generated answer appended. Your Lambda must read the response from the fields that match the dataset format you are using.

The container invokes your Lambda once per sample, passing a list that contains a single sample object. Your Lambda must iterate the list, but currently it contains exactly one item per invocation. The following sections show the payload your Lambda receives for each supported dataset format.

#### OpenAI Chat format
<a name="model-customize-evaluation-custom-scorers-lambda-input-openai"></a>

```
[
  {
    "id": "123",
    "messages": [
      { "role": "system", "content": "You are helpful." },
      { "role": "user", "content": "What is the capital of France?" },
      { "role": "assistant", "content": "Paris" },
      { "role": "assistant", "content": "The capital of France is Paris." }
    ],
    "reference_answer": { "text": "Paris" }
  }
]
```

Notes on the OpenAI payload:
+ The model's answer is the last `assistant` message. The container appends the model response as a new assistant turn.
+ If your dataset already ends with an assistant message (the ground-truth turn), the payload contains two trailing assistant messages—the original ground-truth turn followed by the model's response.
+ The ground truth is also provided at top-level `reference_answer.text` (the runtime-normalized copy).
+ `id` is a container-generated identifier (present for this format).

#### verl format
<a name="model-customize-evaluation-custom-scorers-lambda-input-verl"></a>

```
[
  {
    "data_source": "openai/gsm8k",
    "prompt": [
      { "role": "user", "content": "What is the capital of France?" },
      { "role": "assistant", "content": "The capital of France is Paris." }
    ],
    "response": "The capital of France is Paris.",
    "reward_model": { "style": "rule", "ground_truth": "Paris" },
    "extra_info": {
      "reference_answer": { "text": "Paris" },
      "processor_config": { "aggregation": "mean" }
    }
  }
]
```

Notes on the verl payload:
+ The model's answer is in `response` (and also appended as the final `assistant` turn in `prompt`).
+ Ground truth is always emitted at `extra_info.reference_answer.text`. It is `{"text": ""}` when the dataset provides no ground truth. Read ground truth from this field.
+ `data_source` defaults to `"customized"` when the dataset entry doesn't set it.
+ `reward_model` and other verl-specific fields (`id`, `ability`, `attributes`, `difficulty`) are passed through only if present in the dataset entry. They are not added by default.

#### Hugging Face Prompt-Completion format
<a name="model-customize-evaluation-custom-scorers-lambda-input-hf-prompt"></a>

```
[
  {
    "id": "123",
    "prompt": "What is the capital of France?",
    "completion": "The capital of France is Paris.",
    "reference_answer": { "text": "Paris" }
  }
]
```

Notes on the Hugging Face Prompt-Completion payload:
+ The model's answer is in `completion` (the container overwrites the dataset's original completion with the model response).
+ Ground truth is at `reference_answer.text` (the dataset's original completion).

#### Hugging Face Preference format
<a name="model-customize-evaluation-custom-scorers-lambda-input-hf-preference"></a>

```
[
  {
    "id": "123",
    "prompt": "What is the capital of France?",
    "completion": "The capital of France is Paris.",
    "chosen": "Paris",
    "rejected": "London",
    "reference_answer": { "text": "Paris" }
  }
]
```

Notes on the Hugging Face Preference payload:
+ The model's answer is in `completion`.
+ The original `chosen` and `rejected` preference pair is passed through.
+ Ground truth is at `reference_answer.text` (resolved from `chosen`).

#### SageMaker AI Evaluation format
<a name="model-customize-evaluation-custom-scorers-lambda-input-sm-eval"></a>

```
[
  {
    "id": "123",
    "model_response": "The capital of France is Paris.",
    "query": "What is the capital of France?",
    "response": "Paris",
    "system": "You are a helpful assistant.",
    "reference_answer": { "text": "Paris" }
  }
]
```

Notes on the SageMaker AI Evaluation payload:
+ The model's answer is in `model_response`. All original dataset fields are passed through unchanged (`query`, `response`, `system`, `category`, and `metadata`).
+ The ground truth appears in two top-level fields with the same value: the original `response`, and `reference_answer.text`. Read either.

**Note**  
These are the payloads your Lambda receives. SageMaker AI takes each entry from your evaluation dataset, appends the model's generated response, and sends it to your scorer. See [Supported Dataset Formats for Bring-Your-Own-Dataset (BYOD) Tasks](model-customize-evaluation-dataset-formats.md) for how to author each dataset format. Write your Lambda to parse the fields of the format your dataset uses.

### Sample Lambda Output Payload
<a name="model-customize-evaluation-custom-scorers-lambda-output"></a>

Your AWS Lambda function must return one result object per input sample. The SageMaker AI eval container accepts either of two response envelopes:

#### Option A – Raw list (recommended)
<a name="model-customize-evaluation-custom-scorers-lambda-output-raw"></a>

```
[
  {
    "id": "123",
    "aggregate_reward_score": 0.85,
    "metrics_list": [
      { "name": "factual_accuracy", "value": 0.9, "type": "Reward" },
      { "name": "format_compliance", "value": 0.8, "type": "Metric" }
    ]
  }
]
```

#### Option B – API Gateway-style wrapper
<a name="model-customize-evaluation-custom-scorers-lambda-output-wrapped"></a>

In this format, `body` is the JSON-encoded string of the result list. This is the format emitted by the Studio "Create Reward Function" template.

```
{
  "statusCode": 200,
  "body": "[{\"id\": \"123\", \"aggregate_reward_score\": 0.85, \"metrics_list\": [...]}]"
}
```

The following notes apply to both response envelopes:
+ In Option B, `body` must be a JSON string (not a nested JSON object), and `statusCode` must be `200`. A non-200 status causes the eval container to treat that sample as a failure: it is counted in `byoc_failure_count` and its custom metrics are dropped, but the overall evaluation job still completes.
+ `metrics_list` is optional; when present, each entry must include `name`, `value`, and `type` (`"Reward"` or `"Metric"`).
+ Each result's `id` must match the input sample's `id`.

### Custom Lambda Definition
<a name="model-customize-evaluation-custom-scorers-lambda-definition"></a>

Find an example of a fully-implemented custom scorer with sample input and expected output at: [https://docs.aws.amazon.com/sagemaker/latest/dg/nova-implementing-reward-functions.html\#nova-reward-llm-judge-example](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-implementing-reward-functions.html#nova-reward-llm-judge-example)

Use the following skeleton as a starting point for your own function.

```
def lambda_handler(event, context):
    return lambda_grader(event)

def lambda_grader(samples: list[dict]) -> list[dict]:
    """
    Args:
        Samples: List of dictionaries; each sample's shape mirrors your evaluation dataset format
            (OpenAI, verl, Hugging Face Prompt-Completion, Hugging Face Preference, or SageMaker Evaluation).
            See the Sample Lambda Input Payload section above for the per-format shape.
            
        # Example shown is the OpenAI format; other dataset formats use different fields.
        Example input:
        {
            "id": "123",
            "messages": [
                {
                    "role": "user",
                    "content": "Do you have a dedicated security team?"
                },
                {
                    "role": "assistant",
                    "content": "As an AI developed by Company, I do not have a dedicated security team..."
                }
            ],
            # reference_answer contents vary by dataset; reference_answer.text holds the normalized ground truth
            "reference_answer": {
                "text": "No, as an AI developed by Company, I do not have a dedicated security team."
            }
        }
        
    Returns:
        List of dictionaries with reward scores:
        {
            "id": str,                              # Same id as input sample
            "aggregate_reward_score": float,        # Overall score for the sample
            "metrics_list": [                       # OPTIONAL: Component scores
                {
                    "name": str,                    # Name of the component score
                    "value": float,                 # Value of the component score
                    "type": str                     # "Reward" or "Metric"
                }
            ]
        }
    """
```

### Input and output fields
<a name="model-customize-evaluation-custom-scorers-fields"></a>

**Input fields**


| Field | Description | Additional notes | 
| --- | --- | --- | 
| id | Unique identifier for the sample | Echoed back in output. String. Present for the OpenAI, Hugging Face, and SageMaker AI Evaluation formats; for verl it appears only if set in the dataset entry. | 
| reference\_answer.text | Normalized ground truth for the sample | Present in every format (top-level for most; under extra\_info for verl). Value is "" when the dataset provides no ground truth. Read ground truth from this field. | 
| messages | Ordered chat history (OpenAI-format datasets only) | Array of message objects. The model's response is the last assistant message. | 
| messages[].role | Speaker of the message | Common values: "user", "assistant", "system" | 
| messages[].content | Text content of the message | Plain string | 
| prompt | Input prompt (Hugging Face formats: string; verl: chat array) | For verl, the model response is also appended as the final assistant turn. | 
| completion | Model's response (Hugging Face Prompt-Completion and Preference formats) | The container overwrites the dataset's original completion with the model response. | 
| chosen or rejected | Preferred and rejected responses (Hugging Face Preference format) | Passed through from the dataset. Ground truth resolves from chosen. | 
| response | Model's response (verl) / ground-truth response (SageMaker AI Evaluation) | In SageMaker AI Evaluation this holds the original ground truth (same value as reference\_answer.text). | 
| model\_response | Model's generated response (SageMaker AI Evaluation format) | String | 
| data\_source, reward\_model, extra\_info | verl-specific fields | data\_source defaults to "customized." reward\_model and other verl fields are passed through only if present in the dataset entry. | 
| metadata | Free-form information to aid grading | Object; optional fields passed through from your dataset | 

**Output fields**


**Output Fields**  

| Field | Description | Additional notes | 
| --- | --- | --- | 
| id | Same identifier as input sample | Must match input | 
| aggregate\_reward\_score | Overall score for the sample | Float (e.g., 0.0–1.0 or task-defined range) | 
| metrics\_list | Component scores that make up the aggregate | Array of metric objects | 

### Required Permissions
<a name="model-customize-evaluation-custom-scorers-permissions"></a>

Ensure that the SageMaker execution role you use to run evaluation has AWS Lambda permissions.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "lambda:InvokeFunction"
            ],
            "Resource": "arn:aws:lambda:region:account-id:function:function-name"
        }
    ]
}
```

Ensure your AWS Lambda Function's execution role has basic Lambda execution permissions, as well as additional permissions you may require for any downstream AWS calls.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    }
  ]
}
```