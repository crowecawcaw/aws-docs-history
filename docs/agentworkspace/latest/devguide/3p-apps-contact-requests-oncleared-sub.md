# Creates a subscription

whenever a contact cleared event occurs in Amazon Connect Agent Workspace

It creates a subscription whenever a contact cleared event occurs in Amazon Connect Agent Workspace. If no contact ID is provided, then it uses the
context of the current contact that the 3P app was opened on.

**Signature**

```

onCleared(handler: ContactClearedHandler, contactId?: string)

```

**Usage**

```

const handler: ContactClearedHandler = async (data: ContactCleared) => {
    console.log("Contact cleared occurred! " + data);
};

contactClient.onCleared(handler);

// ContactCleared Structure
{
    contactId: string;
}

```

**Permissions required:**

```
Contact.Details.View

```
