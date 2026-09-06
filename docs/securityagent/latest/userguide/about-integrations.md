

# How integrations work with Agent Spaces
<a name="about-integrations"></a>

AWS Security Agent connects to third-party source code and documentation providers so the agent can analyze your code and documentation during security assessments. Before you connect a specific provider, it helps to understand how integrations relate to Agent Spaces and capabilities.

## Register once, reuse everywhere
<a name="_register_once_reuse_everywhere"></a>

Connecting a provider to AWS Security Agent involves two distinct steps that happen at different levels:

1.  **Register the integration (account level).** You register a provider one time from the **Integrations** page in the AWS Security Agent Management Console. A registration represents the authorized connection to a provider account, such as a GitHub organization, a GitLab group, a Bitbucket workspace, or a Confluence site. Registrations are account-level resources.

1.  **Connect resources to an Agent Space (Agent Space level).** From within an Agent Space, you connect resources from a registered integration — repositories for source code providers, or pages for Confluence — and configure how the agent uses them. This step is specific to each Agent Space.

A single registration is reused across every Agent Space in your account. If you registered a provider while setting up one Agent Space, that same registration is available when you connect resources to another Agent Space — you do not register the same provider again.

## One connection, shared across capabilities
<a name="_one_connection_shared_across_capabilities"></a>

When you connect a resource to an Agent Space, that resource is shared across the agent’s capabilities. You do not connect a repository separately for each capability.
+  **Read access is granted by connecting the resource.** When you connect a repository, AWS Security Agent can read it for full code scans (code review), penetration testing context, and threat modeling. When you connect a Confluence page, AWS Security Agent can read it for documentation context in design reviews, threat modeling, and penetration tests.
+  **Write actions are opt-in, per repository.** When you connect source code repositories to an Agent Space, you can additionally enable write actions for each repository:
  +  **Code review comments** - AWS Security Agent posts review findings as comments on pull requests (or merge requests in GitLab).
  +  **Code remediation** - AWS Security Agent opens pull requests (or merge requests) with fixes for discovered vulnerabilities.

    These write actions are not available for public repositories. Read-only analysis still applies.

**Note**  
Confluence is a documentation provider rather than a source code provider. AWS Security Agent reads connected Confluence pages to provide context for design reviews, threat modeling, and penetration tests. Selecting a page grants read access; there are no per-page capability toggles.

## Supported providers
<a name="_supported_providers"></a>

AWS Security Agent supports the following providers:
+  **Source code** - GitHub (cloud-hosted GitHub and cloud-hosted GitHub Enterprise), GitHub Enterprise Server (self-hosted), GitLab (cloud-hosted), GitLab Self-Managed (self-hosted), and Bitbucket Cloud.
+  **Documentation** - Confluence Cloud.

For self-hosted providers that are not reachable over the public internet, you can route the agent’s traffic through a private connection. For more information, see [Connect to privately hosted source control](connect-private-connection.md).

## AWS Security Agent IP addresses
<a name="agent-ip-addresses"></a>

AWS Security Agent connects to your source code repositories from a fixed set of IP addresses, one set per AWS Region. The same IP addresses are used for every supported source code provider: GitHub, GitLab, and Bitbucket. This includes self-hosted GitHub Enterprise Server and GitLab Self-Managed instances that are reachable over the public internet.

**Important**  
If your repository provider or the network in front of it restricts access with an IP allow list, add the AWS Security Agent IP addresses for your Agent Space’s AWS Region to that allow list. Wait a few minutes for the change to take effect, then register the integration. Examples include a GitHub organization IP allow list, a GitLab allowed IP range, Bitbucket workspace IP allowlisting, or a firewall in front of a self-hosted instance.

The following IP addresses are used to access your connected repositories:
+ US East (N. Virginia) (us-east-1)
  +  `34.228.181.128` 
  +  `44.219.176.187` 
  +  `54.226.244.221` 
+ US West (Oregon) (us-west-2)
  +  `34.212.16.133` 
  +  `52.89.67.212` 
  +  `54.187.135.61` 
+ Asia Pacific (Mumbai) (ap-south-1)
  +  `13.126.209.199` 
  +  `13.234.6.24` 
  +  `35.154.102.216` 
+ Asia Pacific (Singapore) (ap-southeast-1)
  +  `18.139.13.125` 
  +  `47.130.240.215` 
  +  `54.179.238.173` 
+ Asia Pacific (Sydney) (ap-southeast-2)
  +  `13.237.95.197` 
  +  `13.238.84.102` 
  +  `52.64.174.242` 
+ Asia Pacific (Tokyo) (ap-northeast-1)
  +  `13.192.12.233` 
  +  `35.74.181.230` 
  +  `57.183.50.158` 
+ Europe (Frankfurt) (eu-central-1)
  +  `18.158.110.140` 
  +  `52.57.96.160` 
  +  `52.59.55.56` 
+ Europe (Ireland) (eu-west-1)
  +  `34.251.85.24` 
  +  `52.30.157.157` 
  +  `52.51.192.222` 
+ South America (São Paulo) (sa-east-1)
  +  `54.94.247.213` 
  +  `54.207.222.14` 
  +  `54.232.201.242` 

## Next steps
<a name="_next_steps"></a>
+ Register a provider from the **Integrations** page. See the connect topic for your provider, such as [Connect AWS Security Agent to GitHub repositories](connect-github.md).
+ Connect resources to an Agent Space and configure capabilities. See [Enable code review](enable-code-review-scan.md) and [Enable penetration test](enable-penetration-test.md).