# Connecting GitHub

GitHub integration enables AWS DevOps Agent to access code repositories and receive deployment events during incident investigations. This integration follows a two-step process: account-level registration of GitHub, followed by connecting specific repositories to individual Agent Spaces.

## Prerequisites

Before connecting GitHub, ensure you have:

- Access to the AWS DevOps Agent admin console
- A GitHub user account or organization with admin permissions
- Authorization to install GitHub apps in your account or organization

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

### Step 3: Complete GitHub OAuth flow

1. Click **Submit** to initiate the GitHub authentication flow
2. You'll be redirected to GitHub to install the AWS DevOps Agent GitHub app
3. Select which account or organization to install the app in
4. The app allows AWS DevOps Agent to receive events from connected repositories, including deployment events

### Step 4: Select repositories

Choose which repositories to allow the app to access:

- **All repositories** – Grant access to all current and future repositories
- **Select repositories** – Choose specific repositories from your account or organization

### Step 5: Complete installation

After selecting repositories, complete the GitHub app installation. You'll be redirected back to the AWS DevOps Agent console, where GitHub will appear as registered at the account level.

## Connecting repositories to an Agent Space

After registering GitHub at the account level, you can connect specific repositories to individual Agent Spaces:

1. In the AWS DevOps Agent console, select your Agent Space
2. Go to the **Capabilities** tab
3. In the **Pipeline** section, click **Add**
4. Select **GitHub** from the list of available providers
5. Select the subset of repositories relevant to this Agent Space
6. Click **Add** to complete the connection

You can connect different sets of repositories to different Agent Spaces based on your organizational needs.

### Associating AWS resources with project deployments

See [Associating AWS resources with project deployments](configuring-capabilities-for-aws-devops-agent-connecting-to-cicd-pipelines-associating-aws-resources-with-project-deployments.md "configuring-capabilities-for-aws-devops-agent-connecting-to-cicd-pipelines-associating-aws-resources-with-project-deployments.md") to associate deployments with AWS resources. This helps incident investigations correlate recent deployments with possible root causes.

## Understanding the GitHub app

The AWS DevOps Agent GitHub app:

- Requests read-only access to your repositories
- Receives deployment events and other repository events
- Allows AWS DevOps Agent to correlate code changes with operational incidents
- Can be uninstalled at any time through your GitHub settings

## Managing GitHub connections

- **Updating repository access** – To change which repositories the GitHub app can access, go to your GitHub account or organization settings, navigate to installed GitHub apps, and modify the AWS DevOps Agent app configuration.
- **Viewing connected repositories** – In the AWS DevOps Agent console, select your Agent Space and go to the Capabilities tab to view connected repositories in the Pipeline section.
- **Removing GitHub connection** – To disconnect GitHub from an Agent Space, select the connection in the Pipeline section and click **Remove**. To uninstall the GitHub app completely, uninstall it from your GitHub account or organization settings.
