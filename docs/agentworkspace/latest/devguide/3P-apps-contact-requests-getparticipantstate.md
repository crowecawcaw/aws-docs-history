

# Get participant state in Connect Customer agent workspace

Retrieves the current state of a specific participant.

 **Signature** 

```typescript
getParticipantState(participantId: string): Promise<ParticipantState>
```

 **Usage** 

```typescript
const state = await contactClient.getParticipantState("participant-456");
if (state.value === "connected") {
    console.log("Participant is connected");
} else if (state.value === "hold") {
    console.log("Participant is on hold");
}
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| participantId Required | string | The unique identifier for the participant | 

 **Output - ParticipantState** 

The ParticipantState type can be:
+ { value: ParticipantStateType } where ParticipantStateType includes: connecting, connected, hold, disconnected, rejected, silent\_monitor, barge
+ { value: "other"; actual: string } for unknown states

 **Contact scope:** 

Requires an instance that is scoped to the contact that the participant belongs to, or an instance without a contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```typescript
*
```