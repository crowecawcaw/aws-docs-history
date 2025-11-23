# Pushing a multi-architecture

image to an Amazon ECR private repository

You can push multi-architecture images to an Amazon ECR repository by creating and
pushing Docker manifest lists. A _manifest list_ is a list of
images that is created by specifying one or more image names. In most cases, the
manifest list is created from images that serve the same function but are for
different operating systems or architectures. The manifest list isn't required. For
more information, see [docker
manifest](https://docs.docker.com/engine/reference/commandline/manifest/ "https://docs.docker.com/engine/reference/commandline/manifest/").

A manifest list can be pulled or referenced in an Amazon ECS task definition or Amazon EKS
pod spec like other Amazon ECR images.

**Prerequisites**

- In your Docker CLI, turn on experimental features. For information about
  experimental features, see [Experimental
  features](https://docs.docker.com/engine/reference/commandline/cli/#experimental-features "https://docs.docker.com/engine/reference/commandline/cli/#experimental-features") in the Docker documentation.
- The Amazon ECR repository must exist before you push the image. For more
  information, see [Creating an Amazon ECR private repository to store
  images](repository-create.md "repository-create.md").
- Images must be pushed to your repository before you create the Docker
  manifest. For information about how to push an image, see [Pushing a Docker image to an Amazon ECR private
  repository](docker-push-ecr-image.md "docker-push-ecr-image.md").

###### To push a multi-architecture Docker image to an Amazon ECR repository

1. Authenticate your Docker client to the Amazon ECR registry to which you intend
   to push your image. Authentication tokens must be obtained for each registry
   used, and the tokens are valid for 12 hours. For more information, see [Private registry authentication in Amazon ECR](registry_auth.md "registry_auth.md").

To authenticate Docker to an Amazon ECR registry, run the **aws ecr
get-login-password** command. When passing the authentication
token to the **docker login** command, use the value
`AWS` for the username and specify the Amazon ECR registry URI you
want to authenticate to. If authenticating to multiple registries, you must
repeat the command for each registry.

###### Important

If you receive an error, install or upgrade to the latest version of
the AWS CLI. For more information, see [Installing the
AWS Command Line Interface](../../../cli/latest/userguide/install-cliv2.md "../../../cli/latest/userguide/install-cliv2.md") in the _AWS Command Line Interface User Guide_.

```
`aws ecr get-login-password --region `<region>` | docker login --username AWS --password-stdin `<`aws_account_id`>`.dkr.ecr.`<region>`.amazonaws.com`
```

2. List the images in your repository, confirming the image tags.

```
`aws ecr describe-images --repository-name `my-repository``
```

3. Create the Docker manifest list. The `manifest create` command
   verifies that the referenced images are already in your repository and creates the
   manifest locally.

```
`docker manifest create ``aws_account_id`.dkr.ecr.`region`.amazonaws.com`/`my-repository` ``aws_account_id`.dkr.ecr.`region`.amazonaws.com`/`my-repository`:`image_one_tag` ``aws_account_id`.dkr.ecr.`region`.amazonaws.com`/`my-repository`:`image_two``
```

4. (Optional) Inspect the Docker manifest list. This enables you to confirm
   the size and digest for each image manifest referenced in the manifest
   list.

```
`docker manifest inspect ``aws_account_id`.dkr.ecr.`region`.amazonaws.com`/`my-repository``
```

5. Push the Docker manifest list to your Amazon ECR repository.

```
`docker manifest push ``aws_account_id`.dkr.ecr.`region`.amazonaws.com`/`my-repository``
```
