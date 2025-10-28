# Set up integrations in the console

The Integrations console provides a streamlined interface for creating and managing integrations. When you access the Integrations tab, you see all available applications in a unified grid. The console setup process adapts based on the integration you select, your user tier, and existing integrations.

## Choose integration options

When you select an integration from the main grid, the console branches based on several factors:

- **Integration capabilities** - Each application
  supports different combinations of actions and knowledge base creation. For
  example, Google Drive supports data ingestion not actions. OneDrive supports
  both data ingestion and actions.
- **User tier** - Professional subscriptions enable
  you to create knowledge bases out of Google Drive, OneDrive, Confluence, and
  SharePoint. In order to set up actions and bring data from S3 and Web Crawler,
  you need to have the Enterprise subscriptions.
- **Existing integrations** - The console first shows existing integrations before offering to create new ones.

## View setup process examples

The following examples show how different integrations guide you through different console setup processes:

### Google Drive - Bring data for

Q&A

Google Drive supports data access integrations and knowledge base creation.

1. In the console, choose **Integrations**.
2. From the integration grid, choose **Google Drive**, and
   select the add icon.
3. The OAuth popup appears. Complete the OAuth process and grant it all the
   necessary permissions. Choose **Continue**.
4. You are taken to the Create knowledge base page. Select the files you want
   to assign to your knowledge base, and choose Select.
5. Enter a name and description. Choose **Create**.

### OneDrive - Perform actions and bring data for

Q&A

OneDrive supports the capabilities to both perform actions and bring data for
Q&A. The console provides options for both capabilities during setup.

1. In the console, choose **Integrations**.
2. From the integration grid, choose **OneDrive**.
3. In the Create Integration dialog, select your integration type:
   - **Perform actions in OneDrive** - Enables actions
     like creating, updating, or managing OneDrive files.
   - **Bring data from OneDrive** - Enables you to ask
     questions about and get insights from your OneDrive content.
   - **Both** - Combines task and data ingestion
     capabilities.

4. Enter integration details and configure Microsoft 365 authentication.
5. If you selected "Bring data from OneDrive", select the files you want to
   add to your knowledge base using the file picker interface.
6. Choose **Create** to complete the setup.

### Working with existing integrations

When you select an integration type that you've used before, the console first displays your existing integrations.

1. In the console, choose **Integrations**.
2. Choose an integration type you've used before (for example, **OneDrive**).
3. The console displays a table of existing integrations with columns for:
   - **Name** - Integration name
   - **Status** - The status of the integration (ex.
     Available, Completed with issues)
   - **Visibiliy** - The visilibity level of the
     integration (ex. Personal, Shared)
   - **Owner** - The integration creator
   - **Last Modified** - Most recent update
   - **Actions** - A dropdown menu to
     perform actions on existing integrations

4. Choose an existing integration to view details, or choose add
   **+** to set up an additional connection.

## Integration management options

After creating integrations, you can manage them through several console options:

- **Edit integration** - Modify integration settings, authentication details, and configuration options
- **Delete integration** - Remove integrations with confirmation dialogs to prevent accidental deletion
- **Knowledge base management** - Separate flows for creating, editing, and deleting knowledge bases associated with your integrations
