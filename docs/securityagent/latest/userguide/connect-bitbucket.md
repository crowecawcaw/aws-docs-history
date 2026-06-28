# Connect AWS Security Agent to Bitbucket repositories

Connect your AWS Security Agent to Bitbucket Cloud repositories to enable code review, threat modeling, penetration testing, and automated remediation capabilities. Bitbucket integration serves multiple purposes:

- **Code review** - Automatically analyze pull requests against your organizational security requirements
- **Threat modeling** - Provide application understanding by analyzing source code, data flows, and architecture
- **Penetration testing context** - Provide application understanding for penetration testing
- **Automated remediation** - Submit pull requests with fixes for vulnerabilities discovered during security assessments
  Connecting Bitbucket to AWS Security Agent requires installing the AWS Security Agent Forge app on your Atlassian site and completing the OAuth authorization flow.

###### Note

AWS Security Agent supports Bitbucket Cloud only. Bitbucket Server and Bitbucket Data Center are not supported.

## How Bitbucket integration works

**Code review** happens within Bitbucket. After you install the Forge app and connect repositories in the AWS Management Console, you can enable code review for specific repositories. AWS Security Agent will then automatically analyze pull requests in those repositories. You review the findings directly in Bitbucket as pull request comments.

**Penetration testing** and **threat modeling** are initiated within the AWS Security Agent Web Application. Users specify target domains and select connected repositories to provide application context.

###### Note

Automated remediation is not available for public Bitbucket repositories to avoid disclosing vulnerabilities before they are fixed.

## Prerequisites

Before you begin, ensure you have:

- A Bitbucket Cloud workspace with admin access
- An Atlassian account with site administrator privileges
- Permissions to configure integrations for your Agent Space in the AWS Management Console
- The installation ID from the AWS Security Agent Forge app (see [Find your Atlassian installation ID](find-atlassian-installation-id.md "find-atlassian-installation-id.md"))

###### Important

One Atlassian site can only be associated with one AWS account per region. If you need to connect the same Bitbucket site to AWS Security Agent in a different AWS account within the same region, you must first remove the existing integration.

###### Note

Atlassian Forge app pricing applies to this integration. For more information, see [Forge platform pricing](https://developer.atlassian.com/platform/forge/forge-platform-pricing/ "https://developer.atlassian.com/platform/forge/forge-platform-pricing/") in the Atlassian documentation.

For more information about finding your installation ID, see [Find your Atlassian installation ID](find-atlassian-installation-id.md "find-atlassian-installation-id.md").

## Register a Bitbucket connection

1. In the AWS Security Agent Management Console, navigate to **Integrations**.
2. Choose **Add integration**.
3. Select **Bitbucket**.
4. Choose **Next**.
5. Choose **Install and authorize**.

You’ll be redirected to Atlassian to install the Forge app and authorize access. 6. On the Atlassian consent screen, review the permissions and authorize the AWS Security Agent app. The following permissions are requested:

    * Read and write pull requests
    * Read and write repository content

7. You’ll be redirected back to the AWS Management Console to complete the registration. 8. In the **Registration details** section, configure the following fields:

    1. **Installation ID** - Paste the installation ID you copied from the Forge app in Bitbucket (see [Find your Atlassian installation ID](find-atlassian-installation-id.md "find-atlassian-installation-id.md")).
    2. **Registration name** - Enter a descriptive name for this Bitbucket connection, such as "Acme-Engineering-Bitbucket".

9. Choose **Connect**.

## Troubleshoot Bitbucket integration

If you encounter issues during the Bitbucket integration process, use the following guidance to resolve common problems.

### Unable to complete registration

If the registration process is interrupted (browser closed, session timeout), the Forge app may be installed on your Atlassian site but not registered in the AWS Console.

#### Resolution

- Return to the AWS Security Agent console and restart the integration process.
- The Forge app remains installed and does not need to be reinstalled.

### Site already connected to another AWS account

#### Symptoms

- Error indicating the Atlassian site is already associated with another account

#### Resolution

- One Atlassian site can only be connected to one AWS account per region.
- Identify which AWS account has the existing integration and use that account, or remove the existing integration first.

## Next steps

After connecting Bitbucket to AWS Security Agent:

- Navigate to the Agent Space where you want to use these repositories
- Choose **Enable code review** or **Setup penetration testing** to connect specific repositories to your Agent Space
- Enable automated remediation to allow AWS Security Agent to submit pull requests with vulnerability fixes
