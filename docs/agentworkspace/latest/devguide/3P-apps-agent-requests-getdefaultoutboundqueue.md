

# Get the default outbound queue for the agent in Connect Customer agent workspace
<a name="3P-apps-agent-requests-getdefaultoutboundqueue"></a>

Returns the default outbound queue for the agent currently logged in to the Connect Customer agent workspace. This is the queue used for outbound contacts the agent originates when no other queue is specified. The returned `Queue` contains `name`, `queueARN`, and `queueId`.

```
async getDefaultOutboundQueue(): Promise<Queue>
```

 **Permissions required:** 

```
*
```