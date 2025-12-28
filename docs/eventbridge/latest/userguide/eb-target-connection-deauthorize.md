# De-authorizing connections in EventBridge

You can de-authorize a connection. De-authorizing a connection removes all authorization parameters. Removing
authorization parameters removes the secret from the connection, so you can reuse it
without having to create a new connection.

###### Note

You must update any API destinations or Step Functions workflow tasks that use the de-authorized connection to use a
different connection to successfully send requests to the HTTPS endpoint.

In addition to manual de-authorization, EventBridge de-authorizes a connection if the following
occurs:

- EventBridge cannot retrieve the secret because it has been deleted.
- For connections using OAuth authentication, EventBridge cannot refresh the necessary OAuth token.
- For connections using Basic or API Key authentication, EventBridge receives a `401 (UnAuthorize)` or `407 (Proxy_Authentication_required)` error code.

In this case, update the connection with appropriate credentials to resolve the error.

- If you have specified a customer managed key for EventBridge to use for secret encryption, and EventBridge receives a KMS key error when encrypting or decrypting the connection's secret. For more information, see [Customer managed key
  errors](encryption-connections.md#encryption-connections-deauth "encryption-connections.md#encryption-connections-deauth").

###### Note

EventBridge emits events when the state of a connection changes. You can use these events to track changes in a connection.

For more information, see [Connection
events](event-reference.md#event-reference-connections "event-reference.md#event-reference-connections").

###### To de-authorize a connection using the EventBridge console

1. Log in to AWS using an account that has permissions to manage EventBridge and open the
   [EventBridge console](https://console.aws.amazon.com/events "https://console.aws.amazon.com/events").
2. In the left navigation pane, under **Integration**, choose **Connections**.
3. In the **Connections** table, choose the connection.
4. On the **Connection details** page, choose
   **De-authorize**.
5. In the **Deauthorize connection?** dialog box, enter the name
   of the connection, and then choose **De-authorize**.

The status of the connection changes to **De-authorizing** until the
process is complete. Then the status changes to **De-authorized**. Now
you can edit the connection to add new authorization parameters.

###### To de-authorize a connection using the AWS CLI

- Use the `deauthorize-connection` command.
