

# CompleteOutboundCall
<a name="contact-actions-completeoutboundcall"></a>

When a flow is run before an outbound call is made as part of an outbound contact, this action calls the outbound destination. If this action is not used, the first participant action implicitly completes the outbound call. 

## Parameter object
<a name="completeoutboundcall-parameter"></a>

```
""CallerId": { Optional, an override of the caller ID to present when calling. Is ignored when using VoiceConnectors
  "Number": The caller ID number to present when calling. Can either be fully static or a single valid JSONPath identifier
}
"VoiceConnector": { Optional, Configuration of the voice connector 
   "VoiceConnectorType": Only support "ChimeConnector". Must be defined statically.
   "VoiceConnectorArn": The ARN of the Voice Connector. Can be set statically or dynamically.
   "FromUser": The user who makes the call. Can be set statically or dynamically.
   "ToUser": The user who receives the call. Can be set statically or dynamically.
   "UserToUserInformation": Optional, SIP user-to-user information. Can be set statically or dynamically.
}
"ConnectionTimeLimitSeconds": Optional, Only used for Voice Connector use case. An integer between 1 and 600 
                                                         (inclusive) representing the number of seconds 
                                                        to wait for the voice connector to answer before 
                                                        canceling the call. Can be set statically or dynamically.
```

## Results and conditions
<a name="completeoutboundcall-results"></a>

None.

## Errors
<a name="completeoutboundcall-errors"></a>

None.

## Restrictions
<a name="completeoutboundcall-restrictions"></a>

This action can be used only when the contact is in the process of making an outbound call, but has not yet called the outbound number. 

## Corresponding block in the UI
<a name="completeoutboundcall-ui"></a>

[Call phone number](https://docs.aws.amazon.com/connect/latest/adminguide/call-phone-number.html) 