

# Check if the current user is on hold in Connect Customer agent workspace
<a name="3P-apps-voice-requests-isselfonhold"></a>

Checks whether the current user's participant is currently on hold for a specific contact.

 **Signature** 

```
isSelfOnHold(contactId: string): Promise<boolean>
```

 **Usage** 

```
const isOnHold = await voiceClient.isSelfOnHold("contact-123");
if (isOnHold) {
  console.log("You are on hold");
}
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| contactId Required | string | The unique identifier for the contact | 

 **Output** 

Returns a Promise that resolves to a boolean: true if the current user is on hold, false otherwise

 **Contact scope:** 

Requires an instance that is scoped to the contact that you pass in `contactId`, or an instance without a contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```
*
```