

# Actions, resources, and condition keys for AWS Marketplace Deployment Service
<a name="list_marketplace-deployment"></a>

AWS Marketplace Deployment Service (service prefix: `aws-marketplace`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/marketplace-deployment/latest/api-reference/Welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/marketplace-deployment/latest/api-reference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/marketplace/) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/aws-marketplace/aws-marketplace.json) for this service.

**Topics**
+ [API operations defined by AWS Marketplace Deployment Service](#list_marketplace-deployment-operations)
+ [Actions defined by AWS Marketplace Deployment Service](#list_marketplace-deployment-actions-as-permissions)
+ [Resource types defined by AWS Marketplace Deployment Service](#list_marketplace-deployment-resources-for-iam-policies)
+ [Condition keys for AWS Marketplace Deployment Service](#list_marketplace-deployment-policy-keys)

## API operations defined by AWS Marketplace Deployment Service
<a name="list_marketplace-deployment-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_marketplace-deployment-actions-as-permissions).




- **   ListTagsForResource  **
  - **IAM action:**  [aws-marketplace:ListTagsForResource](#list_marketplace-deployment-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutDeploymentParameter  **
  - **IAM action:**  [aws-marketplace:PutDeploymentParameter](#list_marketplace-deployment-action-PutDeploymentParameter)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-marketplace:TagResource](#list_marketplace-deployment-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   TagResource  **
  - **IAM action:**  [aws-marketplace:TagResource](#list_marketplace-deployment-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [aws-marketplace:UntagResource](#list_marketplace-deployment-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write



## Actions defined by AWS Marketplace Deployment Service
<a name="list_marketplace-deployment-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ListTagsForResource](https://docs.aws.amazon.com/marketplace-deployment/latest/api-reference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a deployment parameter resource
  - **Resource types (\*required):** [DeploymentParameter](#list_marketplace-deployment-resource-DeploymentParameter)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_marketplace-deployment-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_marketplace-deployment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-deployment-aws_TagKeys)
  - **Access level:** Read

- **   [PutDeploymentParameter](https://docs.aws.amazon.com/marketplace-deployment/latest/api-reference/API_PutDeploymentParameter.html)  **
  - **Description:** Grants permission to create or update a deployment parameter resource
  - **Resource types (\*required):** [DeploymentParameter\*](#list_marketplace-deployment-resource-DeploymentParameter)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_marketplace-deployment-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_marketplace-deployment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-deployment-aws_TagKeys)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/marketplace-deployment/latest/api-reference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a deployment parameter resource
  - **Resource types (\*required):** [DeploymentParameter\*](#list_marketplace-deployment-resource-DeploymentParameter)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_marketplace-deployment-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_marketplace-deployment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-deployment-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/marketplace-deployment/latest/api-reference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a deployment parameter resource
  - **Resource types (\*required):** [DeploymentParameter\*](#list_marketplace-deployment-resource-DeploymentParameter)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_marketplace-deployment-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_marketplace-deployment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-deployment-aws_TagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by AWS Marketplace Deployment Service
<a name="list_marketplace-deployment-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [DeploymentParameter](https://docs.aws.amazon.com/marketplace-deployment/latest/api-reference/API_DeploymentParameterInput.html)  | arn:${Partition}:aws-marketplace:${Region}:${Account}:DeploymentParameter:catalogs/${CatalogName}/products/${ProductId}/${ResourceId} | [aws:RequestTag/${TagKey}](#list_marketplace-deployment-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_marketplace-deployment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_marketplace-deployment-aws_TagKeys) | 

## Condition keys for AWS Marketplace Deployment Service
<a name="list_marketplace-deployment-policy-keys"></a>

AWS Marketplace Deployment Service defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by tag keys that are passed in the request | ArrayOfString | 