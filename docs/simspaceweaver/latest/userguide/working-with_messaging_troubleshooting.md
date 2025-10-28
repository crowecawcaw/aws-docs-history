End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Messaging errors and

troubleshooting

You might experience the following errors when you use the messaging APIs.

## Endpoint resolution errors

These errors can occur before an app sends a message.

### Domain name

check

Sending a message to an invalid endpoint results in the following
error:

```
ManifoldError::InvalidArgument {"No DomainId found for the given domain name" }
```

This can happen when you try to send a message to a custom app and that custom
app hasn't joined the simulation yet. Use the
`DescribeSimulation` API to make sure your
custom app has launched before you send a message to it. This behavior is the
same in SimSpace Weaver Local and the AWS Cloud.

### Position

check

Trying to resolve an endpoint with a valid domain name but an invalid position
results in the following error.

```
ManifoldError::InvalidArgument {"Could not resolve endpoint from domain : DomainId { value: domain-id } and position: Vector2F32 { x: x-position, y: y-position}" }
```

We suggest using the `MessageEndpointResolver` in
the `MessageUtils` library contained in the
SimSpace Weaver app SDK.

## Message

sending errors

The following errors can occur as an app sends a message.

### Message sending

limit per app, per tick, exceeded

The current limit for the number of messages that can be sent per app per
simulation tick is 128. Subsequent calls on the same tick will fail with the
following error:

```
ManifoldError::CapacityExceeded {"At Max Outgoing Message capacity: {}", 128}
```

SimSpace Weaver tries to send unsent messages on the next tick. Lower the send
frequency to resolve this problem. Combine message payloads that are smaller
than the 256 byte limit to lower the number of outbound messages.

This behavior is the same in SimSpace Weaver Local and in the AWS Cloud.

### Message

payload size limit exceeded

The current limit for message payload size is 256 bytes in both
SimSpace Weaver Local and in the AWS Cloud. Sending a message with a payload larger
than 256 bytes results in the following error:

```
ManifoldError::CapacityExceeded {"Message data too large! Max size: {}", 256}
```

SimSpace Weaver checks each message and only rejects those that exceed the limit.
For example, if your app tries to send 10 messages and 1 fails the check, only
that 1 message is rejected. SimSpace Weaver sends the other 9 messages.

This behavior is the same in SimSpace Weaver Local and the AWS Cloud.

### Destination is the same as source

Apps can't send messages to partitions they own. You get the following error
if an app sends a message to a partition it owns.

```
ManifoldError::InvalidArgument { "Destination is the same as source" }
```

This behavior is the same in SimSpace Weaver Local and the AWS Cloud.

### Best effort

messaging

SimSpace Weaver doesn't guarantee message delivery. The service will try to
complete delivery of messages on the subsequent simulation tick, but messages
might get lost or be delayed.
