

# Get participant state in Connect Customer agent workspace
<a name="3P-apps-contact-requests-getparticipantstate"></a>

Retrieves the current state of a specific participant.

 **Signature** 

```
getParticipantState(participantId: string): Promise<ParticipantState>
```

 **Usage** 

```
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

 **Permissions required:** 

```
*
```