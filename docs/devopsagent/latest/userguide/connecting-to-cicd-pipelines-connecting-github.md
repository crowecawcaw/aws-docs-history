# Connecting GitHub

GitHub integration enables AWS DevOps Agent to access code repositories and receive deployment events during incident investigations. This integration follows a two-step process: account-level registration of GitHub, followed by connecting specific repositories to individual Agent Spaces.

AWS DevOps Agent supports both GitHub.com (SaaS) and GitHub Enterprise Server (self-hosted) instances.

## Prerequisites

Before connecting GitHub, ensure you have:

- Access to the AWS DevOps Agent admin console
- A GitHub user account or organization with admin permissions
- Authorization to install GitHub apps in your account or organization

For GitHub Enterprise Server, you also need:

- A GitHub Enterprise Server instance (version 3.x or later) accessible over HTTPS
- The HTTPS URL of your GitHub Enterprise Server instance (for example, `https://github.example.com`)
- (Optional) A private connection, if your GitHub Enterprise Server instance is not publicly accessible

## Registering GitHub (account-level)

GitHub is registered at the AWS account level and shared among all Agent Spaces in that account. You only need to register GitHub once per AWS account.

### Step 1: Navigate to pipeline providers

1. Sign in to the AWS Management Console
2. Navigate to the AWS DevOps Agent console
3. Go to the **Capabilities** tab
4. In the **Pipeline** section, click **Add**
5. Select **GitHub** from the list of available providers

If GitHub hasn't been registered yet, you'll be prompted to register it first.

### Step 2: Choose connection type

On the "Register GitHub Account / Organization" screen, select whether you're connecting as a user or organization:

- **User** – Your personal GitHub account with a username and profile
- **Organization** – A shared GitHub account where multiple people can collaborate across many projects at once

If you are connecting to a GitHub Enterprise Server instance, check the **Use GitHub Enterprise Server** checkbox and enter the HTTPS URL of your instance (for example, `https://github.example.com`).

If your GitHub Enterprise Server instance is not publicly accessible, you can optionally configure a private connection to allow AWS DevOps Agent to securely reach your instance. For more information, see [Connecting to privately hosted tools](configuring-capabilities-for-aws-devops-agent-connecting-to-privately-hosted-tools.md "configuring-capabilities-for-aws-devops-agent-connecting-to-privately-hosted-tools.md").

###### Note

Do not include `/api/v3` or any trailing path in the URL — enter only the base URL.

### Step 3: Set up the GitHub App

Click **Submit** to begin the app setup process. The next steps differ depending on whether you are connecting to GitHub.com or GitHub Enterprise Server.

#### For GitHub.com

1. You'll be redirected to GitHub to install the AWS DevOps Agent GitHub app.
2. Select which account or organization to install the app in.
3. The app allows AWS DevOps Agent to receive events from connected repositories, including deployment events.

#### For GitHub Enterprise Server

GitHub Enterprise Server uses a GitHub App Manifest flow, which automatically sets up a new GitHub App on your instance. This involves two redirects to your GitHub Enterprise Server instance.

1. Your browser will be redirected to your GitHub Enterprise Server instance's "Create GitHub App" page.
2. You'll see the app name pre-filled. Feel free to change the name as needed. Click **Create GitHub App**.
3. You'll be redirected back to AWS DevOps Agent, which exchanges the manifest code for app credentials.

### Step 4: Select repositories and complete installation

1. You'll see the **Install & Authorize** page for the GitHub App.
2. Select which repositories to allow the app to access:
   - **All repositories** – Grant access to all current and future repositories
   - **Only select repositories** – Choose specific repositories from your account or organization

3. Click **Install & Authorize**.
4. You'll be redirected back to the AWS DevOps Agent console, where GitHub will appear as registered at the account level.

## Connecting repositories to an Agent Space

After registering GitHub at the account level, you can connect specific repositories to individual Agent Spaces:

1. In the AWS DevOps Agent console, select your Agent Space
2. Go to the **Capabilities** tab
3. In the **Pipeline** section, click **Add**
4. Select **GitHub** from the list of available providers
5. Select the subset of repositories relevant to this Agent Space
6. Click **Add** to complete the connection

You can connect different sets of repositories to different Agent Spaces based on your organizational needs.

## Understanding the GitHub app

The AWS DevOps Agent GitHub app:

- Requests read-only access to your repositories
- Receives deployment events and other repository events
- Allows AWS DevOps Agent to correlate code changes with operational incidents
- Can be uninstalled at any time through your GitHub settings

For GitHub Enterprise Server, the GitHub App is automatically created on your instance during registration. You can manage the app's repository access or uninstall it through **Settings > Applications > Installed GitHub Apps**. To delete the app definition entirely, go to **Settings > Developer settings > GitHub Apps**.

## Managing GitHub connections

- **Updating repository access** – To change which repositories the GitHub app can access, go to your GitHub account or organization settings (or your GitHub Enterprise Server instance settings), navigate to installed GitHub apps, and modify the AWS DevOps Agent app configuration.
- **Viewing connected repositories** – In the AWS DevOps Agent console, select your Agent Space and go to the Capabilities tab to view connected repositories in the Pipeline section.
- **Removing GitHub connection** – To disconnect GitHub from an Agent Space, select the connection in the Pipeline section and click **Remove**. To uninstall the GitHub app completely, uninstall it from your GitHub account or organization settings. For GitHub Enterprise Server, because the GitHub App is created directly on your instance during registration, you can optionally clean up the app entirely by performing both of the following:
  - **Uninstall the app** – Go to **Settings > Applications > Installed GitHub Apps**, click **Configure** on the app, then uninstall it.
  - **Delete the app** – Go to **Settings > Developer settings > GitHub Apps**, select the app, go to the **Advanced** tab, and choose **Delete GitHub App**. **Warning:** Deleting the GitHub App is permanent and cannot be undone. If you delete it, you will need to re-register GitHub Enterprise Server from the beginning in the AWS DevOps Agent console to create a new app.
