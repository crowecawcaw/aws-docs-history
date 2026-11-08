

# Subscribe a callback function when an Connect Customer agent workspace contact turns to Connecting state
<a name="3P-apps-contact-events-connecting-sub"></a>

Subscribes a callback function to-be-invoked whenever a contact turns to Connecting state in the Connect Customer agent workspace. The Connecting state means the contact is being routed to the agent and has not yet been fully assigned. If you omit `contactId`, the handler receives the event for every contact that the instance is allowed to see: only its own contact for a contact-scoped instance, and all of the agent's contacts for an instance with no scope value. An instance with the `idle` scope receives none.

 **Signature** 

```
onConnecting(handler: ContactConnectingHandler, contactId?: string)
```

 **Usage** 

```
const handler: ContactConnectingHandler = async (data: ContactConnecting) => {
    console.log("Contact Connecting occurred! " + data.contactId);
};

contactClient.onConnecting(handler);

// ContactConnecting Structure
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