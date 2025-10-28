# Get specific attributes for

a contact in Amazon Connect Agent Workspace

Returns the requested attribute associated with the contact in Amazon Connect
Agent Workspace.

```

async getAttribute(
  contactId: string,
  attribute: string,
): Promise<string | undefined>

```

**Permissions required:**

```

Contact.Attributes.View

```
