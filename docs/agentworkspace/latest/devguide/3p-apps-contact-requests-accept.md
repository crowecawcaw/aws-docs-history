# Accept the incoming contact for

the given contactId in Amazon Connect Agent Workspace

Accept the incoming contact for the given contactId.

**Signature**

```

accept(contactId: string): Promise<void>

```

**Usage**

```

await contactClient.accept(AppContactScope.CurrentContactId);

```

**Input**

| **Parameter**        | **Type** | **Description**                                                                                                                                |
| -------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| contactId _Required_ | string   | The id of the contact to which a participant needs to be added.<br>Use `AppContactScope.CurrentContactId` to represent<br>the current contact. |

**Permissions required:**

```
Contact.Details.Edit

```
