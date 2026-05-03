# Unsubscribe from accepted email notifications in Amazon Connect Customer agent workspace

Unsubscribes a callback function from the event that is fired when an inbound
email contact is accepted.

**Signature**

```
offAcceptedEmail(handler: SubscriptionHandler<EmailContactId>, contactId?: string): void
```

**Usage**

```
emailClient.offAcceptedEmail(handler);
```
