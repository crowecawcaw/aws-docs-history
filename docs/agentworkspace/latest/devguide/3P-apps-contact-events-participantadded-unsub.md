

# Unsubscribe from participant added events in Connect Customer agent workspace

Unsubscribes from participant added events.

 **Signature** 

```typescript
offParticipantAdded(handler: ParticipantAddedHandler, contactId?: string): void
```

 **Usage** 

```typescript
contactClient.offParticipantAdded(handleParticipantAdded);
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| handler Required | ParticipantAddedHandler | Event handler function to remove | 
| contactId | string | Optional contact ID to unsubscribe from specific contact events | 