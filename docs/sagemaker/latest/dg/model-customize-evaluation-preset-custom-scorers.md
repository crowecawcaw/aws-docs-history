# Evaluate with Preset and Custom Scorers

When using the Custom Scorer evaluation type, SageMaker Evaluation supports two built-in scorers (also referred to as "reward functions") Prime Math and Prime Code taken from the [volcengine/verl](https://github.com/volcengine/verl "https://github.com/volcengine/verl") RL training library, or your own custom scorer implemented as a Lambda Function.

## Built-in Scorers

**Prime Math**

The prime math scorer expects a custom JSONL dataset of entries containing a math question as the prompt/query and the correct answer as ground truth. The dataset can be any of the supported formats mentioned in [Supported Dataset Formats for Bring-Your-Own-Dataset (BYOD) Tasks](model-customize-evaluation-dataset-formats.md "model-customize-evaluation-dataset-formats.md").

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

````
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
````

## Custom Scorers (Bring Your Own Metrics)

Fully customize your model evaluation workflow with custom post-processing logic which allows you to compute custom metrics tailored to your needs. You must implement your custom scorer as an AWS Lambda function that accepts model responses and returns reward scores.

### Sample Lambda Input Payload

Your custom AWS Lambda expects inputs in the OpenAI format. Example:

```
{
    "id": "123",
    "messages": [
        {
            "role": "user",
            "content": "Do you have a dedicated security team?"
        },
        {
            "role": "assistant",
            "content": "As an AI developed by Amazon, I do not have a dedicated security team..."
        }
    ],
    "reference_answer": {
        "compliant": "No",
        "explanation": "As an AI developed by Company, I do not have a traditional security team..."
    }
}
```

### Sample Lambda Output Payload

The SageMaker evaluation container expects your Lambda responses to follow this format:

```
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
```

### Custom Lambda Definition

Find an example of a fully-implemented custom scorer with sample input and expected output at: [https://docs.aws.amazon.com/sagemaker/latest/dg/nova-implementing-reward-functions.html#nova-reward-llm-judge-example](nova-implementing-reward-functions.md#nova-reward-llm-judge-example "nova-implementing-reward-functions.md#nova-reward-llm-judge-example")

Use the following skeleton as a starting point for your own function.

```
def lambda_handler(event, context):
    return lambda_grader(event)

def lambda_grader(samples: list[dict]) -> list[dict]:
    """
    Args:
        Samples: List of dictionaries in OpenAI format

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
            # This section is the same as your training dataset
            "reference_answer": {
                "compliant": "No",
                "explanation": "As an AI developed by Company, I do not have a traditional security team..."
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

**Input fields**

| Field              | Description                           | Additional notes                                  |
| ------------------ | ------------------------------------- | ------------------------------------------------- |
| id                 | Unique identifier for the sample      | Echoed back in output. String format              |
| messages           | Ordered chat history in OpenAI format | Array of message objects                          |
| messages[].role    | Speaker of the message                | Common values: "user", "assistant", "system"      |
| messages[].content | Text content of the message           | Plain string                                      |
| metadata           | Free-form information to aid grading  | Object; optional fields passed from training data |

**Output fields**

Output Fields| Field | Description | Additional notes |
| --- | --- | --- |
| id | Same identifier as input sample | Must match input |
| aggregate\_reward\_score | Overall score for the sample | Float (e.g., 0.0–1.0 or task-defined range) |
| metrics\_list | Component scores that make up the aggregate | Array of metric objects |

### Required Permissions

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
