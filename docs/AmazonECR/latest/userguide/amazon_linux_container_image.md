# Pulling the Amazon Linux container image

The Amazon Linux container image is built from the same software components that are included
in the Amazon Linux AMI. The Amazon Linux container image is available for use in any environment as a
base image for Docker workloads. If you use the Amazon Linux AMI for applications in Amazon EC2, you
can containerize your applications with the Amazon Linux container image.

You can use the Amazon Linux container image in your local development environment and then
push your application to AWS using Amazon ECS. For more information, see [Using Amazon ECR images with Amazon ECS](ECR_on_ECS.md "ECR_on_ECS.md").

The Amazon Linux container image is available on Amazon ECR Public and
on [Docker Hub](https://hub.docker.com/_/amazonlinux/ "https://hub.docker.com/_/amazonlinux/"). For
support for the Amazon Linux container image, go to the [AWS developer forums](https://forums.aws.amazon.com/forum.jspa?forumID=228 "https://forums.aws.amazon.com/forum.jspa?forumID=228").

###### To pull the Amazon Linux container image from Amazon ECR Public

1. Authenticate your Docker client to the Amazon Linux Public registry. Authentication
   tokens are valid for 12 hours. For more information, see [Private registry authentication in Amazon ECR](registry_auth.md "registry_auth.md").

###### Note

The **ecr-public** commands are available in the AWS CLI
starting with version `1.18.1.187`, however we recommend using
the latest version of the AWS CLI. For more information, see [Installing the AWS Command Line Interface](../../../cli/latest/userguide/install-cliv2.md "../../../cli/latest/userguide/install-cliv2.md") in the
_AWS Command Line Interface User Guide_.

```
`aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws`
```

The output is as follows:

```
Login succeeded
```

2. Pull the Amazon Linux container image using the **docker pull**
   command. To view the Amazon Linux container image on the Amazon ECR Public Gallery, see
   [Amazon ECR Public Gallery - amazonlinux](https://gallery.ecr.aws/amazonlinux/amazonlinux "https://gallery.ecr.aws/amazonlinux/amazonlinux").

```
`docker pull public.ecr.aws/amazonlinux/amazonlinux:latest`
```

3. (Optional) Run the container locally.

```
`docker run -it public.ecr.aws/amazonlinux/amazonlinux /bin/bash`
```

###### To pull the Amazon Linux container image from Docker Hub

1. Pull the Amazon Linux container image using the **docker pull**
   command.

```
`docker pull amazonlinux`
```

2. (Optional) Run the container locally.

```
`docker run -it amazonlinux:latest /bin/bash`
```
