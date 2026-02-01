# Create an API destination in Amazon EventBridge

Creating an API destination enables you to specify an HTTP endpoint as the target of a rule.

Each API destination requires a connection. A _connection_
specifies the authorization type and credentials to use to authorize with the API
destination endpoint. You can choose an existing connection, or create a connection at
the same time that you create the API destination. For more information, see [Connections for API targets in Amazon EventBridge](eb-target-connection.md "eb-target-connection.md")

###### To create an API destination using the EventBridge console

1. Log in to AWS using an account that has permissions to manage EventBridge and open
   the [EventBridge
   console](https://console.aws.amazon.com/events "https://console.aws.amazon.com/events").
2. In the left navigation pane, choose **API
   destinations**.
3. Scroll down to the **API destinations** table, and then
   choose **Create API destination**.
4. On the **Create API destination** page, enter a
   **Name** and Description for the API destination.

The name must be unique to your account in the current Region. You can use up
to 64 uppercase or lowercase letters, numbers, dot (.), dash (-), or underscore
(\_) characters.

###### Important

When creating a new API destination for your connection, ensure that the connection reaches the AUTHORIZED state before creating the API destination. 5. Enter an **API destination endpoint** for the API
destination.

The **API destination endpoint** is an HTTP invocation
endpoint target for events. The authorization information you include in the
connection used for this API destination is used to authorize against this
endpoint. The URL must use HTTPS. 6. Enter the **HTTP method** to use to connect to the
**API destination endpoint**. 7. (Optional) For **Invocation rate limit per second** field,
enter the maximum number of invocations per second to send to the API
destination endpoint.

The rate limit you set may affect how EventBridge delivers events. For more
information, see [How invocation rate affects event
delivery](eb-api-destinations.md#eb-api-destination-event-delivery "eb-api-destinations.md#eb-api-destination-event-delivery"). 8. For **Connection**, do one of the following:

    * Choose **Use an existing connection**, and then
     select the connection to use for this API destination.
    * Choose **Create a new connection**, and then enter
     the details for the connection to create.


    For detailed instructions, see [Creating
     connections](eb-target-connection-create.md "eb-target-connection-create.md").

9. Choose **Create**.
