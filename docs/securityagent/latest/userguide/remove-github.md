

# Remove a GitHub integration
<a name="remove-github"></a>

Remove a GitHub integration when you no longer need AWS Security Agent to access repositories from a specific GitHub organization or user account. You must first uninstall the AWS Security Agent GitHub App from GitHub before removing the integration in the AWS Console.

## Prerequisites for removal
<a name="_prerequisites_for_removal"></a>

Before removing a GitHub integration, ensure you have:
+ Checked which Agent Spaces have repositories connected from this integration
+ Understood the impact: Removing this integration will break repository connections for code review, penetration testing context, and penetration test remediation across all Agent Spaces using repositories from this integration
+ GitHub organization admin access or user account owner access to uninstall the GitHub App

## Step 1: Uninstall the AWS Security Agent GitHub App from GitHub
<a name="remove-github-step-1"></a>

First, uninstall the AWS Security Agent GitHub App from your GitHub organization or user account.

 **For GitHub Organizations:** 

1. Go to github.com and open your organization page.

1. In the left sidebar, choose **Settings**.

1. Under **Code, planning, and automation**, choose **Installed GitHub Apps**.

1. Locate the **AWS Security Agent** app in the list.

1. Choose **Configure** next to the AWS Security Agent app.

1. Scroll to the bottom of the configuration page and choose **Uninstall**.

1. Confirm the uninstallation when prompted.

 **For GitHub User Accounts:** 

1. Go to github.com.

1. Choose your profile picture.

1. Choose **Settings**.

1. In the left sidebar, select **Applications**.

1. Open the **Installed GitHub Apps** tab.

1. Locate the **AWS Security Agent** app in the list.

1. Choose **Configure** next to the AWS Security Agent app.

1. Scroll to the bottom of the configuration page and choose **Uninstall**.

1. Confirm the uninstallation when prompted.

## Step 2: Remove the integration from AWS Security Agent
<a name="_step_2_remove_the_integration_from_aws_security_agent"></a>

After uninstalling the GitHub App, remove the integration registration from the AWS Console.

1. In the AWS Security Agent Management Console, navigate to **Integrations**.

1. Locate the GitHub integration you want to remove in the integrations list.

1. Select the integration by clicking on it.

1. Choose **Remove**.

1. Review the confirmation dialog, which warns you about the impact:
**Warning**  
Removing this integration will affect all Agent Spaces that have repositories connected from this GitHub organization or user account. This will break:  
Code review functionality for connected repositories
Penetration testing context from connected repositories
Penetration test remediation capabilities for connected repositories
Ensure you have uninstalled the AWS Security Agent GitHub App from GitHub before proceeding.

1. If you have not yet uninstalled the GitHub App from GitHub, you’ll receive a warning. Return to Step 1 to complete the uninstallation first.

1. If you have uninstalled the GitHub App and understand the impact, choose **Confirm removal**.

1. The integration is removed from your integrations list. Any Agent Spaces with repositories from this integration no longer have access to those repositories for code review, penetration testing context, or automated remediation.