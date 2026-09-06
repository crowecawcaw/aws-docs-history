# New Relic integration

With the New Relic connector, you can access the New Relic observability
platform directly in Amazon Quick through natural language.
You can investigate incidents, analyze application performance, query telemetry data,
and generate reports without leaving Amazon Quick.

New Relic is available as a built-in connector in Amazon Quick. To set up this
integration, complete the following two steps. First, prepare your New Relic account
with the required access. Then, create the integration in Amazon Quick and authenticate
with your New Relic credentials. This integration uses OAuth 2.0 user authentication.
For information about the authentication methods that Amazon Quick supports, see
[Authentication methods](quick-action-auth.md "quick-action-auth.md").

## Prerequisites

Before you set up the integration, make sure that you have the following
resources and access.

- An active New Relic account with the required permissions and access.
  For information about account requirements and access configuration, see
  [New Relic AI MCP](https://docs.newrelic.com/docs/agentic-ai/mcp/overview/ "https://docs.newrelic.com/docs/agentic-ai/mcp/overview/")
  in the New Relic documentation.
- For information about subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md "integration-console-setup-process.md").

## Verify your New Relic account

Before you configure Amazon Quick, verify that your New Relic account meets the
following requirements.

- Your New Relic account is active and you can sign in to
  [login.newrelic.com](https://login.newrelic.com "https://login.newrelic.com").
- The entities and data that you want to query are accessible to your
  account.

## Set up the integration in Amazon Quick

After you verify your New Relic account access, create the integration in
Amazon Quick.

1. In the Amazon Quick console, choose
   **Connectors**.
2. Choose the **Create for your team** tab.
3. Find and choose **New Relic**.
4. In the **Create integration** dialog, enter the
   following fields:

   - **Name** – A descriptive name for your
     New Relic integration.
   - **Description** (Optional) – Notes about how
     you plan to use this connection.
   - **Connection type** – Choose
     **Public network**.

5. Choose **Create and continue**.
6. On the integration detail page, choose **Sign in** and
   authenticate with your New Relic account credentials. This step authorizes
   Amazon Quick to access New Relic on behalf of the authenticated
   user.
7. (Optional) Choose the users to share the integration with.
8. Choose **Done**.

The integration appears in the **Existing actions** panel with
a status of **Available**.

## Available actions

After you set up the integration, you can use the following actions.

New Relic available actions| Category | Action | Description |
| --- | --- | --- |
| Incident analysis | Generate Alert Insights Report | Generates an alert intelligence analysis report for a specific<br>issue. Provides insights into root cause, impact, and recommended<br>actions. |
| Incident analysis | Generate User Impact Report | Analyzes affected entities and their relationships to quantify<br>end-user impact through metrics like affected user count, degraded<br>services, and severity indicators. |
| Incident analysis | Search Incident | Retrieves alert incident events with flexible filtering by issue<br>ID, entity GUID, or policy and condition pair. |
| Incident analysis | List Recent Issues | Lists all recent issues (last 24 hours) for a specified<br>account. |
| Performance analysis | Analyze Transactions | Identifies slow and error-prone transactions, their traces,<br>common transaction paths, and error distributions. |
| Performance analysis | Analyze Golden Metrics | Analyzes key health indicators (throughput, response time, error<br>rate, and saturation) across application and infrastructure<br>entities. |
| Performance analysis | Analyze Deployment Impact | Compares metrics before and after a deployment to identify<br>regressions or improvements. |
| Performance analysis | Analyze Kafka Metrics | Analyzes Kafka metrics including consumer lag, producer<br>throughput, message latency, partition balance, and resource<br>utilization. |
| Performance analysis | Analyze Threads | Analyzes thread metric data including thread state, CPU usage,<br>and memory consumption. Provides language-specific insights for<br>applications. |
| Performance analysis | List Garbage Collection Metrics | Retrieves garbage collection and memory metrics for a given<br>entity. Use this action to identify whether GC issues are affecting<br>application performance. |
| Log analysis | Analyze Entity Logs | Analyzes application logs to identify error patterns, anomalous<br>behavior, and recurring issues within a specified time<br>window. |
| Log analysis | List Recent Logs | Retrieves recent logs for a specified account and entity<br>GUID. |
| Error analysis | List Entity Error Groups | Retrieves error groups from the Errors Inbox within a time<br>window. Groups errors by message and prioritizes by user<br>impact. |
| Queries | Natural Language to NRQL Query | Converts a natural language request into a New Relic Query<br>Language (NRQL) query, runs it against New Relic, and returns the<br>results. |
| Queries | Execute NRQL Query | Runs an NRQL query directly against New Relic telemetry<br>data. |
| Entities | Get Entity | Retrieves entities by GUID or searches by name pattern. |
| Entities | List Related Entities | Retrieves entities that are related to a given entity<br>GUID. |
| Entities | Search Entity with Tag | Searches for entities by using tag key and value<br>pairs. |
| Entities | List Entity Types | Lists the complete catalog of New Relic entity types with their<br>domain, type, and metric definitions. |
| Alerts | List Alert Policies | Lists alert policies for a specified account, with optional<br>filtering by policy name. |
| Alerts | List Alert Conditions | Retrieves alert condition details for a specific alert<br>policy. |
| Dashboards | List Dashboards | Lists all dashboards for a New Relic account. |
| Dashboards | Get Dashboard | Retrieves detailed information for a specific dashboard by<br>entity GUID. |
| Change tracking | List Change Events | Retrieves a history of change events such as deployments,<br>configuration changes, and other tracked activities for an<br>entity. |
| Monitoring | List Synthetic Monitors | Lists synthetic monitors that check service availability and<br>performance from multiple geographic locations. |
| Account | List Available New Relic Accounts | Lists all New Relic account IDs that are accessible to the<br>authenticated user. |
| Utilities | Convert Time Period to Epoch Ms | Converts a natural language time period to epoch milliseconds<br>for use with time-based queries. |

###### Note

The actions that you can use depend on the permissions that are configured
in your New Relic account and the entities that are accessible to the
authenticated user.

## Manage and troubleshoot

To edit, share, or delete your integration, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations "integration-workflows.md#managing-existing-integrations").

### Authentication issues

- **Sign-in fails** – Verify that your
  New Relic account is active and that you can sign in to
  [login.newrelic.com](https://login.newrelic.com "https://login.newrelic.com") directly. If your organization uses
  single sign-on (SSO), confirm that your identity provider is
  configured correctly.
- **MCP server access denied** – Verify
  that your user has the required permissions to access the New Relic
  MCP server. For information about access requirements, see
  [New Relic AI MCP](https://docs.newrelic.com/docs/agentic-ai/mcp/overview/ "https://docs.newrelic.com/docs/agentic-ai/mcp/overview/")
  in the New Relic documentation.
