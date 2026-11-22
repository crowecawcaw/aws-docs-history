

# Actions, resources, and condition keys for Amazon OpenSearch Memory

Amazon OpenSearch Memory (service prefix: `osm`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/memory.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/security-iam-memory.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/osm/osm.json) for this service.

**Topics**
+ [Actions defined by Amazon OpenSearch Memory](#list_opensearchmemory-actions-as-permissions)
+ [Resource types defined by Amazon OpenSearch Memory](#list_opensearchmemory-resources-for-iam-policies)
+ [Condition keys for Amazon OpenSearch Memory](#list_opensearchmemory-policy-keys)

## Actions defined by Amazon OpenSearch Memory
<a name="list_opensearchmemory-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. For each action, the table lists the resource types and condition keys supported by that action. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchGetEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_BatchGetEvent.html)  **
  - **Description:** Grants permission to retrieve multiple events from a session in an OpenSearch Memory space
  - **Resource types (\*required):** [space\*](#list_opensearchmemory-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_opensearchmemory-aws_ResourceTag___TagKey_)<br />[osm:actorId](#list_opensearchmemory-osm_actorId)<br />[osm:sessionId](#list_opensearchmemory-osm_sessionId)
  - **Access level:** Read

- **   [CreateEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateEvent.html)  **
  - **Description:** Grants permission to submit an event to a session within an OpenSearch Memory space
  - **Resource types (\*required):** [space\*](#list_opensearchmemory-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_opensearchmemory-aws_ResourceTag___TagKey_)<br />[osm:actorId](#list_opensearchmemory-osm_actorId)<br />[osm:sessionId](#list_opensearchmemory-osm_sessionId)
  - **Access level:** Write

- **   [CreateMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateMemory.html)  **
  - **Description:** Grants permission to submit a pre-formed memory into an OpenSearch Memory space
  - **Resource types (\*required):** [space\*](#list_opensearchmemory-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_opensearchmemory-aws_ResourceTag___TagKey_)<br />[osm:actorId](#list_opensearchmemory-osm_actorId)<br />[osm:strategyName](#list_opensearchmemory-osm_strategyName)
  - **Access level:** Write

- **   [CreateSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateSpace.html)  **
  - **Description:** Grants permission to create an OpenSearch Memory space
  - **Resource types (\*required):** [space\*](#list_opensearchmemory-resource-space)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_opensearchmemory-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_opensearchmemory-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_opensearchmemory-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteEvent.html)  **
  - **Description:** Grants permission to delete an event from a session within an OpenSearch Memory space
  - **Resource types (\*required):** [space\*](#list_opensearchmemory-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_opensearchmemory-aws_ResourceTag___TagKey_)<br />[osm:actorId](#list_opensearchmemory-osm_actorId)<br />[osm:sessionId](#list_opensearchmemory-osm_sessionId)
  - **Access level:** Write

- **   [DeleteMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteMemory.html)  **
  - **Description:** Grants permission to delete a single memory from an OpenSearch Memory space
  - **Resource types (\*required):** [space\*](#list_opensearchmemory-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_opensearchmemory-aws_ResourceTag___TagKey_)<br />[osm:actorId](#list_opensearchmemory-osm_actorId)<br />[osm:strategyName](#list_opensearchmemory-osm_strategyName)
  - **Access level:** Write

- **   [DeleteSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteSpace.html)  **
  - **Description:** Grants permission to delete an OpenSearch Memory space
  - **Resource types (\*required):** [space\*](#list_opensearchmemory-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_opensearchmemory-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetEvent.html)  **
  - **Description:** Grants permission to retrieve a single event from an OpenSearch Memory space
  - **Resource types (\*required):** [space\*](#list_opensearchmemory-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_opensearchmemory-aws_ResourceTag___TagKey_)<br />[osm:actorId](#list_opensearchmemory-osm_actorId)<br />[osm:sessionId](#list_opensearchmemory-osm_sessionId)
  - **Access level:** Read

- **   [GetMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetMemory.html)  **
  - **Description:** Grants permission to retrieve a single memory from an OpenSearch Memory space
  - **Resource types (\*required):** [space\*](#list_opensearchmemory-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_opensearchmemory-aws_ResourceTag___TagKey_)<br />[osm:actorId](#list_opensearchmemory-osm_actorId)<br />[osm:strategyName](#list_opensearchmemory-osm_strategyName)
  - **Access level:** Read

- **   [GetSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetSpace.html)  **
  - **Description:** Grants permission to retrieve metadata about an OpenSearch Memory space
  - **Resource types (\*required):** [space\*](#list_opensearchmemory-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_opensearchmemory-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListEvents](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListEvents.html)  **
  - **Description:** Grants permission to list event metadata for a session within an OpenSearch Memory space
  - **Resource types (\*required):** [space\*](#list_opensearchmemory-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_opensearchmemory-aws_ResourceTag___TagKey_)<br />[osm:actorId](#list_opensearchmemory-osm_actorId)<br />[osm:sessionId](#list_opensearchmemory-osm_sessionId)
  - **Access level:** List

- **   [ListMemories](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListMemories.html)  **
  - **Description:** Grants permission to enumerate the memories in an OpenSearch Memory space
  - **Resource types (\*required):** [space\*](#list_opensearchmemory-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_opensearchmemory-aws_ResourceTag___TagKey_)<br />[osm:actorId](#list_opensearchmemory-osm_actorId)<br />[osm:strategyName](#list_opensearchmemory-osm_strategyName)
  - **Access level:** List

- **   [ListSpaces](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListSpaces.html)  **
  - **Description:** Grants permission to list the OpenSearch Memory spaces in the account
  - **Resource types (\*required):** [space\*](#list_opensearchmemory-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_opensearchmemory-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags on an OpenSearch Memory space
  - **Resource types (\*required):** [space\*](#list_opensearchmemory-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_opensearchmemory-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SearchEvents](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchEvents.html)  **
  - **Description:** Grants permission to run a relevance search over the raw event index of an OpenSearch Memory space
  - **Resource types (\*required):** [space\*](#list_opensearchmemory-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_opensearchmemory-aws_ResourceTag___TagKey_)<br />[osm:actorId](#list_opensearchmemory-osm_actorId)<br />[osm:sessionId](#list_opensearchmemory-osm_sessionId)
  - **Access level:** Read

- **   [SearchMemories](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchMemories.html)  **
  - **Description:** Grants permission to run a relevance search over the memory indexes of an OpenSearch Memory space
  - **Resource types (\*required):** [space\*](#list_opensearchmemory-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_opensearchmemory-aws_ResourceTag___TagKey_)<br />[osm:actorId](#list_opensearchmemory-osm_actorId)<br />[osm:strategyName](#list_opensearchmemory-osm_strategyName)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add or overwrite tags on an OpenSearch Memory space
  - **Resource types (\*required):** [space\*](#list_opensearchmemory-resource-space)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_opensearchmemory-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_opensearchmemory-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_opensearchmemory-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from an OpenSearch Memory space
  - **Resource types (\*required):** [space\*](#list_opensearchmemory-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_opensearchmemory-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_opensearchmemory-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_UpdateMemory.html)  **
  - **Description:** Grants permission to update a single memory in an OpenSearch Memory space
  - **Resource types (\*required):** [space\*](#list_opensearchmemory-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_opensearchmemory-aws_ResourceTag___TagKey_)<br />[osm:actorId](#list_opensearchmemory-osm_actorId)<br />[osm:strategyName](#list_opensearchmemory-osm_strategyName)
  - **Access level:** Write

- **   [UpdateSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_UpdateSpace.html)  **
  - **Description:** Grants permission to update the configuration of an OpenSearch Memory space
  - **Resource types (\*required):** [space\*](#list_opensearchmemory-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_opensearchmemory-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon OpenSearch Memory
<a name="list_opensearchmemory-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [space](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/security-iam-memory.html#security-iam-memory-id-based-policies-resources)  | arn:${Partition}:osm:${Region}:${Account}:space/${SpaceId} | [aws:ResourceTag/${TagKey}](#list_opensearchmemory-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon OpenSearch Memory
<a name="list_opensearchmemory-policy-keys"></a>

Amazon OpenSearch Memory defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [osm:actorId](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/security-iam-memory.html#security_iam_memory-conditionkeys)  | Filters access by the actor IDs specified in the request | ArrayOfString | 
|   [osm:sessionId](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/security-iam-memory.html#security_iam_memory-conditionkeys)  | Filters access by the session IDs specified in the request | ArrayOfString | 
|   [osm:strategyName](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/security-iam-memory.html#security_iam_memory-conditionkeys)  | Filters access by the memory strategy names specified in the request | ArrayOfString | 