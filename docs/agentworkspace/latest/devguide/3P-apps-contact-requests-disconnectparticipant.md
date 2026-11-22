

# Disconnect a participant from a contact in Connect Customer agent workspace

Disconnects a specific participant from the contact.

 **Signature** 

```typescript
disconnectParticipant(participantId: string): Promise<void>
```

 **Usage** 

```typescript
await contactClient.disconnectParticipant("participant-456");
console.log("Participant disconnected");
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| participantId Required | string | The unique identifier for the participant to disconnect | 

 **Contact scope:** 

Requires an instance that is scoped to the contact that the participant belongs to, or an instance without a contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```typescript
*
```