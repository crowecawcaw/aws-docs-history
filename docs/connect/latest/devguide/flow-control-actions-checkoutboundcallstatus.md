

# CheckOutboundCallStatus
<a name="flow-control-actions-checkoutboundcallstatus"></a>

Engages with the output provided by an answering machine, and provides branches to route the contact accordingly.

## Parameter object
<a name="checkoutboundcallstatus-parameter"></a>

```
{
 
}
```

## Execution results and conditions
<a name="checkoutboundcallstatus-results"></a>
+ "CallAnswered" if the call has been answered by a person.
+ "VoicemailBeep" if Connect Customer identifies that the call ended in a voice mail and it detects a beep.
+ "VoicemailNoBeep" if Connect Customer identifies that call ended in a voicemail, but it doesn't detect a beep, or the beep is unknown.
+ "NotDetected" if Connect Customer could not detect whether there is a voicemail. This happens when Connect Customer is unable to make a positive determination of whether a call was answered by a live voice or an answering machine. Typical situations that result in this state include long silences or excessive background noise.

Conditions are supported, but only the "Equals" operator is supported. "CallAnswered", "VoicemailBeep" , "VoicemailNoBeep" and "NotDetected" are the only supported operands.

## Errors
<a name="checkoutboundcallstatus-errors"></a>
+ NoMatchingError if no condition matches.

## Restrictions
<a name="checkoutboundcallstatus-restrictions"></a>

This action works with [Connect Customer outbound campaigns](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html) only. 

## Corresponding block in the UI
<a name="checkoutboundcallstatus-ui"></a>

[Check call progress](https://docs.aws.amazon.com/connect/latest/adminguide/check-call-progress.html) 