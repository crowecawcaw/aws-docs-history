# Error Handling in the IVS Web Broadcast

SDK | Real-Time Streaming

This section is an overview of error conditions, how the Web broadcast SDK reports
them to the application, and what an application should do when those errors are
encountered. Errors are reported by the SDK to listeners of the
`StageEvents.ERROR` event:

```
stage.on(StageEvents.ERROR, (error: StageError) => {
    // log or handle errors here
    console.log(`${error.code}, ${error.category}, ${error.message}`);
});
```

## Stage Errors

A StageError is reported when the SDK encounters a problem it cannot recover from
and generally requires app intervention and/or network reconnection to
recover.

Each reported `StageError` has a code (or `StageErrorCode`),
message (string), and category (`StageErrorCategory`). Each is related to
an underlying operation category.

The operation category of the error is determined based on whether it is related
to the connection to the stage (`JOIN_ERROR`), sending media to the stage
(`PUBLISH_ERROR`), or receiving an incoming media stream from the
stage (`SUBSCRIBE_ERROR`).

The code property of a `StageError` reports the specific
problem:

| Name                     | Code | Recommended Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------ | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TOKEN_MALFORMED          | 1    | Create a valid token and retry instantiating the<br>stage.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| TOKEN_EXPIRED            | 2    | Create an unexpired token and retry instantiating the<br>stage.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| TIMEOUT                  | 3    | The operation timed out. If the stage exists and the token<br>is valid, this failure likely is a network issue. In that case,<br>wait for the device’s connectivity to recover.                                                                                                                                                                                                                                                                                                                               |
| FAILED                   | 4    | A fatal condition was encountered when attempting an<br>operation. Check error details.<br>If the stage exists and the token is valid, this failure<br>likely is a network issue. In that case, wait for the device’s<br>connectivity to recover.<br>For most failures related to network stability, the SDK will<br>retry internally for a period of up to 30 seconds before<br>emitting a FAILED error.                                                                                                     |
| CANCELED                 | 5    | Check application code and ensure there are no repeated<br>`join`, `refreshStrategy`, or<br>`replaceStrategy` invocations, which may cause<br>repeated operations to be started and canceled before<br>completion.                                                                                                                                                                                                                                                                                            |
| STAGE_AT_CAPACITY        | 6    | This error indicates that the stage or your account is at<br>capacity. If the stage has reached its participant limit, try<br>the operation again when the stage is no longer at capacity, by<br>refreshing the strategy. If your account has reached its<br>concurrent subscriptions or concurrent publishers quota, reduce<br>usage or request a quota increase through the [AWS<br>Service Quotas console](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/"). |
| CODEC_MISMATCH           | 7    | The codec is not supported by the stage. Check the browser<br>and platform for codec support. For IVS real-time streaming,<br>browsers must support the H.264 codec for video and the Opus<br>codec for audio.                                                                                                                                                                                                                                                                                                |
| TOKEN_NOT_ALLOWED        | 8    | The token does not have permission for the operation.<br>Recreate the token with the correct permission(s) and try<br>again.                                                                                                                                                                                                                                                                                                                                                                                  |
| STAGE_DELETED            | 9    | None; attempting to join a deleted stage triggers this<br>error.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| PARTICIPANT_DISCONNECTED | 10   | None; attempting to join with a token of a disconnected<br>participant triggers this error.                                                                                                                                                                                                                                                                                                                                                                                                                   |

### Handling StageError

Example

Use the StageError code to determine if the error is due to an expired
token:

```
stage.on(StageEvents.ERROR, (error: StageError) => {
    if (error.code === StageError.TOKEN_EXPIRED) {
        // recreate the token and stage instance and re-join
    }
});
```

### Network Errors when

Already Joined

If the device’s network connection goes down, the SDK may lose its connection
to stage servers. You may see errors in the console because the SDK can no
longer reach backend services. POSTs to https://broadcast.stats.live-video.net
will fail.

If you are publishing and/or subscribing, you will see errors in the console
related to attempts to publish/subscribe.

Internally the SDK will try to reconnect with an exponential backoff
strategy.

**Action**: Wait for the device’s connectivity to
recover.

## Errored States

We recommend you use these states for application logging and to display messaging
to users that alerts them of connectivity issues to the stage for a particular
participant.

### Publish

The SDK reports `ERRORED` when a publish fails.

```
stage.on(StageEvents.STAGE_PARTICIPANT_PUBLISH_STATE_CHANGED, (participantInfo, state) => {
  if (state === StageParticipantPublishState.ERRORED) {
      // Log and/or display message to user
  }
});
```

### Subscribe

The SDK reports `ERRORED` when a subscribe fails. This can occur
due to network conditions or if a stage is at capacity for subscribers.

```
stage.on(StageEvents.STAGE_PARTICIPANT_SUBSCRIBE_STATE_CHANGED, (participantInfo, state) => {
  if (state === StageParticipantSubscribeState.ERRORED) {
    // Log and/or display message to user
  }
});
```
