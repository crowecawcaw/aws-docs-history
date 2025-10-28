# What is Amazon Bedrock?

Amazon Bedrock is a fully managed service that makes high-performing foundation models (FMs) from
leading AI companies and Amazon available for your use through a unified API. You can choose from a
wide range of foundation models to find the model that is best suited for your use case. Amazon Bedrock also
offers a broad set of capabilities to build generative AI applications with security, privacy, and
responsible AI. Using Amazon Bedrock, you can easily experiment with and evaluate top foundation models for
your use cases, privately customize them with your data using techniques such as fine-tuning and
Retrieval Augmented Generation (RAG), and build agents that execute tasks using your enterprise
systems and data sources.

With Amazon Bedrock's serverless experience, you can get started quickly, privately customize
foundation models with your own data, and easily and securely integrate and deploy them into your
applications using AWS tools without having to manage any infrastructure.

###### Topics

- [What can I do with Amazon Bedrock?](#servicename-feature-overview "#servicename-feature-overview")
- [How do I get started with Amazon Bedrock?](#first-time-user "#first-time-user")
- [Amazon Bedrock pricing](bedrock-pricing.md "bedrock-pricing.md")
- [Key terminology](key-definitions.md "key-definitions.md")

## What can I do with Amazon Bedrock?

You can use Amazon Bedrock to do the following:

- **Experiment with prompts and configurations** – [Submit prompts and generate responses with model inference](inference.md "inference.md") by sending prompts using different
  configurations and foundation models to generate responses. You can use the API or the text,
  image, and chat playgrounds in the console to experiment in a graphical interface. When you're
  ready, set up your application to make requests to the `InvokeModel` APIs.
- **Augment response generation with information from your data
  sources** – [Create knowledge bases](knowledge-base.md "knowledge-base.md") by
  uploading data sources to be queried in order to augment a foundation model's generation of
  responses.
- **Create applications that reason through how to help a
  customer** – [Build agents](agents.md "agents.md") that use foundation
  models, make API calls, and (optionally) query knowledge bases in order to reason through and
  carry out tasks for your customers.
- **Adapt models to specific tasks and domains with training
  data** – [Customize an Amazon Bedrock foundation
  model](custom-models.md "custom-models.md") by providing training data for fine-tuning or continued-pretraining in order to
  adjust a model's parameters and improve its performance on specific tasks or in certain
  domains.
- **Improve your FM-based application's efficiency and output**
  – [Purchase Provisioned Throughput](prov-throughput.md "prov-throughput.md") for a foundation
  model in order to run inference on models more efficiently and at discounted rates.
- **Determine the best model for your use case** – [Evaluate outputs of different models](evaluation.md "evaluation.md") with built-in or custom
  prompt datasets to determine the model that is best suited for your application.
- **Prevent inappropriate or unwanted content** – [Use guardrails](guardrails.md "guardrails.md") to implement safeguards for your generative AI
  applications.
- **Optimize your FM's latency** – [Get faster response times and improved responsiveness](latency-optimized-inference.md "latency-optimized-inference.md") for AI applications with
  Latency-optimized inference for foundation models.

###### Note

The Latency Optimized Inference feature is in preview release for Amazon Bedrock and is
subject to change.

To learn about Regions that support Amazon Bedrock and the foundation models and features that Amazon Bedrock supports, see [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md") and [Feature support by AWS Region in Amazon Bedrock](features-regions.md "features-regions.md").

## How do I get started with Amazon Bedrock?

We recommend that you start with Amazon Bedrock by doing the following:

1. Familiarize yourself
   with the [terms and concepts](key-definitions.md "key-definitions.md") that Amazon Bedrock uses.
2. Understand how AWS [charges](bedrock-pricing.md "bedrock-pricing.md") you for using Amazon Bedrock.
3. Try the [Get started with Amazon Bedrock](getting-started.md "getting-started.md") tutorials. In the tutorials, you learn how to use the playgrounds in Amazon Bedrock console. You also learn and how to use the [AWS SDK](getting-started-api.md "getting-started-api.md") to call Amazon Bedrock API operations.
4. Read the documentation for the features that you want to include
   in your application.
