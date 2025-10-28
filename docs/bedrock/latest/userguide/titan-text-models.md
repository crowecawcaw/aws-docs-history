# Amazon Titan Text models

Amazon Titan text models include Amazon Titan Text G1 - Premier, Amazon Titan Text G1 - Express and Amazon Titan Text G1 - Lite.

## Amazon Titan Text G1 - Premier

Amazon Titan Text G1 - Premier is a large language model for text generation. It is useful for a wide range of tasks including open-ended and context-based
question answering, code generation, and summarization. This model is integrated with Amazon Bedrock Knowledge Base and Amazon Bedrock Agents. The model also supports Custom fine-tuning
in preview.

- **Model ID** – `amazon.titan-text-premier-v1:0`
- **Max tokens** – 32K
- **Languages** – English
- **Supported use cases** – 32k context window, open-ended text generation, brainstorming,
  summarizations, code generation, table creation, data formatting, paraphrasing, chain of thought, rewrite, extraction, QnA, chat, Knowledge Base
  support, Agents support, Model Customization (preview).
- **Inference parameters** – Temperature, Top P (defaults: Temperature = 0.7, Top P = 0.9)

**AWS AI Service Card - [Amazon Titan Text Premier](https://aws.amazon.com/machine-learning/responsible-machine-learning/titan-text-premier/ "https://aws.amazon.com/machine-learning/responsible-machine-learning/titan-text-premier/")**

## Amazon Titan Text G1 - Express

Amazon Titan Text G1 - Express is a large language model for text generation. It is useful
for a wide range of advanced, general language tasks such as open-ended text generation and conversational chat, as well as support within Retrieval Augmented
Generation (RAG). At launch, the model is optimized for English, with multilingual support for 100 additional languages available in preview.

- **Model ID** – `amazon.titan-text-express-v1`
- **Max tokens** – 8K
- **Languages** – English (GA), 100 additional languages (Preview)
- **Supported use cases** – Retrieval augmented generation, open-ended text generation, brainstorming,
  summarizations, code generation, table creation, data formatting, paraphrasing, chain of thought, rewrite, extraction, QnA, and chat.

## Amazon Titan Text G1 - Lite

Amazon Titan Text G1 - Lite is a light weight efficient model, ideal for fine-tuning of English-language
tasks, including summarizations and copy writing, where customers want a smaller, more cost-effective model that is also highly customizable.

- **Model ID** – `amazon.titan-text-lite-v1`
- **Max tokens** – 4K
- **Languages** – English
- **Supported use cases** – Open-ended text generation,
  brainstorming, summarizations, code generation, table creation, data formatting, paraphrasing,
  chain of thought, rewrite, extraction, QnA, and chat.

## Amazon Titan Text Model Customization

For more information on customizing Amazon Titan text models, see the following pages.

- [Prepare your training datasets for fine-tuning and continued
  pre-training](model-customization-prepare.md "model-customization-prepare.md")
- [Amazon Titan text model customization
  hyperparameters](cm-hp-titan-text.md "cm-hp-titan-text.md")

## Amazon Titan Text Prompt Engineering Guidelines

Amazon Titan text models can be used in a wide variety of applications for different use cases. Amazon Titan Text models have prompt engineering guidelines for the following applications including:

- Chatbot
- Text2SQL
- Function Calling
- RAG (Retrieval Augmented Generation)

For more information on Amazon Titan Text prompt engineering guidelines, see [Amazon Titan Text Prompt Engineering Guidelines](https://d2eo22ngex1n9g.cloudfront.net/Documentation/User+Guides/Titan/Amazon+Titan+Text+Prompt+Engineering+Guidelines.pdf "https://d2eo22ngex1n9g.cloudfront.net/Documentation/User+Guides/Titan/Amazon+Titan+Text+Prompt+Engineering+Guidelines.pdf").

For general prompt engineering guidelines, see [Prompt Engineering Guidelines](prompt-engineering-guidelines.md "prompt-engineering-guidelines.md").

**AWS AI Service Card - [Amazon Titan Text](https://aws.amazon.com/machine-learning/responsible-machine-learning/titan-text/ "https://aws.amazon.com/machine-learning/responsible-machine-learning/titan-text/")**

AI Service Cards provide transparency and document the intended use cases and fairness considerations for our AWS AI services. AI Service Cards provide a single
place to find information on the intended use cases, responsible AI design choices, best practices, and performance for a set of AI service use cases.
