# Clears the contact for the given

contactId in Amazon Connect Agent Workspace

Clears the contact for the given contactId.

**Signature**

```

clear(contactId: string): Promise<void>

```

**Usage**

```

await contactClient.clear(AppContactScope.CurrentContactId);

```

**Input**

| **Parameter**        | **Type** | **Description**                                                                                                                          |
| -------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| contactId _Required_ | string   | The id of the contact to which a participant needs to be added. Use `AppContactScope.CurrentContactId` to represent the current contact. | **Permissions required:** `Contact.Details.Edit` |
