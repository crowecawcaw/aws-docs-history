

# Subscribe a callback function when an Connect Customer agent workspace contact turns to Pending state
<a name="3P-apps-contact-events-pending-sub"></a>

Subscribes a callback function to-be-invoked whenever a contact turns to Pending state in the Connect Customer agent workspace. For Queued Callback contacts, the Pending state is transient and requires no action from the agent. For preview contacts, the agent must call [engagePreviewContact()](3P-apps-contact-requests-engagepreviewcontact.md) to proceed to the Connecting state, or [disconnectSelf()](3P-apps-contact-requests-disconnectself.md) to decline it. If you omit `contactId`, the handler receives the event for every contact that the instance is allowed to see: only its own contact for a contact-scoped instance, and all of the agent's contacts for an instance with no scope value. An instance with the `idle` scope receives none.

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