# Prerequisites for direct ingestion

To use direct ingestion, an IAM role must have permissions to use the `KnowledgeBaseDocs` API operations. If your IAM role has the [AmazonBedrockFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonBedrockFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonBedrockFullAccess") AWS managed policy attached, you can skip this section.

The following policy can be attached to an IAM role to allow it to perform direct ingestion on the knowledge bases that you specify in the `Resource` field.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DirectIngestion",
 "Effect": "Allow",
 "Action": [
 "bedrock:StartIngestionJob",
 "bedrock:IngestKnowledgeBaseDocuments",
 "bedrock:GetKnowledgeBaseDocuments",
 "bedrock:ListKnowledgeBaseDocuments",
 "bedrock:DeleteKnowledgeBaseDocuments"
 ],
 "Resource": [
 "arn:aws:bedrock:`us-east-1`:`123456789012`:knowledge-base/`${KnowledgeBaseId}`"
 ]
 }
 ]
}`

```

To further restrict permissions, you can omit actions, or you can specify resources and condition keys by which to filter permissions. For more information about actions, resources, and condition keys, see the following topics in the _Service Authorization Reference_:

- [Actions defined by Amazon Bedrock](../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-actions-as-permissions") – Learn about actions, the resource types that you can scope them to in the `Resource` field, and the condition keys that you can filter permissions on in the `Condition` field.
- [Resource types defined by Amazon Bedrock](../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-resources-for-iam-policies") – Learn about the resource types in Amazon Bedrock.
- [Condition keys for Amazon Bedrock](../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-policy-keys "../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-policy-keys") – Learn about the condition keys in Amazon Bedrock.
