

# Actions, resources, and condition keys for Amazon OpenSearch Serverless
<a name="list_opensearchserverless"></a>

Amazon OpenSearch Serverless (service prefix: `aoss`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/security-iam-serverless.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/aoss/aoss.json) for this service.

**Topics**
+ [API operations defined by Amazon OpenSearch Serverless](#list_opensearchserverless-operations)
+ [Actions defined by Amazon OpenSearch Serverless](#list_opensearchserverless-actions-as-permissions)
+ [Resource types defined by Amazon OpenSearch Serverless](#list_opensearchserverless-resources-for-iam-policies)
+ [Condition keys for Amazon OpenSearch Serverless](#list_opensearchserverless-policy-keys)

## API operations defined by Amazon OpenSearch Serverless
<a name="list_opensearchserverless-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_opensearchserverless-actions-as-permissions).




- **   BatchGetCollection  **
  - **IAM action:**  [aoss:BatchGetCollection](#list_opensearchserverless-action-BatchGetCollection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetCollectionGroup  **
  - **IAM action:**  [aoss:BatchGetCollectionGroup](#list_opensearchserverless-action-BatchGetCollectionGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetEffectiveLifecyclePolicy  **
  - **IAM action:**  [aoss:BatchGetEffectiveLifecyclePolicy](#list_opensearchserverless-action-BatchGetEffectiveLifecyclePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetLifecyclePolicy  **
  - **IAM action:**  [aoss:BatchGetLifecyclePolicy](#list_opensearchserverless-action-BatchGetLifecyclePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetVpcEndpoint  **
  - **IAM action:**  [aoss:BatchGetVpcEndpoint](#list_opensearchserverless-action-BatchGetVpcEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CreateAccessPolicy  **
  - **IAM action:**  [aoss:CreateAccessPolicy](#list_opensearchserverless-action-CreateAccessPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCollection  **
  - **IAM action:**  [aoss:AddCollectionToCollectionGroup](#list_opensearchserverless-action-AddCollectionToCollectionGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aoss:CreateCollection](#list_opensearchserverless-action-CreateCollection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aoss:TagResource](#list_opensearchserverless-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateCollectionGroup  **
  - **IAM action:**  [aoss:CreateCollectionGroup](#list_opensearchserverless-action-CreateCollectionGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aoss:TagResource](#list_opensearchserverless-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateIndex  **
  - **IAM action:**  [aoss:CreateIndex](#list_opensearchserverless-action-CreateIndex) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateLifecyclePolicy  **
  - **IAM action:**  [aoss:CreateLifecyclePolicy](#list_opensearchserverless-action-CreateLifecyclePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSecurityConfig  **
  - **IAM action:**  [aoss:CreateSecurityConfig](#list_opensearchserverless-action-CreateSecurityConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSecurityPolicy  **
  - **IAM action:**  [aoss:CreateSecurityPolicy](#list_opensearchserverless-action-CreateSecurityPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateVpcEndpoint  **
  - **IAM action:**  [aoss:CreateVpcEndpoint](#list_opensearchserverless-action-CreateVpcEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAccessPolicy  **
  - **IAM action:**  [aoss:DeleteAccessPolicy](#list_opensearchserverless-action-DeleteAccessPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCollection  **
  - **IAM action:**  [aoss:DeleteCollection](#list_opensearchserverless-action-DeleteCollection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCollectionGroup  **
  - **IAM action:**  [aoss:DeleteCollectionGroup](#list_opensearchserverless-action-DeleteCollectionGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIndex  **
  - **IAM action:**  [aoss:DeleteIndex](#list_opensearchserverless-action-DeleteIndex) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLifecyclePolicy  **
  - **IAM action:**  [aoss:DeleteLifecyclePolicy](#list_opensearchserverless-action-DeleteLifecyclePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSecurityConfig  **
  - **IAM action:**  [aoss:DeleteSecurityConfig](#list_opensearchserverless-action-DeleteSecurityConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSecurityPolicy  **
  - **IAM action:**  [aoss:DeleteSecurityPolicy](#list_opensearchserverless-action-DeleteSecurityPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVpcEndpoint  **
  - **IAM action:**  [aoss:DeleteVpcEndpoint](#list_opensearchserverless-action-DeleteVpcEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccessPolicy  **
  - **IAM action:**  [aoss:GetAccessPolicy](#list_opensearchserverless-action-GetAccessPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAccountSettings  **
  - **IAM action:**  [aoss:GetAccountSettings](#list_opensearchserverless-action-GetAccountSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIndex  **
  - **IAM action:**  [aoss:GetIndex](#list_opensearchserverless-action-GetIndex) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPoliciesStats  **
  - **IAM action:**  [aoss:GetPoliciesStats](#list_opensearchserverless-action-GetPoliciesStats) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSecurityConfig  **
  - **IAM action:**  [aoss:GetSecurityConfig](#list_opensearchserverless-action-GetSecurityConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSecurityPolicy  **
  - **IAM action:**  [aoss:GetSecurityPolicy](#list_opensearchserverless-action-GetSecurityPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAccessPolicies  **
  - **IAM action:**  [aoss:ListAccessPolicies](#list_opensearchserverless-action-ListAccessPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCollectionGroups  **
  - **IAM action:**  [aoss:ListCollectionGroups](#list_opensearchserverless-action-ListCollectionGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCollections  **
  - **IAM action:**  [aoss:ListCollections](#list_opensearchserverless-action-ListCollections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLifecyclePolicies  **
  - **IAM action:**  [aoss:ListLifecyclePolicies](#list_opensearchserverless-action-ListLifecyclePolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSecurityConfigs  **
  - **IAM action:**  [aoss:ListSecurityConfigs](#list_opensearchserverless-action-ListSecurityConfigs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSecurityPolicies  **
  - **IAM action:**  [aoss:ListSecurityPolicies](#list_opensearchserverless-action-ListSecurityPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [aoss:ListTagsForResource](#list_opensearchserverless-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVpcEndpoints  **
  - **IAM action:**  [aoss:ListVpcEndpoints](#list_opensearchserverless-action-ListVpcEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   TagResource  **
  - **IAM action:**  [aoss:TagResource](#list_opensearchserverless-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [aoss:UntagResource](#list_opensearchserverless-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAccessPolicy  **
  - **IAM action:**  [aoss:UpdateAccessPolicy](#list_opensearchserverless-action-UpdateAccessPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAccountSettings  **
  - **IAM action:**  [aoss:UpdateAccountSettings](#list_opensearchserverless-action-UpdateAccountSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCollection  **
  - **IAM action:**  [aoss:UpdateCollection](#list_opensearchserverless-action-UpdateCollection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCollectionGroup  **
  - **IAM action:**  [aoss:UpdateCollectionGroup](#list_opensearchserverless-action-UpdateCollectionGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateIndex  **
  - **IAM action:**  [aoss:UpdateIndex](#list_opensearchserverless-action-UpdateIndex) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLifecyclePolicy  **
  - **IAM action:**  [aoss:UpdateLifecyclePolicy](#list_opensearchserverless-action-UpdateLifecyclePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSecurityConfig  **
  - **IAM action:**  [aoss:UpdateSecurityConfig](#list_opensearchserverless-action-UpdateSecurityConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSecurityPolicy  **
  - **IAM action:**  [aoss:UpdateSecurityPolicy](#list_opensearchserverless-action-UpdateSecurityPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateVpcEndpoint  **
  - **IAM action:**  [aoss:UpdateVpcEndpoint](#list_opensearchserverless-action-UpdateVpcEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon OpenSearch Serverless
<a name="list_opensearchserverless-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [APIAccessAll](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_APIAccessAll.html)  **
  - **Description:** Grant permission to all the supported Opensearch APIs
  - **Resource types (\*required):** [Collection\*](#list_opensearchserverless-resource-Collection)
  - **Condition keys:** [aoss:collection](#list_opensearchserverless-aoss_collection)<br />[aoss:CollectionId](#list_opensearchserverless-aoss_CollectionId)<br />[aws:ResourceTag/${TagKey}](#list_opensearchserverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AddCollectionToCollectionGroup](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateCollection.html)  **
  - **Description:** Grants permission to add a serverless collection to a specified collection group
  - **Resource types (\*required):** [CollectionGroup\*](#list_opensearchserverless-resource-CollectionGroup)
  - **Condition keys:** [aoss:collection-group](#list_opensearchserverless-aoss_collection-group)<br />[aws:ResourceTag/${TagKey}](#list_opensearchserverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchGetCollection](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_BatchGetCollection.html)  **
  - **Description:** Grants permission to get attributes for one or more collections
  - **Resource types (\*required):** 
  - **Condition keys:** [aoss:collection](#list_opensearchserverless-aoss_collection)
  - **Access level:** Read

- **   [BatchGetCollectionGroup](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_BatchGetCollectionGroup.html)  **
  - **Description:** Grants permission to get attributes for one or more collection groups
  - **Resource types (\*required):** 
  - **Condition keys:** [aoss:collection-group](#list_opensearchserverless-aoss_collection-group)
  - **Access level:** Read

- **   [BatchGetEffectiveLifecyclePolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_BatchGetEffectiveLifecyclePolicy.html)  **
  - **Description:** Grants permission to get the information about a lifecycle policy applied to one or more AOSS resources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchGetLifecyclePolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_BatchGetLifecyclePolicy.html)  **
  - **Description:** Grants permission to get information about one or more lifecycle policies
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchGetVpcEndpoint](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_BatchGetVpcEndpoint.html)  **
  - **Description:** Grants permission to get attributes for one or more VPC endpoints
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [CreateAccessPolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateAccessPolicy.html)  **
  - **Description:** Grants permission to create a data access policy
  - **Resource types (\*required):** 
  - **Condition keys:** [aoss:collection](#list_opensearchserverless-aoss_collection)<br />[aoss:index](#list_opensearchserverless-aoss_index)
  - **Access level:** Write

- **   [CreateCollection](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateCollection.html)  **
  - **Description:** Grants permission to create a serverless collection
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_opensearchserverless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_opensearchserverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_opensearchserverless-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCollectionGroup](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateCollectionGroup.html)  **
  - **Description:** Grants permission to create a serverless collection group
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_opensearchserverless-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_opensearchserverless-aws_TagKeys)
  - **Access level:** Write

- **   [CreateIndex](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateIndex.html)  **
  - **Description:** Grants permission to create an opensearch index
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateLifecyclePolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateLifecyclePolicy.html)  **
  - **Description:** Grants permission to create a lifecycle policy
  - **Resource types (\*required):** 
  - **Condition keys:** [aoss:index](#list_opensearchserverless-aoss_index)
  - **Access level:** Write

- **   [CreateSecurityConfig](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateSecurityConfig.html)  **
  - **Description:** Grants permission to create a serverless security configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateSecurityPolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateSecurityPolicy.html)  **
  - **Description:** Grants permission to create a network or encryption policy
  - **Resource types (\*required):** 
  - **Condition keys:** [aoss:collection](#list_opensearchserverless-aoss_collection)
  - **Access level:** Write

- **   [CreateVpcEndpoint](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateVpcEndpoint.html)  **
  - **Description:** Grants permission to create an OpenSearch-Serverless-managed interface VPC endpoint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DashboardsAccessAll](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DashboardsAccessAll.html)  **
  - **Description:** Grants permission to Opensearch Serverless Dashboards
  - **Resource types (\*required):** [Dashboards\*](#list_opensearchserverless-resource-Dashboards)
  - **Condition keys:** [aoss:collection](#list_opensearchserverless-aoss_collection)<br />[aoss:CollectionId](#list_opensearchserverless-aoss_CollectionId)
  - **Access level:** Write

- **   [DeleteAccessPolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteAccessPolicy.html)  **
  - **Description:** Grants permission to delete a data access policy
  - **Resource types (\*required):** 
  - **Condition keys:** [aoss:collection](#list_opensearchserverless-aoss_collection)<br />[aoss:index](#list_opensearchserverless-aoss_index)
  - **Access level:** Write

- **   [DeleteCollection](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteCollection.html)  **
  - **Description:** Grants permission to delete a serverless collection
  - **Resource types (\*required):** [Collection\*](#list_opensearchserverless-resource-Collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_opensearchserverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCollectionGroup](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteCollectionGroup.html)  **
  - **Description:** Grants permission to delete a serverless collection group
  - **Resource types (\*required):** [CollectionGroup\*](#list_opensearchserverless-resource-CollectionGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_opensearchserverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIndex](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteIndex.html)  **
  - **Description:** Grants permission to delete an opensearch index
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteLifecyclePolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteLifecyclePolicy.html)  **
  - **Description:** Grants permission to delete a lifecycle policy
  - **Resource types (\*required):** 
  - **Condition keys:** [aoss:index](#list_opensearchserverless-aoss_index)
  - **Access level:** Write

- **   [DeleteSecurityConfig](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteSecurityConfig.html)  **
  - **Description:** Grants permission to delete a security configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSecurityPolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteSecurityPolicy.html)  **
  - **Description:** Grants permission to delete a security policy
  - **Resource types (\*required):** 
  - **Condition keys:** [aoss:collection](#list_opensearchserverless-aoss_collection)
  - **Access level:** Write

- **   [DeleteVpcEndpoint](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteVpcEndpoint.html)  **
  - **Description:** Grants permission to delete an OpenSearch Serverless-managed interface VPC endpoint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetAccessPolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_GetAccessPolicy.html)  **
  - **Description:** Grants permission to get information about a data access policy
  - **Resource types (\*required):** 
  - **Condition keys:** [aoss:collection](#list_opensearchserverless-aoss_collection)<br />[aoss:index](#list_opensearchserverless-aoss_index)
  - **Access level:** Read

- **   [GetAccountSettings](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_GetAccountSettings.html)  **
  - **Description:** Grants permission to get account settings, including capacity settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetIndex](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_GetIndex.html)  **
  - **Description:** Grants permission to get an opensearch index
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPoliciesStats](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_GetPoliciesStats.html)  **
  - **Description:** Grants permission to get statistis about the security policies in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSecurityConfig](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_GetSecurityConfig.html)  **
  - **Description:** Grants permission to get information about a serverless security configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSecurityPolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_GetSecurityPolicy.html)  **
  - **Description:** Grants permission to get information about a security policy
  - **Resource types (\*required):** 
  - **Condition keys:** [aoss:collection](#list_opensearchserverless-aoss_collection)
  - **Access level:** Read

- **   [ListAccessPolicies](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListAccessPolicies.html)  **
  - **Description:** Grants permission to list data access policies
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCollectionGroups](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListCollectionGroups.html)  **
  - **Description:** Grants permission to list collection groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCollections](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListCollections.html)  **
  - **Description:** Grants permission to list collections
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLifecyclePolicies](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListLifecyclePolicies.html)  **
  - **Description:** Grants permission to list lifecycle policies
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSecurityConfigs](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListSecurityConfigs.html)  **
  - **Description:** Grants permission to list security configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSecurityPolicies](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListSecurityPolicies.html)  **
  - **Description:** Grants permission to list security policies
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a collection
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListVpcEndpoints](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListVpcEndpoints.html)  **
  - **Description:** Grants permission to list OpenSearch Serverless-managed VPC endpoints
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [TagResource](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a serverless collection
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_opensearchserverless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_opensearchserverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_opensearchserverless-aws_TagKeys)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a collection
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:TagKeys](#list_opensearchserverless-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateAccessPolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateAccessPolicy.html)  **
  - **Description:** Grants permission to update a data access policy
  - **Resource types (\*required):** 
  - **Condition keys:** [aoss:collection](#list_opensearchserverless-aoss_collection)<br />[aoss:index](#list_opensearchserverless-aoss_index)
  - **Access level:** Write

- **   [UpdateAccountSettings](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateAccountSettings.html)  **
  - **Description:** Grants permission to update account settings, including capacity settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateCollection](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateCollection.html)  **
  - **Description:** Grants permission to update a collection
  - **Resource types (\*required):** [Collection\*](#list_opensearchserverless-resource-Collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_opensearchserverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCollectionGroup](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateCollectionGroup.html)  **
  - **Description:** Grants permission to update a collection group
  - **Resource types (\*required):** [CollectionGroup\*](#list_opensearchserverless-resource-CollectionGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_opensearchserverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateIndex](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateIndex.html)  **
  - **Description:** Grants permission to update an opensearch index
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateLifecyclePolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateLifecyclePolicy.html)  **
  - **Description:** Grants permission to update a lifecycle policy
  - **Resource types (\*required):** 
  - **Condition keys:** [aoss:index](#list_opensearchserverless-aoss_index)
  - **Access level:** Write

- **   [UpdateSecurityConfig](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateSecurityConfig.html)  **
  - **Description:** Grants permission to update a security configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSecurityPolicy](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateSecurityPolicy.html)  **
  - **Description:** Grants permission to update a security policy
  - **Resource types (\*required):** 
  - **Condition keys:** [aoss:collection](#list_opensearchserverless-aoss_collection)
  - **Access level:** Write

- **   [UpdateVpcEndpoint](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateVpcEndpoint.html)  **
  - **Description:** Grants permission to update an OpenSearch Serverless-managed VPC endpoint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon OpenSearch Serverless
<a name="list_opensearchserverless-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Collection](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html)  | arn:${Partition}:aoss:${Region}:${Account}:collection/${CollectionId} | [aws:ResourceTag/${TagKey}](#list_opensearchserverless-aws_ResourceTag___TagKey_) | 
|  [CollectionGroup](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html)  | arn:${Partition}:aoss:${Region}:${Account}:collection-group/${CollectionGroupId} | [aws:ResourceTag/${TagKey}](#list_opensearchserverless-aws_ResourceTag___TagKey_) | 
|  [Dashboards](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html)  | arn:${Partition}:aoss:${Region}:${Account}:dashboards/default |   | 

## Condition keys for Amazon OpenSearch Serverless
<a name="list_opensearchserverless-policy-keys"></a>

Amazon OpenSearch Serverless defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aoss:CollectionId](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/security-iam-serverless.html#security_iam_serverless-conditionkeys)  | Filters access by the identifier of the collection | String | 
|   [aoss:collection](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/security-iam-serverless.html#security_iam_serverless-conditionkeys)  | Filters access by the collection name | String | 
|   [aoss:collection-group](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/security-iam-serverless.html#security_iam_serverless-conditionkeys)  | Filters access by the collection group name | String | 
|   [aoss:index](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/security-iam-serverless.html#security_iam_serverless-conditionkeys)  | Filters access by the index | String | 
|   [aws:RequestTag/${TagKey}](security-iam-serverless.html#condition-keys-requesttag)  | Filters access based on the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](security-iam-serverless.html#condition-keys-resourcetag)  | Filters access based on the tags associated with the resource | String | 
|   [aws:TagKeys](security-iam-serverless.html#condition-keys-tagkeys)  | Filters access based on the tag keys that are passed in the request | ArrayOfString | 