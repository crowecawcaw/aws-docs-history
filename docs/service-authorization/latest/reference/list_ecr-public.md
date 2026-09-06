

# Actions, resources, and condition keys for Amazon Elastic Container Registry Public
<a name="list_ecr-public"></a>

Amazon Elastic Container Registry Public (service prefix: `ecr-public`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonECR/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonECR/latest/userguide/ECR-Public_IAM_policies.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/ecr-public/ecr-public.json) for this service.

**Topics**
+ [API operations defined by Amazon Elastic Container Registry Public](#list_ecr-public-operations)
+ [Actions defined by Amazon Elastic Container Registry Public](#list_ecr-public-actions-as-permissions)
+ [Resource types defined by Amazon Elastic Container Registry Public](#list_ecr-public-resources-for-iam-policies)
+ [Condition keys for Amazon Elastic Container Registry Public](#list_ecr-public-policy-keys)

## API operations defined by Amazon Elastic Container Registry Public
<a name="list_ecr-public-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_ecr-public-actions-as-permissions).




- **   BatchCheckLayerAvailability  **
  - **IAM action:**  [ecr-public:BatchCheckLayerAvailability](#list_ecr-public-action-BatchCheckLayerAvailability) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchDeleteImage  **
  - **IAM action:**  [ecr-public:BatchDeleteImage](#list_ecr-public-action-BatchDeleteImage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CompleteLayerUpload  **
  - **IAM action:**  [ecr-public:CompleteLayerUpload](#list_ecr-public-action-CompleteLayerUpload) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRepository  **
  - **IAM action:**  [ecr-public:CreateRepository](#list_ecr-public-action-CreateRepository)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecr-public:TagResource](#list_ecr-public-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteRepository  **
  - **IAM action:**  [ecr-public:DeleteRepository](#list_ecr-public-action-DeleteRepository) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRepositoryPolicy  **
  - **IAM action:**  [ecr-public:DeleteRepositoryPolicy](#list_ecr-public-action-DeleteRepositoryPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeImageTags  **
  - **IAM action:**  [ecr-public:DescribeImageTags](#list_ecr-public-action-DescribeImageTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeImages  **
  - **IAM action:**  [ecr-public:DescribeImages](#list_ecr-public-action-DescribeImages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRegistries  **
  - **IAM action:**  [ecr-public:DescribeRegistries](#list_ecr-public-action-DescribeRegistries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeRepositories  **
  - **IAM action:**  [ecr-public:DescribeRepositories](#list_ecr-public-action-DescribeRepositories) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetAuthorizationToken  **
  - **IAM action:**  [ecr-public:GetAuthorizationToken](#list_ecr-public-action-GetAuthorizationToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sts:GetServiceBearerToken](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_bearer.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetRegistryCatalogData  **
  - **IAM action:**  [ecr-public:GetRegistryCatalogData](#list_ecr-public-action-GetRegistryCatalogData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRepositoryCatalogData  **
  - **IAM action:**  [ecr-public:GetRepositoryCatalogData](#list_ecr-public-action-GetRepositoryCatalogData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRepositoryPolicy  **
  - **IAM action:**  [ecr-public:GetRepositoryPolicy](#list_ecr-public-action-GetRepositoryPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InitiateLayerUpload  **
  - **IAM action:**  [ecr-public:InitiateLayerUpload](#list_ecr-public-action-InitiateLayerUpload) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListTagsForResource  **
  - **IAM action:**  [ecr-public:ListTagsForResource](#list_ecr-public-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutImage  **
  - **IAM action:**  [ecr-public:PutImage](#list_ecr-public-action-PutImage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutRegistryCatalogData  **
  - **IAM action:**  [ecr-public:PutRegistryCatalogData](#list_ecr-public-action-PutRegistryCatalogData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutRepositoryCatalogData  **
  - **IAM action:**  [ecr-public:PutRepositoryCatalogData](#list_ecr-public-action-PutRepositoryCatalogData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetRepositoryPolicy  **
  - **IAM action:**  [ecr-public:SetRepositoryPolicy](#list_ecr-public-action-SetRepositoryPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   TagResource  **
  - **IAM action:**  [ecr-public:TagResource](#list_ecr-public-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [ecr-public:UntagResource](#list_ecr-public-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UploadLayerPart  **
  - **IAM action:**  [ecr-public:UploadLayerPart](#list_ecr-public-action-UploadLayerPart) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Elastic Container Registry Public
<a name="list_ecr-public-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchCheckLayerAvailability](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_BatchCheckLayerAvailability.html)  **
  - **Description:** Grants permission to check the availability of multiple image layers in a specified registry and repository
  - **Resource types (\*required):** [repository\*](#list_ecr-public-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-public-aws_ResourceTag___TagKey_)<br />[ecr-public:ResourceTag/${TagKey}](#list_ecr-public-ecr-public_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchDeleteImage](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_BatchDeleteImage.html)  **
  - **Description:** Grants permission to delete a list of specified images within a specified repository
  - **Resource types (\*required):** [repository\*](#list_ecr-public-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-public-aws_ResourceTag___TagKey_)<br />[ecr-public:ResourceTag/${TagKey}](#list_ecr-public-ecr-public_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CompleteLayerUpload](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_CompleteLayerUpload.html)  **
  - **Description:** Grants permission to inform Amazon ECR that the image layer upload for a specified registry, repository name, and upload ID, has completed
  - **Resource types (\*required):** [repository\*](#list_ecr-public-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-public-aws_ResourceTag___TagKey_)<br />[ecr-public:ResourceTag/${TagKey}](#list_ecr-public-ecr-public_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateRepository](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_CreateRepository.html)  **
  - **Description:** Grants permission to create an image repository
  - **Resource types (\*required):** [repository\*](#list_ecr-public-resource-repository)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ecr-public-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ecr-public-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecr-public-aws_TagKeys)<br />[ecr-public:ResourceTag/${TagKey}](#list_ecr-public-ecr-public_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRepository](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_DeleteRepository.html)  **
  - **Description:** Grants permission to delete an existing image repository
  - **Resource types (\*required):** [repository\*](#list_ecr-public-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-public-aws_ResourceTag___TagKey_)<br />[ecr-public:ResourceTag/${TagKey}](#list_ecr-public-ecr-public_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRepositoryPolicy](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_DeleteRepositoryPolicy.html)  **
  - **Description:** Grants permission to delete the repository policy from a specified repository
  - **Resource types (\*required):** [repository\*](#list_ecr-public-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-public-aws_ResourceTag___TagKey_)<br />[ecr-public:ResourceTag/${TagKey}](#list_ecr-public-ecr-public_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeImageTags](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_DescribeImageTags.html)  **
  - **Description:** Grants permission to describe all the image tags for a given repository
  - **Resource types (\*required):** [repository\*](#list_ecr-public-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-public-aws_ResourceTag___TagKey_)<br />[ecr-public:ResourceTag/${TagKey}](#list_ecr-public-ecr-public_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeImages](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_DescribeImages.html)  **
  - **Description:** Grants permission to get metadata about the images in a repository, including image size, image tags, and creation date
  - **Resource types (\*required):** [repository\*](#list_ecr-public-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-public-aws_ResourceTag___TagKey_)<br />[ecr-public:ResourceTag/${TagKey}](#list_ecr-public-ecr-public_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRegistries](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_DescribeRegistries.html)  **
  - **Description:** Grants permission to retrieve the catalog data associated with a registry
  - **Resource types (\*required):** [registry\*](#list_ecr-public-resource-registry)
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeRepositories](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_DescribeRepositories.html)  **
  - **Description:** Grants permission to describe image repositories in a registry
  - **Resource types (\*required):** [repository](#list_ecr-public-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-public-aws_ResourceTag___TagKey_)<br />[ecr-public:ResourceTag/${TagKey}](#list_ecr-public-ecr-public_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetAuthorizationToken](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_GetAuthorizationToken.html)  **
  - **Description:** Grants permission to retrieve a token that is valid for a specified registry for 12 hours
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRegistryCatalogData](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_GetRegistryCatalogData.html)  **
  - **Description:** Grants permission to retrieve the catalog data associated with a registry
  - **Resource types (\*required):** [registry\*](#list_ecr-public-resource-registry)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRepositoryCatalogData](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_GetRepositoryCatalogData.html)  **
  - **Description:** Grants permission to retrieve the catalog data associated with a repository
  - **Resource types (\*required):** [repository\*](#list_ecr-public-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-public-aws_ResourceTag___TagKey_)<br />[ecr-public:ResourceTag/${TagKey}](#list_ecr-public-ecr-public_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRepositoryPolicy](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_GetRepositoryPolicy.html)  **
  - **Description:** Grants permission to retrieve the repository policy for a specified repository
  - **Resource types (\*required):** [repository\*](#list_ecr-public-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-public-aws_ResourceTag___TagKey_)<br />[ecr-public:ResourceTag/${TagKey}](#list_ecr-public-ecr-public_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InitiateLayerUpload](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_InitiateLayerUpload.html)  **
  - **Description:** Grants permission to notify Amazon ECR that you intend to upload an image layer
  - **Resource types (\*required):** [repository\*](#list_ecr-public-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-public-aws_ResourceTag___TagKey_)<br />[ecr-public:ResourceTag/${TagKey}](#list_ecr-public-ecr-public_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListTagsForResource](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for an Amazon ECR resource
  - **Resource types (\*required):** [repository\*](#list_ecr-public-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-public-aws_ResourceTag___TagKey_)<br />[ecr-public:ResourceTag/${TagKey}](#list_ecr-public-ecr-public_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutImage](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_PutImage.html)  **
  - **Description:** Grants permission to create or update the image manifest associated with an image
  - **Resource types (\*required):** [repository\*](#list_ecr-public-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-public-aws_ResourceTag___TagKey_)<br />[ecr-public:ResourceTag/${TagKey}](#list_ecr-public-ecr-public_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutRegistryCatalogData](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_PutRegistryCatalogData.html)  **
  - **Description:** Grants permission to create and update the catalog data associated with a registry
  - **Resource types (\*required):** [registry\*](#list_ecr-public-resource-registry)
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutRepositoryCatalogData](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_PutRepositoryCatalogData.html)  **
  - **Description:** Grants permission to update the catalog data associated with a repository
  - **Resource types (\*required):** [repository\*](#list_ecr-public-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-public-aws_ResourceTag___TagKey_)<br />[ecr-public:ResourceTag/${TagKey}](#list_ecr-public-ecr-public_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetRepositoryPolicy](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_SetRepositoryPolicy.html)  **
  - **Description:** Grants permission to apply a repository policy on a specified repository to control access permissions
  - **Resource types (\*required):** [repository\*](#list_ecr-public-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-public-aws_ResourceTag___TagKey_)<br />[ecr-public:ResourceTag/${TagKey}](#list_ecr-public-ecr-public_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [TagResource](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag an Amazon ECR resource
  - **Resource types (\*required):** [repository\*](#list_ecr-public-resource-repository)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ecr-public-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ecr-public-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecr-public-aws_TagKeys)<br />[ecr-public:ResourceTag/${TagKey}](#list_ecr-public-ecr-public_ResourceTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag an Amazon ECR resource
  - **Resource types (\*required):** [repository\*](#list_ecr-public-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-public-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecr-public-aws_TagKeys)<br />[ecr-public:ResourceTag/${TagKey}](#list_ecr-public-ecr-public_ResourceTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [UploadLayerPart](https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_UploadLayerPart.html)  **
  - **Description:** Grants permission to upload an image layer part to Amazon ECR Public
  - **Resource types (\*required):** [repository\*](#list_ecr-public-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-public-aws_ResourceTag___TagKey_)<br />[ecr-public:ResourceTag/${TagKey}](#list_ecr-public-ecr-public_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Elastic Container Registry Public
<a name="list_ecr-public-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/iam-policy-structure.html#ECR-Public_ARN_Format)  | arn:${Partition}:ecr-public::${Account}:registry/${RegistryId} |   | 
|  [repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/iam-policy-structure.html#ECR-Public_ARN_Format)  | arn:${Partition}:ecr-public::${Account}:repository/${RepositoryName} | [aws:ResourceTag/${TagKey}](#list_ecr-public-aws_ResourceTag___TagKey_)<br />[ecr-public:ResourceTag/${TagKey}](#list_ecr-public-ecr-public_ResourceTag___TagKey_) | 

## Condition keys for Amazon Elastic Container Registry Public
<a name="list_ecr-public-policy-keys"></a>

Amazon Elastic Container Registry Public defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters create requests based on the allowed set of values for each of the tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions based on tag-value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters create requests based on the presence of mandatory tags in the request | ArrayOfString | 
|   [ecr-public:ResourceTag/${TagKey}](https://docs.aws.amazon.com/AmazonECR/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters actions based on tag-value associated with the resource | String | 