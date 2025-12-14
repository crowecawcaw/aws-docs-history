# IVS Broadcast SDK: Token Exchange | Real-Time Streaming

Token exchange enables you to upgrade or downgrade participant-token capabilities and update token attributes
within the mobile broadcast SDK, without requiring participants to reconnect. This is useful for scenarios like co-hosting,
where participants may start with subscribe-only capabilities and later need publish capabilities.

Limitations:

- Token exchange only works with tokens created on your server using a
  [key pair](getting-started-distribute-tokens.md#getting-started-distribute-tokens-self-signed "getting-started-distribute-tokens.md#getting-started-distribute-tokens-self-signed").
  It does not work with tokens created via the
  [CreateParticipantToken API](../RealTimeAPIReference/API_CreateParticipantToken.md "../RealTimeAPIReference/API_CreateParticipantToken.md").
- If you use token exchange to change attributes that drive server-side-composition layouts
  (such as featuredParticipantAttribute and participantOrderAttribute), the layout of an active composition will
  not update until the participant reconnects.

## Exchanging Tokens

Exchanging tokens is straightforward: call the `exchangeToken` API on the `Stage` / `IVSStage` object
and provide the new token. If the `capabilities` of the new token are different than those of the previous token,
the new token's capabilities are evaluated immediately. For example, if the previous token did not have the `publish`
capability and the new token does, the stage strategy functions for publishing are invoked, allowing the host
application to decide if they want to publish right away with the new capability, or wait. The same is true for
removed capabilities: if the previous token had the `publish` capability and the new token does not, the participant
immediately unpublishes without invoking the stage strategy functions for publishing.

When exchanging a token, the previous and new token must have the same values for the following payload fields:

- `topic`
- `resource`
- `jti`
- `whip_url`
- `events_url`

These fields are immutable. Exchanging a token that modifies an immutable field results in the SDK immediately rejecting the exchange.

The remaining fields can be changed, including:

- `attributes`
- `capabilities`
- `user`
- `_id`
- `iat`
- `exp`

### iOS

```
let stage = try IVSStage(token: originalToken, strategy: self)
stage.join()
stage.exchangeToken(newToken)
```

### Android

```
val stage = Stage(context, originalToken, strategy)
stage.join()
stage.exchangeToken(newToken)
```

## Receiving Updates

A function in `StageRenderer` / `IVSStageRenderer` receives updates about already-published,
remote participants that exchange their tokens to update their `userId` or `attributes`.
Remote participants that are not already publishing will have their updated `userId` and `attributes`
exposed via the existing `onParticipantJoined` / `participantDidJoin` renderer functions
if they eventually publish.

### iOS

```
class MyStageRenderer: NSObject, IVSStageRenderer {
    func stage(_ stage: IVSStage, participantMetadataDidUpdate participant: IVSParticipantInfo) {
        // participant will be a new IVSParticipantInfo instance with updated properties.
    }
}
```

### Android

```
private val stageRenderer = object : StageRenderer {
    override fun onParticipantMetadataUpdated(stage: Stage, participantInfo: ParticipantInfo) {
        // participantInfo will be a new ParticipantInfo instance with updated properties.
    }
}
```

## Visibility of Updates

When a participant exchanges a token to update their `userId` or `attributes`,
the visibility of these changes depends on their current publishing state:

- **If the participant is _not_ publishing:**
  The update is processed silently. If they eventually publish, all SDKs will receive the updated `userId` and `attributes`
  as part of the initial publish event.
- **If the participant _is_ already publishing:**
  The update is broadcast immediately. However, only mobile SDKs v1.37.0+ receive the notification. Participants on the web SDK, older mobile SDKs, and server-side composition do not see the change until the participant unpublishes and republishes.

This table clarifies the matrix of support:

| Participant State                                | Observer: Mobile SDK 1.37.0+                                        | Observer: Older Mobile SDKs, Web SDK, Server-Side Composition         |
| ------------------------------------------------ | ------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Not publishing (then starts)                     | ✅ Visible (on publish through participant joined event)            | ✅ Visible (on publish through participant joined event)              |
| Already publishing (never republishes)           | ✅ Visible (immediately through participant metadata updated event) | ❌ Not Visible                                                        |
| Already publishing (unpublishes and republishes) | ✅ Visible (immediately through participant metadata updated event) | ⚠️ Eventually Visible (on republish through participant joined event) |
