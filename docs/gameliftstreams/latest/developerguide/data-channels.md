# Data channel communication between an application and web client

Data channels allow you to securely communicate arbitrary messages between your Amazon GameLift Streams application and the web client (the JavaScript code running in the end-user's web browser). This allows end-users to interact with the application that Amazon GameLift Streams is streaming, via the web browser where they're viewing the stream.

Here are some example use cases of data channels in Amazon GameLift Streams:

- Users can open URLs in the application in their local browser.
- Users can pass content in the clipboard back and forth to the application.
- Users can upload content from their local machine to the application.
- Developers can implement UI in the browser that sends commands to the application.
- Users can pass schemas to control display of visualization layers.

## Features

###### Message size limits

Amazon GameLift Streams Web SDK imposes a maximum size limit of 64 KB (65536 bytes) per message.
This ensures that the message size limits are compatible with most browsers, and
that the communication has low impact on the total bandwidth of the stream.

###### Metrics

Metrics on your data channel usage are sent to your AWS account when a stream
session ends. For more information, refer to [Data channels](monitoring-cloudwatch.md#monitoring-data-channels "monitoring-cloudwatch.md#monitoring-data-channels") in the _Monitoring Amazon GameLift Streams_ section.

## Using data channels

The Amazon GameLift Streams Web SDK provides the `sendApplicationMessage` function that
sends a message as a byte array to the application. The message is processed by a
callback function, `clientConnection.applicationMessage` that you define.

If the client sends messages before the application connects to the data channel port,
the messages are queued. Then, when the application connects, it receives the messages.
However, if the application sends messages before the client connects to the data
channel port, the messages are lost. The application must check the connection state of
the clients before sending a message.

## On the client-side

Write the following code in your web client application.

1. Define the callback function to receive incoming messages from the application.

```
function streamApplicationMessageCallback(message) {
    console.log('Received ' + message.length + ' bytes of message from
    Application');
}
```

2. Set `clientConnection.applicationMessage` to your callback function.

```
clientConnection: {
    connectionState: streamConnectionStateCallback,
    channelError: streamChannelErrorCallback,
    serverDisconnect: streamServerDisconnectCallback,
    applicationMessage: streamApplicationMessageCallback,
}
```

3. Call the `GameLiftStreams.sendApplicationMessage` function to send messages to your application. You can call this any time, as long as the stream session is active and the input is attached.

As an example, refer to the Amazon GameLift Streams Web SDK sample client, which demonstrates how
to set up a simple data channel on the client-side.

## On the application-side

Write the following logic in your application.

### Step 1. Connect to the data channel port

When your application starts, connect to port `40712` on `localhost`. Your application should maintain this connection for the entire
duration of execution. If the application closes the connection, it cannot be
reopened.

### Step 2. Listen for events

An event starts with a fixed-size header, followed by variable-length associated
data. When your application receives an event, parse the event to retrieve the
information.

**Event format**

- **Header**: A 4-byte header in the form
  `abcc`
  - `a` : Client id byte. This identifies a specific client
    connection, in the case of multiple connections (due to
    disconnection and reconnection).
  - `b` : Event type byte. `0` - the client
    connected, `1` - the client disconnected, `2`
  * a message is sent from the client. Other event types may be
    received with future Amazon GameLift Streams service updates, and should be ignored.
  - `cc` : Length of the associated event data. This is
    represented as 2 bytes with big-endian ordering (first byte is the
    most significant). If the event type is 2, the event data represents
    the message contents from the client.

- **Data**: The remaining bytes contain the
  event data, such as a client message. The length of the data is
  indicated by `cc` in the header.

###### To listen for events

1. Read the four header bytes to retrieve the client id, event type,
   and length of the event data.
2. Read the variable-length event data, regardless of the client id and
   event type, according to the length described in the header. It's important to read the data unconditionally so that event data is never left in the buffer, where it could be confused with the next event header. Do not make assumptions about the length of the data based on event types.
3. Take appropriate action based on the event type, if recognized by your
   application. This action might include logging an incoming connection or
   disconnection, or parsing the client message and triggering application logic.

### Step 3. Transmit messages to the client

The application should transmit messages with the same four-byte header format used by incoming events.

###### To transmit a message to the client

1. Write the header with the following properties:
   1. `a` : Client id byte. If your message is in
      response to a client message, it should reuse the same client id as the
      incoming client message, to avoid race conditions such as delivering a
      response from an old client connection to a newly reconnected client. If
      your application is sending an unsolicited message to the client, it
      should set the client id to match the most recent "client connection"
      event (event type 0).
   2. `b` : The event type of outgoing messages must
      always be 2. The client ignores messages with other event types.
   3. `cc` : Length of the message, in bytes.

2. Write the message bytes.

The message delivers to the specified client, unless the client disconnects. When
a disconnected client reconnects, a new client ID is assigned via a client connected
event. Any undelivered messages for the old client ID are discarded.

###### Example

The following pseudo-code demonstrates the logic to communicate messages in the application-side. For a complete example using Winsock, refer to [Complete Winsock Client Code](https://learn.microsoft.com/en-us/windows/win32/winsock/complete-client-code "https://learn.microsoft.com/en-us/windows/win32/winsock/complete-client-code") in the Windows Sockets 2 documentation.

```

connection = connect_to_tcp_socket("localhost:40712")
loop:
    while has_pending_bytes(connection):
        client_id = read_unsigned_byte(connection)
        event_type = read_unsigned_byte(connection)
        event_length = 256 * read_unsigned_byte(connection)
        event_length = event_length + read_unsigned_byte(connection)
        event_data = read_raw_bytes(connection, event_length)
        if message_type == 0:
            app_process_client_connected(client_id)
        else if message_type == 1:
            app_process_client_disconnected(client_id)
        else if message_type == 2:
            app_process_client_message(client_id, event_data)
        else:
            log("ignoring unrecognized event type")
    while app_has_outgoing_messages():
        target_client_id, message_bytes = app_next_outgoing_message()
        message_length = length(message_bytes)
        write_unsigned_byte(connection, target_client_id)
        write_unsigned_byte(connection, 2)
        write_unsigned_byte(connection, message_length / 256)
        write_unsigned_byte(connection, message_length mod 256)
        write_raw_bytes(connection, message_bytes)

```
