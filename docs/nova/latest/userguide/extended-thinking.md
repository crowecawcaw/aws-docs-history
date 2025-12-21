# Understanding model reasoning with extended reasoning

###### Note

This documentation is for Version 1. For information on how to use Extended thinking in version 2, visit [Extended thinking](../nova2-userguide/extended-thinking.md "../nova2-userguide/extended-thinking.md").

Extended thinking is a setting that allows a model to approach complex problems with a
distinct reasoning phase. During this phase, it first generates dedicated reasoning content in
`reasoningContent` blocks involving a step by step systemic exploration of a problem.
The model then reflects on its reasoning, identifying potential errors or alternative approaches.
Then, it finalizes its response. This provides a clean final answer while providing transparent insight
into the model's process

Due to extended thinking's large computational requirements, Nova allows selective enablement for
a hybrid approach. This means you can toggle on extended thinking for complex, less time-critical queries.
For queries that are simple or require rapid response, you can disable extended thinking to reduce
computational resource load.

## How extended reasoning works

When extended thinking is enabled, Nova creates reasoningContent blocks in its response where it outputs
its internal thinking process. The model uses this reasoning to inform its final text response, creating
a clear separation between the thinking phase and the final answer.

The following is an API response including `reasoningContent` blocks followed by text content blocks:

```

{
  "output": {
    "message": {
      "role": "assistant",
      "content": [
        {
          "reasoningContent": {
            "reasoningText": {
              "text": "Let me analyze this optimization problem systematically. First, I need to understand the constraints: 5 warehouses, 12 distribution centers, 200 retail locations, with a 50-mile maximum distance requirement. This is a classic facility location problem with distance constraints...",
            }
          }
        },
        {
          "text": "Based on my analysis, I recommend implementing a two-phase optimization approach. Phase 1 should focus on clustering retail locations using k-means algorithm to identify natural distribution center catchment areas..."
        }
      ]
    }
  }
}


```

## Using extended reasoning

The following is an example of a Converse API call with extended reasoning enabled:

```

import boto3
import json

client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Enable extended thinking for complex problem-solving
response = client.converse(
    modelId="amazon.nova-lite-1-5-v1:0",
    messages=[{
        "role": "user",
        "content": [{"text": "I need to optimize a logistics network with 5 warehouses, 12 distribution centers, and 200 retail locations. The goal is to minimize total transportation costs while ensuring no location is more than 50 miles from a distribution center. What approach should I take?"}]
    }],
    inferenceConfig={
        "maxTokens": 40000,
        "temperature": 0
    },
    additionalModelRequestFields={
        "reasoningConfig": {
            "type": "enabled",
            "maxReasoningEffort": "high"
        }
    }
)

# The response will contain reasoning blocks followed by the final answer
for block in response["output"]["message"]["content"]:
    if "reasoningContent" in block:
        reasoning_text = block["reasoningContent"]["reasoningText"]["text"]
        print(f"Nova's thinking process:\n{reasoning_text}\n")
    elif "text" in block:
        print(f"Final recommendation:\n{block['text']}")


```

If you exclude the `reasoningConfig` element, the model will disable extended thinking by default.

### Extended thinking configuration options

Nova provides flexible controls for extended thinking behavior through the reasoningConfig parameter, allowing you to
optimize the inference-time compute allocation for your specific needs.

###### Reasoning control

You can toggle extended thinking capabilities between two modes. Setting `type` to `disabled` (the default) means Nova uses
efficient latent reasoning, optimizing for speed and efficiency. Setting `type` to `enabled` activates Nova's explicit
extended thinking with a visible reasoning process.

###### Reasoning effort levels

When extended thinking is enabled, you can control how much computational effort Nova invests in the reasoning process. Setting `maxReasoningEffort` to
low is suitable for moderately complex tasks requiring some additional reasoning. The medium setting works well for complex problems requiring substantial
analysis. The high setting provides the most thorough reasoning for highly complex, multi-faceted tasks, using up to 32,000 reasoning tokens.

```

{
  "modelId": "amazon.nova-lite-1-5-v1:0",
  "inferenceConfig": {
    "maxTokens": 40000,
    "temperature": 0
  },
  "additionalModelRequestFields": {
    "reasoningConfig": {
      "type": "enabled",
      "maxReasoningEffort": "high"
    }
  }
}


```

###### Note

When using `low` and `medium` settings, reasoning content will be streamed as each token is generated when using `ConverseStream`.
However, the `high` works differently, applying different approaches to improve quality resulting in outputting all the reasoning content in a final chunk. This
may significantly increase time to first token and require additional client-side work to manage effectively.

## Best practices for extended thinking

### Identifying extended reasoning use cases

This section will go over potential use cases where extended reasoning is and is not applicable.

### Use cases where extended thinking is applicable:

- **Complex Problem Solving** — Multi-step mathematical calculations and proofs, algorithmic challenges requiring systematic
  approaches, scientific analysis with multiple interdependent variables, and financial modeling with complex scenarios and constraints all benefit from the model's
  ability to work through problems methodically in a dedicated thinking phase.
- **Advanced Coding Tasks** — Large codebase refactoring across multiple files and dependencies, complex debugging scenarios
  requiring systematic elimination of possibilities, system architecture design with multiple technical considerations, and migration planning across multiple services
  and platforms all benefit from Nova's ability to reason through the problem space comprehensively before proposing solutions.
- **Analytical Tasks** — Document analysis requiring synthesis across multiple sources, strategic planning with competing priorities
  and constraints, research tasks requiring evaluation of conflicting evidence, and legal or compliance analysis requiring careful consideration of regulations all benefit from
  the model's ability to work through complex information systematically.
- **Multi-Step Planning** — Project planning with dependencies and resource constraints, workflow design requiring optimization across
  multiple criteria, risk analysis requiring evaluation of multiple scenarios, and business process optimization requiring systematic evaluation all benefit from Nova's enhanced
  planning capabilities.

### Use cases where extended reasoning is not applicable:

- **Simple Queries** — Basic factual questions like "What is the capital of France?", straightforward definitions such as "What does API stand for?",
  simple calculations involving basic arithmetic, and direct information retrieval from provided context all work efficiently with Nova's default latent reasoning mode.
- **Speed-Critical Applications** — Real-time chat applications where latency matters, high-frequency API calls in production systems, simple
  content generation for high-volume use cases, and basic classification or sentiment analysis tasks all benefit from the faster response times of latent reasoning.
- **Cost-Sensitive Workloads** — High-volume processing where speed and cost matter more than reasoning depth, simple automation tasks with
  straightforward logic, basic content moderation or filtering, and routine data processing and transformation typically don't require the additional computational investment of extended
  thinking.

### Choosing reasoning effort levels

- **Low** — Works optimally for code review and improvement suggestions, basic analysis tasks requiring some additional consideration, simple
  problem-solving that benefits from a structured approach, and most day-to-day development tasks with moderate complexity. This level provides meaningful reasoning enhancement while
  maintaining reasonable cost and latency characteristics.
- **Medium** — Works well for complex debugging scenarios requiring systematic investigation, multi-step calculations with interdependencies,
  moderate planning tasks with multiple constraints, and analysis requiring evaluation of several alternatives. This level provides substantial reasoning depth for problems that benefit
  from more thorough analysis.
- **High** — Delivers the best results for advanced mathematical problems and proofs, complex system design with multiple architectural considerations,
  research tasks requiring deep analysis and synthesis, critical decision-making scenarios with significant implications, and multi-step workflows requiring careful planning and verification.
  This level enables Nova to invest substantial computational resources in working through complex problems comprehensively.

### Managing cost and performance

###### Cost optimization

Optimizing for cost requires thoughtful application of extended thinking. Use extended thinking only when the complexity justifies the additional computational cost, since reasoning tokens
are billed as output tokens. Start with low effort and increase incrementally based on results to find the optimal balance for your use cases. Monitor reasoning token usage patterns in your
applications to identify optimization opportunities. Consider batch processing for non-time-sensitive reasoning-heavy tasks to reduce costs. Remember that latent reasoning with extended thinking
disabled handles most tasks effectively and should remain your default approach.

###### Performance optimization

Optimizing for performance involves setting appropriate maxTokens values to accommodate both reasoning and final response content. Use streaming for complex reasoning tasks to improve perceived
performance and user experience. Cache reasoning patterns for frequently encountered problem types where possible. Consider reasoning effort level based on user expectations and time constraints, balancing
thorough analysis with response time requirements.
