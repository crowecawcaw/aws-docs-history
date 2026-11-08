

# Get specific attributes of a contact in Connect Customer agent workspace
<a name="3P-apps-contact-requests-getcontactattributes"></a>

Returns the requested attributes of the contact as a map of attribute key to value. The map contains only the requested attributes that the contact has. The map includes attributes that have no value, with an empty string as the value.

 **Signature** 

```
getContactAttributes(
  contactId: string,
  attributes: ContactAttributeKey[],
): Promise<Record<string, string>>

type ContactAttributeKey = string;
```

 **Usage** 

```
const attributes = await contactClient.getContactAttributes(contactId, [
  "accountId",
  "priority",
]);
// { "accountId": "12345", "priority": "" }
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| contactId Required | string | The unique identifier for the contact | 
| attributes Required | ContactAttributeKey[] | The keys of the attributes to retrieve | 

 **Contact scope:** 

Requires an instance that is scoped to the contact that you pass in `contactId`, or an instance without a contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```
*
```