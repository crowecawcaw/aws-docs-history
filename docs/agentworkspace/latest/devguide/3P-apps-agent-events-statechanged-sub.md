# Subscribe a callback

function when an Amazon Connect Agent Workspace agent state changes

Subscribes a callback function to-be-invoked whenever an agent state changed event
occurs in the Amazon Connect agent workspace.

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
