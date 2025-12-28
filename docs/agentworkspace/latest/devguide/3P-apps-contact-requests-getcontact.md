# Get detailed contact information

in
Amazon Connect Agent Workspace

Retrieves detailed information for a specific contact by its ID.

**Signature**

```

getContact(contactId: string): Promise<ContactData>

```

**Usage**

```

const contactData = await contactClient.getContact("contact-123");
console.log(`Contact type: ${contactData.type}`);
console.log(`Queue: ${contactData.queue.name}`);

```

**Input**

| **Parameter**        | **Type** | **Description**                       |
| -------------------- | -------- | ------------------------------------- |
| contactId _Required_ | string   | The unique identifier for the contact |

**Output - ContactData**

The ContactData interface includes:

- `contactId`: string - Unique identifier for the contact
- `type`: ContactType - Type of contact (voice, chat, task)
- `subtype`: string - Subtype providing additional classification
- `initialContactId`?: string - Initial contact ID for transferred
  contacts
- `queue`: Queue - Queue information

**Permissions required:**

```

*

```
