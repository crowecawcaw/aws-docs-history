

# Resume the current user from hold in Connect Customer agent workspace
<a name="3P-apps-voice-requests-resumeself"></a>

Resumes the current user's participant from hold for a specific contact.

 **Signature** 

```
resumeSelf(contactId: string): Promise<void>
```

 **Usage** 

```
const canResume = await voiceClient.canResumeSelf("contact-123");
if (canResume) {
  await voiceClient.resumeSelf("contact-123");
}
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