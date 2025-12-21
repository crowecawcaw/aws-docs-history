# What is prompt engineering

Prompt engineering refers to the practice of optimizing textual input to a large language model (LLM) to improve output and receive the responses you want. Prompting helps an LLM perform a wide variety of tasks, including classification, question answering, code generation, creative writing, and more. The quality of prompts that you provide to a LLM can impact the quality of the model's responses. This section provides you the necessary information to get started with prompt engineering. It also covers tools to help you find the best possible prompt format for your use case when using a LLM on Amazon Bedrock

The effectiveness of prompts is contingent upon the quality of the information provided and the craftsmanship of the prompt itself. Prompts may encompass instructions, questions, contextual details, inputs, and examples to effectively guide the model and enhance the quality of the results. This document outlines strategies and tactics for optimizing the performance of Amazon Nova 2 Sonic family of models. The methods presented herein may be employed in various combinations to amplify their effectiveness. We encourage you to engage in experimentation to identify the approaches most suitable for their specific needs.

## Getting started with prompt engineering

Before you start prompt engineering, we recommend that you have the following elements in place, so you can iteratively develop the most optimal prompt for your use case:

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
