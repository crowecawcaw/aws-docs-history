

# Unsubscribe from draft email creation notifications in Connect Customer agent workspace
<a name="3P-apps-email-requests-draftemailcreated-unsubscribing"></a>

Unsubscribes a callback function from the event that is fired when a draft email contact is created.

 **Signature** 

```
offDraftEmailCreated(handler: SubscriptionHandler<EmailContactId>, contactId?: string): void
```

 **Usage** 

```
emailClient.offDraftEmailCreated(handler);
```