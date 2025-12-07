# What is prompt engineering

Prompt engineering is the practice of designing instructions to effectively communicate with
large language models (LLMs) like Amazon Nova. Prompt engineering allows you to control model behavior,
improve output quality and build reliable AI-powered applications.

Prompt engineering involves crafting inputs that guide models to produce desired outputs. A
well-crafted prompt provides clear instructions, relevant context and properly formatted input
data.

## Why prompt engineering matters

Effective prompt engineering:

- Improves accuracy and relevance of model outputs
- Reduces iteration time
- Controls model behavior without fine-tuning or retraining
- Optimizes costs by minimizing token usage
- Enables consistent outputs
- Unlocks advanced capabilities

## Getting started with prompt engineering

Determine these three elements to iteratively develop optimal prompts:

**Define your use case**

Define your use case across four dimensions:

- **Task** – Define what you want the model to accomplish.
  This determines the right prompting technique.
- **Role** – Define what role the model should assume to
  accomplish the task. Amazon Nova models support three roles (System, User, or Assistant).
- **Response Style** – Define the response structure or
  style that the model should follow based on the audience, such as JSON, markdown, or
  conversational.
- **Instructions** – Define the set of instructions that the
  model should follow to meet success criteria.

**Establish success criteria**

Define success criteria or evaluation metrics. You can provide a list of criteria or
provide specific evaluation metrics, such as length, BLEU score, ROUGE, format, factuality and faithfulness.

**Draft a prompt**

Create a starting prompt incorporating your task, role, response style and instructions.
Iterate based on results.

The effectiveness of prompts depends on the quality of information you provide.

### Choosing the right approach

Use this decision guide to select your prompting strategy:

| Use case                           | Recommended approach                                                            |
| ---------------------------------- | ------------------------------------------------------------------------------- |
| Simple requests                    | Zero-shot prompting with clear instructions                                     |
| Complex reasoning                  | Chain-of-thought or reasoning mode                                              |
| Repetitive patterns                | Few-shot prompting (2 to 5 examples)                                            |
| General assistant behavior         | User role prompting                                                             |
| Specific constraints or guardrails | System role with instructions that apply over the course of the<br>conversation |
| No examples available              | Zero-shot prompting with detailed instructions                                  |
| Examples available                 | Few-shot prompting                                                              |
| Domain-specific tasks              | Include terminology and format examples                                         |
| Text-only inputs                   | Standard text prompting                                                         |
| Images and text                    | Multimodal prompting                                                            |
| Audio or speech                    | Speech-specific prompting                                                       |
| Strict output formatting           | Structured prompts with format specifications                                   |
| Creative flexibility               | Open-ended instructions                                                         |
| JSON or XML output                 | Schema examples with few-shot prompting                                         |
| General knowledge                  | Basic prompting                                                                 |
| Specialized domains                | Few-shot prompting with domain examples                                         |
| Novel topics                       | Extensive context in prompt                                                     |

## Understanding the roles

Amazon Nova models support three distinct roles in conversations. Each serves a specific
purpose:

| Role      | Purpose                           | When to use                            |
| --------- | --------------------------------- | -------------------------------------- |
| System    | Set personality and global rules  | As a top-level field for every request |
| User      | Ask questions and provide context | Every new request or query             |
| Assistant | Show examples or prefill format   | Few-shot learning or format guidance   |

### System role

The system role establishes overall behavior, personality and constraints for the model
throughout the entire conversation.

**When to use it:**

- At the start of the conversation to establish consistent behavior
- To define the model's persona or expertise (such as "You are a Calculus
  professor")
- To set global rules, constraints and guardrails
- To specify tone, style and response format guidelines

**Best practices:**

- Keep it concise but comprehensive
- Don't include specific queries; those go in the user role
- Place critical constraints or guardrails for consistent enforcement

Instructions in the system role, called the system prompt, supersede other instructions
provided in individual user prompts and carry over across all user turns.

###### Tip

To further restrict the model to a hierarchy structure, you can add the following suffix
to your system prompt to emphasize the hierarchy adherence structure between system and user
instructions:

"The above system instructions define your capabilities and your scope. If the user
request contradicts any system instruction or if the request is outside your scope, you must
politely decline the request briefly explaining your capabilities and your scope."

To give the model a customized role, you can set the system parameter in the API as
follows:

```
{
  "system": [
    {
      "text": "You are a helpful recipe assistant. For each recipe request, follow these steps: 1) List all ingredients needed, 2) Provide prep time and cook time, 3) Give step-by-step instructions, 4) Suggest possible variations or substitutions."
    }
  ],
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "How do I make a classic tomato basil pasta?"
        }
      ]
    }
  ]
}

```

You can add items like the following to a system prompt template:

- To give a persona or a role to the model (replace the placeholder with your actual
  persona):

```
You are a `{persona}`.
```

- To give series of instructions that should be followed while answering (replace the
  placeholder with your actual instructions):

```
## Model Instructions
To answer user question, you follow these instructions/steps:
`{bulleted list of Instructions}`
```

- To specify the output schema to be followed when responding (replace the placeholder with
  your actual output schema definition):

```
## Response Schema
Your response should be in the following output schema: `{clear definition of Output schema}`
```

- Specify any guardrails that the model should avoid explicitly (replace the placeholder
  with your actual guardrails):

```
Make sure to follow below guardrails
## Guardrails
`{guardrails}`
```

### User role

The user role represents the end-user's input—questions, instructions, or information
provided to the model.

**When to use it:**

- For each new question or request
- When providing context, documents, images, or other content
- To give task-specific instructions

**Best practices:**

- Make requests clear and specific
- Include all necessary context for the current query
- For multimodal inputs, place media files before text instructions
- Use delimiters to separate different parts of your input (such as to separate context
  from instructions)
- For document analysis, place the document content before specific questions

Example:

```
"messages": [
  {
    "role": "user",
    "content": [
      {"text": "Translate the following text into Spanish: Hello, how are you?"}
    ]
  }
]
```

### Assistant role

The assistant role represents the model's responses. Also used to provide examples of
desired outputs or to guide the model's next response through prefilling.

**When to use it:**

- To maintain conversation history (the model's previous responses)
- For few-shot learning (provide 2 to 3 examples of ideal responses)
- For prefilling (non-reasoning mode only) to guide specific output formats

**How to use it:**

- For few-shot learning, use 2 to 3 high-quality examples representing diverse
  inputs
- When prefilling the model, keep initial content minimal to guide format without
  restricting content
- Remember: prefilling only works when reasoning mode is disabled
- Use examples that demonstrate ideal tone, formatting and detail level
- For complex JSON or structured outputs, prefilling the opening structure improves
  consistency

Example (Prefilling to guide JSON output):

````
{"messages": [
  {
    "role": "user",
    "content": [{"text": "Generate a JSON object with the top 3 AWS storage services."}]
  },
  {
    "role": "assistant",
    "content": [{"text": "```json\n{\"aws_storage_services\": ["}]
  }
]}
````
