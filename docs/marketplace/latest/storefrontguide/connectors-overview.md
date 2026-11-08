

# Connector overview
<a name="connectors-overview"></a>

Connectors integrate AWS Marketplace Storefront with external customer relationship management (CRM), procurement, and collaboration systems. Connectors fall into three categories: CRM connectors, procurement catalog connectors, and notifications and collaboration connectors.

## Connector overview
<a name="connector-overview"></a>

The **Connectors** tab lists configured connectors in a table with columns Application, Account, Status, Inbound, Outbound, and Action. To manage a connector, choose the action menu in its row. To add a new connector, choose **\+ Add Connector**.

### Available connectors
<a name="connector-overview-available-connectors"></a>

The following connectors are available.


| Category | Connector | Purpose | Data flow | 
| --- | --- | --- | --- | 
| CRM | AWS ACE | Co-selling opportunity sync with AWS | Bidirectional | 
| Procurement catalog | Amazon Business | Imports Amazon Business products and prices into one storefront and adds a Buy button that sends buyers to Amazon Business | Inbound | 
| CRM | HubSpot | CRM integration for deal and contact sync | Bidirectional | 
| Notifications and collaboration | Slack | Sends storefront and deal notifications to a Slack workspace | Outbound | 

### How connectors work
<a name="connector-overview-how-connectors-work"></a>

Connectors work in the following stages:

1. **Connect** - Authenticate with the external system using credentials.

1. **Configure** - Map fields between Storefront and the external system.

1. **Activate** - Enable data synchronization.

After you activate a connector, it runs automatically based on its configured triggers (real-time events or scheduled sync).

The Amazon Business connector doesn't use field mapping. You enter API credentials, test the connection, and bind the connector to one storefront. For more information, see [Amazon Business connector](connector-amazon-business.md).

### To manage connectors
<a name="connector-overview-to-manage-connectors"></a>

1. Choose your profile avatar in the top-right corner.

1. Choose **Organization Settings**.

1. Choose the **Connectors** tab.

1. The page shows all available connectors with their current status:
   + **Connected** - Active and syncing
   + **Disconnected** - Configured but not active
   + **Not configured** - Available but not set up

1. To configure or manage a connector, choose it.

### Common connector actions
<a name="connector-overview-common-connector-actions"></a>

You can take the following actions on a connector:
+ **Connect** - Provide credentials and establish the connection
+ **Test Connection** - Verify that the integration is working
+ **Configure** - Set up field mappings and sync rules
+ **Disconnect** - Remove the integration (doesn't delete synced data)
+ **View Logs** - See sync history and errors

### Notes
<a name="connector-overview-notes"></a>

Keep the following in mind when you work with connectors:
+ You configure each connector at the organization level, and it applies to all accounts and storefronts in the organization. The exception is the Amazon Business connector, which you bind to one storefront. Its imported products and prices appear only in that storefront.
+ AWS Marketplace Storefront encrypts connector credentials and stores them securely.
+ If a connector encounters errors, it retries automatically. Persistent errors generate notifications.

### Related topics
<a name="connector-overview-related-topics"></a>
+ [Amazon Business connector](connector-amazon-business.md)
+ Workflow automation
+ Notification settings