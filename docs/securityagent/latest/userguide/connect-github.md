# Connect AWS Security Agent to GitHub repositories

Connect your AWS Security Agent to GitHub repositories to enable code review, threat modeling, penetration testing, and automated remediation capabilities. AWS Security Agent supports both cloud-hosted GitHub and cloud-hosted GitHub Enterprise. Before you begin, review [How integrations work with Agent Spaces](about-integrations.md "about-integrations.md") to understand how a registration is reused across Agent Spaces and shared across capabilities.

GitHub integration serves multiple purposes:

###### Note

This page covers cloud-hosted GitHub (github.com) and cloud-hosted GitHub Enterprise. For self-hosted GitHub Enterprise Server, see [Connect AWS Security Agent to GitHub Enterprise Server](connect-github-enterprise-server.md "connect-github-enterprise-server.md").

- **Code review** - Automatically analyze the code changes in each pull request against your organizational security requirements, and run on-demand full-repository scans
- **Threat modeling** - Provide application understanding by analyzing source code, data flows, and architecture
- **Penetration testing context** - Provide application understanding for penetration testing by analyzing source code
- **Automated remediation** - Submit pull requests with fixes for vulnerabilities discovered during security assessments
  Connecting GitHub to AWS Security Agent requires authorizing the AWS Security Agent GitHub App for your GitHub organization or user account, then registering the connection in the AWS Console.

## How GitHub integration works

**Pull request analysis** happens within GitHub. After you authorize the GitHub App, connect repositories, and enable code review comments in the AWS Management Console, AWS Security Agent automatically scans the changes in each new pull request (a differential scan of just the changed code) and posts findings as pull request comments.

You create and run **full code reviews** — which scan a repository’s entire codebase — in the AWS Security Agent web application, not in GitHub.

**Penetration testing** and **threat modeling** are initiated within the AWS Security Agent web application. Users select connected repositories to provide application context, and specify target domains for penetration testing. If you enable automated remediation, users can request AWS Security Agent to fix findings by opening pull requests to connected repositories.

## Prerequisites

Before you begin, ensure you have:

- GitHub organization admin access or GitHub user account owner access
- Permissions to configure integrations for your Agent Space in the AWS Management Console
- Understanding of which repositories you want to connect for code review, threat modeling, and penetration testing

###### Important

A GitHub App can only be installed once to a GitHub account or GitHub organization. If you need to connect the same GitHub organization to AWS Security Agent, you must use the same AWS account where the integration was first registered.

###### Note

If your GitHub enterprise organization has enabled IP allowlisting, you must accept the allowed IP addresses on the GitHub app. You can also choose to automatically add the IP addresses to your allow list. For more information, see [Allowing access by GitHub Apps](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps "https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps") and [Enabling allowed IP addresses](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#enabling-allowed-ip-addresses "https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#enabling-allowed-ip-addresses") in the GitHub documentation.

The following IP addresses are used to access your GitHub resources:

- US East (N. Virginia) (us-east-1)

  - `34.228.181.128`
  - `44.219.176.187`
  - `54.226.244.221`

- US West (Oregon) (us-west-2)

  - `34.212.16.133`
  - `52.89.67.212`
  - `54.187.135.61`

- Asia Pacific (Mumbai) (ap-south-1)

  - `13.126.209.199`
  - `13.234.6.24`
  - `35.154.102.216`

- Asia Pacific (Singapore) (ap-southeast-1)

  - `18.139.13.125`
  - `47.130.240.215`
  - `54.179.238.173`

- Asia Pacific (Sydney) (ap-southeast-2)

  - `13.237.95.197`
  - `13.238.84.102`
  - `52.64.174.242`

- Asia Pacific (Tokyo) (ap-northeast-1)

  - `13.192.12.233`
  - `35.74.181.230`
  - `57.183.50.158`

- Europe (Frankfurt) (eu-central-1)

  - `18.158.110.140`
  - `52.57.96.160`
  - `52.59.55.56`

- Europe (Ireland) (eu-west-1)

  - `34.251.85.24`
  - `52.30.157.157`
  - `52.51.192.222`

- South America (São Paulo) (sa-east-1)

  - `54.94.247.213`
  - `54.207.222.14`
  - `54.232.201.242`

## Authorize and register the AWS Security Agent GitHub App

Authorize the AWS Security Agent GitHub App to access your GitHub organization or user account, then register the connection in the AWS Console.

###### Important

Complete all steps in this process without closing your browser or navigating away. If the registration process is interrupted, you may need to uninstall the GitHub App and start over.

1. In the AWS Security Agent Management Console, navigate to **Integrations**.
2. Choose **Add integration**.
3. Select **GitHub**.
4. Choose **Next**.
5. Choose **Install and authorize**.

You are redirected to GitHub to complete the authorization. Ensure you’re logged into GitHub with an account that has admin access to the organization or user account you want to connect. 6. In GitHub, select the account or organization where you want to install the AWS Security Agent GitHub App. 7. Select which repositories AWS Security Agent can access:

    * **All repositories** - Grant access to all current and future repositories in the organization or user account
    * **Only select repositories** - Choose specific repositories from the dropdown. You can select multiple repositories one at a time.


    ###### Note

    You can modify repository access at any time by visiting the GitHub App settings in your GitHub organization or user account settings.

8. Choose **Install and authorize**. 9. You are redirected back to the AWS Management Console to complete the registration. 10. In the **Registration details** section, configure the following fields:

    1. **Registration name** - Enter a descriptive name for this GitHub connection. Use a name that identifies the GitHub organization or user account, such as "Acme-Corp-Org" or "Production-Repos".
    2. **Account type** - Select one of the following from the dropdown:




    	* **Organization** - If you connected a GitHub organization account
    	* **User** - If you connected a personal GitHub user account
    3. **Organization name** (appears only if you selected Organization) - Enter the exact name of your GitHub organization as it appears in GitHub.

11. Choose **Connect**. 12. You see a confirmation message and return to the Integrations page, where your new GitHub connection appears with its registration name. To connect additional GitHub organizations or user accounts, repeat this process by choosing **Add integration** again.

## Troubleshoot GitHub integration

If you encounter issues during the GitHub integration process, use the following guidance to resolve common problems.

### Unable to complete registration

If you were unable to complete the registration process (for example, your browser was closed, you navigated away from the registration page, or you encountered a session interruption), the AWS Security Agent GitHub App may be installed in your GitHub organization but not registered in the AWS Console.

**Symptoms:**

- When you try to authorize the GitHub App again, GitHub shows "Configure" instead of "Install"
- You cannot complete the registration in the AWS Console
- The integration does not appear in your Integrations list

**Resolution:**

1. Uninstall the AWS Security Agent GitHub App from your GitHub organization or user account.
2. Return to the AWS Security Agent console and start the integration process again from the beginning.

### Multiple AWS accounts trying to integrate the same GitHub organization

A GitHub App can only be installed once to a GitHub account or GitHub organization. If you need to use repositories from a GitHub organization that is already integrated with a different AWS Security Agent account, you must use the AWS account where the integration was first registered.

**Resolution:**

- Identify which AWS Security Agent account has the GitHub integration registered
- Use that AWS account to create Agent Spaces and connect repositories
- If you need to move the integration to a different AWS account, uninstall the GitHub App from the original AWS account first, then integrate it with the new account

## Next steps

After connecting GitHub to AWS Security Agent:

- Navigate to the Agent Space where you want to use these repositories
- Choose **Enable code review** or **Setup penetration testing** to connect specific repositories to your Agent Space and configure their usage (see [Enable code review](enable-code-review-scan.md "enable-code-review-scan.md") and [Enable penetration test](enable-penetration-test.md "enable-penetration-test.md"))
- Enable **Code review comments** to have AWS Security Agent analyze each pull request and post findings in GitHub (see [Review code security findings in pull requests](review-code-findings-github.md "review-code-findings-github.md"))
- Enable **Code remediation** to allow AWS Security Agent to submit pull requests with vulnerability fixes (see [Enable users to start remediation of penetration test and code review findings](enable-remediate-findings.md "enable-remediate-findings.md"))
- Create threat models from connected repositories in the web application (see [Enable threat modeling](enable-threat-model.md "enable-threat-model.md"))
- Review GitHub App permissions and repository access in your GitHub organization settings
