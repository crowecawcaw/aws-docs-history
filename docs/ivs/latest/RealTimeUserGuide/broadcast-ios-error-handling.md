# Error Handling in the IVS iOS Broadcast

SDK | Real-Time Streaming

This section is an overview of error conditions, how the IVS real-time streaming iOS
broadcast SDK reports them to the application, and what an application should do when
those errors are encountered.

## Fatal vs. Non-Fatal

Errors

The error object has an "is fatal" boolean. This is a dictionary entry under
`IVSBroadcastErrorIsFatalKey` which contains a boolean.

In general, fatal errors are related to connection to the Stages server (either a
connection cannot be established or is lost and cannot be recovered). The
application should re-create the stage and re-join, possibly with a new token or
when the device’s connectivity recovers.

Non-fatal errors generally are related to the publish/subscribe state and are
handled by the SDK, which retries the publish/subscribe operation.

You can check this property:

```
let nsError = error as NSError
if nsError.userInfo[IVSBroadcastErrorIsFatalKey] as? Bool == true {
  // the error is fatal
}
```

## Join Errors

### Malformed

Token

This happens when the stage token is malformed.

The SDK throws a Swift exception with error code = 1000 and
IVSBroadcastErrorIsFatalKey = YES.

**Action**: Create a valid token and retry
joining.

### Expired

Token

This happens when the stage token is expired.

The SDK throws a Swift exception with error code = 1001 and
IVSBroadcastErrorIsFatalKey = YES.

**Action**: Create a new token and retry
joining.

### Invalid or

Revoked Token

This happens when the stage token is not malformed but is rejected by the
Stages server. This is reported asynchronously through the application-supplied
stage renderer.

The SDK calls `stage(didChange connectionState, withError error)`
with error code = 1026 and IVSBroadcastErrorIsFatalKey = YES.

**Action**: Create a valid token and retry
joining.

### Network

Errors for Initial Join

This happens when the SDK cannot contact the Stages server to establish a
connection. This is reported asynchronously through the application-supplied
stage renderer.

The SDK calls `stage(didChange connectionState, withError error)`
with error code = 1300 and IVSBroadcastErrorIsFatalKey = YES.

**Action**: Wait for the device’s connectivity to
recover and retry joining.

### Network

Errors when Already Joined

If the device’s network connection goes down, the SDK may lose its connection
to Stage servers. This is reported asynchronously through the
application-supplied stage renderer.

The SDK calls `stage(didChange connectionState, withError error)`
with error code = 1300 and IVSBroadcastErrorIsFatalKey value = YES.

**Action**: Wait for the device’s connectivity to
recover and retry joining.

## Publish/Subscribe

Errors

### Initial

There are several errors:

- MultihostSessionOfferCreationFailPublish (1020)
- MultihostSessionOfferCreationFailSubscribe (1021)
- MultihostSessionNoIceCandidates (1022)
- MultihostSessionStageAtCapacity (1024)
- SignallingSessionCannotRead (1201)
- SignallingSessionCannotSend (1202)
- SignallingSessionBadResponse (1203)

These are reported asynchronously through the application-supplied stage
renderer.

The SDK retries the operation for a limited number of times. During retries,
the publish/subscribe state is `ATTEMPTING_PUBLISH` /
`ATTEMPTING_SUBSCRIBE`. If the retry attempts succeed, the state
changes to `PUBLISHED` / `SUBSCRIBED`.

The SDK calls `IVSErrorDelegate:didEmitError` with the relevant
error code and `IVSBroadcastErrorIsFatalKey == NO`.

**Action**: No action is needed, as the SDK
retries automatically. Optionally, the application can refresh the strategy to
force more retries.

### Already

Established, Then Fail

A publish or subscribe can fail after it is established, most likely due to a
network error. The error code for a "peer connection lost due to network error"
is 1400.

This is reported asynchronously through the application-supplied stage
renderer.

The SDK retries the publish/subscribe operation. During retries, the
publish/subscribe state is `ATTEMPTING_PUBLISH` /
`ATTEMPTING_SUBSCRIBE`. If the retry attempts succeed, the state
changes to `PUBLISHED` / `SUBSCRIBED`.

The SDK calls `didEmitError` with error code = 1400 and
IVSBroadcastErrorIsFatalKey = NO.

**Action**: No action is needed, as the SDK
retries automatically. Optionally, the application can refresh the strategy to
force more retries. In the event of total connectivity loss, it’s likely that
the connection to Stages will fail too.
