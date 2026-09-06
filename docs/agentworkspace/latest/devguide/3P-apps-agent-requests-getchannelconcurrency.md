

# Get the limit of contacts for the agent in Connect Customer agent workspace
<a name="3P-apps-agent-requests-getchannelconcurrency"></a>

Returns a map of `ChannelType`-to-number indicating how many concurrent contacts can an Connect Customer agent workspace agent have on a given channel. 0 represents a disabled channel.

```
async getChannelConcurrency(): Promise<AgentChannelConcurrencyMap>         
```

 **Permissions required:** 

```
User.Configuration.View              
```