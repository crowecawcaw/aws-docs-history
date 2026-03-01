# Troubleshooting pull through cache issues in Amazon ECR

When pulling an upstream image using a pull through cache rule, the following are the
most common errors you may receive.

**Repository does not exist**

An error indicating that the repository doesn't exist is most often caused
by either the repository not existing in your Amazon ECR private registry or the
`ecr:CreateRepository` permission not being granted to the
IAM principal pulling the upstream image. To resolve this error, you
should verify that the repository URI in your pull command is correct, the
required IAM permissions are granted to the IAM principal pulling the
upstream image, or that the repository for the upstream image to be pushed
to is created in your Amazon ECR private registry before doing the upstream image
pull. For more information about the required IAM permissions, see [IAM permissions required to sync an upstream registry with an Amazon ECR private registry](pull-through-cache-iam.md "pull-through-cache-iam.md")

The following is an example of this error.

```
Error response from daemon: repository 111122223333.dkr.ecr.us-east-1.amazonaws.com/ecr-public/amazonlinux/amazonlinux not found: name unknown: The repository with name 'ecr-public/amazonlinux/amazonlinux' does not exist in the registry with id '111122223333'
```

**Requested image not found**

An error indicating that the image can't be found is most often caused by
either the image not existing in the upstream registry or the
`ecr:BatchImportUpstreamImage` permission not being granted
to the IAM principal pulling the upstream image but the repository already
being created in your Amazon ECR private registry. To resolve this error, you
should verify the upstream image and image tag name is correct and that it
exists and the required IAM permissions are granted to the IAM principal
pulling the upstream image. For more information about the required IAM
permissions, see [IAM permissions required to sync an upstream registry with an Amazon ECR private registry](pull-through-cache-iam.md "pull-through-cache-iam.md").

The following is an example of this error.

```
Error response from daemon: manifest for 111122223333.dkr.ecr.us-east-1.amazonaws.com/ecr-public/amazonlinux/amazonlinux:latest not found: manifest unknown: Requested image not found
```

**403 Forbidden when pulling from a Docker Hub
repository**

When pulling from a Docker Hub repository that is tagged as a
**Docker Official Image**, you must include the
`/library/` in the URI you use. For example,
``aws_account_id`.dkr.ecr.`region`.amazonaws.com/docker-hub**/library/**`image_name:tag``.
If you omit the `/library/` for Docker Hub Official images, a
`403 Forbidden` error will be returned when you attempt to
pull the image using a pull through cache rule. For more information, see
[Pulling an image with a pull through cache rule in Amazon ECR](pull-through-cache-working-pulling.md "pull-through-cache-working-pulling.md").

The following is an example of this error.

```
Error response from daemon: failed to resolve reference "111122223333.dkr.ecr.us-west-2.amazonaws.com/docker-hub/amazonlinux:2023": pulling from host 111122223333.dkr.ecr.us-west-2.amazonaws.com failed with status code [manifests 2023]: 403 Forbidden
```
