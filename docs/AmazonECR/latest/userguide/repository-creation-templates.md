# Templates to control repositories created

during a pull through cache, create on push, or replication action

Use Amazon ECR repository creation templates to define the settings for repositories created by
Amazon ECR on your behalf. The settings in a repository creation template are only applied during
repository creation and don't have any effect on existing repositories or repositories
created using any other method. Currently, repository creation templates can be used to
apply settings during repository creation for these features:

- Pull through cache
- Create on push
- Replication

## How repository creation templates

work

There are times when Amazon ECR needs to create a new private repository on your behalf.
For example:

- The first time you use a pull through cache rule to retrieve the contents of
  an upstream repository and store it in your Amazon ECR private registry.
- When you push an image to a repository that does not yet exist.
- When you want Amazon ECR to replicate a repository to another region or
  account.

When there isn't a repository creation template that matches your pull through cache
rule or replicated repository, Amazon ECR uses the default settings for the new repository.
These default settings include turning off tag immutability, using `AES-256`
encryption, and not applying any repository or lifecycle policies.

When there isn't a repository creation template that matches the target repository
for an image push, Amazon ECR will not create a repository with default settings.

Using a repository creation template gives you the ability to define the settings
Amazon ECR applies to new repositories created through the pull through cache, create on push, and replication
actions. You can define the tag immutability, encryption configuration, repository
permissions, lifecycle policy, and resource tags for the new repositories.

The following diagram shows the workflow that Amazon ECR uses when a repository creation
template is used.

![A display of how repository creation templates are applied to new repositories.](images/repository_creation_template_light.png)

The following describes each parameter in a repository creation template in
detail.

Prefix

The **Prefix** is the repository namespace prefix to
associate with the template. All repositories created using this prefix will
have the settings applied that are defined in this template. For example, a
prefix of `prod` would apply to all repositories beginning with
`prod/`. Similarly, a prefix of `prod/team` would
apply to all repositories beginning with `prod/team/`. In a
registry containing two templates, if one template has the prefix "prod" and
the other has the prefix "prod/team", the template with the prefix
"prod/team" will be applied to all repositories whose names start with
"prod/team/".

To apply a template to all repositories in your registry that don't have
an associated creation template, you can use `ROOT` as the
prefix.

###### Important

There is always an assumed `/` applied to the end of the
prefix. If you specify `ecr-public` as the prefix, Amazon ECR
treats that as `ecr-public/`. When using a pull through cache
rule, the repository prefix you specify during rule creation is what you
should specify as your repository creation template prefix as
well.

Description

This **template description** is optional and is used to
describe the purpose for the repository creation template.

Applied For

The **applied for** setting determines which Amazon ECR-created
repositories will be created with this template. The valid values are
`PULL_THROUGH_CACHE`, `CREATE_ON_PUSH`, and `REPLICATION`. For
example, the first time you use a pull through cache rule to retrieve the
contents of an upstream repository and store it in your Amazon ECR private
registry. When there isn't a repository creation template that matches your
pull through cache rule, Amazon ECR uses the default settings for the new
repository.

Repository creation role

The **repository creation role** is an IAM role ARN
that will be assumed by Amazon ECR when creating and configuring repositories via
repository creation templates. This role must be provided when using
repository tags and/or KMS in the template, otherwise the repository
creation will fail.

Image tag mutability

The **tag mutability** setting to use for repositories
created using the template. If this parameter is omitted, the default
setting of **MUTABLE** will be used which will allow image
tags to be overwritten. This is the recommended setting to use for templates
used for repositories created by pull through cache actions. This ensures
that Amazon ECR can update the cached images when the tags are the same.

If **IMMUTABLE** is specified, all image tags within the
repository will be immutable which will prevent them from being
overwritten.

Encryption configuration

###### Important

Dual-layer server-side encryption with AWS KMS (DSSE-KMS) is only available in
the AWS GovCloud (US) Regions.

The **encryption configuration** to use for repositories
created using the template.

If you use the **KMS** encryption type, the contents of
the repository will be encrypted using server-side encryption with an
AWS Key Management Service key stored in AWS KMS. When you use AWS KMS to
encrypt your data, you can either use the default AWS managed AWS KMS key
for Amazon ECR, or specify your own AWS KMS key, which you already created. You can
further choose to use Single-layer or Dual-layer encryption with AWS KMS. For
more information, see [Encryption at rest](encryption-at-rest.md "encryption-at-rest.md") . If you're using the
**KMS** encryption type and using it with cross region
replication, you may need additional permissions. For more information, see
[Creating a KMS key policy for replication](registry-permissions-create.md "registry-permissions-create.md").

If you use the **AES256** encryption type, Amazon ECR uses
server-side encryption with Amazon S3-managed encryption keys which encrypts the
images in the repository using an AES-256 encryption algorithm. For more
information, see [Protecting data
using server-side encryption with Amazon S3-managed encryption keys
(SSE-S3)](../../../AmazonS3/latest/dev/UsingServerSideEncryption.md "../../../AmazonS3/latest/dev/UsingServerSideEncryption.md") in the _Amazon Simple Storage Service User Guide_.

Repository permissions

The **repository policy** to apply to repositories
created using the template. A repository policy uses resource-based
permissions to control access to a repository. Resource-based permissions
let you specify which IAM users or roles have access to a repository and
what actions they can perform on it. By default, only the AWS account that
created the repository has access to a repository. You can apply a policy
document to grant or deny additional permissions to your repository. For
more information, see [Private repository policies in Amazon ECR](repository-policies.md "repository-policies.md").

Repository lifecycle policy

The **lifecycle policy** to use for repositories created
using the template. A lifecycle policy provides more control over the
lifecycle management of images in a private repository. A lifecycle policy
contains one or more rules, where each rule defines an action for Amazon ECR.
This provides a way to automate the cleaning up of your container images by
expiring images based on age or count. For more information, see [Automate the cleanup of images by using lifecycle
policies in Amazon ECR](LifecyclePolicies.md "LifecyclePolicies.md").

Resource tags

The **resource tags** are metadata to apply to the
repository to help you categorize and organize them. Each tag consists of a
key and an optional value, both of which you define. This permission needs
to be applied on the destination registry policy if you are using repository
creation templates with cross region replication.
