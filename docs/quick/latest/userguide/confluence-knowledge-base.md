

# Atlassian Confluence Cloud knowledge base integration
<a name="confluence-knowledge-base"></a>

Use the Atlassian Confluence Cloud knowledge base integration to index Confluence content so that Amazon Quick agents can search and answer questions about it. Amazon Quick supports optional document-level access controls (ACLs) for Confluence knowledge bases. When enabled, users only see answers from documents they are authorized to access in Confluence. For more information, see [Document-level access controls](confluence-kb-acl.md).

## Before you begin
<a name="confluence-kb-prerequisites"></a>

Make sure you have the following before you set up the integration.
+ An Atlassian Confluence Cloud instance.
+ For Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md).

If you plan to enable document-level access controls, you must provide Atlassian admin credentials during setup. These credentials allow Amazon Quick to access all user and group information regardless of individual email visibility settings. Without admin credentials, the ACL option is not available during knowledge base creation. To provide admin credentials, you need the following from your Atlassian organization administrator:
+ **Atlassian admin API key** – An alphanumeric string generated in the Atlassian admin portal.
+ **Organization ID (UUID)** – The unique identifier for your Atlassian organization. You can find this in your browser URL when signed in to the admin portal: `admin.atlassian.com/o/{{orgId}}`.
+ **Directory ID (UUID)** – The unique identifier for your user directory. Retrieve this value using the Atlassian Admin Workspace API.

For detailed steps to obtain these credentials, see [Obtain Atlassian admin credentials](confluence-kb-acl.md#confluence-kb-atlassian-admin-credentials).

## Set up the knowledge base integration
<a name="confluence-kb-setup"></a>

The setup wizard has three steps: authentication, knowledge base creation, and additional settings.

### Authenticate your account
<a name="confluence-kb-setup-auth"></a>

1. In the Amazon Quick console, choose **Knowledge**.

1. Under **Knowledge**, choose **Atlassian Confluence Cloud** and choose the Add (plus "\+") button.

1. In the **Create Confluence knowledge base** dialog, under **Authentication method**, choose an existing connected account from the **Name** dropdown, or choose **Add account** to create a new connection.

1. If you are adding a new account, complete the following fields:
   + **Name** – A descriptive name for your connection.
   + **Description** (Optional) – Notes about the connection.
   + **Confluence URL** – The URL of your Atlassian site (for example, `https://{{your-site}}.atlassian.net`).

1. (Optional) Under **ACL Management**, select **Use Atlassian admin credentials** to provide Atlassian admin credentials. When selected, enter the following:
   + **API key** – The Atlassian admin API key.
   + **OrganizationID (UUID)** – Your Atlassian organization ID.
   + **Directory ID (UUID)** – Your Atlassian user directory ID.
**Important**  
Atlassian admin credentials are required to enable document-level access controls (ACLs) in **Additional settings**. Without admin credentials, the ACL option is disabled. Admin credentials cannot be added after the knowledge base is created. For steps to obtain these credentials, see [Obtain Atlassian admin credentials](confluence-kb-acl.md#confluence-kb-atlassian-admin-credentials).

1. Choose **Next**.

1. Complete the Confluence Cloud authentication popup that appears. Review the requested permissions and choose **Accept** to authorize Amazon Quick to access your Confluence content.

### Create the knowledge base
<a name="confluence-kb-setup-create"></a>

1. Under **Create knowledge base**, enter a **Name** for your knowledge base.

1. (Optional) Enter a **Description** with notes about how the knowledge base will be used.

1. Under **Confluence URLs**, paste the URLs of the Confluence spaces, blogs, or pages that you want to include. Choose **Add** after each URL.
**Note**  
URLs that follow the structure `https://{{company}}.atlassian.net/wiki/spaces/{{space-key}}/overview` are treated as page URLs, not space URLs. To index an entire space, use the space URL without `/overview` (for example, `https://{{company}}.atlassian.net/wiki/spaces/{{space-key}}`).

1. Choose **Next: Additional settings** to configure access controls and indexing options, or choose **Create** to create the knowledge base with default settings.

### Configure additional settings
<a name="confluence-kb-setup-settings"></a>

1. To enable document-level access controls, select **Control document access with ACLs**. This option is only available if you provided Atlassian admin credentials in **Authentication method**. When enabled, Amazon Quick syncs access control lists from Confluence and verifies each user's permissions at query time. For more information about how access controls work, see [Document-level access controls](confluence-kb-acl.md).

   If you do not enable ACLs, access is controlled at the knowledge base level. Anyone who has access to the knowledge base can get insights from all of the content within it. When ACLs are enabled, access is controlled at the document level. Users who have access to the knowledge base only see answers from documents that they are authorized to access in Confluence.
**Important**  
ACL management cannot be changed after the knowledge base is created. If you need to change this setting, you must create a new knowledge base.
**Note**  
If you did not provide Atlassian admin credentials in **Authentication method**, this option is disabled. To enable ACLs, choose **Back** or cancel the wizard and start again with a connected account that includes admin credentials.

1. Under **Multi-media content, file size, and file patterns**, configure the following indexing options as needed:
   + **Visual content in documents** – Index visual content such as images and charts embedded in documents.
   + **Audio files** – Index audio file attachments.
   + **Video files** – Index video file attachments.
   + **Maximum single file size** – The maximum file size for individual attachments (default: 50 MB).

1. Choose **Create**.

## Supported content types
<a name="confluence-kb-content-types"></a>
+ Confluence pages and blog posts
+ Page and blog post attachments

When you add a Confluence space URL, Amazon Quick crawls all pages and blog posts within that space. For supported attachment file types and size limits, see [File size and content limits](knowledge-base-integrations.md#file-size-and-content-limits).

## Manage knowledge bases
<a name="confluence-kb-management"></a>

### Edit existing knowledge bases
<a name="confluence-kb-edit"></a>

1. In the Amazon Quick console, choose **Knowledge bases**.

1. Select your Confluence Cloud knowledge base from the list.

1. Choose the three-dot icon under **Actions**, then choose **Edit knowledge base**.

1. Update your configuration settings as needed and choose **Save**.

## Troubleshoot
<a name="confluence-kb-troubleshooting"></a>

To edit, share, or delete your integration, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations).

For general knowledge base troubleshooting, including sync issues and missing documents, see [Troubleshooting knowledge bases](troubleshooting-knowledge-bases.md).

### Blocked OAuth app authorization
<a name="confluence-kb-troubleshooting-blocked-oauth"></a>

**Symptoms:**
+ Error message: "Your site admin must authorize this app for the site {{instance-name}}.atlassian.net before the app can access your account."
+ Choosing **Accept** in the consent dialog has no effect.

**Cause:**

Your Atlassian site administrator has blocked user-installed OAuth apps. When this setting is enabled, only a site or organization administrator can authorize new third-party apps.

**Resolution steps:**

Use one of the following options to resolve this issue.
+ **Option 1 (Recommended): Admin authorizes the app directly**

  1. An Atlassian site administrator navigates to Amazon Quick and starts a new knowledge base setup with Confluence Cloud.

  1. Because the administrator has site-level permissions, a clean consent screen appears without the error.

  1. The administrator chooses **Accept** to install the app.

  After the administrator authorizes the app, all other users on the site can connect without issues.
+ **Option 2: Temporarily allow user-installed apps** – An administrator goes to `admin.atlassian.com`, navigates to **Apps**, **Atlassian Apps**, then chooses the link for third-party and Marketplace apps. Under **Settings**, find **User Installed Apps** and toggle to allow user apps. After the user authorizes Amazon Quick, toggle the setting back to block user apps.

**Important**  
Admin authorization applies per Atlassian site, not per organization. If your company has multiple sites (for example, `team-a.atlassian.net` and `team-b.atlassian.net`), each site requires separate authorization.

**Note**  
While user-installed apps are unblocked (Option 2), any user on the site can authorize any OAuth app. Re-enable the block promptly after the user has connected.

### Authentication popup fails
<a name="confluence-kb-troubleshooting-auth-popup"></a>

**Symptoms:**
+ Authentication popup does not appear or closes immediately.
+ Popup appears but fails to complete the OAuth flow.

**Resolution steps:**

1. Verify that your browser allows popups from the Amazon Quick console domain.

1. Verify that your Confluence Cloud instance is accessible from your network.

1. Try using a different browser or clearing your browser cache.

### Missing content in knowledge base
<a name="confluence-kb-troubleshooting-missing-content"></a>

**Symptoms:**
+ Knowledge base sync completes but expected content is not indexed.
+ Search results do not include content from specific spaces or pages.
+ Only one document is indexed for an entire space.

**Resolution steps:**

1. Verify that the Confluence Cloud user who authenticated has access to the spaces and pages you selected during setup.

1. Check that the selected content types are supported (pages, blog posts, and attachments).

1. Review the content selection in your knowledge base configuration to confirm the correct spaces and pages are included.

1. Check your Confluence URLs for the `/overview` suffix. URLs that end with `/wiki/spaces/{{space-key}}/overview` are treated as a single page URL, not a full space. If you intended to index the entire space, use the space URL without `/overview` (for example, `https://{{company}}.atlassian.net/wiki/spaces/{{space-key}}`).

### ACL-related issues
<a name="confluence-kb-troubleshooting-acl"></a>

**No results from ACL-enabled knowledge base**
+ Verify that the end user has signed in to Confluence when prompted during their first query. The sign-in is required for real-time permission verification.
+ Verify that the end user has access to the relevant Confluence content in their Confluence instance.

**Documents skipped during sync**
+ If sync reports show items with status SKIPPED, verify that the authenticating user has access to the Confluence spaces and pages included in the knowledge base.
+ For more information about verifying document access, see [Check document access (ACL verification)](sync-reports-observability.md#sync-reports-acl-verification).