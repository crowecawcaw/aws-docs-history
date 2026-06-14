# Connect AWS Security Agent to Confluence

Connect your AWS Security Agent to Confluence Cloud to provide documentation context for security assessments. Unlike code providers, Confluence serves as a documentation source that provides threat models, architecture documents, API specifications, and other materials that enhance the quality of security reviews.

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

AWS Security Agent can also write content back to Confluence, creating or updating pages with security assessment results.

## Prerequisites

Before you begin, ensure you have:

- A Confluence Cloud site with admin access
- An Atlassian account with site administrator privileges
- Permissions to configure integrations for your Agent Space in the AWS Management Console
- The installation ID from the AWS Security Agent Forge app (see [Find your Atlassian installation ID](find-atlassian-installation-id.md "find-atlassian-installation-id.md"))

###### Important

One Atlassian site can only be associated with one AWS account per region. If you need to connect the same Confluence site to AWS Security Agent in a different AWS account within the same region, you must first remove the existing integration.

###### Note

Atlassian Forge app pricing applies to this integration. For more information, see [Forge platform pricing](https://developer.atlassian.com/platform/forge/forge-platform-pricing/ "https://developer.atlassian.com/platform/forge/forge-platform-pricing/") in the Atlassian documentation.

For more information about finding your installation ID, see [Find your Atlassian installation ID](find-atlassian-installation-id.md "find-atlassian-installation-id.md").

## Register a Confluence connection

1. In the AWS Security Agent Management Console, navigate to **Integrations**.
2. Choose **Add integration**.
3. Select **Confluence**.
4. Choose **Next**.
5. Choose **Install and authorize**.

You’ll be redirected to Atlassian to install the Forge app and authorize access. The following OAuth scopes are requested:

    * `read:page:confluence` - View page content
    * `write:page:confluence` - Create and update pages
    * `read:space:confluence` - View space details
    * `read:confluence-content.summary` - Read content summaries

6. On the Atlassian consent screen, review the permissions and authorize the AWS Security Agent app.
7. You’ll be redirected back to the AWS Management Console to complete the registration.
8. In the **Registration details** section, configure the following fields:

   1. **Installation ID** - Paste the installation ID you copied from the Forge app in Confluence (see [Find your Atlassian installation ID](find-atlassian-installation-id.md "find-atlassian-installation-id.md")).
   2. **Registration name** - Enter a descriptive name for this Confluence connection, such as "Engineering-Docs-Confluence".

9. Choose **Connect**.

## Selecting content

After registering the Confluence integration, you connect specific spaces and pages to your Agent Space.

When connecting Confluence content to an Agent Space, you select individual pages that are relevant to your security assessment. A dedicated permission wizard allows you to configure which capabilities each page supports.

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
