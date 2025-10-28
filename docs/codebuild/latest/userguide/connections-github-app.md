# GitHub App connections for GitHub and GitHub Enterprise Server

You can use GitHub App to connect with CodeBuild. GitHub App connections are
supported through [AWS CodeConnections](../../../dtconsole/latest/userguide/welcome-connections.md "../../../dtconsole/latest/userguide/welcome-connections.md").

The source provider access enables you to trigger a build by subscribing
to [GitHub webhook events](github-webhook.md "github-webhook.md") using [CreateWebhook](../APIReference/API_CreateWebhook.md "../APIReference/API_CreateWebhook.md"), or to use [Tutorial: Configure a CodeBuild-hosted GitHub
Actions runner](action-runner.md "action-runner.md") in CodeBuild.

###### Note

CodeConnections is available in fewer regions than CodeBuild. You can use cross-region connections in CodeBuild. Connections
created in opt-in regions, cannot be used in other regions. For more information, see
[AWS CodeConnections endpoints and quotas](../../../general/latest/gr/codestar_connections.md "../../../general/latest/gr/codestar_connections.md").

###### Topics

- [Step 1: Create a connection to GitHub App
  (console)](#connections-github-console "#connections-github-console")
- [Step 2: Grant CodeBuild project IAM role access to use the connection](#connections-github-role-access "#connections-github-role-access")
- [Step 3: Configure CodeBuild to use the new connection](#connections-github-account-credential "#connections-github-account-credential")
- [Troubleshooting the GitHub App](#connections-github-troubleshooting "#connections-github-troubleshooting")

## Step 1: Create a connection to GitHub App

(console)

Use these steps to use the CodeBuild console to add a connection for your project in GitHub.

###### To create a connection to GitHub

- Follow the instructions in the _Developer Tools User Guide_ for
  [Create a connection to GitHub](../../../dtconsole/latest/userguide/connections-create-github.md "../../../dtconsole/latest/userguide/connections-create-github.md").

###### Note

Instead of creating or using an existing connection in your account, you can use a connection shared from another AWS account.
For more information, see [Share connections with AWS accounts](../../../dtconsole/latest/userguide/connections-share.md "../../../dtconsole/latest/userguide/connections-share.md").

## Step 2: Grant CodeBuild project IAM role access to use the connection

You can grant CodeBuild project IAM role access to use the GitHub tokens vended by your connection.

###### To grant CodeBuild project IAM role access

1. Create an IAM role for your CodeBuild project by following the instructions to [Allow CodeBuild to interact with other AWS
   services](setting-up-service-role.md "setting-up-service-role.md") for your CodeBuild project.
2. While following the instructions, add the following IAM policy to your CodeBuild project role to grant access to the connection.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codeconnections:GetConnectionToken",
 "codeconnections:GetConnection"
 ],
 "Resource": [
 "`arn:aws:iam::*:role/Service*`"
 ]
 }
 ]
}`

```

## Step 3: Configure CodeBuild to use the new connection

You can configure a connection as an account level credential and use it in a project.

AWS Management Console

###### To configure a connection as an account level credential in the AWS Management Console

1. For **Source provider**, choose
   **GitHub**.
2. For **Credential**, do one of the following:
   - Choose **Default source credential** to use
     your account's default source credential to apply to all projects.
     1. If you aren't connected to GitHub, choose **Manage default source credential**.
     2. For **Credential type**, choose **GitHub App**.
     3. In **Connection**, choose to use an existing connection or create a new connection.

   - Choose **Custom source credential** to use
     a custom source credential to override your account's default settings.
     1. For **Credential type**, choose **GitHub App**.
     2. In **Connection**, choose to use an existing connection or create a new connection.

AWS CLI

###### To configure a connection as an account level credential in the AWS CLI

- Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run
  the **import-source-credentials** command, specifying the
  `--auth-type`, `--server-type`, and `--token` for your
  connection.

Use the following command:

```
aws codebuild import-source-credentials --auth-type CODECONNECTIONS --server-type GITHUB --token `<connection-arn>`
```

You can also set up multiple tokens for your CodeBuild projects. For more information, see [Configure multiple tokens as source level credentials](multiple-access-tokens.md#asm-source-credential "multiple-access-tokens.md#asm-source-credential").

## Troubleshooting problems with the GitHub App

The following information can help you troubleshoot common issues with the GitHub App.

###### Topics

- [Install the AWS Connector for GitHub app in an undesired region](#connections-github-troubleshooting.undesired-region "#connections-github-troubleshooting.undesired-region")
- [The GitHub App connection doesn't have access to repositories](#connections-github-troubleshooting.repo-access "#connections-github-troubleshooting.repo-access")
- [The AWS service's IAM role is missing necessary IAM permissions.](#connections-github-troubleshooting.iam-permissions "#connections-github-troubleshooting.iam-permissions")

### Install the AWS Connector for GitHub app in an undesired region

**Issue:** You installed the AWS Connector for GitHub from the GitHub Marketplace, but the connection was
created in an undesired region. If you attempt to reconfigure the app on the GitHub website, it won't work because the app is already installed
on your GitHub account.

**Possible cause:** The app is already installed in your GitHub account, so you can only reconfigure the app
permissions.

**Recommended solution:** You can create a new connection with the installation ID in the desired region.

1. Open the CodeConnections console at [https://console.aws.amazon.com/codesuite/settings/connections](https://console.aws.amazon.com/codesuite/settings/connections "https://console.aws.amazon.com/codesuite/settings/connections")
   and navigate to the desired region
   using the region selector in the AWS console navigation bar.
2. Follow the instructions in the _Developer Tools User Guide_ for
   [Create a connection to GitHub](../../../dtconsole/latest/userguide/connections-create-github.md "../../../dtconsole/latest/userguide/connections-create-github.md").

###### Note

Since you've already installed the AWS Connector for GitHub app, you can choose it instead of installing a new app.

### The GitHub App connection doesn't have access to repositories

**Issue:** An AWS service using the connection, such as CodeBuild or CodePipeline, reports that it doesn't have access to
the repository or the repository doesn't exist. Some possible error messages include:

- `Authentication required for primary source.`
- `Unable to create webhook at this time. Please try again later.`
- `Failed to create webhook. GitHub API limit reached. Please try again later.`

**\*Possible cause:** You might have been using the GitHub app and haven't granted the webhook permission scope.\*

**Recommended solution:** To grant the required permission scope, follow the instructions
in [Navigating to the GitHub App you want to review or modify](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#navigating-to-the-github-app-you-want-to-review-or-modify "https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#navigating-to-the-github-app-you-want-to-review-or-modify") to configure the installed app. Under the permissions section,
you'll see the app doesn't have webhooks permission, and there is an option for you to review the newly requested permissions.
Review and accept the new permissions. For more infomation, see [Approving updated permissions for a GitHub App](https://docs.github.com/en/apps/using-github-apps/approving-updated-permissions-for-a-github-app "https://docs.github.com/en/apps/using-github-apps/approving-updated-permissions-for-a-github-app").

**\*Possible cause:** The connection was working as expected, but suddenly doesn’t have access to the repositories.\*

**Possible solution:** Start by reviewing your [authorizations](https://docs.github.com/en/apps/using-github-apps/reviewing-and-revoking-authorization-of-github-apps "https://docs.github.com/en/apps/using-github-apps/reviewing-and-revoking-authorization-of-github-apps") and your [installations](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps "https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps"), then verify the GitHub App is authorized and installed. If the GitHub App installation is suspended, then you need to unsuspended it.
If the GitHub App is not authorized for a [UAT
(User Access Token)](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-with-a-github-app-on-behalf-of-a-user "https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-with-a-github-app-on-behalf-of-a-user") connection, or not installed for an [IAT (Installation Access Token)](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app-installation "https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app-installation") connection, the existing connection is not usable any more, and you will need to create a new connection. Note that reinstalling the GitHub App will not
revive the previous connection that was associated to the old installation.

**Possible solution:** If the connection is a UAT connection, make sure the connection is not concurrently being used, such as a being used in multiple CodeBuild concurrent runs of build.
This is because GitHub immediately invalidates a previously issued UAT if an expiring token is refreshed by the connection. If you need to use UAT connection for multiple concurrent CodeBuild builds, you can
create multiple connections and use each connection independently.

**Possible solution:** If the UAT connection hasn't been used in the past 6 months, the connection will be invalidated by GitHub. To fix this, create a new connection.

**\*Possible cause:** You might have been using a UAT connection without installing the app.\*

**Recommended solution:** Though creating a UAT connection doesn't require associating the connection with a GitHub App installation,
an installation is required for the repository to be accessible. Follow the instructions to [review installations](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps "https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps") to make sure the GitHub App is installed. If it is not installed,
navigate to the [GitHub App's page](https://github.com/marketplace/aws-connector-for-github "https://github.com/marketplace/aws-connector-for-github") to install the app. For more information about UAT's access,
see [About user access tokens](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app#about-user-access-tokens "https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app#about-user-access-tokens").

### The AWS service's IAM role is missing necessary IAM permissions.

**Issue:** You see any of the following error messages:

- `Access denied to connection `<connection-arn>``
- `Failed to get access token from `<connection-arn>``

**Recommended solution:** Typically you use a connection with an AWS service, such as CodePipeline or CodeBuild.
When you give the AWS service an IAM role, the AWS service can use the role's permission to act on your behalf. Make sure the IAM role has
necessary permission. For more information about the necessary IAM permission, see [Grant CodeBuild
project IAM role access to use the connection](#connections-github-role-access "#connections-github-role-access") and [Identity and access management for AWS CodeStar Notifications and CodeConnections](../../../dtconsole/latest/userguide/security-iam.md "../../../dtconsole/latest/userguide/security-iam.md")
in the _Developer Tools console User Guide_.
