

# Get the type of contact in Connect Customer agent workspace
<a name="3P-apps-contact-requests-getchanneltype"></a>

 Get the type of the contact in Connect Customer agent workspace. This indicates what type of media is carried over the connections of the contact. 

 **Signature** 

```
 getChannelType(contactId: string): Promise<ContactChannelType>                 
```

 **Usage** 

```
const contactType: ContactChannelType = await contactClient.getChannelType(contactId);   
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
|  contactId Required  |  string  |  The id of the contact.  | 

 **Output - ContactChannelType** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
|  type  |  string  |  The possible values are voice, queue\_callback, chat, task, email  | 
|  subtype  |  string  | For the types `voice` & `queue_callback`, it will be `connect:Telephony` \| `connect:WebRTC` .<br />For the type `chat`, it will be `connect:Chat` \| `connect:SMS` \| `connect:Apple` \| ` connect:Guide`.<br />For the type `task`, it will be `connect:Task` .<br />For the type `email`, it will be `connect:Email` . | 

 **Contact scope:** 

Requires an instance that is scoped to the contact that you pass in `contactId`, or an instance without a contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```
Contact.Details.View              
```