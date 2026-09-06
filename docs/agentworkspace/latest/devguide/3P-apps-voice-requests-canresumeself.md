

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