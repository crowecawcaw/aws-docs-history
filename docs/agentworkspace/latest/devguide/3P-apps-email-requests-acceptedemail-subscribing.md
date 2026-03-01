# Subscribe to accepted email notifications in Amazon Connect Agent Workspace

Subscribes a callback function to-be-invoked whenever an inbound email contact has
been accepted.

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
