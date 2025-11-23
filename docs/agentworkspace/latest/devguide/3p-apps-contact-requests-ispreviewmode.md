# Check if contact is in

preview mode in Amazon Connect Agent Workspace

Returns whether the contact is being previewed. During this time, calling
engagePreviewContact will trigger the outbound dial to the end customer and end
preview mode.

**Signature**

```

isPreviewMode(contactId: string): Promise<boolean>

```

**Usage**

```

const isPreviewMode = await contactClient.isPreviewMode(currentContactId);

```

**Input**

| **Parameter**        | **Type** | **Description**        |
| -------------------- | -------- | ---------------------- |
| contactId _Required_ | string   | The id of the contact. |
