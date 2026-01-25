# Pushing an image to an Amazon ECR private repository

You can push your Docker images, manifest lists, and Open Container Initiative (OCI)
images and compatible artifacts to your private repositories.

Amazon ECR provides a way to replicate your images to other repositories. By
specifying a replication configuration in your private registry settings, you can
replicate across Regions in your own registry and across different accounts. For more
information, see [Private registry settings in Amazon ECR](registry-settings.md "registry-settings.md").

###### Note

If you push an image that is currently archived, that image will be automatically
restored and removed from the archive. For more information about archiving and
restoring images, see [Archiving an image in Amazon ECR](archive_restore_image.md "archive_restore_image.md").

When registry blob mounting is enabled and mounting parameters are included, Amazon ECR automatically checks for existing layers in your registry during push operations.
If a layer already exists in another repository within the same registry, Amazon ECR will mount the existing
layer instead of uploading a duplicate. For more information, see [Blob mounting in Amazon ECR](blob-mounting.md "blob-mounting.md").

###### Topics

- [IAM permissions for pushing an image to an Amazon ECR
  private repository](image-push-iam.md "image-push-iam.md")
- [Pushing a Docker image to an Amazon ECR private
  repository](docker-push-ecr-image.md "docker-push-ecr-image.md")
- [Pushing a multi-architecture
  image to an Amazon ECR private repository](docker-push-multi-architecture-image.md "docker-push-multi-architecture-image.md")
- [Pushing a Helm chart to an Amazon ECR private
  repository](push-oci-artifact.md "push-oci-artifact.md")
