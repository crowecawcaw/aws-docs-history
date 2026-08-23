# Connect AWS Security Agent to GitHub Enterprise

Connect AWS Security Agent to GitHub Enterprise (GHE) to enable code review, threat modeling, penetration testing, and automated remediation for your repositories.

GitHub Enterprise integration provides the same capabilities as cloud-hosted GitHub (see [Connect AWS Security Agent to GitHub repositories](connect-github.md "connect-github.md")). Before you begin, review [How integrations work with Agent Spaces](about-integrations.md "about-integrations.md") to understand how a registration is reused across Agent Spaces and shared across capabilities.

###### Note

GitHub Enterprise is registered through the **GitHub** integration, not a separate integration type. In the registration flow, you choose **GitHub Enterprise** as the instance type. This instance type covers both a GitHub Enterprise Server instance that you operate and a GitHub Enterprise Cloud with data residency (a `.ghe.com` host). For the cloud-hosted GitHub.com flow, see [Connect AWS Security Agent to GitHub repositories](connect-github.md "connect-github.md").

## How GitHub Enterprise integration works

**Pull request analysis** happens within GitHub Enterprise. After you authorize the connection, connect repositories, and enable code review comments in the AWS Management Console, AWS Security Agent automatically scans the changes in each new pull request (a differential scan of just the changed code) and posts findings as pull request comments.

You create and run **full code reviews** — which scan a repository’s entire codebase — in the AWS Security Agent web application, not in GitHub Enterprise.

**Penetration testing** and **threat modeling** are initiated within the AWS Security Agent web application. Users specify target domains and select connected repositories to provide application context. If you enable automated remediation, users can request AWS Security Agent to fix findings by opening pull requests to connected repositories.

## GitHub Enterprise Cloud with data residency (.ghe.com)

GitHub Enterprise Cloud with data residency serves your organization from a dedicated, GitHub-operated tenant on a `.ghe.com` host rather than from `github.com`. Connect it through the same **GitHub Enterprise** instance type you use for GitHub Enterprise Server, following the steps below. A data residency tenant installs the AWS Security Agent GitHub App under an organization, so you choose the **Organization** account type during registration.

###### Important

AWS Security Agent processes your repository content in the Region of the AWS Security Agent instance you connect from. If that Region differs from your tenant’s data residency Region, AWS Security Agent processes your content outside that Region. See [Cross-Region data processing](data-protection.md#cross-region-processing "data-protection.md#cross-region-processing").

## Prerequisites

Before you begin, ensure you have:

- Permissions to configure integrations in the AWS Security Agent Management Console

For a GitHub Enterprise Server instance:

- An instance that is either publicly accessible over the internet, or reachable through a private connection (see [Connect to privately hosted source control](connect-private-connection.md "connect-private-connection.md"))
- Site administrator or organization administrator access on the instance
- The instance must serve HTTPS traffic with a minimum TLS version of 1.2

For GitHub Enterprise Cloud with data residency:

- An organization on your `.ghe.com` tenant, and permission to install a GitHub App in it

###### Note

GitHub Enterprise integrations can be used across multiple AWS accounts.

## Register a GitHub Enterprise connection

Registering a GitHub Enterprise connection uses an OAuth-based authorization flow.

###### Important

Complete all steps in this process without closing your browser or navigating away. If the registration process is interrupted, you may need to restart from the beginning.

1. In the AWS Security Agent Management Console, navigate to **Integrations**.
2. Choose **Add integration**.
3. Select **GitHub**, then choose **Next**.
4. Under **Instance type**, select **GitHub Enterprise**.
5. In the **GitHub Enterprise URL** field, enter the HTTPS URL of your instance. For a GitHub Enterprise Server instance, enter its host, for example `https://github.example.com`. For GitHub Enterprise Cloud with data residency, enter your `.ghe.com` host, for example `https://acme.ghe.com`. Do not include an `api.` prefix or additional subdomain levels.
6. (GitHub Enterprise Server only) If your instance is not publicly accessible, select **Connect to endpoint using a private connection**, then choose an existing private connection or create a new one. See [Connect to privately hosted source control](connect-private-connection.md "connect-private-connection.md").
7. In the **Register details** section, configure the following fields:

   1. **Registration name** - Enter a descriptive name for this connection. Valid characters are letters, numbers, periods, underscores, and hyphens.
   2. **GitHub account type** - Select **Organization** or **User**. For a GitHub Enterprise Cloud with data residency, you must select **Organization**; **User** accounts are not supported.
   3. **Organization name** (appears only if you selected Organization) - Enter the exact name of your GitHub Enterprise organization. Names are case sensitive.

8. Choose **Connect**.

###### Note

AWS Security Agent redirects you away from the console to complete authorization with your GitHub Enterprise instance. After authorization completes, you return to the console and the new connection appears on the **Integrations** page.

## Private connectivity

If your GitHub Enterprise Server instance is not publicly accessible, you must create a private connection before registering the integration. See [Connect to privately hosted source control](connect-private-connection.md "connect-private-connection.md") for detailed instructions.

###### Important

Service-managed private connections require the GHE instance to be running in the **same AWS account** where the Agent Space is created. For cross-account access, use a self-managed private connection.

###### Note

If your GHE instance uses TLS certificates issued by a private certificate authority, provide the PEM-encoded public key of the certificate when creating the private connection.

## Troubleshoot GitHub Enterprise integration

If you encounter issues connecting AWS Security Agent to GitHub Enterprise, use the following guidance to diagnose and resolve common problems.

### OAuth redirect failure

#### Symptoms

- Browser redirects fail during the authorization flow
- Error page displayed after authorizing on GHE

#### Resolution

- Verify your GHE instance is accessible from your browser
- Ensure the OAuth callback URL is correctly configured
- Restart the integration process from the beginning

### Instance unreachable

#### Symptoms

- Connection fails with timeout or network error

#### Resolution

- Verify your GHE instance is running and accessible
- If using a private connection, verify VPC Lattice connectivity
- Verify security groups allow traffic on the configured port
- Verify TLS certificate is valid (TLS 1.2 minimum)

## Next steps

After connecting GitHub Enterprise to AWS Security Agent:

- Navigate to the Agent Space where you want to use these repositories
- Choose **Enable code review** or **Setup penetration testing** to connect specific repositories (see [Enable code review](enable-code-review-scan.md "enable-code-review-scan.md") and [Enable penetration test](enable-penetration-test.md "enable-penetration-test.md"))
- Enable **Code review comments** to have AWS Security Agent analyze each pull request and post findings in GitHub Enterprise (see [Review code security findings in pull requests](review-code-findings-github.md "review-code-findings-github.md"))
- Enable **Code remediation** to allow AWS Security Agent to submit pull requests with vulnerability fixes (see [Enable users to start remediation of penetration test and code review findings](enable-remediate-findings.md "enable-remediate-findings.md"))
- Create threat models from connected repositories in the web application (see [Enable threat modeling](enable-threat-model.md "enable-threat-model.md"))
