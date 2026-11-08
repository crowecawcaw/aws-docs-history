

# Get started with AWS Transform for Windows modernization
<a name="windows-setup"></a>

## Configuring AWS Transform
<a name="dotnet-setup-configuring"></a>

To enable AWS Transform for your AWS account, follow the instructions at [Getting Started with AWS Transform](getting-started.md).

You can configure authentication with IAM Identity Center, IAM-only access, or both:
+ [Getting started with AWS IAM Identity Center](transform-setup.md#transform-app-admin-starting-idc)
+ [Getting started with IAM-only access](transform-setup.md#transform-iam-only-access)

Take note of the **Web application URL** and the **Start URL for IDE**.
+ **Web application URL**: For web users, this is the browser link to the AWS Transform web application. For Visual Studio IDE users, this link must be provided when configuring a sign-in profile for IAM credentials.
+ **Start URL for IDE**: For Visual Studio IDE users, this link must be provided when configuring a sign-in profile for IAM Identity Center.

## Configuring IDE
<a name="windows-setup-configuring-ide"></a>

Developers who work in Visual Studio should [configure AWS Toolkit for Visual Studio](dotnet-ide-toolkit.md) and create a sign-in profile.