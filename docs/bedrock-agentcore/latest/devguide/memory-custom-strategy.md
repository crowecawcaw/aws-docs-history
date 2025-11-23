# Built-in with overrides strategy

For advanced or domain-specific use cases, you can create a built-in with overrides
strategy to gain fine-grained control over the long-term memory process. Built-in with
overrides strategies let you override the default behavior of the built-in strategies by
providing your own instructions and selecting a specific foundation model for the extraction
and consolidation steps.

## When to use a built-in with overrides

strategy

Choose a built-in with overrides strategy when you need to tailor the memory logic to
your specific requirements. Common use cases include:

- **Domain-specific extraction:** Constraining the
  strategy to extract only certain types of information. For example, capturing a
  user's food and dietary preferences while ignoring their preferences for
  clothing.
- **Controlling granularity:** Adjusting the level
  of detail in the extracted memory. For example, instructing the summary strategy
  to only save high-level key points rather than a detailed narrative.
- **Model selection:** Using a specific foundation
  model that is better suited for your particular domain or task, such as a model
  fine-tuned for financial or legal text.

## How to customize a strategy

You can configure a Built-in with overrides strategy by providing a model ID and your
own set of instructions that will be added to the system prompt for both extraction and
consolidation.

**Pre-requisite:** Since built-in with overrides
strategies override the behavior of the built-in strategies - to effectively override a
strategy you should first understand its [built-in](built-in-strategies.md "built-in-strategies.md") (default) behavior.

To use a built-in with overrides strategy, use the [CreateMemory](../../../bedrock-agentcore-control/latest/APIReference/API_CreateMemory.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateMemory.md") operation or the [UpdateMemory](../../../bedrock-agentcore-control/latest/APIReference/API_UpdateMemory.md "../../../bedrock-agentcore-control/latest/APIReference/API_UpdateMemory.md") operation.

The model ID can be provided `modelId` field when you configure a built-in
with overrides strategy. To use a model, first enable access for that model in your
AWS account. For more information, see [Add or remove access to
Amazon Bedrock foundation models](../../../bedrock/latest/userguide/model-access-modify.md "../../../bedrock/latest/userguide/model-access-modify.md"). Also, obtain sufficient Amazon Bedrock capacity. For
more information, see [Amazon Bedrock capacity for built-in
with overrides strategies](bedrock-capacity.md "bedrock-capacity.md").

The instructions are passed in the `appendToPrompt` field when you
configure the strategy via the API. This field replaces the default instructions part of
the system prompt in the built-in strategies, letting you guide the model's behavior,
while the Output Schema remains unchanged.

You set the `modelId` and `appendToPrompt` fields in the
`semanticOverride`, `summaryOverride`, or
`userPreferenceOverride` fields found through the
`memoryStrategies` (`MemoryStrategyInput`) field of
`CreateMemory` and `UpdateMemory`.

For example, you can modify the extraction instruction for semantic memory strategy to
add new instructions when customizing it.

###### Built-in semantic memory strategy instructions

The following shows the built-in instructions for the semantic memory
strategy:

```

You are a long-term memory extraction agent supporting a lifelong learning system. Your
task is to identify and extract meaningful information about the users from a given
list of messages.

Analyze the conversation and extract structured information about the user according to
the schema below. Only include details that are explicitly stated or can be logically
inferred from the conversation.

- Extract information ONLY from the user messages. You should use assistant messages
only as supporting context.
- If the conversation contains no relevant or noteworthy information, return an empty
list.

- Do NOT extract anything from prior conversation history, even if provided. Use it
solely for context.
- Do NOT incorporate external knowledge.
- Avoid duplicate extractions.

IMPORTANT: Maintain the original language of the user's conversation. If the user
communicates in a specific language, extract and format the extracted information
in that same language.

```

You could append a new rule to these instructions, such as:

```

- Focus exclusively on extracting facts related to travel and booking preferences.

```

or edit an existing rule such as:

```

IMPORTANT: Always extract memories in English irrespective of the original language of the user's conversation.

```

###### All instructions you can update

You can update the following instructions:

- [Semantic memory
  strategy extraction instructions](memory-system-prompt.md#semantic-memory-extraction-instructions "memory-system-prompt.md#semantic-memory-extraction-instructions")
- [Semantic memory
  strategy consolidation instructions](memory-system-prompt.md#semantic-memory-consolidation-instructions "memory-system-prompt.md#semantic-memory-consolidation-instructions")
- [User preference
  memory strategy extraction instructions](memory-user-prompt.md#user-preference-memory-extraction-instructions "memory-user-prompt.md#user-preference-memory-extraction-instructions")
- [User
  preference memory strategy consolidation instructions](memory-user-prompt.md#user-preference-memory-consolidation-instructions "memory-user-prompt.md#user-preference-memory-consolidation-instructions")
- Summary Memory Strategy Consolidation Instructions

There are no default instructions for built-in Summary memory strategy. You
can add your own instructions to `appendToPrompt` input in the API.
To understand how built-in Summary memory strategy generates and updates the
summary, summary memory strategy Consolidation output schemas in [Built-in strategies](built-in-strategies.md "built-in-strategies.md").

## Best practices for customization

- **Build upon existing instructions:** We strongly
  recommend you use the built-in strategies instructions as a starting point. The
  base structure and instructions are critical to the memory functionality. You
  should add your task-specific guidance to the existing instructions rather than
  writing entirely new ones from scratch.
- **Provide clear instructions:** The content of
  `appendToPrompt` replaces the default instructions in the system
  prompt. Make sure your instructions are logical and complete, as empty or poorly
  formed instructions can lead to undesirable results.

## Important considerations

To maintain the reliability of the memory pipeline, please adhere to the following
guidelines:

- **Do not modify schemas in prompts:** You should
  only add or modify instructions that guide _how_ memories are
  extracted or consolidated. Do not attempt to alter the conversation or memory
  schema definitions within the prompt itself, as this can cause unexpected
  failures.
- **Do not rename consolidation operations:** When
  customizing a consolidation prompt, do not change the operation names (e.g.,
  `AddMemory`, `UpdateMemory`). Altering these names
  will cause the long-term memory pipeline to fail.
- **Output schema is not editable:** built-in with
  overrides strategies do not let you change the final output schema of the
  extracted or consolidated memory. The output schema that will be added to the
  system prompt for the built-in with overrides strategy will be same as the
  built-in strategies. For information about the output schemas, see the
  following:
  - [System prompt for semantic memory
    strategy](memory-system-prompt.md "memory-system-prompt.md")
  - [System prompt for user preference memory
    strategy](memory-user-prompt.md "memory-user-prompt.md")
  - [System prompt for summary strategy](memory-summary-prompt.md "memory-summary-prompt.md")

For full control over the end-to-end memory process, including the output schema, see
[Self-managed strategy](memory-self-managed-strategies.md "memory-self-managed-strategies.md").

## Execution role

When using built-in with overrides strategies you are also required to provide a
`memoryExecutionRoleArn` in the `CreateMemory` API. Bedrock
Amazon Bedrock AgentCore will assume this role to call the bedrock models in your AWS account
for extraction and consolidation.

###### Note

When using built-in with overrides strategies, the LLM usage for extraction and
consolidation will be charged separately to your AWS account, and additional
charges may apply.
