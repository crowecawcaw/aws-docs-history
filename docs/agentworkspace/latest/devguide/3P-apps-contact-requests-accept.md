

# Accept the incoming contact for the given contactId in Connect Customer agent workspace
<a name="3P-apps-contact-requests-accept"></a>

Accept the incoming contact for the given contactId.

 **Signature** 

```
accept(contactId: string): Promise<void>                
```

 **Usage** 

```
await contactClient.accept(contactId);   
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
|  contactId Required  |  string  |  The id of the contact that needs to be accepted.  | 

 **Contact scope:** 

Requires an instance that is scoped to the contact that you pass in `contactId`, or an instance without a contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```
Contact.Details.Edit
```