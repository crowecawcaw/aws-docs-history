

# List all contacts for the current agent in Connect Customer agent workspace
<a name="3P-apps-contact-requests-listcontacts"></a>

Lists all contacts for the current agent.

 **Signature** 

```
listContacts(): Promise<ListContactsResult>
```

 **Usage** 

```
const contacts = await contactClient.listContacts();
console.log(`Active contacts: ${contacts.length}`);
contacts.forEach((contact) => {
    console.log(`Contact ${contact.contactId}: ${contact.type}`);
});
```

 **Output - ListContactsResult** 

Returns an array of contact data objects (currently typed as CoreContactData[]).

 **Contact scope:** 

You can call this operation only from an application instance that is running without a contact scope, such as a cross-contact application that is launched at the top level. The request fails authorization if the instance is scoped to a contact or to `idle`, including a cross-contact application that inherited a scope from the application that launched it.

 **Permissions required:** 

```
*
```