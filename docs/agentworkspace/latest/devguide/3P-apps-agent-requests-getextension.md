# Get the extension of the agent

in Amazon Connect Agent Workspace

Returns phone number of the agent currently logged in to the Amazon Connect agent workspace. This is
the phone number that is dialed by the Amazon Connect to connect calls to the agent for incoming
and outgoing calls if soft phone is not enabled.

```

async getExtension(): Promise<string | null>

```

**Permissions required:**

```

User.Configuration.View

```
