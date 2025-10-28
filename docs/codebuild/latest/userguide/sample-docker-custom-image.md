# Docker in custom image sample for CodeBuild

The following sample builds and runs a Docker image by using AWS CodeBuild and a custom Docker
build image (`docker:dind` in Docker Hub).

To learn how to build a Docker image by using a build image provided by CodeBuild with Docker
support instead, see our ['Publish Docker image to Amazon ECR'
sample](sample-docker.md "sample-docker.md").

###### Important

Running this sample might result in charges to your AWS account. These include
possible charges for CodeBuild and for AWS resources and actions related to Amazon S3, AWS KMS,
and CloudWatch Logs. For more information, see [CodeBuild pricing](http://aws.amazon.com/codebuild/pricing "http://aws.amazon.com/codebuild/pricing"), [Amazon S3
pricing](http://aws.amazon.com/s3/pricing "http://aws.amazon.com/s3/pricing"), [AWS Key Management Service
pricing](http://aws.amazon.com/kms/pricing "http://aws.amazon.com/kms/pricing"), and [Amazon CloudWatch
pricing](http://aws.amazon.com/cloudwatch/pricing "http://aws.amazon.com/cloudwatch/pricing").

###### Topics

- [Run the Docker in custom image
  sample](#sample-docker-custom-image-running "#sample-docker-custom-image-running")

## Run the Docker in custom image

sample

Use the following procedure to run the Docker in custom image sample. For more
information about this sample, see [Docker in custom image sample for CodeBuild](sample-docker-custom-image.md "sample-docker-custom-image.md").

###### To run the Docker in custom image sample

1. Create the files as described in the [Directory structure](#sample-docker-custom-image-dir "#sample-docker-custom-image-dir") and [Files](#sample-docker-custom-image-files "#sample-docker-custom-image-files") sections of this topic,
   and then upload them to an S3 input bucket or an AWS CodeCommit, GitHub, or Bitbucket
   repository.

###### Important

Do not upload `(root directory
 name)`, just the files inside of
`(root directory
 name)`.

If you are using an S3 input bucket, be sure to create a ZIP file that
contains the files, and then upload it to the input bucket. Do not add
`(root directory
 name)` to the ZIP file, just the files inside of
`(root directory
 name)`. 2. Create a build project, run the build, and view related build
information.

If you use the AWS CLI to create the build project, the JSON-formatted input to
the `create-project` command might look similar to this.
(Replace the placeholders with your own values.)

```
{
  "name": "sample-docker-custom-image-project",
  "source": {
    "type": "S3",
    "location": "codebuild-`region-ID`-`account-ID`-input-bucket/`DockerCustomImageSample`.zip"
  },
  "artifacts": {
    "type": "NO_ARTIFACTS"
  },
  "environment": {
    "type": "LINUX_CONTAINER",
    "image": "docker:dind",
    "computeType": "BUILD_GENERAL1_SMALL",
    "privilegedMode": false
  },
  "serviceRole": "arn:aws:iam::`account-ID`:role/`role-name`",
  "encryptionKey": "arn:aws:kms:`region-ID`:`account-ID`:key/`key-ID`"
}
```

###### Note

By default, Docker daemon is enabled for non-VPC builds. If you would like to use Docker
containers for VPC builds, see [Runtime
Privilege and Linux Capabilities](https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities "https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities") on the Docker Docs website and enable privileged mode. Also, Windows does not support privileged mode. 3. To see the build results, look in the build's log for the string `Hello,
 World!`. For more information, see [View build details](view-build-details.md "view-build-details.md").

### Directory structure

This sample assumes this directory structure.

```
`(root directory name)`
├── buildspec.yml
└── Dockerfile
```

### Files

The base image of the operating system used in this sample is Ubuntu. The sample
uses these files.

`buildspec.yml` (in `(root directory
 name)`)

```
version: 0.2

phases:
  pre_build:
    commands:
      - docker build -t helloworld .
  build:
    commands:
      - docker images
      - docker run helloworld echo "Hello, World!"
```

`Dockerfile` (in `(root directory
 name)`)

```
FROM maven:3.3.9-jdk-8

RUN echo "Hello World"
```
