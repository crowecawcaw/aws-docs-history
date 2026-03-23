# Atlassian Confluence Cloud knowledge base integration

Use the Atlassian Confluence Cloud knowledge base integration to index Confluence content
so that Amazon Quick agents can search and answer questions about it.

## Before you begin

Make sure you have the following before you set up the integration.

- Atlassian Confluence Cloud.
- For subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md "integration-console-setup-process.md").

## Authentication

For knowledge base integrations, Amazon Quick handles authentication through a
popup flow during setup. Complete the following steps.

1. Complete the Confluence Cloud authentication popup that appears.
2. Grant permissions for Amazon Quick to access your Confluence content.
3. Review and complete the authentication process.

## Set up the knowledge base integration

1. In the Amazon Quick console, choose **Integrations**.
2. Choose **Atlassian Confluence Cloud** and choose the Add
   (plus "+") button.
3. In the **Create Confluence knowledge base** dialog,
   under **Connected account**, complete the following
   fields:
   - **Name** – A descriptive name for your
     data access integration.
   - **Confluence URL** – The URL of your
     Atlassian site (for example,
     ``your-site`.atlassian.net`).

4. Choose **Sign in** and complete the Confluence Cloud
   authentication flow in the popup window.
5. Under **Create knowledge base**, complete the
   following fields:
   - **Name** – A name for your knowledge
     base.
   - **Description** (Optional) – Notes about
     how the knowledge base will be used.

6. Under **Content**, paste the URLs of the Confluence
   spaces, blogs, or pages that you want to include. Choose
   **Add** after each URL.

###### Note

URLs that follow the structure
`https://`company`.atlassian.net/wiki/spaces/`space-key`/overview`
are treated as page URLs. 7. Choose **Create**.

## Supported content types

- Confluence pages and blog posts
- Spaces content
- Page and blog attachments

## Access controls

###### Important

Amazon Quick doesn't sync access control lists (ACLs) from data sources.
When you create a knowledge base in Amazon Quick, by default, only you can
get insights from the knowledge base. For shared content, you can provide
access to different users and groups by updating the knowledge base
permissions.

## Manage knowledge bases

### Edit existing knowledge bases

1. In the Amazon Quick console, choose **Knowledge
   bases**.
2. Select your Confluence Cloud knowledge base from the list.
3. Choose the three-dot icon under **Actions**, then
   choose **Edit knowledge base**.
4. Update your configuration settings as needed and choose
   **Save**.

## Troubleshoot

To edit, share, or delete your integration, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations "integration-workflows.md#managing-existing-integrations").

For general knowledge base troubleshooting, including sync issues and missing
documents, see [Troubleshooting knowledge bases](troubleshooting-knowledge-bases.md "troubleshooting-knowledge-bases.md").

### Blocked OAuth app authorization

**Symptoms:**

- Error message: "Your site admin must authorize this app for
  the site `instance-name`.atlassian.net before
  the app can access your account."
- Clicking **Accept** in the consent dialog
  has no effect.

**Cause:**

Your Atlassian site administrator has blocked user-installed OAuth apps.
When this setting is enabled, only a site or organization administrator can
authorize new third-party apps.

**Resolution steps:**

Use one of the following options to resolve this issue.

- **Option 1 (Recommended): Admin authorizes the
  app directly**

      1. An Atlassian site administrator navigates to Amazon Quick
       and starts a new knowledge base setup with Confluence Cloud.
      2. Because the administrator has site-level permissions, a
       clean consent screen appears without the error.
      3. The administrator chooses **Accept** to
       install the app.

  After the administrator authorizes the app, all other users on the
  site can connect without issues.

- **Option 2: Temporarily allow user-installed
  apps** – An administrator goes to
  `admin.atlassian.com`, navigates to
  **Apps**, **Atlassian Apps**,
  then chooses the link for third-party and Marketplace apps. Under
  **Settings**, find **User Installed
  Apps** and toggle to allow user apps. After the user
  authorizes Amazon Quick, toggle the setting back to block user
  apps.

###### Important

Admin authorization applies per Atlassian site, not per organization.
If your company has multiple sites (for example,
`team-a.atlassian.net` and
`team-b.atlassian.net`), each site requires separate
authorization.

###### Note

While user-installed apps are unblocked (Option 2), any user on the
site can authorize any OAuth app. Re-enable the block promptly after the
user has connected.

### Authentication popup fails

**Symptoms:**

- Authentication popup does not appear or closes
  immediately.
- Popup appears but fails to complete the OAuth
  flow.

**Resolution steps:**

1. Verify that your browser allows popups from the Amazon Quick
   console domain.
2. Verify that your Confluence Cloud instance is accessible from
   your network.
3. Try using a different browser or clearing your browser
   cache.

### Missing content in knowledge base

**Symptoms:**

- Knowledge base sync completes but expected content is not
  indexed.
- Search results do not include content from specific spaces
  or pages.
- Only one document is indexed for an entire
  space.

**Resolution steps:**

1. Verify that the Confluence Cloud user who authenticated has
   access to the spaces and pages you selected during
   setup.
2. Check that the selected content types are supported (pages,
   blog posts, and attachments).
3. Review the content selection in your knowledge base
   configuration to confirm the correct spaces and pages are
   included.
4. Check your Confluence URLs for the `/overview` suffix.
   URLs that end with
   `/wiki/spaces/`space-key`/overview`
   are treated as a single page URL, not a full space. If you intended
   to index the entire space, use the space URL without
   `/overview` (for example,
   `https://`company`.atlassian.net/wiki/spaces/`space-key``).
