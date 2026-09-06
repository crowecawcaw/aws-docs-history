

# Actions, resources, and condition keys for AWS Agent Registry
<a name="list_agent-registry"></a>

AWS Agent Registry (service prefix: `agent-registry`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/agent-registry/latest/APIReference/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/agent-registry/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/agent-registry/latest/APIReference/) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/agent-registry/agent-registry.json) for this service.

**Topics**
+ [API operations defined by AWS Agent Registry](#list_agent-registry-operations)
+ [Actions defined by AWS Agent Registry](#list_agent-registry-actions-as-permissions)
+ [Permission-only actions for AWS Agent Registry](#list_agent-registry-permission-only-actions)
+ [Resource types defined by AWS Agent Registry](#list_agent-registry-resources-for-iam-policies)
+ [Condition keys for AWS Agent Registry](#list_agent-registry-policy-keys)

## API operations defined by AWS Agent Registry
<a name="list_agent-registry-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_agent-registry-actions-as-permissions).




- **   BatchGetDiscoverableRegistryRecord  **
  - **SDK client:** agent-registry
  - **IAM action:**  [agent-registry:GetDiscoverableRegistryRecord](#list_agent-registry-action-GetDiscoverableRegistryRecord) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDiscoverableRegistryRecords  **
  - **SDK client:** agent-registry
  - **IAM action:**  [agent-registry:ListDiscoverableRegistryRecords](#list_agent-registry-action-ListDiscoverableRegistryRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchDiscoverableRegistryRecords  **
  - **SDK client:** agent-registry
  - **IAM action:**  [agent-registry:SearchDiscoverableRegistryRecords](#list_agent-registry-action-SearchDiscoverableRegistryRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CreateRegistry  **
  - **SDK client:** agent-registry-control
  - **IAM action:**  [agent-registry:CreateRegistry](#list_agent-registry-action-CreateRegistry)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [agent-registry:TagResource](#list_agent-registry-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRegistryRecord  **
  - **SDK client:** agent-registry-control
  - **IAM action:**  [agent-registry:CreateRegistryRecord](#list_agent-registry-action-CreateRegistryRecord)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [agent-registry:TagResource](#list_agent-registry-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [bedrock-agentcore:GetResourceOauth2Token](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetResourceOauth2Token.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock-agentcore:GetWorkloadAccessToken](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetWorkloadAccessToken.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** agent-registry.amazonaws.com / **Access level:** Write

- **   DeleteRegistry  **
  - **SDK client:** agent-registry-control
  - **IAM action:**  [agent-registry:DeleteRegistry](#list_agent-registry-action-DeleteRegistry) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRegistryRecord  **
  - **SDK client:** agent-registry-control
  - **IAM action:**  [agent-registry:DeleteRegistryRecord](#list_agent-registry-action-DeleteRegistryRecord) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetRegistry  **
  - **SDK client:** agent-registry-control
  - **IAM action:**  [agent-registry:GetRegistry](#list_agent-registry-action-GetRegistry) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRegistryRecord  **
  - **SDK client:** agent-registry-control
  - **IAM action:**  [agent-registry:GetRegistryRecord](#list_agent-registry-action-GetRegistryRecord) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListRegistries  **
  - **SDK client:** agent-registry-control
  - **IAM action:**  [agent-registry:ListRegistries](#list_agent-registry-action-ListRegistries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRegistryRecords  **
  - **SDK client:** agent-registry-control
  - **IAM action:**  [agent-registry:ListRegistryRecords](#list_agent-registry-action-ListRegistryRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** agent-registry-control
  - **IAM action:**  [agent-registry:ListTagsForResource](#list_agent-registry-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SubmitRegistryRecordForApproval  **
  - **SDK client:** agent-registry-control
  - **IAM action:**  [agent-registry:SubmitRegistryRecordForApproval](#list_agent-registry-action-SubmitRegistryRecordForApproval) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** agent-registry-control
  - **IAM action:**  [agent-registry:TagResource](#list_agent-registry-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** agent-registry-control
  - **IAM action:**  [agent-registry:UntagResource](#list_agent-registry-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateRegistry  **
  - **SDK client:** agent-registry-control
  - **IAM action:**  [agent-registry:UpdateRegistry](#list_agent-registry-action-UpdateRegistry) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRegistryRecord  **
  - **SDK client:** agent-registry-control
  - **IAM action:**  [agent-registry:UpdateRegistryRecord](#list_agent-registry-action-UpdateRegistryRecord)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:GetResourceOauth2Token](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetResourceOauth2Token.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock-agentcore:GetWorkloadAccessToken](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetWorkloadAccessToken.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** agent-registry.amazonaws.com / **Access level:** Write

- **   UpdateRegistryRecordStatus  **
  - **SDK client:** agent-registry-control
  - **IAM action:**  [agent-registry:UpdateRegistryRecordStatus](#list_agent-registry-action-UpdateRegistryRecordStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Agent Registry
<a name="list_agent-registry-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateRegistry](https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_CreateRegistry.html)  **
  - **Description:** Grants permission to create a new registry
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_agent-registry-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_agent-registry-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRegistryRecord](https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_CreateRegistryRecord.html)  **
  - **Description:** Grants permission to create a new registry record
  - **Resource types (\*required):** [registry\*](#list_agent-registry-resource-registry)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_agent-registry-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_agent-registry-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_agent-registry-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteRegistry](https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_DeleteRegistry.html)  **
  - **Description:** Grants permission to delete an existing registry
  - **Resource types (\*required):** [registry\*](#list_agent-registry-resource-registry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_agent-registry-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRegistryRecord](https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_DeleteRegistryRecord.html)  **
  - **Description:** Grants permission to delete an existing registry record
  - **Resource types (\*required):** [registry-record\*](#list_agent-registry-resource-registry-record)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_agent-registry-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetDiscoverableRegistryRecord](https://docs.aws.amazon.com/agent-registry/latest/APIReference/API_BatchGetDiscoverableRegistryRecord.html)  **
  - **Description:** Grants permission to retrieve an individual approved registry record. This is a permission-only action used for fine-grained access control with BatchGetApprovedRegistryRecord
  - **Resource types (\*required):** [registry-record\*](#list_agent-registry-resource-registry-record)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_agent-registry-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRegistry](https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_GetRegistry.html)  **
  - **Description:** Grants permission to retrieve an existing registry
  - **Resource types (\*required):** [registry\*](#list_agent-registry-resource-registry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_agent-registry-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRegistryRecord](https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_GetRegistryRecord.html)  **
  - **Description:** Grants permission to retrieve an existing registry record
  - **Resource types (\*required):** [registry-record\*](#list_agent-registry-resource-registry-record)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_agent-registry-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InvokeRegistryMcp](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-mcp-endpoint.html)  **
  - **Description:** Grants permission to invoke an MCP operation against an existing registry
  - **Resource types (\*required):** [registry\*](#list_agent-registry-resource-registry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_agent-registry-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDiscoverableRegistryRecords](https://docs.aws.amazon.com/agent-registry/latest/APIReference/API_ListDiscoverableRegistryRecords.html)  **
  - **Description:** Grants permission to list approved registry records in a registry
  - **Resource types (\*required):** [registry\*](#list_agent-registry-resource-registry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_agent-registry-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRegistries](https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_ListRegistries.html)  **
  - **Description:** Grants permission to list existing registries
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRegistryRecords](https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_ListRegistryRecords.html)  **
  - **Description:** Grants permission to list existing registry records in a registry
  - **Resource types (\*required):** [registry\*](#list_agent-registry-resource-registry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_agent-registry-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for an Agent Registry resource
  - **Resource types (\*required):** [registry](#list_agent-registry-resource-registry) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_agent-registry-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [registry-record](#list_agent-registry-resource-registry-record) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_agent-registry-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [SearchDiscoverableRegistryRecords](https://docs.aws.amazon.com/agent-registry/latest/APIReference/API_SearchDiscoverableRegistryRecords.html)  **
  - **Description:** Grants permission to search for registry records
  - **Resource types (\*required):** [registry\*](#list_agent-registry-resource-registry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_agent-registry-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SubmitRegistryRecordForApproval](https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_SubmitRegistryRecordForApproval.html)  **
  - **Description:** Grants permission to submit a registry record for approval
  - **Resource types (\*required):** [registry-record\*](#list_agent-registry-resource-registry-record)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_agent-registry-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag an Agent Registry resource
  - **Resource types (\*required):** [registry](#list_agent-registry-resource-registry) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_agent-registry-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_agent-registry-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_agent-registry-aws_TagKeys)
  - **Resource types (\*required):** [registry-record](#list_agent-registry-resource-registry-record) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_agent-registry-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_agent-registry-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_agent-registry-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag an Agent Registry resource
  - **Resource types (\*required):** [registry](#list_agent-registry-resource-registry) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_agent-registry-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_agent-registry-aws_TagKeys)
  - **Resource types (\*required):** [registry-record](#list_agent-registry-resource-registry-record) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_agent-registry-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_agent-registry-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateRegistry](https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_UpdateRegistry.html)  **
  - **Description:** Grants permission to update an existing registry
  - **Resource types (\*required):** [registry\*](#list_agent-registry-resource-registry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_agent-registry-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRegistryRecord](https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_UpdateRegistryRecord.html)  **
  - **Description:** Grants permission to update an existing registry record
  - **Resource types (\*required):** [registry-record\*](#list_agent-registry-resource-registry-record)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_agent-registry-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRegistryRecordStatus](https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_UpdateRegistryRecordStatus.html)  **
  - **Description:** Grants permission to update the status of a registry record
  - **Resource types (\*required):** [registry-record\*](#list_agent-registry-resource-registry-record)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_agent-registry-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS Agent Registry
<a name="list_agent-registry-permission-only-actions"></a>

The following actions are defined by AWS Agent Registry but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-cross-account-sharing.html)  **
  - **Description:** Grants permission to delete the resource-based policy from a specified resource
  - **Resource types (\*required):** [registry](#list_agent-registry-resource-registry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_agent-registry-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetResourcePolicy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-cross-account-sharing.html)  **
  - **Description:** Grants permission to retrieve the resource-based policy for a specified resource
  - **Resource types (\*required):** [registry](#list_agent-registry-resource-registry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_agent-registry-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutResourcePolicy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-cross-account-sharing.html)  **
  - **Description:** Grants permission to set a resource-based policy for a specified resource
  - **Resource types (\*required):** [registry](#list_agent-registry-resource-registry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_agent-registry-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Agent Registry
<a name="list_agent-registry-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [registry](https://docs.aws.amazon.com/agent-registry/latest/APIReference/registry.html)  | arn:${Partition}:agent-registry:${Region}:${Account}:registry/${RegistryId} | [aws:ResourceTag/${TagKey}](#list_agent-registry-aws_ResourceTag___TagKey_) | 
|  [registry-record](https://docs.aws.amazon.com/agent-registry/latest/APIReference/registryRecord.html)  | arn:${Partition}:agent-registry:${Region}:${Account}:registry/${RegistryId}/record/${RecordId} | [aws:ResourceTag/${TagKey}](#list_agent-registry-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Agent Registry
<a name="list_agent-registry-policy-keys"></a>

AWS Agent Registry defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [agent-registry:RecordCreatorAccount](https://docs.aws.amazon.com/agent-registry/latest/APIReference/)  | Filters access by the AWS account ID of the principal that created the registry record | String | 
|   [agent-registry:RecordSourceAccount](https://docs.aws.amazon.com/agent-registry/latest/APIReference/)  | Filters access by the AWS account ID of the source resource associated with a registry record | String | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-globally-available)  | Filters access by creating requests based on the allowed set of values for each of the mandatory tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-globally-available)  | Filters access by having actions based on the tag value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-globally-available)  | Filters access by creating requests based on the presence of mandatory tags in the request | ArrayOfString | 