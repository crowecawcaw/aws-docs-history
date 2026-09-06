

# Actions, resources, and condition keys for Amazon OpenSearch Ingestion
<a name="list_osis"></a>

Amazon OpenSearch Ingestion (service prefix: `osis`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_Operations_Amazon_OpenSearch_Ingestion.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/osis/osis.json) for this service.

**Topics**
+ [API operations defined by Amazon OpenSearch Ingestion](#list_osis-operations)
+ [Actions defined by Amazon OpenSearch Ingestion](#list_osis-actions-as-permissions)
+ [Resource types defined by Amazon OpenSearch Ingestion](#list_osis-resources-for-iam-policies)
+ [Condition keys for Amazon OpenSearch Ingestion](#list_osis-policy-keys)

## API operations defined by Amazon OpenSearch Ingestion
<a name="list_osis-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_osis-actions-as-permissions).




- **   CreatePipeline  **
  - **IAM action:**  [osis:CreatePipeline](#list_osis-action-CreatePipeline)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [osis:TagResource](#list_osis-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** osis-pipelines.amazonaws.com / **Access level:** Write

- **   CreatePipelineEndpoint  **
  - **IAM action:**  [osis:CreatePipelineEndpoint](#list_osis-action-CreatePipelineEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePipeline  **
  - **IAM action:**  [osis:DeletePipeline](#list_osis-action-DeletePipeline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePipelineEndpoint  **
  - **IAM action:**  [osis:DeletePipelineEndpoint](#list_osis-action-DeletePipelineEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **IAM action:**  [osis:DeleteResourcePolicy](#list_osis-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetPipeline  **
  - **IAM action:**  [osis:GetPipeline](#list_osis-action-GetPipeline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPipelineBlueprint  **
  - **IAM action:**  [osis:GetPipelineBlueprint](#list_osis-action-GetPipelineBlueprint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPipelineChangeProgress  **
  - **IAM action:**  [osis:GetPipelineChangeProgress](#list_osis-action-GetPipelineChangeProgress) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **IAM action:**  [osis:GetResourcePolicy](#list_osis-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPipelineBlueprints  **
  - **IAM action:**  [osis:ListPipelineBlueprints](#list_osis-action-ListPipelineBlueprints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPipelineEndpointConnections  **
  - **IAM action:**  [osis:ListPipelineEndpointConnections](#list_osis-action-ListPipelineEndpointConnections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPipelineEndpoints  **
  - **IAM action:**  [osis:ListPipelineEndpoints](#list_osis-action-ListPipelineEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPipelines  **
  - **IAM action:**  [osis:ListPipelines](#list_osis-action-ListPipelines) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [osis:ListTagsForResource](#list_osis-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutResourcePolicy  **
  - **IAM action:**  [osis:PutResourcePolicy](#list_osis-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RevokePipelineEndpointConnections  **
  - **IAM action:**  [osis:RevokePipelineEndpointConnections](#list_osis-action-RevokePipelineEndpointConnections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartPipeline  **
  - **IAM action:**  [osis:StartPipeline](#list_osis-action-StartPipeline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopPipeline  **
  - **IAM action:**  [osis:StopPipeline](#list_osis-action-StopPipeline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [osis:TagResource](#list_osis-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [osis:UntagResource](#list_osis-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdatePipeline  **
  - **IAM action:**  [osis:UpdatePipeline](#list_osis-action-UpdatePipeline)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** osis-pipelines.amazonaws.com / **Access level:** Write

- **   ValidatePipeline  **
  - **IAM action:**  [osis:ValidatePipeline](#list_osis-action-ValidatePipeline)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** osis-pipelines.amazonaws.com / **Access level:** Write



## Actions defined by Amazon OpenSearch Ingestion
<a name="list_osis-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreatePipeline](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_CreatePipeline.html)  **
  - **Description:** Grants permission to create an OpenSearch Ingestion pipeline
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_osis-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_osis-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePipelineEndpoint](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_CreatePipelineEndpoint.html)  **
  - **Description:** Grants permission to create an OpenSearch Ingestion pipeline endpoint
  - **Resource types (\*required):** [pipeline\*](#list_osis-resource-pipeline)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_osis-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_osis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_osis-aws_TagKeys)
  - **Access level:** Write

- **   [DeletePipeline](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_DeletePipeline.html)  **
  - **Description:** Grants permission to delete an OpenSearch Ingestion pipeline
  - **Resource types (\*required):** [pipeline\*](#list_osis-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_osis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePipelineEndpoint](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_DeletePipelineEndpoint.html)  **
  - **Description:** Grants permission to delete an OpenSearch Ingestion pipeline endpoint in the current account
  - **Resource types (\*required):** [pipeline-endpoint\*](#list_osis-resource-pipeline-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_osis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete a resource policy for an OpenSearch Ingestion resource
  - **Resource types (\*required):** [pipeline\*](#list_osis-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_osis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetPipeline](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_GetPipeline.html)  **
  - **Description:** Grants permission to retrieve configuration information for an OpenSearch Ingestion pipeline
  - **Resource types (\*required):** [pipeline\*](#list_osis-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_osis-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPipelineBlueprint](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_GetPipelineBlueprint.html)  **
  - **Description:** Grants permission to get the contents of an OpenSearch Ingestion pipeline blueprint
  - **Resource types (\*required):** [pipeline-blueprint\*](#list_osis-resource-pipeline-blueprint)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPipelineChangeProgress](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_GetPipelineChangeProgress.html)  **
  - **Description:** Grants permission to get granular information about the status of an OpenSearch Ingestion pipeline
  - **Resource types (\*required):** [pipeline\*](#list_osis-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_osis-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_GetResourcePolicy.html)  **
  - **Description:** Grants permission to get a resource policy for an OpenSearch Ingestion resource
  - **Resource types (\*required):** [pipeline\*](#list_osis-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_osis-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [Ingest](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client.html)  **
  - **Description:** Grants permission to ingest data through an OpenSearch Ingestion pipeline
  - **Resource types (\*required):** [pipeline\*](#list_osis-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_osis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListPipelineBlueprints](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_ListPipelineBlueprints.html)  **
  - **Description:** Grants permission to list the names of available blueprints for an OpenSearch Ingestion pipeline configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPipelineEndpointConnections](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_ListPipelineEndpointConnections.html)  **
  - **Description:** Grants permission to list OpenSearch Ingestion pipeline endpoint connections to pipelines in the current account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPipelineEndpoints](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_ListPipelineEndpoints.html)  **
  - **Description:** Grants permission to list OpenSearch Ingestion pipeline endpoints in the current account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPipelines](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_ListPipelines.html)  **
  - **Description:** Grants permission to list basic configuration for each OpenSearch Ingestion pipeline in the current account and Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_ListTagsForResource.html)  **
  - **Description:** Grants permission to list all resource tags associated with an OpenSearch Ingestion pipeline
  - **Resource types (\*required):** [pipeline\*](#list_osis-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_osis-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutResourcePolicy](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_PutResourcePolicy.html)  **
  - **Description:** Grants permission to put a resource policy for an OpenSearch Ingestion resource
  - **Resource types (\*required):** [pipeline\*](#list_osis-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_osis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RevokePipelineEndpointConnections](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_RevokePipelineEndpointConnections.html)  **
  - **Description:** Grants permission to revoke an OpenSearch Ingestion pipeline endpoint connection from a pipeline in the current account
  - **Resource types (\*required):** [pipeline\*](#list_osis-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_osis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartPipeline](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_StartPipeline.html)  **
  - **Description:** Grants permission to start an OpenSearch Ingestion pipeline
  - **Resource types (\*required):** [pipeline\*](#list_osis-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_osis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopPipeline](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_StopPipeline.html)  **
  - **Description:** Grants permission to stop an OpenSearch Ingestion pipeline
  - **Resource types (\*required):** [pipeline\*](#list_osis-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_osis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_TagResource.html)  **
  - **Description:** Grants permission to attach resource tags to an OpenSearch Ingestion pipeline
  - **Resource types (\*required):** [pipeline\*](#list_osis-resource-pipeline)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_osis-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_osis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_osis-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_UntagResource.html)  **
  - **Description:** Grants permission to remove resource tags from an OpenSearch Ingestion Service pipeline
  - **Resource types (\*required):** [pipeline\*](#list_osis-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_osis-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_osis-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdatePipeline](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_UpdatePipeline.html)  **
  - **Description:** Grants permission to modify the configuration of an OpenSearch Ingestion pipeline
  - **Resource types (\*required):** [pipeline\*](#list_osis-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_osis-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ValidatePipeline](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_ValidatePipeline.html)  **
  - **Description:** Grants permission to validate the configuration of an OpenSearch Ingestion pipeline
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read



## Resource types defined by Amazon OpenSearch Ingestion
<a name="list_osis-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [pipeline](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_Pipeline.html)  | arn:${Partition}:osis:${Region}:${Account}:pipeline/${PipelineName} | [aws:ResourceTag/${TagKey}](#list_osis-aws_ResourceTag___TagKey_) | 
|  [pipeline-blueprint](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_PipelineBlueprint.html)  | arn:${Partition}:osis:${Region}:${Account}:blueprint/${BlueprintName} |   | 
|  [pipeline-endpoint](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_PipelineEndpoint.html)  | arn:${Partition}:osis:${Region}:${Account}:endpoint/${EndpointId} | [aws:ResourceTag/${TagKey}](#list_osis-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon OpenSearch Ingestion
<a name="list_osis-policy-keys"></a>

Amazon OpenSearch Ingestion defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 