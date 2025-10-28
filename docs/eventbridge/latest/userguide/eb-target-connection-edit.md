# Updating connections in EventBridge

You can update existing connections.

## Updating authentication of connections

When you update certain authentication parameters, EventBridge re-authorizes and verifies
network connectivity of the connection accordingly.

Updating the connection with authorization parameters of a different authorization type, without updating the authorization type itself, has no effect.

**When EventBridge re-authenticates connections to public APIs**

For connections to public APIs, EventBridge re-authorizes the connection if you:

- Update the connection to invoke a private API instead.
- Update the connection authorization method _and_ authorization
  parameters.

**When EventBridge re-authenticates connections to private APIs**

For connections to private APIs, if you do any of the following:

- Update the connection to invoke a different private API, or a public API.
- Update the connection authorization method.
- Update the connection authorization parameters for the specified authorization method.

EventBridge does the following:

- Re-authorizes the connection.
- Verifies the network connectivity of the connection.

If you have updated the connection to use a different private API, or a
public API, EventBridge also removes or updates
existing network connectivity artifacts as appropriate.

###### To update a connection using the EventBridge console

1. Log in to AWS using an account that has permissions to manage EventBridge and open the
   [EventBridge console](https://console.aws.amazon.com/events "https://console.aws.amazon.com/events").
2. In the left navigation pane, under **Integration**, choose **Connections**.
3. In the **Connections** table, choose the connection to
   edit.
4. On the **Connection details** page, choose
   **Edit**.
5. Update the values for the connection, and then choose
   **Update**.

For information on updating the KMS key for EventBridge to use when encrypting a
connection, see [Updating
AWS KMS keys](encryption-connections-configure.md#encryption-connections-update "encryption-connections-configure.md#encryption-connections-update").

###### To update a connection using the AWS CLI

- Use the `update-connection` command.

To update a connection's invocation or authorization endpoint from a private API to a public API,
you must specify an empty string (`""`) for the `ResourceConfigurationArn` parameter.
Specifying `null` for this parameter has no effect.

The following example updates the connection to use a public API, by setting
the `ResourceConfigurationArn` that represents a private API resource
configuration to an empty string.

```
aws events update-connection \
--name myConnection \
--authorization-type BASIC \
--auth-parameters '{"BasicAuthParameters": {"Username": "username", "Password": "***"}}' \
--region us-east-1 \
--invocation-connectivity-parameters ResourceParameters={ResourceConfigurationArn=\"\"}
```
