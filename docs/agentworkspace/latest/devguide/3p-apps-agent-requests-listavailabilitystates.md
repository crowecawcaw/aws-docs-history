# Get all the

availability states configured for the current agent in Amazon Connect Agent Workspace

Get all the availability states configured for the current agent.

**Signature**

```
listAvailabilityStates(): Promise<AgentState[]>

```

**Usage**

```
const availabilityStates: AgentState[] = await agentClient.listAvailabilityStates();

```

**Output - AgentState**

| **Parameter**  | **Type** | **Description**                                        |
| -------------- | -------- | ------------------------------------------------------ | --------------------------------------------------- | ----------------------------------------------------- | -------- | ------- |
| agentStateARN  | string   | Amazon Reference Number of agent state                 |
| type           | string   | It could be "routable"                                 | "not_routable"                                      | "after_call_work"                                     | "system" | "error" |
| "offline"      |          | name                                                   | string                                              | Name of the agent state like `Available` or `Offline` |
| startTimestamp | Date     | A `Date` object that indicates when the state was set. | **Permissions required:** `User.Configuration.View` |
