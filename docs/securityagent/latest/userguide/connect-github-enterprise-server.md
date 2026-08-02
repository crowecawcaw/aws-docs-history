# Connect AWS Security Agent to GitHub Enterprise Server

Connect your AWS Security Agent to a GitHub Enterprise Server (GHES) instance to enable code review, threat modeling, penetration testing, and automated remediation capabilities for repositories hosted on your own infrastructure.

GitHub Enterprise Server integration provides the same capabilities as cloud-hosted GitHub (see [Connect AWS Security Agent to GitHub repositories](connect-github.md "connect-github.md")) with additional configuration for network connectivity to your self-hosted instance. Before you begin, review [How integrations work with Agent Spaces](about-integrations.md "about-integrations.md") to understand how a registration is reused across Agent Spaces and shared across capabilities.

###### Note

GitHub Enterprise Server is registered through the **GitHub** integration, not a separate integration type. In the registration flow you choose **GitHub Enterprise Server** as the instance type. The cloud-hosted GitHub.com flow is described in [Connect AWS Security Agent to GitHub repositories](connect-github.md "connect-github.md").

## How GitHub Enterprise Server integration works

**Pull request analysis** happens within GitHub Enterprise Server. After you authorize the connection, connect repositories, and enable code review comments in the AWS Management Console, AWS Security Agent automatically scans the changes in each new pull request (a differential scan of just the changed code) and posts findings as pull request comments.

You create and run **full code reviews** — which scan a repository’s entire codebase — in the AWS Security Agent web application, not in GitHub Enterprise Server.

**Penetration testing** and **threat modeling** are initiated within the AWS Security Agent web application. Users specify target domains and select connected repositories to provide application context. If you enable automated remediation, users can request AWS Security Agent to fix findings by opening pull requests to connected repositories.

## Prerequisites

Before you begin, ensure you have:

- A GitHub Enterprise Server instance that is either:

  - Publicly accessible over the internet, OR
  - Accessible via a private connection (see [Connect to privately hosted source control](connect-private-connection.md "connect-private-connection.md"))

- Site administrator or organization administrator access on your GHES instance
- Your GHES instance must serve HTTPS traffic with a minimum TLS version of 1.2
- Permissions to configure integrations in the AWS Security Agent Management Console

###### Note

GitHub Enterprise Server integrations can be used across multiple AWS accounts.

## Register a GitHub Enterprise Server connection

Registering a GitHub Enterprise Server connection uses an OAuth-based authorization flow.

###### Important

Complete all steps in this process without closing your browser or navigating away. If the registration process is interrupted, you may need to restart from the beginning.

1. In the AWS Security Agent Management Console, navigate to **Integrations**.
2. Choose **Add integration**.
3. Select **GitHub**, then choose **Next**.
4. Under **Instance type**, select **GitHub Enterprise Server**.
5. In the **GitHub Enterprise Server URL** field, enter the HTTPS URL of your instance, for example `https://github.example.com`.
6. If your instance is not publicly accessible, select **Connect to endpoint using a private connection**, then choose an existing private connection or create a new one. See [Connect to privately hosted source control](connect-private-connection.md "connect-private-connection.md").
7. In the **Register details** section, configure the following fields:

   1. **Registration name** - Enter a descriptive name for this connection. Valid characters are letters, numbers, periods, underscores, and hyphens.
   2. **GitHub account type** - Select **Organization** or **User**.
   3. **Organization name** (appears only if you selected Organization) - Enter the exact name of your GitHub Enterprise Server organization. Names are case sensitive.

8. Choose **Connect**.

###### Note

AWS Security Agent redirects you away from the console to complete authorization with your GitHub Enterprise Server instance. After authorization completes, you return to the console and the new connection appears on the **Integrations** page.

## Private connectivity

If your GitHub Enterprise Server instance is not publicly accessible, you must create a private connection before registering the integration. See [Connect to privately hosted source control](connect-private-connection.md "connect-private-connection.md") for detailed instructions.

###### Important

Service-managed private connections require the GHES instance to be running in the **same AWS account** where the Agent Space is created. For cross-account access, use a self-managed private connection.

###### Note

If your GHES instance uses TLS certificates issued by a private certificate authority, provide the PEM-encoded public key of the certificate when creating the private connection.

## Troubleshoot GitHub Enterprise Server integration

If you encounter issues connecting AWS Security Agent to GitHub Enterprise Server, use the following guidance to diagnose and resolve common problems.

### OAuth redirect failure

#### Symptoms

- Browser redirects fail during the authorization flow
- Error page displayed after authorizing on GHES

#### Resolution

- Verify your GHES instance is accessible from your browser
- Ensure the OAuth callback URL is correctly configured
- Restart the integration process from the beginning

### Instance unreachable

#### Symptoms

- Connection fails with timeout or network error

#### Resolution

- Verify your GHES instance is running and accessible
- If using a private connection, verify VPC Lattice connectivity
- Verify security groups allow traffic on the configured port
- Verify TLS certificate is valid (TLS 1.2 minimum)

## Next steps

After connecting GitHub Enterprise Server to AWS Security Agent:

- Navigate to the Agent Space where you want to use these repositories
- Choose **Enable code review** or **Setup penetration testing** to connect specific repositories
- Enable **Code remediation** to allow AWS Security Agent to submit pull requests with vulnerability fixes
