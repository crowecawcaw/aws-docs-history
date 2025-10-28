# Docker image build server sample for CodeBuild

The following sample offloads your Docker builds to a managed image build server. You can adapt this
sample to provision a dedicated and managed Docker image build server in your CodeBuild project configuration. Note
that the provisioned instance is active while builds are actively run for the project, and the instance
is stopped when builds are not running. The provisioned instance is stored for up to a month before it is recycled.
For more information, see [CodeBuild Docker Server Capability](https://aws.amazon.com/blogs/aws/accelerate-ci-cd-pipelines-with-the-new-aws-codebuild-docker-server-capability "https://aws.amazon.com/blogs/aws/accelerate-ci-cd-pipelines-with-the-new-aws-codebuild-docker-server-capability").

###### Important

Running this sample might result in charges to your AWS account. These include
possible charges for CodeBuild and for AWS resources and actions related to Amazon S3, AWS KMS,
and CloudWatch Logs. For more information, see [CodeBuild pricing](http://aws.amazon.com/codebuild/pricing "http://aws.amazon.com/codebuild/pricing"), [Amazon S3
pricing](http://aws.amazon.com/s3/pricing "http://aws.amazon.com/s3/pricing"), [AWS Key Management Service
pricing](http://aws.amazon.com/kms/pricing "http://aws.amazon.com/kms/pricing"), and [Amazon CloudWatch
pricing](http://aws.amazon.com/cloudwatch/pricing "http://aws.amazon.com/cloudwatch/pricing").

###### Topics

- [Configure a Docker server](#sample-docker-server-running "#sample-docker-server-running")

## Configure a Docker server

Use the following procedure to provision a dedicated compute environment for a CodeBuild
project that manages Docker workloads and stores Docker image layers.

###### To configure a Docker server

1. Create the files as described in the [Directory structure](#sample-docker-server-dir "#sample-docker-server-dir") and [Files](#sample-docker-server-files "#sample-docker-server-files") sections of this topic,
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
information:

    1. In the **Environment** section of the console, choose **Additional configuration**,
     navigate to **Docker server configuration**, and then select **Enable docker server for this project**.
     You can then choose the **Docker server compute type** and supply a **Registry credential**.
    2. If you use the AWS CLI to create the build project, the JSON-formatted input to
     the `create-project` command might look similar to this.
     (Replace the placeholders with your own values.)



    ```
    {
      "name": "sample-docker-custom-image-project",
      "source": {
        "type": "S3",
        "location": "codebuild-`region-ID`-`account-ID`-input-bucket/`DockerServerSample`.zip"
      },
      "artifacts": {
        "type": "NO_ARTIFACTS"
      },
      "environment": {
        "type": "LINUX_CONTAINER",
        "image": "aws/codebuild/amazonlinux-x86_64-standard:5.0",
        "computeType": "BUILD_GENERAL1_LARGE",
        "dockerServer": [
             {
                "computeType": "BUILD_GENERAL1_LARGE",
                "securityGroupIds": [ "`security-groups-ID`" ]
             }
          ]
      },
      "serviceRole": "arn:aws:iam::`account-ID`:role/`role-name`"
    }
    ```

    ###### Note

    Security groups configured for Docker servers should allow ingress network traffic from the VPC configured in the project. They should allow ingress on port 9876.

3. To see the build results, look in the build's log for the string `Hello,
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
  build:
    commands:
      - docker buildx build .
      - docker run helloworld echo "Hello, World!"
```

`Dockerfile` (in `(root directory
 name)`)

```
FROM public.ecr.aws/amazonlinux/amazonlinux:latest

RUN echo "Hello World"
```
