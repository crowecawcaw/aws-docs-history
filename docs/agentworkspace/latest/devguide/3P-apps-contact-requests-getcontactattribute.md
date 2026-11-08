

# Get a specific attribute value of a contact in Connect Customer agent workspace
<a name="3P-apps-contact-requests-getcontactattribute"></a>

Returns the value of the requested attribute of the contact as a string. If the contact has the attribute but no value is set, the operation returns an empty string. If the contact does not have the attribute, the operation returns `undefined`.

 **Signature** 

```
async getContactAttribute(
  contactId: string,
  attribute: ContactAttributeKey,
): Promise<string | undefined>

type ContactAttributeKey = string;
```

 **Usage** 

```
const accountId = await contactClient.getContactAttribute(contactId, "accountId");
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| contactId Required | string | The unique identifier for the contact | 
| attribute Required | ContactAttributeKey | The key of the attribute to retrieve | 

 **Contact scope:** 

Requires an instance that is scoped to the contact that you pass in `contactId`, or an instance without a contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```
*
```