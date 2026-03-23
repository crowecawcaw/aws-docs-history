# Integration workflows

The following procedures describe the general workflows for creating and managing different types of integrations in Amazon Quick.

## Creating a knowledge base from scratch

Data access integrations establish the connection to external systems creating
knowledge bases from external data sources.

1. In the Amazon Quick console, choose **Integrations**.
2. Choose the **Knowledge bases** tab.
3. From the integration grid, choose the application you want to connect to (for example, **Google Drive**, **OneDrive**, or **S3**).
4. In the Integration details section, select the "Add" option (**+**). If required, complete the authentication process
   in the popup that occurs.
5. Fill in the appropriate details, depending on your chosen integration. For
   example, for Amazon S3, select your AWS account and your Amazon S3 bucket url.
6. Enter a **Name** for your integration.
7. Enter the required connection details for your chosen application.
8. If required, choose **Create and continue** to
   continue to knowledge base creation.
9. Specify a name for your knowledge base.
10. Specify the files you want to include in your knowledge base using the file
    picker or appropriate sync options (for example, **S3** allows you to choose to add all content of specific
    content).
11. Choose **Create**.

Syncing of your content will automatically begin after creation of the
knowledge base.

## Creating an action connector

Action Connectors enable you to perform actions in external applications directly from
Amazon Quick.

1. In the Amazon Quick console, choose **Integrations**.
2. Choose the **Actions** tab.
3. From the integration grid, choose an application that supports action connectors (for example, **OneDrive**, **Confluence**, or **Slack**).
4. In the Integration details section, select the "Add" option (**+**).
5. Enter a **Name** for your action connector.
6. Configure the task-specific settings for your chosen application.
7. Choose **Next** to complete the authentication
   and setup process.

After successful creation, your action connector is available for use in Amazon Quick workflows and can be triggered from analyses, dashboards, or automated processes.

## Managing existing integrations

You can edit, delete, share, and manage existing integrations from the Integrations console. You can access management options from the integrations list or from an integration's details page.

### To edit an integration

From the integrations list:

1. In the Amazon Quick console, choose **Integrations**.
2. Choose the **Knowledge bases** or **Actions** tab.
3. Choose the **Open menu** icon in the row of the integration you want to edit.
4. Choose **Edit**.
5. Modify the integration settings as needed and choose **Save changes**.

You can also edit from the integration details page by choosing the integration name, then choosing the menu icon (⋮) and selecting **Edit**.

### To delete an integration

From the integrations list:

1. In the Amazon Quick console, choose **Integrations**.
2. Choose the **Knowledge bases** or **Actions** tab.
3. Choose the **Open menu** icon in the row of the integration you want to delete.
4. Choose **Delete**.
5. In the confirmation dialog, review the integration details and choose **Delete** to confirm.

You can also delete from the integration details page by choosing the integration name, then choosing the menu icon (⋮) and selecting **Delete**.

The integration is permanently removed from your account. Any dependent resources
(such as knowledge bases) that rely on this integration will be impacted.

### To share an integration

From the integrations list, choose the **Open menu** icon in the row of the integration and choose **Share**. You can also choose **Share** from the integration details page.

### Managing action connectors

Action connector integrations have additional management options available from the integration details page.

**Sign in or re-connect**

For integrations that use user-based OAuth authentication, you must sign in to the server before you can use its actions. If you have not yet signed in, a **Sign in** button appears at the top of the details page. After you sign in, the button changes to **Re-Connect**, which you can use to re-authenticate if your session expires or the connection is interrupted.

**Test action APIs**

Choose **Test action APIs** in the Actions section of the details page to test individual actions provided by the integration. This lets you verify that the connection is working correctly and that the server responds as expected.

###### Note

The **Test action APIs** option is available for action connectors only. Knowledge base integrations do not support action testing.
