

# Subscribe a callback function when an Connect Customer agent workspace agent's availability state changes
<a name="3P-apps-agent-events-availabilitystatechanged-sub"></a>

Subscribes a callback function to be invoked whenever the agent's availability state changes in the Connect Customer agent workspace.

This API supersedes [onStateChanged()](3P-apps-agent-events-statechanged-sub.md), which is now deprecated.

 **Signature** 

```
onAvailabilityStateChanged(handler: AvailabilityStateChangedHandler)
```

 **Usage** 

```
const handler: AvailabilityStateChangedHandler = async (data: AgentAvailabilityStateChanged) => {
    console.log("Agent availability state changed! " + data.state.name);
};

agentClient.onAvailabilityStateChanged(handler);

// AgentAvailabilityStateChanged Structure
{
  state: AgentState;
  previous?: {
    state: AgentState;
  };
}
```

 **Permissions required:** 

```
*
```