# Extended thinking in Amazon Nova 2

Amazon Nova 2 Lite introduces **extended thinking** capabilities
that enable the model to engage in deeper reasoning for complex problems. This optional
feature gives you control over when and how the model allocates additional computational
resources to think through challenging tasks.

## How Extended Thinking Works

Amazon Nova 2 introduces extended thinking as a **hybrid
capability**. You have complete control:

- **Extended thinking OFF (default)**: Amazon Nova 2
  operates with efficient latent reasoning, optimal for everyday tasks and
  high-volume applications.
- **Extended thinking ON**: Amazon Nova 2 engages in
  explicit, step-by-step reasoning best for complex problems requiring deep
  analysis.

### Reasoning effort

The following shows different levels of reasoning effort.

#### Low Effort

(maxReasoningeffort:"low")

**Best for:** Tasks with added complexity
requiring structured thinking. For example, you can use this for code review and
improvement suggestions where the model needs to carefully consider existing
code quality, analysis tasks that require thoughtful consideration of multiple
factors, or problem-solving scenarios that benefit from a methodical approach.
Low effort is ideal for compound tasks where basic reasoning improves accuracy
without requiring deep multi-step planning.

#### Medium effort (maxReasoningEffort:

"medium")

**Best for:** Multi-step tasks and coding
workflows. For example, you can use this for software development and debugging
where the model needs to understand existing code structure before implementing
changes, code generation that requires coordination across multiple files or
components, multi-step calculations with interdependencies, or planning tasks
with multiple constraints. Medium effort is optimal for agentic workflows that
coordinate multiple tools and require the model to maintain context across
several sequential operations.

#### High Effort

(maxReasoningeffort:"high")

**Best for:** STEM reasoning and advanced
problem-solving. For example, you can use this for advanced mathematical
problems and proofs that require rigorous step-by-step verification, scientific
analysis and research tasks demanding deep investigation, complex system design
with architectural considerations across multiple dimensions, or critical
decision-making scenarios with significant implications. High effort delivers
maximum accuracy for tasks requiring sophisticated reasoning, careful evaluation
of alternatives, and thorough validation of conclusions.

### Quick start: Enabling Extended

Thinking

Extended thinking is controlled through the `reasoningConfig`
parameter.

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

content_list = response["output"]["message"]["content"]

for item in content_list:
    if "reasoningContent" in item:
        reasoning_text = item["reasoningContent"]["reasoningText"]["text"]
        print("=== REASONING ===")
        print(reasoning_text)
        print()
    elif "text" in item:
        print("=== ANSWER ===")
        print(item["text"])
```

Reasoning Parameters:

- `type: enabled` or `disabled` (default:
  `disabled`)
- `maxReasoningEffort`: `low`, `medium`, or
  `high`

###### Note

Temperature, topP and topK cannot be used with `maxReasoningEffort`
set to `high`. Using these parameters together causes an
error.

For full examples of code that utilizes extended thinking, see [Code library](code-library.md "code-library.md").

### Response Structure

When you enable extended thinking, responses include `reasoningContent`
blocks followed by `text` content blocks:

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
process.Reasoning content is displayed as `[REDACTED]`. You are still
charged for reasoning tokens as they contribute to improved response
quality.

## Configuration Options

Amazon Nova 2 introduces a new `reasoningConfig` parameter that you can add to
your existing converse request structure to enable reasoning:

```

additionalModelRequestFields={
    "reasoningConfig": {
        "type": "enabled",  # or "disabled" (default)
        "maxReasoningEffort": "high"  # "low", "medium", or "high"
    }
}

```

**Parameters:**

- **type:** Toggle between `"enabled"`
  and `"disabled"` (default is `"disabled"`)
- **`maxReasoningEffort`:** When
  enabled, control reasoning depth
- **"low"":** Moderately complex tasks
- **"medium"":** Complex problems requiring
  substantial analysis
- **"high"":** Most thorough reasoning for highly
  complex tasks

###### Note

when using `"high"`, temp, topP, and maxToken must be unset. In this
mode, the model performs deeper analysis to find the best solution. This more
thorough processing may generate output that exceeds 65k tokens The exact amount
depends on your request's complexity but for some problems we have see it go up to
128K tokens. This ensures you get complete, high-quality reasoning rather than
truncated results.

## Supported models

Extended thinking is currently available in: Amazon Nova 2 Lite
(us.amazon.nova-2-lite-v1:0)

## Extended thinking with tool use

Extended thinking works seamlessly with tool calling, allowing Amazon Nova to reason about
which tools to use and how to interpret their results.

## Understanding Reasoning Tokens and

Pricing

### Token types

Extended thinking tokens are billed as output tokens:

- **Input tokens**: Your original request
  content (standard input pricing)
- **Output tokens**: This includes reasoning
  tokens and the final visible response content (standard output pricing)

### Usage breakdown

All three token types are included in your usage metrics and billing. Reasoning
tokens are priced the same as output tokens and will appear as "REDACTED" in the
model response".

```

  {
  "usage": {
    "inputTokens": 45,
    "outputTokens": 1240,
    "totalTokens": 1285
  }
}

```

## Frequently Asked Questions

Why does Amazon Nova 2 Lite show "[REDACTED]" for reasoning content instead of
displaying the model's thinking process?

Our primary focus for this launch is ensuring Nova 2 delivers best in
class intelligence for your tasks, and you'll see this reflected in the
improved accuracy.

We recognize that visibility into the reasoning process is valuable, and
we've heard strong customer interest in understanding how the model thinks
through problems.

We are looking at ways to make this available soon.

**You are still billed for reasoning
tokens**, as they represent actual work that improves your output
quality

which will be captured in the `outputTokens` along with the
answer tokens.

How do I know if extended thinking is working if reasoning is redacted?

You can confirm extended thinking is working by checking the output for
`reasoningContent` blocks in the response (these only appear
when reasoning is enabled)
