Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Deploying an AWS CDK app with a workflow

This section describes how to deploy an AWS Cloud Development Kit (AWS CDK) app into your AWS account using a
workflow. To accomplish this, you must add the **AWS CDK deploy** action to your
workflow. The **AWS CDK deploy** action synthesizes and deploys your AWS Cloud Development Kit (AWS CDK)
app into AWS. If your app already exists in AWS, the action updates it if necessary.

For general information about writing apps using the AWS CDK, see [What is the AWS CDK?](../../../cdk/v2/guide/home.md "../../../cdk/v2/guide/home.md") in the
_AWS Cloud Development Kit (AWS CDK) Developer Guide_.

###### Topics

- [When to use the 'AWS CDK deploy' action](#cdk-dep-action-when-to-use "#cdk-dep-action-when-to-use")
- [How the 'AWS CDK deploy' action works](#cdk-dep-action-how-it-works "#cdk-dep-action-how-it-works")
- [CDK CLI versions used by the 'AWS CDK
  deploy' action](#cdk-dep-action-cdk-version "#cdk-dep-action-cdk-version")
- [Runtime image used by the 'AWS CDK deploy'
  action](#cdk-dep-action-runtime "#cdk-dep-action-runtime")
- [How many stacks can the action
  deploy?](#cdk-dep-action-how-many-stacks "#cdk-dep-action-how-many-stacks")
- [Example: Deploying an AWS CDK app](cdk-dep-action-example-workflow.md "cdk-dep-action-example-workflow.md")
- [Adding the 'AWS CDK deploy' action](cdk-dep-action-add.md "cdk-dep-action-add.md")
- ['AWS CDK deploy' variables](cdk-dep-action-variables.md "cdk-dep-action-variables.md")
- ['AWS CDK deploy' action YAML](cdk-dep-action-ref.md "cdk-dep-action-ref.md")

## When to use the 'AWS CDK deploy' action

Use this action if you have developed an app using the AWS CDK, and you now want to deploy
it automatically as part of automated continuous integration and delivery (CI/CD) workflow.
For example, you might want to deploy your AWS CDK app automatically whenever someone merges a
pull request related to your AWS CDK app source.

## How the 'AWS CDK deploy' action works

The **AWS CDK deploy** works as follows:

1. At runtime, if you specified version 1.0.12 or earlier of the action, the action
   downloads the latest CDK CLI (also called the AWS CDK Tookit) to the CodeCatalyst [runtime environment image](#cdk-dep-action-runtime "#cdk-dep-action-runtime").

If you specified version 1.0.13 or later, the action comes bundled with a [specific version](#cdk-dep-action-cdk-version "#cdk-dep-action-cdk-version") of the CDK CLI, so
no download occurs. 2. The action uses the CDK CLI to run the `cdk deploy` command. This
command synthesizes and deploys your AWS CDK app into AWS. For more information about this
command, see the [AWS CDK
Toolkit (cdk command)](../../../cli/latest/reference/s3/sync.md "../../../cli/latest/reference/s3/sync.md") topic in the _AWS Cloud Development Kit (AWS CDK) Developer Guide_.

## CDK CLI versions used by the 'AWS CDK

deploy' action

The following table shows which version of the CDK CLI is used by default by
different versions of the **AWS CDK deploy** action.

###### Note

You might be able to override the default. For more information, see [CdkCliVersion](cdk-dep-action-ref.md#cdk.dep.cdk.cli.version "cdk-dep-action-ref.md#cdk.dep.cdk.cli.version") in the ['AWS CDK deploy' action YAML](cdk-dep-action-ref.md "cdk-dep-action-ref.md").

| 'AWS CDK deploy' action version | AWS CDK CLI version |
| ------------------------------- | ------------------- |
| 1.0.0 – 1.0.12                  | latest              |
| 1.0.13 or later                 | 2.99.1              |

## Runtime image used by the 'AWS CDK deploy'

action

The following table shows the runtime environment images that CodeCatalyst uses to run
different versions of the **AWS CDK deploy** action. The images include
different sets of preinstalled tooling. For more information, see [Active images](build-images.md#build-curated-images "build-images.md#build-curated-images").

###### Note

We recommend upgrading your **AWS CDK deploy** action to version 2.x to
take advantage of the latest tooling available on the March 2024 image. To upgrade the
action, set its `Identifier` property to `aws/cdk-deploy@v2`
in your workflow definition file. For more information, see ['AWS CDK deploy' action YAML](cdk-dep-action-ref.md "cdk-dep-action-ref.md").

| 'AWS CDK deploy' action version | Runtime environment images |
| ------------------------------- | -------------------------- |
| 1.x                             | November 2022 images       |
| 2.x                             | March 2024 images          |

## How many stacks can the action

deploy?

The **AWS CDK deploy** can deploy a single stack only. If your AWS CDK app
consists of multiple stacks, you must create a parent stack with nested stacks, and deploy the
parent using this action.
