

# Connecting DataDog
<a name="connecting-telemetry-sources-connecting-datadog"></a>

## Built-in, 1 way integration
<a name="built-in-1-way-integration"></a>

Currently, AWS DevOps Agent supports Datadog users with built-in, 1 way integration, enabling the following:
+ **Automated Investigation triggering** - Datadog events can be configured to trigger AWS DevOps Agent incident resolution Investigations via AWS DevOps Agent webhooks.
+ **Telemetry introspection** - AWS DevOps Agent can introspect Datadog telemetry as it investigates an issue via each provider's remote MCP server.

## Onboarding
<a name="onboarding"></a>

### Step 1: Connect
<a name="step-1-connect"></a>

Establish connection to your Datadog remote MCP endpoint with account access credentials

#### Configuration
<a name="configuration"></a>

1. Go to the **Capability Providers** page (accessible from the side navigation)

1. Find **Datadog** in the **Available** providers section under **Telemetry** and choose **Register**

1. Enter your Datadog MCP server details:
   + **Server Name** - Unique identifier (e.g., my-datadog-server)
   + **Endpoint URL** - Your Datadog MCP server endpoint. The endpoint URL varies depending on your Datadog site. See the Datadog site endpoint table below.
   + **Description** - Optional server description

1. Choose Next

1. Review and submit

#### Datadog site endpoints
<a name="datadog-site-endpoints"></a>

The MCP endpoint URL varies depending on your Datadog site. To identify your site, check the URL in your browser when logged into Datadog, or see [Access the Datadog site](https://docs.datadoghq.com/getting_started/site/#access-the-datadog-site).


| Datadog Site | Site Domain | MCP Endpoint URL | 
| --- | --- | --- | 
| US1 (default) | datadoghq.com | https://mcp.datadoghq.com/api/unstable/mcp-server/mcp | 
| US3 | us3.datadoghq.com | https://mcp.us3.datadoghq.com/api/unstable/mcp-server/mcp | 
| US5 | us5.datadoghq.com | https://mcp.us5.datadoghq.com/api/unstable/mcp-server/mcp | 
| EU1 | datadoghq.eu | https://mcp.datadoghq.eu/api/unstable/mcp-server/mcp | 
| AP1 | ap1.datadoghq.com | https://mcp.ap1.datadoghq.com/api/unstable/mcp-server/mcp | 
| AP2 | ap2.datadoghq.com | https://mcp.ap2.datadoghq.com/api/unstable/mcp-server/mcp | 

#### Authorization
<a name="authorization"></a>

Complete OAuth authorization by:
+ Authorizing as your user on the Datadog OAuth page
+ If not logged in, choose Allow, login, then authorize

Once configured, Datadog becomes available across all Agent spaces.

Each registration connects to one Datadog organization. To connect additional Datadog organizations, repeat this process for each one and give each registration its own **Server Name**.

### Step 2: Enable
<a name="step-2-enable"></a>

Activate DataDog in a specific Agent space and configure appropriate scoping

#### Configuration
<a name="configuration"></a>

1. From the agent spaces page, select an agent space and press view details (if you have not yet created an agent space see [Creating an Agent Space](getting-started-with-aws-devops-agent-creating-an-agent-space.md))

1. Select the Capabilities tab

1. Scroll down to the Telemetry section

1. Press Add

1. Choose the Datadog registration you want to enable.

1. Next

1. Review and press Save

1. Copy the Webhook URL and API Key (shown once at save; the API Key can't be viewed later — if you lose it, regenerate it from the webhook details on the Capabilities tab, which invalidates the previous key)

**Note:** For instructions on retrieving or rotating webhook credentials, see [Managing webhook credentials](configuring-integrations-and-knowledge-invoking-devops-agent-through-webhook.md).

A single Agent Space can use more than one Datadog registration. To add another registration, repeat these steps.

### Step 3: Configure webhooks
<a name="step-3-configure-webhooks"></a>

Using the Webhook URL and API Key from Step 2, you can configure Datadog to send events that trigger an investigation, such as when a monitor alerts.

Datadog webhooks use bearer token authentication. For the general webhook request format and payload schema, see [Invoking DevOps Agent through Webhook](configuring-integrations-and-knowledge-invoking-devops-agent-through-webhook.md). The following sections provide a ready-to-use Datadog configuration; you don't need to construct the payload yourself.

#### Step 3.1: Create the webhook in Datadog
<a name="step-31-create-the-webhook-in-datadog"></a>

1. In Datadog, open **Integrations**, search for **Webhooks**, and open the integration tile. For more information, see [Webhooks](https://docs.datadoghq.com/integrations/webhooks/) in the Datadog documentation.

1. Under **Webhooks**, choose **New**.

1. For **Name**, enter a name such as `devops-agent`. You reference this name as `@webhook-devops-agent` in monitor messages.

1. For **URL**, paste the Webhook URL from Step 2 (viewable again from the Datadog entry on your agent space's **Capabilities** tab).

1. For **Payload**, replace the default payload with the template in Step 3.2.

1. Leave **Auth Method** unconfigured, and instead select **Custom Headers** and enter the header shown in the following example, replacing `<API_KEY_FROM_STEP_2>` with the API Key from Step 2.

1. Leave **Encode as form** cleared. The webhook endpoint requires a raw JSON body; form encoding causes the payload to fail processing.

1. Save the webhook.

Custom header value for step 6:

```
{"Authorization": "Bearer <API_KEY_FROM_STEP_2>"}
```

To avoid storing the key in plain view, define a custom variable (for example, `$DEVOPS_AGENT_API_KEY`) in the webhook tile with **Hide from view** selected, and reference the variable in the header value instead.

#### Step 3.2: Payload template for monitor-triggered alerts
<a name="step-32-payload-template-for-monitor-triggered-alerts"></a>

The following template works for standard monitor alerts, including metric, log, APM, and Synthetics monitors. Datadog substitutes the `$VARIABLE` placeholders when it sends the webhook; leave them as written.

```
{
  "eventType": "incident",
  "incidentId": "datadog-$ALERT_CYCLE_KEY",
  "action": "created",
  "priority": "HIGH",
  "title": "$ALERT_TITLE",
  "description": "$TEXT_ONLY_MSG",
  "service": "datadog",
  "data": {
    "monitorId": "$ALERT_ID",
    "eventType": "$EVENT_TYPE",
    "alertQuery": "$ALERT_QUERY",
    "alertScope": "$ALERT_SCOPE",
    "alertMetric": "$ALERT_METRIC",
    "alertTransition": "$ALERT_TRANSITION",
    "alertPriority": "$ALERT_PRIORITY",
    "tags": "$TAGS",
    "eventUrl": "$LINK",
    "hostname": "$HOSTNAME"
  }
}
```

#### How Datadog variables map to the webhook schema
<a name="how-datadog-variables-map-to-the-webhook-schema"></a>


| Webhook field | Value to use | Notes | 
| --- | --- | --- | 
| eventType | The literal string incident | Required constant. | 
| incidentId | datadog-$ALERT\_CYCLE\_KEY | $ALERT\_CYCLE\_KEY stays the same from when a monitor triggers until it resolves, so re-notifications deduplicate into a single investigation. Use $ID (the per-event ID) instead only if you want every notification to start a separate investigation. | 
| action | The literal string created | Do not map $ALERT\_TRANSITION to this field. Its values (such as Triggered and Recovered) are not valid action values. Control when the webhook fires from the monitor message instead (see Step 3.3). | 
| priority | One of the literal strings CRITICAL, HIGH, MEDIUM, LOW, or MINIMAL | Do not use $ALERT\_PRIORITY here. It expands to Datadog monitor priorities (P1–P5), which are not valid values for this field. The webhook returns a 200 response, but no investigation starts. To send different priorities, create one webhook per priority level (for example, devops-agent-critical and devops-agent-high) and reference the appropriate webhook from each monitor. | 
| title | $ALERT\_TITLE | The monitor's alert title. | 
| description | $TEXT\_ONLY\_MSG | The event text with Markdown stripped. Prefer this over $EVENT\_MSG, whose Markdown formatting adds noise. | 
| service | A literal service name | Optional. A static string identifying the source, such as datadog or your service's name. | 
| timestamp | Omit | Optional. Datadog's date variables ($DATE, $DATE\_POSIX) are epoch values, not the ISO 8601 format this field expects, so omit the field. | 
| data | Datadog context variables | Optional but recommended. Everything in data is passed to the agent as the original event, giving the investigation the monitor query, scope, tags, and a link back to the Datadog event. | 

#### Step 3.3: Reference the webhook from your monitors
<a name="step-33-reference-the-webhook-from-your-monitors"></a>

In each monitor whose alerts should trigger an investigation, add the webhook mention to the monitor message, scoped so that only the alert transition fires it:

```
{{#is_alert}}
@webhook-devops-agent
{{/is_alert}}
```

Without the `{{#is_alert}}` conditional, warning and recovery notifications also send the webhook. Recovery events deduplicate against the open investigation through `$ALERT_CYCLE_KEY`, but warnings start investigations for thresholds you might not want investigated.

#### Verify the configuration
<a name="verify-the-configuration"></a>

Send a test notification from a monitor (**Test Notifications** in the monitor editor) and confirm the following:

1. **The webhook returns a 200 response.** You can see the delivery status in the Datadog webhook integration's event stream. A 4xx response means the `Authorization` header is wrong. Re-check the API Key and confirm that **Encode as form** is cleared.

1. **An investigation starts in your Agent Space.** (A test notification's investigation closes without root causes — that's expected.) A 200 response without an investigation means the payload failed validation after it was accepted. Check the webhook response body in the Datadog event stream: an invalid payload returns a 200 response whose body lists the validation errors (for example, `'P2' is not one of ['CRITICAL', 'HIGH', ...]`), while a valid payload returns `{"message": "Webhook received"}`. The most common causes are a non-literal `priority` value (see the preceding mapping table) and a duplicate `incidentId` from an earlier test in the same alert cycle.

For general webhook troubleshooting, see [Invoking DevOps Agent through Webhook](configuring-integrations-and-knowledge-invoking-devops-agent-through-webhook.md).

Learn more: [Datadog Remote MCP Server](https://www.datadoghq.com/blog/datadog-remote-mcp-server/)

## Removal
<a name="removal"></a>

The telemetry source is connected at two levels at the agent space level and at account level. To completely remove it you must first remove from all agent spaces where it is used and then it can be unregistered.

### Step 1: Remove from agent space
<a name="step-1-remove-from-agent-space"></a>

1. From the agent spaces page, select an agent space and press view details

1. Select the Capabilities tab

1. Scroll down to the Telemetry section

1. Select Datadog

1. Press remove

### Step 2: Deregister from account
<a name="step-2-deregister-from-account"></a>

1. Go to the **Capability Providers** page (accessible from the side navigation)

1. Scroll to the **Currently registered** section.

1. Check the agent space count is zero (if not repeat Step 1 above in your other agent spaces)

1. Select Datadog, then choose **Deregister** from the **Actions** menu.