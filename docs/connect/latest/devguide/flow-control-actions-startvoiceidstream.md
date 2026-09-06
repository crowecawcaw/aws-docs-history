

# StartVoiceIdStream
<a name="flow-control-actions-startvoiceidstream"></a>

Sends audio to Connect Customer Voice ID to verify the caller's identity and match against fraudsters in watchlist, as soon as the call is connected to a flow.

## Parameter object
<a name="startvoiceidstream-parameter"></a>

```
{
 
}
```

## Execution results and conditions
<a name="startvoiceidstream-results"></a>

None. No conditions are supported. 

## Errors
<a name="startvoiceidstream-errors"></a>
+ NoMatchingError if no condition matches.

## Restrictions
<a name="startvoiceidstream-restrictions"></a>

Only supported for the voice channel. If used with the chat or task channels, the action takes the **Error** branch. Not supported in hold flows.

## Corresponding block in the UI
<a name="startvoiceidstream-ui"></a>

[Set Voice ID](https://docs.aws.amazon.com/connect/latest/adminguide/set-voice-id.html) 