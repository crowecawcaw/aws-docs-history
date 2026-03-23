# Google Drive knowledge base integration

Use the Google Drive knowledge base integration to index Google Drive content
so that Amazon Quick agents can search and answer questions about it.

## Google Drive capabilities

With the Google Drive integration, you can ask questions about content stored
in your Google Drive. For example, you can find key findings from Google Docs,
presentation highlights from Google Slides, or specific information across
multiple document types. Responses include contextual details such as publication
dates, modification history, and document ownership.

###### Note

Google Drive integration supports data ingestion only. It does not provide
action capabilities for managing Google Drive files through APIs.

## Before you begin

Make sure you have the following before you set up the integration.

- A Google account with Google Drive access.
- Google Drive files and folders to index.
- For subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md "integration-console-setup-process.md").

## Authentication

For knowledge base integrations, Amazon Quick handles authentication through a
popup flow during setup. Google Drive integration uses managed three-legged OAuth
(3LO) authentication.

1. Complete the Google sign-in popup that appears.
2. Review the permissions that Amazon Quick is requesting.
3. Select both permissions and choose **Continue** to
   grant access and complete the authentication process.

### Permissions granted during consent

When you authorize the connection, Amazon Quick requests the following
permissions from your Google account:

See and download all your Google Drive files

- See your Google Drive files
- Download your files
- See the names and emails of people you share files with

See information about your Google Drive files

- The titles and descriptions of your files
- The names and email addresses of people you share files with
- Your folders and how files are organized

###### Note

You can review and remove this access at any time from your Google
Account permissions settings.

## Set up the knowledge base integration

1. In the Amazon Quick console, in the navigation pane under
   **Connect apps and data**, choose
   **Integrations**.
2. Choose the **Knowledge bases** tab.
3. Under **Set up new knowledge base**, find
   **Google Drive** and choose the
   **Add** (+) icon.
4. In the **Create Google Drive knowledge base** dialog,
   under **Connected account**, select
   an existing Google Drive connection or choose
   **+ Add account** to connect a new Google account. If
   you add a new account, complete the Google sign-in and consent
   flow.
5. Under **Create knowledge base**, enter a name and
   an optional description for your knowledge base.
6. In the **Content** section, choose
   **Add content** to select the Google Drive files and
   folders to index.
7. In the **Add files or folders** dialog, browse your
   Google Drive content using the following tabs:
   - **My Drive** – Files and folders from your
     personal drive.
   - **Shared with me** – Files and folders that
     others have shared with you.
   - **Shared drives** – Files and folders from
     shared drives in your organization.

8. Select the files or folders to include and choose
   **Select**.
9. Review the selected content in the **Content** table.
   To remove an item, choose the delete icon in the
   **Actions** column.
10. Choose **Create**.

After you choose **Create**, the data sync starts
automatically.

## Supported content types

In addition to the common file types supported across all knowledge base
integrations, the Google Drive connector supports the following Google
Workspace-specific formats:

- **Google Workspace files:** Google Docs,
  Google Sheets, Google Slides

For more information about supported file types, size limits, and content
processing options, see [Common configuration settings](knowledge-base-integrations.md#common-configuration-settings "knowledge-base-integrations.md#common-configuration-settings").

## Access controls

###### Important

Amazon Quick does not sync access control lists (ACLs) from data sources.
When you create a knowledge base in Amazon Quick, by default, only you can
get insights from the knowledge base. To share content, update the knowledge
base permissions to provide access to different users and groups.

## Manage knowledge bases

After you set up your Google Drive integration, you can manage your knowledge
bases.

### Edit existing knowledge bases

1. In the Amazon Quick console, choose **Knowledge
   bases**.
2. Select your Google Drive knowledge base from the list.
3. Choose the three-dot icon under **Actions**, then
   choose **Edit knowledge base**.
4. Update your configuration settings as needed and choose
   **Save**.

## Manage and troubleshoot

For instructions on editing, sharing, or deleting your integration, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations "integration-workflows.md#managing-existing-integrations").

For more information about knowledge base troubleshooting, including sync
issues and missing documents, see [Troubleshooting knowledge bases](troubleshooting-knowledge-bases.md "troubleshooting-knowledge-bases.md").

### Google Drive-specific issues

- **Authentication popup fails** –
  Verify that your browser allows popups from the Amazon Quick console
  domain. Try using a different browser or clearing your browser
  cache.
- **Permissions revoked** – If you
  previously revoked Amazon Quick access from your Google Account
  permissions settings, you need to re-authenticate by editing the
  integration and signing in again.
- **Missing content** – Verify that the
  Google account that you used for authentication has access to the
  files and folders you selected. Content that was shared with you
  after the initial sync requires a resync to be indexed.
- **Google API rate limiting** – Google
  Drive might throttle requests during high usage periods. If syncs
  fail or are incomplete, retry during off-peak hours.

## Limitations

When using Google Drive integrations in Amazon Quick, be aware of the following
limitations:

- File comments synchronization is not supported.
