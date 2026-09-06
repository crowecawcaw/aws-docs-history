

# Product and service integrations with AWS CodeConnections
<a name="integrations-connections"></a>

AWS CodeConnections is integrated with a number of AWS services and partner products and services. Use the information in the following sections to help you configure connections to integrate with the products and services you use.

The following related resources can help you as you work with this service.

**Topics**
+ [Amazon CodeGuru Reviewer](#integrations-connections-codeguru)
+ [Amazon Q Developer](#integrations-connections-codewhisperer)
+ [Amazon SageMaker](#integrations-connections-sagemaker)
+ [AWS App Runner](#integrations-connections-apprunner)
+ [AWS CloudFormation](#integrations-connections-cloudformation)
+ [AWS CodeBuild](#integrations-connections-codebuild)
+ [AWS CodePipeline](#integrations-connections-codepipeline)
+ [Service Catalog](#integrations-connections-servicecatalog)
+ [AWS Proton](#integrations-connections-proton)

## Amazon CodeGuru Reviewer
<a name="integrations-connections-codeguru"></a>

[CodeGuru Reviewer](http://aws.amazon.com/codeguru/) is a service for monitoring your repository code. You can use connections to associate the third-party repository that has the code you want to review. For a tutorial where you learn how to configure CodeGuru Reviewer to monitor source code in a GitHub repository so that it can create recommendations that improve the code, see [Tutorial: monitor source code in a GitHub repository](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/tutorial-github-reviewer.html) in the *Amazon CodeGuru Reviewer User Guide*.

## Amazon Q Developer
<a name="integrations-connections-codewhisperer"></a>

Amazon Q Developer is a generative AI-powered conversational assistant that can help you to understand, build, extend, and operate AWS applications. For more information, see [What is Amazon Q Developer?](https://docs.aws.amazon.com/amazonq/latest/aws-builder-use-ug/what-is.html) in the *Amazon Q Developer User Guide*. 

## Amazon SageMaker
<a name="integrations-connections-sagemaker"></a>

[Amazon SageMaker](http://aws.amazon.com/sagemaker/) is a service for building, training, and deploying machine learning language models. For a tutorial where you configure a connection to your GitHub repository, see [SageMaker MLOps Project Walkthrough Using Third-party Git Repos](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-walkthrough-3rdgit.html) in the *Amazon SageMaker Developer Guide*.

## AWS App Runner
<a name="integrations-connections-apprunner"></a>

[AWS App Runner](http://aws.amazon.com/apprunner/) is a service that provides a fast, simple, and cost-effective way to deploy from source code or a container image directly to a scalable and secure web application in the AWS Cloud. You can deploy application code from your repository with an App Runner automatic integration and delivery pipeline. You can use connections to deploy your source code to an App Runner service from a private GitHub repository. For more information, see [Source code repository providers](https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code.html) in the *AWS App Runner Developer Guide*.

## AWS CloudFormation
<a name="integrations-connections-cloudformation"></a>

[AWS CloudFormation](http://aws.amazon.com/cloudformation/) is a service that helps you model and set up your AWS resources so that you can spend less time managing those resources and more time focusing on your applications that run in AWS. You create a template that describes all the AWS resources that you want (like Amazon EC2 instances or Amazon RDS DB instances), and CloudFormation takes care of provisioning and configuring those resources for you. 

You use connections with Git sync in CloudFormation to create a sync configuration that monitors your Git repository. For a tutorial that walks you through using Git sync for stack deployments, see [Working with CloudFormation Git sync](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/git-sync.html) in the *CloudFormation User Guide*.

 For more information about CloudFormation, see [Registering your account to publish CloudFormation extensions](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html) in the *CloudFormation Command Line Interface User Guide*.

## AWS CodeBuild
<a name="integrations-connections-codebuild"></a>

[AWS CodeBuild](http://aws.amazon.com/codebuild/) is a service for building and testing your code. CodeBuild eliminates the need to provision, manage, and scale your own build servers, and it provides prepackaged build environments for popular programming languages and build tools. For more information about using CodeBuild with connections to GitLab, see [GitLab connections](https://docs.aws.amazon.com/codebuild/latest/userguide/connections-gitlab.html) in the *AWS CodeBuild User Guide*.

## AWS CodePipeline
<a name="integrations-connections-codepipeline"></a>

[CodePipeline](http://aws.amazon.com/codepipeline/) is a continuous delivery service you can use to model, visualize, and automate the steps required to release your software. You can use connections to configure a third-party repository for CodePipeline source actions.

Learn more: 
+ See the CodePipeline action configuration reference page for the `SourceConnections` action. To view configuration parameters and an example JSON/YAML snippet, see [CodeStarSourceConnection](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodestarConnectionSource.html) in the *AWS CodePipeline User Guide*.
+ To view a **Getting started** tutorial that creates a pipeline with a third-party source repository, see [Getting started with connections](getting-started-connections.md) .

## Service Catalog
<a name="integrations-connections-servicecatalog"></a>

[Service Catalog](http://aws.amazon.com/servicecatalog/) enables organizations to create and manage catalogs of products that are approved for use on AWS.

When you authorize a connection between your AWS account and an external repository provider, such as GitHub, GitHub Enterprise, or Bitbucket, the connection allows you to sync Service Catalog products to template files that are managed through third-party repositories.

For more information, see [Syncing Service Catalog products to template files from GitHub, GitHub Enterprise, or Bitbucket](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/git-synced-sc-products.html) in the *Service Catalog User Guide*.

## AWS Proton
<a name="integrations-connections-proton"></a>

[AWS Proton](http://aws.amazon.com/proton/) is a cloud-based service for deploying to cloud infrastructure. You can use connections to create a link to your third-party repositories for the resources in your templates for AWS Proton. For more information, see [Create a link to your repository](https://docs.aws.amazon.com/proton/latest/userguide/ag-create-repo.html) in the *AWS Proton User Guide*.