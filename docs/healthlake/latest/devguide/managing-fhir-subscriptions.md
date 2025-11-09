# Managing FHIR Subscriptions in AWS HealthLake

AWS HealthLake supports FHIR Subscriptions, allowing you to receive real-time
notifications when specific healthcare data changes occur. This capability implements the
FHIR R5 Backport topic-based subscription model, providing improved scalability
and flexibility over the traditional FHIR R4 subscription model.

With FHIR Subscriptions, you can build event-driven healthcare applications
that respond immediately to changes in clinical data, enabling timely interventions, automated
workflows, and enhanced care coordination.

###### Topics

- [How FHIR Subscriptions work](#managing-fhir-subs-how-subs-work "#managing-fhir-subs-how-subs-work")
- [Key components](#managing-fhir-subs-components "#managing-fhir-subs-components")
- [Best practices](#managing-fhir-subs-best-practices "#managing-fhir-subs-best-practices")
- [Subscription lifecycle](managing-fhir-subscriptions-lifecycle.md "managing-fhir-subscriptions-lifecycle.md")
- [Creating a Subscription](managing-fhir-subscriptions-create.md "managing-fhir-subscriptions-create.md")
- [Searching for Subscriptions](managing-fhir-subscriptions-searching.md "managing-fhir-subscriptions-searching.md")
- [Filtering notifications](managing-fhir-subscriptions-filter-notif.md "managing-fhir-subscriptions-filter-notif.md")

## How FHIR Subscriptions work

FHIR Subscriptions in HealthLake operate on a topic-based model where:

1. **Create topics to define events**: Create Subscription
   Topics that specify events that can trigger notifications
2. **You subscribe**: Create Subscriptions to these topics
   with specific filtering criteria
3. **HealthLake monitors**: The service continuously monitors
   for events matching your criteria
4. **Notifications delivered**: CWhen matching events occur,
   HealthLake delivers notifications through your chosen channel

## Key components

FHIR Subscriptions consist of the following components.

### Subscription Topics

Subscription Topics are the foundation of the notification system and define:

- **Trigger events**: What changes trigger notifications
  (For example: Resource creation, updates, deletes)
- **Available filters**: What filtering options are
  available to subscribers
- **Notification content**: What data is included in
  notifications

The following table lists the common topic types.

| Event type        | Description                           | Common use cases                                   |
| ----------------- | ------------------------------------- | -------------------------------------------------- |
| Resource creation | Triggered when resources are created  | New patient registration, new observation recorded |
| Resource updates  | Triggered when resources are modified | Status changes, clinical updates                   |
| Resource deletion | Triggered when resources are deleted  | Audit and compliance tracking                      |

### Subscriptions

A Subscription is your request to receive notifications for specific events defined by a
Subscription Topic. Each subscription includes:

- **Topic reference**: Specifies which Subscription Topic
  you are subscribing to

- **Filters**: Criteria to select which events generate
  notifications

- **Channel configuration**: Where and how notifications
  should be delivered

- **Payload preferences**: What level of detail should be
  included in notifications

### Notification channels

HealthLake supports the following notification channels:

| Channel type | Use cases                                                                      |
| ------------ | ------------------------------------------------------------------------------ |
| EventBridge  | Enterprise integrations, serverless workflows, cross-AWS service orchestration |
| REST Hook    | Direct endpoint notifications, third-party system integration                  |

### Notification payloads

Choose the appropriate payload type based on your needs:

| Payload type  | Description                                                                                                                    | Security considerations              |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------ |
| ID-only       | Contains only resource identifiers                                                                                             | Minimal PHI exposure                 |
| Full-resource | Contains complete resource content with a max size of 256 KB. If the size is<br>greater than 256KB, it will go back to ID-only | Contains PHI; Verify secure handling |

## Best practices

Performance optimization

- **Use focused filters**: Narrow your criteria to receive only essential notifications
- **Choose appropriate payload types**: Use ID-only payloads when possible for better performance
- **Implement efficient receivers**: Ensure notification receivers process messages quickly

Security considerations

- **Secure endpoints**: Implement proper authentication for REST Hook endpoints
- **PHI protection**: Be cautious with full-resource payloads as they contain PHI
- **Access control**: Restrict Subscription creation to authorized users only

Operational excellence

- **Set appropriate end dates**: Use end dates for temporary Subscriptions
- **Monitor Subscription status**: Regularly check the status of your Subscriptions
- **Implement error handling**: Design your applications to handle notification delivery failures
