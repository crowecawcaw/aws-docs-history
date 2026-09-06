

# Subscribe a callback function when an Connect Customer agent workspace contact turns to Connecting state
<a name="3P-apps-contact-events-connecting-sub"></a>

Subscribes a callback function to-be-invoked whenever a contact turns to Connecting state in the Connect Customer agent workspace. The Connecting state means the contact is being routed to the agent and has not yet been fully assigned. If no contact ID is provided, then it uses the context of the current contact that the 3P app was opened on.

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