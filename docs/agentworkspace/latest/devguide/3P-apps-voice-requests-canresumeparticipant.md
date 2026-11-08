

# Check if a participant can be resumed from hold in Connect Customer agent workspace
<a name="3P-apps-voice-requests-canresumeparticipant"></a>

Checks whether a specific participant can be resumed from hold.

 **Signature** 

```
canResumeParticipant(participantId: string): Promise<boolean>
```

 **Usage** 

```
const canResume = await voiceClient.canResumeParticipant("participant-456");
if (canResume) {
  await voiceClient.resumeParticipant("participant-456");
}
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| participantId Required | string | The unique identifier for the participant | 

 **Output** 

Returns a Promise that resolves to a boolean: true if the participant can be resumed, false otherwise

 **Contact scope:** 

Requires an instance that is scoped to the contact that the participant belongs to, or an instance without a contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```
*
```