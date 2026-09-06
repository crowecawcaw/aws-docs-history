

# Get the current state of the agent in Connect Customer agent workspace - Deprecated
<a name="3P-apps-agent-requests-getstate"></a>

**Note**  
This API is deprecated, use [getAvailabilityState()](3P-apps-agent-requests-getavailabilitystate.md) instead.

Returns the Connect Customer agent workspace agent's current `AgentState` object indicating their availability state type. This object contains the following fields:
+ `agentStateARN`: The agent's current state ARN.
+ `name`: The name of the agent's current availability state.
+ `startTimestamp`: A `Date` object that indicates when the state was set.
+ `type`: The agent's current availability state type, as per the ` AgentStateType` enumeration. The different values are as follows:
  +  `routable` 
  +  `not_routable` 
  +  `after_call_work` 
  +  `system` 
  +  `error` 
  +  `offline` 

```
async getState(): Promise<AgentState>          
```

 **Permissions required:** 

```
User.Status.View                
```