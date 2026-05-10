# Get the timestamp of the contact in Connect Customer Customer agent workspace

Returns a `Date` object with the timestamp associated with when the contact
was placed in the queue in the Connect Customer Customer agent workspace.

```

async getQueueTimestamp(contactId: string): Promise<Date | undefined>

```

**Permissions required:**

```

Contact.Details.View

```
