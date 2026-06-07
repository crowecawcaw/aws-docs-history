# Clears the contact for the given contactId in Connect Customer agent workspace

Clears the contact for the given contactId.

**Signature**

```

clear(contactId: string): Promise<void>

```

**Usage**

```

await contactClient.clear(contactId);

```

**Input**

| **Parameter**        | **Type** | **Description**                                 |
| -------------------- | -------- | ----------------------------------------------- |
| contactId _Required_ | string   | The id of the contact that needs to be cleared. |

**Permissions required:**

```
Contact.Details.Edit

```
