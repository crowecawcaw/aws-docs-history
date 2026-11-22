

# Stop a conversational analytics for external voice

You can use the [StopContactRecording](https://docs.aws.amazon.com/connect/latest/APIReference/API_StopContactRecording.html) API to end a conversational analytics for an external voice contact while the call is in progress. You can do this only through the API. Stopping recording ends the recording and conversational analytics capabilities.

If the call involved transfers or conferences, the conversational analytics ends for every contact in the chain, not only the contact you specify.

Call StopContactRecording with `InstanceId`, `InitialContactId`, and `ContactId`. To end the session, pass the initial contact or any contact currently in the chain.