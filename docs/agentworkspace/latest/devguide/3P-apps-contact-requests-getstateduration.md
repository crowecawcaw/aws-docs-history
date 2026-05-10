# Get the duration of the contact state in Connect Customer Customer agent workspace

Returns the duration of the contact state in milliseconds relative to local time,
in the Connect Customer Customer agent workspace. This takes into account time skew between the JS client and the
Connect Customer backend servers.

```

async getStateDuration(contactId: string): Promise<number>

```

**Permissions required:**

```

Contact.Details.View

```
