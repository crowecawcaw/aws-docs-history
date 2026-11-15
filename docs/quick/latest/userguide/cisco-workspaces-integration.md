

# Cisco Workspaces integration
<a name="cisco-workspaces-integration"></a>

Monitor Webex device health and workspace utilization directly from AWS Quick using natural language. With the Cisco Workspaces connector, you can inspect device inventory, review workspace metrics, and look up locations without leaving AWS Quick.

This connector supports OAuth 2.0 authentication with a Webex client ID and client secret. For more information about the authentication methods that AWS Quick supports, see [Authentication methods](quick-action-auth.md).

## Prerequisites
<a name="cisco-workspaces-prerequisites"></a>

Before you set up the connector, verify that you have the following resources and access.
+ An active Cisco Webex organization with access to Webex Control Hub.
+ A Control Hub administrator who has provisioned the Model Context Protocol (MCP) server for Cisco Workspaces and its tools for your organization.
+ A registered Webex OAuth application with the required scopes. See [Configuring Cisco Workspaces](#cisco-workspaces-source-setup).
+ A subscription that meets the requirements described in [Set up integrations in the console](integration-console-setup-process.md).

## Configuring Cisco Workspaces
<a name="cisco-workspaces-source-setup"></a>

Prepare the Webex side before you create the connector in AWS Quick.

1. Sign in to Webex Control Hub as an organization administrator and confirm that the MCP server for Cisco Workspaces is provisioned.

1. Register or open the Webex OAuth application that AWS Quick will use. Set the issuer to `https://webexapis.com`. Grant the application the following scopes: `spark:mcp spark-admin:devices_read spark-admin:workspace_metrics_read spark-admin:workspaces_read spark-admin:workspace_locations_read`.

1. Add the AWS Quick callback URL as a redirect URI: `https://{{region}}.quicksight.aws.amazon.com/sn/oauthcallback`. Replace {{region}} with your AWS Region, for example, `us-east-1`.

1. Record the client ID and client secret. You enter these when you set up the connector in AWS Quick.

## Setting up the integration in AWS Quick
<a name="cisco-workspaces-integration-setup"></a>

After you configure Cisco Workspaces, create the connector in AWS Quick.

1. In the AWS Quick console, choose **Connectors**, and then choose **Model Context Protocol** to start a new custom MCP connector.

1. For **Name**, enter a descriptive name. For **MCP Server URL**, enter `https://mcp.webexapis.com/mcp/workspaces`.

1. For **Connection type**, choose **Public network**. For **OAuth Configuration**, enter the client ID, client secret, authorization URL, token URL, scopes, and redirect URL.

1. Choose **Next**. If a Webex authorization window appears, review the requested access and choose **Allow**.

1. On the **Publish** page, specify who can access the connector and choose **Publish**.

## Using available actions
<a name="cisco-workspaces-integration-actions"></a>

After you set up the connector, you can use the following tool groups from Cisco Workspaces.


**Cisco Workspaces available actions**  

| Group | Description | 
| --- | --- | 
| Devices (10 tools) | Inspect device inventory, configuration, and event history. Includes device\_search, device\_event\_history, device\_configuration\_list, and others. | 
| Workspaces (5 tools) | Retrieve utilization, capacity, and popularity metrics. Includes workspace\_search, workspace\_metrics, and others. | 
| Locations (1 tool) | Look up locations configured for your organization. Tool: location\_search. | 

To see the current set of actions, open the connector's **Available actions** view in the AWS Quick console.

## Troubleshooting
<a name="cisco-workspaces-troubleshooting"></a>

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations).

The following issues can occur when you set up or use the connector.

### Authentication fails or returns an authorization error
<a name="cisco-workspaces-troubleshoot-auth-fail"></a>

Confirm that the client ID and client secret are entered correctly and have not expired.

### A tool returns a permissions error
<a name="cisco-workspaces-troubleshoot-permission"></a>

Verify that all five required scopes are granted to the Webex application. A missing scope disables the tools that depend on it.

### Server rejects the connection
<a name="cisco-workspaces-troubleshoot-server"></a>

Ask your Webex Control Hub administrator to confirm that the MCP server for Cisco Workspaces is provisioned for your organization.

### Redirects fail or authorization window doesn't complete
<a name="cisco-workspaces-troubleshoot-redirect"></a>

Confirm that the AWS Quick callback URL is registered as a redirect URI on the Webex application and that {{region}} matches your AWS Region.