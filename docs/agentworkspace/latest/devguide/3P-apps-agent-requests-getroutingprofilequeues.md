

# Get the queues on the agent's routing profile in Connect Customer agent workspace
<a name="3P-apps-agent-requests-getroutingprofilequeues"></a>

Returns the list of queues on the routing profile of the agent currently logged in to the Connect Customer agent workspace. Each `Queue` contains `name`, `queueARN`, and `queueId`.

```
async getRoutingProfileQueues(): Promise<Queue[]>
```

 **Permissions required:** 

```
*
```