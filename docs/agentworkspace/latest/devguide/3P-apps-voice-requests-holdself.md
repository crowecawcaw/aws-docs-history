

# Place the current user on hold in Connect Customer agent workspace
<a name="3P-apps-voice-requests-holdself"></a>

Places the current user's participant on hold for a specific contact.

 **Signature** 

```
holdSelf(contactId: string): Promise<void>
```

 **Usage** 

```
await voiceClient.holdSelf("contact-123");
console.log("You are now on hold");
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