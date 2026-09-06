

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

 **Permissions required:** 

```
Contact.Details.Edit
```