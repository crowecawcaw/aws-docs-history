# Get the queue of the contact in Connect Customer agent workspace

Returns the queue associated with the contact in the Connect Customer agent workspace. The `Queue`
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
