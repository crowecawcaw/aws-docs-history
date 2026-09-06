

# Installing the Amazon Q Developer extension or plugin in your IDE
<a name="q-in-IDE-setup"></a>

**End of support notice**  
On April 30, 2027, AWS will discontinue support for Amazon Q Developer IDE plugins. For capabilities similar to Amazon Q Developer IDE plugins, explore Kiro to access the latest models and features, including agentic coding, chat and MCP support. For more information, see [Amazon Q Developer IDE plugins end of support](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-developer-ide-end-of-support.html).

To set up Amazon Q Developer in your integrated development environment (IDE), complete the following steps. After installing the Amazon Q extension or plugin, authenticate through IAM Identity Center or AWS Builder ID. You can use Amazon Q for free, without an AWS account, by authenticating with Builder ID. 

To get started, download the Amazon Q extension or plugin for your IDE:
+ [Download Amazon Q for Eclipse](https://marketplace.eclipse.org/content/amazon-q)
+ [Download Amazon Q for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.amazon-q-vscode)
+ [Download Amazon Q for JetBrains IDEs](https://plugins.jetbrains.com/plugin/24267-amazon-q/)
+ [Download Amazon Q in the AWS Toolkit for Visual Studio](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.AWSToolkitforVisualStudio2022)

**Note**  
In general, the default duration for a session that is authenticated through IAM Identity Center is 8 hours. However, in the case of Amazon Q, the default session lasts 90 days (if you set up IAM Identity Center on April 18, 2024 or later). For more information refer to [How to extend the session duration for Amazon Q in the IDE](https://docs.aws.amazon.com/singlesignon/latest/userguide/configure-user-session.html#90-day-extended-session-duration) in the *AWS IAM Identity Center User Guide*

To sign in and authenticate, complete the steps in this section.

**Topics**
+ [Prerequisite: Supported IDE versions](#q-in-IDE-setup-prereqs)
+ [Authenticating in Eclipse IDEs](#setup-eclipse)
+ [Authenticating in JetBrains IDEs](#setup-jetbrains)
+ [Authenticating in Visual Studio Code](#setup-vscode)
+ [Authenticating in Visual Studio](#setup-vs)
+ [Using an IAM principal in your AWS console](#q-no-IAM-in-IDEs)

## Prerequisite: Supported IDE versions
<a name="q-in-IDE-setup-prereqs"></a>
+ The minimum version of Eclipse supported by Amazon Q is 2024-06 (4.32).
+ The minimum version of JetBrains IDEs (including IntelliJ and PyCharm) supported by Amazon Q is 2024.3. 
+ The minimum version of Visual Studio Code supported by Amazon Q is 1.85.0.
+ Only Visual Studio for Windows is supported by Amazon Q. The minimum version of Visual Studio supported is Visual Studio 2022 version 17.7. All Visual Studio 2022 editions are supported.

## Authenticating in Eclipse IDEs
<a name="setup-eclipse"></a>

You can authenticate for free with AWS Builder ID or with IAM Identity Center with a Amazon Q Developer Pro subscription. Choose your authentication method to see steps to start using Amazon Q in Eclipse.

------
#### [ Builder ID ]

This procedure does not require you to have Builder ID. If you have not yet signed up for Builder ID, you will have the opportunity to do so during the sign-in process.

1. Install the [Amazon Q plugin](https://marketplace.eclipse.org/content/amazon-q) in Eclipse.

1. Choose the Amazon Q icon in the IDE toolbar.

1. An Amazon Q tab opens in the IDE. Under **Choose a sign-in option**, choose **Personal account**, and then choose **Continue**. You are redirected to your browser.

1. Follow the instructions in your browser to authenticate with Builder ID. When you've completed authentication, return to the Eclipse IDE.

1. To begin using Amazon Q, choose the Amazon Q icon to open the chat Amazon Q panel.

------
#### [ IAM Identity Center ]

Before you begin this procedure, your administrator should have:
+ Created an identity for you in IAM Identity Center
+ Subscribed that identity to Amazon Q Developer Pro

After your identity has been subscribed to Amazon Q Developer Pro, complete the following steps to authenticate:

1. Install the [Amazon Q plugin](https://marketplace.eclipse.org/content/amazon-q) in Eclipse.

1. Choose the Amazon Q icon in the IDE toolbar.

1. An Amazon Q tab opens in the IDE. Under **Choose a sign-in option**, choose **Company account**, and then choose **Continue**.

1. Enter the **Start URL** that your administrator got from [the Amazon Q subscription console](manage-account-details.md).

1. Choose the AWS Region in which your administrator set up your [IAM Identity Center instance](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-instances.html).

1. Choose **Continue**. You are redirected to your browser.

1. Follow the instructions in your browser to authenticate with IAM Identity Center. When you've completed authentication, return to the Eclipse IDE.

1. To begin using Amazon Q, choose the Amazon Q icon to open the chat Amazon Q panel.

------

## Authenticating in JetBrains IDEs
<a name="setup-jetbrains"></a>

You can authenticate for free with AWS Builder ID or with IAM Identity Center with a Amazon Q Developer Pro subscription. Choose your authentication method to see steps to start using Amazon Q in your JetBrains IDE.

------
#### [ Builder ID ]

This procedure does not require you to have Builder ID. If you have not yet signed up for Builder ID, you will have the opportunity to do so during the sign-in process.

1. Install the [Amazon Q plugin](https://plugins.jetbrains.com/plugin/24267-amazon-q/) in your JetBrains IDE.

1. Choose the Amazon Q icon in your IDE.

   The icon will be on the side of the interface by default.

1. Follow the instructions in your browser to authenticate with Builder ID.

1. To begin using Amazon Q, choose the Amazon Q icon to chat with Amazon Q, or choose **Amazon Q** from the IDE navigation bar.

------
#### [ IAM Identity Center ]

Before you begin this procedure, your administrator should have:
+ Created an identity for you in IAM Identity Center
+ Subscribed that identity to Amazon Q Developer Pro

After your identity has been subscribed to Amazon Q Developer Pro, complete the following steps to authenticate:

1. Install the [Amazon Q plugin](https://plugins.jetbrains.com/plugin/24267-amazon-q/) in your JetBrains IDE.

1. Choose the Amazon Q icon in your IDE.

   The icon will be on the side of the interface by default.

1. Choose **Company account**.

1. Provide the **Start URL** that your administrator got from [the Amazon Q subscription console](manage-account-details.md).

1. Provide the AWS Region in which your administrator set up your IAM Identity Center [ instance](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-instances.html).

1. Choose **Continue**. The focus will switch to your web browser.

1. Follow the instructions in your browser to authenticate with IAM Identity Center, and then return to the IDE.

1. If your administrator has configured more than one Amazon Q Developer profile, you will see the profiles you have access to. Choose the profile that meets your current working needs, or that your administrator has instructed you to use. For more information about profiles, see [What is the Amazon Q Developer profile?](subscribe-understanding-profile.md).

   If there is only one profile available, that profile will automatically be chosen and you can begin using Amazon Q.

   To change your Amazon Q Developer profile, choose **Amazon Q** from the IDE navigation bar, and then choose **Change profile**. From the window that appears, choose the profile you'd like to use. 

1. To begin using Amazon Q, choose the Amazon Q icon to chat with Amazon Q, or choose **Amazon Q** from the IDE navigation bar.

------

## Authenticating in Visual Studio Code
<a name="setup-vscode"></a>

You can authenticate for free with AWS Builder ID or with IAM Identity Center with a Amazon Q Developer Pro subscription. Choose your authentication method to see steps to start using Amazon Q in VS Code.

------
#### [ Builder ID ]

This procedure does not require you to have Builder ID. If you have not yet signed up for Builder ID, you will have the opportunity to do so during the sign-in process.

1. Install the [Amazon Q extension](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.amazon-q-vscode) in VS Code.

1. Choose the Amazon Q icon in your IDE.

   The icon will be on the side of the interface by default.

1. Follow the instructions in your browser to authenticate with Builder ID.

1. To begin using Amazon Q, choose the Amazon Q icon to chat with Amazon Q, or choose **Amazon Q** from the IDE navigation bar.

------
#### [ IAM Identity Center ]

Before you begin this procedure, your administrator should have:
+ Created an identity for you in IAM Identity Center
+ Subscribed that identity to Amazon Q Developer Pro

After your identity has been subscribed to Amazon Q Developer Pro, complete the following steps to authenticate:

1. Install the [Amazon Q extension](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.amazon-q-vscode) in VS Code.

1. Choose the Amazon Q icon in your IDE.

   The icon will be on the side of the interface by default.

1. Choose **Company account**.

1. Provide the **Start URL** that your administrator got from [the Amazon Q subscription console](manage-account-details.md).

1. Provide the AWS Region in which your administrator set up your IAM Identity Center [ instance](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-instances.html).

1. Choose **Continue**. The focus will switch to your web browser.

1. Follow the instructions in your browser to authenticate with IAM Identity Center, and then return to the IDE.

1. If your administrator has configured more than one Amazon Q Developer profile, you will see the profiles you have access to. Choose the profile that meets your current working needs, or that your administrator has instructed you to use. For more information about profiles, see [What is the Amazon Q Developer profile?](subscribe-understanding-profile.md).

   If there is only one profile available, that profile will automatically be chosen and you can begin using Amazon Q.

   To change your Amazon Q Developer profile, choose **Amazon Q** from the IDE navigation bar, and then choose **Change profile**. From the command palette, choose the profile you'd like to use. 

1. To begin using Amazon Q, choose the Amazon Q icon to chat with Amazon Q, or choose **Amazon Q** from the IDE navigation bar.

------

## Authenticating in Visual Studio
<a name="setup-vs"></a>

To connect to your AWS accounts from the Toolkit for Visual Studio, open the **Getting Started with the AWS Toolkit** User Interface (connection UI) by completing the following procedure.

1. From the Visual Studio main menu, expand **Extensions** then expand the **AWS Toolkit**.

1. From the **AWS Toolkit** menu options choose **Getting Started**.

1. The **Getting Started with the AWS Toolkit** connection UI opens in Visual Studio.

You can authenticate for free with AWS Builder ID or with IAM Identity Center with a Amazon Q Developer Pro subscription. Choose your authentication method to see steps to start using Amazon Q in Visual Studio.

------
#### [ Builder ID ]

1. From Visual Studio, expand **Extensions** from the main menu and then expand the **AWS Toolkit** sub-menu.

1. Choose **Getting started**. The **Getting Started** tab opens in the Visual Studio editor window. 

1. In the **Amazon Q** section, choose **Enable**. 

1. From the **Free Tier** section, choose the **Sign up or Sign in** button. 

1. Confirm that you want to open the AWS Authorize request portal in your default web browser. 

1. Follow the prompts in your default web browser. You're notified when the authorization process is complete, and it's safe to close your browser and return to Visual Studio.

------
#### [ IAM Identity Center ]

1. From Visual Studio, expand **Extensions** from the main menu and then expand the **AWS Toolkit** sub-menu.

1. Choose **Getting started**. The **Getting Started** tab opens in the Visual Studio editor window. 

1. In the **Amazon Q** section, choose **Enable**. You will fill out the Professional Tier section to authenticate.

1. The credentials profile is made up of the Profile Name, Start URL, Profile Region, or SSO Region provided by an administrator at your company or organization. For detailed information about IAM Identity Center credentials, see [What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) in the *IAM Identity Center User Guide*.

   If you have an existing credentials profile, choose it from the dropdown menu in the Professional tier panel, and then choose **Connect**.

   To create a new credentials profile, fill out the following fields from the Professional tier section:

   1. In the **Profile Name** text field, enter the name of the IAM Identity Center profile you want to authenticate with.

   1. In the **Start URL** text field, enter the start URL that's attached to your IAM Identity Center credentials.

   1. From the **Profile Region (defaults to us-east-1)** drop-down menu, choose the AWS Region that's defined by the IAM Identity Center user profile you're authenticating with.

   1. From the **SSO Region (defaults to us-east-1)** drop-down menu, choose the **SSO Region** that's defined by your IAM Identity Center credentials, then choose the **Connect** button to open the **Log in with AWS IAM Identity Center** dialog.

1. Confirm that you want to open the AWS Authorize request portal in your default web browser.

1. Follow the prompts in your default web browser. You're notified when the authorization process is complete, and it's safe to close your browser and return to Visual Studio.

1. A **Sign into Amazon Q** window appears. In the credentials profile dropdown, choose the profile you used to authenticate in the previous steps. 

1. If your administrator has configured more than one Amazon Q Developer profile, you are then prompted to choose a Q Developer profile from the dropdown menu. Choose the profile that meets your current working needs, or that your administrator has instructed you to use. For more information about profiles, see [What is the Amazon Q Developer profile?](subscribe-understanding-profile.md).

   If there is only one profile available, that profile will automatically be chosen and you can begin using Amazon Q.

   To change your Amazon Q Developer profile, choose **Amazon Q** from the IDE navigation bar, and then choose **Change Q Developer Profile**. From the window that appears, choose the profile you'd like to use. 

   You can also change your profile by choosing the overflow menu in the chat panel header, and then choosing **Change Q Developer Profile**.

------

For more information about authenticating in the Toolkit for Visual Studio, see [Getting Started](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/getting-set-up.html) in the *AWS Toolkit for Visual Studio User Guide*.

## Using an IAM principal in your AWS console
<a name="q-no-IAM-in-IDEs"></a>

Depending on how you use AWS, you may be accustomed to using your IAM credentials to sign in to the console for all AWS services. However, you cannot use Amazon Q Developer in the IDE as an IAM principal, or with an IAM role. You must authenticate with credentials from either IAM Identity Center or Builder ID.