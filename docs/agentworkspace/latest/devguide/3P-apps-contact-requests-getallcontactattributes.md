

# Get all attributes of a contact in Connect Customer agent workspace
<a name="3P-apps-contact-requests-getallcontactattributes"></a>

Returns every attribute of the contact as a map of attribute key to value. The map includes attributes that have no value, with an empty string as the value.

 **Signature** 

```
getAllContactAttributes(contactId: string): Promise<Record<string, string>>
```

 **Usage** 

```
const attributes = await contactClient.getAllContactAttributes(contactId);
// { "accountId": "12345", "priority": "" }
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| contactId Required | string | The unique identifier for the contact | 

 **Contact scope:** 

Requires an instance that is scoped to the contact that you pass in `contactId`, or an instance without a contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```
*
```