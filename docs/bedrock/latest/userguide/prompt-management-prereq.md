# Prerequisites for prompt management

For a role to use prompt management, you need to allow it to perform a certain set of API actions. Review the following prerequisites and fulfill the ones that apply to your use case:

1. If your role has the [AmazonBedrockFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonBedrockFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonBedrockFullAccess") AWS managed policy attached, you can skip this section. Otherwise, follow the steps at [Update the permissions policy for a role](../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md#id_roles_update-role-permissions-policy "../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md#id_roles_update-role-permissions-policy") and attach the following policy to a role to provide permissions to perform actions related to Prompt management:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "PromptManagementPermissions",
 "Effect": "Allow",
 "Action": [
 "bedrock:CreatePrompt",
 "bedrock:UpdatePrompt",
 "bedrock:GetPrompt",
 "bedrock:ListPrompts",
 "bedrock:DeletePrompt",
 "bedrock:CreatePromptVersion",
 "bedrock:OptimizePrompt",
 "bedrock:GetFoundationModel",
 "bedrock:ListFoundationModels",
 "bedrock:GetInferenceProfile",
 "bedrock:ListInferenceProfiles",
 "bedrock:InvokeModel",
 "bedrock:InvokeModelWithResponseStream",
 "bedrock:RenderPrompt",
 "bedrock:TagResource",
 "bedrock:UntagResource",
 "bedrock:ListTagsForResource"
 ],
 "Resource": "*"
 }
 ]
}`

```

To further restrict permissions, you can omit actions, or you can specify resources and condition keys by which to filter permissions. For more information about actions, resources, and condition keys, see the following topics in the _Service Authorization Reference_:

    * [Actions defined by Amazon Bedrock](../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-actions-as-permissions") – Learn about actions, the resource types that you can scope them to in the `Resource` field, and the condition keys that you can filter permissions on in the `Condition` field.
    * [Resource types defined by Amazon Bedrock](../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-resources-for-iam-policies") – Learn about the resource types in Amazon Bedrock.
    * [Condition keys for Amazon Bedrock](../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-policy-keys "../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-policy-keys") – Learn about the condition keys in Amazon Bedrock.

###### Note

    * If you plan to deploy your prompt using the [Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md") API, see [Prerequisites for running model inference](inference-prereq.md "inference-prereq.md") to learn about the permissions that you must set up to invoke a prompt.
    * If you plan to use a [flow](flows.md "flows.md") in Amazon Bedrock Flows to deploy your prompt, see [Prerequisites for Amazon Bedrock Flows](flows-prereq.md "flows-prereq.md") to learn about the permissions that you must set up to create a flow.

2. If you plan to encrypt your prompt with a customer managed key rather than using an AWS managed key (for more information, see [AWS KMS keys](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md")), create the following policies:
   1. Follow the steps at [Creating a key policy](../../../kms/latest/developerguide/key-policy-overview.md "../../../kms/latest/developerguide/key-policy-overview.md") and attach the following key policy to a KMS key to allow Amazon Bedrock encrypt and decrypt a prompt with the key, replacing the `values` as necessary. The policy contains optional condition keys (see [Condition keys for Amazon Bedrock](../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-policy-keys "../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-policy-keys") and [AWS global condition context keys](../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-policy-keys "../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-policy-keys")) in the `Condition` field that we recommend you use as a security best practice.

   ```
   {
       "Sid": "EncryptFlowKMS",
       "Effect": "Allow",
       "Principal": {
           "Service": "bedrock.amazonaws.com"
       },
       "Action": [
           "kms:GenerateDataKey",
           "kms:Decrypt"
       ],
       "Resource": "*",
       "Condition": {
           "StringEquals": {
               "kms:EncryptionContext:aws:bedrock-prompts:arn": "arn:`${partition}`:bedrock:`${region}`:`${account-id}`:prompt/`${prompt-id}`"
           }
       }
   }
   ```

   2. Follow the steps at [Update the permissions policy for a role](../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md#id_roles_update-role-permissions-policy "../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md#id_roles_update-role-permissions-policy") and attach the following policy to the prompt management role, replacing the `values` as necessary, to allow it to generate and decrypt the customer managed key for a prompt. The policy contains optional condition keys (see [Condition keys for Amazon Bedrock](../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-policy-keys "../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-policy-keys") and [AWS global condition context keys](../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-policy-keys "../../../service-authorization/latest/reference/list_amazonbedrock.md#amazonbedrock-policy-keys")) in the `Condition` field that we recommend you use as a security best practice.

   ```
   {
       "Sid": "KMSPermissions",
       "Effect": "Allow",
       "Action": [
           "kms:GenerateDataKey",
           "kms:Decrypt"
       ],
       "Resource": [
           "arn:aws:kms:`${region}`:`${account-id}`:key/`${key-id}`"
       ],
        "Condition": {
           "StringEquals": {
               "aws:ResourceAccount": "`${account-id}`"
           }
       }
   }
   ```
