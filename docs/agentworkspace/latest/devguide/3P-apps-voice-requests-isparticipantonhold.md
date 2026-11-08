

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

 **Contact scope:** 

Requires an instance that is scoped to the contact that the participant belongs to, or an instance without a contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```
*
```