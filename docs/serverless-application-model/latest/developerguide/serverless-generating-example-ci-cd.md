# Generate a starter CI/CD pipeline with AWS SAM

When you are ready automate deployment, you can use one of AWS SAM’s starter pipeline templates to
generate a deployment pipeline for the CI/CD system you choose to use. Your deployment pipeline
is what you configure and use to automate the deployment of your serverless application.
A starter pipeline template is pre-configured to help you quickly set up your deployment pipeline
for your serverless application.

With a starter pipeline template, you can generate pipelines in minutes using the
[sam pipeline init](sam-cli-command-reference-sam-pipeline-init.md "sam-cli-command-reference-sam-pipeline-init.md") command.

The starter pipeline templates use the familiar JSON/YAML syntax of the CI/CD system, and
incorporate best practices such as managing artifacts across multiple accounts and regions, and
using the minimum amount of permissions required to deploy the application. Currently, the AWS SAM
CLI supports generating starter CI/CD pipeline configurations for [AWS CodePipeline](https://aws.amazon.com/codepipeline "https://aws.amazon.com/codepipeline"), [Jenkins](https://www.jenkins.io/ "https://www.jenkins.io/"),
[GitLab CI/CD](https://docs.gitlab.com/ee/ci/ "https://docs.gitlab.com/ee/ci/"), [GitHub Actions](https://github.com/features/actions "https://github.com/features/actions"), and [Bitbucket Pipelines](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/ "https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/").

Here are the high-level tasks you need to perform to generate a starter pipeline
configuration:

1. **Create infrastructure resources** – Your pipeline
   requires certain AWS resources, for example the IAM user and roles with necessary
   permissions, an Amazon S3 bucket, and optionally an Amazon ECR repository.
2. **Connect your Git repository with your CI/CD system**
   – Your CI/CD system needs to know which Git repository will trigger the pipeline to
   run. Note that this step may not be necessary, depending on which combination of Git
   repository and CI/CD system you are using.
3. **Generate your pipeline configuration** – This step
   generates a starter pipeline configuration that includes two deployment stages.
4. **Commit your pipeline configuration to your Git
   repository** – This step is necessary to ensure your CI/CD system is aware
   of your pipeline configuration, and will run when changes are committed.
   After you've generated the starter pipeline configuration and committed it to your Git
   repository, whenever someone commits a code change to that repository your pipeline will be
   triggered to run automatically.

The ordering of these steps, and details of each step, vary based on your CI/CD
system:

- If you are using AWS CodePipeline, see [Generating starter pipeline
  for AWS CodePipeline in AWS SAM](serverless-generating-example-ci-cd-codepipeline.md "serverless-generating-example-ci-cd-codepipeline.md").
- If you are using Jenkins, GitLab CI/CD, GitHub Actions, or Bitbucket Pipelines, see
  [Use AWS SAM to generate starter pipelines for Jenkins, GitLab CI/CD, GitHub
  Actions, Bitbucket Pipelines](serverless-generating-example-ci-cd-others.md "serverless-generating-example-ci-cd-others.md").
