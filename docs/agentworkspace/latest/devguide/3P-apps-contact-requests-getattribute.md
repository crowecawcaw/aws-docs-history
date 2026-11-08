

# Get a specific attribute of a contact in Connect Customer agent workspace - Deprecated
<a name="3P-apps-contact-requests-getattribute"></a>

**Note**  
This operation is deprecated. Use [getContactAttribute()](3P-apps-contact-requests-getcontactattribute.md) instead, which returns the attribute value as a string.

Returns the requested attribute of the contact as an `AttributeDetail` object, or `undefined` if the contact does not have the attribute. To get the attribute value, read the `value` property of the object. The `value` property is undefined if the attribute has no value set.

```
async getAttribute(
  contactId: string,
  attribute: string,
): Promise<AttributeDetail | undefined>

interface AttributeDetail {
  name: string;
  value?: string;
}
```

 **Contact scope:** 

Requires an instance that is scoped to the contact that you pass in `contactId`, or an instance without a contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```
Contact.Attributes.View
```