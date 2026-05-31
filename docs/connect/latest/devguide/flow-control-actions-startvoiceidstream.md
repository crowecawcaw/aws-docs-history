# StartVoiceIdStream

Sends audio to Connect Customer Voice ID to verify the caller's identity and match
against fraudsters in watchlist, as soon as the call is connected to a flow.

## Parameter object

```
{

}
```

## Execution results and conditions

None. No conditions are supported.

## Errors

- NoMatchingError if no condition matches.

## Restrictions

Only supported for the voice channel. If used with the chat or task channels, the
action takes the **Error** branch. Not supported in hold
flows.

## Corresponding block in the UI

[Set
Voice ID](../adminguide/set-voice-id.md "../adminguide/set-voice-id.md")
