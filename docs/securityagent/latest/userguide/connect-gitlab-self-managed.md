# Connect AWS Security Agent to GitLab Self-Managed

Connect your AWS Security Agent to a GitLab Self-Managed instance to enable code review, threat modeling, penetration testing, and automated remediation capabilities for repositories hosted on your own infrastructure.

GitLab Self-Managed integration works the same as GitLab Cloud (see [Connect AWS Security Agent to GitLab repositories](connect-gitlab.md "connect-gitlab.md")) with additional configuration for network connectivity to your private instance.

## Prerequisites

Before you begin, ensure you have:

- A GitLab Self-Managed instance that is either:

  - Publicly accessible over the internet, OR
  - Accessible via a private connection (see [Connect to privately hosted source control](connect-private-connection.md "connect-private-connection.md"))

- A GitLab Personal Access Token with the following scopes:

  - `api` - Full read/write API access
  - `read_repository` - Access repository content
  - `write_repository` - Push remediation merge requests

- Maintainer or Owner access to the projects you want to connect
- Your GitLab instance must serve HTTPS traffic with a minimum TLS version of 1.2

###### Note

If your GitLab Self-Managed instance uses TLS certificates issued by a private certificate authority, you can provide the PEM-encoded public key of the certificate when creating a private connection. This allows AWS Security Agent to trust the TLS connection to your instance.

## Register a GitLab Self-Managed connection

1. In the AWS Security Agent Management Console, navigate to **Integrations**.
2. Choose **Add integration**.
3. Select **GitLab Self-Managed**.
4. Choose **Next**.
5. On the registration page, configure the following fields:

   1. **Connection type** - Select **Personal** or **Group**.
   2. **Instance URL** - Enter the URL of your GitLab Self-Managed instance (for example, `https://gitlab.yourcompany.com`). Custom domains are supported.
   3. **Access token** - Paste your GitLab Personal Access Token.
   4. **Private connection** (optional) - If your instance is not publicly accessible, select an existing private connection or create a new one. See [Connect to privately hosted source control](connect-private-connection.md "connect-private-connection.md").
   5. **Registration name** - Enter a descriptive name for this connection.

6. Choose **Connect**.

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
- Enable automated remediation for merge request-based fixes
