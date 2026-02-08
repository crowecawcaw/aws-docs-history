# Connect AWS Security Agent to GitHub repositories

Connect your AWS Security Agent to GitHub repositories to enable code review and penetration testing capabilities. AWS Security Agent supports both cloud-hosted GitHub and cloud-hosted GitHub Enterprise. GitHub integration serves multiple purposes:

- **Code review** - Automatically analyze pull requests against your organizational security requirements
- **Penetration testing context** - Provide application understanding by analyzing source code, data flows, and architecture
- **Automated remediation** - Submit pull requests with fixes for vulnerabilities discovered during penetration testing
  Connecting GitHub to AWS Security Agent requires authorizing the AWS Security Agent GitHub App for your GitHub organization or user account, then registering the connection in the AWS Console.

## How GitHub integration works

**Code review** happens within GitHub. After you authorize the GitHub App and connect repositories in the AWS Management Console, you can enable code review for specific repositories. AWS Security Agent will then automatically analyze pull requests in those repositories. You review the findings directly in GitHub as pull request comments.

**Penetration testing** is initiated within the AWS Security Agent Web Application. Users specify target domains and select connected repositories to provide application context. If you enable automated remediation, users can request AWS Security Agent to fix findings by opening pull requests to connected repositories.

## Prerequisites

Before you begin, ensure you have:

- GitHub organization admin access or GitHub user account owner access
- Permissions to configure integrations for your Agent Space in the AWS Management Console
- Understanding of which repositories you want to connect for code review and penetration testing

###### Important

A GitHub App can only be installed once to a GitHub account or GitHub organization. If you need to connect the same GitHub organization to AWS Security Agent, you must use the same AWS account where the integration was first registered.

###### Note

If your GitHub enterprise organization has enabled IP allowlisting, you must accept the allowed IP addresses on the GitHub app. You can also choose to automatically add the IP addresses to your allow list. For more information, see [Allowing access by GitHub Apps](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps "https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps") and [Enabling allowed IP addresses](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#enabling-allowed-ip-addresses "https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#enabling-allowed-ip-addresses") in the GitHub documentation.

The following IP addresses are used to access your GitHub resources:

```
34.228.181.128
44.219.176.187
54.226.244.221
```

## Authorize and register the AWS Security Agent GitHub App

Authorize the AWS Security Agent GitHub App to access your GitHub organization or user account, then register the connection in the AWS Console.

###### Important

Complete all steps in this process without closing your browser or navigating away. If the registration process is interrupted, you may need to uninstall the GitHub App and start over.

1. In the AWS Security Agent Management Console, navigate to **Integrations**.
2. Click **Add integration**.
3. Select **GitHub**.
4. Click **Next**.
5. Click **Install and authorize**.

You’ll be redirected to GitHub to complete the authorization. Ensure you’re logged into GitHub with an account that has admin access to the organization or user account you want to connect. 6. In GitHub, select the account or organization where you want to install the AWS Security Agent GitHub App. 7. Select which repositories AWS Security Agent can access:

    * **All repositories** - Grant access to all current and future repositories in the organization or user account
    * **Only select repositories** - Choose specific repositories from the dropdown. You can select multiple repositories one at a time.


    ###### Note

    You can modify repository access at any time by visiting the GitHub App settings in your GitHub organization or user account settings.

8. Click **Install and authorize**.
9. You’ll be redirected back to the AWS Management Console to complete the registration.
10. In the **Registration details** section, configure the following fields:
    1. **Registration name** - Enter a descriptive name for this GitHub connection. Use a name that identifies the GitHub organization or user account, such as "Acme-Corp-Org" or "Production-Repos".
    2. **Account type** - Select one of the following from the dropdown:
       - **Organization** - If you connected a GitHub organization account
       - **User** - If you connected a personal GitHub user account

    3. **Organization name** (appears only if you selected Organization) - Enter the exact name of your GitHub organization as it appears in GitHub.

11. Click **Connect**.
12. You’ll see a confirmation message and return to the Integrations page, where your new GitHub connection appears with its registration name. To connect additional GitHub organizations or user accounts, repeat this process by clicking **Add integration** again.

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
- Click **Enable code review** or **Setup penetration testing** to connect specific repositories to your Agent Space and configure their usage
- Enable automated remediation to allow AWS Security Agent to submit pull requests with vulnerability fixes
- Review GitHub App permissions and repository access in your GitHub organization settings
