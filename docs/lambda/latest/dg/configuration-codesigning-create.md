# Creating code signing configurations for Lambda

To enable code signing for a function, you create a _code signing configuration_ and attach
it to the function. A code signing configuration defines a list of allowed signing profiles and the policy action
to take if any of the validation checks fail.

###### Note

Functions defined as container images do not support code signing.

###### Sections

- [Configuration prerequisites](#config-codesigning-prereqs "#config-codesigning-prereqs")
- [Creating code signing configurations](#config-codesigning-config-console "#config-codesigning-config-console")
- [Enabling code signing for a function](#config-codesigning-function-console "#config-codesigning-function-console")

## Configuration prerequisites

Before you can configure code signing for a Lambda function, use AWS Signer to do the following:

- Create one or more [signing profiles](../../../signer/latest/developerguide/signing-profiles.md "../../../signer/latest/developerguide/signing-profiles.md").
- Use a signing profile to [create a signed code package for your function](../../../signer/latest/developerguide/lambda-workflow.md "../../../signer/latest/developerguide/lambda-workflow.md").

## Creating code signing configurations

A code signing configuration defines a list of allowed signing profiles and the signature validation
policy.

###### To create a code signing configuration (console)

1. Open the [Code signing configurations
   page](https://console.aws.amazon.com/lambda/home#/code-signing-configurations "https://console.aws.amazon.com/lambda/home#/code-signing-configurations") of the Lambda console.
2. Choose **Create configuration**.
3. For **Description**, enter a descriptive name for the configuration.
4. Under **Signing profiles**, add up to 20 signing profiles to the configuration.
   1. For **Signing profile version ARN**, choose a profile version's Amazon Resource Name
      (ARN), or enter the ARN.
   2. To add an additional signing profile, choose **Add signing profiles**.

5. Under **Signature validation policy**, choose **Warn** or
   **Enforce**.
6. Choose **Create configuration**.

## Enabling code signing for a function

To enable code signing for a function, add a code signing configuration to the function.

###### Important

Code signing configurations only prevent new deployments of unsigned code. If you add a code signing configuration to an existing function that has unsigned code, that code keeps running until you deploy a new code package.

###### To associate a code signing configuration with a function (console)

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Choose the function for which you want to enable code signing.
3. Open the **Configuration** tab.
4. Scroll down and choose **Code signing**.
5. Choose **Edit**.
6. In **Edit code signing**, choose a code signing configuration for this function.
7. Choose **Save**.
