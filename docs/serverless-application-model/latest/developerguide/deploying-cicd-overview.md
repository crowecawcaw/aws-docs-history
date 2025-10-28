# Using CI/CD systems and pipelines to deploy with AWS SAM

AWS SAM helps organizations create pipelines for their preferred CI/CD systems, so that they
can realize the benefits of CI/CD with minimal effort, such as accelerating deployment
frequency, shortening lead time for changes, and reducing deployment errors.

AWS SAM simplifies CI/CD tasks for serverless applications with the help of build container
images. The images that AWS SAM provides include the AWS SAM CLI and build tools for a number of
supported AWS Lambda runtimes. This makes it easier to build and package serverless
applications using the AWS SAM CLI. These images also alleviate the need for teams to create and
manage their own images for CI/CD systems. For more information about AWS SAM build container
images, see [Image repositories for AWS SAM](serverless-image-repositories.md "serverless-image-repositories.md").

Multiple CI/CD systems support AWS SAM build container images. Which CI/CD system you should
use depends on several factors. These include whether your application uses a single runtime
or multiple runtimes, or whether you want to build your application within a container image
or directly on a host machine, either a virtual machine (VM) or bare metal host.

AWS SAM also provides a set of default pipeline templates for multiple CI/CD systems that
encapsulate AWS's deployment best practices. These default pipeline templates use standard
JSON/YAML pipeline configuration formats, and the built-in best practices help perform
multi-account and multi-region deployments, and verify that pipelines cannot make unintended
changes to infrastructure.

You have two main options for using AWS SAM to deploy your serverless applications: 1)
Modify your existing pipeline configuration to use AWS SAM CLI commands, or 2) Generate an
example CI/CD pipeline configuration that you can use as a starting point for your own
application.

###### Topics

- [What is a pipeline?](#deploying-whatis-pipeline "#deploying-whatis-pipeline")
- [How AWS SAM uploads local files at deployment](deploy-upload-local-files.md "deploy-upload-local-files.md")
- [Generate a starter CI/CD pipeline with AWS SAM](serverless-generating-example-ci-cd.md "serverless-generating-example-ci-cd.md")
- [How to customize starter pipelines with AWS SAM](serverless-customizing-starter-pipelines.md "serverless-customizing-starter-pipelines.md")
- [Automate the deployment of your AWS SAM application](serverless-deploying-modify-pipeline.md "serverless-deploying-modify-pipeline.md")
- [How to use OIDC authentication with AWS SAM pipelines](deploying-with-oidc.md "deploying-with-oidc.md")

## What is a pipeline?

A pipeline is an automated sequence of steps that are performed to release a new version of an application.
With AWS SAM, you can use many common CI/CD systems to deploy your applications, including [AWS CodePipeline](https://aws.amazon.com/codepipeline "https://aws.amazon.com/codepipeline"), [Jenkins](https://www.jenkins.io/ "https://www.jenkins.io/"), [GitLab CI/CD](https://docs.gitlab.com/ee/ci/ "https://docs.gitlab.com/ee/ci/"), and [GitHub
Actions](https://github.com/features/actions "https://github.com/features/actions").

Pipeline templates include AWS deployment best practices to help with multi-account and multi-Region deployments.
AWS environments such as dev and production typically exist in different AWS accounts. This allows development teams
to configure safe deployment pipelines, without making unintended changes to infrastructure.

You can also supply your own custom pipeline templates to help to standardize pipelines across development teams.
