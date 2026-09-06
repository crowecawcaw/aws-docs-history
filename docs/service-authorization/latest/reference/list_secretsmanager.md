

# Actions, resources, and condition keys for AWS Secrets Manager
<a name="list_secretsmanager"></a>

AWS Secrets Manager (service prefix: `secretsmanager`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/secretsmanager/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/secretsmanager/latest/apireference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/secretsmanager/secretsmanager.json) for this service.

**Topics**
+ [API operations defined by AWS Secrets Manager](#list_secretsmanager-operations)
+ [Actions defined by AWS Secrets Manager](#list_secretsmanager-actions-as-permissions)
+ [Resource types defined by AWS Secrets Manager](#list_secretsmanager-resources-for-iam-policies)
+ [Condition keys for AWS Secrets Manager](#list_secretsmanager-policy-keys)

## API operations defined by AWS Secrets Manager
<a name="list_secretsmanager-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_secretsmanager-actions-as-permissions).




- **   BatchGetSecretValue  **
  - **IAM action:**  [secretsmanager:BatchGetSecretValue](#list_secretsmanager-action-BatchGetSecretValue)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [secretsmanager:GetSecretValue](#list_secretsmanager-action-GetSecretValue)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [secretsmanager:ListSecrets](#list_secretsmanager-action-ListSecrets)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   CancelRotateSecret  **
  - **IAM action:**  [secretsmanager:CancelRotateSecret](#list_secretsmanager-action-CancelRotateSecret) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSecret  **
  - **IAM action:**  [secretsmanager:CreateSecret](#list_secretsmanager-action-CreateSecret)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [secretsmanager:ReplicateSecretToRegions](#list_secretsmanager-action-ReplicateSecretToRegions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [secretsmanager:TagResource](#list_secretsmanager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteResourcePolicy  **
  - **IAM action:**  [secretsmanager:DeleteResourcePolicy](#list_secretsmanager-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteSecret  **
  - **IAM action:**  [secretsmanager:DeleteSecret](#list_secretsmanager-action-DeleteSecret) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeSecret  **
  - **IAM action:**  [secretsmanager:DescribeSecret](#list_secretsmanager-action-DescribeSecret) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRandomPassword  **
  - **IAM action:**  [secretsmanager:GetRandomPassword](#list_secretsmanager-action-GetRandomPassword) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **IAM action:**  [secretsmanager:GetResourcePolicy](#list_secretsmanager-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSecretValue  **
  - **IAM action:**  [secretsmanager:GetSecretValue](#list_secretsmanager-action-GetSecretValue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSecretVersionIds  **
  - **IAM action:**  [secretsmanager:ListSecretVersionIds](#list_secretsmanager-action-ListSecretVersionIds) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSecrets  **
  - **IAM action:**  [secretsmanager:ListSecrets](#list_secretsmanager-action-ListSecrets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutResourcePolicy  **
  - **IAM action:**  [secretsmanager:PutResourcePolicy](#list_secretsmanager-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutSecretValue  **
  - **IAM action:**  [secretsmanager:PutSecretValue](#list_secretsmanager-action-PutSecretValue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveRegionsFromReplication  **
  - **IAM action:**  [secretsmanager:RemoveRegionsFromReplication](#list_secretsmanager-action-RemoveRegionsFromReplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ReplicateSecretToRegions  **
  - **IAM action:**  [secretsmanager:ReplicateSecretToRegions](#list_secretsmanager-action-ReplicateSecretToRegions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RestoreSecret  **
  - **IAM action:**  [secretsmanager:RestoreSecret](#list_secretsmanager-action-RestoreSecret) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RotateSecret  **
  - **IAM action:**  [secretsmanager:RotateSecret](#list_secretsmanager-action-RotateSecret)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** secretsmanager.amazonaws.com / **Access level:** Write

- **   StopReplicationToReplica  **
  - **IAM action:**  [secretsmanager:StopReplicationToReplica](#list_secretsmanager-action-StopReplicationToReplica) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [secretsmanager:TagResource](#list_secretsmanager-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [secretsmanager:UntagResource](#list_secretsmanager-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateSecret  **
  - **IAM action:**  [secretsmanager:UpdateSecret](#list_secretsmanager-action-UpdateSecret) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSecretVersionStage  **
  - **IAM action:**  [secretsmanager:UpdateSecretVersionStage](#list_secretsmanager-action-UpdateSecretVersionStage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ValidateResourcePolicy  **
  - **IAM action:**  [secretsmanager:PutResourcePolicy](#list_secretsmanager-action-PutResourcePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [secretsmanager:ValidateResourcePolicy](#list_secretsmanager-action-ValidateResourcePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write



## Actions defined by AWS Secrets Manager
<a name="list_secretsmanager-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchGetSecretValue](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_BatchGetSecretValue.html)  **
  - **Description:** Grants permission to retrieve and decrypt a list of secrets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [CancelRotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CancelRotateSecret.html)  **
  - **Description:** Grants permission to cancel an in-progress secret rotation
  - **Resource types (\*required):** [Secret\*](#list_secretsmanager-resource-Secret)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_secretsmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_secretsmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_secretsmanager-aws_TagKeys)<br />[secretsmanager:resource/AllowRotationLambdaArn](#list_secretsmanager-secretsmanager_resource_AllowRotationLambdaArn)<br />[secretsmanager:resource/Type](#list_secretsmanager-secretsmanager_resource_Type)<br />[secretsmanager:ResourceTag/tag-key](#list_secretsmanager-secretsmanager_ResourceTag_tag-key)<br />[secretsmanager:SecretId](#list_secretsmanager-secretsmanager_SecretId)<br />[secretsmanager:SecretPrimaryRegion](#list_secretsmanager-secretsmanager_SecretPrimaryRegion)
  - **Access level:** Write

- **   [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html)  **
  - **Description:** Grants permission to create a secret that stores encrypted data that can be queried and rotated
  - **Resource types (\*required):** [Secret\*](#list_secretsmanager-resource-Secret)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_secretsmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_secretsmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_secretsmanager-aws_TagKeys)<br />[secretsmanager:AddReplicaRegions](#list_secretsmanager-secretsmanager_AddReplicaRegions)<br />[secretsmanager:Description](#list_secretsmanager-secretsmanager_Description)<br />[secretsmanager:ForceOverwriteReplicaSecret](#list_secretsmanager-secretsmanager_ForceOverwriteReplicaSecret)<br />[secretsmanager:KmsKeyArn](#list_secretsmanager-secretsmanager_KmsKeyArn)<br />[secretsmanager:KmsKeyId](#list_secretsmanager-secretsmanager_KmsKeyId)<br />[secretsmanager:Name](#list_secretsmanager-secretsmanager_Name)<br />[secretsmanager:resource/AllowRotationLambdaArn](#list_secretsmanager-secretsmanager_resource_AllowRotationLambdaArn)<br />[secretsmanager:resource/Type](#list_secretsmanager-secretsmanager_resource_Type)<br />[secretsmanager:ResourceTag/tag-key](#list_secretsmanager-secretsmanager_ResourceTag_tag-key)<br />[secretsmanager:Type](#list_secretsmanager-secretsmanager_Type)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete the resource policy attached to a secret
  - **Resource types (\*required):** [Secret\*](#list_secretsmanager-resource-Secret)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_secretsmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_secretsmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_secretsmanager-aws_TagKeys)<br />[secretsmanager:resource/AllowRotationLambdaArn](#list_secretsmanager-secretsmanager_resource_AllowRotationLambdaArn)<br />[secretsmanager:resource/Type](#list_secretsmanager-secretsmanager_resource_Type)<br />[secretsmanager:ResourceTag/tag-key](#list_secretsmanager-secretsmanager_ResourceTag_tag-key)<br />[secretsmanager:SecretId](#list_secretsmanager-secretsmanager_SecretId)<br />[secretsmanager:SecretPrimaryRegion](#list_secretsmanager-secretsmanager_SecretPrimaryRegion)
  - **Access level:** Permissions management, Write

- **   [DeleteSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DeleteSecret.html)  **
  - **Description:** Grants permission to delete a secret
  - **Resource types (\*required):** [Secret\*](#list_secretsmanager-resource-Secret)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_secretsmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_secretsmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_secretsmanager-aws_TagKeys)<br />[secretsmanager:ForceDeleteWithoutRecovery](#list_secretsmanager-secretsmanager_ForceDeleteWithoutRecovery)<br />[secretsmanager:RecoveryWindowInDays](#list_secretsmanager-secretsmanager_RecoveryWindowInDays)<br />[secretsmanager:resource/AllowRotationLambdaArn](#list_secretsmanager-secretsmanager_resource_AllowRotationLambdaArn)<br />[secretsmanager:resource/Type](#list_secretsmanager-secretsmanager_resource_Type)<br />[secretsmanager:ResourceTag/tag-key](#list_secretsmanager-secretsmanager_ResourceTag_tag-key)<br />[secretsmanager:SecretId](#list_secretsmanager-secretsmanager_SecretId)<br />[secretsmanager:SecretPrimaryRegion](#list_secretsmanager-secretsmanager_SecretPrimaryRegion)
  - **Access level:** Write

- **   [DescribeSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DescribeSecret.html)  **
  - **Description:** Grants permission to retrieve the metadata about a secret, but not the encrypted data
  - **Resource types (\*required):** [Secret\*](#list_secretsmanager-resource-Secret)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_secretsmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_secretsmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_secretsmanager-aws_TagKeys)<br />[secretsmanager:resource/AllowRotationLambdaArn](#list_secretsmanager-secretsmanager_resource_AllowRotationLambdaArn)<br />[secretsmanager:resource/Type](#list_secretsmanager-secretsmanager_resource_Type)<br />[secretsmanager:ResourceTag/tag-key](#list_secretsmanager-secretsmanager_ResourceTag_tag-key)<br />[secretsmanager:SecretId](#list_secretsmanager-secretsmanager_SecretId)<br />[secretsmanager:SecretPrimaryRegion](#list_secretsmanager-secretsmanager_SecretPrimaryRegion)
  - **Access level:** Read

- **   [GetRandomPassword](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetRandomPassword.html)  **
  - **Description:** Grants permission to generate a random string for use in password creation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetResourcePolicy.html)  **
  - **Description:** Grants permission to get the resource policy attached to a secret
  - **Resource types (\*required):** [Secret\*](#list_secretsmanager-resource-Secret)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_secretsmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_secretsmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_secretsmanager-aws_TagKeys)<br />[secretsmanager:resource/AllowRotationLambdaArn](#list_secretsmanager-secretsmanager_resource_AllowRotationLambdaArn)<br />[secretsmanager:resource/Type](#list_secretsmanager-secretsmanager_resource_Type)<br />[secretsmanager:ResourceTag/tag-key](#list_secretsmanager-secretsmanager_ResourceTag_tag-key)<br />[secretsmanager:SecretId](#list_secretsmanager-secretsmanager_SecretId)<br />[secretsmanager:SecretPrimaryRegion](#list_secretsmanager-secretsmanager_SecretPrimaryRegion)
  - **Access level:** Read

- **   [GetSecretValue](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html)  **
  - **Description:** Grants permission to retrieve and decrypt the encrypted data
  - **Resource types (\*required):** [Secret\*](#list_secretsmanager-resource-Secret)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_secretsmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_secretsmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_secretsmanager-aws_TagKeys)<br />[secretsmanager:resource/AllowRotationLambdaArn](#list_secretsmanager-secretsmanager_resource_AllowRotationLambdaArn)<br />[secretsmanager:resource/Type](#list_secretsmanager-secretsmanager_resource_Type)<br />[secretsmanager:ResourceTag/tag-key](#list_secretsmanager-secretsmanager_ResourceTag_tag-key)<br />[secretsmanager:SecretId](#list_secretsmanager-secretsmanager_SecretId)<br />[secretsmanager:SecretPrimaryRegion](#list_secretsmanager-secretsmanager_SecretPrimaryRegion)<br />[secretsmanager:VersionId](#list_secretsmanager-secretsmanager_VersionId)<br />[secretsmanager:VersionStage](#list_secretsmanager-secretsmanager_VersionStage)
  - **Access level:** Read

- **   [ListSecretVersionIds](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ListSecretVersionIds.html)  **
  - **Description:** Grants permission to list the available versions of a secret
  - **Resource types (\*required):** [Secret\*](#list_secretsmanager-resource-Secret)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_secretsmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_secretsmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_secretsmanager-aws_TagKeys)<br />[secretsmanager:resource/AllowRotationLambdaArn](#list_secretsmanager-secretsmanager_resource_AllowRotationLambdaArn)<br />[secretsmanager:resource/Type](#list_secretsmanager-secretsmanager_resource_Type)<br />[secretsmanager:ResourceTag/tag-key](#list_secretsmanager-secretsmanager_ResourceTag_tag-key)<br />[secretsmanager:SecretId](#list_secretsmanager-secretsmanager_SecretId)<br />[secretsmanager:SecretPrimaryRegion](#list_secretsmanager-secretsmanager_SecretPrimaryRegion)
  - **Access level:** Read

- **   [ListSecrets](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ListSecrets.html)  **
  - **Description:** Grants permission to list the available secrets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutResourcePolicy](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to attach a resource policy to a secret
  - **Resource types (\*required):** [Secret\*](#list_secretsmanager-resource-Secret)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_secretsmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_secretsmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_secretsmanager-aws_TagKeys)<br />[secretsmanager:BlockPublicPolicy](#list_secretsmanager-secretsmanager_BlockPublicPolicy)<br />[secretsmanager:resource/AllowRotationLambdaArn](#list_secretsmanager-secretsmanager_resource_AllowRotationLambdaArn)<br />[secretsmanager:resource/Type](#list_secretsmanager-secretsmanager_resource_Type)<br />[secretsmanager:ResourceTag/tag-key](#list_secretsmanager-secretsmanager_ResourceTag_tag-key)<br />[secretsmanager:SecretId](#list_secretsmanager-secretsmanager_SecretId)<br />[secretsmanager:SecretPrimaryRegion](#list_secretsmanager-secretsmanager_SecretPrimaryRegion)
  - **Access level:** Permissions management, Write

- **   [PutSecretValue](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_PutSecretValue.html)  **
  - **Description:** Grants permission to create a new version of the secret with new encrypted data
  - **Resource types (\*required):** [Secret\*](#list_secretsmanager-resource-Secret)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_secretsmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_secretsmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_secretsmanager-aws_TagKeys)<br />[secretsmanager:resource/AllowRotationLambdaArn](#list_secretsmanager-secretsmanager_resource_AllowRotationLambdaArn)<br />[secretsmanager:resource/Type](#list_secretsmanager-secretsmanager_resource_Type)<br />[secretsmanager:ResourceTag/tag-key](#list_secretsmanager-secretsmanager_ResourceTag_tag-key)<br />[secretsmanager:SecretId](#list_secretsmanager-secretsmanager_SecretId)<br />[secretsmanager:SecretPrimaryRegion](#list_secretsmanager-secretsmanager_SecretPrimaryRegion)
  - **Access level:** Write

- **   [RemoveRegionsFromReplication](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RemoveRegionsFromReplication.html)  **
  - **Description:** Grants permission to remove regions from replication
  - **Resource types (\*required):** [Secret\*](#list_secretsmanager-resource-Secret)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_secretsmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_secretsmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_secretsmanager-aws_TagKeys)<br />[secretsmanager:resource/AllowRotationLambdaArn](#list_secretsmanager-secretsmanager_resource_AllowRotationLambdaArn)<br />[secretsmanager:resource/Type](#list_secretsmanager-secretsmanager_resource_Type)<br />[secretsmanager:ResourceTag/tag-key](#list_secretsmanager-secretsmanager_ResourceTag_tag-key)<br />[secretsmanager:SecretId](#list_secretsmanager-secretsmanager_SecretId)<br />[secretsmanager:SecretPrimaryRegion](#list_secretsmanager-secretsmanager_SecretPrimaryRegion)
  - **Access level:** Write

- **   [ReplicateSecretToRegions](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ReplicateSecretToRegions.html)  **
  - **Description:** Grants permission to convert an existing secret to a multi-Region secret and begin replicating the secret to a list of new regions
  - **Resource types (\*required):** [Secret\*](#list_secretsmanager-resource-Secret)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_secretsmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_secretsmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_secretsmanager-aws_TagKeys)<br />[secretsmanager:AddReplicaRegions](#list_secretsmanager-secretsmanager_AddReplicaRegions)<br />[secretsmanager:ForceOverwriteReplicaSecret](#list_secretsmanager-secretsmanager_ForceOverwriteReplicaSecret)<br />[secretsmanager:resource/AllowRotationLambdaArn](#list_secretsmanager-secretsmanager_resource_AllowRotationLambdaArn)<br />[secretsmanager:resource/Type](#list_secretsmanager-secretsmanager_resource_Type)<br />[secretsmanager:ResourceTag/tag-key](#list_secretsmanager-secretsmanager_ResourceTag_tag-key)<br />[secretsmanager:SecretId](#list_secretsmanager-secretsmanager_SecretId)<br />[secretsmanager:SecretPrimaryRegion](#list_secretsmanager-secretsmanager_SecretPrimaryRegion)
  - **Access level:** Write

- **   [RestoreSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RestoreSecret.html)  **
  - **Description:** Grants permission to cancel deletion of a secret
  - **Resource types (\*required):** [Secret\*](#list_secretsmanager-resource-Secret)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_secretsmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_secretsmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_secretsmanager-aws_TagKeys)<br />[secretsmanager:resource/AllowRotationLambdaArn](#list_secretsmanager-secretsmanager_resource_AllowRotationLambdaArn)<br />[secretsmanager:resource/Type](#list_secretsmanager-secretsmanager_resource_Type)<br />[secretsmanager:ResourceTag/tag-key](#list_secretsmanager-secretsmanager_ResourceTag_tag-key)<br />[secretsmanager:SecretId](#list_secretsmanager-secretsmanager_SecretId)<br />[secretsmanager:SecretPrimaryRegion](#list_secretsmanager-secretsmanager_SecretPrimaryRegion)
  - **Access level:** Write

- **   [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html)  **
  - **Description:** Grants permission to start rotation of a secret
  - **Resource types (\*required):** [Secret\*](#list_secretsmanager-resource-Secret)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_secretsmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_secretsmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_secretsmanager-aws_TagKeys)<br />[secretsmanager:ExternalSecretRotationRoleArn](#list_secretsmanager-secretsmanager_ExternalSecretRotationRoleArn)<br />[secretsmanager:ModifyRotationRules](#list_secretsmanager-secretsmanager_ModifyRotationRules)<br />[secretsmanager:resource/AllowRotationLambdaArn](#list_secretsmanager-secretsmanager_resource_AllowRotationLambdaArn)<br />[secretsmanager:resource/Type](#list_secretsmanager-secretsmanager_resource_Type)<br />[secretsmanager:ResourceTag/tag-key](#list_secretsmanager-secretsmanager_ResourceTag_tag-key)<br />[secretsmanager:RotateImmediately](#list_secretsmanager-secretsmanager_RotateImmediately)<br />[secretsmanager:RotationLambdaARN](#list_secretsmanager-secretsmanager_RotationLambdaARN)<br />[secretsmanager:SecretId](#list_secretsmanager-secretsmanager_SecretId)<br />[secretsmanager:SecretPrimaryRegion](#list_secretsmanager-secretsmanager_SecretPrimaryRegion)
  - **Access level:** Write

- **   [StopReplicationToReplica](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_StopReplicationToReplica.html)  **
  - **Description:** Grants permission to remove the secret from replication and promote the secret to a regional secret in the replica Region
  - **Resource types (\*required):** [Secret\*](#list_secretsmanager-resource-Secret)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_secretsmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_secretsmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_secretsmanager-aws_TagKeys)<br />[secretsmanager:resource/AllowRotationLambdaArn](#list_secretsmanager-secretsmanager_resource_AllowRotationLambdaArn)<br />[secretsmanager:resource/Type](#list_secretsmanager-secretsmanager_resource_Type)<br />[secretsmanager:ResourceTag/tag-key](#list_secretsmanager-secretsmanager_ResourceTag_tag-key)<br />[secretsmanager:SecretId](#list_secretsmanager-secretsmanager_SecretId)<br />[secretsmanager:SecretPrimaryRegion](#list_secretsmanager-secretsmanager_SecretPrimaryRegion)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a secret
  - **Resource types (\*required):** [Secret\*](#list_secretsmanager-resource-Secret)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_secretsmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_secretsmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_secretsmanager-aws_TagKeys)<br />[secretsmanager:resource/AllowRotationLambdaArn](#list_secretsmanager-secretsmanager_resource_AllowRotationLambdaArn)<br />[secretsmanager:resource/Type](#list_secretsmanager-secretsmanager_resource_Type)<br />[secretsmanager:ResourceTag/tag-key](#list_secretsmanager-secretsmanager_ResourceTag_tag-key)<br />[secretsmanager:SecretId](#list_secretsmanager-secretsmanager_SecretId)<br />[secretsmanager:SecretPrimaryRegion](#list_secretsmanager-secretsmanager_SecretPrimaryRegion)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a secret
  - **Resource types (\*required):** [Secret\*](#list_secretsmanager-resource-Secret)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_secretsmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_secretsmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_secretsmanager-aws_TagKeys)<br />[secretsmanager:resource/AllowRotationLambdaArn](#list_secretsmanager-secretsmanager_resource_AllowRotationLambdaArn)<br />[secretsmanager:resource/Type](#list_secretsmanager-secretsmanager_resource_Type)<br />[secretsmanager:ResourceTag/tag-key](#list_secretsmanager-secretsmanager_ResourceTag_tag-key)<br />[secretsmanager:SecretId](#list_secretsmanager-secretsmanager_SecretId)<br />[secretsmanager:SecretPrimaryRegion](#list_secretsmanager-secretsmanager_SecretPrimaryRegion)
  - **Access level:** Tagging, Write

- **   [UpdateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_UpdateSecret.html)  **
  - **Description:** Grants permission to update a secret with new metadata or with a new version of the encrypted data
  - **Resource types (\*required):** [Secret\*](#list_secretsmanager-resource-Secret)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_secretsmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_secretsmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_secretsmanager-aws_TagKeys)<br />[secretsmanager:Description](#list_secretsmanager-secretsmanager_Description)<br />[secretsmanager:KmsKeyArn](#list_secretsmanager-secretsmanager_KmsKeyArn)<br />[secretsmanager:KmsKeyId](#list_secretsmanager-secretsmanager_KmsKeyId)<br />[secretsmanager:resource/AllowRotationLambdaArn](#list_secretsmanager-secretsmanager_resource_AllowRotationLambdaArn)<br />[secretsmanager:resource/Type](#list_secretsmanager-secretsmanager_resource_Type)<br />[secretsmanager:ResourceTag/tag-key](#list_secretsmanager-secretsmanager_ResourceTag_tag-key)<br />[secretsmanager:SecretId](#list_secretsmanager-secretsmanager_SecretId)<br />[secretsmanager:SecretPrimaryRegion](#list_secretsmanager-secretsmanager_SecretPrimaryRegion)<br />[secretsmanager:Type](#list_secretsmanager-secretsmanager_Type)
  - **Access level:** Write

- **   [UpdateSecretVersionStage](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_UpdateSecretVersionStage.html)  **
  - **Description:** Grants permission to move a stage from one secret to another
  - **Resource types (\*required):** [Secret\*](#list_secretsmanager-resource-Secret)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_secretsmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_secretsmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_secretsmanager-aws_TagKeys)<br />[secretsmanager:resource/AllowRotationLambdaArn](#list_secretsmanager-secretsmanager_resource_AllowRotationLambdaArn)<br />[secretsmanager:resource/Type](#list_secretsmanager-secretsmanager_resource_Type)<br />[secretsmanager:ResourceTag/tag-key](#list_secretsmanager-secretsmanager_ResourceTag_tag-key)<br />[secretsmanager:SecretId](#list_secretsmanager-secretsmanager_SecretId)<br />[secretsmanager:SecretPrimaryRegion](#list_secretsmanager-secretsmanager_SecretPrimaryRegion)<br />[secretsmanager:VersionStage](#list_secretsmanager-secretsmanager_VersionStage)
  - **Access level:** Write

- **   [ValidateResourcePolicy](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ValidateResourcePolicy.html)  **
  - **Description:** Grants permission to validate a resource policy before attaching policy
  - **Resource types (\*required):** [Secret\*](#list_secretsmanager-resource-Secret)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_secretsmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_secretsmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_secretsmanager-aws_TagKeys)<br />[secretsmanager:resource/AllowRotationLambdaArn](#list_secretsmanager-secretsmanager_resource_AllowRotationLambdaArn)<br />[secretsmanager:resource/Type](#list_secretsmanager-secretsmanager_resource_Type)<br />[secretsmanager:ResourceTag/tag-key](#list_secretsmanager-secretsmanager_ResourceTag_tag-key)<br />[secretsmanager:SecretId](#list_secretsmanager-secretsmanager_SecretId)<br />[secretsmanager:SecretPrimaryRegion](#list_secretsmanager-secretsmanager_SecretPrimaryRegion)
  - **Access level:** Permissions management, Write



## Resource types defined by AWS Secrets Manager
<a name="list_secretsmanager-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Secret](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssecretsmanager.html#awssecretsmanager-resources-for-iam-policies)  | arn:${Partition}:secretsmanager:${Region}:${Account}:secret:${SecretId} | [aws:RequestTag/${TagKey}](#list_secretsmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_secretsmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_secretsmanager-aws_TagKeys)<br />[secretsmanager:ResourceTag/tag-key](#list_secretsmanager-secretsmanager_ResourceTag_tag-key)<br />[secretsmanager:resource/AllowRotationLambdaArn](#list_secretsmanager-secretsmanager_resource_AllowRotationLambdaArn)<br />[secretsmanager:resource/Type](#list_secretsmanager-secretsmanager_resource_Type) | 

## Condition keys for AWS Secrets Manager
<a name="list_secretsmanager-policy-keys"></a>

AWS Secrets Manager defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a key that is present in the request the user makes to the Secrets Manager service | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the list of all the tag key names present in the request the user makes to the Secrets Manager service | ArrayOfString | 
|   [secretsmanager:AddReplicaRegions](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by the list of Regions in which to replicate the secret | ArrayOfString | 
|   [secretsmanager:BlockPublicPolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by whether the resource policy blocks broad AWS account access | Bool | 
|   [secretsmanager:Description](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by the description text in the request | String | 
|   [secretsmanager:ExternalSecretRotationRoleArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by the managed external secret rotation role ARN in the request | ARN | 
|   [secretsmanager:ForceDeleteWithoutRecovery](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by whether the secret is to be deleted immediately without any recovery window | Bool | 
|   [secretsmanager:ForceOverwriteReplicaSecret](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by whether to overwrite a secret with the same name in the destination Region | Bool | 
|   [secretsmanager:KmsKeyArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by the key ARN of the KMS key in the request | ARN | 
|   [secretsmanager:KmsKeyId](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by the key identifier of the KMS key in the request. Deprecated: Use secretsmanager:KmsKeyArn | String | 
|   [secretsmanager:ModifyRotationRules](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by whether the rotation rules of the secret are to be modified | Bool | 
|   [secretsmanager:Name](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by the friendly name of the secret in the request | String | 
|   [secretsmanager:RecoveryWindowInDays](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by the number of days that Secrets Manager waits before it can delete the secret | Numeric | 
|   [secretsmanager:ResourceTag/tag-key](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by a tag key and value pair | String | 
|   [secretsmanager:RotateImmediately](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by whether the secret is to be rotated immediately | Bool | 
|   [secretsmanager:RotationLambdaARN](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by the ARN of the rotation Lambda function in the request | ARN | 
|   [secretsmanager:SecretId](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by the SecretID value in the request | ARN | 
|   [secretsmanager:SecretPrimaryRegion](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by primary region in which the secret is created if the secret is a multi-Region secret | String | 
|   [secretsmanager:Type](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by the managed external secret type in the request | String | 
|   [secretsmanager:VersionId](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by the unique identifier of the version of the secret in the request | String | 
|   [secretsmanager:VersionStage](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by the list of version stages in the request | String | 
|   [secretsmanager:resource/AllowRotationLambdaArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by the ARN of the rotation Lambda function associated with the secret | ARN | 
|   [secretsmanager:resource/Type](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by the managed external secret type associated with the secret | String | 