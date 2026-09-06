

# Subscribe a callback function when an Connect Customer agent workspace contact is missed
<a name="3P-apps-contact-events-missed-sub"></a>

Subscribes a callback function to-be-invoked whenever a contact missed event occurs in the Connect Customer agent workspace. If no contact ID is provided, then it uses the context of the current contact that the 3P app was opened on.

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
}
```

 **Permissions required:** 

```
Contact.Details.View               
```