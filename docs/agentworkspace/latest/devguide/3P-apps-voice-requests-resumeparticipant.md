

# Resume a participant from hold in Connect Customer agent workspace
<a name="3P-apps-voice-requests-resumeparticipant"></a>

Resumes a specific participant from hold.

 **Signature** 

```
resumeParticipant(participantId: string): Promise<void>
```

 **Usage** 

```
await voiceClient.resumeParticipant("participant-456");
console.log("Participant has been resumed");
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| participantId Required | string | The unique identifier for the participant to resume | 

 **Contact scope:** 

Requires an instance that is scoped to the contact that the participant belongs to, or an instance without a contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```
*
```