# Connect AWS Security Agent to GitLab repositories

Connect your AWS Security Agent to GitLab Cloud repositories to enable code review, threat modeling, penetration testing, and automated remediation capabilities. Before you begin, review [How integrations work with Agent Spaces](about-integrations.md "about-integrations.md") to understand how a registration is reused across Agent Spaces and shared across capabilities.

GitLab integration serves multiple purposes:

- **Code review** - Automatically analyze merge requests against your organizational security requirements
- **Threat modeling** - Provide application understanding by analyzing source code, data flows, and architecture
- **Penetration testing context** - Provide application understanding for penetration testing by analyzing source code
- **Automated remediation** - Submit merge requests with fixes for vulnerabilities discovered during security assessments
  Connecting GitLab to AWS Security Agent requires providing a GitLab access token with the appropriate permissions, then registering the connection in the AWS Console.

## How GitLab integration works

**Code review** happens within GitLab. After you provide your access token and connect repositories in the AWS Management Console, you can enable code review for specific projects. AWS Security Agent will then automatically analyze merge requests in those projects. You review the findings directly in GitLab as merge request comments.

**Penetration testing** and **threat modeling** are initiated within the AWS Security Agent Web Application. Users specify target domains and select connected repositories to provide application context. If you enable automated remediation, users can request AWS Security Agent to fix findings by opening merge requests to connected repositories.

###### Note

Automated remediation is not available for public GitLab repositories to avoid disclosing vulnerabilities before they are fixed.

## Prerequisites

Before you begin, ensure you have:

- A GitLab.com account with Maintainer or Owner access to the projects you want to connect
- A GitLab access token with the scopes required for your connection type:

  - **Personal** - A personal access token with all read permissions and the `api` permission.
  - **Group** - A group access token with the `read_api` and `read_repository` scopes.

- Permissions to configure integrations in the AWS Security Agent Management Console

###### Important

Set the token expiration to a maximum of 365 days after the current date.

###### Note

GitLab Personal Access Tokens can be used across multiple AWS accounts. Unlike GitHub and Atlassian integrations, there is no restriction on connecting the same GitLab account to multiple AWS Security Agent instances.

## Register a GitLab connection

1. In the AWS Security Agent Management Console, navigate to **Integrations**.
2. Choose **Add integration**.
3. Select **GitLab**, then choose **Next**.
4. Under **Choose an account type**, select one of the following:

   - **Personal** - Connect your individual GitLab user account.
   - **Group** - Connect a GitLab group that contains multiple projects. Enter your **Group ID**.

5. In the **Access token** field, paste your GitLab access token.
6. In the **Registration name** field, enter a descriptive name for this connection, such as `Engineering-Team-GitLab`. Valid characters are letters, numbers, periods, underscores, and hyphens.
7. Choose **Connect**.

You return to the **Integrations** page, where the new connection appears with its registration name.

## Troubleshoot GitLab integration

If you encounter issues during the GitLab integration process, use the following guidance to resolve common problems.

### Invalid or expired token

#### Symptoms

- Integration fails to connect
- Previously working integration stops functioning
- Error message indicating authentication failure

#### Resolution

1. In GitLab, navigate to your user settings and select **Access Tokens**.
2. Verify your token has not expired.
3. Verify the token has the required scopes for its type.
4. If the token has expired, create a new token and update the integration in the AWS Console.

### Rate limiting

#### Symptoms

- Intermittent failures during code review
- Delayed merge request analysis

#### Resolution

- GitLab applies rate limits to API requests. If you have a large number of repositories or frequent merge requests, some requests may be throttled.
- Wait for the rate limit window to reset, or contact GitLab support to increase your rate limits.

## Next steps

After connecting GitLab to AWS Security Agent:

- Navigate to the Agent Space where you want to use these repositories
- Choose **Enable code review** or **Setup penetration testing** to connect specific projects to your Agent Space and configure their usage
- Enable **Code remediation** to allow AWS Security Agent to submit merge requests with vulnerability fixes
- For privately hosted GitLab instances, see [Connect AWS Security Agent to GitLab Self-Managed](connect-gitlab-self-managed.md "connect-gitlab-self-managed.md")
