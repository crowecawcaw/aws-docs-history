

# Get specific participant information in Connect Customer agent workspace
<a name="3P-apps-contact-requests-getparticipant"></a>

Retrieves information for a specific participant.

 **Signature** 

```
getParticipant(participantId: string): Promise<ParticipantData>
```

 **Usage** 

```
const participant = await contactClient.getParticipant("participant-456");
console.log(`Participant type: ${participant.type.value}`);
console.log(`Is initial: ${participant.isInitial}`);
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| participantId Required | string | The unique identifier for the participant | 

 **Output - ParticipantData** 

Returns a ParticipantData object with participant details.

 **Permissions required:** 

```
*
```