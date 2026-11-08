

# Subscribe a callback function when an Connect Customer agent workspace contact is missed
<a name="3P-apps-contact-events-missed-sub"></a>

Subscribes a callback function to-be-invoked whenever a contact missed event occurs in the Connect Customer agent workspace. If you omit `contactId`, the handler receives the event for every contact that the instance is allowed to see: only its own contact for a contact-scoped instance, and all of the agent's contacts for an instance with no scope value. An instance with the `idle` scope receives none.

 **Signature** 

```
onMissed(handler: ContactMissedHandler, contactId?: string)
```

 **Usage** 

```
const handler: ContactMissedHandler = async (data: ContactMissed) => {
    console.log("Contact missed occurred! " + data);
};

contactClient.onMissed(handler);

// ContactMissed Structure
{
    contactId: string;
    initialContactId: string | undefined;
    type: ContactChannelType["type"];
    subtype: ContactChannelType["subtype"];
}
```

 **Permissions required:** 

```
Contact.Details.View               
```