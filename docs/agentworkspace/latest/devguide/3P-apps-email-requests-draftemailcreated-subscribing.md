

# Subscribe to draft email creation notifications in Connect Customer agent workspace
<a name="3P-apps-email-requests-draftemailcreated-subscribing"></a>

Subscribes a callback function to-be-invoked whenever a draft email contact has been created.

 **Signature** 

```
onDraftEmailCreated(handler: SubscriptionHandler<EmailContactId>, contactId?: string): void
```

 **Usage** 

```
const handler: SubscriptionHandler<EmailContactId> = async (emailContact: EmailContactId) => {
   const { contactId } = emailContact;
   console.log(`Draft Email Contact Created with Id: ${contactId}`);
}

emailClient.onDraftEmailCreated(handler);

// EmailContactId Structure
{
   contactId: string;
}
```