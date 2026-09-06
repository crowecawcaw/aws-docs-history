

# Unsubscribe from self hold events in Connect Customer agent workspace
<a name="3P-apps-voice-requests-offselfhold"></a>

Unsubscribes from self hold events.

 **Signature** 

```
offSelfHold(
  handler: ParticipantHoldHandler,
  contactId?: string
): void
```

 **Usage** 

```
voiceClient.offSelfHold(handleSelfHold);
```

 **Input** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
| handler Required | ParticipantHoldHandler | Event handler function to remove | 
| contactId | string | Optional contact ID to unsubscribe from specific contact events | 