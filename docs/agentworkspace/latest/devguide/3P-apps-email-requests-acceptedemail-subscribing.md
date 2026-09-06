

# Subscribe to accepted email notifications in Connect Customer agent workspace
<a name="3P-apps-email-requests-acceptedemail-subscribing"></a>

Subscribes a callback function to-be-invoked whenever an inbound email contact has been accepted.

 **Signature** 

```
onAcceptedEmail(handler: SubscriptionHandler<EmailContactId> contactId?: string): void
```

 **Usage** 

```
const handler: SubscriptionHandler<EmailContactId> = async (emailContact: EmailContactId) => {
   const { contactId } = emailContact;
   console.log(`Accepted Email Contact with Id: ${contactId}`);
}

emailClient.onAcceptedEmail(handler);

// EmailContactId Structure
{
   contactId: string;
}
```