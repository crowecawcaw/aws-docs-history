

# Getting started with AWS User Experience Customization
<a name="getting-started-uxc"></a>

With UXC, account administrators can configure account customizations for the AWS Management Console.

## Prerequisites
<a name="getting-started-uxc-prerequisites"></a>

Before you begin, you need the following:
+ An AWS account
+ Appropriate AWS Identity and Access Management (IAM) permissions for UXC. For more information, see [How AWS User Experience Customization works with IAM](security_iam_service-with-iam.md) and [AWS managed policies for the AWS Management Console](security-iam-awsmanpol.md).

## Accessing UXC settings in the AWS Management Console
<a name="accessing-uxc-console"></a>

To access account color in the AWS Management Console, see [Accessing account information in the AWS Management Console](ainfo.md). To access service visibility and Region visibility in the AWS Management Console, see [Configuring the AWS Management Console using Unified Settings](unified-settings.md).

**To set an account color in the console**

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/).

1. On the navigation bar, choose your account name.

1. Choose **Account**.

1. In **Account display settings**, choose a color.

1. Choose **Update**.

**To set visible Regions in the console**

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/).

1. Open [Unified Settings](https://console.aws.amazon.com/settings/home).

1. Choose **Edit** in the **Visible Regions** section.

1. Set your visible Regions to **All available Regions** or **Select Regions** and configure your list.

1. Choose **Save changes**.

**To set visible services in the console**

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/).

1. Open [Unified Settings](https://console.aws.amazon.com/settings/home).

1. Choose **Edit** in the **Visible services** section.

1. Set your visible services to **All services** or **Select services** and configure your list.

1. Choose **Save changes**.

## Accessing UXC settings programmatically
<a name="accessing-uxc-programmatically"></a>

You can also manage account customization settings programmatically or as infrastructure as code. For more information, see the [AWS User Experience Customization API Reference](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/APIReference/Welcome.html) and the [AWS::UXC::AccountCustomization](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-uxc-accountcustomization.html) CloudFormation template reference.