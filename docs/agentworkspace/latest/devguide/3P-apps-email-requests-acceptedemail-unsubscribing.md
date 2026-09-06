

# Unsubscribe from accepted email notifications in Connect Customer agent workspace
<a name="3P-apps-email-requests-acceptedemail-unsubscribing"></a>

Unsubscribes a callback function from the event that is fired when an inbound email contact is accepted.

 **Signature** 

```
offAcceptedEmail(handler: SubscriptionHandler<EmailContactId>, contactId?: string): void
```

 **Usage** 

```
emailClient.offAcceptedEmail(handler);
```