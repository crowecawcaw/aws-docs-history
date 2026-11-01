

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

#### Choosing an authentication method
<a name="choosing-an-authentication-method"></a>

You connect AWS DevOps Agent to the Datadog Model Context Protocol (MCP) server through one of three authentication methods. You choose the method when you register Datadog. The method stays the same for the life of the registration.

The **Authentication method** setting has the following options:
+ **OAuth** – Uses Open Authorization (OAuth) 2.0, with a sign-in to your Datadog account. AWS DevOps Agent registers its own OAuth client through dynamic client registration (DCR). For more information about DCR, see [OAuth 2.0 Dynamic Client Registration Protocol](https://datatracker.ietf.org/doc/html/rfc7591) on the IETF website.
+ **API key and application key** – Uses a Datadog API key and a Datadog application key. For more information about these keys, see [API and Application Keys](https://docs.datadoghq.com/account_management/api-app-keys/) on the Datadog website.
+ **Access token** – Uses a Datadog personal access token or service access token. For more information about these tokens, see [Personal Access Tokens](https://docs.datadoghq.com/account_management/personal-access-tokens/) and [Service Access Tokens](https://docs.datadoghq.com/account_management/service-access-tokens/) on the Datadog website.

With OAuth or a personal access token, you use your own Datadog user identity. With a service access token, you connect as a Datadog service account, which doesn't belong to a person. With an application key, you connect as the key owner. For more information about each method, see [Set Up the Datadog MCP Server](https://docs.datadoghq.com/mcp_server/setup/) on the Datadog website.

A Datadog administrator must turn on **MCP Access** in **Organization Settings**, and **MCP Write Access** for agent-action (write) tools. The Datadog account that you connect with must also have the MCP read permission. For agent-action tools, it must have the MCP write permission too. The Datadog Standard Role includes both permissions by default.

#### Configuration
<a name="configuration"></a>

Before you register Datadog, make sure that the following are true:
+ You know the MCP endpoint URL for your Datadog site.
+ You have the Datadog credentials for the authentication method that you chose.

To register Datadog with AWS DevOps Agent:

1. Open the [Capability Providers page](https://console.aws.amazon.com/devops-agent/home#/services) in the AWS DevOps Agent console.

1. On the **Capability Providers** page, choose **Register** for **Datadog**.

1. On the server details page, enter the following values:
   + For **Server Name**, enter a unique name for the registration.
   + For **Endpoint URL**, enter the MCP endpoint URL for your Datadog site.
   + (Optional) For **Description**, enter a description of the server.

1. For **Authentication method**, select the method that you chose.

1. Enter the credentials for the method that you selected:
   + For API key and application key, enter your keys in **API key** and **Application key**.
   + For Access token, enter your personal access token or service access token in **Access token**.
   + For OAuth, continue to the next step.

1. Choose **Next**.

1. On the **Review and Submit** page, choose **Add**.

After Datadog accepts the credentials, the registration appears on the **Capability Providers** page. If Datadog rejects them, you can return to the previous steps, correct the values, and choose **Add** again.

#### Datadog site endpoints
<a name="datadog-site-endpoints"></a>

The MCP endpoint URL varies depending on your Datadog site. To identify your site, check the URL in your browser when logged into Datadog, or see [Access the Datadog site](https://docs.datadoghq.com/getting_started/site/#access-the-datadog-site).

**Note**  
** Ensure the endpoint URL matches your Datadog site region. Using an incorrect region might result in registration failures.


| Datadog site | Site domain | MCP endpoint URL | 
| --- | --- | --- | 
| AP1 | ap1.datadoghq.com | https://mcp.ap1.datadoghq.com/v1/mcp | 
| AP2 | ap2.datadoghq.com | https://mcp.ap2.datadoghq.com/v1/mcp | 
| EU1 | datadoghq.eu | https://mcp.datadoghq.eu/v1/mcp | 
| UK1 | uk1.datadoghq.com | https://mcp.uk1.datadoghq.com/v1/mcp | 
| US1 (default) | datadoghq.com | https://mcp.datadoghq.com/v1/mcp | 
| US3 | us3.datadoghq.com | https://mcp.us3.datadoghq.com/v1/mcp | 
| US5 | us5.datadoghq.com | https://mcp.us5.datadoghq.com/v1/mcp | 

#### Selecting Datadog toolsets
<a name="selecting-datadog-toolsets"></a>

By default, only the core Datadog toolset is available at the endpoint. A toolset is a group of the MCP tools that Datadog exposes through its remote MCP server. To expose more of these tools, append the `toolsets` query parameter to your endpoint URL. Use `?toolsets=all` to enable every available toolset. To enable specific toolsets, pass a comma-separated list. You can use an agent-action (write) tool only if you include its toolset in the URL.
+ To enable every available toolset, use `https://mcp.datadoghq.com/v1/mcp?toolsets=all`.
+ To enable specific toolsets, use a URL such as `https://mcp.datadoghq.com/v1/mcp?toolsets=core,cases,dashboards`.

For more information about the available toolsets and the tools each one contains, see [Datadog MCP server](https://docs.datadoghq.com/bits_ai/mcp_server/) on the Datadog website.

#### Authorizing with OAuth
<a name="authorizing-with-oauth"></a>

With OAuth, you finish the registration in Datadog. After you choose **Add**, the Datadog consent page opens in the same browser tab. For more information about OAuth in Datadog, see [OAuth 2.0 (recommended)](https://docs.datadoghq.com/mcp_server/setup/#oauth-20-recommended) on the Datadog website.

To authorize AWS DevOps Agent in Datadog:

1. On the Datadog consent page, sign in with the Datadog account that you want to connect.

1. On the Datadog consent page, choose **Authorize**.

After you approve access, the registration appears on the **Capability Providers** page.

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
| data | Datadog context variables | Optional. The template fills data with monitor context, such as the query, scope, tags, and a link back to the Datadog event. The webhook accepts data, but doesn't include its contents in the investigation context. Only title, description, priority, and the incident reference reach the agent. Put anything the investigation needs in $TEXT\_ONLY\_MSG or in the monitor message. | 

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

## Credential updates
<a name="credential-updates"></a>

Use this procedure to replace the credentials of a Datadog registration without deregistering it. Your Agent Space associations stay in place. You update a registration after you rotate a Datadog key or token, or before a token expires. An OAuth refresh token lasts 90 days, and you can't extend it. After it expires, AWS DevOps Agent can't use the Datadog tools until you re-authorize.

What the update does depends on the authentication method of the registration:
+ **OAuth** – Restarts the Datadog consent flow. After you approve access, Datadog issues a new refresh token that lasts 90 days.
+ **API key and application key** – Replaces the API key and the application key. You enter both keys, even if only one of them has changed.
+ **Access token** – Replaces the personal access token or service access token with the token that you enter.

To update the credentials of a Datadog registration:

1. Open the [Capability Providers page](https://console.aws.amazon.com/devops-agent/home#/services) in the AWS DevOps Agent console.

1. On the **Capability Providers** page, select the Datadog registration that you want to update.

1. Choose **Actions**.

1. Choose **Update**.

1. On the **Datadog MCP Server Details** page, do one of the following:
   + For an API key and application key, enter a new **API key** and a new **Application key**.
   + For an access token, enter a new **Access token**.
   + For OAuth, leave the fields as they are.

1. Choose **Next**.

1. On the **Review and update** page, choose **Update**.

With keys or a token, you see a confirmation after Datadog accepts the new values. With OAuth, you then choose **Authorize** again on the Datadog consent page.

You can change the **Server Name** of a registration. To change its endpoint URL or authentication method, you deregister Datadog and then register it again. For instructions on deregistering Datadog, see [Removal](#removal).

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