

# Unsubscribe from participant added events in Connect Customer agent workspace
<a name="3P-apps-contact-events-participantadded-unsub"></a>

Unsubscribes from participant added events.

 **Signature** 

```
offParticipantAdded(handler: ParticipantAddedHandler, contactId?: string): void
```

 **Usage** 

```
contactClient.offParticipantAdded(handleParticipantAdded);
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| handler Required | ParticipantAddedHandler | Event handler function to remove | 
| contactId | string | Optional contact ID to unsubscribe from specific contact events | 