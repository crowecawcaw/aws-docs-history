# Amazon ECR public repositories

Amazon Elastic Container Registry provides API operations to create, monitor, and delete public image repositories
and set permissions that control who can push images to them. You can perform the same
actions in the **Repositories** section of the Amazon ECR console. Amazon ECR
integrates with the Docker CLI to push images from your development environments to your
public repositories.

A public repository is open to pull images from and is visible on the
Amazon ECR Public Gallery. When you create a public repository, you specify catalog data that
helps users find and use your images. For more information about the Amazon ECR Public Gallery,
see [Amazon ECR Public Gallery](public-gallery.md "public-gallery.md").

###### Topics

- [Public repository concepts](#public-repository-concepts "#public-repository-concepts")
- [Creating an Amazon ECR public repository to store
  images](public-repository-create.md "public-repository-create.md")
- [Editing an Amazon ECR public repository](public-repository-edit.md "public-repository-edit.md")
- [Specifying the repository catalog data
  in Amazon ECR public](public-repository-catalog-data.md "public-repository-catalog-data.md")
- [Viewing the contents and details of a
  repository in Amazon ECR public](public-repository-info.md "public-repository-info.md")
- [Deleting a public repository policy statement
  Amazon ECR public](public-repository-delete.md "public-repository-delete.md")
- [Public repository policies in Amazon ECR Public](public-repository-policies.md "public-repository-policies.md")
- [Tag an Amazon ECR Public repository](ecr-public-using-tags.md "ecr-public-using-tags.md")

## Public repository concepts

- The public repositories that you create with images appear publicly on the
  Amazon ECR Public Gallery. Visit the Amazon ECR Public Gallery at [https://gallery.ecr.aws](https://gallery.ecr.aws "https://gallery.ecr.aws"). For more
  information, see [Amazon ECR Public Gallery](public-gallery.md "public-gallery.md").
- By default, your account has read and write access to the repositories in your
  public registry. However, users require permissions to make calls to the Amazon ECR
  APIs and to push images to your repositories.
- Public repositories can be controlled with both IAM user access policies and
  repository policies. For more information, see [Public repository policies in Amazon ECR Public](public-repository-policies.md "public-repository-policies.md").
