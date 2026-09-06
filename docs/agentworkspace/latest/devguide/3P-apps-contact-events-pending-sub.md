

# Subscribe a callback function when an Connect Customer agent workspace contact turns to Pending state
<a name="3P-apps-contact-events-pending-sub"></a>

Subscribes a callback function to-be-invoked whenever a contact turns to Pending state in the Connect Customer agent workspace. For Queued Callback contacts, the Pending state is transient and requires no action from the agent. For preview contacts, the agent must call [engagePreviewContact()](3P-apps-contact-requests-engagepreviewcontact.md) to proceed to the Connecting state, or [disconnectSelf()](3P-apps-contact-requests-disconnectself.md) to decline it. If no contact ID is provided, then it uses the context of the current contact that the 3P app was opened on.

 **Signature** 

```
onPending(handler: ContactPendingHandler, contactId?: string)
```

 **Usage** 

```
const handler: ContactPendingHandler = async (data: ContactPending) => {
    console.log("Contact Pending occurred! " + data.contactId);
};

contactClient.onPending(handler);

// ContactPending Structure
{
    contactId: string;
    initialContactId: string | undefined;
    type: string;
    subtype: string;
}
```

 **Permissions required:** 

```
*
```