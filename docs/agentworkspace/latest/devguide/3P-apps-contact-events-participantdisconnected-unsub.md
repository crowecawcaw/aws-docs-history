

# Unsubscribe from participant disconnected events in Connect Customer agent workspace

Unsubscribes from participant disconnected events.

 **Signature** 

```typescript
offParticipantDisconnected(handler: ParticipantDisconnectedHandler, contactId?: string): void
```

 **Usage** 

```typescript
contactClient.offParticipantDisconnected(handleParticipantDisconnected);
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| handler Required | ParticipantDisconnectedHandler | Event handler function to remove | 
| contactId | string | Optional contact ID to unsubscribe from specific contact events | 