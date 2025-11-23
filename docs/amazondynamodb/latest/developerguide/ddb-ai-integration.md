# Using generative AI with DynamoDB

Amazon DynamoDB is a serverless, fully managed, distributed NoSQL database with single-digit millisecond performance at any scale. DynamoDB is optimized for high-throughput workloads and you can extend its
capabilities by integrating with generative AI models. Using generative AI models, you can
work with data stored in DynamoDB tables in real-time and build applications that are
contextually aware and highly personalized. You can also enhance the end user experience by
fully leveraging your business, user, and application data to customize your generative AI
solutions.

For more information about gen AI and the solutions AWS provides to build gen AI
applications, see [Transform your business
with generative AI](https://aws.amazon.com/ai/generative-ai/ "https://aws.amazon.com/ai/generative-ai/").

###### Topics

- [Generative AI use cases for DynamoDB](#gen-ai-use-case-ddb "#gen-ai-use-case-ddb")
- [Generative AI blogs for DynamoDB](#gen-ai-blogs "#gen-ai-blogs")
- [Leveraging DynamoDB Zero-ETL integration with
  OpenSearch Service](ddb-and-amazon-bedrock.md "ddb-and-amazon-bedrock.md")

## Generative AI use cases for DynamoDB

DynamoDB is widely used in AI powered conversational applications, such as chatbots and
call centers built with a [Foundation Model (FM)](https://aws.amazon.com/what-is/foundation-models/ "https://aws.amazon.com/what-is/foundation-models/"). You can access FMs through Amazon Bedrock, Amazon SageMaker AI, or
other model providers. Such applications commonly use DynamoDB to improve personalization
and enhance the user experience across three data patterns: application data, business
data, and user data. Some examples of these data patterns are as follows:

- Storage of application data, such as chat message history, through
  integrations with [LangChain](https://js.langchain.com/v0.1/docs/integrations/chat_memory/dynamodb/ "https://js.langchain.com/v0.1/docs/integrations/chat_memory/dynamodb/"), [LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/docstore/DynamoDBDocstoreDemo/ "https://docs.llamaindex.ai/en/stable/examples/docstore/DynamoDBDocstoreDemo/"), or a custom code. This context enhances the user
  experience by allowing the model to _converse_ back and forth
  with the user.
- Creation of a customized user experience by leveraging business data, such as
  inventory, pricing, and documentation.
- Application of user data, such as web history, past orders, and user
  preferences, to provide personalized answers.

For instance, an insurance company can build a chatbot using DynamoDB to provide their
[Retrieval-Augmented Generation (RAG)](../../../sagemaker/latest/dg/jumpstart-foundation-models-customize-rag.md "../../../sagemaker/latest/dg/jumpstart-foundation-models-customize-rag.md") based gen AI model access to near
real-time data. Examples of such data are real-time mortgage rates, product pricing,
compliant/standard contract copy, user web history, and user preferences. Combining
DynamoDB with RAG adds in-depth and updated information about insurance products and the
user data. This enriches the prompts and answers to provide end users with an accurate,
personalized, and near real-time experience.

Similarly, financial services industry customers use DynamoDB, [Amazon Bedrock
knowledge bases](../../../bedrock/latest/userguide/knowledge-base.md "../../../bedrock/latest/userguide/knowledge-base.md"), and [Amazon Bedrock
agents](https://aws.amazon.com/bedrock/agents/ "https://aws.amazon.com/bedrock/agents/") to build RAG-based gen AI applications. These applications can use
open-source earnings reports and call transcripts. They can also use user-specific
portfolio and transaction history to generate an on-demand summary of portfolio
including an outlook for the future.

## Generative AI blogs for DynamoDB

The following articles offer detailed use cases, best practices, and step-by-step
guides to help you leverage DynamoDB's capabilities in building advanced AI-powered
applications.

- [Amazon DynamoDB data models for generative AI chatbots](https://aws.amazon.com/blogs/database/amazon-dynamodb-data-models-for-generative-ai-chatbots/ "https://aws.amazon.com/blogs/database/amazon-dynamodb-data-models-for-generative-ai-chatbots/")
- [Build a scalable, context-aware chatbot with Amazon DynamoDB, Amazon Bedrock, and
  LangChain](https://aws.amazon.com/blogs/database/build-a-scalable-context-aware-chatbot-with-amazon-dynamodb-amazon-bedrock-and-langchain/ "https://aws.amazon.com/blogs/database/build-a-scalable-context-aware-chatbot-with-amazon-dynamodb-amazon-bedrock-and-langchain/")
