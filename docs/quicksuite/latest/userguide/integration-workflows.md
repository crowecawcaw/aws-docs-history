# Integration workflows

The following procedures describe the general workflows for creating and managing different types of integrations in Amazon Quick Suite.

## Creating a knowledge base from scratch

Data access integrations establish the connection to external systems creating
knowledge bases from external data sources.

1. In the Amazon Quick Suite console, choose **Integrations**.
2. From the integration grid, choose the application you want to connect to (for example, **Google Drive**, **OneDrive**, or **S3**).
3. In the Integration details section, select the "Add" option (**+**). If required, complete the authentication process
   in the popup that occurs.
4. Fill in the appropriate details, depending on your chosen integration. For
   example, for Amazon S3, select your AWS account and your Amazon S3 bucket url.
5. Enter a **Name** for your integration.
6. Enter the required connection details for your chosen application.
7. If required, choose **Create and continue** to
   continue to knowledge base creation.
8. Specify a name for your knowledge base.
9. Specify the files you want to include in your knowledge base using the file
   picker or appropriate sync options (for example, **S3** allows you to choose to add all content of specific
   content).
10. Choose **Create**.

Syncing of your content will automatically begin after creation of the
knowledge base.

## Creating an action connector

Action Connectors enable you to perform actions in external applications directly from
Amazon Quick Suite.

1. In the Amazon Quick Suite console, choose **Integrations**.
2. From the integration grid, choose an application that supports action connectors (for example, **OneDrive**, **Confluence**, or **Slack**).
3. In the Integration details section, select the "Add" option (**+**).
4. Enter a **Name** for your action connector.
5. Configure the task-specific settings for your chosen application.
6. Choose **Next** to complete the authentication
   and setup process.

After successful creation, your action connector is available for use in Amazon Quick Suite workflows and can be triggered from analyses, dashboards, or automated processes.

## Creating a knowledge base integration from an existing data access integration

Knowledge base integrations allow you to create searchable repositories of information
from external sources.

Follow the procedure below to quickly create a knowledge base for one of the six
supported data sources.

1. Open the Amazon Quick Suite console and choose **Integrations**.
   Then click on the **Data** tab.
2. Select your data source from the available options in the
   **Data** tab,
3. Selecting the three-dot menu option under **Actions**, and
   then select **Create knowledge base**.
4. Add a name and enter an optional description.
5. Select the content to include in your knowledge base. Choose
   **Create**.

Data synchronization begins automatically. Sync jobs can take a few mins to hours
depending upon the size of your data, but you can see what documents are available for
querying from the Refresh Reports tab. The knowledge base status changes from
_Syncing_ to _Available_ when the sync is
complete.

## Managing existing integrations

You can edit, delete, and manage existing integrations from the Integrations console.

1. In the Amazon Quick Suite console, choose **Integrations**.
2. From the integrations table, select the integration you want to modify.
3. Select the three-dot drop-down menu under "Actions"and then select "Edit
   integration".
4. Modify the integration settings as needed.
5. Choose **Save changes** to apply your modifications.

Your integration settings are updated and the changes take effect immediately for new operations using the integration.

### To delete an integration

1. In the Amazon Quick Suite console, choose **Integrations**.
2. From the integrations table, select the integration you want to remove.
3. Select the three-dot drop-down menu under "Actions"and then select "Delete
   integration".
4. In the confirmation dialog, review the integration details and any dependent resources that will be affected.
5. Choose **Delete** to confirm the removal.

The integration is permanently removed from your account. Any dependent resources
(such as knowledge bases) that rely on this integration will be impacted.
