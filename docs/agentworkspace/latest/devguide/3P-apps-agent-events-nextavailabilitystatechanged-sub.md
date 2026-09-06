

# Subscribe a callback function when an Connect Customer agent workspace agent's next queued availability state changes
<a name="3P-apps-agent-events-nextavailabilitystatechanged-sub"></a>

Subscribes a callback function to be invoked whenever the agent's next queued availability state changes in the Connect Customer agent workspace. The next state is the availability state that is queued to apply once all of the agent's active contacts are cleared. This event fires when a new next state is queued, when a queued next state is replaced, or when a queued next state is cleared.

 **Signature** 

```
onNextAvailabilityStateChanged(handler: NextAvailabilityStateChangedHandler)
```

 **Usage** 

```
const handler: NextAvailabilityStateChangedHandler = async (data: NextAgentAvailabilityStateChanged) => {
    console.log("Next availability state changed! " + data.nextState?.name);
};

agentClient.onNextAvailabilityStateChanged(handler);

// NextAgentAvailabilityStateChanged Structure
{
  nextState: AgentState | null;
  previous?: {
    nextState: AgentState;
  };
}
```

 **Permissions required:** 

```
*
```