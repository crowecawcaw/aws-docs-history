# Reject the incoming contact for the given contactId in Connect Customer agent workspace

Reject the incoming contact for the given contactId. The contact will not be
connected to the agent and will be routed back to the queue.

**Signature**

```

reject(contactId: string): Promise<void>

```

**Usage**

```

await contactClient.reject(contactId);

```

**Input**

| **Parameter**        | **Type** | **Description**                           |
| -------------------- | -------- | ----------------------------------------- |
| contactId _Required_ | string   | The id of the incoming contact to reject. |

**Permissions required:**

```
*
```
