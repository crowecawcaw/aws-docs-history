# Amazon ECR public registries

Amazon ECR public registries host your container images in a highly available and scalable
architecture, allowing you to deploy containers reliably for your applications. You can use
your public registry to manage public image repositories consisting of Docker and Open
Container Initiative (OCI) images. Each AWS account is provided with a default public and
private Amazon ECR registry. For information about private registries, see [Amazon ECR
registries](../userguide/Registries.md "../userguide/Registries.md") in the _Amazon Elastic Container Registry User Guide._

###### Topics

- [Public registry concepts](#public-registry-concepts "#public-registry-concepts")
- [Registry authentication in Amazon ECR public](public-registry-auth.md "public-registry-auth.md")
- [Required IAM permissions for Amazon ECR public registries](public-registry-settings-iam.md "public-registry-settings-iam.md")
- [Updating registry settings in Amazon ECR public](public-registry-settings.md "public-registry-settings.md")

## Public registry concepts

The following concepts apply to your public registry.

- A default alias is assigned to your public registry after creating your first
  public repository. A custom alias can be requested in the public registry
  settings in the Amazon ECR console.
- Each repository you create in your public registry
  is available publicly in the Amazon ECR Public Gallery.
  The Amazon ECR Public Gallery is available at `https://gallery.ecr.aws`.
  The URL to access a repository in your public registry on the
  Amazon ECR Public Gallery is
  `https://gallery.ecr.aws/`registry_alias`/`repository_name``.

###### Note

Any active alias for your public registry can be used. This includes both
the default alias and custom alias for your public registry.

- The URI to use when pulling images from a repository in your public registry
  is
  `public.ecr.aws/`registry_alias`/`repository_name`:`image_tag``.

###### Note

Any active alias for your public registry can be used. This includes both
the default alias and custom alias for your public registry.

- By default, your account has read and write access to the repositories in your
  private registry. However, users require permissions to make calls to the Amazon ECR
  APIs and to push images to your repositories. Anyone will be able to pull images
  from your public repository from the
  Amazon ECR Public Gallery.

###### Important

If you've previously authenticated to Amazon ECR Public, if your auth token has
expired you may receive an authentication error when attempting to do
unauthenticated docker pulls from Amazon ECR Public. To resolve this issue, it
may be necessary to run `docker logout public.ecr.aws` to avoid
the error. This will result in an unauthenticated pull. For more
information, see [Authentication issues](public-troubleshooting.md#public-troubleshooting-authentication "public-troubleshooting.md#public-troubleshooting-authentication").

- You must authenticate your Docker client to your public registry so that you
  can use the **docker push** command to push images to the
  repositories in your public registry. For more information, see [Registry authentication in Amazon ECR public](public-registry-auth.md "public-registry-auth.md").
- Repositories can be controlled with both IAM user access policies and
  repository policies. For more information about repository policies, see [Public repository policies in Amazon ECR Public](public-repository-policies.md "public-repository-policies.md").
