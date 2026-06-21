# Connector overview

Connectors integrate AWS Marketplace Storefront with external CRM and collaboration systems. Connectors fall into two categories: CRM connectors and notifications and collaboration connectors.

## Connector overview

The Connectors tab lists configured connectors in a table with columns Application, Account, Status, Inbound, Outbound, and Action. Choose the action menu in a row to manage that connector. To add a new connector, choose **+ Add Connector**.

### Available connectors

| Category                        | Connector | Purpose                                                      | Data flow     |
| ------------------------------- | --------- | ------------------------------------------------------------ | ------------- |
| CRM                             | AWS ACE   | Co-selling opportunity sync with AWS                         | Bidirectional |
| CRM                             | HubSpot   | CRM integration for deal and contact sync                    | Bidirectional |
| Notifications and collaboration | Slack     | Sends storefront and deal notifications to a Slack workspace | Outbound      |

### How connectors work

1. **Connect** - Authenticate with the external system using credentials.
2. **Configure** - Map fields between Storefront and the external system.
3. **Activate** - Enable data synchronization.

Once activated, connectors run automatically based on configured triggers (real-time events or scheduled sync).

### To manage connectors

1. Choose your profile avatar in the top-right corner.
2. Choose **Organization Settings**.
3. Choose the **Connectors** tab.
4. The page shows all available connectors with their current status:

   - **Connected** - Active and syncing
   - **Disconnected** - Configured but not active
   - **Not configured** - Available but not set up

5. Choose a connector to configure or manage it.

### Common connector actions

- **Connect** - Provide credentials and establish the connection
- **Test Connection** - Verify the integration is working
- **Configure** - Set up field mappings and sync rules
- **Disconnect** - Remove the integration (does not delete synced data)
- **View Logs** - See sync history and errors

### Notes

- Each connector is configured at the organization level and applies to all accounts and storefronts within the organization.
- Connector credentials are stored securely and encrypted.
- If a connector encounters errors, it retries automatically. Persistent errors generate notifications.

### Related topics

- Workflow automation
- Notification settings
