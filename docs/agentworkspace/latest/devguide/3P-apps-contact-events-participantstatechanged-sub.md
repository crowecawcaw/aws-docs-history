# Subscribe to participant state change events in Amazon Connect Agent Workspace

Subscribes to participant state change events. This event fires when a participant's
state
changes (e.g., from connecting to connected, or to hold).

**Signature**

```

onParticipantStateChanged(handler: ParticipantStateChangedHandler, participantId?: string): void

```

**Usage**

```

    const handleStateChanged = (event) => {
    console.log(
    `Participant ${event.participantId} state changed to: ${event.state.value}`
    );

    if (event.state.value === "connected") {
    console.log("Participant is now connected");
    } else if (event.state.value === "hold") {
    console.log("Participant is now on hold");
    }
    };

    // Subscribe to all participants
    contactClient.onParticipantStateChanged(handleStateChanged);

    // Or subscribe to a specific participant
    contactClient.onParticipantStateChanged(handleStateChanged, "participant-456");

```

**Input**

| **Parameter**      | **Type**                       | **Description**                                                     |
| ------------------ | ------------------------------ | ------------------------------------------------------------------- |
| handler _Required_ | ParticipantStateChangedHandler | Event handler function to call when participant states change       |
| participantId      | string                         | Optional participant ID to filter events for a specific participant |

**Event Structure - ParticipantStateChanged**

The handler receives a ParticipantStateChanged event with:

- `participantId`: string - The ID of the participant whose state
  changed
- `state`: ParticipantState - The new state of the participant

**Permissions required:**

```

Contact.Details.View

```
