# Private images in Amazon ECR

Amazon ECR stores Docker images, Open Container Initiative (OCI) images, and OCI compatible
artifacts in private repositories. You can use the Docker CLI, or your preferred client, to
push and pull images to and from your repositories.

With Amazon ECR support for OCI v1.1, you can store and manage reference artifacts that are
defined by the OCI [Referrers API](https://github.com/opencontainers/distribution-spec/blob/main/spec.md#enabling-the-referrers-api "https://github.com/opencontainers/distribution-spec/blob/main/spec.md#enabling-the-referrers-api"). Artifacts include signatures, Software Bill of Materials
(SBoMs), Helm charts, scan results, and attestations. A set of artifacts for a container
image is transferred with that container and stored as a separate image that counts as an
image consumed for your repository.

The [Signing an image stored in an Amazon ECR private
repository](image-signing.md "image-signing.md") and [Deleting signatures and other artifacts from an
Amazon ECR private repository](image-artifact-delete.md "image-artifact-delete.md") pages provide
examples of how to use signature-related artifacts. For more information on signing
container images, see [Signing container
images](../../../signer/latest/developerguide/container-workflow.md "../../../signer/latest/developerguide/container-workflow.md") in the _AWS Signer Developer Guide_.

###### Topics

- [Pushing an image to an Amazon ECR private repository](image-push.md "image-push.md")
- [Signing an image stored in an Amazon ECR private
  repository](image-signing.md "image-signing.md")
- [Deleting signatures and other artifacts from an
  Amazon ECR private repository](image-artifact-delete.md "image-artifact-delete.md")
- [Viewing image details in Amazon ECR](image-info.md "image-info.md")
- [Pulling an image to your local environment from
  an Amazon ECR private repository](docker-pull-ecr-image.md "docker-pull-ecr-image.md")
- [Pulling the Amazon Linux container image](amazon_linux_container_image.md "amazon_linux_container_image.md")
- [Deleting an image in Amazon ECR](delete_image.md "delete_image.md")
- [Retagging an image in Amazon ECR](image-retag.md "image-retag.md")
- [Preventing image tags from being overwritten in
  Amazon ECR](image-tag-mutability.md "image-tag-mutability.md")
- [Container image manifest format support in
  Amazon ECR](image-manifest-formats.md "image-manifest-formats.md")
- [Using Amazon ECR images with Amazon ECS](ECR_on_ECS.md "ECR_on_ECS.md")
- [Using Amazon ECR Images with Amazon EKS](ECR_on_EKS.md "ECR_on_EKS.md")
