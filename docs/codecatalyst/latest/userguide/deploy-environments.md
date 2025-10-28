Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Deploying into AWS accounts and VPCs

Using [CodeCatalyst workflows](workflow.md "workflow.md"), you can deploy applications and
other resources to target AWS accounts and Amazon VPCs in the AWS cloud. To enable these
deployments, you must set up CodeCatalyst environments.

A CodeCatalyst _environment_, not to be confused with a [Dev Environment](devenvironment.md "devenvironment.md"), defines the target AWS account and optional Amazon VPC that
a CodeCatalyst [workflow](workflow.md "workflow.md") connects to. An environment also defines
the [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that
a workflow needs to access the AWS services and resources within the target account.

You can set up multiple environments and give them names such as development, test, staging,
and production. When you deploy into these environments, information about the deployments
appears on the CodeCatalyst **Deployment activity** and **Deployment
targets** tabs in the environment.

## How do I get started with

environments?

The high-level steps to add and use a CodeCatalyst environment are as follows:

1. In your CodeCatalyst space, **connect one or more AWS
   accounts**. During this process, add the IAM roles that your workflow
   requires to access resources in your AWS account. For more information, see [Allowing access to AWS resources with connected
   AWS accounts](ipa-connect-account.md "ipa-connect-account.md").
2. In your CodeCatalyst project, **create an environment** that
   includes one of the AWS accounts and IAM roles from step 1. For more information, see
   [Creating an environment](deploy-environments-creating-environment.md "deploy-environments-creating-environment.md").
3. In your CodeCatalyst project, in a workflow, **add an [action](workflows-actions.md "workflows-actions.md") that points to the environment**
   you created in step 2. For more information, see [Adding an action to a workflow](workflows-add-action.md "workflows-add-action.md").

You have now configured an environment. The action can now deploy resources into the
AWS account specified in the environment.

###### Note

You can also add an Amazon VPC to the environment. For more information, see [Adding
VPC connections for a space](../adminguide/managing-vpcs.md "../adminguide/managing-vpcs.md") in the _CodeCatalyst Administration
Guide_ and [Associating a VPC with an
environment](deploy-environments-associate-vpc.md "deploy-environments-associate-vpc.md").

## Can multiple environments exist within a single

workflow?

Yes. If a workflow includes multiple actions, each of those actions can be assigned an
environment. For example, you could have a workflow that includes two deploy actions, where
one is assigned a `my-staging-enviroment` environment and another is assigned a
`my-production-environment` environment.

## Which workflow actions support

environments?

Any workflow action that deploys resources into the AWS cloud, or communicates with
AWS services for other reasons (such as monitoring and reporting), supports
environments.

## Which actions support having their

deployment information displayed in CodeCatalyst?

Of the workflow actions that support environments, only a few support having their
deployment information displayed on the **Deployment activity** and
**Deployment targets** pages of the CodeCatalyst console.

The following workflow actions support having their deployment information
displayed:

- **Deploy AWS CloudFormation stack** – For more information, see [Deploying an AWS CloudFormation stack](deploy-action-cfn.md "deploy-action-cfn.md")
- **Deploy to Amazon ECS** – For more information, see [Deploying to Amazon ECS with a workflow](deploy-action-ecs.md "deploy-action-ecs.md")
- **Deploy to Kubernetes cluster** – For more information, see [Deploying to Amazon EKS with a
  workflow](deploy-action-eks.md "deploy-action-eks.md")
- **AWS CDK deploy** – For more information, see [Deploying an AWS CDK app with a workflow](cdk-dep-action.md "cdk-dep-action.md")

## Supported Regions

The **Environments** page can display resources in any AWS
Region.

## Is an environment

mandatory?

An environment is mandatory if the workflow action to which it is assigned deploys
resources into the AWS cloud, or communicates with AWS services for other reasons (such as
monitoring and reporting).

For example, if you have a build action that builds an application but doesn't need to
communicate with your AWS account or Amazon VPC, then you do not need to assign an environment to
the action. If, however, the build action sends logs to the Amazon CloudWatch service in your
AWS account, then the action must have an environment assigned.

###### Topics

- [Creating an environment](deploy-environments-creating-environment.md "deploy-environments-creating-environment.md")
- [Associating an environment with
  an action](deploy-environments-add-app-to-environment.md "deploy-environments-add-app-to-environment.md")
- [Associating a VPC with an
  environment](deploy-environments-associate-vpc.md "deploy-environments-associate-vpc.md")
- [Associating an AWS account with an
  environment](deploy-environments-associate-account.md "deploy-environments-associate-account.md")
- [Changing the IAM role of an action](deploy-environments-switch-role.md "deploy-environments-switch-role.md")
