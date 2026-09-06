

# Data retrieval APIs for Amazon Elastic Container Registry
<a name="amazonelasticcontainerregistry"></a>

Amazon Elastic Container Registry provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="ecr-BatchCheckLayerAvailability"></a>[BatchCheckLayerAvailability](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_BatchCheckLayerAvailability.html) | Check the availability of multiple image layers in a specified registry and repository | Read | 
| <a name="ecr-BatchGetImage"></a>[BatchGetImage](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_BatchGetImage.html) | Get detailed information for specified images within a specified repository | Read | 
| <a name="ecr-BatchGetRepositoryScanningConfiguration"></a>[BatchGetRepositoryScanningConfiguration](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_BatchGetRepositoryScanningConfiguration.html) | Retrieve repository scanning configuration for a list of repositories | Read | 
| <a name="ecr-DescribeImageReplicationStatus"></a>[DescribeImageReplicationStatus](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeImageReplicationStatus.html) | Retrieve replication status about an image in a registry, including failure reason if replication fails | Read | 
| <a name="ecr-DescribeImageScanFindings"></a>[DescribeImageScanFindings](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeImageScanFindings.html) | Describe the image scan findings for the specified image | Read | 
| <a name="ecr-DescribeImageSigningStatus"></a>[DescribeImageSigningStatus](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeImageSigningStatus) | Retrieve signing status about an image in a specified registry | Read | 
| <a name="ecr-DescribeImages"></a>[DescribeImages](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeImages.html) | Get metadata about the images in a repository, including image size, image tags, and creation date | List | 
| <a name="ecr-DescribePullThroughCacheRules"></a>[DescribePullThroughCacheRules](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribePullThroughCacheRules.html) | Describe the pull-through cache rules | List | 
| <a name="ecr-DescribeRegistry"></a>[DescribeRegistry](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeRegistry.html) | Describe the registry settings | Read | 
| <a name="ecr-DescribeRepositories"></a>[DescribeRepositories](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeRepositories.html) | Describe image repositories in a registry | Read | 
| <a name="ecr-DescribeRepositoryCreationTemplates"></a>[DescribeRepositoryCreationTemplates](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeRepositoryCreationTemplates.html) | Describe the repository creation template | Read | 
| <a name="ecr-GetAccountSetting"></a>[GetAccountSetting](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetAccountSetting.html) | Retrieve account settings | Read | 
| <a name="ecr-GetAuthorizationToken"></a>[GetAuthorizationToken](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetAuthorizationToken.html) | Retrieve a token that is valid for a specified registry for 12 hours | Read | 
| <a name="ecr-GetDownloadUrlForLayer"></a>[GetDownloadUrlForLayer](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetDownloadUrlForLayer.html) | Retrieve the download URL corresponding to an image layer | Read | 
| <a name="ecr-GetImageCopyStatus"></a>[GetImageCopyStatus](https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-through-cache.html) | Retrieve the status about an image copy | Read | 
| <a name="ecr-GetLifecyclePolicy"></a>[GetLifecyclePolicy](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetLifecyclePolicy.html) | Retrieve the specified lifecycle policy | Read | 
| <a name="ecr-GetLifecyclePolicyPreview"></a>[GetLifecyclePolicyPreview](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetLifecyclePolicyPreview.html) | Retrieve the results of the specified lifecycle policy preview request | Read | 
| <a name="ecr-GetRegistryPolicy"></a>[GetRegistryPolicy](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetRegistryPolicy.html) | Retrieve the registry policy | Read | 
| <a name="ecr-GetRegistryScanningConfiguration"></a>[GetRegistryScanningConfiguration](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetRegistryScanningConfiguration.html) | Retrieve registry scanning configuration | Read | 
| <a name="ecr-GetRepositoryPolicy"></a>[GetRepositoryPolicy](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetRepositoryPolicy.html) | Retrieve the repository policy for a specified repository | Read | 
| <a name="ecr-GetSigningConfiguration"></a>[GetSigningConfiguration](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetSigningConfiguration) | Retrieve the signing configuration for the registry | Read | 
| <a name="ecr-ListImages"></a>[ListImages](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ListImages.html) | List all the image IDs for a given repository | List | 
| <a name="ecr-ListPullTimeUpdateExclusions"></a>[ListPullTimeUpdateExclusions](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ListPullTimeUpdateExclusions) | List pull time update exclusions for the registry | List | 
| <a name="ecr-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ListTagsForResource.html) | List the tags for an Amazon ECR resource | Read | 
| <a name="ecr-ValidatePullThroughCacheRule"></a>[ValidatePullThroughCacheRule](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ValidatePullThroughCacheRule.html) | Validate the pull-through cache rule | Read | 