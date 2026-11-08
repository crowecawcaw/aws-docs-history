

# Get the attributes of a contact in Connect Customer agent workspace - Deprecated
<a name="3P-apps-contact-requests-getattributes"></a>

**Note**  
This operation is deprecated. To get specific attributes, use [getContactAttributes()](3P-apps-contact-requests-getcontactattributes.md). To get every attribute, use [getAllContactAttributes()](3P-apps-contact-requests-getallcontactattributes.md) instead of the `"*"` filter. Both operations return attribute values as strings.

Returns a map of the requested attributes of the contact, or of every attribute if you pass `"*"`. Each value in the map is an `AttributeDetail` object rather than a string. To get an attribute value, read the `value` property of the object.

```
// example { "foo": { "name": "foo", "value": "bar" } }
```

```
getAttributes(
  contactId: string,
  attributes: ContactAttributeFilter,
): Promise<Record<string, AttributeDetail>>
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