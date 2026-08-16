# Connect AWS Security Agent to GitLab repositories

Connect your AWS Security Agent to GitLab Cloud repositories to enable code review, threat modeling, penetration testing, and automated remediation capabilities. Before you begin, review [How integrations work with Agent Spaces](about-integrations.md "about-integrations.md") to understand how a registration is reused across Agent Spaces and shared across capabilities.

GitLab integration serves multiple purposes:

- **Code review** - Automatically analyze the code changes in each merge request against your organizational security requirements, and run on-demand full-repository scans
- **Threat modeling** - Provide application understanding by analyzing source code, data flows, and architecture
- **Penetration testing context** - Provide application understanding for penetration testing by analyzing source code
- **Automated remediation** - Submit merge requests with fixes for vulnerabilities discovered during security assessments
  Connecting GitLab to AWS Security Agent requires providing a GitLab access token with the appropriate permissions, then registering the connection in the AWS Console.

## How GitLab integration works

**Merge request analysis** happens within GitLab. After you provide your access token, connect projects, and enable code review comments in the AWS Management Console, AWS Security Agent automatically scans the changes in each new merge request (a differential scan of just the changed code) and posts findings as merge request comments.

You create and run **full code reviews** — which scan a project’s entire codebase — in the AWS Security Agent web application, not in GitLab.

**Penetration testing** and **threat modeling** are initiated within the AWS Security Agent web application. Users specify target domains and select connected repositories to provide application context. If you enable automated remediation, users can request AWS Security Agent to fix findings by opening merge requests to connected repositories.

###### Note

Automated remediation is not available for public GitLab repositories to avoid disclosing vulnerabilities before they are fixed.

## Prerequisites

Before you begin, ensure you have:

- A GitLab.com account with Maintainer or Owner access to the projects you want to connect
- A GitLab access token with the scopes required for your connection type:

  - **Personal** - A personal access token with all read permissions and the `api` permission.
  - **Group** - A group access token with the `read_api` and `read_repository` scopes.

- Permissions to configure integrations in the AWS Security Agent Management Console

###### Note

Keep the following in mind when you create your GitLab access token:

- **Scope** – The `read_api` scope is sufficient only for read-only operations, such as listing repositories. The full `api` scope is required for any operation that writes to GitLab, including posting code review comments on merge requests and automated remediation (creating merge requests). The `read_repository` and `write_repository` scopes grant Git-over-HTTPS access only. They do **not** grant REST API access, and a token with only those scopes returns `401 Unauthorized` for API operations.
- **Expiration** – Set the token expiration to a maximum of 365 days after the current date.
- **Reuse across accounts** – GitLab Personal Access Tokens can be used across multiple AWS accounts.

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

- Integration fails to connect during registration
- Registration succeeds, but a later operation (such as listing repositories, `ListResourcesFromIntegration`, code review, or remediation) fails
- A previously working integration stops functioning
- An error that includes `GITLAB authentication failed: Invalid or expired token`, or the GitLab API response `{"message":"401 Unauthorized"}`

#### Resolution

1. In GitLab, navigate to your user settings and select **Access Tokens**.
2. Verify the token has not expired. GitLab returns `401 Unauthorized` for expired, revoked, or malformed tokens.
3. Verify the token has the scopes required for the operations you use (see [Missing or insufficient token scope](#gitlab-token-scopes "#gitlab-token-scopes")).
4. If the token has expired or was revoked, create a new token and update the integration in the AWS Console.

###### Tip

To confirm whether a token is valid independently of AWS Security Agent, call the GitLab REST API directly. A valid token returns HTTP 200 with a JSON list; an invalid, expired, or wrong-scope token returns `{"message":"401 Unauthorized"}`.

```
curl --header "PRIVATE-TOKEN: <your-token>" https://gitlab.example.com/api/v4/projects
```

### Missing or insufficient token scope

A token can be valid and unexpired but still return `401 Unauthorized` if it lacks the scopes required for the operation. This most commonly happens when a repository-only token (created for Git operations) is reused for API operations.

#### Symptoms

- Registration or `ListResourcesFromIntegration` returns `401 Unauthorized` even though the token is current
- Reading repositories works, but posting code review comments or creating merge requests fails

#### Resolution

Select scopes based on the capabilities you need:

| Capability                                                                                     | Minimum scope | Notes                                                                                                 |
| ---------------------------------------------------------------------------------------------- | ------------- | ----------------------------------------------------------------------------------------------------- |
| List and read repositories (threat modeling, penetration testing context)                      | `read_api`    | Read-only access to the REST API.                                                                     |
| Post code review comments and automated remediation (create merge requests, push fix branches) | `api`         | Full read/write API access. The `api` scope is a superset that also covers Git read/write over HTTPS. |

###### Important

The `read_repository` and `write_repository` scopes grant Git-over-HTTPS access only. They do **not** grant REST API access, so a token with only those scopes returns `401 Unauthorized` for API operations such as listing resources. Use `read_api` or `api` for API access.

### Group access token requires a paid GitLab.com tier

On GitLab.com, group access tokens are available only with a Premium or Ultimate subscription, and not on a trial. The integration supports the **Personal** and **Group** account types only. It does not support project access tokens, which on GitLab.com also require a Premium or Ultimate subscription.

#### Symptoms

- You cannot create a group access token in GitLab on a free GitLab.com namespace.
- Registration fails when you select the **Group** account type with a free GitLab.com namespace.

#### Resolution

- On a free GitLab.com namespace, select the **Personal** account type and use a personal access token, which is available on all tiers.
- To use the **Group** account type, upgrade the group’s namespace to Premium or Ultimate, then create a group access token with the `read_api` and `read_repository` scopes.
- On GitLab self-managed, group access token availability depends on your instance’s license tier.

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
- Choose **Enable code review** or **Setup penetration testing** to connect specific projects to your Agent Space and configure their usage (see [Enable code review](enable-code-review-scan.md "enable-code-review-scan.md") and [Enable penetration test](enable-penetration-test.md "enable-penetration-test.md"))
- Enable **Code review comments** to have AWS Security Agent analyze each merge request and post findings in GitLab (see [Review code security findings in pull requests](review-code-findings-github.md "review-code-findings-github.md"))
- Enable **Code remediation** to allow AWS Security Agent to submit merge requests with vulnerability fixes (see [Enable users to start remediation of penetration test and code review findings](enable-remediate-findings.md "enable-remediate-findings.md"))
- Create threat models from connected projects in the web application (see [Enable threat modeling](enable-threat-model.md "enable-threat-model.md"))
- For privately hosted GitLab instances, see [Connect AWS Security Agent to GitLab Self-Managed](connect-gitlab-self-managed.md "connect-gitlab-self-managed.md")
