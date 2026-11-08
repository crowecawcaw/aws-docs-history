

# Configure AWS Toolkit for Visual Studio
<a name="dotnet-ide-toolkit"></a>

## Step 1: Install AWS Toolkit
<a name="transform-dotnet-prerequisites"></a>

You can use AWS Transform with Visual Studio 2026 or 2022. Install the latest [AWS Toolkit for Visual Studio](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.AWSToolkitforVisualStudio2022) from the Visual Studio Marketplace website, or from within Visual Studio under **Extensions > Manage Extensions**.

## Step 2: Configure authentication
<a name="dotnet-setup-authentication-vs"></a>

To sign in, navigate to the Getting Started page at **Extensions > AWS Toolkit > AWS Transform > Getting Started**. You can sign in via IAM Identity Center and/or IAM depending on your [authentication settings](windows-setup.md#dotnet-setup-configuring). On the AWS Transform panel, select an existing profile or create a new one.

**First-time setup (IAM Identity Center)**

1. In Visual Studio, navigate to the Getting Started page.

1. On the AWS Transform panel, choose **Enable** to enable AWS Transform.

1. Choose the **Change authentication method** link if displayed.

1. Select sign-in option **IAM Identity Center** and choose **Continue**.

1. Add a new profile:
   + In the Profile dropdown, choose **Add new profile**.
   + Enter a profile name, your **AWS Transform Start URL for IDE**, and select the AWS Region.

1. Choose **Connect** and follow the prompts to sign in through your browser and grant access to the AWS Toolkit.

1. After you sign in, you are taken to the AWS Transform Dashboard.

**First-time setup (IAM credentials)**

1. In Visual Studio, navigate to the Getting Started page.

1. On the AWS Transform panel, choose **Enable** to enable AWS Transform.

1. Choose the **Change authentication method** link if displayed.

1. Select sign-in option **IAM** and choose **Continue**.

1. In the Profile dropdown, select an existing profile or choose **Add new profile**.
   + **Existing profile:** IAM profiles found in local `~/.aws/config` and `~/.aws/credentials` files are automatically listed for access keys, assume-role, SSO accounts and roles, and `credential_process`.
   + **New profile:** Enter a profile name, an **Access Key** and **Secret Access Key** for your IAM credential, and your AWS Transform **Web application URL**.

1. Choose **Connect** to sign in.

1. After you sign in, you are taken to the AWS Transform Dashboard.

In future IDE sessions, you can select the AWS Transform profile you just set up on the Getting Started page.