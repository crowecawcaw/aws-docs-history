

# Subscribe to self hold events in Connect Customer agent workspace
<a name="3P-apps-voice-requests-onselfhold"></a>

Subscribes to events when the current user's participant is put on hold.

 **Signature** 

```
onSelfHold(
  handler: ParticipantHoldHandler,
  contactId?: string
): void
```

 **Usage** 

```
const handleSelfHold = (event) => {
  console.log("You have been put on hold");
  console.log(`Contact: ${event.contactId}`);
};
// Subscribe to all contacts
voiceClient.onSelfHold(handleSelfHold);
// Or subscribe to a specific contact
voiceClient.onSelfHold(handleSelfHold, "contact-123");
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| handler Required | ParticipantHoldHandler | Event handler function to call when the current user's participant is put on hold | 
| contactId | string | Optional contact ID to filter events for a specific contact | 