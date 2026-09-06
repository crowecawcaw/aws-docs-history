

# Connector overview
<a name="connectors-overview"></a>

Connectors integrate AWS Marketplace Storefront with external CRM and collaboration systems. Connectors fall into two categories: CRM connectors and notifications and collaboration connectors.

## Connector overview
<a name="connector-overview"></a>

The Connectors tab lists configured connectors in a table with columns Application, Account, Status, Inbound, Outbound, and Action. Choose the action menu in a row to manage that connector. To add a new connector, choose **\+ Add Connector**.

### Available connectors
<a name="connector-overview-available-connectors"></a>


| Category | Connector | Purpose | Data flow | 
| --- | --- | --- | --- | 
| CRM | AWS ACE | Co-selling opportunity sync with AWS | Bidirectional | 
| CRM | HubSpot | CRM integration for deal and contact sync | Bidirectional | 
| Notifications and collaboration | Slack | Sends storefront and deal notifications to a Slack workspace | Outbound | 

### How connectors work
<a name="connector-overview-how-connectors-work"></a>

1. **Connect** - Authenticate with the external system using credentials.

1. **Configure** - Map fields between Storefront and the external system.

1. **Activate** - Enable data synchronization.

Once activated, connectors run automatically based on configured triggers (real-time events or scheduled sync).

### To manage connectors
<a name="connector-overview-to-manage-connectors"></a>

1. Choose your profile avatar in the top-right corner.

1. Choose **Organization Settings**.

1. Choose the **Connectors** tab.

1. The page shows all available connectors with their current status:
   + **Connected** - Active and syncing
   + **Disconnected** - Configured but not active
   + **Not configured** - Available but not set up

1. Choose a connector to configure or manage it.

### Common connector actions
<a name="connector-overview-common-connector-actions"></a>
+ **Connect** - Provide credentials and establish the connection
+ **Test Connection** - Verify the integration is working
+ **Configure** - Set up field mappings and sync rules
+ **Disconnect** - Remove the integration (does not delete synced data)
+ **View Logs** - See sync history and errors

### Notes
<a name="connector-overview-notes"></a>
+ Each connector is configured at the organization level and applies to all accounts and storefronts within the organization.
+ Connector credentials are stored securely and encrypted.
+ If a connector encounters errors, it retries automatically. Persistent errors generate notifications.

### Related topics
<a name="connector-overview-related-topics"></a>
+ Workflow automation
+ Notification settings