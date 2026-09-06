

# Getting started with notifications
<a name="getting-started"></a>

The easiest way to get started with notifications is to set up a notification rule on one of your build projects, deployment applications, pipelines, or repositories.

**Note**  
The first time you create a notification rule, a service-linked role is created in your account. For more information, see [Using service-linked roles for AWS CodeStar Notifications](using-service-linked-roles.md).

**Topics**
+ [Prerequisites](#getting-started-prerequisites)
+ [Create a notification rule for a repository](getting-started-repository.md)
+ [Create a notification rule for a build project](getting-started-build.md)
+ [Create a notification rule for a deployment application](getting-started-deploy.md)
+ [Create a notification rule for a pipeline](getting-started-pipeline.md)

## Prerequisites
<a name="getting-started-prerequisites"></a>

Complete the steps in [Setting up](setting-up.md). You also need a resource for which you create a notification rule.
+ [Create a build project in CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/create-project.html) or use an existing one.
+ [Create an application](https://docs.aws.amazon.com/codedeploy/latest/userguide/applications-create.html) or use an existing deployment application.
+ [Create a pipeline in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-create.html) or use an existing one.
+ [Create an AWS CodeCommit repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-repository.html) or use an existing one.