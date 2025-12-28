# Get the routing profile

of the agent in Amazon Connect Agent Workspace

Returns the routing profile of the agent currently logged in to the Amazon Connect agent workspace.
The routing profile contains the following fields:

- `channelConcurrencyMap`: See agent.[Get the limit of
  contacts for the agent in Amazon Connect Agent Workspace](3P-apps-agent-requests-getchannelconcurrency.md "3P-apps-agent-requests-getchannelconcurrency.md") for more
  info.
- `defaultOutboundQueue`: The default queue which should be
  associated with outbound contacts. See queues for details on properties.
- `name`: The name of the routing profile.
- `queues`: The queues contained in the routing profile. Each queue
  object has the following properties:
  - `name`: The name of the queue.
  - `queueARN`: The ARN of the queue.
  - `queueId`: Alias for queueARN.

- `routingProfileARN`: The routing profile ARN.
- `routingProfileId`: Alias for `routingProfileARN`.

```

async getRoutingProfile(): Promise<AgentRoutingProfile>

```

**Permissions required:**

```

User.Configuration.View

```
