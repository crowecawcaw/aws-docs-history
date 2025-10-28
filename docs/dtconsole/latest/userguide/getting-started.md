# Getting started with notifications

The easiest way to get started with notifications is to set up a notification rule on one of your
build projects, deployment applications, pipelines, or repositories.

###### Note

The first time you create a notification rule, a service-linked role is created in
your account. For more information, see [Using service-linked roles for
AWS CodeStar Notifications](using-service-linked-roles.md "using-service-linked-roles.md").

###### Topics

- [Prerequisites](#getting-started-prerequisites "#getting-started-prerequisites")
- [Create a notification rule for a
  repository](getting-started-repository.md "getting-started-repository.md")
- [Create a notification rule for a build
  project](getting-started-build.md "getting-started-build.md")
- [Create a notification rule for a deployment application](getting-started-deploy.md "getting-started-deploy.md")
- [Create a notification rule for a
  pipeline](getting-started-pipeline.md "getting-started-pipeline.md")

## Prerequisites

Complete the steps in [Setting up](setting-up.md "setting-up.md"). You
also need a resource for which you create a notification rule.

- [Create a build project in
  CodeBuild](../../../codebuild/latest/userguide/create-project.md "../../../codebuild/latest/userguide/create-project.md") or use an existing one.
- [Create an
  application](../../../codedeploy/latest/userguide/applications-create.md "../../../codedeploy/latest/userguide/applications-create.md") or use an existing deployment application.
- [Create a pipeline in
  CodePipeline](../../../codepipeline/latest/userguide/pipelines-create.md "../../../codepipeline/latest/userguide/pipelines-create.md") or use an existing one.
- [Create an AWS CodeCommit
  repository](../../../codecommit/latest/userguide/how-to-create-repository.md "../../../codecommit/latest/userguide/how-to-create-repository.md") or use an existing one.
