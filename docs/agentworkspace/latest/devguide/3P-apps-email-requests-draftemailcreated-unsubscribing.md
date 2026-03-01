# Unsubscribe from draft email creation notifications in Amazon Connect Agent Workspace

Unsubscribes a callback function from the event that is fired when a draft email
contact is created.

**Signature**

```
offDraftEmailCreated(handler: SubscriptionHandler<EmailContactId>, contactId?: string): void
```

**Usage**

```
emailClient.offDraftEmailCreated(handler);
```
