# Connect AWS Security Agent to GitLab Self-Managed

Connect your AWS Security Agent to a GitLab Self-Managed instance to enable code review, threat modeling, penetration testing, and automated remediation capabilities for repositories hosted on your own infrastructure.

GitLab Self-Managed integration works the same as GitLab Cloud (see [Connect AWS Security Agent to GitLab repositories](connect-gitlab.md "connect-gitlab.md")) with additional configuration for network connectivity to your private instance. Before you begin, review [How integrations work with Agent Spaces](about-integrations.md "about-integrations.md") to understand how a registration is reused across Agent Spaces and shared across capabilities.

###### Note

GitLab Self-Managed is registered through the **GitLab** integration, not a separate integration type. In the registration flow you select **Use GitLab self-hosted endpoint** and provide your instance URL. The cloud-hosted GitLab flow is described in [Connect AWS Security Agent to GitLab repositories](connect-gitlab.md "connect-gitlab.md").

## Prerequisites

Before you begin, ensure you have:

- A GitLab Self-Managed instance that is either:

  - Publicly accessible over the internet, OR
  - Accessible via a private connection (see [Connect to privately hosted source control](connect-private-connection.md "connect-private-connection.md"))

- A GitLab access token with the scopes required for your connection type:

  - **Personal** - A personal access token with all read permissions and the `api` permission.
  - **Group** - A group access token with the `read_api` and `read_repository` scopes.

- Maintainer or Owner access to the projects you want to connect
- Your GitLab instance must serve HTTPS traffic with a minimum TLS version of 1.2

###### Note

If your GitLab Self-Managed instance uses TLS certificates issued by a private certificate authority, you can provide the PEM-encoded public key of the certificate when creating a private connection. This allows AWS Security Agent to trust the TLS connection to your instance.

## Register a GitLab Self-Managed connection

1. In the AWS Security Agent Management Console, navigate to **Integrations**.
2. Choose **Add integration**.
3. Select **GitLab**, then choose **Next**.
4. Under **Choose an account type**, select **Personal** or **Group**. If you select **Group**, enter your **Group ID**.
5. Select **Use GitLab self-hosted endpoint**.
6. In the **GitLab self-hosted endpoint URL** field, enter the URL of your instance, for example `https://gitlab.example.com`.
7. If your instance is not publicly accessible, select **Connect to endpoint using a private connection**, then choose an existing private connection or create a new one. See [Connect to privately hosted source control](connect-private-connection.md "connect-private-connection.md").
8. In the **Access token** field, paste your GitLab access token.
9. In the **Registration name** field, enter a descriptive name for this connection. Valid characters are letters, numbers, periods, underscores, and hyphens.
10. Choose **Connect**.

You return to the **Integrations** page, where the new connection appears with its registration name.

## Private connectivity

If your GitLab Self-Managed instance is not publicly accessible, you must create a private connection before registering the integration. See [Connect to privately hosted source control](connect-private-connection.md "connect-private-connection.md") for detailed instructions.

###### Important

Service-managed private connections require the GitLab Self-Managed instance to be running in the **same AWS account** where the Agent Space is created. For cross-account access, use a self-managed private connection where you provide your own VPC Lattice resource configuration.

## Troubleshoot GitLab Self-Managed integration

In addition to the troubleshooting steps in [Connect AWS Security Agent to GitLab repositories](connect-gitlab.md "connect-gitlab.md"), the following issues are specific to self-managed instances:

### Instance unreachable

#### Symptoms

- Connection fails with timeout or network error
- Integration was previously working but stops functioning

#### Resolution

- Verify your GitLab instance is running and accessible
- If using a private connection, verify the VPC Lattice resource gateway is healthy and the ENIs have network connectivity to your instance
- Verify security groups allow traffic on the configured port
- Verify TLS certificate is valid and not expired

### TLS certificate errors

#### Symptoms

- Connection fails with SSL/TLS error

#### Resolution

- Verify your instance serves HTTPS with TLS 1.2 or higher
- If using a private certificate authority, ensure the PEM-encoded public key was provided during private connection setup
- Verify the certificate is not expired

## Next steps

After connecting GitLab Self-Managed to AWS Security Agent:

- Navigate to the Agent Space where you want to use these repositories
- Choose **Enable code review** or **Setup penetration testing** to connect specific projects
- Enable **Code remediation** for merge request-based fixes
