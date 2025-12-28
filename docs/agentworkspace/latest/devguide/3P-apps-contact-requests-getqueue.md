# Get the queue of the contact in

Amazon Connect Agent Workspace

Returns the queue associated with the contact in the Amazon Connect agent workspace. The `Queue`
object has the following fields:

- `name`: The name of the queue.
- `queueARN`: The ARN of the queue.
- `queueId`: Alias for `queueARN`.

```

async getQueue(contactId: string): Promise<Queue>

```

**Permissions required:**

```

Contact.Details.View

```
