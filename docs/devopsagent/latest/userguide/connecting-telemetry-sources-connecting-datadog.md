# Connecting DataDog

## Built-in, 1 way integration

Currently, AWS DevOps Agent supports Datadog users with built-in, 1 way integration, enabling the following:

- **Automated Investigation triggering** - Datadog events can be configured to trigger AWS DevOps Agent incident resolution Investigations via AWS DevOps Agent webhooks.
- **Telemetry introspection** - AWS DevOps Agent can introspect Datadog telemetry as it investigates an issue via each provider's remote MCP server.

## Onboarding

### Step 1: Connect

Establish connection to your Datadog remote MCP endpoint with account access credentials

#### Configuration

1. Go to the **Capability Providers** page (accessible from the side navigation)
2. Find **Datadog** in the **Available** providers section under **Telemetry** and click **Register**
3. Enter your Datadog MCP server details:
   - **Server Name** - Unique identifier (e.g., my-datadog-server)
   - **Endpoint URL** - Your Datadog MCP server endpoint. The endpoint URL varies depending on your Datadog site. See the Datadog site endpoint table below.
   - **Description** - Optional server description

4. Click Next
5. Review and submit

#### Datadog site endpoints

The MCP endpoint URL varies depending on your Datadog site. To identify your site, check the URL in your browser when logged into Datadog, or see [Access the Datadog site](https://docs.datadoghq.com/getting_started/site/#access-the-datadog-site "https://docs.datadoghq.com/getting_started/site/#access-the-datadog-site").

| Datadog Site  | Site Domain         | MCP Endpoint URL                                            |
| ------------- | ------------------- | ----------------------------------------------------------- |
| US1 (default) | `datadoghq.com`     | `https://mcp.datadoghq.com/api/unstable/mcp-server/mcp`     |
| US3           | `us3.datadoghq.com` | `https://mcp.us3.datadoghq.com/api/unstable/mcp-server/mcp` |
| US5           | `us5.datadoghq.com` | `https://mcp.us5.datadoghq.com/api/unstable/mcp-server/mcp` |
| EU1           | `datadoghq.eu`      | `https://mcp.datadoghq.eu/api/unstable/mcp-server/mcp`      |
| AP1           | `ap1.datadoghq.com` | `https://mcp.ap1.datadoghq.com/api/unstable/mcp-server/mcp` |
| AP2           | `ap2.datadoghq.com` | `https://mcp.ap2.datadoghq.com/api/unstable/mcp-server/mcp` |

#### Authorization

Complete OAuth authorization by:

- Authorizing as your user on the Datadog OAuth page
- If not logged in, click Allow, login, then authorize

Once configured, Datadog becomes available across all Agent spaces.

### Step 2: Enable

Activate DataDog in a specific Agent space and configure appropriate scoping

#### Configuration

1. From the agent spaces page, select an agent space and press view details (if you have not yet created an agent space see [Creating an Agent Space](getting-started-with-aws-devops-agent-creating-an-agent-space.md "getting-started-with-aws-devops-agent-creating-an-agent-space.md"))
2. Select the Capabilities tab
3. Scroll down to the Telemetry section
4. Press Add
5. Select Datadog
6. Next
7. Review and press Save
8. Copy the Webhook URL and API Key

### Step 3: Configure webhooks

Using the Webhook URL and API Key you can configure Datadog to send events to trigger an investigation, for example from an alarm.

Datadog webhooks use bearer token authentication. For the complete webhook request format, payload schema, and example code, see [Invoking DevOps Agent through Webhook](configuring-capabilities-for-aws-devops-agent-invoking-devops-agent-through-webhook.md "configuring-capabilities-for-aws-devops-agent-invoking-devops-agent-through-webhook.md"). Use the Version 2 (Bearer token authentication) examples, setting the `Authorization: Bearer <Token>` header with the API Key from Step 2.

Send webhooks with Datadog [https://docs.datadoghq.com/integrations/webhooks/](https://docs.datadoghq.com/integrations/webhooks/ "https://docs.datadoghq.com/integrations/webhooks/") (note select no authorization and instead use the custom header option).

Learn more: [Datadog Remote MCP Server](https://www.datadoghq.com/blog/datadog-remote-mcp-server/ "https://www.datadoghq.com/blog/datadog-remote-mcp-server/")

## Removal

The telemetry source is connected at two levels at the agent space level and at account level. To completely remove it you must first remove from all agent spaces where it is used and then it can be unregistered.

### Step 1: Remove from agent space

1. From the agent spaces page, select an agent space and press view details
2. Select the Capabilities tab
3. Scroll down to the Telemetry section
4. Select Datadog
5. Press remove

### Step 2: Deregister from account

1. Go to the **Capability Providers** page (accessible from the side navigation)
2. Scroll to the **Currently registered** section.
3. Check the agent space count is zero (if not repeat Step 1 above in your other agent spaces)
4. Press Deregister next to Datadog
