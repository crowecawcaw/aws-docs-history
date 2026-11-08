

# Subscribe a callback function when an Connect Customer agent workspace contact turns to Error state
<a name="3P-apps-contact-events-error-sub"></a>

Subscribes a callback function to-be-invoked whenever a contact turns to Error state in the Connect Customer agent workspace. If you omit `contactId`, the handler receives the event for every contact that the instance is allowed to see: only its own contact for a contact-scoped instance, and all of the agent's contacts for an instance with no scope value. An instance with the `idle` scope receives none.

 **Signature** 

```
onError(handler: ContactErrorHandler, contactId?: string)
```

 **Usage** 

```
const handler: ContactErrorHandler = async (data: ContactError) => {
    console.log("Contact Error occurred! " + data.contactId);
};

contactClient.onError(handler);

// ContactError Structure
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