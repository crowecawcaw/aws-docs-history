# Preventing image tags from being overwritten in Amazon ECR

You can prevent image tags from being overwritten by turning on tag immutability in a
repository. After tag immutability is turned on, the `ImageTagAlreadyExistsException` error is returned if you push an image with a tag
that is already in the repository. Tag immutability affects all tags. You cannot make
some tags immutable while others aren't.

You can use the AWS Management Console and AWS CLI tools to set image tag mutability for a new
repository or for an existing repository. To create a repository using console steps,
see [Creating an Amazon ECR private repository to store images](repository-create.md "repository-create.md").

## Setting image tag mutability (AWS Management Console)

###### To set image tag mutability

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories "https://console.aws.amazon.com/ecr/repositories").
2. From the navigation bar, choose the Region that contains the repository to
   edit.
3. In the navigation pane, choose **Repositories** under **Private
   registry**.

If you don't see **Repositories**, choose **Private
registry** to expand the menu and then choose **Repositories**. 4. On the **Private repositories** page, choose the radio
button before the repository name for which you want to set the image tag
mutability settings. 5. Choose **Actions** and then choose **Repository**
under **Edit**. 6. For **Image tag immutability**, choose one of the
following tag mutability settings for the repository.

    * **Mutable** – Choose this option if you
     want image tags to be overwritten. Recommended for repositories
     using pull through cache actions to ensure Amazon ECR can update cached
     images. Additionally, to disable tag updates for a few mutable tags,
     enter tag names or use wildcards (\*) to match multiple similar tags
     in the **Mutable tag exclusion** text box.
    * **Immutable** – Choose this option if you
     want to prevent image tags from being overwritten, and it applies to
     all tags and exclusions in the repository when pushing an image with
     existing tag. Amazon ECR returns an `ImageTagAlreadyExistsException`
     if you attempt to push an image with an existing tag. Additionally,
     to enable tag updates for a few immutable tags, enter tag names or
     use wildcards (\*) to match multiple similar tags in the **Immutable
     tag
     exclusion** text box.

7. For **Image scan settings**, while you can specify the
   scan settings at the repository level for basic scanning, it is best
   practice to specify the scan configuration at the private registry level.
   Specify the scanning settings at the private registry allow you to enable
   either enhanced scanning or basic scanning as well as define filters to
   specify which repositories are scanned. For more information, see [Scan images for software vulnerabilities in Amazon ECR](image-scanning.md "image-scanning.md").
8. For **Encryption settings**, this is a view only field as
   the encryption settings for a repository can't be changed once the
   repository is created.
9. Choose **Save** to update the repository settings.

## Setting image tag mutability (AWS CLI)

###### To create a repository with immutable tags configured

Use one of the following commands to create a new image repository with
immutable tags configured.

- [create-repository](../../../cli/latest/reference/ecr/create-repository.md "../../../cli/latest/reference/ecr/create-repository.md")
  (AWS CLI) with image tag mutability

```
`aws ecr create-repository --repository-name `name` --image-tag-mutability `IMMUTABLE` --region `us-east-2``
```

- [create-repository](../../../cli/latest/reference/ecr/create-repository.md "../../../cli/latest/reference/ecr/create-repository.md")
  (AWS CLI) with image tag mutability exclusion filters

```
`aws ecr create-repository --repository-name `name` --image-tag-mutability `IMMUTABLE_WITH_EXCLUSION` --image-tag-mutability-exclusion-filters filterType=`WILDCARD`,filter=`filter-text`` `--region `us-east-2``
```

- [New-ECRRepository](../../../powershell/latest/reference/items/New-ECRRepository.md "../../../powershell/latest/reference/items/New-ECRRepository.md")
  (AWS Tools for Windows PowerShell) with image tag mutability

```
`New-ECRRepository -RepositoryName `name` -ImageTagMutability `IMMUTABLE` -Region `us-east-2` -Force`
```

- [New-ECRRepository](../../../powershell/latest/reference/items/New-ECRRepository.md "../../../powershell/latest/reference/items/New-ECRRepository.md")
  (AWS Tools for Windows PowerShell) with image tag mutability exclusion filters

```
`New-ECRRepository -RepositoryName `name` -ImageTagMutability `IMMUTABLE_WITH_EXCLUSION` -ImageTagMutabilityExclusionFilter @{FilterType=`WILDCARD` Filter=`filter-text`}` `-Region `us-east-2` -Force`
```

###### To update the image tag mutability settings for a repository

Use one of the following commands to update the image tag mutability settings
for an existing repository.

- [put-image-tag-mutability](../../../cli/latest/reference/ecr/put-image-tag-mutability.md "../../../cli/latest/reference/ecr/put-image-tag-mutability.md") (AWS CLI) with image tag mutability

```
`aws ecr put-image-tag-mutability --repository-name `name` --image-tag-mutability `IMMUTABLE` --region `us-east-2``
```

- [put-image-tag-mutability](../../../cli/latest/reference/ecr/put-image-tag-mutability.md "../../../cli/latest/reference/ecr/put-image-tag-mutability.md") (AWS CLI) with image tag mutability exclusion
  filters

```
`aws ecr put-image-tag-mutability --repository-name `name` --image-tag-mutability `IMMUTABLE_WITH_EXCLUSION` --image-tag-mutability-exclusion-filters filterType=`WILDCARD`,filter=`latest`` `--region `us-east-2``
```

- [Write-ECRImageTagMutability](../../../powershell/latest/reference/items/Write-ECRImageTagMutability.md "../../../powershell/latest/reference/items/Write-ECRImageTagMutability.md") (AWS Tools for Windows PowerShell) with image tag mutability

```
`Write-ECRImageTagMutability -RepositoryName `name` -ImageTagMutability `IMMUTABLE` -Region `us-east-2` -Force`
```

- [Write-ECRImageTagMutability](../../../powershell/latest/reference/items/Write-ECRImageTagMutability.md "../../../powershell/latest/reference/items/Write-ECRImageTagMutability.md") (AWS Tools for Windows PowerShell) with image tag mutability
  exclusion filters

```
`Write-ECRImageTagMutability -RepositoryName `name` -ImageTagMutability `IMMUTABLE_WITH_EXCLUSION` -ImageTagMutabilityExclusionFilter @{FilterType=`WILDCARD` Filter=`latest`}`
```
