# Get the duration of the contact state in Amazon Connect Customer agent workspace

Returns the duration of the contact state in milliseconds relative to local time,
in the Amazon Connect Customer agent workspace. This takes into account time skew between the JS client and the
Amazon Connect backend servers.

```

async getStateDuration(contactId: string): Promise<number>

```

**Permissions required:**

```

Contact.Details.View

```
