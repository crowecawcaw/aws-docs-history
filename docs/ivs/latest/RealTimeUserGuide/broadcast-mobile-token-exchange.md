

# IVS Broadcast SDK: Token Exchange \| Real-Time Streaming
<a name="broadcast-mobile-token-exchange"></a>

Token exchange enables you to upgrade or downgrade participant-token capabilities and update token attributes within the broadcast SDK, without requiring participants to reconnect. This is useful for scenarios like co-hosting, where participants may start with subscribe-only capabilities and later need publish capabilities.

Token exchange is supported in both the mobile and web broadcast SDKs. When a participant exchanges a token, server-side composition detects the updated attributes in real time and automatically adjusts the layout — for example, reassigning the featured slot, reordering participants, or moving a participant into the picture-in-picture overlay — without requiring a reconnect. 

Limitation: Token exchange only works with tokens created on your server using a [key pair](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-distribute-tokens.html#getting-started-distribute-tokens-self-signed). It does not work with tokens created via the [CreateParticipantToken API](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CreateParticipantToken.html).

## Exchanging Tokens
<a name="broadcast-mobile-token-exchange-exchanging-tokens"></a>

Exchanging tokens is straightforward: call the `exchangeToken` API on the `Stage` / `IVSStage` object and provide the new token. If the `capabilities` of the new token are different than those of the previous token, the new token's capabilities are evaluated immediately. For example, if the previous token did not have the `publish` capability and the new token does, the stage strategy functions for publishing are invoked, allowing the host application to decide if they want to publish right away with the new capability, or wait. The same is true for removed capabilities: if the previous token had the `publish` capability and the new token does not, the participant immediately unpublishes without invoking the stage strategy functions for publishing.

When exchanging a token, the previous and new token must have the same values for the following payload fields: 
+ `topic`
+ `resource`
+ `jti`
+ `whip_url`
+ `events_url`

These fields are immutable. Exchanging a token that modifies an immutable field results in the SDK immediately rejecting the exchange.

The remaining fields can be changed, including:
+ `attributes`
+ `capabilities`
+ `user`
+ `_id`
+ `iat`
+ `exp`

### iOS
<a name="broadcast-mobile-token-exchange-exchanging-tokens-ios"></a>



```
let stage = try IVSStage(token: originalToken, strategy: self)
stage.join()
stage.exchangeToken(newToken)
```

### Android
<a name="broadcast-mobile-token-exchange-exchanging-tokens-android"></a>



```
val stage = Stage(context, originalToken, strategy)
stage.join()
stage.exchangeToken(newToken)
```

### Web
<a name="broadcast-web-token-exchange-exchanging-tokens"></a>



```
const stage = new Stage(originalToken, strategy);
await stage.join();
await stage.exchangeToken(newToken);
```

## Receiving Updates
<a name="broadcast-mobile-token-exchange-receiving-updates"></a>

A function in `StageRenderer` / `IVSStageRenderer` receives updates about already-published, remote participants that exchange their tokens to update their `userId` or `attributes`. Remote participants that are not already publishing will have their updated `userId` and `attributes` exposed via the existing `onParticipantJoined` / `participantDidJoin` renderer functions if they eventually publish.

### iOS
<a name="broadcast-mobile-token-exchange-receiving-updates-ios"></a>



```
class MyStageRenderer: NSObject, IVSStageRenderer {
    func stage(_ stage: IVSStage, participantMetadataDidUpdate participant: IVSParticipantInfo) {
        // participant will be a new IVSParticipantInfo instance with updated properties.
    }
}
```

### Android
<a name="broadcast-mobile-token-exchange-receiving-updates-android"></a>



```
private val stageRenderer = object : StageRenderer {
    override fun onParticipantMetadataUpdated(stage: Stage, participantInfo: ParticipantInfo) {
        // participantInfo will be a new ParticipantInfo instance with updated properties.
    }
}
```

### Web
<a name="broadcast-web-token-exchange-receiving-updates"></a>



```
stage.on(StageEvents.STAGE_PARTICIPANT_METADATA_CHANGED, (participantInfo: StageParticipantInfo) => { 
    // participantInfo properties will be updated with the changed properties 
    }
);
```

## Visibility of Updates
<a name="broadcast-mobile-token-exchange-visibility"></a>

When a participant exchanges a token to update their `userId` or `attributes`, the visibility of these changes depends on their current publishing state: 
+ **If the participant is *not* publishing:** The update is processed silently. If they eventually publish, all SDKs will receive the updated `userId` and `attributes` as part of the initial publish event.
+ **If the participant *is* already publishing:** The update is broadcast immediately for participants using mobile SDKs v1.37.0\+, the web SDK, and server-side composition. Participants using older mobile SDKs do not see the change until the participant unpublishes and republishes.

This table clarifies the matrix of support:


| Participant State | Observer: Mobile SDK 1.37.0\+, Web SDK, Server-Side Composition  | Observer: Older Mobile SDKs | 
| --- | --- | --- | 
| Not publishing (then starts) | ✅ Visible (on publish through participant joined event) | ✅ Visible (on publish through participant joined event) | 
| Already publishing (never republishes) | ✅ Visible (immediately through participant metadata updated event) | ❌ Not Visible | 
| Already publishing (unpublishes and republishes) | ✅ Visible (immediately through participant metadata updated event) | ⚠️ Eventually Visible (on republish through participant joined event) | 