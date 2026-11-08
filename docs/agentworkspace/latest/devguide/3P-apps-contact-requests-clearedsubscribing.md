

# Creates a subscription whenever a contact cleared event occurs in Connect Customer agent workspace
<a name="3P-apps-contact-requests-clearedsubscribing"></a>

 It creates a subscription whenever a contact cleared event occurs in Connect Customer agent workspace. If you omit `contactId`, the handler receives the event for every contact that the instance is allowed to see: only its own contact for a contact-scoped instance, and all of the agent's contacts for an instance with no scope value. An instance with the `idle` scope receives none.

 **Signature** 

 onCleared(handler: ContactClearedHandler, contactId?: string) 

 **Usage** 

```
const handler: ContactClearedHandler = async (data: ContactCleared) => {
    console.log("Contact cleared occurred! " + data);
};

contactClient.onCleared(handler);

// ContactCleared Structure
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