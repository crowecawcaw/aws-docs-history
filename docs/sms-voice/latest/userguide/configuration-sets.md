# Configuration sets in AWS End User Messaging SMS

A _configuration set_ is a set of rules that are applied when you send
a message. For example, a configuration set can specify a destination for events related to
a message. When SMS events occur (such as delivery or failure events), they are routed to
the destination associated with the configuration set that you specified when you sent the
message. You're not required to use configuration sets when you send messages, but we
recommend that you do. If you don't specify a configuration set with an event destination,
the API doesn't emit event records. These event records are a useful way to determine how
many messages you sent, how much you paid for each one, and whether or not the message was
received by the recipient.

Once you have created a configuration set you should add an [event destination](configuration-sets-event-destinations.md "configuration-sets-event-destinations.md") to help monitor your
message send and receive events and a [protect
configuration](protect-configuration.md "protect-configuration.md") to create allow rules to only send messages to the destinations you do business in.

###### Topics

- [Create a configuration set](configuration-set-create.md "configuration-set-create.md")
- [Edit a configuration set](configuration-set-edit.md "configuration-set-edit.md")
- [View all configuration sets](configuration-set-view.md "configuration-set-view.md")
- [Delete a configuration set](configuration-set-delete.md "configuration-set-delete.md")
- [Manage tags for a configuration set](configuration-set-tags.md "configuration-set-tags.md")
- [Edit a configuration set protect configuration](configuration-set-edit-protect-configuration.md "configuration-set-edit-protect-configuration.md")
