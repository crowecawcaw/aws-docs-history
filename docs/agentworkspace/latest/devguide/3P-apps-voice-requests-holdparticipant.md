

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