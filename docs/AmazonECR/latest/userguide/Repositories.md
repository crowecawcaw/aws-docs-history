# Amazon ECR private repositories

An Amazon ECR private repository contains your Docker images, Open Container Initiative (OCI)
images, and OCI compatible artifacts. You can create, monitor, and delete image repositories
and set permissions that control who can access them by using Amazon ECR API operations or the
**Repositories** section of the Amazon ECR console. Amazon ECR also integrates
with the Docker CLI, so that you can push and pull images from your development environments
to your repositories.

###### Topics

- [Private repository concepts](#repository-concepts "#repository-concepts")
- [Creating an Amazon ECR private repository to store
  images](repository-create.md "repository-create.md")
- [Viewing the contents and details of a private
  repository in Amazon ECR](repository-info.md "repository-info.md")
- [Deleting a private repository in Amazon ECR](repository-delete.md "repository-delete.md")
- [Private repository policies in Amazon ECR](repository-policies.md "repository-policies.md")
- [Tagging a private repository in Amazon ECR](ecr-using-tags.md "ecr-using-tags.md")

## Private repository concepts

- By default, your account has read and write access to the repositories in your
  default registry
  (``aws_account_id`.dkr.ecr.`region`.amazonaws.com`).
  However, users require permissions to make calls to the Amazon ECR APIs and to push
  or pull images to and from your repositories. Amazon ECR provides several managed
  policies to control user access at varying levels. For more information, see
  [Amazon Elastic Container Registry Identity-based policy
  examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").
- Repositories can be controlled with both user access policies and individual
  repository policies. For more information, see [Private repository policies in Amazon ECR](repository-policies.md "repository-policies.md").
- Repository names can support namespaces, which you can use to group similar
  repositories. For example, if there are several teams using the same registry,
  Team A can use the `team-a` namespace, and Team B can use the
  `team-b` namespace. By doing this, each team has their own image
  called `web-app` with each image prefaced with the team namespace.
  This configuration allows these images on each team to be used simultaneously
  without interference. Team A's image is `team-a/web-app`, and Team
  B's image is `team-b/web-app`.
- Your images can be replicated to other repositories across Regions in your own
  registry and across accounts. You can do this by specifying a replication
  configuration in your registry settings. For more information, see [Private registry settings in Amazon ECR](registry-settings.md "registry-settings.md").
- When blob mounting is enabled at the registry level, repositories can share common image layers.
