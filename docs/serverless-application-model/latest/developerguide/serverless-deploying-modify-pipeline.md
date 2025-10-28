# Automate the deployment of your AWS SAM application

In AWS SAM, how you automate the deployment of your AWS SAM application varies depending on the CI/CD system you are using.
For this reason, the examples in this section show you how to configure various CI/CD systems to automate building
serverless applications in an AWS SAM build container image. These build container images make it easier to build and package
serverless applications using the AWS SAM CLI.

The procedures for your existing CI/CD pipeline to deploy serverless applications using
AWS SAM are slightly different depending on which CI/CD system you are using.

The following topics provide examples for configuring your CI/CD system to build serverless
applications within an AWS SAM build container image:

###### Topics

- [Using AWS CodePipeline to deploy with AWS SAM](deploying-using-codepipeline.md "deploying-using-codepipeline.md")
- [Using Bitbucket Pipelines to deploying with AWS SAM](deploying-using-bitbucket.md "deploying-using-bitbucket.md")
- [Using Jenkins to deploy with AWS SAM](deploying-using-jenkins.md "deploying-using-jenkins.md")
- [Using GitLab CI/CD to deploy with AWS SAM](deploying-using-gitlab.md "deploying-using-gitlab.md")
- [Using GitHub Actions to deploy with AWS SAM](deploying-using-github.md "deploying-using-github.md")
