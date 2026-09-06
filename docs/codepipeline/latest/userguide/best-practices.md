

# CodePipeline use cases
<a name="best-practices"></a>

The following sections describe use cases for CodePipeline.

**Topics**
+ [Use cases for CodePipeline](#use-cases)

## Use cases for CodePipeline
<a name="use-cases"></a>

You can create pipelines that integrate with other AWS services. These can be AWS services, such as Amazon S3, or third-party products, such as GitHub. This section provides examples for using CodePipeline to automate your code releases using different product integrations. For a full list of integrations with CodePipeline organized by action type, see [CodePipeline pipeline structure reference](reference-pipeline-structure.md).

**Topics**
+ [Use CodePipeline with Amazon S3, AWS CodeCommit, and AWS CodeDeploy](#use-cases-S3-codedeploy)
+ [Use CodePipeline with third-party action providers (GitHub and Jenkins)](#use-cases-thirdparty)
+ [Use CodePipeline to compile, build, and test code with CodeBuild](#use-cases-codebuild)
+ [Use CodePipeline with Amazon ECS for continuous delivery of container-based applications to the cloud](#use-cases-ecs)
+ [Use CodePipeline with Elastic Beanstalk for continuous delivery of web applications to the cloud](#use-cases-elasticbeanstalk)
+ [Use CodePipeline with AWS Lambda for continuous delivery of Lambda-based and serverless applications](#use-cases-lambda)
+ [Use CodePipeline with CloudFormation templates for continuous delivery to the cloud](#use-cases-cloudformation)

### Use CodePipeline with Amazon S3, AWS CodeCommit, and AWS CodeDeploy
<a name="use-cases-S3-codedeploy"></a>

When you create a pipeline, CodePipeline integrates with AWS products and services that act as action providers in each stage of your pipeline. When you choose stages in the wizard, you must choose a source stage and at least a build or deploy stage. The wizard creates the stages for you with default names that cannot be changed. These are the stage names created when you set up a full three-stage pipeline in the wizard:
+ A source action stage with a default name of “Source.”
+ A build action stage with a default name of “Build.”
+ A deploy action stage with a default name of “Staging.”

You can use the tutorials in this guide to create pipelines and specify stages:
+ The steps in [Tutorial: Create a simple pipeline (S3 bucket)](tutorials-simple-s3.md) help you use the wizard to create a pipeline with two default stages: “Source” and “Staging”, where your Amazon S3 repository is the source provider. This tutorial creates a pipeline that uses AWS CodeDeploy to deploy a sample application from an Amazon S3 bucket to Amazon EC2 instances running Amazon Linux.
+ The steps in [Tutorial: Create a simple pipeline (CodeCommit repository)](tutorials-simple-codecommit.md) help you use the wizard to create a pipeline with a “Source” stage that uses your AWS CodeCommit repository as the source provider. This tutorial creates a pipeline that uses AWS CodeDeploy to deploy a sample application from an AWS CodeCommit repository to an Amazon EC2 instance running Amazon Linux.

### Use CodePipeline with third-party action providers (GitHub and Jenkins)
<a name="use-cases-thirdparty"></a>

You can create pipelines that integrate with third-party products such as GitHub and Jenkins. The steps in [Tutorial: Create a four-stage pipeline](tutorials-four-stage-pipeline.md) show you how to create a pipeline that:
+ Gets source code from a GitHub repository,
+ Uses Jenkins to build and test the source code,
+ Uses AWS CodeDeploy to deploy the built and tested source code to Amazon EC2 instances running Amazon Linux or Microsoft Windows Server.

### Use CodePipeline to compile, build, and test code with CodeBuild
<a name="use-cases-codebuild"></a>

CodeBuild is a managed build service in the cloud that lets you build and test your code without a server or system. Use CodePipeline with CodeBuild to automate running revisions through the pipeline for continuous delivery of software builds whenever there is a change to the source code. For more information, see [Use CodePipeline with CodeBuild to test code and run builds](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-create-pipeline.html).

### Use CodePipeline with Amazon ECS for continuous delivery of container-based applications to the cloud
<a name="use-cases-ecs"></a>

Amazon ECS is a container management service that lets you deploy container-based applications to Amazon ECS instances in the cloud. Use CodePipeline with Amazon ECS to automate running revisions through the pipeline for continuous deployment of container-based applications whenever there is a change to the source image repository. For more information, see [Tutorial: Continuous Deployment with CodePipeline](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-cd-pipeline.html).

### Use CodePipeline with Elastic Beanstalk for continuous delivery of web applications to the cloud
<a name="use-cases-elasticbeanstalk"></a>

Elastic Beanstalk is a compute service that lets you deploy web applications and services to web servers. Use CodePipeline with Elastic Beanstalk for continuous deployment of web applications to your application environment. You can also use AWS CodeStar to create a pipeline with an Elastic Beanstalk deploy action.

### Use CodePipeline with AWS Lambda for continuous delivery of Lambda-based and serverless applications
<a name="use-cases-lambda"></a>

You can use AWS Lambda with CodePipeline for invoking an AWS Lambda function, as described in [Deploying Serverless Applications](https://docs.aws.amazon.com/lambda/latest/dg/automating-deployment.html). You can also use AWS Lambda and AWS CodeStar to create a pipeline for deploying serverless applications.

### Use CodePipeline with CloudFormation templates for continuous delivery to the cloud
<a name="use-cases-cloudformation"></a>

You can use CloudFormation with CodePipeline for continuous delivery and automation. For more information, see [Continuous Delivery with CodePipeline](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline.html). CloudFormation is also used to create the templates for pipelines created in AWS CodeStar.