

# Preparing data for RFT on Amazon Nova 2
<a name="nova-data-prep-rft-2"></a>

RFT on Amazon Nova 2 currently supports text-based training data. This page describes the data format, supported features, constraints, and best practices for preparing RFT training data for Amazon Nova 2 Understanding models.

**Tip**  
To validate your dataset format before starting a training job, see [Validation tools](nova-data-preparation.md#nova-data-validation-tools).

**Topics**
+ [Data format](#nova-2-rft-data-overview)
+ [Sample inputs](#nova-2-rft-data-examples)
+ [Supported features](#nova-2-rft-supported-features)
+ [General/Text understanding](#rft-general-constraints)
+ [Tool calling](#rft-tool-calling)
+ [Reasoning](#rft-reasoning)
+ [Characteristics of effective training data](#nova-rft-effective-data)
+ [RFT training using LLM as a judge](#nova-rft-llm-judge)

## Data format
<a name="nova-2-rft-data-overview"></a>

RFT training data follows the OpenAI Reinforcement Fine-Tuning [format](https://developers.openai.com/api/docs/guides/reinforcement-fine-tuning#prepare-your-dataset). Each line in your JSONL training file is a JSON object with the following top-level fields. Expand a section to learn more:

### messages
<a name="rft-field-messages"></a>

Required. An array of conversational turns using `system`, `user`, and optionally `assistant` roles.
+ **role** – Required. Common values: `system` (instructions for the model) and `user` (the task or input).
+ **content** – Required. The text content of the message. For system turns this is instructions; for user turns this is the task or input.

```
"messages": [
    {
        "role": "system",
        "content": "{{instructions}}"
    },
    {
        "role": "user",
        "content": "{{prompt}}"
    }
]
```

### reference\_answer
<a name="rft-field-reference-answer"></a>

Required. The expected output or evaluation criteria that your reward function uses to score the model's response. This field is not limited to structured outputs — it can contain any format that helps your reward function evaluate quality.

```
"reference_answer": {
    "{{field}}": "{{value}}"
}
```

### tools (optional)
<a name="rft-field-tools"></a>

Optional. An array of tool specifications available to the model during this example. Each item defines a tool's interface and metadata. For a complete example, see [Tool calling](#rft-tool-calling).

```
"tools": [
    {
        "type": "function",
        "function": {
            "name": "{{tool-name}}",
            "description": "{{tool-description}}",
            "parameters": { {{...}} }
        }
    }
]
```

### Additional properties (optional)
<a name="rft-field-additional-properties"></a>

The RFT data format supports custom fields beyond `messages` and `reference_answer`. Include any additional data your reward function needs for proper evaluation. You don't need to configure these in your recipe — they are passed to your reward function in the `metadata` field at runtime.

Common examples include:

**Metadata**
+ `id` – Unique identifier for tracking
+ `task_id` – Task-level identifier
+ `difficulty_level` – Problem complexity indicator
+ `domain` – Subject area or category
+ `expected_reasoning_steps` – Number of steps in solution

**Evaluation criteria**
+ `evaluation_criteria` – Specific grading rubrics
+ `custom_scoring_weights` – Relative importance of different aspects
+ `context_data` – Background information for the problem
+ `external_references` – Links to relevant documentation or resources

**Validating your data**

Before submitting your training job, validate your dataset to catch formatting issues early. For available validation tools, see [Validation tools](nova-data-preparation.md#nova-data-validation-tools).

## Sample inputs
<a name="nova-2-rft-data-examples"></a>

The following are complete example JSON objects showing how to combine the fields for different RFT use cases.

------
#### [ Chemistry problem ]

```
{
    "id": "chem-01",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful chemistry assistant"
        },
        {
            "role": "user",
            "content": "Calculate the molecular weight of caffeine (C8H10N4O2)"
        }
    ],
    "reference_answer": {
        "molecular_weight": 194.19,
        "unit": "g/mol",
        "calculation": "8(12.01) + 10(1.008) + 4(14.01) + 2(16.00) = 194.19"
    }
}
```

------
#### [ Math problem ]

```
{
    "id": "math-001",
    "messages": [
        {
            "role": "system",
            "content": "You are a math tutor"
        },
        {
            "role": "user",
            "content": "Solve: 2x + 5 = 13"
        }
    ],
    "reference_answer": {
        "solution": "x = 4",
        "steps": ["2x = 13 - 5", "2x = 8", "x = 4"]
    }
}
```

------
#### [ Code problem ]

```
{
    "id": "code-002",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful programming assistant"
        },
        {
            "role": "user",
            "content": "Write a Python function that reverses a string without using built-in reverse methods"
        }
    ],
    "reference_answer": {
        "code": "def reverse_string(s):\n    result = ''\n    for i in range(len(s) - 1, -1, -1):\n        result += s[i]\n    return result",
        "test_cases": [
            {
                "input": "hello",
                "expected_output": "olleh"
            },
            {
                "input": "",
                "expected_output": ""
            },
            {
                "input": "a",
                "expected_output": "a"
            },
            {
                "input": "Python123",
                "expected_output": "321nohtyP"
            }
        ],
        "all_tests_pass": true
    }
}
```

------
#### [ Tool usage ]

```
{
    "id": "tool-001",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful game master assistant"
        },
        {
            "role": "user",
            "content": "Generate a strength stat for a warrior character. Apply a +2 racial bonus modifier."
        }
    ],
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "StatRollAPI",
                "description": "Generates character stats by rolling 4d6, dropping the lowest die result, and applying a modifier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "modifier": {
                            "description": "An integer representing the modifier to apply to the total of the stat roll.",
                            "type": "integer"
                        }
                    },
                    "required": ["modifier"]
                }
            }
        }
    ],
    "reference_answer": {
        "tool_called": "StatRollAPI",
        "tool_parameters": {
            "modifier": 2
        },
        "expected_behavior": "Call StatRollAPI with modifier=2 and return the calculated stat value"
    }
}
```

------
#### [ With additional properties ]

The following example includes custom metadata fields that are passed to your reward function during evaluation, enabling sophisticated scoring logic tailored to your specific use case.

```
{
    "messages": [
        {
            "role": "system",
            "content": "You are a math tutor"
        },
        {
            "role": "user",
            "content": "Solve: 2x + 5 = 13"
        }
    ],
    "reference_answer": {
        "solution": "x = 4",
        "steps": ["2x = 13 - 5", "2x = 8", "x = 4"]
    },
    "task_id": "algebra_001",
    "difficulty_level": "easy",
    "domain": "algebra",
    "expected_reasoning_steps": 3
}
```

------

## Supported features
<a name="nova-2-rft-supported-features"></a>

The following table summarizes feature support for RFT on Amazon Nova 2.


**RFT feature support**  

| Feature | RFT on Amazon Nova 2 | 
| --- | --- | 
| Text understanding | Supported on Nova 2.0 Lite. See [General/Text understanding](#rft-general-constraints). | 
| Image understanding | Not supported | 
| Video understanding | Not supported | 
| Document understanding | Not supported | 
| Tool calling | Supported on Nova 2.0 Lite. See [Tool calling](#rft-tool-calling). | 
| Reasoning | Supported on Nova 2.0 Lite. See [Reasoning](#rft-reasoning). | 

## General/Text understanding
<a name="rft-general-constraints"></a>

This section summarizes the general constraints and best practices for preparing RFT on Amazon Nova 2 training data.

**Constraints**


**General dataset constraints**  

| Constraint | Details | 
| --- | --- | 
| Dataset format | JSONL (one JSON object per line). | 
| Minimum training examples | 100 | 
| Minimum evaluation examples | 100 | 
| Supported modalities | Text only | 

**Best practices**
+ We recommend starting with the minimum dataset sizes (100 training and 100 evaluation examples) and scaling up after you have validated your reward function and confirmed RFT is appropriate for your use case.
+ We recommend an evaluation-first approach. Before investing in large-scale RFT training, evaluate your model's baseline performance:
  + **High performance (>95% reward)** – RFT may be unnecessary because your model already performs well.
  + **Very poor performance (0% reward)** – Switch to SFT first to establish basic capabilities.
  + **Moderate performance** – RFT is likely appropriate.
+ Starting with a small dataset helps you validate that your reward function is bug-free, confirm RFT is the right approach, identify and fix issues early, and test the workflow before scaling up.
+ Prioritize high-quality input data and a reliable reward function that executes consistently on model responses.

**Sample input**

### Text-only sample
<a name="rft-general-sample"></a>

```
{
    "id": "math-001",
    "messages": [
        {
            "role": "system",
            "content": "You are a math tutor"
        },
        {
            "role": "user",
            "content": "Solve: 2x + 5 = 13"
        }
    ],
    "reference_answer": {
        "solution": "x = 4",
        "steps": ["2x = 13 - 5", "2x = 8", "x = 4"]
    }
}
```

## Tool calling
<a name="rft-tool-calling"></a>

RFT supports training models on tool calling patterns, enabling your model to learn when and how to invoke external tools or functions.

**Constraints**


**Tool calling constraints**  

| Constraint | Details | 
| --- | --- | 
| Tool definition location | Tools are declared in the top-level tools array of the training example. | 
| Tool definition format | Each tool must include type, function.name, function.description, and a valid JSON Schema in function.parameters. | 
| Reference answer | Use reference\_answer to specify the expected tool invocation (for example, tool\_called, tool\_parameters) so your reward function can evaluate correctness. | 

**Best practices**
+ Ensure your tool definitions are consistent across all training samples.
+ The model learns tool invocation patterns from the demonstrations you provide.
+ Include diverse examples of when to use each tool and when not to use tools.

**Sample input**

### Tool usage sample
<a name="rft-tool-sample"></a>

```
{
    "id": "tool-001",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful game master assistant"
        },
        {
            "role": "user",
            "content": "Generate a strength stat for a warrior character. Apply a +2 racial bonus modifier."
        }
    ],
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "StatRollAPI",
                "description": "Generates character stats by rolling 4d6, dropping the lowest die result, and applying a modifier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "modifier": {
                            "description": "An integer representing the modifier to apply to the total of the stat roll.",
                            "type": "integer"
                        }
                    },
                    "required": ["modifier"]
                }
            }
        }
    ],
    "reference_answer": {
        "tool_called": "StatRollAPI",
        "tool_parameters": {
            "modifier": 2
        },
        "expected_behavior": "Call StatRollAPI with modifier=2 and return the calculated stat value"
    }
}
```

## Reasoning
<a name="rft-reasoning"></a>

RFT on Amazon Nova 2 supports reasoning mode, where the model generates explicit thinking tokens before producing a final answer. You control reasoning behavior during training with the `reasoning_effort` training configuration field.

**Constraints**


**Reasoning constraints**  

| Constraint | Details | 
| --- | --- | 
| Available modes | none (omit the reasoning\_effort field), low, and high. There is no medium option for RFT. | 
| Default behavior | If the reasoning\_effort field is absent from your configuration, reasoning is disabled. | 
| Token limit | When reasoning is enabled, set max\_new\_tokens to 32768 to accommodate extended reasoning outputs. | 

**When to use each mode**

Use `high` reasoning for:
+ Complex analytical tasks
+ Mathematical problem-solving
+ Multi-step logical deduction
+ Tasks where step-by-step thinking adds value

Use `none` (omit `reasoning_effort`) or `low` reasoning for:
+ Simple factual queries
+ Direct classifications
+ Speed and cost optimization
+ Straightforward question-answering

**Cost and performance trade-offs**

Higher reasoning modes increase:
+ Training time and cost
+ Inference latency and cost
+ Model capability for complex reasoning tasks

## Characteristics of effective training data
<a name="nova-rft-effective-data"></a>

**Clarity and consistency**

Good RFT examples require clear, unambiguous input data that enables accurate reward calculation across different model outputs. Avoid noise in your data, including:
+ Inconsistent formatting
+ Contradictory labels or instructions
+ Ambiguous prompts
+ Conflicting reference answers

Any ambiguity will mislead the training process and cause the model to learn unintended behaviors.

**Diversity**

Your dataset should capture the full diversity of production use cases to ensure robust real-world performance. Include:
+ Different input formats and edge cases
+ Map actual production usage patterns from logs and user analytics
+ Sample across user types, geographic regions, and seasonal variations
+ Include difficulty levels from simple to complex problems

**Reward function considerations**

Design your reward function for efficient training:
+ Execute within seconds (not minutes)
+ Parallelize effectively with Lambda
+ Return consistent, reliable scores
+ Handle different types of model outputs gracefully

Fast, scalable reward functions enable rapid iteration and cost-effective experimentation.

## RFT training using LLM as a judge
<a name="nova-rft-llm-judge"></a>

### Overview
<a name="nova-rft-llm-judge-overview"></a>

Large language models (LLMs) are increasingly being used as judges in reinforcement fine-tuning (RFT) workflows, providing automated reward signals that guide model optimization. In this approach, an LLM evaluates model outputs against specified criteria—whether assessing correctness, quality, style adherence, or semantic equivalence—and assigns rewards that drive the reinforcement learning process.

This is particularly valuable for tasks where traditional reward functions are difficult to define programmatically, such as determining whether different representations (like "1/3", "0.333", and "one-third") are semantically equivalent, or evaluating nuanced qualities like coherence and relevance. By using LLM-based judges as reward functions, you can scale RFT to complex domains without requiring extensive human annotation, enabling rapid iteration and continuous improvement of your models across diverse use cases beyond traditional alignment problems.

### Validating your LLM judge
<a name="nova-rft-validating-judge"></a>

Before deploying an LLM-as-a-judge in production, validate that the judge model's evaluations align with human judgment. This involves:
+ Measuring agreement rates between the LLM judge and human evaluators on representative samples of your task
+ Ensuring that the LLM's agreement with humans meets or exceeds inter-human agreement rates
+ Identifying potential biases in the judge model
+ Building confidence that the reward signal guides your model in the intended direction

This validation step helps ensure the automated evaluation process will produce models that meet your production quality criteria.

### Lambda configuration for LLM judge
<a name="nova-rft-lambda-config"></a>

Using an LLM as a judge is an extension of using Lambda functions for Reinforcement Learning with Verifiable Rewards (RLVR). Inside the Lambda function, you make a call to one of the models hosted in Amazon Bedrock.

**Important configuration requirements:**


| Configuration | Requirement | Details | 
| --- | --- | --- | 
| Amazon Bedrock throughput | Sufficient quota | Ensure your throughput quota for the Amazon Bedrock model used is sufficient for your training workload | 
| Lambda timeout | Extended timeout | Configure your Lambda function timeout up to the maximum of 15 minutes. The default setting is 3 seconds, which is insufficient for Amazon Bedrock model responses | 
| Lambda concurrency | Increased concurrency | The Lambda gets invoked in parallel during training. Increase concurrency to maximize available throughput | 
| Recipe configuration | Match Lambda settings | The concurrency limit must be configured in your recipe | 