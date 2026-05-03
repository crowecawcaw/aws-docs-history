# Get the limit of contacts for the agent in Amazon Connect Customer agent workspace

Returns a map of `ChannelType`-to-number indicating how many concurrent
contacts can an Amazon Connect Customer agent workspace agent have on a given channel. 0 represents a disabled
channel.

```

async getChannelConcurrency(): Promise<AgentChannelConcurrencyMap>

```

**Permissions required:**

```

User.Configuration.View

```
