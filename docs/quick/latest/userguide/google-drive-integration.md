# Google Drive integration

With Google Drive integration in Amazon Quick, you can create knowledge bases from
documents stored in Google Drive. This integration supports data access capabilities for
indexing and searching Google Drive content including Google Docs, Sheets, and
Slides.

## What you can do

Google Drive users can ask questions about content stored in their Google Drive. For
example, users can inquire about key findings from Google Docs, presentation highlights
from Google Slides, or search for specific information across multiple document types.
The integration enables users to quickly access and understand information from their
Google Drive content, regardless of file location or type, while providing contextual
details such as publication dates, modification history, and document ownership—all
contributing to more efficient information discovery and better-informed decision
making.

###### Note

Google Drive integration supports data ingestion only. It doesn't provide action
capabilities for managing Google Drive files through APIs.

## Before you begin

Before you set up Google Drive integration, make sure you have the following:

- Google account with Google Drive access.
- Google Drive files and folders to index
- Amazon Quick Professional subscription or
  higher.

## Prepare Google Drive authentication

Google Drive integration uses managled three-legged OAuth (3LO) authentication. Before setting up the
integration in Amazon Quick, understand the authentication process and required
permissions:

### Authentication methods

**Managed three-legged OAuth (3LO)**

Personal access method for individual Google Drive content:

- Requires user authentication and consent
- Provides access to personal and shared content

### Required permissions and scopes

Amazon Quick requests the following Google Drive permissions during authentication:

- `https://www.googleapis.com/auth/drive.readonly` - Read-only access to Google Drive files and folders
- `https://www.googleapis.com/auth/drive.metadata.readonly` - Read-only access to file metadata, sharing settings, and properties

### OAuth authentication process

During the integration setup, you will be prompted to:

1. Select your Google account from the list or sign in with your credentials.
2. Review the permissions that Amazon Quick is requesting:
   - See and download all your Google Drive files.
   - See information about your Google Drive files.

3. Select both permissions and click **Continue** to grant
   permissions and complete the authentication process.

## Set up Google Drive integration

After understanding the authentication requirements, follow these steps to create your Google Drive integration:

1. In the Amazon Quick console, choose **Integrations**.
2. Click **Add** (plus "+" button).
3. Select your account and complete the authentication process.
4. Select **Continue**.
5. On the "Add files or folders" section, select the files to place in your
   knowledge base. You select the files you want Amazon Quick to sync with using a
   point-and-click experience.
6. Complete the knowledge base details:
   - **Name** - Enter a descriptive name for your knowledge base.
   - **Description** (optional) - Describe the purpose of this knowledge
     base.

7. Select **Create**.

After clicking create, the data sync is started automatically.

## Manage knowledge bases

After setting up your Google Drive integration, you can create and manage knowledge bases from your Google Drive content.

### Edit existing knowledge bases

You can modify your existing Google Drive knowledge bases:

1. In the Amazon Quick console, choose **Knowledge bases**.
2. Select your Google Drive knowledge base from the list.
3. Choose the three-dot icon under **Actions**, then choose
   **Edit knowledge base**.
4. Update your configuration settings as needed and choose **Save**.

### Create additional knowledge bases

You can create multiple knowledge bases from the same Google Drive integration:

1. In the Amazon Quick console, choose **Integrations**, and
   then select the **Data** tab.
2. Choose your existing Google Drive integration from the list.
3. Choose the three-dot icon under **Actions**, then choose
   **Create knowledge base**.
4. Configure your knowledge base settings and choose **Create**.

For detailed information about knowledge base configuration options, see [Common configuration settings](knowledge-base-integrations.md#common-configuration-settings "knowledge-base-integrations.md#common-configuration-settings").

###### Note

Amazon Quick doesn’t sync ACLs from data sources. When you create a knowledge base in Amazon Quick,
by default only you can get insights from the knowledge base.
For shared content, you can provide access to different users and groups by updating the knowledge base permissions.

## Limitations

When using Google Drive integrations in Amazon Quick, be aware of the following
limitations:

- File comments synchronization is not supported..
