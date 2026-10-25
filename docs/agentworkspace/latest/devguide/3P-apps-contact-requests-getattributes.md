

# Get the attributes of a contact in Connect Customer agent workspace
<a name="3P-apps-contact-requests-getattributes"></a>

Returns a map of the attributes associated with the contact in the Connect Customer agent workspace. Each value in the map has the following shape: `{ name: string, value: string }`.

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

 **Contact scope:** 

Requires an instance that is scoped to the contact that you pass in `contactId`, or an instance without a contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```
Contact.Attributes.View              
```