

# Creating code signing configurations for Lambda
<a name="configuration-codesigning-create"></a>

To enable code signing for a function, you create a *code signing configuration* and attach it to the function. A code signing configuration defines a list of allowed signing profiles and the policy action to take if any of the validation checks fail.

**Note**  
Functions defined as container images do not support code signing.

**Topics**
+ [Configuration prerequisites](#config-codesigning-prereqs)
+ [Creating code signing configurations](#config-codesigning-config-console)
+ [Enabling code signing for a function](#config-codesigning-function-console)

## Configuration prerequisites
<a name="config-codesigning-prereqs"></a>

Before you can configure code signing for a Lambda function, use AWS Signer to do the following:
+ Create one or more [signing profiles](https://docs.aws.amazon.com/signer/latest/developerguide/signing-profiles.html).
+ Use a signing profile to [create a signed code package for your function](https://docs.aws.amazon.com/signer/latest/developerguide/lambda-workflow.html).

## Creating code signing configurations
<a name="config-codesigning-config-console"></a>

A code signing configuration defines a list of allowed signing profiles and the signature validation policy.

**To create a code signing configuration (console)**

1. Open the [Code signing configurations page](https://console.aws.amazon.com/lambda/home#/code-signing-configurations) of the Lambda console.

1. Choose **Create configuration**.

1. For **Description**, enter a descriptive name for the configuration.

1. Under **Signing profiles**, add up to 20 signing profiles to the configuration.

   1. For **Signing profile version ARN**, choose a profile version's Amazon Resource Name (ARN), or enter the ARN.

   1. To add an additional signing profile, choose **Add signing profiles**.

1. Under **Signature validation policy**, choose **Warn** or **Enforce**.

1. Choose **Create configuration**.

## Enabling code signing for a function
<a name="config-codesigning-function-console"></a>

To enable code signing for a function, add a code signing configuration to the function.

**Important**  
Code signing configurations only prevent new deployments of unsigned code. If you add a code signing configuration to an existing function that has unsigned code, that code keeps running until you deploy a new code package.

**To associate a code signing configuration with a function (console)**

1. Open the [Event Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the function for which you want to enable code signing.

1. Open the **Configuration** tab.

1. Scroll down and choose **Code signing**.

1. Choose **Edit**.

1. In **Edit code signing**, choose a code signing configuration for this function.

1. Choose **Save**.