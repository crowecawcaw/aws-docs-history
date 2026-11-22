

# Checkmarx integration

Bring Checkmarx One application security data into AWS Quick using natural language. With the Checkmarx connector, you can trigger scans, retrieve findings, and query your security posture without leaving AWS Quick. You can also use Checkmarx tools inside AWS Quick Flows to run reusable security workflows on demand or on a schedule.

This connector supports Predefined OAuth Client authentication. The connector authenticates through a Checkmarx OAuth login workflow that uses a fixed, pre-registered OAuth client (client ID `cx-mcp-client`). For more information about the authentication methods that AWS Quick supports, see [Authentication methods](quick-action-auth.md).

## Prerequisites
<a name="checkmarx-integration-prerequisites"></a>

Before you set up the connector, verify that you have the following resources and access.
+ An active Checkmarx One account with access to the tenant that you want to query.
+ Checkmarx license packages that cover the tools you plan to use. Only licensed tools and scanners are available through the connector. Remediation tools require a Checkmarx One Assist, AI Protection, or Checkmarx Developer Assist license.
+ Checkmarx One IAM permissions for the operations you want to run. Tool access follows your user permissions.
+ The ability to register the AWS Quick callback URL as a redirect URI for the OAuth client. See [Configuring Checkmarx](#checkmarx-source-setup).
+ A subscription that meets the requirements described in [Set up integrations in the console](integration-console-setup-process.md).

## Configuring Checkmarx
<a name="checkmarx-source-setup"></a>

Prepare the OAuth configuration on the Checkmarx side before you create the connector in AWS Quick.

1. Identify the AWS Region where you run AWS Quick, for example `us-east-1`.

1. Register the AWS Quick callback URL as a redirect URI for the predefined OAuth client (`cx-mcp-client`): `https://{{region}}.quicksight.aws.amazon.com/sn/oauthcallback`. Replace {{region}} with your AWS Region. If you cannot register the redirect URI yourself, contact Checkmarx Support.

1. Confirm the Checkmarx Model Context Protocol (MCP) Server URL for your tenant and keep it available for the next procedure.

For more information about the Checkmarx MCP Server, see [Checkmarx MCP Server](https://docs.checkmarx.com/en/34965-659697-1-checkmarx-mcp-server.html) on the Checkmarx website.

## Setting up the integration in AWS Quick
<a name="checkmarx-integration-setup"></a>

After you configure Checkmarx, create the connector in AWS Quick.

1. In the AWS Quick console, choose **Connectors**, and then choose **Model Context Protocol** to start a new custom MCP connector.

1. For **Name**, enter a descriptive name. For **MCP Server URL**, enter the Checkmarx MCP Server URL for your tenant.

1. For **Connection type**, choose **Public network**. For **OAuth Configuration**, choose Predefined OAuth Client and enter the client ID (`cx-mcp-client`), authorization URL, token URL, scopes, and redirect URL.

1. Choose **Next**. If an authorization window opens, sign in to Checkmarx and choose **Allow**.

1. On the **Publish** page, specify who can access the connector and choose **Publish**.

The tools that appear depend on your Checkmarx license packages and your IAM permissions.

## Using available actions
<a name="checkmarx-integration-actions"></a>

After you set up the connector, you can use the following categories of tools from Checkmarx.


**Checkmarx available actions**  

| Category | Description | 
| --- | --- | 
| Remediation | Tools that help resolve findings. Requires a Checkmarx One Assist, AI Protection, or Checkmarx Developer Assist license. | 
| Scan workflow | Start and manage scans. For example, triggerScan starts a scan asynchronously. | 
| Project and application management | Look up and resolve projects and applications. For example, resolveProject resolves a project and getApplicationDetails returns details for an application. | 
| Scan history | Retrieve prior scan results for a project. | 
| Triage | Review and act on findings. For example, getTenantVulnerabilitiesSummary returns a vulnerability summary across the tenant. | 

To see the current set of tools available to you, open the connector's **Available actions** view in the AWS Quick console.

## Troubleshooting
<a name="checkmarx-integration-troubleshooting"></a>

To edit, share, or delete your connector, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations).

The following issues can occur when you set up or use the connector.

### Connector creation fails during authorization
<a name="checkmarx-troubleshoot-auth-fail"></a>

The AWS Quick callback URI is not registered for the OAuth client. Contact Checkmarx Support to configure the redirect URI for your tenant, and then create the connector again.

### A tool does not appear or returns a permission error
<a name="checkmarx-troubleshoot-permission"></a>

The tool is not covered by your license packages, or your Checkmarx One IAM permissions do not allow the operation. Confirm your license tier and permissions in Checkmarx One.

### Publishing fails because of a tool schema error
<a name="checkmarx-troubleshoot-creation-failed"></a>

Publishing returns a `Creation failed` message when a tool's input schema isn't compliant with JSON Schema Draft 7. Contact Checkmarx Support.

### A tool call fails with HTTP 424 (timeout)
<a name="checkmarx-troubleshoot-http424"></a>

The operation exceeded the AWS Quick timeout. Limit the scope of the request, or use `triggerScan` to start scans asynchronously.