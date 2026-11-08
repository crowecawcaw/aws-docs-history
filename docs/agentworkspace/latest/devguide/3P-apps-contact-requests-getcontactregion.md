

# Get the AWS Region of a contact in Connect Customer agent workspace
<a name="3P-apps-contact-requests-getcontactregion"></a>

Returns the AWS Region that the given contact is handled in, for example `us-east-1`.

 **Signature** 

```
getContactRegion(contactId: string): Promise<string>
```

 **Usage** 

```
const region: string = await contactClient.getContactRegion(contactId);
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