

# Subscribe a callback function when an Connect Customer agent workspace contact turns to Error state
<a name="3P-apps-contact-events-error-sub"></a>

Subscribes a callback function to-be-invoked whenever a contact turns to Error state in the Connect Customer agent workspace. If no contact ID is provided, then it uses the context of the current contact that the 3P app was opened on.

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