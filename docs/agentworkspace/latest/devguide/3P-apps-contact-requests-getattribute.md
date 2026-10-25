

# Get specific attributes for a contact in Connect Customer agent workspace
<a name="3P-apps-contact-requests-getattribute"></a>

Returns the requested attribute associated with the contact in the Connect Customer agent workspace.

```
async getAttribute(
  contactId: string,
  attribute: string,
): Promise<string | undefined>
```

 **Contact scope:** 

Requires an instance that is scoped to the contact that you pass in `contactId`, or an instance without a contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```
Contact.Attributes.View              
```