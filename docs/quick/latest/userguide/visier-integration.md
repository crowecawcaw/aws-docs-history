# Visier Agent integration

With the Visier Agent connector, you can access Visier's people
analytics platform directly in Amazon Quick through natural language. You can
query live workforce data, analyze headcount trends, assess retention health,
generate workforce briefings, and more without leaving Amazon Quick.

Visier Agent uses Custom OAuth app authentication. For more information about
the authentication methods that Amazon Quick supports, see [Authentication methods](quick-action-auth.md "quick-action-auth.md").

## Before you begin

Make sure that you have the following before you set up the
integration.

- An active Visier account with API access and Visier Agent enabled.
  For information about enabling Visier Agent and configuring
  authentication, see [Visier MCP Server documentation](https://docs.visier.com/developer/agents/mcp/mcp-server-set-up.htm "https://docs.visier.com/developer/agents/mcp/mcp-server-set-up.htm").
- Appropriate data access scopes configured in your Visier account
  for the workforce data you want to query.
- OAuth credentials (Client ID and Client Secret) from your Visier
  administrator.
- For Amazon Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md "integration-console-setup-process.md").

## Configuring Visier

Before you configure Amazon Quick, complete the following steps in your
Visier admin console.

1. Sign in to your Visier admin console and confirm that your account
   is active.
2. Enable the Visier Agent capability under **Settings**,
   **API & Integrations**.
3. Register an OAuth client for Amazon Quick and add the Amazon Quick
   callback URL to the list of redirect URIs:
   `https://`{region}`.quicksight.aws.amazon.com/sn/oauthcallback`

Replace `{region}` with your AWS
Region (for example, `us-east-1`). 4. Record the **Client ID** and
**Client Secret**. You need them when
you configure Amazon Quick. 5. Confirm that the workforce data and analytics you want to query are
accessible to your account.

## Setting up the connector in Amazon Quick

1. In the Amazon Quick console, choose
   **Connectors**.
2. Choose the **Create for your team** tab.
3. Find and choose **Visier Agent**.
4. Enter a **Name** for your connector. Optionally,
   choose **+ Add Description** to add a description.
5. For **Connection type**, choose **Public
   network**.
6. For **OAuth Configuration**, choose **Custom
   OAuth app** and configure the following fields:

   - **Base URL** – The Visier Agent MCP base
     URL, pre-filled by Amazon Quick.
   - **Client ID** – The OAuth client ID from
     your Visier admin console.
   - **Public OAuth client** (Optional) –
     Select this option if your Visier OAuth client is configured
     as a public client (no client secret).
   - **Client secret** – The OAuth client
     secret from your Visier admin console.
   - **Token URL** – The OAuth token endpoint,
     pre-filled by Amazon Quick.
   - **Authorization URL** – The OAuth
     authorization endpoint, pre-filled by Amazon Quick.
   - **Redirect URL** – Pre-filled with the
     Amazon Quick callback URL.

7. Choose **Next**.
8. In the Visier sign-in popup that appears, enter your Visier
   credentials and choose **Sign in** to authorize
   Amazon Quick to access Visier on your behalf.
9. On the **Review** page, Amazon Quick discovers
   the tools that Visier Agent exposes and displays them in a table.
   Review the list of available actions and choose
   **Next**.
10. On the **Publish** page, choose who can access the
    connector. You can enable access for everyone in your organization or
    search for specific teams or groups.
11. Choose **Publish**.

## Available actions

After you set up the connector, you can use the following actions. Visier
Agent exposes its people analytics capabilities as callable tools.

Visier Agent available actions| Action | Description |
| --- | --- |
| `ask_vee_question` | Asks Visier's Vee AI a natural language workforce question,<br>such as headcount, turnover, or requisitions. |
| `aggregate_metric_values` | Computes aggregate values for a metric, optionally grouped by<br>a dimension and filtered by specific members. |
| `sample_vee_questions` | Returns a list of sample questions that you can ask Vee to<br>get started. |
| `search_analytic_objects` | Finds analytic objects (for example, Employee or Applicant)<br>matching a search string. |
| `search_analytic_object_properties` | Returns all available properties for a given analytic<br>object. |
| `list_analytic_object_property_values` | Lists property values for specific analytic object members,<br>such as employee tenure or pay. |
| `search_metrics` | Finds metrics matching a search string. |
| `search_dimensions_for_metric` | Finds dimensions available for a given metric, usable for<br>grouping or filtering. |
| `search_dimensions_for_analytic_object` | Finds dimensions available for a given analytic<br>object. |
| `search_filter_dimension_members` | Returns filterable members for a given dimension. |
| `get_object_reference_graph` | Returns the reference graph showing how a given analytic<br>object connects to others. |

## Managing and troubleshooting

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations "integration-workflows.md#managing-existing-integrations").

### Authentication issues

- **MCP server connection fails** –
  Verify that you enabled the Visier Agent capability in your
  Visier admin console under **Settings**,
  **API & Integrations**. Confirm that you
  entered the Base URL, Token URL, and Authorization URL correctly
  in Amazon Quick.
- **Invalid client credentials** –
  Verify that the Client ID and Client secret match the values from
  your Visier admin console. Confirm that the redirect URI in your
  Visier OAuth client matches the Amazon Quick callback URL.
- **Data access errors** – Verify
  that the data access scopes configured in your Visier account
  include the workforce data you are trying to query. Contact your
  Visier administrator to review your account permissions.
- **No tools discovered** – If
  Amazon Quick does not discover any tools after you create the
  connector, confirm that Visier Agent is active and that your
  authentication credentials have not expired.
