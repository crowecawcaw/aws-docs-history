# Unsubscribe a callback function when an Connect Customer agent workspace agent state changes - Deprecated

###### Note

This API is deprecated, use [offAvailabilityStateChanged()](3P-apps-agent-events-availabilitystatechanged-unsub.md "3P-apps-agent-events-availabilitystatechanged-unsub.md") instead.

Unsubscribes the callback function from the agent stated change event in the Connect Customer
agent workspace.

**Signature**

```

offStateChanged(handler: AgentStateChangedHandler)

```

**Usage**

```

agentClient.offStateChanged(handler);

```
