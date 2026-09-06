

# Get specific attributes for a contact in Connect Customer agent workspace
<a name="3P-apps-contact-requests-getattribute"></a>

Returns the requested attribute associated with the contact in the Connect Customer agent workspace.

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