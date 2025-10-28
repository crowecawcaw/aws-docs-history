# Set the agent

state with the given agent state name in Amazon Connect Agent Workspace

Sets the agent state with the given agent state name. The promise resolves after
the agent state is set in the backend. The response status is either
`updated` or `queued` based on the current agent
state.

**Signature**

```
setAvailabilityStateByName(
    agentStateName: string,
  ): Promise<SetAvailabilityStateResult>

```

**Usage**

```

const availabilityStateResult: SetAvailabilityStateResult = await agentClient.setAvailabilityStateByName('Available');

```

**Input**

| **Parameter**             | **Type**   | **Description**                                                                                           |
| ------------------------- | ---------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| agentStateName _Required_ | string     | The name of the agent state                                                                               | **Output - SetAvailabilityStateResult**             |
| **Parameter**             | **Type**   | **Description**                                                                                           |
| ---                       | ---        | ---                                                                                                       |
| status                    | string     | The status will be "updated" or "queued" depends on if the agent is currently handling an active contact. |
| current                   | AgentState | Reperesents the current state of the agent.                                                               |
| next                      | AgentState | It'll be the target state if the agent is handling active contact. Applicable when the status is `queued` | **Permissions required:** `User.Configuration.Edit` |
