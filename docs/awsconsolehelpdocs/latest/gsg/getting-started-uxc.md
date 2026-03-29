# Getting started with AWS User Experience Customization

With UXC, account administrators can configure account customizations for the AWS Management Console.

## Prerequisites

Before you begin, you need the following:

- An AWS account
- Appropriate AWS Identity and Access Management (IAM) permissions for UXC. For more information, see [How AWS User Experience Customization works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md") and [AWS managed policies for the AWS Management Console](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

## Accessing UXC settings in the AWS Management Console

To access account color in the AWS Management Console, see [Accessing account information in the AWS Management Console](ainfo.md "ainfo.md"). To access service visibility and Region visibility in the AWS Management Console, see [Configuring the AWS Management Console using Unified Settings](unified-settings.md "unified-settings.md").

###### To set an account color in the console

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. On the navigation bar, choose your account name.
3. Choose **Account**.
4. In **Account display settings**, choose a color.
5. Choose **Update**.

###### To set visible Regions in the console

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. Open [Unified Settings](https://console.aws.amazon.com/settings/home "https://console.aws.amazon.com/settings/home").
3. Choose **Edit** in the **Visible Regions** section.
4. Set your visible Regions to **All available Regions** or **Select Regions** and configure your list.
5. Choose **Save changes**.

###### To set visible services in the console

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. Open [Unified Settings](https://console.aws.amazon.com/settings/home "https://console.aws.amazon.com/settings/home").
3. Choose **Edit** in the **Visible services** section.
4. Set your visible services to **All services** or **Select services** and configure your list.
5. Choose **Save changes**.

## Accessing UXC settings programmatically

You can also manage account customization settings programmatically or as infrastructure as code. For more information, see the [AWS User Experience Customization API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md") and the [AWS::UXC::AccountCustomization](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-uxc-accountcustomization.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-uxc-accountcustomization.md") CloudFormation template reference.
