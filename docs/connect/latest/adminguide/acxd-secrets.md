# Secrets

Secrets let you securely store reusable values that may be needed when
configuring Data requests in agentic CX designer.

Use Secrets for values that should not be hardcoded directly into URLs, headers, or
request payloads, such as API keys, tokens, passwords, authorization headers, or
other sensitive configuration values.

Secrets can also help teams manage commonly reused values more efficiently
because the value can be stored once and referenced where needed.

To access Secrets, select **Resources** from your workspace menu, then choose
**Secrets**.

A Secret is a workspace resource that stores a value for later use.

Secrets are commonly used when configuring Data requests that call external
systems or MCP servers. Instead of typing a sensitive value directly into a Data
request, you can reference the Secret as a placeholder.

Use Secrets for values such as:

- API keys
- Bearer tokens
- Authorization headers
- Passwords
- Webhook secrets
- Reusable endpoint values
- Environment-specific configuration values
  Secrets help reduce exposure of sensitive information and make it easier to update
  values in one place when credentials or shared configuration values change.

## Creating a Secret

###### To create a Secret

1. Open **Resources** from the workspace menu.
2. Select **Secrets**.
3. Select **Create Secret**.
4. Enter a clear name.
5. Enter the Secret value.
6. Add an optional description.
7. Keep **Sensitive** enabled if the value should be hidden and redacted.
8. Select **Save**.

Use a clear name that helps teammates understand what the Secret is used for.

## Sensitive setting

When the **Sensitive** setting is enabled, the Secret value is hidden and redacted
where supported.

Keep **Sensitive** enabled for values such as:

- API keys
- Tokens
- Passwords
- Authorization headers
- Customer identifiers
- Credentials
- Any value your organization considers private or restricted

Only disable **Sensitive** for values that are safe for teammates to view and that do
not need to be redacted.

## Referencing Secrets

After a Secret is created, you can reference it when configuring a Data request.

Secrets may be used in places such as:

- Endpoint URLs
- Headers
- Authorization values
- Request payload fields
- Dynamic configuration values

To reference a Secret, type an open curly brace { in a supported field, then select
the Secret from the available placeholder options.

## Using Secrets in an External implementation

Use Secrets in an External Data request implementation when calling an API or
webhook that requires secure values.

###### To use a Secret in an External implementation

1. Open **Resources**.
2. Select **Data requests**.
3. Create a new Data request or open an existing one.
4. Go to the **Implementation** tab.
5. Select **External**.
6. Add the endpoint URL.
7. Add any required headers.
8. In a supported URL, header, or payload field, type {.
9. Select the Secret you want to reference.
10. Save the Data request.

For example, if an API requires an authorization header, store the token as a Secret
and reference it in the header value instead of entering the token directly.

## Using Secrets in an MCP implementation

Use Secrets in an MCP Data request implementation when the MCP server requires
authentication or other protected configuration values.

###### To use a Secret with an MCP implementation

1. Open **Resources**.
2. Select **Data requests**.
3. Create a new Data request or open an existing one.
4. Go to the **Implementation** tab.
5. Select **MCP**.
6. Enter the MCP server endpoint.
7. Add required headers, such as Authorization.
8. In the header value field, type {.
9. Select the Secret that stores the required token or credential.
10. Save the Data request.
11. Sync the MCP server to retrieve available tools.

Secrets are especially useful for MCP implementations because MCP servers often
require authorization values that should not be typed directly into the Data request
configuration.

## Using Secrets in a Data request node

You can also reference Secrets when configuring a Data request node in a flow, if
the selected Data request includes fields that can accept dynamic values.

###### To use a Secret in a Data request node

1. Select a flow.
2. Add or select a Data request node.
3. Choose the Data request you want to call.
4. Locate the payload field where the Secret should be used.
5. Type {.
6. Select the Secret from the available placeholder options.
7. Save the node and test the flow.

Use this when a specific Data request call needs a secure or reusable value at runtime.

## Testing

After adding or updating a Secret, test the Data request that uses it.

###### To test

1. Open the Data request.
2. Select the **Test** option.
3. Run the test.
4. Confirm that the request succeeds.
5. Review whether the expected response is returned.

If the test fails, check:

- The Secret value
- Header name and format
- Endpoint URL
- Request method
- Request payload
- Whether the correct environment is being tested
- Whether the external service expects a prefix such as Bearer
