# Pushing an image to an Amazon ECR private repository

You can push your Docker images, manifest lists, and Open Container Initiative (OCI)
images and compatible artifacts to your private repositories.

Amazon ECR also provides a way to replicate your images to other repositories. By
specifying a replication configuration in your private registry settings, you can
replicate across Regions in your own registry and across different accounts. For more
information, see [Private registry settings in Amazon ECR](registry-settings.md "registry-settings.md").

###### Note

If you push an image that is currently archived, that image will be automatically
restored and removed from the archive. For more information about archiving and
restoring images, see [Archiving an image in Amazon ECR](archive_restore_image.md "archive_restore_image.md").

###### Topics

- [IAM permissions for pushing an image to an Amazon ECR
  private repository](image-push-iam.md "image-push-iam.md")
- [Pushing a Docker image to an Amazon ECR private
  repository](docker-push-ecr-image.md "docker-push-ecr-image.md")
- [Pushing a multi-architecture
  image to an Amazon ECR private repository](docker-push-multi-architecture-image.md "docker-push-multi-architecture-image.md")
- [Pushing a Helm chart to an Amazon ECR private
  repository](push-oci-artifact.md "push-oci-artifact.md")
