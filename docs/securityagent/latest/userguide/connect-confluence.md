# Connect AWS Security Agent to Confluence

Connect your AWS Security Agent to Confluence Cloud to provide documentation context for security assessments. Unlike code providers, Confluence serves as a documentation source that provides threat models, architecture documents, API specifications, and other materials that enhance the quality of security reviews. Before you begin, review [How integrations work with Agent Spaces](about-integrations.md "about-integrations.md") to understand how a registration is reused across Agent Spaces.

Confluence integration serves multiple purposes:

- **Design review context** - Provide architectural documents and design specifications for security design reviews
- **Threat modeling** - Provide existing threat models and system documentation for threat analysis
- **Penetration testing context** - Provide application documentation for deeper understanding during penetration testing
  Connecting Confluence to AWS Security Agent requires installing the AWS Security Agent Forge app on your Atlassian site and completing the OAuth authorization flow.

###### Note

AWS Security Agent supports Confluence Cloud only. Confluence Data Center and Confluence Server are not supported.

## How Confluence integration works

Confluence is a **documentation provider** rather than a source code provider. After you install the Forge app and connect spaces or pages in the AWS Management Console, AWS Security Agent can access your Confluence content to provide context during security assessments.

AWS Security Agent reads page content to understand your application architecture, security requirements, and design decisions. This context improves the quality and relevance of security findings during design reviews, code reviews, and penetration tests.

## Prerequisites

Before you begin, ensure you have:

- A Confluence Cloud site with admin access
- An Atlassian account with site administrator privileges
- Permissions to configure integrations in the AWS Security Agent Management Console

###### Important

One Atlassian site can only be associated with one AWS account per region. If you need to connect the same Confluence site to AWS Security Agent in a different AWS account within the same region, you must first remove the existing integration.

###### Note

Atlassian Forge app pricing applies to this integration. For more information, see [Forge platform pricing](https://developer.atlassian.com/platform/forge/forge-platform-pricing/ "https://developer.atlassian.com/platform/forge/forge-platform-pricing/") in the Atlassian documentation.

## Register a Confluence connection

1. In the AWS Security Agent Management Console, navigate to **Integrations**.
2. Choose **Add integration**.
3. Select **Confluence**, then choose **Next**.
4. Install the AWS Security Agent Forge app in your Atlassian site, following the on-screen instructions. After installation, copy the installation ID. See [Find your Atlassian installation ID](find-atlassian-installation-id.md "find-atlassian-installation-id.md").
5. In the **Confluence site URL** field, enter your site URL, for example `https://acme.atlassian.net`.
6. In the **Installation ID** field, paste the installation ID you copied from Confluence.
7. Choose **Authorize**.

You are redirected to Atlassian to authorize AWS Security Agent to access your Confluence site. After authorization completes, you return to the console. 8. In the **Register details** section, enter a **Registration name** for this connection. Valid characters are letters, numbers, periods, underscores, and hyphens. 9. Choose **Connect**.

## Select pages for an Agent Space

After you register the Confluence integration, connect specific pages to an Agent Space. Selecting a page grants AWS Security Agent read (fetch) access to that page’s content. There are no per-page capability options — the agent reads every connected page. In the review step of the connect wizard, you can remove any pages you do not want the agent to access.

## Troubleshoot Confluence integration

If you encounter issues during the Confluence integration process, use the following guidance to resolve common problems.

### Unable to complete registration

If the registration process is interrupted, the Forge app may be installed on your Atlassian site but not registered in the AWS Console.

#### Resolution

- Return to the AWS Security Agent console and restart the integration process.
- The Forge app remains installed and does not need to be reinstalled.

### Forge app uninstalled from Atlassian

If the AWS Security Agent Forge app is uninstalled from your Atlassian site while the integration still exists in AWS Security Agent:

#### Symptoms

- Integration appears in the AWS Console but cannot access Confluence content
- Errors when attempting to list or read pages

#### Resolution

- Reinstall the Forge app from the Atlassian Marketplace
- If the issue persists, remove the integration in the AWS Console and re-register

### Site already connected to another AWS account

#### Resolution

- One Atlassian site can only be connected to one AWS account per region.
- Identify which AWS account has the existing integration and use that account, or remove the existing integration first.

## Next steps

After connecting Confluence to AWS Security Agent:

- Navigate to the Agent Space where you want to use this documentation
- Select specific pages to include as context for design reviews and penetration tests
- Upload additional documentation via S3 if needed (see [Provide agent resources from an S3 bucket](enable-s3-bucket.md "enable-s3-bucket.md"))
