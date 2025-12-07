# Using the Converse API

The Converse API provides a unified interface for interacting with Amazon Nova models. It
abstracts away model-specific details and provides a consistent way to handle multi-turn
conversations, system prompts and streaming responses across all Amazon Nova models.

###### Topics

- [Request structure](#converse-api-request-structure "#converse-api-request-structure")
- [Using system prompts](#converse-api-system-prompt "#converse-api-system-prompt")
- [Inference parameters](#converse-api-inference-params "#converse-api-inference-params")
- [Using reasoning](#converse-api-reasoning "#converse-api-reasoning")

## Request structure

- **Multi-turn conversations:** Maintain context
  across multiple exchanges
- **System prompts:** System instructions such as
  personas or response guidelines
- **Document chat:** Interact with and query
  documents or collections of documents
- **Vision:** Process and analyze images and
  video
- **Tool use:** Enable models to use external tools
  and APIs
- **Guardrails:** Apply content filtering and
  safety controls
- **Reasoning:** Extended thinking for complex
  problem-solving

A basic Converse API request includes the model ID and a list of messages:

```
import boto3

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

response = bedrock.converse(
    modelId='us.amazon.nova-2-lite-v1:0',
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'What is machine learning?'}]
        }
    ]
)

content_list = response["output"]["message"]["content"]
# Extract the first text block
text = next((item["text"] for item in content_list if "text" in item), None)
if text is not None:
    print(text)
```

## Using system prompts

System prompts provide context and instructions to the model:

```
import boto3

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

response = bedrock.converse(
    modelId='us.amazon.nova-2-lite-v1:0',
    system=[
        {'text': 'You are a helpful AI assistant specializing in cloud computing.'}
    ],
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Explain serverless computing.'}]
        }
    ]
)

# Print the response text
content_list = response["output"]["message"]["content"]
text = next((item["text"] for item in content_list if "text" in item), None)
if text is not None:
    print(text)
```

## Inference parameters

Control the model's output using inference parameters. The following are available inference parameters.

- maxTokens (integer): Maximum number of tokens to generate (up to 65,000). If not specified, the model uses a dynamic default based on the request context.
- temperature (float): Controls randomness (0.0-1.0, default 0.7). Lower values make output more deterministic
- topP (float): Nucleus sampling threshold (0-1, default 0.9). Lower values make output more focused
- stopSequences (array): Sequences of characters that stop generation when encountered

Example:

```
import boto3
bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

response = bedrock.converse(
    modelId='us.amazon.nova-2-lite-v1:0',
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Write a short story.'}]
        }
    ],
    inferenceConfig={
        'maxTokens': 512,
        'temperature': 0.7,
        'topP': 0.9,
        'stopSequences': ['END']
    }
)

content_list = response["output"]["message"]["content"]
text = next((item["text"] for item in content_list if "text" in item), None)
if text is not None:
    print(text)
```

## Using reasoning

Nova 2 Lite supports extended thinking for complex
problem-solving. Enable reasoning with `reasoningConfig`.

By default, reasoning is disabled to optimize for speed and cost on simple
queries. When you needto go beyond these straightforward tasks, you can enable reasoning. Nova 2 provides flexible control over reasoning depth through three effort levels:

Low effort (`maxReasoningEffort: "low"`)

BEST FOR: TASKS WITH ADDED COMPLEXITY REQUIRING STRUCTURED THINKING. For example, you can use this for code review and improvement suggestions where the model needs to carefully consider existing code quality, analysis tasks that require thoughtful consideration of multiple factors, or problem-solving scenarios that benefit from a methodical approach. Low effort is ideal for compound tasks where basic reasoning improves accuracy without requiring deep multi-step planning.

Medium effort (`maxReasoningEffort: "medium"`)

BEST FOR: MULTI-STEP TASKS AND CODING WORKFLOWS. For example, you can use this for software development and debugging where the model needs to understand existing code structure before implementing changes, code generation that requires coordination across multiple files or components, multi-step calculations with interdependencies, or planning tasks with multiple constraints. Medium effort is optimal for agentic workflows that coordinate multiple tools and require the model to maintain context across several sequential operations.

High effort (`maxReasoningEffort: "high"`)

BEST FOR: STEM REASONING AND ADVANCED PROBLEM-SOLVING. For example, you can use this for advanced mathematical problems and proofs that require rigorous step-by-step verification, scientific analysis and research tasks demanding deep investigation, complex system design with architectural considerations across multiple dimensions, or critical decision-making scenarios with significant implications. High effort delivers maximum accuracy for tasks requiring sophisticated reasoning, careful evaluation of alternatives, and thorough validation of conclusions.

The following examples show different reasoning effort levels:

Low effort

```
import boto3

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

response = bedrock.converse(
    modelId='us.amazon.nova-2-lite-v1:0',
    system=[{"text": "You are a highly capable personal assistant"}],
    messages=[{
        "role": "user",
        "content": [{"text": "Provide a meal plan for a gluten free family of 4."}]
    }],
    inferenceConfig={
        "temperature": 0.7,
        "topP": 0.9,
        "maxTokens": 10000
    },
    additionalModelRequestFields={
        "reasoningConfig": {
            "type": "enabled",
            "maxReasoningEffort": "low"
        }
    }
)

```

**Reasoning parameters:**

The following are reasoning parameters

- `type`: `enabled` or `disabled` (default:
  `disabled`)
- `maxReasoningEffort`: `low`, `medium`, or
  `high`. This is required when reasoning is enabled.

###### Note

Temperature, topP and topK cannot be used with `maxReasoningEffort`
set to `high`. This will cause an error.

The response includes reasoning content:

```
{
    "output": {
        "message": {
            "role": "assistant",
            "content": [
                {
                    "reasoningContent": {
                        "reasoningText": {
                            "text": "[REDACTED]"
                        }
                    }
                },
                {
                    "text": "Based on the premises, we can conclude..."
                }
            ]
        }
    },
    "stopReason": "end_turn"
}
```

###### Note

With Amazon Nova 2, reasoning content displays as `[REDACTED]`. You're
still charged for reasoning tokens as they contribute to improved output
quality. We include this field in the response structure now to preserve the
option of exposing reasoning content in the future. We are actively working with
customers to determine the best approach for surfacing the model's reasoning
process.
