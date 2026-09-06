

# Secrets
<a name="acxd-secrets"></a>

Secrets let you securely store reusable values that may be needed when configuring Data requests in agentic CX designer.

Use Secrets for values that should not be hardcoded directly into URLs, headers, or request payloads, such as API keys, tokens, passwords, authorization headers, or other sensitive configuration values.

Secrets can also help teams manage commonly reused values more efficiently because the value can be stored once and referenced where needed.

To access Secrets, select **Resources** from your workspace menu, then choose **Secrets**.

A Secret is a workspace resource that stores a value for later use.

Secrets are commonly used when configuring Data requests that call external systems or MCP servers. Instead of typing a sensitive value directly into a Data request, you can reference the Secret as a placeholder.

Use Secrets for values such as:
+ API keys
+ Bearer tokens
+ Authorization headers
+ Passwords
+ Webhook secrets
+ Reusable endpoint values
+ Environment-specific configuration values

Secrets help reduce exposure of sensitive information and make it easier to update values in one place when credentials or shared configuration values change.

## Creating a Secret
<a name="acxd-secrets-create"></a>

**To create a Secret**

1. Open **Resources** from the workspace menu.

1. Select **Secrets**.

1. Select **Create Secret**.

1. Enter a clear name.

1. Enter the Secret value.

1. Add an optional description.

1. Keep **Sensitive** enabled if the value should be hidden and redacted.

1. Select **Save**.

Use a clear name that helps teammates understand what the Secret is used for.

## Sensitive setting
<a name="acxd-secrets-sensitive"></a>

When the **Sensitive** setting is enabled, the Secret value is hidden and redacted where supported.

Keep **Sensitive** enabled for values such as:
+ API keys
+ Tokens
+ Passwords
+ Authorization headers
+ Customer identifiers
+ Credentials
+ Any value your organization considers private or restricted

Only disable **Sensitive** for values that are safe for teammates to view and that do not need to be redacted.

## Referencing Secrets
<a name="acxd-secrets-reference"></a>

After a Secret is created, you can reference it when configuring a Data request.

Secrets may be used in places such as:
+ Endpoint URLs
+ Headers
+ Authorization values
+ Request payload fields
+ Dynamic configuration values

To reference a Secret, type an open curly brace { in a supported field, then select the Secret from the available placeholder options.

## Using Secrets in an External implementation
<a name="acxd-secrets-external"></a>

Use Secrets in an External Data request implementation when calling an API or webhook that requires secure values.

**To use a Secret in an External implementation**

1. Open **Resources**.

1. Select **Data requests**.

1. Create a new Data request or open an existing one.

1. Go to the **Implementation** tab.

1. Select **External**.

1. Add the endpoint URL.

1. Add any required headers.

1. In a supported URL, header, or payload field, type {.

1. Select the Secret you want to reference.

1. Save the Data request.

For example, if an API requires an authorization header, store the token as a Secret and reference it in the header value instead of entering the token directly.

## Using Secrets in an MCP implementation
<a name="acxd-secrets-mcp"></a>

Use Secrets in an MCP Data request implementation when the MCP server requires authentication or other protected configuration values.

**To use a Secret with an MCP implementation**

1. Open **Resources**.

1. Select **Data requests**.

1. Create a new Data request or open an existing one.

1. Go to the **Implementation** tab.

1. Select **MCP**.

1. Enter the MCP server endpoint.

1. Add required headers, such as Authorization.

1. In the header value field, type {.

1. Select the Secret that stores the required token or credential.

1. Save the Data request.

1. Sync the MCP server to retrieve available tools.

Secrets are especially useful for MCP implementations because MCP servers often require authorization values that should not be typed directly into the Data request configuration.

## Using Secrets in a Data request node
<a name="acxd-secrets-in-node"></a>

You can also reference Secrets when configuring a Data request node in a flow, if the selected Data request includes fields that can accept dynamic values.

**To use a Secret in a Data request node**

1. Select a flow.

1. Add or select a Data request node.

1. Choose the Data request you want to call.

1. Locate the payload field where the Secret should be used.

1. Type {.

1. Select the Secret from the available placeholder options.

1. Save the node and test the flow.

Use this when a specific Data request call needs a secure or reusable value at runtime.

## Testing
<a name="acxd-secrets-testing"></a>

After adding or updating a Secret, test the Data request that uses it.

**To test**

1. Open the Data request.

1. Select the **Test** option.

1. Run the test.

1. Confirm that the request succeeds.

1. Review whether the expected response is returned.

If the test fails, check:
+ The Secret value
+ Header name and format
+ Endpoint URL
+ Request method
+ Request payload
+ Whether the correct environment is being tested
+ Whether the external service expects a prefix such as Bearer