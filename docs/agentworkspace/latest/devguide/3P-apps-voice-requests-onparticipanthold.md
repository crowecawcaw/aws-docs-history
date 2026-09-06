

# Subscribe to participant hold events in Connect Customer agent workspace
<a name="3P-apps-voice-requests-onparticipanthold"></a>

Subscribes to events when any participant is put on hold.

 **Signature** 

```
onParticipantHold(
  handler: ParticipantHoldHandler,
  participantId?: string
): void
```

 **Usage** 

```
const handleParticipantHold = (event) => {
  console.log(`Participant ${event.participantId} is now on hold`);
  console.log(`Contact: ${event.contactId}`);
};
// Subscribe to all participants
voiceClient.onParticipantHold(handleParticipantHold);
// Or subscribe to a specific participant
voiceClient.onParticipantHold(handleParticipantHold, "participant-456");
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| handler Required | ParticipantHoldHandler | Event handler function to call when participants are put on hold | 
| participantId | string | Optional participant ID to filter events for a specific participant | 