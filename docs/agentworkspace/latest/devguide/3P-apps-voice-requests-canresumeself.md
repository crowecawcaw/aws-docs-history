# Check if the current user can be

resumed from hold in Amazon Connect Agent Workspace

Checks whether the current user's participant can be resumed from hold for a specific
contact.

**Signature**

```
canResumeSelf(contactId: string): Promise<boolean>
```

**Usage**

```
const canResume = await voiceClient.canResumeSelf("contact-123");
if (canResume) {
  // Resume logic here
}
```

**Input**

| **Parameter**        | **Type** | **Description**                       |
| -------------------- | -------- | ------------------------------------- |
| contactId _Required_ | string   | The unique identifier for the contact |

**Output**

Returns a Promise that resolves to a boolean: true if the current user can be resumed,
false otherwise
