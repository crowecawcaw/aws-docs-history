

# Subscribe a callback function when an Connect Customer agent workspace contact is connected
<a name="3P-apps-contact-events-connected-sub"></a>

Subscribes a callback function to-be-invoked whenever a contact Connected event occurs in the Connect Customer agent workspace. If no contact ID is provided, then it uses the context of the current contact that the 3P app was opened on.

 **Signature** 

```
onConnected(handler: ContactConnectedHandler, contactId?: string)
```

 **Usage** 

```
const handler: ContactConnectedHandler = async (data: ContactConnected) => {
    console.log("Contact Connected occurred! " + data);
};

contactClient.onConnected(handler);

// ContactConnected Structure
{
    contactId: string;
}
```

 **Permissions required:** 

```
Contact.Details.View               
```