Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Bootstrapping an AWS CDK app with a workflow

This section describes how to bootstrap an AWS CDK application using a CodeCatalyst workflow. To
accomplish this, you must add the **AWS CDK bootstrap** action to your workflow.
The **AWS CDK bootstrap** action provisions a bootstrap stack in your AWS
environment using the [modern template](../../../cdk/v2/guide/bootstrapping.md#bootstrapping-template "../../../cdk/v2/guide/bootstrapping.md#bootstrapping-template"). If a
bootstrap stack already exists, the action updates it if necessary. Having a bootstrap stack
present in AWS is a prerequisite for deploying an AWS CDK app.

For more information about bootstrapping, see [Bootstrapping](../../../cdk/v2/guide/bootstrapping.md "../../../cdk/v2/guide/bootstrapping.md") in the
_AWS Cloud Development Kit (AWS CDK) Developer Guide_.

###### Topics

- [When to use the 'AWS CDK bootstrap' action](#cdk-boot-action-when-to-use "#cdk-boot-action-when-to-use")
- [How the 'AWS CDK bootstrap' action works](#cdk-boot-action-how-it-works "#cdk-boot-action-how-it-works")
- [CDK CLI versions used by the "AWS CDK
  bootstrap" action](#cdk-boot-action-cdk-version "#cdk-boot-action-cdk-version")
- [Runtime image used by the 'AWS CDK bootstrap'
  action](#cdk-boot-action-runtime "#cdk-boot-action-runtime")
- [Example: Bootstrapping an AWS CDK app](cdk-boot-action-example-workflow.md "cdk-boot-action-example-workflow.md")
- [Adding the 'AWS CDK bootstrap' action](cdk-boot-action-add.md "cdk-boot-action-add.md")
- ['AWS CDK bootstrap' variables](cdk-boot-action-variables.md "cdk-boot-action-variables.md")
- ['AWS CDK bootstrap' action YAML](cdk-boot-action-ref.md "cdk-boot-action-ref.md")

## When to use the 'AWS CDK bootstrap' action

Use this action if you have a workflow that deploys an AWS CDK app, and you want to deploy
(and update, if needed) the bootstrap stack at the same time. In this case, you would add the
**AWS CDK bootstrap** action to the same workflow as the one that deploys
your AWS CDK app.

**Do not** use this action if either of the following
applies:

- You already deployed a bootstrap stack using another mechanism, and you want to keep
  it intact (no updates).
- You want to use a [custom bootstrap
  template](../../../cdk/v2/guide/bootstrapping.md#bootstrapping-customizing "../../../cdk/v2/guide/bootstrapping.md#bootstrapping-customizing"), which is not supported with the **AWS CDK bootstrap**
  action.

## How the 'AWS CDK bootstrap' action works

The **AWS CDK bootstrap** works as follows:

1. At runtime, if you specified version 1.0.7 or earlier of the action, the action
   downloads the latest CDK CLI (also called the AWS CDK Tookit) to the CodeCatalyst [build image](build-images.md "build-images.md").

If you specified version 1.0.8 or later, the action comes bundled with a [specific version](cdk-dep-action.md#cdk-dep-action-cdk-version "cdk-dep-action.md#cdk-dep-action-cdk-version") of the CDK CLI, so
no download occurs. 2. The action uses the CDK CLI to run the `cdk bootstrap` command. This
command performs the bootstrapping tasks described in the [Bootstrapping](../../../cdk/v2/guide/bootstrapping.md "../../../cdk/v2/guide/bootstrapping.md") topic in the
_AWS Cloud Development Kit (AWS CDK) Developer Guide_.

## CDK CLI versions used by the "AWS CDK

bootstrap" action

The following table shows which version of the CDK CLI is used by default by
different versions of the **AWS CDK bootstrap** action.

###### Note

You might be able to override the default. For more information, see [CdkCliVersion](cdk-boot-action-ref.md#cdk.boot.cdk.cli.version "cdk-boot-action-ref.md#cdk.boot.cdk.cli.version") in the ['AWS CDK bootstrap' action YAML](cdk-boot-action-ref.md "cdk-boot-action-ref.md").

| 'AWS CDK bootstrap' action version | AWS CDK CLI version |
| ---------------------------------- | ------------------- |
| 1.0.0 – 1.0.7                      | latest              |
| 1.0.8 or later                     | 2.99.1              |

## Runtime image used by the 'AWS CDK bootstrap'

action

The following table shows the runtime environment images that CodeCatalyst uses to run
different versions of the **AWS CDK bootstrap** action. The images include
different sets of preinstalled tooling. For more information, see [Active images](build-images.md#build-curated-images "build-images.md#build-curated-images").

###### Note

We recommend upgrading your **AWS CDK bootstrap** action to version 2.x to
take advantage of the latest tooling available on the March 2024 image. To upgrade the
action, set its `Identifier` property to `aws/cdk-bootstrap@v2`
in your workflow definition file. For more information, see ['AWS CDK deploy' action YAML](cdk-dep-action-ref.md "cdk-dep-action-ref.md").

| 'AWS CDK bootstrap' action version | Runtime environment images |
| ---------------------------------- | -------------------------- |
| 1.x                                | November 2022 images       |
| 2.x                                | March 2024 images          |
