# Connecting New Relic

## Built-in, 1 way integration

Currently, AWS DevOps Agent supports New Relic users with built-in, 1 way integration, enabling the following:

- **Automated Investigation triggering** - New Relic events can be configured to trigger AWS DevOps Agent incident resolution Investigations via AWS DevOps Agent webhooks.
- **Telemetry introspection** - AWS DevOps Agent can introspect New Relic telemetry as it investigates an issue via each provider's remote MCP server.

## Onboarding

### Step 1: Connect

Establish connection to your New Relic remote MCP endpoint with account access credentials

Please use a Full Platform User (not Basic/Core) in New relic to enable New Relic MCP tools.

#### Configuration

1. Go to the **Capability Providers** page (accessible from the side navigation)
2. Find **New Relic** in the **Available** providers section under **Telemetry** and choose **Register**
3. Follow the instructions to obtain your New Relic API Key
4. Enter your New Relic MCP server API Key details:

   - **Account ID:** Enter your New Relic account ID obtained above
   - **API Key:** Enter the API Key obtained above
   - **Select US or EU region** based on where your New Relic account is.

5. Choose Add

Each registration connects to one New Relic account. To connect additional New Relic accounts, repeat this process for each one.

### Step 2: Enable

Activate New Relic in a specific Agent space and configure appropriate scoping

#### Configuration

1. From the agent spaces page, select an agent space and press view details (if you have not yet created an agent space see [Creating an Agent Space](getting-started-with-aws-devops-agent-creating-an-agent-space.md "getting-started-with-aws-devops-agent-creating-an-agent-space.md"))
2. Select the Capabilities tab
3. Scroll down to the Telemetry section
4. Press Add
5. Choose the New Relic registration you want to enable.
6. Next
7. Review and press Save
8. Copy the Webhook URL and API Key

A single Agent Space can use more than one New Relic registration. To add another registration, repeat these steps.

### Step 3: Configure webhooks

Using the Webhook URL and API Key you can configure New Relic to send events to trigger an investigation, for example from an alarm. For more details on setting up webhooks, see [Change tracking webhooks](https://docs.newrelic.com/docs/change-tracking/change-tracking-webhooks/ "https://docs.newrelic.com/docs/change-tracking/change-tracking-webhooks/").

New Relic webhooks use bearer token authentication. For the complete webhook request format, payload schema, and example code, see [Invoking DevOps Agent through Webhook](configuring-integrations-and-knowledge-invoking-devops-agent-through-webhook.md "configuring-integrations-and-knowledge-invoking-devops-agent-through-webhook.md"). Use the Version 2 (Bearer token authentication) examples, setting the `Authorization: Bearer <Token>` header with the API Key from Step 2.

Send webhooks with New Relic [https://newrelic.com/instant-observability/webhook-notifications](https://newrelic.com/instant-observability/webhook-notifications "https://newrelic.com/instant-observability/webhook-notifications"). You can either select Bearer token for the authorization type, or select no authorization and add the `Authorization: Bearer <Token>` as a custom header instead.

Learn more: [https://docs.newrelic.com/docs/agentic-ai/mcp/overview/](https://docs.newrelic.com/docs/agentic-ai/mcp/overview/ "https://docs.newrelic.com/docs/agentic-ai/mcp/overview/")

## Removal

The telemetry source is connected at two levels at the agent space level and at account level. To completely remove it you must first remove from all agent spaces where it is used and then it can be unregistered.

### Step 1: Remove from agent space

1. From the agent spaces page, select an agent space and press view details
2. Select the Capabilities tab
3. Scroll down to the Telemetry section
4. Select New Relic
5. Press remove

### Step 2: Deregister from account

1. Go to the **Capability Providers** page (accessible from the side navigation)
2. Scroll to the **Currently registered** section.
3. Check the agent space count is zero (if not repeat Step 1 above in your other agent spaces)
4. Select New Relic, then choose **Deregister** from the **Actions** menu.
