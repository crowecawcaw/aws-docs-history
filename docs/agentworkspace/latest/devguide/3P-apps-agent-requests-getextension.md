# Get the extension of the agent in Connect Customer Customer agent workspace

Returns phone number of the agent currently logged in to the Connect Customer Customer agent workspace. This is
the phone number that is dialed by the Connect Customer to connect calls to the agent for incoming
and outgoing calls if soft phone is not enabled.

```

async getExtension(): Promise<string | null>

```

**Permissions required:**

```

User.Configuration.View

```
