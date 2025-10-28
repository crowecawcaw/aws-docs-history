# Pulling an image with a

pull through cache rule in Amazon ECR

The following examples show the command syntax to use when pulling an image
using a pull through cache rule. If you receive an error pulling an upstream
image using a pull through cache rule, see [Troubleshooting pull through cache
issues in Amazon ECR](error-pullthroughcache.md "error-pullthroughcache.md")
for the most common errors and how to resolve them.

Before you start working with your pull through cache rules, verify that you have the proper
IAM permissions. For more information, see [IAM permissions required to sync an upstream registry with an Amazon ECR private registry](pull-through-cache-iam.md "pull-through-cache-iam.md").

###### Note

The following examples use the default Amazon ECR repository namespace values
that the AWS Management Console uses. Ensure that you use the Amazon ECR private repository
URI that you've configured.

```
docker pull `aws_account_id`.dkr.ecr.`region`.amazonaws.com/`ecr-public`/`repository_name/image_name:tag`
```

```
docker pull `aws_account_id`.dkr.ecr.`region`.amazonaws.com/`kubernetes`/`repository_name/image_name:tag`
```

```
docker pull `aws_account_id`.dkr.ecr.`region`.amazonaws.com/`quay`/`repository_name/image_name:tag`
```

For Docker Hub official images:

```
docker pull `aws_account_id`.dkr.ecr.`region`.amazonaws.com/docker-hub/library/`image_name:tag`
```

###### Note

For Docker Hub official images, the `/library` prefix must be
included. For all other Docker Hub repositories, you should omit the
`/library` prefix.

For all other Docker Hub images:

```
docker pull `aws_account_id`.dkr.ecr.`region`.amazonaws.com/`docker-hub`/`repository_name/image_name:tag`
```

```
docker pull `aws_account_id`.dkr.ecr.`region`.amazonaws.com/`github`/`repository_name/image_name:tag`
```

```
docker pull `aws_account_id`.dkr.ecr.`region`.amazonaws.com/`azure`/`repository_name/image_name:tag`
```

```
docker pull `aws_account_id`.dkr.ecr.`region`.amazonaws.com/`gitlab`/`repository_name/image_name:tag`
```
