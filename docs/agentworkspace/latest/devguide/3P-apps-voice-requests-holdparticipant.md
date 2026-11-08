

# Place a participant on hold in Connect Customer agent workspace
<a name="3P-apps-voice-requests-holdparticipant"></a>

Places a specific participant on hold.

 **Signature** 

```
holdParticipant(participantId: string): Promise<void>
```

 **Usage** 

```
await voiceClient.holdParticipant("participant-456");
console.log("Participant is now on hold");
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| participantId Required | string | The unique identifier for the participant to place on hold | 

 **Contact scope:** 

Requires an instance that is scoped to the contact that the participant belongs to, or an instance without a contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```
*
```