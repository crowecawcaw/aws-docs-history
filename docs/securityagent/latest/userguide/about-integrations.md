# How integrations work with Agent Spaces

AWS Security Agent connects to third-party source code and documentation providers so the agent can analyze your code and documentation during security assessments. Before you connect a specific provider, it helps to understand how integrations relate to Agent Spaces and capabilities.

## Register once, reuse everywhere

Connecting a provider to AWS Security Agent involves two distinct steps that happen at different levels:

1. **Register the integration (account level).** You register a provider one time from the **Integrations** page in the AWS Security Agent Management Console. A registration represents the authorized connection to a provider account, such as a GitHub organization, a GitLab group, a Bitbucket workspace, or a Confluence site. Registrations are account-level resources.
2. **Connect resources to an Agent Space (Agent Space level).** From within an Agent Space, you connect resources from a registered integration — repositories for source code providers, or pages for Confluence — and configure how the agent uses them. This step is specific to each Agent Space.

A single registration is reused across every Agent Space in your account. If you registered a provider while setting up one Agent Space, that same registration is available when you connect resources to another Agent Space — you do not register the same provider again.

## One connection, shared across capabilities

When you connect a resource to an Agent Space, that resource is shared across the agent’s capabilities. You do not connect a repository separately for each capability.

- **Read access is granted by connecting the resource.** When you connect a repository, AWS Security Agent can read it for full code scans (code review), penetration testing context, and threat modeling. When you connect a Confluence page, AWS Security Agent can read it for documentation context in design reviews, threat modeling, and penetration tests.
- **Write actions are opt-in, per repository.** When you connect source code repositories to an Agent Space, you can additionally enable write actions for each repository:

  - **Code review comments** - AWS Security Agent posts review findings as comments on pull requests (or merge requests in GitLab).
  - **Code remediation** - AWS Security Agent opens pull requests (or merge requests) with fixes for discovered vulnerabilities.

  These write actions are not available for public repositories. Read-only analysis still applies.

###### Note

Confluence is a documentation provider rather than a source code provider. AWS Security Agent reads connected Confluence pages to provide context for design reviews, threat modeling, and penetration tests. Selecting a page grants read access; there are no per-page capability toggles.

## Supported providers

AWS Security Agent supports the following providers:

- **Source code** - GitHub (cloud-hosted GitHub and cloud-hosted GitHub Enterprise), GitHub Enterprise Server (self-hosted), GitLab (cloud-hosted), GitLab Self-Managed (self-hosted), and Bitbucket Cloud.
- **Documentation** - Confluence Cloud.

For self-hosted providers that are not reachable over the public internet, you can route the agent’s traffic through a private connection. For more information, see [Connect to privately hosted source control](connect-private-connection.md "connect-private-connection.md").

## Next steps

- Register a provider from the **Integrations** page. See the connect topic for your provider, such as [Connect AWS Security Agent to GitHub repositories](connect-github.md "connect-github.md").
- Connect resources to an Agent Space and configure capabilities. See [Enable code review](enable-code-review-scan.md "enable-code-review-scan.md") and [Enable penetration test](enable-penetration-test.md "enable-penetration-test.md").
