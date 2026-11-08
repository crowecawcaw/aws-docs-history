

# Check if the current user can be resumed from hold in Connect Customer agent workspace
<a name="3P-apps-voice-requests-canresumeself"></a>

Checks whether the current user's participant can be resumed from hold for a specific contact.

 **Signature** 

```
canResumeSelf(contactId: string): Promise<boolean>
```

 **Usage** 

```
const canResume = await voiceClient.canResumeSelf("contact-123");
if (canResume) {
  // Resume logic here
}
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| contactId Required | string | The unique identifier for the contact | 

 **Output** 

Returns a Promise that resolves to a boolean: true if the current user can be resumed, false otherwise

 **Contact scope:** 

Requires an instance that is scoped to the contact that you pass in `contactId`, or an instance without a contact scope. For details, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

 **Permissions required:** 

```
*
```