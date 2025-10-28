# Deploy your application and resources with AWS SAM

Deploying your application provisions and configures your AWS resources in the AWS Cloud,
making your application run in the cloud. AWS SAM uses [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide.md "../../../AWSCloudFormation/latest/UserGuide.md") as its underlying deployment mechanism.
AWS SAM uses the build artifacts you create when running the **sam build** command as the standard inputs
for deploying your serverless application.

With AWS SAM, you can deploy your serverless application manually, or you can automate deployments. To automate deployments,
you use AWS SAM pipelines with a continuous integration and continuous deployment (CI/CD) system of your choice. Your deployment pipeline is an automated
sequence of steps that are performed to release a new version of your serverless application.

The topics in this section provide guidance on both automated and manual deployments.
To deploy your application manually, you use AWS SAM CLI commands.
To automate deployments, refer to the topics in this section.
They specifically provide in-depth content on automating deployments using pipelines and a CI/CD system.
This includes generating a starter pipeline, setting up automation, troubleshooting deployments,
using OpenID Connect (OIDC) user authentication, and uploading local files at deployment.

###### Topics

- [Introduction to deploying with AWS SAM](using-sam-cli-deploy.md "using-sam-cli-deploy.md")
- [Options for deploying your application with AWS SAM](deploying-options.md "deploying-options.md")
- [Using CI/CD systems and pipelines to deploy with AWS SAM](deploying-cicd-overview.md "deploying-cicd-overview.md")
- [Introduction to using sam sync to sync to AWS Cloud](using-sam-cli-sync.md "using-sam-cli-sync.md")
