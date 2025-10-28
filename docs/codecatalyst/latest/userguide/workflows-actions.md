Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Configuring workflow actions

An _action_ is the main building block of a workflow, and defines a
logical unit of work, or task, to perform during a workflow run. Typically, a workflow includes multiple
actions that run sequentially or in parallel depending on how you've configured them.

###### Topics

- [Action types](#workflows-actions-types "#workflows-actions-types")
- [Adding an action to a workflow](workflows-add-action.md "workflows-add-action.md")
- [Removing an action from a workflow](workflows-delete-action.md "workflows-delete-action.md")
- [Developing a custom action](workflows-custom-action.md "workflows-custom-action.md")
- [Grouping actions into action groups](workflows-group-actions.md "workflows-group-actions.md")
- [Sequencing actions](workflows-depends-on.md "workflows-depends-on.md")
- [Sharing artifacts and files between
  actions](workflows-working-artifacts.md "workflows-working-artifacts.md")
- [Specifying the action version to use](workflows-action-versions.md "workflows-action-versions.md")
- [Listing the available action
  versions](workflows-action-versions-determine.md "workflows-action-versions-determine.md")
- [Viewing an action's source code](workflows-view-source.md "workflows-view-source.md")
- [Integrating with GitHub Actions](integrations-github-actions.md "integrations-github-actions.md")

## Action types

Within an Amazon CodeCatalyst workflow, you can use the following types of actions.

###### Action types

- [CodeCatalyst actions](#workflows-actions-types-cc "#workflows-actions-types-cc")
- [CodeCatalyst Labs actions](#workflows-actions-types-cc-labs "#workflows-actions-types-cc-labs")
- [GitHub Actions](#workflows-actions-types-github "#workflows-actions-types-github")
- [Third-party actions](#workflows-actions-types-3p "#workflows-actions-types-3p")

### CodeCatalyst actions

A _CodeCatalyst action_ is an action that is authored, maintained,
and fully supported by the CodeCatalyst development team.

There are CodeCatalyst actions for building, testing, and deploying applications, as
well as for performing miscellaneous tasks, such as invoking an AWS Lambda
function.

The following CodeCatalyst actions are available:

- **Build**

This action builds your artifacts and runs your unit tests in a Docker
container. For more information, see [Adding the build action](build-add-action.md "build-add-action.md").

- **Test**

This action runs integration and system tests against your application or
artifacts. For more information, see [Adding the test action](test-add-action.md "test-add-action.md").

- **Amazon S3 publish**

This action copies your application artifacts to an Amazon S3 bucket. For more
information, see [Publishing files to Amazon S3 with a workflow](s3-pub-action.md "s3-pub-action.md").

- **AWS CDK bootstrap**

This action provisions the resources that the AWS CDK needs to deploy your
CDK app. For more information, see [Bootstrapping an AWS CDK app with a workflow](cdk-boot-action.md "cdk-boot-action.md").

- **AWS CDK deploy**

This action synthesizes and deploys an AWS Cloud Development Kit (AWS CDK) app. For more
information, see [Deploying an AWS CDK app with a workflow](cdk-dep-action.md "cdk-dep-action.md").

- **AWS Lambda invoke**

This action invokes an AWS Lambda function. For more information, see [Invoking a Lambda function using a workflow](lam-invoke-action.md "lam-invoke-action.md").

- **GitHub Actions**

This action is a _CodeCatalyst_ action that allows you to run
GitHub Actions within a CodeCatalyst workflow. For more information, see [Invoking a Lambda function using a workflow](lam-invoke-action.md "lam-invoke-action.md").

- **Deploy AWS CloudFormation stack**

This action deploys AWS CloudFormation stacks. For more information, see [Deploying an AWS CloudFormation stack](deploy-action-cfn.md "deploy-action-cfn.md").

- **Deploy to Amazon ECS**

This action registers an Amazon ECS task definition and deploys it to an Amazon ECS
service. For more information, see [Deploying to Amazon ECS with a workflow](deploy-action-ecs.md "deploy-action-ecs.md").

- **Deploy to Kubernetes cluster**

This action deploys an application to a Kubernetes cluster. For more
information, see [Deploying to Amazon EKS with a
workflow](deploy-action-eks.md "deploy-action-eks.md").

- **Render Amazon ECS task definition**

This action inserts a container image URI into an Amazon ECS task definition
JSON file, creating a new task definition file. For more information, see
[Modifying an Amazon ECS task definition](render-ecs-action.md "render-ecs-action.md").

Documentation for CodeCatalyst actions is available in this guide, and in each action's
readme.

For information about the available CodeCatalyst actions, and how to add one to a
workflow, see [Adding an action to a workflow](workflows-add-action.md "workflows-add-action.md").

### CodeCatalyst Labs actions

A _CodeCatalyst Labs action_ is an action that is part of Amazon
CodeCatalyst Labs, a proving ground for experimental applications. CodeCatalyst Labs actions
have been developed to showcase integrations with AWS services.

The following CodeCatalyst Labs actions are available:

- **Deploy to AWS Amplify Hosting**

This action deploys an application to Amplify Hosting.

- **Deploy to AWS App Runner**

This action deploys the latest image in a source image repository to
App Runner.

- **Deploy to Amazon CloudFront and Amazon S3**

This action deploys an application to CloudFront and Amazon S3.

- **Deploy with AWS SAM**

This action deploys your serverless application with AWS Serverless Application Model
(AWS SAM).

- **Invalidate Amazon CloudFront Cache**

This action invalidates a CloudFront cache for a given set of paths.

- **Outgoing Webhook**

This action allows users to send messages within a workflow to an
arbitrary web server using an HTTPS request.

- **Publish to AWS CodeArtifact**

This action publishes packages to a CodeArtifact repository.

- **Publish to Amazon SNS**

This action allows users to integrate with Amazon SNS by creating a topic,
publishing to a topic, or subscribing to a topic.

- **Push to Amazon ECR**

This action builds and publishes a Docker image to an Amazon Elastic Container Registry (Amazon ECR)
repository.

- **Scan with Amazon CodeGuru Security**

This action creates a zip archive of a configured code path and uses
CodeGuru Security to run a code scan.

- **Terraform Community Edition**

This action runs Terraform Community Edition `plan` and
`apply` operations.

Documentation for CodeCatalyst Labs actions is available in each action's readme.

For information about adding a CodeCatalyst Labs action to a workflow and viewing its
readme, see [Adding an action to a workflow](workflows-add-action.md "workflows-add-action.md").

### GitHub Actions

A _GitHub Action_ is a lot like a [CodeCatalyst action](#workflows-actions-types-cc "#workflows-actions-types-cc"), except that it was developed for
use with GitHub workflows. For details about GitHub Actions, see the [GitHub Actions](https://docs.github.com/en/actions "https://docs.github.com/en/actions") documentation.

You can use GitHub Actions alongside native CodeCatalyst actions in a CodeCatalyst workflow.

For your convenience, the CodeCatalyst console provides access to several popular GitHub
Actions. You can also use any GitHub Action listed in the [GitHub Marketplace](https://github.com/marketplace/actions "https://github.com/marketplace/actions")
(subject to a few limitations).

Documentation for GitHub Actions is available in each action's readme.

For more information, see [Integrating with GitHub Actions](integrations-github-actions.md "integrations-github-actions.md").

### Third-party actions

A _third-party action_ is an action that is authored by a
third-party vendor, and made available in the CodeCatalyst console. Examples of
third-party actions include the **Mend SCA** and
**SonarCloud Scan** actions, authored by Mend and Sonar,
respectively.

Documentation for third-party actions is available in each action's readme.
Additional documentation might also be provided by the third-party vendor.

For information about adding a third-party action to a workflow and viewing its
readme, see [Adding an action to a workflow](workflows-add-action.md "workflows-add-action.md").
