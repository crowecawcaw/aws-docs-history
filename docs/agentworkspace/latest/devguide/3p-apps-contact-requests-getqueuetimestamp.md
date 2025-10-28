# Get the timestamp of

the contact in Amazon Connect Agent Workspace

Returns a `Date` object with the timestamp associated with when the
contact was placed in the queue in Amazon Connect Agent Workspace.

```

async getQueueTimestamp(contactId: string): Promise<Date | undefined>

```

**Permissions required:**

```

Contact.Details.View

```
