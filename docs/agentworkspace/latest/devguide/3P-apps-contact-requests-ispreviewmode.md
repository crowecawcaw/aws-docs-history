

# Check if contact is in preview mode in Connect Customer agent workspace
<a name="3P-apps-contact-requests-ispreviewmode"></a>

Returns whether the contact is being previewed. During this time, calling engagePreviewContact will trigger the outbound dial to the end customer and end preview mode.

 **Signature** 

```
isPreviewMode(contactId: string): Promise<boolean>                
```

 **Usage** 

```
const isPreviewMode = await contactClient.isPreviewMode(currentContactId);   
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
|  contactId Required  |  string  |  The id of the contact.  | 

 **Permissions required:** 

```
*
```