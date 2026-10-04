

# Connect AWS Security Agent to Bitbucket Data Center
<a name="connect-bitbucket-data-center"></a>

Connect your AWS Security Agent to a Bitbucket Data Center instance to enable code review, threat modeling, penetration testing, and automated remediation capabilities for repositories hosted on your own infrastructure.

Bitbucket Data Center is a self-hosted provider. It is registered as its own integration type—separate from Bitbucket Cloud (see [Connect AWS Security Agent to Bitbucket repositories](connect-bitbucket.md))—because the two use different authentication models. Bitbucket Data Center uses an OAuth application that you create on your own instance, with additional configuration for network connectivity to a private instance. Before you begin, review [How integrations work with Agent Spaces](about-integrations.md) to understand how a registration is reused across Agent Spaces and shared across capabilities.

## How Bitbucket Data Center integration works
<a name="_how_bitbucket_data_center_integration_works"></a>

 **Pull request analysis** happens within Bitbucket Data Center. Unlike other providers, AWS Security Agent does not create the pull request webhook automatically for Bitbucket Data Center, because doing so would require elevated permissions. Instead, after you register the integration and enable code review comments, you create a webhook on your instance using a payload URL and signing secret that AWS Security Agent generates for you (see [Set up the pull request webhook](#connect-bitbucket-data-center-webhook)). The webhook notifies AWS Security Agent of new pull requests; it then scans the changes in each pull request (a differential scan of just the changed code) and posts findings as pull request comments.

You create and run **full code reviews**—which scan a repository’s entire codebase—in the AWS Security Agent web application, not in Bitbucket Data Center.

 **Penetration testing** and **threat modeling** are initiated within the AWS Security Agent web application. Users specify target domains and select connected repositories to provide application context.

## Prerequisites
<a name="_prerequisites"></a>

Before you begin, ensure you have:
+ A Bitbucket Data Center instance that is either:
  + Publicly accessible over the internet, OR
  + Accessible via a private connection (see [Connect to privately hosted source control](connect-private-connection.md))
+ Administrator access to your Bitbucket Data Center instance to create an OAuth 2.0 external application (incoming) link with the **Repository Read** and **Repository Write** permissions (`REPO_READ` and `REPO_WRITE`). During registration, the AWS Security Agent console shows you the redirect URI and the permissions to configure on the link. Have the link’s client ID and client secret ready to enter in the console.
+ Administrator access to the projects and repositories you want to connect
+ Your instance must serve HTTPS traffic with a minimum TLS version of 1.2

**Important**  
If your Bitbucket Data Center instance is reachable over the public internet and restricts inbound access with an IP allow list or firewall, add the AWS Security Agent IP addresses for your AWS Region before you register the integration. For the IP addresses, see [AWS Security Agent IP addresses](about-integrations.md#agent-ip-addresses). Instances reached through a private connection do not need this step. That traffic arrives over the private network path, not from these public IP addresses.

**Note**  
If your Bitbucket Data Center instance uses TLS certificates issued by a private certificate authority, you can provide the PEM-encoded public key of the certificate when creating a private connection. This allows AWS Security Agent to trust the TLS connection to your instance.

## Register a Bitbucket Data Center connection
<a name="_register_a_bitbucket_data_center_connection"></a>

1. In the AWS Security Agent Management Console, navigate to **Integrations**.

1. Choose **Add integration**.

1. Select **Bitbucket Data Center**, then choose **Next**.

1. In the **Instance URL** field, enter the base URL of your instance, for example `https://bitbucket.example.com`.

1. The console displays the **redirect URI** (the AWS Security Agent Bitbucket Data Center OAuth callback) and the permissions to configure on your OAuth application link. The redirect URI is specific to your Agent Space’s AWS Region and has the form:

   ```
   https://securityagent.{region}.api.aws/oauth2/provider/register/callback/bitbucketdatacenter
   ```

   Copy the exact redirect URI shown in the console—it is the value your OAuth application link must redirect to.

1. In Bitbucket Data Center, create an OAuth 2.0 external application (incoming) link using the redirect URI shown in the console, and grant it the **Repository Read** and **Repository Write** permissions (`REPO_READ` and `REPO_WRITE`). In Bitbucket Data Center, **Repository Write** includes **Repository Read**, so selecting **Repository Write** grants both. Copy the generated **Client ID** and **Client secret**. See the following note about which user approves the link.

1. Back in the console, enter the **Client ID** and **Client secret** from the link.

1. If your instance is not publicly accessible, select **Connect to endpoint using a private connection**, then choose an existing private connection or create a new one. See [Connect to privately hosted source control](connect-private-connection.md).

1. In the **Registration name** field, enter a descriptive name for this connection. Valid characters are letters, numbers, periods, underscores, and hyphens.

1. Choose **Connect**.

   AWS Security Agent runs the OAuth authorization against your instance and returns you to the **Integrations** page, where the new connection appears with its registration name.

**Important**  
AWS Security Agent acts as the Bitbucket Data Center user who approves the OAuth authorization. It has no separate application identity on your instance. Every action it takes is performed as, and attributed to, that user. This includes reading source, fetching pull request diffs, posting comments, and opening remediation pull requests. Its access is capped at that user’s permissions.  
We strongly recommend that a Bitbucket Data Center administrator create a dedicated user for this purpose (for example, `aws-security-agent`) and approve the authorization while signed in as that user. Then:  
 **Scope that user’s access** to only the repositories and projects you intend AWS Security Agent to scan. Because the OAuth token inherits the user’s permissions, this is the primary control that bounds what AWS Security Agent can reach.
 **Recognize the identity in your logs.** AWS Security Agent’s reads, comments, and pull requests appear in your Bitbucket Data Center audit logs and pull request history under this user. A dedicated user makes automated activity distinguishable from a real person’s.

## Set up the pull request webhook
<a name="connect-bitbucket-data-center-webhook"></a>

Pull request scanning requires a webhook on your Bitbucket Data Center instance. Unlike other providers, AWS Security Agent does not create this webhook automatically, because doing so would require broad administrative permissions on your instance. Instead, AWS Security Agent generates the webhook’s payload URL and signing secret, and you create the webhook on your instance with those values. Without the webhook, new pull requests are never analyzed and no comments are posted.

Set this up after you register the integration:

1. In the AWS Security Agent Management Console, open the **Integrations** page, find your Bitbucket Data Center connection, and choose **Manage**.

1. Choose **Create webhook**. AWS Security Agent generates:
   + A **Payload URL**—the endpoint your instance sends pull request events to.
   + A **Signing secret**—AWS Security Agent uses it to verify that inbound events genuinely originate from your instance.
**Important**  
The signing secret is shown only once. Copy it before you close the dialog—it cannot be retrieved afterward. If you lose it, rotate the secret (see [Rotate the signing secret](#connect-bitbucket-data-center-webhook-rotate)) to generate a new one.

1. In Bitbucket Data Center, create a webhook on each repository (or project) you want scanned:

   1. Set the **URL** to the payload URL from the console.

   1. Set the **Secret** to the signing secret from the console.

   1. Subscribe to these events:

       **Repository** 
      + Push

       **Pull request** 
      + Opened
      + Source branch updated
      + Modified
      + Comment added

1. Save the webhook on your instance.

1. In the AWS Security Agent web application, configure the repository in an Agent Space to start receiving code review comments and automated remediation. See [Enable code review](enable-code-review-scan.md).

**Important**  
Subscribe to only the events listed above. Always set the signing secret—without it, AWS Security Agent cannot verify that events came from your instance, and pull requests are not scanned.

### Rotate the signing secret
<a name="connect-bitbucket-data-center-webhook-rotate"></a>

If the signing secret is lost or compromised, rotate it. On the **Manage webhook** dialog, choose **Rotate**, then **Rotate secret**. Rotating generates a new signing secret and invalidates the current one; the payload URL does not change. Event delivery stops until you update the webhook in Bitbucket Data Center with the new secret, so update it promptly.

## Private connectivity
<a name="_private_connectivity"></a>

If your Bitbucket Data Center instance is not publicly accessible, you must create a private connection before registering the integration. For instructions, see [Create a private connection](connect-private-connection.md#create-a-private-connection).

**Important**  
Service-managed private connections require the Bitbucket Data Center instance to be running in the **same AWS account** where the Agent Space is created. For cross-account access, use a self-managed private connection where you provide your own VPC Lattice resource configuration.

## Troubleshoot Bitbucket Data Center integration
<a name="_troubleshoot_bitbucket_data_center_integration"></a>

### Instance unreachable
<a name="_instance_unreachable"></a>

#### Symptoms
<a name="_symptoms"></a>
+ Connection fails with timeout or network error
+ Integration was previously working but stops functioning

#### Resolution
<a name="_resolution"></a>
+ Verify your Bitbucket Data Center instance is running and accessible
+ If using a private connection, verify the VPC Lattice resource gateway is healthy and the ENIs have network connectivity to your instance
+ Verify security groups allow traffic on the configured port
+ Verify the TLS certificate is valid and not expired

### TLS certificate errors
<a name="_tls_certificate_errors"></a>

#### Symptoms
<a name="_symptoms_2"></a>
+ Connection fails with an SSL/TLS error

#### Resolution
<a name="_resolution_2"></a>
+ Verify your instance serves HTTPS with TLS 1.2 or higher
+ If using a private certificate authority, ensure the PEM-encoded public key was provided during private connection setup
+ Verify the certificate is not expired

### Authorization fails
<a name="_authorization_fails"></a>

#### Symptoms
<a name="_symptoms_3"></a>
+ The authorization step returns an error, or an operation reports that authentication failed.

#### Resolution
<a name="_resolution_3"></a>
+ A response from your instance means the request reached it and Bitbucket Data Center rejected the credentials—the problem is the OAuth application, not connectivity. Verify the client ID and client secret, and that the OAuth application grants the repository read (and, for comments or remediation, write) access AWS Security Agent needs.
+ A connection timeout or a TLS error (rather than a response from your instance) indicates a network or certificate problem. See **Instance unreachable** and **TLS certificate errors**.

### Pull requests are not reviewed
<a name="_pull_requests_are_not_reviewed"></a>

#### Symptoms
<a name="_symptoms_4"></a>
+ The integration is registered and repositories are connected, but new pull requests are never analyzed and no comments are posted.

#### Resolution
<a name="_resolution_4"></a>
+ Verify that you created the webhook on your Bitbucket Data Center instance with the correct payload URL, signing secret, and events (see [Set up the pull request webhook](#connect-bitbucket-data-center-webhook)). This step is manual for Bitbucket Data Center and is the most common reason pull requests are not scanned.
+ Verify that code review comments are enabled for the repository in the Agent Space (see [Enable code review](enable-code-review-scan.md)).
+ Verify the webhook is enabled and uses the current signing secret, and that no firewall or IP allow list blocks delivery from the AWS Security Agent IP addresses for your AWS Region (see [AWS Security Agent IP addresses](about-integrations.md#agent-ip-addresses)).

## Next steps
<a name="_next_steps"></a>

After connecting Bitbucket Data Center to AWS Security Agent:
+ Navigate to the Agent Space where you want to use these repositories
+ Choose **Enable code review** or **Setup penetration testing** to connect specific repositories to your Agent Space (see [Enable code review](enable-code-review-scan.md) and [Enable penetration test](enable-penetration-test.md))
+ Enable **Code review comments** to have AWS Security Agent analyze each pull request and post findings in Bitbucket Data Center (see [Review code security findings in pull requests](review-code-findings-github.md))
+ Enable **Code remediation** to allow AWS Security Agent to submit pull requests with vulnerability fixes (see [Enable users to start remediation of penetration test and code review findings](enable-remediate-findings.md))
+ Create threat models from connected repositories in the web application (see [Enable threat modeling](enable-threat-model.md))