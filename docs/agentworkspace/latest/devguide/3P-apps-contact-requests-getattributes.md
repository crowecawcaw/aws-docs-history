# Get the attributes of a contact in Connect Customer Customer agent workspace

Returns a map of the attributes associated with the contact in the Connect Customer Customer agent workspace. Each
value in the map has the following shape: `{ name: string, value: string
 }`.

```

// example { "foo": { "name": "foo", "value": "bar" } }

```

```

getAttributes(
  contactId: string,
  attributes: ContactAttributeFilter,
): Promise<Record<string, string>>

```

```

ContactAttributeFilter is either string[] of attributes or '*'

```

**Permissions required:**

```

Contact.Attributes.View

```
