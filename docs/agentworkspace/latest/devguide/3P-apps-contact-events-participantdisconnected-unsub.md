

# Unsubscribe from participant disconnected events in Connect Customer agent workspace
<a name="3P-apps-contact-events-participantdisconnected-unsub"></a>

Unsubscribes from participant disconnected events.

 **Signature** 

```
offParticipantDisconnected(handler: ParticipantDisconnectedHandler, contactId?: string): void
```

 **Usage** 

```
contactClient.offParticipantDisconnected(handleParticipantDisconnected);
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| handler Required | ParticipantDisconnectedHandler | Event handler function to remove | 
| contactId | string | Optional contact ID to unsubscribe from specific contact events | 