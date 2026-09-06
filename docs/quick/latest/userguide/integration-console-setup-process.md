

# Set up integrations in the console
<a name="integration-console-setup-process"></a>

The console organizes integrations into separate categories based on their purpose. Use **Knowledge** to connect data sources for Q&A and insights. Use **Connectors** to set up connectors that perform operations in external applications. The setup process adapts based on the integration you select, your subscription, and existing integrations.

## Choose integration options
<a name="main-integration-choices"></a>

When you set up an integration, the console guides you based on several factors:
+ **Integration capabilities** – Each application supports different combinations of actions and knowledge base creation. For example, Google Drive supports both actions and knowledge base creation. Web Crawler supports knowledge base creation only.
+ **Subscription** – Configuring integrations requires an Enterprise subscription. This includes creating connectors, setting up knowledge bases, and managing integration settings. Users with a Professional subscription can use integrations that have been shared with them.
+ **Existing integrations** – When you choose a connector that already exists, the console shows your existing connectors before offering to create new ones.

## View setup process examples
<a name="setup-process-examples"></a>

The following examples show how different integrations guide you through different console setup processes.

### Google Drive – Set up a knowledge base
<a name="google-drive-kb-setup-flow"></a>

Google Drive supports knowledge base creation through user-managed or admin-managed authentication.

1. In the console, choose **Knowledge**.

1. Find **Google Drive** and choose the **Add** (\+) icon.

1. Choose your authentication method and complete the sign-in flow.

1. Enter a name and description for your knowledge base.

1. Select the files and folders you want to index, then choose **Create**.

### Google Drive – Set up an action connector
<a name="google-drive-action-setup-flow"></a>

Google Drive also supports connectors for performing file operations directly from .

1. In the console, choose **Connectors**.

1. Choose the **Create for your team** tab.

1. Find and choose **Google Drive**.

1. Enter a **Name** for your connector. Optionally, choose **\+ Add Description** to add a description.

1. Choose your **Connection type** and **OAuth Configuration**, then complete the authentication setup.

1. Review the available actions and choose **Publish**.

### Available connectors tab
<a name="available-connectors-tab"></a>

The **Available** tab on the Connectors page shows connectors that use managed OAuth and are ready to use without additional configuration. Users can connect directly by choosing **Connect** on the connector card.

1. In the console, choose **Connectors**.

1. On the **Available** tab, find the connector you want to use.

1. Choose **Connect**.

1. Complete the sign-in flow for the application.

### Working with existing connectors
<a name="existing-integration-reuse"></a>

When you choose a connector on the **Create for your team** tab that already exists, the console displays your existing connectors before offering to create a new one.

1. In the console, choose **Connectors**.

1. Choose the **Create for your team** tab.

1. Choose a connector that you've configured before.

1. A dialog appears showing your existing connectors. To use an existing connector, choose it. To create a new one, choose **No, create new**.

## Integration management options
<a name="integration-management-options"></a>

After creating integrations, you can manage them through several console options:
+ **Edit integration** – Modify integration settings, authentication details, and configuration options.
+ **Delete integration** – Remove integrations with confirmation dialogs to prevent accidental deletion.
+ **Knowledge base management** – Separate flows for creating, editing, and deleting knowledge bases associated with your integrations.