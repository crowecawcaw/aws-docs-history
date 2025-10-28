# Prerequisites for creating an Amazon Bedrock knowledge

base with a unstructured data source

Amazon Bedrock knowledge bases require data and models to retrieve and generate responses, a vector
store to store the vector representation of the data, and AWS Identity and Access Management permissions to access
your data and perform actions.

Before you can create a knowledge base, you must fulfill the following
prerequisites. For general permissions requirements, see
[Set up permissions for a user or role to create and manage knowledge bases](knowledge-base-prereq-permissions-general.md "knowledge-base-prereq-permissions-general.md")

1. Make sure your data is in a [supported data
   source connector](data-source-connectors.md "data-source-connectors.md").
2. (Optional) [Set up your own supported vector
   store](knowledge-base-setup.md "knowledge-base-setup.md"). You can skip this step if you plan to use the AWS Management Console to
   automatically create a vector store for you.
3. (Optional) Create a custom AWS Identity and Access Management (IAM) [service role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") with the proper permissions by following the instructions
   at [Create a service role for Amazon Bedrock Knowledge Bases](kb-permissions.md "kb-permissions.md"). You can use the
   AWS Management Console to automatically create a service role for you.

###### Note

If you're creating a knowledge base with Amazon OpenSearch Service (including Amazon OpenSearch Serverless), the service role requires additional permissions beyond those covered by the AWS-managed BedrockFullAccess policy. These include `aoss:CreateAccessPolicy`, `iam:CreateServiceLinkedRole`, and `iam:CreateRole` permissions. 4. (Optional) Set up extra security configurations by following the steps at [Encryption of knowledge base resources](encryption-kb.md "encryption-kb.md"). 5. (Optional) If you plan to use the [RetrieveAndGenerate](../APIReference/API_agent-runtime_RetrieveAndGenerate.md "../APIReference/API_agent-runtime_RetrieveAndGenerate.md") API operation to generate
responses based on information retrieved from your knowledge base, request access to
the models that you'll use in the Regions that you'll use them in by following the
steps at [Access Amazon Bedrock foundation models](model-access.md "model-access.md").

###### Topics

- [Prerequisites for your Amazon Bedrock knowledge base
  data](knowledge-base-ds.md "knowledge-base-ds.md")
- [Prerequisites for using a vector store you created for a
  knowledge base](knowledge-base-setup.md "knowledge-base-setup.md")
