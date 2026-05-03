# Get specific attributes for a contact in Amazon Connect Customer agent workspace

Returns the requested attribute associated with the contact in the Amazon Connect
Customer agent workspace.

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
