

# Actions, resources, and condition keys for Amazon Verified Permissions
<a name="list_verifiedpermissions"></a>

Amazon Verified Permissions (service prefix: `verifiedpermissions`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/verifiedpermissions/verifiedpermissions.json) for this service.

**Topics**
+ [Actions defined by Amazon Verified Permissions](#list_verifiedpermissions-actions-as-permissions)
+ [Resource types defined by Amazon Verified Permissions](#list_verifiedpermissions-resources-for-iam-policies)
+ [Condition keys for Amazon Verified Permissions](#list_verifiedpermissions-policy-keys)

## Actions defined by Amazon Verified Permissions
<a name="list_verifiedpermissions-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreateIdentitySource.html)  **
  - **Description:** Grants permission to create a reference to an external identity provider (IdP) that is compatible with OpenID Connect (OIDC) authentication protocol, such as Amazon Cognito
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicy.html)  **
  - **Description:** Grants permission to create a Cedar policy and save it in the specified policy store
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePolicyStore](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicyStore.html)  **
  - **Description:** Grants permission to create a Cedar policy and save it in the specified policy store
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_verifiedpermissions-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_verifiedpermissions-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePolicyStoreAlias](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicyStoreAlias.html)  **
  - **Description:** Grants permission to create an alias against a policy store
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [policy-store-alias\*](#list_verifiedpermissions-resource-policy-store-alias) / **Condition keys:**  
  - **Access level:** Write

- **   [CreatePolicyTemplate](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicyTemplate.html)  **
  - **Description:** Grants permission to create a policy template
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_DeleteIdentitySource.html)  **
  - **Description:** Grants permission to delete an identity source that references an identity provider (IdP) such as Amazon Cognito
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_DeletePolicy.html)  **
  - **Description:** Grants permission to delete the specified policy from the policy store
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePolicyStore](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_DeletePolicyStore.html)  **
  - **Description:** Grants permission to delete the specified policy store
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePolicyStoreAlias](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_DeletePolicyStoreAlias.html)  **
  - **Description:** Grants permission to delete an alias for a policy store
  - **Resource types (\*required):** [policy-store-alias\*](#list_verifiedpermissions-resource-policy-store-alias)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeletePolicyTemplate](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_DeletePolicyTemplate.html)  **
  - **Description:** Grants permission to delete the specified policy template from the policy store
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetIdentitySource.html)  **
  - **Description:** Grants permission to retrieve the details about the specified identity source
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetPolicy.html)  **
  - **Description:** Grants permission to retrieve information about the specified policy
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPolicyStore](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetPolicyStore.html)  **
  - **Description:** Grants permission to retrieve details about a policy store
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPolicyStoreAlias](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetPolicyStoreAlias.html)  **
  - **Description:** Grants permission to retrieve details about an alias for a policy store
  - **Resource types (\*required):** [policy-store-alias\*](#list_verifiedpermissions-resource-policy-store-alias)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPolicyTemplate](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetPolicyTemplate.html)  **
  - **Description:** Grants permission to retrieve the details for the specified policy template in the specified policy store
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSchema](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetSchema.html)  **
  - **Description:** Grants permission to retrieve the details for the specified schema in the specified policy store
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [IsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html)  **
  - **Description:** Grants permission to make an authorization decision about a service request described in the parameters
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [IsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html)  **
  - **Description:** Grants permission to make an authorization decision about a service request described in the parameters. The principal in this request comes from an external identity source
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListIdentitySources](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListIdentitySources.html)  **
  - **Description:** Grants permission to return a paginated list of all of the identity sources defined in the specified policy store
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPolicies](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicies.html)  **
  - **Description:** Grants permission to return a paginated list of all policies stored in the specified policy store
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPolicyStoreAliases](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html)  **
  - **Description:** Grants permission to return a paginated list of all policy store aliases
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPolicyStores](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStores.html)  **
  - **Description:** Grants permission to return a paginated list of all policy stores in the calling Amazon Web Services account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPolicyTemplates](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyTemplates.html)  **
  - **Description:** Grants permission to return a paginated list of all policy templates in the specified policy store
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to view a list of resource tags for the specified policy store
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutSchema](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PutSchema.html)  **
  - **Description:** Grants permission to create or update the policy schema in the specified policy store
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to the specified policy store
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_verifiedpermissions-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_verifiedpermissions-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from the specified policy store
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_verifiedpermissions-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateIdentitySource.html)  **
  - **Description:** Grants permission to update the specified identity source to use a new identity provider (IdP) source, or to change the mapping of identities from the IdP to a different principal entity type
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicy.html)  **
  - **Description:** Grants permission to modify the specified Cedar static policy in the specified policy store
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePolicyStore](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyStore.html)  **
  - **Description:** Grants permission to modify the validation setting for a policy store
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePolicyTemplate](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyTemplate.html)  **
  - **Description:** Grants permission to update the specified policy template
  - **Resource types (\*required):** [policy-store\*](#list_verifiedpermissions-resource-policy-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Verified Permissions
<a name="list_verifiedpermissions-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [policy-store](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-stores.html)  | arn:${Partition}:verifiedpermissions::${Account}:policy-store/${PolicyStoreId} | [aws:ResourceTag/${TagKey}](#list_verifiedpermissions-aws_ResourceTag___TagKey_) | 
|  [policy-store-alias](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-store-aliases.html)  | arn:${Partition}:verifiedpermissions:${Region}:${Account}:policy-store-alias/${AliasName} |   | 

## Condition keys for Amazon Verified Permissions
<a name="list_verifiedpermissions-policy-keys"></a>

Amazon Verified Permissions defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag key and value pair that is allowed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag key and value pair of a resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by a list of tag keys that are allowed in the request | ArrayOfString | 