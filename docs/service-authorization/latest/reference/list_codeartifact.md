

# Actions, resources, and condition keys for AWS CodeArtifact
<a name="list_codeartifact"></a>

AWS CodeArtifact (service prefix: `codeartifact`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/codeartifact/latest/ug/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/codeartifact/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/codeartifact/latest/ug/auth-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/codeartifact/codeartifact.json) for this service.

**Topics**
+ [Actions defined by AWS CodeArtifact](#list_codeartifact-actions-as-permissions)
+ [Resource types defined by AWS CodeArtifact](#list_codeartifact-resources-for-iam-policies)
+ [Condition keys for AWS CodeArtifact](#list_codeartifact-policy-keys)

## Actions defined by AWS CodeArtifact
<a name="list_codeartifact-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateExternalConnection](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssociateExternalConnection.html)  **
  - **Description:** Grants permission to add an external connection to a repository
  - **Resource types (\*required):** [repository\*](#list_codeartifact-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateWithDownstreamRepository](https://docs.aws.amazon.com/codeartifact/latest/ug/repos-upstream.html)  **
  - **Description:** Grants permission to associate an existing repository as an upstream repository to another repository
  - **Resource types (\*required):** [repository\*](#list_codeartifact-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CopyPackageVersions](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_CopyPackageVersions.html)  **
  - **Description:** Grants permission to copy package versions from one repository to another repository in the same domain
  - **Resource types (\*required):** [package\*](#list_codeartifact-resource-package) / **Condition keys:**  
  - **Resource types (\*required):** [repository\*](#list_codeartifact-resource-repository) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDomain](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_CreateDomain.html)  **
  - **Description:** Grants permission to create a new domain
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codeartifact-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_codeartifact-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePackageGroup](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_CreatePackageGroup.html)  **
  - **Description:** Grants permission to create a package group
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codeartifact-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_codeartifact-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRepository](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_CreateRepository.html)  **
  - **Description:** Grants permission to create a new repository
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codeartifact-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_codeartifact-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteDomain](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeleteDomain.html)  **
  - **Description:** Grants permission to delete a domain
  - **Resource types (\*required):** [domain\*](#list_codeartifact-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDomainPermissionsPolicy](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeleteDomainPermissionsPolicy.html)  **
  - **Description:** Grants permission to delete the resource policy set on a domain
  - **Resource types (\*required):** [domain\*](#list_codeartifact-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeletePackage](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeletePackage.html)  **
  - **Description:** Grants permission to delete a package
  - **Resource types (\*required):** [package\*](#list_codeartifact-resource-package)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeletePackageGroup](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeletePackageGroup.html)  **
  - **Description:** Grants permission to delete a package group
  - **Resource types (\*required):** [package-group\*](#list_codeartifact-resource-package-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePackageVersions](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeletePackageVersions.html)  **
  - **Description:** Grants permission to delete package versions
  - **Resource types (\*required):** [package\*](#list_codeartifact-resource-package)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteRepository](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeleteRepository.html)  **
  - **Description:** Grants permission to delete a repository
  - **Resource types (\*required):** [repository\*](#list_codeartifact-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRepositoryPermissionsPolicy](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeleteRepositoryPermissionsPolicy.html)  **
  - **Description:** Grants permission to delete the resource policy set on a repository
  - **Resource types (\*required):** [repository\*](#list_codeartifact-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DescribeDomain](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribeDomain.html)  **
  - **Description:** Grants permission to return information about a domain
  - **Resource types (\*required):** [domain\*](#list_codeartifact-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribePackage](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribePackage.html)  **
  - **Description:** Grants permission to retrieve information about a package
  - **Resource types (\*required):** [package\*](#list_codeartifact-resource-package)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribePackageGroup](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribePackageGroup.html)  **
  - **Description:** Grants permission to return detailed information about a package group
  - **Resource types (\*required):** [package-group\*](#list_codeartifact-resource-package-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribePackageVersion](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribePackageVersion.html)  **
  - **Description:** Grants permission to return information about a package version
  - **Resource types (\*required):** [package\*](#list_codeartifact-resource-package)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeRepository](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribeRepository.html)  **
  - **Description:** Grants permission to return detailed information about a repository
  - **Resource types (\*required):** [repository\*](#list_codeartifact-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DisassociateExternalConnection](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DisassociateExternalConnection.html)  **
  - **Description:** Grants permission to disassociate an external connection from a repository
  - **Resource types (\*required):** [repository\*](#list_codeartifact-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisposePackageVersions](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DisposePackageVersions.html)  **
  - **Description:** Grants permission to set the status of package versions to Disposed and delete their assets
  - **Resource types (\*required):** [package\*](#list_codeartifact-resource-package)
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetAssociatedPackageGroup](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetAssociatedPackageGroup.html)  **
  - **Description:** Grants permission to return a package's associated package group
  - **Resource types (\*required):** [package-group\*](#list_codeartifact-resource-package-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAuthorizationToken](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetAuthorizationToken.html)  **
  - **Description:** Grants permission to generate a temporary authentication token for accessing repositories in a domain
  - **Resource types (\*required):** [domain\*](#list_codeartifact-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDomainPermissionsPolicy](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetDomainPermissionsPolicy.html)  **
  - **Description:** Grants permission to return a domain's resource policy
  - **Resource types (\*required):** [domain\*](#list_codeartifact-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPackageVersionAsset](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetPackageVersionAsset.html)  **
  - **Description:** Grants permission to return an asset (or file) that is part of a package version
  - **Resource types (\*required):** [package\*](#list_codeartifact-resource-package)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPackageVersionReadme](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetPackageVersionReadme.html)  **
  - **Description:** Grants permission to return a package version's readme file
  - **Resource types (\*required):** [package\*](#list_codeartifact-resource-package)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRepositoryEndpoint](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetRepositoryEndpoint.html)  **
  - **Description:** Grants permission to return an endpoint for a repository
  - **Resource types (\*required):** [repository\*](#list_codeartifact-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRepositoryPermissionsPolicy](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetRepositoryPermissionsPolicy.html)  **
  - **Description:** Grants permission to return a repository's resource policy
  - **Resource types (\*required):** [repository\*](#list_codeartifact-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAllowedRepositoriesForGroup](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListRepositoriesInDomain.html)  **
  - **Description:** Grants permission to list the allowed repositories for a package group
  - **Resource types (\*required):** [package-group\*](#list_codeartifact-resource-package-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAssociatedPackages](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListAssociatedPackages.html)  **
  - **Description:** Grants permission to list the packages associated to a package group
  - **Resource types (\*required):** [package-group\*](#list_codeartifact-resource-package-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDomains](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListDomains.html)  **
  - **Description:** Grants permission to list the domains in the current user's AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPackageGroups](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageGroups.html)  **
  - **Description:** Grants permission to list the package groups in a domain
  - **Resource types (\*required):** [domain\*](#list_codeartifact-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPackageVersionAssets](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersionAssets.html)  **
  - **Description:** Grants permission to list a package version's assets
  - **Resource types (\*required):** [package\*](#list_codeartifact-resource-package)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPackageVersionDependencies](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersionDependencies.html)  **
  - **Description:** Grants permission to list the direct dependencies of a package version
  - **Resource types (\*required):** [package\*](#list_codeartifact-resource-package)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPackageVersions](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html)  **
  - **Description:** Grants permission to list a package's versions
  - **Resource types (\*required):** [package\*](#list_codeartifact-resource-package)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPackages](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackages.html)  **
  - **Description:** Grants permission to list the packages in a repository
  - **Resource types (\*required):** [repository\*](#list_codeartifact-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRepositories](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListRepositories.html)  **
  - **Description:** Grants permission to list the repositories administered by the calling account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRepositoriesInDomain](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListRepositoriesInDomain.html)  **
  - **Description:** Grants permission to list the repositories in a domain
  - **Resource types (\*required):** [domain\*](#list_codeartifact-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSubPackageGroups](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListSubPackageGroups.html)  **
  - **Description:** Grants permission to list the sub package groups for a parent package group
  - **Resource types (\*required):** [package-group\*](#list_codeartifact-resource-package-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a CodeArtifact resource
  - **Resource types (\*required):** [domain](#list_codeartifact-resource-domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [package-group](#list_codeartifact-resource-package-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [repository](#list_codeartifact-resource-repository) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [PublishPackageVersion](https://docs.aws.amazon.com/codeartifact/latest/ug/repo-policies.html)  **
  - **Description:** Grants permission to publish assets and metadata to a repository endpoint
  - **Resource types (\*required):** [package\*](#list_codeartifact-resource-package)
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutDomainPermissionsPolicy](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PutDomainPermissionsPolicy.html)  **
  - **Description:** Grants permission to attach a resource policy to a domain
  - **Resource types (\*required):** [domain\*](#list_codeartifact-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutPackageMetadata](https://docs.aws.amazon.com/codeartifact/latest/ug/repo-policies.html)  **
  - **Description:** Grants permission to add, modify or remove package metadata using a repository endpoint
  - **Resource types (\*required):** [package\*](#list_codeartifact-resource-package)
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutPackageOriginConfiguration](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PutPackageOriginConfiguration.html)  **
  - **Description:** Grants permission to set origin configuration for a package
  - **Resource types (\*required):** [package\*](#list_codeartifact-resource-package)
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutRepositoryPermissionsPolicy](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PutRepositoryPermissionsPolicy.html)  **
  - **Description:** Grants permission to attach a resource policy to a repository
  - **Resource types (\*required):** [repository\*](#list_codeartifact-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ReadFromRepository](https://docs.aws.amazon.com/codeartifact/latest/ug/repo-policies.html)  **
  - **Description:** Grants permission to return package assets and metadata from a repository endpoint
  - **Resource types (\*required):** [repository\*](#list_codeartifact-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a CodeArtifact resource
  - **Resource types (\*required):** [domain](#list_codeartifact-resource-domain) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_codeartifact-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codeartifact-aws_TagKeys)
  - **Resource types (\*required):** [package-group](#list_codeartifact-resource-package-group) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_codeartifact-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codeartifact-aws_TagKeys)
  - **Resource types (\*required):** [repository](#list_codeartifact-resource-repository) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_codeartifact-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codeartifact-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove a tag from a CodeArtifact resource
  - **Resource types (\*required):** [domain](#list_codeartifact-resource-domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codeartifact-aws_TagKeys)
  - **Resource types (\*required):** [package-group](#list_codeartifact-resource-package-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codeartifact-aws_TagKeys)
  - **Resource types (\*required):** [repository](#list_codeartifact-resource-repository) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codeartifact-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdatePackageGroup](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageGroup.html)  **
  - **Description:** Grants permission to modify the properties of a package group
  - **Resource types (\*required):** [package-group\*](#list_codeartifact-resource-package-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePackageGroupOriginConfiguration](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageGroupOriginConfiguration.html)  **
  - **Description:** Grants permission to modify the package origin configuration of a package group
  - **Resource types (\*required):** [package-group\*](#list_codeartifact-resource-package-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePackageVersionsStatus](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageVersionsStatus.html)  **
  - **Description:** Grants permission to modify the status of one or more versions of a package
  - **Resource types (\*required):** [package\*](#list_codeartifact-resource-package)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRepository](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdateRepository.html)  **
  - **Description:** Grants permission to modify the properties of a repository
  - **Resource types (\*required):** [repository\*](#list_codeartifact-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS CodeArtifact
<a name="list_codeartifact-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [domain](https://docs.aws.amazon.com/codeartifact/latest/ug/domains.html)  | arn:${Partition}:codeartifact:${Region}:${Account}:domain/${DomainName} | [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_) | 
|  [package](https://docs.aws.amazon.com/codeartifact/latest/ug/packages.html)  | arn:${Partition}:codeartifact:${Region}:${Account}:package/${DomainName}/${RepositoryName}/${PackageFormat}/${PackageNamespace}/${PackageName} |   | 
|  [package-group](https://docs.aws.amazon.com/codeartifact/latest/ug/package-groups.html)  | arn:${Partition}:codeartifact:${Region}:${Account}:package-group/${DomainName}${EncodedPackageGroupPattern} | [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_) | 
|  [repository](https://docs.aws.amazon.com/codeartifact/latest/ug/repos.html)  | arn:${Partition}:codeartifact:${Region}:${Account}:repository/${DomainName}/${RepositoryName} | [aws:ResourceTag/${TagKey}](#list_codeartifact-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS CodeArtifact
<a name="list_codeartifact-policy-keys"></a>

AWS CodeArtifact defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 