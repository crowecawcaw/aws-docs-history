

# Subscribe a callback function when an Connect Customer agent workspace agent state changes - Deprecated
<a name="3P-apps-agent-events-statechanged-sub"></a>

**Note**  
This API is deprecated, use [onAvailabilityStateChanged()](3P-apps-agent-events-availabilitystatechanged-sub.md) instead.

Subscribes a callback function to-be-invoked whenever an agent state changed event occurs in the Connect Customer agent workspace.

 **Signature** 

```
onStateChanged(handler: AgentStateChangedHandler)
```

 **Usage** 

```
const handler: AgentStateChangedHandler = async (data: AgentStateChangedEventData) => {
    console.log("Agent state change occurred! " + data);
};

agentClient.onStateChanged(handler);

// AgentStateChangedEventData Structure
{
  state: string;
  previous: {
    state: string;
  };
}
```

 **Permissions required:** 

```
User.Status.View                
```