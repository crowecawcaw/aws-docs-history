

# Unsubscribe from participant state change events in Connect Customer agent workspace

Unsubscribes from participant state change events. Pass the same handler and `participantId` that you passed to [onParticipantStateChanged()](3P-apps-contact-events-participantstatechanged-sub.md).

 **Signature** 

```typescript
offParticipantStateChanged(handler: ParticipantStateChangedHandler, participantId?: string): void
```

 **Usage** 

```typescript
contactClient.offParticipantStateChanged(handleStateChanged);
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| handler Required | ParticipantStateChangedHandler | Event handler function to remove | 
| participantId | string | Optional participant ID to unsubscribe from specific participant events | 