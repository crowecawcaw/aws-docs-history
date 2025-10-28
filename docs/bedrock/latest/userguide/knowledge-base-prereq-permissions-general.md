# Set up permissions for a user or role to create and manage knowledge bases

For a user or role to perform actions related to Amazon Bedrock Knowledge Bases, you must attach policies to it that grant permissions to perform the
actions. It describes permissions that allow a user to retrieve information from these knowledge bases and generate responses from them.

Expand the following sections to learn how to set up permissions for specific use cases:

To allow an IAM role to create a knowledge base, connect it to a structured data store, manage the knowledge base, and start and manage ingestion jobs from the data source to the knowledge base, you must provide permissions to the `KnowledgeBase`, `DataSource`, and `IngestionJob` actions. To provide permissions to tag knowledge bases, include permissions to `bedrock:TagResource` and `bedrock:UntagResource`.

###### Note

If the user or role has the [AmazonBedrockFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonBedrockFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonBedrockFullAccess") AWS managed policy attached, you can skip this prerequisite.

To allow a role to perform these actions, attach the following policy to the role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CreateKB",
 "Effect": "Allow",
 "Action": [
 "bedrock:CreateKnowledgeBase"
 ],
 "Resource": "*"
 },
 {
 "Sid": "KBDataSourceManagement",
 "Effect": "Allow",
 "Action": [
 "bedrock:GetKnowledgeBase",
 "bedrock:ListKnowledgeBases",
 "bedrock:UpdateKnowledgeBase",
 "bedrock:DeleteKnowledgeBase",
 "bedrock:StartIngestionJob",
 "bedrock:GetIngestionJob",
 "bedrock:ListIngestionJobs",
 "bedrock:StopIngestionJob",
 "bedrock:TagResource",
 "bedrock:UntagResource"
 ],
 "Resource": [
 "arn:aws:bedrock:`us-east-1`:`123456789012`:knowledge-base/`*`"
 ]
 }
 ]
}`

```

After you create a knowledge base, we recommend that you scope the permissions in the `KBDataSourceManagement` statament down by replacing the wildcard (`*`) with the ID of the knowledge base that you created.

This section describes the permissions that you need to perform the `Retrieve` and
`RetrieveAndGenerate` API operations for knowledge bases.

Attach the following policy to the role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GetKB",
 "Effect": "Allow",
 "Action": [
 "bedrock:GetKnowledgeBase"
 ],
 "Resource": [
 "arn:aws:bedrock:`us-east-1`:`123456789012`:knowledge-base/`${KnowledgeBaseId}`"
 ]
 },
 {
 "Sid": "Retrieve",
 "Effect": "Allow",
 "Action": [
 "bedrock:Retrieve"
 ],
 "Resource": [
 "arn:aws:bedrock:`us-east-1`:`123456789012`:knowledge-base/`${KnowledgeBaseId}`"
 ]
 },
 {
 "Sid": "RetrieveAndGenerate",
 "Effect": "Allow",
 "Action": [
 "bedrock:RetrieveAndGenerate"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

You can remove statements that you don't need, depending on your use case:

- The `GetKB` statement is used to get the knowledge base information.
- The `Retrieve` statement is required to call [Retrieve](../APIReference/API_agent-runtime_Retrieve.md "../APIReference/API_agent-runtime_Retrieve.md") to retrieve data from your data store.
- The `RetrieveAndGenerate` statement is required to call [RetrieveAndGenerate](../APIReference/API_agent-runtime_RetrieveAndGenerate.md "../APIReference/API_agent-runtime_RetrieveAndGenerate.md") to retrieve data from your data store
  and generate responses based off the data.
  If you plan to use [RetrieveAndGenerate](../APIReference/API_agent-runtime_RetrieveAndGenerate.md "../APIReference/API_agent-runtime_RetrieveAndGenerate.md") to generate responses based on retrieved data from your data source, request access to the foundation models to use for generation by following the steps at [Access Amazon Bedrock foundation models](model-access.md "model-access.md").

To further restrict permissions, you can omit actions, or you can specify resources and condition keys by which to filter permissions. For more information about actions, resources, and condition keys, see the following topics in the _Service Authorization Reference_:

- [Actions defined by Amazon Bedrock](../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-actions-as-permissions") – Learn about actions, the resource types that you can scope them to in the `Resource` field, and the condition keys that you can filter permissions on in the `Condition` field.
- [Resource types defined by Amazon Bedrock](../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-resources-for-iam-policies") – Learn about the resource types in Amazon Bedrock.
- [Condition keys for Amazon Bedrock](../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-policy-keys "../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-policy-keys") – Learn about the condition keys in Amazon Bedrock.
