# Sets the agent state to Offline

in Amazon Connect Agent Workspace

Sets the agent state to Offline. The promise resolves after the agent state is
set in the backend.

**Signature**

```
  setOffline(): Promise<SetAvailabilityStateResult>

```

**Usage**

```
const availabilityStateResult: SetAvailabilityStateResult = await agentClient.setOffline();

```

**Output - SetAvailabilityStateResult**

| **Parameter** | **Type**   | **Description**                                                                                             |
| ------------- | ---------- | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| status        | string     | The status will be `updated` or `queued` depending on if the agent is currently handling an active contact. |
| current       | AgentState | Represents the current state of the agent.                                                                  |
| next          | AgentState | It'll be the target state if the agent is handling active contact. Applicable when the status is `queued`.  | **Permissions required:** `User.Configuration.Edit` |
