# Implementing CI/CD integration with your Elastic Beanstalk

environment

Elastic Beanstalk integrates with many CI/CD tools to automate your application development
workflow. CI/CD practices enable you to automatically build, test, and deploy your applications
with minimal manual intervention. Continuous delivery/deployment (CD) extends continuous
integration (CI) by automating the deployment process. You can create streamlined deployment
pipelines using AWS services like CodePipeline or third-party tools such as Jenkins and GitLab to
ensure consistent, reliable deployments to your Elastic Beanstalk environments.

## AWS sources to get started

The following list highlights CI/CD tools and the corresponding AWS resources that provide step-by-step guidance for creating automated
deployment pipelines to Elastic Beanstalk environments:

- AWS CodePipeline – This [AWS Getting Started
  Resource Center](https://aws.amazon.com/getting-started/hands-on/continuous-deployment-pipeline/ "https://aws.amazon.com/getting-started/hands-on/continuous-deployment-pipeline/") tutorial shows you how to set up a continuous deployment
  pipeline to Elastic Beanstalk from GitHub , S3, or AWS CodeCommit.
- GitHub Actions – This [.NET on AWS
  Blog](https://aws.amazon.com/blogs/dotnet/deploy-to-elastic-beanstalk-environment-with-github-actions/ "https://aws.amazon.com/blogs/dotnet/deploy-to-elastic-beanstalk-environment-with-github-actions/") post walks you through configuring YAML-based workflows to setup a
  continuous deployment pipeline to Elastic Beanstalk directly from GitHub.
- GitLab – This [AWS
  DevOps Developer Productivity Blog](https://aws.amazon.com/blogs/devops/deploy-a-docker-application-on-aws-elastic-beanstalk-with-gitlab/ "https://aws.amazon.com/blogs/devops/deploy-a-docker-application-on-aws-elastic-beanstalk-with-gitlab/") post demonstrates how to configure GitLab
  continuous pipelines to deploy Node.js applications to Elastic Beanstalk Docker environments.
- Azure DevOps – This [.NET on AWS Blog](https://aws.amazon.com/blogs/dotnet/deploy-to-elastic-beanstalk-with-azure-devops/ "https://aws.amazon.com/blogs/dotnet/deploy-to-elastic-beanstalk-with-azure-devops/")
  post guides you through implementing a continuous deployment pipeline from an Azure DevOps
  Git repository to Elastic Beanstalk using Azure Pipelines.

## Additional resources

The following third-party tools and resources can help you implement automated deployment
pipelines to Elastic Beanstalk environments:

- Jenkins – The [AWS EBDeployment Jenkins
  plugin](https://plugins.jenkins.io/awseb-deployment-plugin/ "https://plugins.jenkins.io/awseb-deployment-plugin/") enables direct deployment to Elastic Beanstalk environments from your Jenkins Job
  Configuration page.
- Circle CI: – The [Orbs for
  Elastic Beanstalk](https://circleci.com/developer/orbs/orb/circleci/aws-elastic-beanstalk "https://circleci.com/developer/orbs/orb/circleci/aws-elastic-beanstalk") provide reusable configuration packages to deploy and scale applications
  to Elastic Beanstalk.
- Bitbucket Pipelines – The article [Deploy Elastic Beanstalk Application using Bitbucket Pipelines](https://avishayil.medium.com/deploy-to-elastic-beanstalk-using-bitbucket-pipelines-189eb75cf052 "https://avishayil.medium.com/deploy-to-elastic-beanstalk-using-bitbucket-pipelines-189eb75cf052") provides a basic
  configuration example for implementing Bitbucket Pipelines with Elastic Beanstalk.
