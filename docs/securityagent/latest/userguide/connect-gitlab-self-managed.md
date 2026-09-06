

# Connect AWS Security Agent to GitLab Self-Managed
<a name="connect-gitlab-self-managed"></a>

Connect your AWS Security Agent to a GitLab Self-Managed instance to enable code review, threat modeling, penetration testing, and automated remediation capabilities for repositories hosted on your own infrastructure.

GitLab Self-Managed integration works the same as GitLab Cloud (see [Connect AWS Security Agent to GitLab repositories](connect-gitlab.md)) with additional configuration for network connectivity to your private instance. Before you begin, review [How integrations work with Agent Spaces](about-integrations.md) to understand how a registration is reused across Agent Spaces and shared across capabilities.

**Note**  
GitLab Self-Managed is registered through the **GitLab** integration, not a separate integration type. In the registration flow you select **Use GitLab self-hosted endpoint** and provide your instance URL. The cloud-hosted GitLab flow is described in [Connect AWS Security Agent to GitLab repositories](connect-gitlab.md).

## Prerequisites
<a name="_prerequisites"></a>

Before you begin, ensure you have:
+ A GitLab Self-Managed instance that is either:
  + Publicly accessible over the internet, OR
  + Accessible via a private connection (see [Connect to privately hosted source control](connect-private-connection.md))
+ A GitLab access token with the scopes required for your connection type:
  +  **Personal** - A personal access token with all read permissions and the `api` permission.
  +  **Group** - A group access token with the `read_api` and `read_repository` scopes.
+ Maintainer or Owner access to the projects you want to connect
+ Your GitLab instance must serve HTTPS traffic with a minimum TLS version of 1.2

**Important**  
If your GitLab Self-Managed instance is reachable over the public internet and restricts inbound access with an IP allow list or firewall, add the AWS Security Agent IP addresses for your AWS Region before you register the integration. For the IP addresses, see [AWS Security Agent IP addresses](about-integrations.md#agent-ip-addresses). Instances reached through a private connection do not need this step. That traffic arrives over the private network path, not from these public IP addresses.

**Note**  
If your GitLab Self-Managed instance uses TLS certificates issued by a private certificate authority, you can provide the PEM-encoded public key of the certificate when creating a private connection. This allows AWS Security Agent to trust the TLS connection to your instance.

## Register a GitLab Self-Managed connection
<a name="_register_a_gitlab_self_managed_connection"></a>

1. In the AWS Security Agent Management Console, navigate to **Integrations**.

1. Choose **Add integration**.

1. Select **GitLab**, then choose **Next**.

1. Under **Choose an account type**, select **Personal** or **Group**. If you select **Group**, enter your **Group ID**.

1. Select **Use GitLab self-hosted endpoint**.

1. In the **GitLab self-hosted endpoint URL** field, enter the URL of your instance, for example `https://gitlab.example.com`.

1. If your instance is not publicly accessible, select **Connect to endpoint using a private connection**, then choose an existing private connection or create a new one. See [Connect to privately hosted source control](connect-private-connection.md).

1. In the **Access token** field, paste your GitLab access token.

1. In the **Registration name** field, enter a descriptive name for this connection. Valid characters are letters, numbers, periods, underscores, and hyphens.

1. Choose **Connect**.

   You return to the **Integrations** page, where the new connection appears with its registration name.

## Private connectivity
<a name="_private_connectivity"></a>

If your GitLab Self-Managed instance is not publicly accessible, you must create a private connection before registering the integration. See [Connect to privately hosted source control](connect-private-connection.md) for detailed instructions.

**Important**  
Service-managed private connections require the GitLab Self-Managed instance to be running in the **same AWS account** where the Agent Space is created. For cross-account access, use a self-managed private connection where you provide your own VPC Lattice resource configuration.

## Troubleshoot GitLab Self-Managed integration
<a name="_troubleshoot_gitlab_self_managed_integration"></a>

In addition to the troubleshooting steps in [Connect AWS Security Agent to GitLab repositories](connect-gitlab.md), the following issues are specific to self-managed instances:

### 401 Unauthorized through a private connection
<a name="_401_unauthorized_through_a_private_connection"></a>

#### Symptoms
<a name="_symptoms"></a>
+ An operation such as `ListResourcesFromIntegration` returns `GITLAB authentication failed: Invalid or expired token` with the body `{"message":"401 Unauthorized"}` 

#### Resolution
<a name="_resolution"></a>
+ A GitLab `401` response means the request **reached** your GitLab instance and GitLab rejected the credentials. This confirms that DNS resolution, TLS, and the private connection (VPC Lattice resource gateway and resource configuration) are all working. The problem is the access token, not connectivity, so do not troubleshoot the private connection for this error.
+ Resolve it as a token issue. See the **Invalid or expired token**, **Missing or insufficient token scope**, and **Group access token requires a paid GitLab.com tier** sections in [Connect AWS Security Agent to GitLab repositories](connect-gitlab.md).
+ By contrast, a connection **timeout** or a **TLS error** (rather than a GitLab JSON response) indicates a network or certificate problem. See **Instance unreachable** and **TLS certificate errors** below.

### Instance unreachable
<a name="_instance_unreachable"></a>

#### Symptoms
<a name="_symptoms_2"></a>
+ Connection fails with timeout or network error
+ Integration was previously working but stops functioning

#### Resolution
<a name="_resolution_2"></a>
+ Verify your GitLab instance is running and accessible
+ If using a private connection, verify the VPC Lattice resource gateway is healthy and the ENIs have network connectivity to your instance
+ Verify security groups allow traffic on the configured port
+ Verify TLS certificate is valid and not expired

### TLS certificate errors
<a name="_tls_certificate_errors"></a>

#### Symptoms
<a name="_symptoms_3"></a>
+ Connection fails with SSL/TLS error

#### Resolution
<a name="_resolution_3"></a>
+ Verify your instance serves HTTPS with TLS 1.2 or higher
+ If using a private certificate authority, ensure the PEM-encoded public key was provided during private connection setup
+ Verify the certificate is not expired

## Next steps
<a name="_next_steps"></a>

After connecting GitLab Self-Managed to AWS Security Agent:
+ Navigate to the Agent Space where you want to use these repositories
+ Choose **Enable code review** or **Setup penetration testing** to connect specific projects (see [Enable code review](enable-code-review-scan.md) and [Enable penetration test](enable-penetration-test.md))
+ Enable **Code review comments** to have AWS Security Agent analyze each merge request and post findings in GitLab (see [Review code security findings in pull requests](review-code-findings-github.md))
+ Enable **Code remediation** for merge request-based fixes (see [Enable users to start remediation of penetration test and code review findings](enable-remediate-findings.md))
+ Create threat models from connected projects in the web application (see [Enable threat modeling](enable-threat-model.md))