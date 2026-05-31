# CheckOutboundCallStatus

Engages with the output provided by an answering machine, and provides branches to
route the contact accordingly.

## Parameter object

```
{

}
```

## Execution results and conditions

- "CallAnswered" if the call has been answered by a person.
- "VoicemailBeep" if Connect Customer identifies that the call ended in a
  voice mail and it detects a beep.
- "VoicemailNoBeep" if Connect Customer identifies that call ended in a
  voicemail, but it doesn't detect a beep, or the beep is unknown.
- "NotDetected" if Connect Customer could not detect whether there is a
  voicemail. This happens when Connect Customer is unable to make a positive
  determination of whether a call was answered by a live voice or an answering
  machine. Typical situations that result in this state include long silences
  or excessive background noise.

Conditions are supported, but only the "Equals" operator is supported.
"CallAnswered", "VoicemailBeep" , "VoicemailNoBeep" and "NotDetected" are the only
supported operands.

## Errors

- NoMatchingError if no condition matches.

## Restrictions

This action works with [Connect Customer outbound campaigns](../adminguide/enable-outbound-campaigns.md "../adminguide/enable-outbound-campaigns.md") only.

## Corresponding block in the UI

[Check call
progress](../adminguide/check-call-progress.md "../adminguide/check-call-progress.md")
