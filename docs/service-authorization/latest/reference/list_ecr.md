

# Actions, resources, and condition keys for Amazon Elastic Container Registry
<a name="list_ecr"></a>

Amazon Elastic Container Registry (service prefix: `ecr`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonECR/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonECR/latest/userguide/security-iam-awsmanpol.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/ecr/ecr.json) for this service.

**Topics**
+ [API operations defined by Amazon Elastic Container Registry](#list_ecr-operations)
+ [Actions defined by Amazon Elastic Container Registry](#list_ecr-actions-as-permissions)
+ [Permission-only actions for Amazon Elastic Container Registry](#list_ecr-permission-only-actions)
+ [Resource types defined by Amazon Elastic Container Registry](#list_ecr-resources-for-iam-policies)
+ [Condition keys for Amazon Elastic Container Registry](#list_ecr-policy-keys)

## API operations defined by Amazon Elastic Container Registry
<a name="list_ecr-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_ecr-actions-as-permissions).




- **   BatchCheckLayerAvailability  **
  - **IAM action:**  [ecr:BatchCheckLayerAvailability](#list_ecr-action-BatchCheckLayerAvailability) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchDeleteImage  **
  - **IAM action:**  [ecr:BatchDeleteImage](#list_ecr-action-BatchDeleteImage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchGetImage  **
  - **IAM action:**  [ecr:BatchGetImage](#list_ecr-action-BatchGetImage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [ecr:BatchImportUpstreamImage](#list_ecr-action-BatchImportUpstreamImage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecr:CreateRepository](#list_ecr-action-CreateRepository)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecr:TagResource](#list_ecr-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   BatchGetRepositoryScanningConfiguration  **
  - **IAM action:**  [ecr:BatchGetRepositoryScanningConfiguration](#list_ecr-action-BatchGetRepositoryScanningConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CompleteLayerUpload  **
  - **IAM action:**  [ecr:CompleteLayerUpload](#list_ecr-action-CompleteLayerUpload) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePullThroughCacheRule  **
  - **IAM action:**  [ecr:CreatePullThroughCacheRule](#list_ecr-action-CreatePullThroughCacheRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ecr.amazonaws.com / **Access level:** Write

- **   CreateRepository  **
  - **IAM action:**  [ecr:CreateRepository](#list_ecr-action-CreateRepository)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecr:TagResource](#list_ecr-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRepositoryCreationTemplate  **
  - **IAM action:**  [ecr:CreateRepository](#list_ecr-action-CreateRepository)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecr:CreateRepositoryCreationTemplate](#list_ecr-action-CreateRepositoryCreationTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecr:PutLifecyclePolicy](#list_ecr-action-PutLifecyclePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecr:SetRepositoryPolicy](#list_ecr-action-SetRepositoryPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ecr.amazonaws.com / **Access level:** Write

- **   DeleteLifecyclePolicy  **
  - **IAM action:**  [ecr:DeleteLifecyclePolicy](#list_ecr-action-DeleteLifecyclePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePullThroughCacheRule  **
  - **IAM action:**  [ecr:DeletePullThroughCacheRule](#list_ecr-action-DeletePullThroughCacheRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRegistryPolicy  **
  - **IAM action:**  [ecr:DeleteRegistryPolicy](#list_ecr-action-DeleteRegistryPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteRepository  **
  - **IAM action:**  [ecr:DeleteRepository](#list_ecr-action-DeleteRepository) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRepositoryCreationTemplate  **
  - **IAM action:**  [ecr:DeleteRepositoryCreationTemplate](#list_ecr-action-DeleteRepositoryCreationTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRepositoryPolicy  **
  - **IAM action:**  [ecr:DeleteRepositoryPolicy](#list_ecr-action-DeleteRepositoryPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteSigningConfiguration  **
  - **IAM action:**  [ecr:DeleteSigningConfiguration](#list_ecr-action-DeleteSigningConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterPullTimeUpdateExclusion  **
  - **IAM action:**  [ecr:DeregisterPullTimeUpdateExclusion](#list_ecr-action-DeregisterPullTimeUpdateExclusion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeImageReplicationStatus  **
  - **IAM action:**  [ecr:DescribeImageReplicationStatus](#list_ecr-action-DescribeImageReplicationStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeImageScanFindings  **
  - **IAM action:**  [ecr:DescribeImageScanFindings](#list_ecr-action-DescribeImageScanFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeImageSigningStatus  **
  - **IAM action:**  [ecr:DescribeImageSigningStatus](#list_ecr-action-DescribeImageSigningStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeImages  **
  - **IAM action:**  [ecr:DescribeImages](#list_ecr-action-DescribeImages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribePullThroughCacheRules  **
  - **IAM action:**  [ecr:DescribePullThroughCacheRules](#list_ecr-action-DescribePullThroughCacheRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeRegistry  **
  - **IAM action:**  [ecr:DescribeRegistry](#list_ecr-action-DescribeRegistry) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRepositories  **
  - **IAM action:**  [ecr:DescribeRepositories](#list_ecr-action-DescribeRepositories) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRepositoryCreationTemplates  **
  - **IAM action:**  [ecr:DescribeRepositoryCreationTemplates](#list_ecr-action-DescribeRepositoryCreationTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAccountSetting  **
  - **IAM action:**  [ecr:GetAccountSetting](#list_ecr-action-GetAccountSetting) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAuthorizationToken  **
  - **IAM action:**  [ecr:GetAuthorizationToken](#list_ecr-action-GetAuthorizationToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDownloadUrlForLayer  **
  - **IAM action:**  [ecr:BatchImportUpstreamImage](#list_ecr-action-BatchImportUpstreamImage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecr:GetDownloadUrlForLayer](#list_ecr-action-GetDownloadUrlForLayer)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetLifecyclePolicy  **
  - **IAM action:**  [ecr:GetLifecyclePolicy](#list_ecr-action-GetLifecyclePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLifecyclePolicyPreview  **
  - **IAM action:**  [ecr:GetLifecyclePolicyPreview](#list_ecr-action-GetLifecyclePolicyPreview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRegistryPolicy  **
  - **IAM action:**  [ecr:GetRegistryPolicy](#list_ecr-action-GetRegistryPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRegistryScanningConfiguration  **
  - **IAM action:**  [ecr:GetRegistryScanningConfiguration](#list_ecr-action-GetRegistryScanningConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRepositoryPolicy  **
  - **IAM action:**  [ecr:GetRepositoryPolicy](#list_ecr-action-GetRepositoryPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSigningConfiguration  **
  - **IAM action:**  [ecr:GetSigningConfiguration](#list_ecr-action-GetSigningConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InitiateLayerUpload  **
  - **IAM action:**  [ecr:InitiateLayerUpload](#list_ecr-action-InitiateLayerUpload) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListImageReferrers  **
  - **IAM action:**  [ecr:BatchGetImage](#list_ecr-action-BatchGetImage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [ecr:BatchImportUpstreamImage](#list_ecr-action-BatchImportUpstreamImage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecr:CreateRepository](#list_ecr-action-CreateRepository)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   ListImages  **
  - **IAM action:**  [ecr:ListImages](#list_ecr-action-ListImages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPullTimeUpdateExclusions  **
  - **IAM action:**  [ecr:ListPullTimeUpdateExclusions](#list_ecr-action-ListPullTimeUpdateExclusions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [ecr:ListTagsForResource](#list_ecr-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutAccountSetting  **
  - **IAM action:**  [ecr:PutAccountSetting](#list_ecr-action-PutAccountSetting) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutImage  **
  - **IAM action:**  [ecr:PutImage](#list_ecr-action-PutImage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutImageScanningConfiguration  **
  - **IAM action:**  [ecr:PutImageScanningConfiguration](#list_ecr-action-PutImageScanningConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutImageTagMutability  **
  - **IAM action:**  [ecr:PutImageTagMutability](#list_ecr-action-PutImageTagMutability) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutLifecyclePolicy  **
  - **IAM action:**  [ecr:PutLifecyclePolicy](#list_ecr-action-PutLifecyclePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutRegistryPolicy  **
  - **IAM action:**  [ecr:PutRegistryPolicy](#list_ecr-action-PutRegistryPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutRegistryScanningConfiguration  **
  - **IAM action:**  [ecr:PutRegistryScanningConfiguration](#list_ecr-action-PutRegistryScanningConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutReplicationConfiguration  **
  - **IAM action:**  [ecr:PutReplicationConfiguration](#list_ecr-action-PutReplicationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutSigningConfiguration  **
  - **IAM action:**  [ecr:PutSigningConfiguration](#list_ecr-action-PutSigningConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterPullTimeUpdateExclusion  **
  - **IAM action:**  [ecr:RegisterPullTimeUpdateExclusion](#list_ecr-action-RegisterPullTimeUpdateExclusion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetRepositoryPolicy  **
  - **IAM action:**  [ecr:SetRepositoryPolicy](#list_ecr-action-SetRepositoryPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   StartImageScan  **
  - **IAM action:**  [ecr:StartImageScan](#list_ecr-action-StartImageScan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartLifecyclePolicyPreview  **
  - **IAM action:**  [ecr:StartLifecyclePolicyPreview](#list_ecr-action-StartLifecyclePolicyPreview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [ecr:TagResource](#list_ecr-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [ecr:UntagResource](#list_ecr-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateImageStorageClass  **
  - **IAM action:**  [ecr:UpdateImageStorageClass](#list_ecr-action-UpdateImageStorageClass) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePullThroughCacheRule  **
  - **IAM action:**  [ecr:UpdatePullThroughCacheRule](#list_ecr-action-UpdatePullThroughCacheRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ecr.amazonaws.com / **Access level:** Write

- **   UpdateRepositoryCreationTemplate  **
  - **IAM action:**  [ecr:CreateRepository](#list_ecr-action-CreateRepository)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecr:PutLifecyclePolicy](#list_ecr-action-PutLifecyclePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecr:SetRepositoryPolicy](#list_ecr-action-SetRepositoryPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [ecr:UpdateRepositoryCreationTemplate](#list_ecr-action-UpdateRepositoryCreationTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ecr.amazonaws.com / **Access level:** Write

- **   UploadLayerPart  **
  - **IAM action:**  [ecr:UploadLayerPart](#list_ecr-action-UploadLayerPart) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ValidatePullThroughCacheRule  **
  - **IAM action:**  [ecr:ValidatePullThroughCacheRule](#list_ecr-action-ValidatePullThroughCacheRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by Amazon Elastic Container Registry
<a name="list_ecr-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchCheckLayerAvailability](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_BatchCheckLayerAvailability.html)  **
  - **Description:** Grants permission to check the availability of multiple image layers in a specified registry and repository
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchDeleteImage](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_BatchDeleteImage.html)  **
  - **Description:** Grants permission to delete a list of specified images within a specified repository
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchGetImage](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_BatchGetImage.html)  **
  - **Description:** Grants permission to get detailed information for specified images within a specified repository
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetRepositoryScanningConfiguration](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_BatchGetRepositoryScanningConfiguration.html)  **
  - **Description:** Grants permission to retrieve repository scanning configuration for a list of repositories
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [CompleteLayerUpload](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_CompleteLayerUpload.html)  **
  - **Description:** Grants permission to inform Amazon ECR that the image layer upload for a specified registry, repository name, and upload ID, has completed
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePullThroughCacheRule](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_CreatePullThroughCacheRule.html)  **
  - **Description:** Grants permission to create new pull-through cache rule
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateRepository](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_CreateRepository.html)  **
  - **Description:** Grants permission to create an image repository
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ecr-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecr-aws_TagKeys)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateRepositoryCreationTemplate](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_CreateRepositoryCreationTemplate.html)  **
  - **Description:** Grants permission to create the repository creation template
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteLifecyclePolicy](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeleteLifecyclePolicy.html)  **
  - **Description:** Grants permission to delete the specified lifecycle policy
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePullThroughCacheRule](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeletePullThroughCacheRule.html)  **
  - **Description:** Grants permission to delete the pull-through cache rule
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteRegistryPolicy](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeleteRegistryPolicy.html)  **
  - **Description:** Grants permission to delete the registry policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [DeleteRepository](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeleteRepository.html)  **
  - **Description:** Grants permission to delete an existing image repository
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRepositoryCreationTemplate](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeleteRepositoryCreationTemplate.html)  **
  - **Description:** Grants permission to delete the repository creation template
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteRepositoryPolicy](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeleteRepositoryPolicy.html)  **
  - **Description:** Grants permission to delete the repository policy from a specified repository
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteSigningConfiguration](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeleteSigningConfiguration)  **
  - **Description:** Grants permission to delete the signing configuration for the registry
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeregisterPullTimeUpdateExclusion](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeregisterPullTimeUpdateExclusion)  **
  - **Description:** Grants permission to deregister a pull time update exclusion
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeImageReplicationStatus](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeImageReplicationStatus.html)  **
  - **Description:** Grants permission to retrieve replication status about an image in a registry, including failure reason if replication fails
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeImageScanFindings](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeImageScanFindings.html)  **
  - **Description:** Grants permission to describe the image scan findings for the specified image
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeImageSigningStatus](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeImageSigningStatus)  **
  - **Description:** Grants permission to retrieve signing status about an image in a specified registry
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeImages](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeImages.html)  **
  - **Description:** Grants permission to get metadata about the images in a repository, including image size, image tags, and creation date
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribePullThroughCacheRules](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribePullThroughCacheRules.html)  **
  - **Description:** Grants permission to describe the pull-through cache rules
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeRegistry](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeRegistry.html)  **
  - **Description:** Grants permission to describe the registry settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeRepositories](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeRepositories.html)  **
  - **Description:** Grants permission to describe image repositories in a registry
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRepositoryCreationTemplates](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeRepositoryCreationTemplates.html)  **
  - **Description:** Grants permission to describe the repository creation template
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAccountSetting](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetAccountSetting.html)  **
  - **Description:** Grants permission to retrieve account settings
  - **Resource types (\*required):** 
  - **Condition keys:** [ecr:AccountSetting](#list_ecr-ecr_AccountSetting)
  - **Access level:** Read

- **   [GetAuthorizationToken](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetAuthorizationToken.html)  **
  - **Description:** Grants permission to retrieve a token that is valid for a specified registry for 12 hours
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDownloadUrlForLayer](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetDownloadUrlForLayer.html)  **
  - **Description:** Grants permission to retrieve the download URL corresponding to an image layer
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLifecyclePolicy](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetLifecyclePolicy.html)  **
  - **Description:** Grants permission to retrieve the specified lifecycle policy
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLifecyclePolicyPreview](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetLifecyclePolicyPreview.html)  **
  - **Description:** Grants permission to retrieve the results of the specified lifecycle policy preview request
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRegistryPolicy](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetRegistryPolicy.html)  **
  - **Description:** Grants permission to retrieve the registry policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRegistryScanningConfiguration](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetRegistryScanningConfiguration.html)  **
  - **Description:** Grants permission to retrieve registry scanning configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRepositoryPolicy](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetRepositoryPolicy.html)  **
  - **Description:** Grants permission to retrieve the repository policy for a specified repository
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSigningConfiguration](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetSigningConfiguration)  **
  - **Description:** Grants permission to retrieve the signing configuration for the registry
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [InitiateLayerUpload](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_InitiateLayerUpload.html)  **
  - **Description:** Grants permission to notify Amazon ECR that you intend to upload an image layer
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListImages](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ListImages.html)  **
  - **Description:** Grants permission to list all the image IDs for a given repository
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPullTimeUpdateExclusions](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ListPullTimeUpdateExclusions)  **
  - **Description:** Grants permission to list pull time update exclusions for the registry
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for an Amazon ECR resource
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ecr-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecr-aws_TagKeys)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutAccountSetting](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutAccountSetting.html)  **
  - **Description:** Grants permission to update account settings
  - **Resource types (\*required):** 
  - **Condition keys:** [ecr:AccountSetting](#list_ecr-ecr_AccountSetting)
  - **Access level:** Write

- **   [PutImage](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutImage.html)  **
  - **Description:** Grants permission to create or update the image manifest associated with an image
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutImageScanningConfiguration](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutImageScanningConfiguration.html)  **
  - **Description:** Grants permission to update the image scanning configuration for a repository
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutImageTagMutability](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutImageTagMutability.html)  **
  - **Description:** Grants permission to update the image tag mutability settings for a repository
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutLifecyclePolicy](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutLifecyclePolicy.html)  **
  - **Description:** Grants permission to create or update a lifecycle policy
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutRegistryPolicy](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutRegistryPolicy.html)  **
  - **Description:** Grants permission to update the registry policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [PutRegistryScanningConfiguration](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutRegistryScanningConfiguration.html)  **
  - **Description:** Grants permission to update registry scanning configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutReplicationConfiguration](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutReplicationConfiguration.html)  **
  - **Description:** Grants permission to update the replication configuration for the registry
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutSigningConfiguration](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutSigningConfiguration)  **
  - **Description:** Grants permission to update the signing configuration for the registry
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RegisterPullTimeUpdateExclusion](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_RegisterPullTimeUpdateExclusion)  **
  - **Description:** Grants permission to register a pull time update exclusion
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SetRepositoryPolicy](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_SetRepositoryPolicy.html)  **
  - **Description:** Grants permission to apply a repository policy on a specified repository to control access permissions
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [StartImageScan](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_StartImageScan.html)  **
  - **Description:** Grants permission to start an image scan
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartLifecyclePolicyPreview](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_StartLifecyclePolicyPreview.html)  **
  - **Description:** Grants permission to start a preview of the specified lifecycle policy
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag an Amazon ECR resource
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ecr-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecr-aws_TagKeys)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag an Amazon ECR resource
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecr-aws_TagKeys)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [UpdateImageStorageClass](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_UpdateImageStorageClass)  **
  - **Description:** Grants permission to get update the storage class of a specified image within a specified repository
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePullThroughCacheRule](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_UpdatePullThroughCacheRule.html)  **
  - **Description:** Grants permission to update the pull-through cache rule
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRepositoryCreationTemplate](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_UpdateRepositoryCreationTemplate.html)  **
  - **Description:** Grants permission to update the repository creation template
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UploadLayerPart](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_UploadLayerPart.html)  **
  - **Description:** Grants permission to upload an image layer part to Amazon ECR
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ValidatePullThroughCacheRule](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ValidatePullThroughCacheRule.html)  **
  - **Description:** Grants permission to validate the pull-through cache rule
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read



## Permission-only actions for Amazon Elastic Container Registry
<a name="list_ecr-permission-only-actions"></a>

The following actions are defined by Amazon Elastic Container Registry but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [BatchImportUpstreamImage](https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-through-cache.html)  **
  - **Description:** Grants permission to retrieve the image from the upstream registry and import it to your private registry
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetImageCopyStatus](https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-through-cache.html)  **
  - **Description:** Grants permission to retrieve the status about an image copy
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ReplicateImage](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-permissions.html)  **
  - **Description:** Grants permission to replicate images to the destination registry
  - **Resource types (\*required):** [repository\*](#list_ecr-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Elastic Container Registry
<a name="list_ecr-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/Repositories.html)  | arn:${Partition}:ecr:${Region}:${Account}:repository/${RepositoryName} | [aws:ResourceTag/${TagKey}](#list_ecr-aws_ResourceTag___TagKey_)<br />[ecr:ResourceTag/${TagKey}](#list_ecr-ecr_ResourceTag___TagKey_) | 

## Condition keys for Amazon Elastic Container Registry
<a name="list_ecr-policy-keys"></a>

Amazon Elastic Container Registry defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the allowed set of values for each of the tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag-value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of mandatory tags in the request | ArrayOfString | 
|   [ecr:AccountSetting](https://docs.aws.amazon.com/AmazonECR/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the ECR account setting name | String | 
|   [ecr:ResourceTag/${TagKey}](https://docs.aws.amazon.com/AmazonECR/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by tag-value associated with the resource | String | 