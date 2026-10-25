

# Clears the contact for the given contactId in Connect Customer agent workspace
<a name="3P-apps-contact-requests-clear"></a>

Clears the contact for the given contactId.

 **Signature** 

```
clear(contactId: string): Promise<void>                
```

 **Usage** 

```
await contactClient.clear(contactId);   
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
|  contactId Required  |  string  |  The id of the contact that needs to be cleared.  | 

 **Contact scope:** 

Requires an instance that is scoped to the contact that you pass in `contactId`, or an instance without a contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```
Contact.Details.Edit              
```