# Create a repository

Because all packages in CodeArtifact are stored in [repositories](codeartifact-concepts.md#welcome-concepts-repository "codeartifact-concepts.md#welcome-concepts-repository"), to use
CodeArtifact, you must create one. You can create a repository using the CodeArtifact console, the AWS Command Line Interface (AWS CLI), or
CloudFormation.
Each repository is associated with the AWS account that you use when you create it. You can
have multiple repositories, and they are created and grouped in [domains](codeartifact-concepts.md#welcome-concepts-domain "codeartifact-concepts.md#welcome-concepts-domain").
When you create a repository, it does not contain any packages. Repositories are polyglot, which means that a single
repository can contain packages of any supported type.

For information about CodeArtifact service limits, such as
the maximum number of allowed repositories in a single domain, see
[Quotas in AWS CodeArtifact](service-limits.md "service-limits.md"). If you hit the maximum
number of allowed repositories, you can [delete repositories](delete-repo.md "delete-repo.md") to make room for more.

A repository can have one or more CodeArtifact repositories associated with it as upstream
repositories. This allows a package manager client to access the packages contained in more
than one repository using a single URL endpoint. For more information, see
[Working with upstream repositories in CodeArtifact](repos-upstream.md "repos-upstream.md").

For more information about
managing CodeArtifact repositories with CloudFormation, see [Creating CodeArtifact resources with AWS CloudFormation](cloudformation-codeartifact.md "cloudformation-codeartifact.md").

###### Note

After you create a repository, you cannot change its name, associated AWS
account, or domain.

###### Topics

- [Create a repository (console)](#create-repo-console "#create-repo-console")
- [Create a repository (AWS CLI)](#create-repo-cli "#create-repo-cli")
- [Create a repository with an
  upstream repository](#creating-a-repository-with-an-upstream "#creating-a-repository-with-an-upstream")

## Create a repository (console)

1. Open the AWS CodeArtifact console at [https://console.aws.amazon.com/codesuite/codeartifact/home](https://console.aws.amazon.com/codesuite/codeartifact/home "https://console.aws.amazon.com/codesuite/codeartifact/home").
2. On the navigation pane, choose **Repositories**, and then
   choose **Create repository**.
3. For **Repository name**, enter a name for your repository.
4. (Optional) In **Repository description**, enter an optional description for
   your repository.
5. (Optional) In **Publish upstream repositories**, add intermediate repositories that
   connect your repositories to package authorities such as Maven Central or npmjs.com.
6. Choose **Next**.
7. In **AWS account**, choose **This AWS
   account** if you are signed in to the account that owns the domain.
   Choose **Different AWS account** if another AWS account owns
   the domain.
8. In **Domain**, choose the domain that the repository will be
   created in.

If there are no domains in the account, you must create one. Enter the name for the new domain in **Domain name**.

Expand **Additional configuration**.

You must use an AWS KMS key (KMS key) to encrypt all
assets in your domain. You can use an AWS managed key or a KMS key that you manage:

###### Important

CodeArtifact only supports [symmetric KMS keys](../../../kms/latest/developerguide/concepts.md#symmetric-cmks "../../../kms/latest/developerguide/concepts.md#symmetric-cmks").
You cannot use an [asymmetric KMS key](../../../kms/latest/developerguide/symmetric-asymmetric.md#asymmetric-cmks "../../../kms/latest/developerguide/symmetric-asymmetric.md#asymmetric-cmks")
to encrypt your CodeArtifact domains. For help determining whether a KMS key is symmetric or asymmetric, see [Identifying symmetric and asymmetric KMS keys](../../../kms/latest/developerguide/find-symm-asymm.md "../../../kms/latest/developerguide/find-symm-asymm.md").

    * Choose **AWS managed key** if you want to use the default
     AWS managed key.
    * Choose **Customer managed key** if you want to use a
     KMS key that you manage. To use a KMS key that you manage, in
     **Customer managed key ARN**, search for and choose the KMS key.

For more information, see [AWS managed keys](../../../kms/latest/developerguide/concepts.md#aws-managed-cmk "../../../kms/latest/developerguide/concepts.md#aws-managed-cmk") and [customer managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the _AWS Key Management Service Developer Guide_. 9. Choose **Next**. 10. In **Review and create**, review what CodeArtifact is creating for you.

    * **Package flow** shows how your domain and repositories
     are connected.
    * **Step 1: Create repository** shows details about the repository and
     optional upstream repositories that will be created.
    * **Step 2: Select domain** shows details about `my_domain`.

When you're ready, choose **Create repository**.

## Create a repository (AWS CLI)

Use the `create-repository` command to create a repository in your
domain.

```
aws codeartifact create-repository --domain `my_domain` --domain-owner `111122223333` --repository `my_repo` --description "`My new repository`"
```

Example output:

```
{
    "repository": {
        "name": "`my_repo`",
        "administratorAccount": "`123456789012`",
        "domainName": "`my_domain`",
        "domainOwner": "`111122223333`",
        "arn": "arn:aws:codeartifact:`region-id`:`111122223333`:repository/`my_domain`/`my_repo`",
        "description": "`My new repository`",
        "upstreams": "[]",
        "externalConnections"" "[]"
    }
}
```

A new repository doesn't contain any packages. Each repository is associated with the
AWS account that you're authenticated to when the repository is created.

### Create a repository with tags

To create a repository with tags, add the `--tags` parameter to your `create-domain` command.

```
aws codeartifact create-repository --domain `my_domain` --domain-owner `111122223333` --repository `my_repo` --tags `key=k1,value=v1 key=k2,value=v2`
```

## Create a repository with an

upstream repository

You can specify one or more upstream repositories when you create a repository.

```
aws codeartifact create-repository --domain `my_domain` --domain-owner `111122223333` --repository `my_repo` \
  --upstreams repositoryName=`my-upstream-repo` --repository-description `"My new repository"`
```

Example output:

```
{
    "repository": {
        "name": "`my_repo`",
        "administratorAccount": "`123456789012`",
        "domainName": "`my_domain`",
        "domainOwner": "`111122223333`",
        "arn": "arn:aws:codeartifact:`region-id`:`111122223333`:repository/`my_domain`/`my_repo`",
        "description": "`My new repository`",
        "upstreams": [
            {
                "repositoryName": "`my-upstream-repo`"
            }
        ],
        "externalConnections"" "[]"
    }
}
```

###### Note

To create a repository with an upstream, you must have permission for the
`AssociateWithDownstreamRepository` action on the upstream
repository.

To add an upstream to a repository after it's been created, see [Add or remove upstream repositories
(console)](repo-upstream-add.md#repo-upstream-add-console "repo-upstream-add.md#repo-upstream-add-console") and
[Add or remove upstream repositories
(AWS CLI)](repo-upstream-add.md#repo-upstream-add-cli "repo-upstream-add.md#repo-upstream-add-cli").
