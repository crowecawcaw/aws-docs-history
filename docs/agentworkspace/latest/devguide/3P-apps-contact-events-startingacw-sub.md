

# Subscribe a callback function when an Connect Customer agent workspace contact starts ACW

Subscribes a callback function to-be-invoked whenever a contact StartingAcw event occurs in the Connect Customer agent workspace. If you omit `contactId`, the handler receives the event for every contact that the instance is allowed to see: only its own contact for a contact-scoped instance, and all of the agent's contacts for an instance with no scope value. An instance with the `idle` scope receives none.

 **Signature** 

```typescript
onStartingAcw(handler: ContactStartingAcwHandler, contactId?: string)
```

 **Usage** 

```typescript
const handler: ContactStartingAcwHandler = async (data: ContactStartingAcw) => {
    console.log("Contact StartingAcw occurred! " + data);
};

contactClient.onStartingAcw(handler);

// ContactStartingAcw Structure
{
    contactId: string;
    initialContactId: string | undefined;
    type: ContactChannelType["type"];
    subtype: ContactChannelType["subtype"];
}
```

 **Permissions required:** 

```typescript
Contact.Details.View               
```