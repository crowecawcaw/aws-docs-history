# Set the agent state

with the given agent state ARN in Amazon Connect Agent Workspace

Set the agent state with the given agent state ARN. By default, the promise
resolves after the agent state is set in the backend. The response status is either
`updated` or `queued` based on the current agent
state.

**Signature**

```
 setAvailabilityState(
    agentStateARN: string,
  ): Promise<SetAvailabilityStateResult>

```

**Usage**

```
const availabilityStates: AgentState[] = await agentClient.listAvailabilityStates();
const availabilityStateResult:SetAvailabilityStateResult **=** await agentClient.setAvailabilityState(availabilityStates[0].agentStateARN);
```

**Input**

| **Parameter**            | **Type** | **Description**            |
| ------------------------ | -------- | -------------------------- |
| agentStateARN _Required_ | string   | The ARN of the agent state |

**Output - SetAvailabilityStateResult**

| **Parameter** | **Type**   | **Description**                                                                                                |
| ------------- | ---------- | -------------------------------------------------------------------------------------------------------------- |
| status        | string     | The status will be `updated` or `queued`<br>depending on if the agent is currently handling an active contact. |
| current       | AgentState | Reperesents the current state of the agent.                                                                    |
| next          | AgentState | It'll be the target state if the agent is handling active<br>contact. Applicable when the status is `queued`.  |

**Permissions required:**

```
User.Configuration.Edit

```
