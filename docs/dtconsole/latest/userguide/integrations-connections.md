# Product and service integrations with

AWS CodeConnections

AWS CodeConnections is integrated with a number of AWS services and partner products and services.
Use the information in the following sections to help you configure connections to integrate
with the products and services you use.

The following related resources
can help you as you work with this service.

###### Topics

- [Amazon CodeGuru Reviewer](#integrations-connections-codeguru "#integrations-connections-codeguru")
- [Amazon Q Developer](#integrations-connections-codewhisperer "#integrations-connections-codewhisperer")
- [Amazon SageMaker](#integrations-connections-sagemaker "#integrations-connections-sagemaker")
- [AWS App Runner](#integrations-connections-apprunner "#integrations-connections-apprunner")
- [AWS CloudFormation](#integrations-connections-cloudformation "#integrations-connections-cloudformation")
- [AWS CodeBuild](#integrations-connections-codebuild "#integrations-connections-codebuild")
- [AWS CodePipeline](#integrations-connections-codepipeline "#integrations-connections-codepipeline")
- [Service Catalog](#integrations-connections-servicecatalog "#integrations-connections-servicecatalog")
- [AWS Proton](#integrations-connections-proton "#integrations-connections-proton")

## Amazon CodeGuru Reviewer

[CodeGuru Reviewer](http://aws.amazon.com/codeguru/ "http://aws.amazon.com/codeguru/") is a service for monitoring your
repository code. You can use connections to associate the third-party repository that has the
code you want to review. For a tutorial where you learn how to configure CodeGuru Reviewer to monitor
source code in a GitHub repository so that it can create recommendations that improve the
code, see [Tutorial:
monitor source code in a GitHub repository](../../../codeguru/latest/reviewer-ug/tutorial-github-reviewer.md "../../../codeguru/latest/reviewer-ug/tutorial-github-reviewer.md") in the _Amazon CodeGuru Reviewer
User Guide_.

## Amazon Q Developer

Amazon Q Developer is a generative AI-powered conversational assistant that can help you to understand, build, extend, and operate AWS applications. For more information, see [What is Amazon Q Developer?](../../../amazonq/latest/aws-builder-use-ug/what-is.md "../../../amazonq/latest/aws-builder-use-ug/what-is.md") in the _Amazon Q Developer User Guide_.

## Amazon SageMaker

[Amazon SageMaker](http://aws.amazon.com/sagemaker/ "http://aws.amazon.com/sagemaker/") is a service for
building, training, and deploying machine learning language models. For a tutorial where you
configure a connection to your GitHub repository, see [SageMaker MLOps Project Walkthrough Using Third-party Git Repos](../../../sagemaker/latest/dg/sagemaker-projects-walkthrough-3rdgit.md "../../../sagemaker/latest/dg/sagemaker-projects-walkthrough-3rdgit.md") in the _Amazon SageMaker Developer Guide_.

## AWS App Runner

[AWS App Runner](http://aws.amazon.com/apprunner/ "http://aws.amazon.com/apprunner/") is a service that provides a
fast, simple, and cost-effective way to deploy from source code or a container image directly
to a scalable and secure web application in the AWS Cloud. You can deploy application code
from your repository with an App Runner automatic integration and delivery pipeline. You can use
connections to deploy your source code to an App Runner service from a private GitHub repository.
For more information, see [Source code repository
providers](../../../apprunner/latest/dg/service-source-code.md "../../../apprunner/latest/dg/service-source-code.md") in the _AWS App Runner Developer Guide_.

## AWS CloudFormation

[AWS CloudFormation](http://aws.amazon.com/cloudformation/ "http://aws.amazon.com/cloudformation/") is a service that helps
you model and set up your AWS resources so that you can spend less time managing those
resources and more time focusing on your applications that run in AWS. You create a template
that describes all the AWS resources that you want (like Amazon EC2 instances or Amazon RDS DB
instances), and CloudFormation takes care of provisioning and configuring those resources for you.

You use connections with Git sync in CloudFormation to create a sync configuration that
monitors your Git repository. For a tutorial that walks you through using Git sync for stack
deployments, see [Working with CloudFormation Git sync](../../../AWSCloudFormation/latest/UserGuide/git-sync.md "../../../AWSCloudFormation/latest/UserGuide/git-sync.md") in the _CloudFormation User
Guide_.

For more information about CloudFormation, see [Registering
your account to publish CloudFormation extensions](../../../cloudformation-cli/latest/userguide/publish-extension.md "../../../cloudformation-cli/latest/userguide/publish-extension.md") in the _CloudFormation Command Line Interface User Guide_.

## AWS CodeBuild

[AWS CodeBuild](http://aws.amazon.com/codebuild/ "http://aws.amazon.com/codebuild/") is a service for building
and testing your code. CodeBuild eliminates the need to provision, manage, and scale your own
build servers, and it provides prepackaged build environments for popular programming
languages and build tools. For more information about using CodeBuild with connections to GitLab,
see [GitLab
connections](../../../codebuild/latest/userguide/connections-gitlab.md "../../../codebuild/latest/userguide/connections-gitlab.md") in the _AWS CodeBuild User Guide_.

## AWS CodePipeline

[CodePipeline](http://aws.amazon.com/codepipeline/ "http://aws.amazon.com/codepipeline/") is a continuous delivery
service you can use to model, visualize, and automate the steps required to release your
software. You can use connections to configure a third-party repository for CodePipeline source
actions.

Learn more:

- See the CodePipeline action configuration reference page for the
  `SourceConnections` action. To view configuration parameters and an example
  JSON/YAML snippet, see [CodeStarSourceConnection](../../../codepipeline/latest/userguide/action-reference-CodestarConnectionSource.md "../../../codepipeline/latest/userguide/action-reference-CodestarConnectionSource.md") in the _AWS CodePipeline User
  Guide_.
- To view a **Getting started** tutorial that creates a
  pipeline with a third-party source repository, see [Getting started with connections](getting-started-connections.md "getting-started-connections.md")
  .

## Service Catalog

[Service Catalog](http://aws.amazon.com/servicecatalog/ "http://aws.amazon.com/servicecatalog/") enables organizations to
create and manage catalogs of products that are approved for use on AWS.

When you authorize a connection between your AWS account and an external repository
provider, such as GitHub, GitHub Enterprise, or
Bitbucket,
the connection allows you to sync Service Catalog products to template files that are managed through
third-party repositories.

For more information, see [Syncing
Service Catalog products to template files from GitHub, GitHub Enterprise, or Bitbucket](../../../servicecatalog/latest/adminguide/git-synced-sc-products.md "../../../servicecatalog/latest/adminguide/git-synced-sc-products.md") in the
_Service Catalog User Guide_.

## AWS Proton

[AWS Proton](http://aws.amazon.com/proton/ "http://aws.amazon.com/proton/") is a cloud-based service for
deploying to cloud infrastructure. You can use connections to create a link to your
third-party repositories for the resources in your templates for AWS Proton. For more information,
see [Create a link to
your repository](../../../proton/latest/userguide/ag-create-repo.md "../../../proton/latest/userguide/ag-create-repo.md") in the _AWS Proton User Guide_.
