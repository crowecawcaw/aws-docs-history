

# Disconnect a participant from a contact in Connect Customer agent workspace
<a name="3P-apps-contact-requests-disconnectparticipant"></a>

Disconnects a specific participant from the contact.

 **Signature** 

```
disconnectParticipant(participantId: string): Promise<void>
```

 **Usage** 

```
await contactClient.disconnectParticipant("participant-456");
console.log("Participant disconnected");
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| participantId Required | string | The unique identifier for the participant to disconnect | 

 **Permissions required:** 

```
*
```