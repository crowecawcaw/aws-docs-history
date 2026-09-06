

# Subscribe a callback function when an Connect Customer agent workspace contact starts ACW
<a name="3P-apps-contact-events-startingacw-sub"></a>

Subscribes a callback function to-be-invoked whenever a contact StartingAcw event occurs in the Connect Customer agent workspace. If no contact ID is provided, then it uses the context of the current contact that the 3P app was opened on.

 **Signature** 

```
onStartingAcw(handler: ContactStartingAcwHandler, contactId?: string)
```

 **Usage** 

```
const handler: ContactStartingAcwHandler = async (data: ContactStartingAcw) => {
    console.log("Contact StartingAcw occurred! " + data);
};

contactClient.onStartingAcw(handler);

// ContactStartingAcw Structure
{
  contactId: string;
}
```

 **Permissions required:** 

```
Contact.Details.View               
```