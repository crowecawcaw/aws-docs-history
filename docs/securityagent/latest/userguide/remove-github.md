# Remove a GitHub integration

Remove a GitHub integration when you no longer need AWS Security Agent to access repositories from a specific GitHub organization or user account. You must first uninstall the AWS Security Agent GitHub App from GitHub before removing the integration in the AWS Console.

## Prerequisites for removal

Before removing a GitHub integration, ensure you have:

- Checked which Agent Spaces have repositories connected from this integration
- Understood the impact: Removing this integration will break repository connections for code review, penetration testing context, and penetration test remediation across all Agent Spaces using repositories from this integration
- GitHub organization admin access or user account owner access to uninstall the GitHub App

## Step 1: Uninstall the AWS Security Agent GitHub App from GitHub

First, uninstall the AWS Security Agent GitHub App from your GitHub organization or user account.

**For GitHub Organizations:**

1. Go to github.com and open your organization page.
2. In the left sidebar, click **Settings**.
3. Under **Code, planning, and automation**, click **Installed GitHub Apps**.
4. Locate the **AWS Security Agent** app in the list.
5. Click **Configure** next to the AWS Security Agent app.
6. Scroll to the bottom of the configuration page and click **Uninstall**.
7. Confirm the uninstallation when prompted.

**For GitHub User Accounts:**

1. Go to github.com.
2. Click your profile picture in the top-right corner.
3. Click **Settings**.
4. In the left sidebar, select **Applications**.
5. Open the **Installed GitHub Apps** tab.
6. Locate the **AWS Security Agent** app in the list.
7. Click **Configure** next to the AWS Security Agent app.
8. Scroll to the bottom of the configuration page and click **Uninstall**.
9. Confirm the uninstallation when prompted.

## Step 2: Remove the integration from AWS Security Agent

After uninstalling the GitHub App, remove the integration registration from the AWS Console.

1. In the AWS Security Agent Management Console, navigate to **Integrations**.
2. Locate the GitHub integration you want to remove in the integrations list.
3. Select the integration by clicking on it.
4. Click **Remove**.
5. Review the confirmation dialog, which warns you about the impact:

###### Warning

Removing this integration will affect all Agent Spaces that have repositories connected from this GitHub organization or user account. This will break:

    * Code review functionality for connected repositories
    * Penetration testing context from connected repositories
    * Penetration test remediation capabilities for connected repositoriesEnsure you have uninstalled the AWS Security Agent GitHub App from GitHub before proceeding.

6. If you have not yet uninstalled the GitHub App from GitHub, you’ll receive a warning. Return to Step 1 to complete the uninstallation first.
7. If you have uninstalled the GitHub App and understand the impact, click **Confirm removal**.
8. The integration will be removed from your integrations list. Any Agent Spaces with repositories from this integration will no longer have access to those repositories for code review, penetration testing context, or automated remediation.
