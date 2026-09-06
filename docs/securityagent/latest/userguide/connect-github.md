

# Connect AWS Security Agent to GitHub repositories
<a name="connect-github"></a>

Connect your AWS Security Agent to GitHub repositories to enable code review, threat modeling, penetration testing, and automated remediation capabilities. AWS Security Agent supports both cloud-hosted GitHub and cloud-hosted GitHub Enterprise. Before you begin, review [How integrations work with Agent Spaces](about-integrations.md) to understand how a registration is reused across Agent Spaces and shared across capabilities.

GitHub integration serves multiple purposes:

**Note**  
This page covers cloud-hosted GitHub (github.com) and cloud-hosted GitHub Enterprise. For self-hosted GitHub Enterprise Server, see [Connect AWS Security Agent to GitHub Enterprise](connect-github-enterprise.md).
+  **Continuum for code review** - Automatically analyze the code changes in each pull request against your organizational security requirements, and run on-demand full-repository scans
+  **Continuum for threat modeling** - Provide application understanding by analyzing source code, data flows, and architecture
+  **Continuum for penetration testing context** - Provide application understanding for penetration testing by analyzing source code
+  **Continuum for automated remediation** - Submit pull requests with fixes for vulnerabilities discovered during security assessments

Connecting GitHub to AWS Security Agent requires authorizing the AWS Security Agent GitHub App for your GitHub organization or user account, then registering the connection in the AWS Console.

## How GitHub integration works
<a name="_how_github_integration_works"></a>

 **Pull request analysis** happens within GitHub. After you authorize the GitHub App, connect repositories, and enable code review comments in the AWS Management Console, AWS Security Agent automatically scans the changes in each new pull request (a differential scan of just the changed code) and posts findings as pull request comments.

You create and run **full code reviews** — which scan a repository’s entire codebase — in the AWS Security Agent web application, not in GitHub.

 **Penetration testing** and **threat modeling** are initiated within the AWS Security Agent web application. Users select connected repositories to provide application context, and specify target domains for penetration testing. If you enable automated remediation, users can request AWS Security Agent to fix findings by opening pull requests to connected repositories.

## Prerequisites
<a name="connect-github-prerequisites"></a>

Before you begin, ensure you have:
+ GitHub organization admin access or GitHub user account owner access
+ Permissions to configure integrations for your Agent Space in the AWS Management Console
+ Understanding of which repositories you want to connect for code review, threat modeling, and penetration testing

**Important**  
Multiple AWS accounts can connect to the same GitHub organization or user account. Each account gets an independent integration. However, only one account can enable **Code review comments** or **Code remediation** per repository. If a second account tries to enable these features for a repository already owned by another account, it receives the error "Code review comments or code remediation is already enabled for this repository by another account."

**Important**  
Your GitHub organization might use an IP allow list. If so, add the AWS Security Agent IP addresses for your AWS Region to the IP allow list. Wait a few minutes for GitHub to apply them, then register the integration. For the IP addresses, see [AWS Security Agent IP addresses](about-integrations.md#agent-ip-addresses).  
Do not rely on the GitHub **Enable IP allow list configuration for installed GitHub Apps** setting. This setting adds IP addresses only for app-installation requests, not for the requests that AWS Security Agent makes during registration. As a result, registration fails even when those addresses appear in your IP allow list.  
For more information about enabling allowed IP addresses for your GitHub organization, see [Enabling allowed IP addresses](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#enabling-allowed-ip-addresses) in the GitHub documentation.

## Authorize and register the AWS Security Agent GitHub App
<a name="_authorize_and_register_the_aws_security_agent_github_app"></a>

Authorize the AWS Security Agent GitHub App to access your GitHub organization or user account, then register the connection in the AWS Console.

**Important**  
Complete all steps in this process without closing your browser or navigating away. If the registration process is interrupted, you may need to uninstall the GitHub App and start over.

1. In the AWS Security Agent Management Console, navigate to **Integrations**.

1. Choose **Add integration**.

1. Select **GitHub**.

1. Choose **Next**.

1. Choose **Install and authorize**.

   You are redirected to GitHub to complete the authorization. Ensure you’re logged into GitHub with an account that has admin access to the organization or user account you want to connect.

1. In GitHub, select the account or organization where you want to install the AWS Security Agent GitHub App.

1. Select which repositories AWS Security Agent can access:
   +  **All repositories** - Grant access to all current and future repositories in the organization or user account
   +  **Only select repositories** - Choose specific repositories from the dropdown. You can select multiple repositories one at a time.
**Note**  
You can modify repository access at any time by visiting the GitHub App settings in your GitHub organization or user account settings.

1. Choose **Install and authorize**.

1. You are redirected back to the AWS Management Console to complete the registration.

1. In the **Registration details** section, configure the following fields:

   1.  **Registration name** - Enter a descriptive name for this GitHub connection. Use a name that identifies the GitHub organization or user account, such as "Acme-Corp-Org" or "Production-Repos".

   1.  **Account type** - Select one of the following from the dropdown:
      +  **Organization** - If you connected a GitHub organization account
      +  **User** - If you connected a personal GitHub user account

   1.  **Organization name** (appears only if you selected Organization) - Enter the exact name of your GitHub organization as it appears in GitHub.

1. Choose **Connect**.

1. You see a confirmation message and return to the Integrations page, where your new GitHub connection appears with its registration name. To connect additional GitHub organizations or user accounts, repeat this process by choosing **Add integration** again.

## Troubleshoot GitHub integration
<a name="_troubleshoot_github_integration"></a>

If you encounter issues during the GitHub integration process, use the following guidance to resolve common problems.

### Unable to complete registration
<a name="_unable_to_complete_registration"></a>

If you were unable to complete the registration process (for example, your browser was closed, you navigated away from the registration page, or you encountered a session interruption), the AWS Security Agent GitHub App may be installed in your GitHub organization but not registered in the AWS Console.

 **Symptoms:** 
+ When you try to authorize the GitHub App again, GitHub shows "Configure" instead of "Install"
+ You cannot complete the registration in the AWS Console
+ The integration does not appear in your Integrations list

 **Resolution:** 

1. Uninstall the AWS Security Agent GitHub App from your GitHub organization or user account.

1. Return to the AWS Security Agent console and start the integration process again from the beginning.

### Registration fails when you enable an IP allow list
<a name="_registration_fails_when_you_enable_an_ip_allow_list"></a>

**Symptoms**  
Registration fails with an error such as "Security token validation error. Please try again." or "Access Denied." The failure occurs even when the AWS Security Agent IP addresses already appear in your IP allow list. The GitHub **Enable IP allow list configuration for installed GitHub Apps** setting added them automatically.

**Resolution**  
Manually add the AWS Security Agent IP addresses for your AWS Region (see [AWS Security Agent IP addresses](about-integrations.md#agent-ip-addresses)) to your organization’s IP allow list. Wait a few minutes for GitHub to apply them, then register the integration again.

### Multiple AWS accounts connecting to the same GitHub organization
<a name="_multiple_aws_accounts_connecting_to_the_same_github_organization"></a>

Multiple AWS accounts can connect to the same GitHub organization or user account. When a second account connects to a GitHub organization where the app is already installed, GitHub shows only the authorization page—no re-installation is needed. The user authorizes and receives an independent integration.

However, only one account can enable **Code review comments** or **Code remediation** per repository. If a second account tries to enable these features for a repository that is already owned by another account, it receives an error: "Code review comments or code remediation is already enabled for this repository by another account."

 **Resolution:** 
+ On-demand features (code review, penetration testing, threat modeling) work for all connected accounts regardless of ownership.
+ To transfer automated scanning ownership, the current owner must disable code review comments for the repository. The new account can then enable it.
+ All accounts can list and access repositories from the shared GitHub organization independently.

## Next steps
<a name="_next_steps"></a>

After connecting GitHub to AWS Security Agent:
+ Navigate to the Agent Space where you want to use these repositories
+ Choose **Enable code review** or **Setup penetration testing** to connect specific repositories to your Agent Space and configure their usage (see [Enable code review](enable-code-review-scan.md) and [Enable penetration test](enable-penetration-test.md))
+ Enable **Code review comments** to have AWS Security Agent analyze each pull request and post findings in GitHub (see [Review code security findings in pull requests](review-code-findings-github.md))
+ Enable **Code remediation** to allow AWS Security Agent to submit pull requests with vulnerability fixes (see [Enable users to start remediation of penetration test and code review findings](enable-remediate-findings.md))
+ Create threat models from connected repositories in the web application (see [Enable threat modeling](enable-threat-model.md))
+ Review GitHub App permissions and repository access in your GitHub organization settings