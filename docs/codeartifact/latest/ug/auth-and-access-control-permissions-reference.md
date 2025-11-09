# AWS CodeArtifact permissions

reference

## AWS CodeArtifact resources and operations

In AWS CodeArtifact, the primary resource is a domain. In a policy, you use an Amazon
Resource Name (ARN) to identify the resource the policy applies to. Repositories are
also resources and have ARNs associated with them. For more information, see [Amazon Resource Names
(ARNs)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") in the _Amazon Web Services General Reference_.

| Resource type                                                                            | ARN format                                                                                                              |
| ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Domain                                                                                   | `arn:aws:codeartifact:`region-ID`:`account-ID`:domain/`my_domain``                                                      |
| Repository                                                                               | `arn:aws:codeartifact:`region-ID`:`account-ID`:repository/`my_domain`/`my_repo``                                        |
| Package group                                                                            | `arn:aws:codeartifact:`region-ID`:`account-ID`:package-group/`my_domain`/`encoded_package_group_pattern``               |
| Package with a namespace                                                                 | `arn:aws:codeartifact:`region-ID`:`account-ID`:package/`my_domain`/`my_repo`/`package-format`/`namespace`/`my_package`` |
| Package without a namespace                                                              | `arn:aws:codeartifact:`region-ID`:`account-ID`:package/`my_domain`/`my_repo`/`package-format`//`my_package``            |
| All CodeArtifact resources                                                               | `arn:aws:codeartifact:*`                                                                                                |
| All CodeArtifact resources owned by the specified account in the<br>specified AWS Region | `arn:aws:codeartifact:`region-ID`:`account-ID`:*`                                                                       |

Which resource ARN you specify depends on which action or actions you want to control access to.

You can indicate a specific domain (`myDomain`)
in your statement using its ARN as follows.

```
"Resource": "arn:aws:codeartifact:`us-east-2`:`123456789012`:domain/`myDomain`"
```

You can indicate a specific repository (`myRepo`)
in your statement using its ARN as follows.

```
"Resource": "arn:aws:codeartifact:`us-east-2`:`123456789012`:domain/`myDomain`/`myRepo`"
```

To specify multiple resources in a single statement, separate their ARNs with commas. The following statement applies to all
packages and repositories in a specific domain.

```
"Resource": [
  "arn:aws:codeartifact:`us-east-2`:`123456789012`:domain/`myDomain`",
  "arn:aws:codeartifact:`us-east-2`:`123456789012`:repository/`myDomain`/*",
  "arn:aws:codeartifact:`us-east-2`:`123456789012`:package/`myDomain`/*"
]
```

###### Note

Many AWS services treat a colon (:) or a forward slash (/) as the same
character in ARNs. However, CodeArtifact uses an exact match in resource patterns and
rules. Be sure to use the correct characters when you create event patterns so
that they match the ARN syntax in the resource.

## AWS CodeArtifact API operations and permission

You can use the following table as a reference when you are setting up access control and writing permissions
policies that you can attach to an IAM identity (identity-based policies).

You can use AWS-wide condition keys in your AWS CodeArtifact policies to express
conditions. For a list, see [IAM JSON Policy
Elements Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys") in the _IAM User Guide_.

You specify the actions in the policy's `Action` field. To specify an
action, use the `codeartifact:` prefix followed by the API operation name (for
example, `codeartifact:CreateDomain` and
`codeartifact:AssociateExternalConnection`). To specify multiple actions in a single
statement, separate them with commas (for example, `"Action": [
 "codeartifact:CreateDomain", "codeartifact:AssociateExternalConnection" ]`).

**Using wildcard characters**

You specify an ARN, with or without a wildcard character (\*), as the resource value in
the policy's `Resource` field. You can use a wildcard to specify multiple
actions or resources. For example, `codeartifact:*` specifies all CodeArtifact actions
and `codeartifact:Describe*` specifies all CodeArtifact actions that begin with the
word `Describe`.

CodeArtifact API operations and required
permissions for actions| AWS CodeArtifact API operations | Required permissions (API actions) | Resources |
| --- | --- | --- |
| `AssociateExternalConnection` | `codeartifact:AssociateExternalConnection`<br>Required to add an external connection to a repository. | `arn:aws:codeartifact:`region-ID`:`account-ID`:repository/`my_domain`/`my_repo`` |
| `CopyPackageVersions` | To copy package versions from a source repository to a destination<br>repository:<br>`codeartifact:CopyPackageVersions`<br>Required on the destination repository.<br>`codeartifact:ReadFromRepository`<br>Required on the source repository. | `arn:aws:codeartifact:`region-ID`:`account-ID`:repository/`my_domain`/`my_repo`` |
| `CreateDomain` | `codeartifact:CreateDomain`<br>Required to create domains.<br>`kms:DescribeKey` and `kms:CreateGrant`<br>Required on the supplied KMS key when specifying a non-default `encryptionKey`. | `arn:aws:codeartifact:`region-ID`:`account-ID`:domain/`my_domain`` |
| `CreatePackageGroup` | `codeartifact:CreatePackageGroup`<br>Required to create package groups. | `arn:aws:codeartifact:`region-ID`:`account-ID`:package-group/`my_domain`/`encoded_package_group_pattern`` |
| `CreateRepository` | `codeartifact:CreateRepository`<br>Required to create repositories.<br>`codeartifact:AssociateWithDownstreamRepository`<br>Required on a repository so it can be added as an upstream repository to downstream<br>repositories. | `arn:aws:codeartifact:`region-ID`:`account-ID`:repository/`my_domain`/`my_repo`` |
| `DeleteDomain` | `codeartifact:DeleteDomain`<br>Required to delete domains. | `arn:aws:codeartifact:`region-ID`:`account-ID`:domain/`my_domain`` |
| `DeleteDomainPermissionsPolicy` | `codeartifact:DeleteDomainPermissionsPolicy`<br>Required to delete a domain's resource policy. | `arn:aws:codeartifact:`region-ID`:`account-ID`:domain/`my_domain`` |
| `DeletePackage` | `codeartifact:DeletePackage`<br>Required to delete a package. | `arn:aws:codeartifact:`region-ID`:`account-ID`:package/`my_domain`/`my_repo`/`package-format`/`namespace`/`my_package`` |
| `DeletePackageGroup` | `codeartifact:DeletePackageGroup`<br>Required to delete a package group. | `arn:aws:codeartifact:`region-ID`:`account-ID`:package-group/`my_domain`/`encoded_package_group_pattern`` |
| `DeletePackageVersions` | `codeartifact:DeletePackageVersions`<br>Required to delete versions of a package. | `arn:aws:codeartifact:`region-ID`:`account-ID`:package/`my_domain`/`my_repo`/`package-format`/`namespace`/`my_package`` |
| `DeleteRepository` | `codeartifact:DeleteRepository`<br>Required to delete a repository. | `arn:aws:codeartifact:`region-ID`:`account-ID`:repository/`my_domain`/`my_repo`` |
| `DeleteRepositoryPermissionsPolicy` | `codeartifact:DeleteRepositoryPermissionsPolicy`<br>Required to delete a repository's resource policy. | `arn:aws:codeartifact:`region-ID`:`account-ID`:repository/`my_domain`/`my_repo`` |
| `DescribeDomain` | `codeartifact:DescribeDomain`<br>Required to get information about a domain. | `arn:aws:codeartifact:`region-ID`:`account-ID`:domain/`my_domain`` |
| `DescribePackage` | `codeartifact:DescribePackage`<br>Required to get information about a package. | `arn:aws:codeartifact:`region-ID`:`account-ID`:package/`my_domain`/`my_repo`/`package-format`/`namespace`/`my_package`` |
| `DescribePackageGroup` | `codeartifact:DescribePackageGroup`<br>Required to get information about a package group. | `arn:aws:codeartifact:`region-ID`:`account-ID`:package-group/`my_domain`/`encoded_package_group_pattern`` |
| `DescribePackageVersion` | `codeartifact:DescribePackageVersion`<br>Required to get information about a package version. | `arn:aws:codeartifact:`region-ID`:`account-ID`:package/`my_domain`/`my_repo`/`package-format`/`namespace`/`my_package`` |
| `DescribeRepository` | `codeartifact:DescribeRepository`<br>Required to get information about a repository. | `arn:aws:codeartifact:`region-ID`:`account-ID`:repository/`my_domain`/`my_repo`` |
| `DisassociateExternalConnection` | `codeartifact:DisassociateExternalConnection`<br>Required to remove an external connection from a repository. | `arn:aws:codeartifact:`region-ID`:`account-ID`:repository/`my_domain`/`my_repo`` |
| `DisposePackageVersions` | `codeartifact:DisposePackageVersions`<br>Required to dispose versions of a package. | `arn:aws:codeartifact:`region-ID`:`account-ID`:package/`my_domain`/`my_repo`/`package-format`/`namespace`/`my_package`` |
| `GetAssociatedPackageGroup` | `codeartifact:GetAssociatedPackageGroup`<br>Required to get the associated package group of a package. | `arn:aws:codeartifact:`region-ID`:`account-ID`:package-group/`my_domain`/`encoded_package_group_pattern`` |
| `GetAuthorizationToken` | `codeartifact:GetAuthorizationToken`<br>`sts:GetServiceBearerToken`<br>Required to get a temporary authorization token for accessing<br>repositories. | `arn:aws:codeartifact:`region-ID`:`account-ID`:domain/`my_domain`` |
| `GetDomainPermissionsPolicy` | `codeartifact:GetDomainPermissionsPolicy`<br>Required to get a domain resource policy. | `arn:aws:codeartifact:`region-ID`:`account-ID`:domain/`my_domain`` |
| `GetPackageVersionAsset` | `codeartifact:GetPackageVersionAsset`<br>Required to get assets in a package version. | `arn:aws:codeartifact:`region-ID`:`account-ID`:package/`my_domain`/`my_repo`/`package-format`/`namespace`/`my_package`` |
| `GetPackageVersionReadme` | `codeartifact:GetPackageVersionReadme`<br>Required to get the readme of a package version. | `arn:aws:codeartifact:`region-ID`:`account-ID`:package/`my_domain`/`my_repo`/`package-format`/`namespace`/`my_package`` |
| `GetRepositoryEndpoint` | `codeartifact:GetRepositoryEndpoint`<br>Required to get a repository endpoint. | `arn:aws:codeartifact:`region-ID`:`account-ID`:repository/`my_domain`/`my_repo`` |
| `GetRepositoryPermissionsPolicy` | `codeartifact:GetRepositoryPermissionsPolicy`<br>Required to get a repository resource policy. | `arn:aws:codeartifact:`region-ID`:`account-ID`:repository/`my_domain`/`my_repo`` |
| `ListAssociatedPackages` | `codeartifact:ListAssociatedPackages`<br>Required to return a list of packages associated with a package group. | `arn:aws:codeartifact:`region-ID`:`account-ID`:package-group/`my_domain`/`encoded_package_group_pattern`` |
| `ListDomains` | `codeartifact:ListDomains`<br>Required to return a paginated list of domains in an AWS<br>account. | `*` |
| `ListPackageGroups` | `codeartifact:ListPackageGroups`<br>Required to return a paginated list of package groups in a domain. | `arn:aws:codeartifact:`region-ID`:`account-ID`:domain/`my_domain`` |
| `ListPackages` | `codeartifact:ListPackages`<br>Required to return a paginated list of packages in a repository. | `arn:aws:codeartifact:`region-ID`:`account-ID`:repository/`my_domain`/`my_repo`` |
| `ListPackageVersionAssets` | `codeartifact:ListPackageVersionAssets`<br>Required to return a paginated list of assets in a package<br>version. | `arn:aws:codeartifact:`region-ID`:`account-ID`:package/`my_domain`/`my_repo`/`package-format`/`namespace`/`my_package`` |
| `ListPackageVersionDependencies` | `codeartifact:ListPackageVersionDependencies`<br>Required to return a paginated list of a package version's<br>dependencies. | `arn:aws:codeartifact:`region-ID`:`account-ID`:package/`my_domain`/`my_repo`/`package-format`/`namespace`/`my_package`` |
| `ListPackageVersions` | `codeartifact:ListPackageVersions`<br>Required to return a paginated list of package versions in a<br>repository. | `arn:aws:codeartifact:`region-ID`:`account-ID`:package/`my_domain`/`my_repo`/`package-format`/`namespace`/`my_package`` |
| `ListRepositories` | `codeartifact:ListRepositories`<br>Required to return a paginated list of repositories in an AWS<br>account. | `*` |
| `ListRepositoriesInDomain` | `codeartifact:ListRepositoriesInDomain`<br>Required to return a paginated list of repositories in a domain. | `arn:aws:codeartifact:`region-ID`:`account-ID`:domain/`my_domain`` |
| `ListSubPackageGroups` | `codeartifact:ListSubPackageGroups`<br>Required to return a list of direct child package groups of a package group. | `arn:aws:codeartifact:`region-ID`:`account-ID`:package-group/`my_domain`/`encoded_package_group_pattern`` |
| `ListTagsForResource` | `codeartifact:ListTagsForResource`<br>Required to list tags for a specified resource. | `arn:aws:codeartifact:`region-ID`:`account-ID`:domain/`my_domain``<br>`arn:aws:codeartifact:`region-ID`:`account-ID`:repository/`my_domain`/`my_repo`` |
| `PublishPackageVersion` | `codeartifact:PublishPackageVersion`<br>Required to publish a package version to a repository. | `arn:aws:codeartifact:`region-ID`:`account-ID`:package/`my_domain`/`my_repo`/`package-format`/`namespace`/`my_package`` |
| `PutDomainPermissionsPolicy` | `codeartifact:PutDomainPermissionsPolicy`<br>Required to add a resource policy to a domain. | `arn:aws:codeartifact:`region-ID`:`account-ID`:domain/`my_domain`` |
| `PutPackageMetadata` | `codeartifact:PutPackageMetadata`<br>Required to publish Maven package versions to a repository, or to add or remove npm tags from<br>npm package versions. | `arn:aws:codeartifact:`region-ID`:`account-ID`:package/`my_domain`/`my_repo`/`package-format`/`namespace`/`my_package`` |
| `PutPackageOriginConfiguration` | `codeartifact:PutPackageOriginConfiguration`<br>Required to update a package's origin configuration. | `arn:aws:codeartifact:`region-ID`:`account-ID`:package/`my_domain`/`my_repo`/`package-format`/`namespace`/`my_package`` |
| `PutRepositoryPermissionsPolicy` | `codeartifact:PutRepositoryPermissionsPolicy`<br>Required to add a resource policy to a repository. | `arn:aws:codeartifact:`region-ID`:`account-ID`:repository/`my_domain`/`my_repo`` |
| `ReadFromRepository` | `codeartifact:ReadFromRepository`<br>Required to read from a repository using a package manager<br>client. | `arn:aws:codeartifact:`region-ID`:`account-ID`:repository/`my_domain`/`my_repo`` |
| `TagResource` | `codeartifact:TagResource`<br>Required to tag a resource. | `arn:aws:codeartifact:`region-ID`:`account-ID`:domain/`my_domain``<br>`arn:aws:codeartifact:`region-ID`:`account-ID`:repository/`my_domain`/`my_repo`` |
| `UntagResource` | `codeartifact:UntagResource`<br>Required to remove a tag from a resource. | `arn:aws:codeartifact:`region-ID`:`account-ID`:domain/`my_domain``<br>`arn:aws:codeartifact:`region-ID`:`account-ID`:repository/`my_domain`/`my_repo`` |
| `UpdatePackageGroup` | `codeartifact:UpdatePackageGroup`<br>Required to update a package group. | `arn:aws:codeartifact:`region-ID`:`account-ID`:package-group/`my_domain`/`encoded_package_group_pattern`` |
| `UpdatePackageGroupOriginConfiguration` | `codeartifact:UpdatePackageGroupOriginConfiguration`<br>Required to update a package group's origin configuration. | `arn:aws:codeartifact:`region-ID`:`account-ID`:package-group/`my_domain`/`encoded_package_group_pattern`` |
| `UpdatePackageVersionsStatus` | `codeartifact:UpdatePackageVersionsStatus`<br>Required to change the status of a package version. | `arn:aws:codeartifact:`region-ID`:`account-ID`:package/`my_domain`/`my_repo`/`package-format`/`namespace`/`my_package`` |
| `UpdateRepository` | `codeartifact:UpdateRepository`<br>Required to update a repository's description or upstream connections. See<br>[Modify a repository upstream<br>configuration](config-repos.md#modify-upstream "config-repos.md#modify-upstream") or<br>[UpdateRepository](../APIReference/API_UpdateRepository.md "../APIReference/API_UpdateRepository.md")<br>in the *CodeArtifact API Guide<br>• for more information.<br>`codeartifact:AssociateWithDownstreamRepository`<br>Required on a repository so it can be added as an upstream repository to downstream<br>repositories. | `arn:aws:codeartifact:`region-ID`:`account-ID`:repository/`my_domain`/`my_repo`` |

## Package group ARNs

###### Note

This section about how package group ARNs and pattern encoding is informational. It is recommended to copy ARNs
from the console, or fetch ARNs using the `DescribePackageGroup` API instead of encoding patterns and constructing ARNs.

IAM policies use the wildcard character, `*`, to match multiple IAM actions or multiple resources. Package group patterns
also use the `*` character. In order to more easily write IAM policies that match a
single package group, the package group ARN format uses an encoded version of the package group pattern.

Specifically, the package group ARN format is as follows:

```
arn:aws:codeartifact:`region`:`account-ID`:package-group/`my_domain`/`encoded_package_group_pattern`
```

Where the encoded package group pattern is the package group pattern, with certain special characters
replaced with their percent-encoded values. The following list
contains the characters and their corresponding percent-encoded values:

- `*` : `%2a`
- `$` : `%24`
- `%` : `%25`

For example, the ARN for a root package group of a domain, (`/*`), would be:

```
arn:aws:codeartifact:`us-east-1`:`111122223333`:package-group/`my_domain`/%2a
```

Note that characters not included in the list can not be encoded, and ARNs are case-sensitive, so `*` must
be encoded as `%2a` and not `%2A`.
