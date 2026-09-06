

# Actions, resources, and condition keys for AWS Entity Resolution
<a name="list_entityresolution"></a>

AWS Entity Resolution (service prefix: `entityresolution`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/entityresolution/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/entityresolution/latest/apireference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/entityresolution/latest/userguide/what-is-service.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/entityresolution/entityresolution.json) for this service.

**Topics**
+ [API operations defined by AWS Entity Resolution](#list_entityresolution-operations)
+ [Actions defined by AWS Entity Resolution](#list_entityresolution-actions-as-permissions)
+ [Resource types defined by AWS Entity Resolution](#list_entityresolution-resources-for-iam-policies)
+ [Condition keys for AWS Entity Resolution](#list_entityresolution-policy-keys)

## API operations defined by AWS Entity Resolution
<a name="list_entityresolution-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_entityresolution-actions-as-permissions).




- **   AddPolicyStatement  **
  - **IAM action:**  [entityresolution:AddPolicyStatement](#list_entityresolution-action-AddPolicyStatement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   BatchDeleteUniqueId  **
  - **IAM action:**  [entityresolution:BatchDeleteUniqueId](#list_entityresolution-action-BatchDeleteUniqueId) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateIdMappingWorkflow  **
  - **IAM action:**  [entityresolution:CreateIdMappingWorkflow](#list_entityresolution-action-CreateIdMappingWorkflow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [entityresolution:TagResource](#list_entityresolution-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** entityresolution.amazonaws.com / **Access level:** Write

- **   CreateIdNamespace  **
  - **IAM action:**  [entityresolution:CreateIdNamespace](#list_entityresolution-action-CreateIdNamespace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [entityresolution:TagResource](#list_entityresolution-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** entityresolution.amazonaws.com / **Access level:** Write

- **   CreateMatchingWorkflow  **
  - **IAM action:**  [entityresolution:CreateMatchingWorkflow](#list_entityresolution-action-CreateMatchingWorkflow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [entityresolution:TagResource](#list_entityresolution-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** entityresolution.amazonaws.com / **Access level:** Write

- **   CreateSchemaMapping  **
  - **IAM action:**  [entityresolution:CreateSchemaMapping](#list_entityresolution-action-CreateSchemaMapping)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [entityresolution:TagResource](#list_entityresolution-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteIdMappingWorkflow  **
  - **IAM action:**  [entityresolution:DeleteIdMappingWorkflow](#list_entityresolution-action-DeleteIdMappingWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIdNamespace  **
  - **IAM action:**  [entityresolution:DeleteIdNamespace](#list_entityresolution-action-DeleteIdNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMatchingWorkflow  **
  - **IAM action:**  [entityresolution:DeleteMatchingWorkflow](#list_entityresolution-action-DeleteMatchingWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePolicyStatement  **
  - **IAM action:**  [entityresolution:DeletePolicyStatement](#list_entityresolution-action-DeletePolicyStatement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteSchemaMapping  **
  - **IAM action:**  [entityresolution:DeleteSchemaMapping](#list_entityresolution-action-DeleteSchemaMapping) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GenerateMatchId  **
  - **IAM action:**  [entityresolution:GenerateMatchId](#list_entityresolution-action-GenerateMatchId) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetIdMappingJob  **
  - **IAM action:**  [entityresolution:GetIdMappingJob](#list_entityresolution-action-GetIdMappingJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIdMappingWorkflow  **
  - **IAM action:**  [entityresolution:GetIdMappingWorkflow](#list_entityresolution-action-GetIdMappingWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIdNamespace  **
  - **IAM action:**  [entityresolution:GetIdNamespace](#list_entityresolution-action-GetIdNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMatchId  **
  - **IAM action:**  [entityresolution:GetMatchId](#list_entityresolution-action-GetMatchId) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMatchingJob  **
  - **IAM action:**  [entityresolution:GetMatchingJob](#list_entityresolution-action-GetMatchingJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMatchingWorkflow  **
  - **IAM action:**  [entityresolution:GetMatchingWorkflow](#list_entityresolution-action-GetMatchingWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPolicy  **
  - **IAM action:**  [entityresolution:GetPolicy](#list_entityresolution-action-GetPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProviderService  **
  - **IAM action:**  [entityresolution:GetProviderService](#list_entityresolution-action-GetProviderService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSchemaMapping  **
  - **IAM action:**  [entityresolution:GetSchemaMapping](#list_entityresolution-action-GetSchemaMapping) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListIdMappingJobs  **
  - **IAM action:**  [entityresolution:ListIdMappingJobs](#list_entityresolution-action-ListIdMappingJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIdMappingWorkflows  **
  - **IAM action:**  [entityresolution:ListIdMappingWorkflows](#list_entityresolution-action-ListIdMappingWorkflows) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIdNamespaces  **
  - **IAM action:**  [entityresolution:ListIdNamespaces](#list_entityresolution-action-ListIdNamespaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMatchingJobs  **
  - **IAM action:**  [entityresolution:ListMatchingJobs](#list_entityresolution-action-ListMatchingJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMatchingWorkflows  **
  - **IAM action:**  [entityresolution:ListMatchingWorkflows](#list_entityresolution-action-ListMatchingWorkflows) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProviderServices  **
  - **IAM action:**  [entityresolution:ListProviderServices](#list_entityresolution-action-ListProviderServices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSchemaMappings  **
  - **IAM action:**  [entityresolution:ListSchemaMappings](#list_entityresolution-action-ListSchemaMappings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [entityresolution:ListTagsForResource](#list_entityresolution-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutPolicy  **
  - **IAM action:**  [entityresolution:PutPolicy](#list_entityresolution-action-PutPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   StartIdMappingJob  **
  - **IAM action:**  [entityresolution:StartIdMappingJob](#list_entityresolution-action-StartIdMappingJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [entityresolution:UseIdNamespace](#list_entityresolution-action-UseIdNamespace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** entityresolution.amazonaws.com / **Access level:** Write

- **   StartMatchingJob  **
  - **IAM action:**  [entityresolution:StartMatchingJob](#list_entityresolution-action-StartMatchingJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [entityresolution:TagResource](#list_entityresolution-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [entityresolution:UntagResource](#list_entityresolution-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateIdMappingWorkflow  **
  - **IAM action:**  [entityresolution:UpdateIdMappingWorkflow](#list_entityresolution-action-UpdateIdMappingWorkflow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** entityresolution.amazonaws.com / **Access level:** Write

- **   UpdateIdNamespace  **
  - **IAM action:**  [entityresolution:UpdateIdNamespace](#list_entityresolution-action-UpdateIdNamespace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** entityresolution.amazonaws.com / **Access level:** Write

- **   UpdateMatchingWorkflow  **
  - **IAM action:**  [entityresolution:UpdateMatchingWorkflow](#list_entityresolution-action-UpdateMatchingWorkflow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** entityresolution.amazonaws.com / **Access level:** Write

- **   UpdateSchemaMapping  **
  - **IAM action:**  [entityresolution:UpdateSchemaMapping](#list_entityresolution-action-UpdateSchemaMapping) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Entity Resolution
<a name="list_entityresolution-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddPolicyStatement](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_AddPolicyStatement.html)  **
  - **Description:** Grants permission to give an AWS service or another account permission to use an AWS Entity Resolution resources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [BatchDeleteUniqueId](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_BatchDeleteUniqueId.html)  **
  - **Description:** Grants permission to batch delete unique Id
  - **Resource types (\*required):** [MatchingWorkflow\*](#list_entityresolution-resource-MatchingWorkflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateIdMappingWorkflow](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_CreateIdMappingWorkflow.html)  **
  - **Description:** Grants permission to create a idmapping workflow
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_entityresolution-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_entityresolution-aws_TagKeys)
  - **Access level:** Write

- **   [CreateIdNamespace](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_CreateIdNamespace.html)  **
  - **Description:** Grants permission to create a IdNamespace
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_entityresolution-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_entityresolution-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMatchingWorkflow](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_CreateMatchingWorkflow.html)  **
  - **Description:** Grants permission to create a matching workflow
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_entityresolution-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_entityresolution-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSchemaMapping](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_CreateSchemaMapping.html)  **
  - **Description:** Grants permission to create a schema mapping
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_entityresolution-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_entityresolution-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteIdMappingWorkflow](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_DeleteIdMappingWorkflow.html)  **
  - **Description:** Grants permission to delete a idmapping workflow
  - **Resource types (\*required):** [IdMappingWorkflow\*](#list_entityresolution-resource-IdMappingWorkflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIdNamespace](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_DeleteIdNamespace.html)  **
  - **Description:** Grants permission to delete a IdNamespace
  - **Resource types (\*required):** [IdNamespace\*](#list_entityresolution-resource-IdNamespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMatchingWorkflow](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_DeleteMatchingWorkflow.html)  **
  - **Description:** Grants permission to delete a matching workflow
  - **Resource types (\*required):** [MatchingWorkflow\*](#list_entityresolution-resource-MatchingWorkflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePolicyStatement](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_DeletePolicyStatement.html)  **
  - **Description:** Grants permission to delete permission given to an AWS service or another account permission to use an AWS Entity Resolution resources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [DeleteSchemaMapping](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_DeleteSchemaMapping.html)  **
  - **Description:** Grants permission to delete a schema mapping
  - **Resource types (\*required):** [SchemaMapping\*](#list_entityresolution-resource-SchemaMapping)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GenerateMatchId](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GenerateMatchId.html)  **
  - **Description:** Grants permission to generate match Id
  - **Resource types (\*required):** [MatchingWorkflow\*](#list_entityresolution-resource-MatchingWorkflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetIdMappingJob](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetIdMappingJob.html)  **
  - **Description:** Grants permission to get a idmapping job
  - **Resource types (\*required):** [IdMappingWorkflow\*](#list_entityresolution-resource-IdMappingWorkflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIdMappingWorkflow](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetIdMappingWorkflow.html)  **
  - **Description:** Grants permission to get a idmapping workflow
  - **Resource types (\*required):** [IdMappingWorkflow\*](#list_entityresolution-resource-IdMappingWorkflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIdNamespace](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetIdNamespace.html)  **
  - **Description:** Grants permission to get a IdNamespace
  - **Resource types (\*required):** [IdNamespace\*](#list_entityresolution-resource-IdNamespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMatchId](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetMatchId.html)  **
  - **Description:** Grants permission to get match Id
  - **Resource types (\*required):** [MatchingWorkflow\*](#list_entityresolution-resource-MatchingWorkflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMatchingJob](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetMatchingJob.html)  **
  - **Description:** Grants permission to get a matching job
  - **Resource types (\*required):** [MatchingWorkflow\*](#list_entityresolution-resource-MatchingWorkflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMatchingWorkflow](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetMatchingWorkflow.html)  **
  - **Description:** Grants permission to get a matching workflow
  - **Resource types (\*required):** [MatchingWorkflow\*](#list_entityresolution-resource-MatchingWorkflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPolicy](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetPolicy.html)  **
  - **Description:** Grants permission to get a resource policy for an AWS Entity Resolution resources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetProviderService](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetProviderService.html)  **
  - **Description:** Grants permission to get provider service
  - **Resource types (\*required):** [ProviderService\*](#list_entityresolution-resource-ProviderService)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSchemaMapping](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetSchemaMapping.html)  **
  - **Description:** Grants permission to get a schema mapping
  - **Resource types (\*required):** [SchemaMapping\*](#list_entityresolution-resource-SchemaMapping)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListIdMappingJobs](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ListIdMappingJobs.html)  **
  - **Description:** Grants permission to list idmapping jobs
  - **Resource types (\*required):** [IdMappingWorkflow\*](#list_entityresolution-resource-IdMappingWorkflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListIdMappingWorkflows](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ListIdMappingWorkflows.html)  **
  - **Description:** Grants permission to list idmapping workflows
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIdNamespaces](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ListIdNamespaces.html)  **
  - **Description:** Grants permission to list IdNamespaces
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMatchingJobs](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ListMatchingJobs.html)  **
  - **Description:** Grants permission to list matching jobs
  - **Resource types (\*required):** [MatchingWorkflow\*](#list_entityresolution-resource-MatchingWorkflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListMatchingWorkflows](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ListMatchingWorkflows.html)  **
  - **Description:** Grants permission to list matching workflows
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProviderServices](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ListProviderServices.html)  **
  - **Description:** Grants permission to list provider service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSchemaMappings](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ListSchemaMappings.html)  **
  - **Description:** Grants permission to list schema mappings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to List tags for a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [PutPolicy](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_PutPolicy.html)  **
  - **Description:** Grants permission to put a resource policy for an AWS Entity Resolution resources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [StartIdMappingJob](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_StartIdMappingJob.html)  **
  - **Description:** Grants permission to start a idmapping job
  - **Resource types (\*required):** [IdMappingWorkflow\*](#list_entityresolution-resource-IdMappingWorkflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartMatchingJob](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_StartMatchingJob.html)  **
  - **Description:** Grants permission to start a matching job
  - **Resource types (\*required):** [MatchingWorkflow\*](#list_entityresolution-resource-MatchingWorkflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_TagResource.html)  **
  - **Description:** Grants permission to adds tags to a resource
  - **Resource types (\*required):** [IdMappingWorkflow](#list_entityresolution-resource-IdMappingWorkflow) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_entityresolution-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_entityresolution-aws_TagKeys)
  - **Resource types (\*required):** [IdNamespace](#list_entityresolution-resource-IdNamespace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_entityresolution-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_entityresolution-aws_TagKeys)
  - **Resource types (\*required):** [MatchingWorkflow](#list_entityresolution-resource-MatchingWorkflow) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_entityresolution-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_entityresolution-aws_TagKeys)
  - **Resource types (\*required):** [ProviderService](#list_entityresolution-resource-ProviderService) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_entityresolution-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_entityresolution-aws_TagKeys)
  - **Resource types (\*required):** [SchemaMapping](#list_entityresolution-resource-SchemaMapping) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_entityresolution-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_entityresolution-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [IdMappingWorkflow](#list_entityresolution-resource-IdMappingWorkflow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_entityresolution-aws_TagKeys)
  - **Resource types (\*required):** [IdNamespace](#list_entityresolution-resource-IdNamespace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_entityresolution-aws_TagKeys)
  - **Resource types (\*required):** [MatchingWorkflow](#list_entityresolution-resource-MatchingWorkflow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_entityresolution-aws_TagKeys)
  - **Resource types (\*required):** [ProviderService](#list_entityresolution-resource-ProviderService) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_entityresolution-aws_TagKeys)
  - **Resource types (\*required):** [SchemaMapping](#list_entityresolution-resource-SchemaMapping) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_entityresolution-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateIdMappingWorkflow](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_UpdateIdMappingWorkflow.html)  **
  - **Description:** Grants permission to update a idmapping workflow
  - **Resource types (\*required):** [IdMappingWorkflow\*](#list_entityresolution-resource-IdMappingWorkflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateIdNamespace](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_UpdateIdNamespace.html)  **
  - **Description:** Grants permission to update a IdNamespace
  - **Resource types (\*required):** [IdNamespace\*](#list_entityresolution-resource-IdNamespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMatchingWorkflow](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_UpdateMatchingWorkflow.html)  **
  - **Description:** Grants permission to update a matching workflow
  - **Resource types (\*required):** [MatchingWorkflow\*](#list_entityresolution-resource-MatchingWorkflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSchemaMapping](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_UpdateSchemaMapping.html)  **
  - **Description:** Grants permission to update a schema mapping
  - **Resource types (\*required):** [SchemaMapping\*](#list_entityresolution-resource-SchemaMapping)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UseIdNamespace](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_UseIdNamespace.html)  **
  - **Description:** Grants permission to give an AWS service or another account permission to use IdNamespace within a workflow
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [UseWorkflow](https://docs.aws.amazon.com/entityresolution/latest/apireference/API_UseWorkflow.html)  **
  - **Description:** Grants permission to give an AWS service or another account permission to use workflow within a IdNamespace
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write



## Resource types defined by AWS Entity Resolution
<a name="list_entityresolution-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [IdMappingWorkflow](https://docs.aws.amazon.com/entityresolution/latest/userguide/)  | arn:${Partition}:entityresolution:${Region}:${Account}:idmappingworkflow/${WorkflowName} | [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_) | 
|  [IdNamespace](https://docs.aws.amazon.com/entityresolution/latest/userguide/)  | arn:${Partition}:entityresolution:${Region}:${Account}:idnamespace/${IdNamespaceName} | [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_) | 
|  [MatchingWorkflow](https://docs.aws.amazon.com/entityresolution/latest/userguide/)  | arn:${Partition}:entityresolution:${Region}:${Account}:matchingworkflow/${WorkflowName} | [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_) | 
|  [ProviderService](https://docs.aws.amazon.com/entityresolution/latest/userguide/)  | arn:${Partition}:entityresolution:${Region}:${Account}:providerservice/${ProviderName}/${ProviderServiceName} | [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_) | 
|  [SchemaMapping](https://docs.aws.amazon.com/entityresolution/latest/userguide/)  | arn:${Partition}:entityresolution:${Region}:${Account}:schemamapping/${SchemaName} | [aws:ResourceTag/${TagKey}](#list_entityresolution-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Entity Resolution
<a name="list_entityresolution-policy-keys"></a>

AWS Entity Resolution defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-permissions.html#iam-contextkeys)  | Filters access by a key that is present in the request the user makes to the entity resolution service | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-permissions.html#iam-contextkeys)  | Filters access by a tag key and value pair | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-permissions.html#iam-contextkeys)  | Filters access by the list of all the tag key names present in the request the user makes to the entity resolution service | ArrayOfString | 