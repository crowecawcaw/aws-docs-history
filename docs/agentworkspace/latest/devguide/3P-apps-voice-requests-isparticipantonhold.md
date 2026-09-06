

# Check if a participant is on hold in Connect Customer agent workspace
<a name="3P-apps-voice-requests-isparticipantonhold"></a>

Checks whether a specific participant is currently on hold.

 **Signature** 

```
isParticipantOnHold(participantId: string): Promise<boolean>
```

 **Usage** 

```
const isOnHold = await voiceClient.isParticipantOnHold("participant-456");
if (isOnHold) {
  console.log("Participant is on hold");
} else {
  console.log("Participant is active");
}
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| participantId Required | string | The unique identifier for the participant | 

 **Output** 

Returns a Promise that resolves to a boolean: true if the participant is on hold, false otherwise