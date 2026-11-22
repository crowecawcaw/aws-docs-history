

# Subscribe a callback function when an Connect Customer agent workspace agent's availability state changes

Subscribes a callback function to be invoked whenever the agent's availability state changes in the Connect Customer agent workspace.

 **Signature** 

```typescript
onAvailabilityStateChanged(handler: AvailabilityStateChangedHandler)
```

 **Usage** 

```typescript
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

```typescript
*
```