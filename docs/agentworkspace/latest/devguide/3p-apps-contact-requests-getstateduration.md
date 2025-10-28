# Get the duration of the

contact state in Amazon Connect Agent Workspace

Returns the duration of the contact state in milliseconds relative to local time,
in Amazon Connect Agent Workspace. This takes into account time skew between the JS client and the
Amazon Connect backend servers.

```

async getStateDuration(contactId: string): Promise<number>

```

**Permissions required:**

```

Contact.Details.View

```
