

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

 **Permissions required:** 

```
*
```