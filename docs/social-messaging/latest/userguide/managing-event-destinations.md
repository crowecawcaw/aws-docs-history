# Message and event destinations in AWS End User Messaging Social

An event destination is an Amazon SNS topic or Amazon Connect instance that WhatsApp events are sent to. When you turn on
event publishing, all of your send and receive events are sent to the
message and event destination. Use events to monitor, track, and analyze the status of outbound messages and
incoming customer communications.

Each WhatsApp Business Account (WABA) can have one event destination. All events from all resources associated
to the WABA are logged to that event destination. For example, you could have a WABA
with three phone numbers associated to it and all events from those phone numbers are logged
to the one event destination.

###### Topics

- [Add a message and event destination to AWS End User Messaging Social](managing-event-destinations-add.md "managing-event-destinations-add.md")
- [Message and event format in AWS End User Messaging Social](managing-event-destination-dlrs.md "managing-event-destination-dlrs.md")
- [WhatsApp message status](managing-event-destinations-status.md "managing-event-destinations-status.md")
