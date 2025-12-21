# Using CloudFormation to set up remote inference for semantic

search

Starting with OpenSearch version 2.9, you can use remote inference with [semantic
search](https://opensearch.org/docs/latest/search-plugins/semantic-search/ "https://opensearch.org/docs/latest/search-plugins/semantic-search/") to host your own machine learning (ML) models. Remote inference uses
the [ML Commons
plugin](https://opensearch.org/docs/latest/ml-commons-plugin/index/ "https://opensearch.org/docs/latest/ml-commons-plugin/index/").

With Remote inference, you can host your model inferences remotely on ML services,
such as Amazon SageMaker AI and Amazon Bedrock, and connect them to Amazon OpenSearch Service with ML connectors.

To ease the setup of remote inference, Amazon OpenSearch Service provides an [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md") template in the console. CloudFormation is an AWS service where you
can, provision, and manage AWS and third-party resources by treating infrastructure as
code.

The OpenSearch CloudFormation template automates the model provisioning process for you, so
that you can easily create a model in your OpenSearch Service domain and then use the model ID to
ingest data and run neural search queries.

When you use neural sparse encoders with OpenSearch Service version 2.12 and onwards, we recommend
that you use the tokenizer model locally instead of deploying remotely. For more
information, see [Sparse encoding models](https://opensearch.org/docs/latest/ml-commons-plugin/pretrained-models/#sparse-encoding-models "https://opensearch.org/docs/latest/ml-commons-plugin/pretrained-models/#sparse-encoding-models") in the OpenSearch documentation.

###### Topics

- [Available CloudFormation templates](#cfn-template-list "#cfn-template-list")
- [Prerequisites](#cfn-template-prereq "#cfn-template-prereq")
- [Amazon Bedrock templates](cfn-template-bedrock.md "cfn-template-bedrock.md")
- [Configuring Agentic Search with
  Bedrock Claude](cfn-template-agentic-search.md "cfn-template-agentic-search.md")
- [MCP server integration templates](cfn-template-mcp-server.md "cfn-template-mcp-server.md")
- [Amazon SageMaker templates](cfn-template-sm.md "cfn-template-sm.md")
- [Remote inference for semantic
  highlighting templates](#cfn-template-semantic-highlighting "#cfn-template-semantic-highlighting")

## Available CloudFormation templates

The following AWS CloudFormation machine learning (ML) templates are available for
use:

###### [Amazon Bedrock templates](cfn-template-bedrock.md "cfn-template-bedrock.md")

**Amazon Titan Text Embeddings Integration**

Connects to Amazon Bedrock's hosted ML models, eliminates the need for separate
model deployment, and uses predetermined Amazon Bedrock endpoints. For more
information, see [Amazon
Titan Text Embeddings](../../../bedrock/latest/userguide/titan-embedding-models.md "../../../bedrock/latest/userguide/titan-embedding-models.md") in the _Amazon Bedrock User
Guide_.

**Cohere Embed Integration**

Provides access to Cohere Embed models, and is optimized for specific
text processing workflows. For more information, see [Embed](https://docs.cohere.com/docs/cohere-embed "https://docs.cohere.com/docs/cohere-embed") on the
_Cohere docs_ website.

**Amazon Titan Multimodal Embeddings**

Supports both text and image embeddings, and enables multimodal search
capabilities. For more information, see [Amazon
Titan Multimodal Embeddings](../../../bedrock/latest/userguide/titan-multiemb-models.md "../../../bedrock/latest/userguide/titan-multiemb-models.md") in the _Amazon Bedrock User
Guide_.

###### [MCP server integration templates](cfn-template-mcp-server.md "cfn-template-mcp-server.md")

**MCP server integration**

Deploys an [Amazon Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.md "../../../bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.md"), provides an agent endpoint, handles
inbound and outbound authentication, and supports OAuth for enterprise
authentication.

###### [Amazon SageMaker templates](cfn-template-sm.md "cfn-template-sm.md")

**Integration with text embedding models through Amazon SageMaker**

Deploys text embedding models in Amazon SageMaker Runtime, creates IAM roles
for model artifact access, and establishes ML connectors for semantic
search.

**Integration with Sparse Encoders through SageMaker**

Sets up sparse encoding models for neural search, creates AWS Lambda
functions for connector management, and returns model IDs for immediate
use.

## Prerequisites

To use a CloudFormation template with OpenSearch Service, complete the following
prerequisites.

### Set up an OpenSearch Service domain

Before you can use a CloudFormation template, you must set up an [Amazon OpenSearch Service domain](osis-get-started.md "osis-get-started.md") with version 2.9 or later and fine-grained access
control enabled. [Create an OpenSearch Service backend role](fgac.md#fgac-roles "fgac.md#fgac-roles")
to give the ML Commons plugin permission to create your connector for you.

The CloudFormation template creates a Lambda IAM role for you with the default
name `LambdaInvokeOpenSearchMLCommonsRole`, which you can override if
you want to choose a different name. After the template creates this IAM role,
you need to give the Lambda function permission to call your OpenSearch Service domain. To do
so, [map the role](fgac.md#fgac-mapping "fgac.md#fgac-mapping") named
`ml_full_access` to your OpenSearch Service backend role with the following
steps:

1. Navigate to the OpenSearch Dashboards plugin for your OpenSearch Service domain. You can
   find the Dashboards endpoint on your domain dashboard on the OpenSearch Service
   console.
2. From the main menu choose **Security**,
   **Roles**, and select the
   **ml_full_access** role.
3. Choose **Mapped users**, **Manage mapping**.
4. Under **Backend roles**, add the ARN of the Lambda
   role that needs permission to call your domain.

```
arn:aws:iam::`account-id`:role/`role-name`
```

5. Select **Map** and confirm the user or
   role shows up under **Mapped
   users**.

After you've mapped the role, navigate to the security configuration of your
domain and add the Lambda IAM role to your OpenSearch Service access policy.

### Enable permissions on your

AWS account

Your AWS account must have permission to access CloudFormation and Lambda, along
with whichever AWS service you choose for your template – either
SageMaker Runtime or Amazon Bedrock.

If you're using Amazon Bedrock, you must also register your model. See [Model
access](../../../bedrock/latest/userguide/model-access.md "../../../bedrock/latest/userguide/model-access.md") in the _Amazon Bedrock User Guide_ to register your
model.

If you're using your own Amazon S3 bucket to provide model artifacts, you must add
the CloudFormation IAM role to your S3 access policy. For more information, see
[Adding
and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the
_IAM User Guide_.

## Remote inference for semantic

highlighting templates

Semantic highlighting is an advanced search feature that enhances result relevance
by analyzing the meaning and context of queries rather than relying solely on exact
keyword matches. This capability uses machine learning models to evaluate semantic
similarity between search queries and document content, identifying and highlighting
the most contextually relevant sentences or passages within documents. Unlike
traditional highlighting methods that focus on exact term matches, semantic
highlighting leverages AI models to assess each sentence using contextual
information from both the query and surrounding text, enabling it to surface
pertinent information even when exact search terms aren' t present in the
highlighted passages. This approach is particularly valuable for AI-driven search
implementations where users prioritize semantic meaning over literal word matching,
allowing search administrators to deliver more intelligent and contextually aware
search experiences that highlight meaningful content spans rather than just keyword
occurrences. For more information, see [Using semantic highlighting](https://docs.opensearch.org/latest/tutorials/vector-search/semantic-highlighting-tutorial/ "https://docs.opensearch.org/latest/tutorials/vector-search/semantic-highlighting-tutorial/").

Use the following procedure open and run an CloudFormation template that automatically
configures Amazon SageMaker models for semantic highlighting.

###### To use the semantic highlighting CloudFormation template

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home "https://console.aws.amazon.com/aos/home ").
2. In the left navigation, choose **Integrations**.
3. Under **Enable Semantic Highlighting through Amazon SageMaker
   integration**, choose **Configure domain**,
   **Configure public domain**.
4. Follow the prompt to set up your model.

###### Note

OpenSearch Service also provides a separate template to configure VPC domain. If you use
this template, you need to provide the VPC ID for the Lambda function.
