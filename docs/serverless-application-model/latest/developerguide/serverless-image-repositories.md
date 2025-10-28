# Image repositories for AWS SAM

AWS SAM simplifies continuous integration and continuous delivery (CI/CD) tasks for
serverless applications with the help of build container images. The images that AWS SAM provides
include the AWS SAM command line interface (CLI) and build tools for a number of supported
AWS Lambda runtimes. This make it easier to build and package serverless applications using the
AWS SAM CLI. You can use these images with CI/CD systems to automate the building and deployment
of AWS SAM applications. For examples, see [Deploy with CI/CD systems and pipelines](deploying-options.md#serverless-deploying-ci-cd "deploying-options.md#serverless-deploying-ci-cd").

AWS SAM build container image URIs are tagged with the version of the AWS SAM CLI included in
that image. If you specify the untagged URI, then the latest version is used. For example,
`public.ecr.aws/sam/build-nodejs20.x` uses the latest image. However,
`public.ecr.aws/sam/build-nodejs20.x:1.24.1` uses the the image containing AWS SAM
CLI version 1.24.1.

Starting with version 1.33.0 of the AWS SAM CLI, both `x86_64` and
`arm64` container images are available for supported runtimes. For more
information, see [Lambda
runtimes](../../../lambda/latest/dg/lambda-runtimes.md "../../../lambda/latest/dg/lambda-runtimes.md") in the _AWS Lambda Developer Guide_.

###### Note

Prior to version 1.22.0 of the AWS SAM CLI, DockerHub was the default repository that the
AWS SAM CLI pulled the container image from. Starting with version 1.22.0, the default
repository changed to Amazon Elastic Container Registry Public (Amazon ECR Public). To pull a container image from a
repository other than the current default, you can use the **[sam build](sam-cli-command-reference-sam-build.md "sam-cli-command-reference-sam-build.md")** command with the
**--build-image** option. The examples at the end of this topic show how to
build applications using DockerHub repository images.

## Image repository URIs

The following table lists the URIs of [Amazon ECR Public](../../../AmazonECR/latest/public/what-is-ecr.md "../../../AmazonECR/latest/public/what-is-ecr.md") build container images
that you can use to build and package serverless applications with AWS SAM.

###### Note

Amazon ECR Public replaced DockerHub starting with the AWS SAM CLI version 1.22.0. If you are using
an earlier version of the AWS SAM CLI, we recommend that you upgrade.

| Runtime                 | Amazon ECR Public                                                                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Custom runtime (AL2023) | [public.ecr.aws/sam/build-provided.al2023](https://gallery.ecr.aws/sam/build-provided.al2023 "https://gallery.ecr.aws/sam/build-provided.al2023") |
| Custom runtime (AL2)    | [public.ecr.aws/sam/build-provided.al2](https://gallery.ecr.aws/sam/build-provided.al2 "https://gallery.ecr.aws/sam/build-provided.al2")          |
| Custom runtime          | [public.ecr.aws/sam/build-provided](https://gallery.ecr.aws/sam/build-provided "https://gallery.ecr.aws/sam/build-provided")                      |
| Java 21                 | [public.ecr.aws/sam/build-java21](https://gallery.ecr.aws/sam/build-java21 "https://gallery.ecr.aws/sam/build-java21")                            |
| Java 17                 | [public.ecr.aws/sam/build-java17](https://gallery.ecr.aws/sam/build-java17 "https://gallery.ecr.aws/sam/build-java17")                            |
| Java 11                 | [public.ecr.aws/sam/build-java11](https://gallery.ecr.aws/sam/build-java11 "https://gallery.ecr.aws/sam/build-java11")                            |
| Java 8                  | [public.ecr.aws/sam/build-java8](https://gallery.ecr.aws/sam/build-java8 "https://gallery.ecr.aws/sam/build-java8")                               |
| .NET 9                  | [public.ecr.aws/sam/build-dotnet9](https://gallery.ecr.aws/sam/build-dotnet9 "https://gallery.ecr.aws/sam/build-dotnet9")                         |
| .NET 8                  | [public.ecr.aws/sam/build-dotnet8](https://gallery.ecr.aws/sam/build-dotnet8 "https://gallery.ecr.aws/sam/build-dotnet8")                         |
| .NET 7                  | [public.ecr.aws/sam/build-dotnet7](https://gallery.ecr.aws/sam/build-dotnet7 "https://gallery.ecr.aws/sam/build-dotnet7")                         |
| .NET 6                  | [public.ecr.aws/sam/build-dotnet6](https://gallery.ecr.aws/sam/build-dotnet6 "https://gallery.ecr.aws/sam/build-dotnet6")                         |
| Node.js 22              | [public.ecr.aws/sam/build-nodejs22.x](https://gallery.ecr.aws/sam/build-nodejs22.x "https://gallery.ecr.aws/sam/build-nodejs22.x")                |
| Node.js 20              | [public.ecr.aws/sam/build-nodejs20.x](https://gallery.ecr.aws/sam/build-nodejs20.x "https://gallery.ecr.aws/sam/build-nodejs20.x")                |
| Node.js 18              | [public.ecr.aws/sam/build-nodejs18.x](https://gallery.ecr.aws/sam/build-nodejs18.x "https://gallery.ecr.aws/sam/build-nodejs18.x")                |
| Node.js 16              | [public.ecr.aws/sam/build-nodejs16.x](https://gallery.ecr.aws/sam/build-nodejs16.x "https://gallery.ecr.aws/sam/build-nodejs16.x")                |
| Python 3.13             | [public.ecr.aws/sam/build-python3.13](https://gallery.ecr.aws/sam/build-python3.13 "https://gallery.ecr.aws/sam/build-python3.13")                |
| Python 3.12             | [public.ecr.aws/sam/build-python3.12](https://gallery.ecr.aws/sam/build-python3.12 "https://gallery.ecr.aws/sam/build-python3.12")                |
| Python 3.11             | [public.ecr.aws/sam/build-python3.11](https://gallery.ecr.aws/sam/build-python3.11 "https://gallery.ecr.aws/sam/build-python3.11")                |
| Python 3.10             | [public.ecr.aws/sam/build-python3.10](https://gallery.ecr.aws/sam/build-python3.10 "https://gallery.ecr.aws/sam/build-python3.10")                |
| Python 3.9              | [public.ecr.aws/sam/build-python3.9](https://gallery.ecr.aws/sam/build-python3.9 "https://gallery.ecr.aws/sam/build-python3.9")                   |
| Python 3.8              | [public.ecr.aws/sam/build-python3.8](https://gallery.ecr.aws/sam/build-python3.8 "https://gallery.ecr.aws/sam/build-python3.8")                   |
| Ruby 3.4                | [public.ecr.aws/sam/build-ruby3.4](https://gallery.ecr.aws/sam/build-ruby3.4 "https://gallery.ecr.aws/sam/build-ruby3.4")                         |
| Ruby 3.3                | [public.ecr.aws/sam/build-ruby3.3](https://gallery.ecr.aws/sam/build-ruby3.3 "https://gallery.ecr.aws/sam/build-ruby3.3")                         |
| Ruby 3.2                | [public.ecr.aws/sam/build-ruby3.2](https://gallery.ecr.aws/sam/build-ruby3.2 "https://gallery.ecr.aws/sam/build-ruby3.2")                         | ## Examples The following two example commands build applications using container images from the image repository: **Build a Node.js 22 application using a container image pulled from Amazon ECR**: ``` `$` `sam build --use-container --build-image `public.ecr.aws/sam/build-nodejs22.x`` ``` **Build a function resource using the Python 3.13 container image pulled from Amazon ECR**: ``` `$` `sam build --use-container --build-image `Function1=public.ecr.aws/sam/build-python3.13`` ``` |
