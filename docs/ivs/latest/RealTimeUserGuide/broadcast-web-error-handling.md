

# Error Handling in the IVS Web Broadcast SDK \| Real-Time Streaming
<a name="broadcast-web-error-handling"></a>

This section is an overview of error conditions, how the Web broadcast SDK reports them to the application, and what an application should do when those errors are encountered. Errors are reported by the SDK to listeners of the `StageEvents.ERROR` event:

```
stage.on(StageEvents.ERROR, (error: StageError) => {
    // log or handle errors here
    console.log(`${error.code}, ${error.category}, ${error.message}`);
});
```

## Stage Errors
<a name="web-error-handling-stage-errors"></a>

A StageError is reported when the SDK encounters a problem it cannot recover from and generally requires app intervention and/or network reconnection to recover.

Each reported `StageError` has a code (or `StageErrorCode`), message (string), and category (`StageErrorCategory`). Each is related to an underlying operation category.

The operation category of the error is determined based on whether it is related to the connection to the stage (`JOIN_ERROR`), sending media to the stage (`PUBLISH_ERROR`), or receiving an incoming media stream from the stage (`SUBSCRIBE_ERROR`).

The code property of a `StageError` reports the specific problem:


| Name | Code | Recommended Action | 
| --- | --- | --- | 
| TOKEN\_MALFORMED | 1 | Create a valid token and retry instantiating the stage. | 
| TOKEN\_EXPIRED | 2 | Create an unexpired token and retry instantiating the stage. | 
| TIMEOUT | 3 | The operation timed out. If the stage exists and the token is valid, this failure likely is a network issue. In that case, wait for the device’s connectivity to recover. | 
| FAILED | 4 | A fatal condition was encountered when attempting an operation. Check error details.<br />If the stage exists and the token is valid, this failure likely is a network issue. In that case, wait for the device’s connectivity to recover.<br />For most failures related to network stability, the SDK will retry internally for a period of up to 30 seconds before emitting a FAILED error.  | 
| CANCELED | 5 | Check application code and ensure there are no repeated `join`, `refreshStrategy`, or `replaceStrategy` invocations, which may cause repeated operations to be started and canceled before completion. | 
| STAGE\_AT\_CAPACITY | 6 | This error indicates that the stage or your account is at capacity. If the stage has reached its participant limit, try the operation again when the stage is no longer at capacity, by refreshing the strategy. If your account has reached its concurrent subscriptions or concurrent publishers quota, reduce usage or request a quota increase through the [AWS Service Quotas console](https://console.aws.amazon.com/servicequotas/).  | 
| CODEC\_MISMATCH | 7 | The codec is not supported by the stage. Check the browser and platform for codec support. For IVS real-time streaming, browsers must support the H.264 codec for video and the Opus codec for audio. | 
| TOKEN\_NOT\_ALLOWED | 8 | The token does not have permission for the operation. Recreate the token with the correct permission(s) and try again. | 
| STAGE\_DELETED | 9 | None; attempting to join a deleted stage triggers this error. | 
| PARTICIPANT\_DISCONNECTED | 10 | None; attempting to join with a token of a disconnected participant triggers this error. | 

### Handling StageError Example
<a name="web-error-handling-stage-errors-example"></a>

Use the StageError code to determine if the error is due to an expired token:

```
stage.on(StageEvents.ERROR, (error: StageError) => {
    if (error.code === StageError.TOKEN_EXPIRED) {
        // recreate the token and stage instance and re-join
    }
});
```

### Network Errors when Already Joined
<a name="web-error-handling-stage-errors-network"></a>

If the device’s network connection goes down, the SDK may lose its connection to stage servers. You may see errors in the console because the SDK can no longer reach backend services. POSTs to https://broadcast.stats.live-video.net will fail.

If you are publishing and/or subscribing, you will see errors in the console related to attempts to publish/subscribe.

Internally the SDK will try to reconnect with an exponential backoff strategy.

**Action**: Wait for the device’s connectivity to recover.

## Errored States
<a name="web-error-handling-errored-states"></a>

We recommend you use these states for application logging and to display messaging to users that alerts them of connectivity issues to the stage for a particular participant.

### Publish
<a name="errored-states-publish"></a>

The SDK reports `ERRORED` when a publish fails.

```
stage.on(StageEvents.STAGE_PARTICIPANT_PUBLISH_STATE_CHANGED, (participantInfo, state) => {
  if (state === StageParticipantPublishState.ERRORED) {
      // Log and/or display message to user
  }
});
```

### Subscribe
<a name="errored-states-subscribe"></a>

The SDK reports `ERRORED` when a subscribe fails. This can occur due to network conditions or if a stage is at capacity for subscribers.

```
stage.on(StageEvents.STAGE_PARTICIPANT_SUBSCRIBE_STATE_CHANGED, (participantInfo, state) => {
  if (state === StageParticipantSubscribeState.ERRORED) {
    // Log and/or display message to user
  }
});
```