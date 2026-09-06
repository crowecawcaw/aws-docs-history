

# Get the current availability state of the agent in Connect Customer agent workspace
<a name="3P-apps-agent-requests-getavailabilitystate"></a>

Returns the current availability state of the agent currently logged in to the Connect Customer agent workspace, along with the next pending state if one is queued because the agent is handling an active contact.

This API supersedes [getState()](3P-apps-agent-requests-getstate.md), which is now deprecated.

```
async getAvailabilityState(): Promise<GetAvailabilityStateResult>
```

 **Output - GetAvailabilityStateResult** 


| **Parameter** | **Type** | **Description** | 
| --- | --- | --- | 
| agentStateARN | string (optional) | The ARN of the agent's current availability state. | 
| name | string | The name of the agent's current availability state. | 
| type | AgentStateType | The agent's current availability state type. One of routable, not\_routable, after\_call\_work, system, error, or offline. | 
| startTimestamp | Date (optional) | The time at which the agent entered this state. | 
| nextState | AgentState (optional) | The next state the agent will transition to once all active contacts are cleared, when one is queued. | 

 **Permissions required:** 

```
*
```