# Managing data access for Security Lake

subscribers

Subscribers with data access to source data in Amazon Security Lake are notified of new objects
for the source as the data is written to the S3 bucket. By default, subscribers are notified
about new objects through an HTTPS endpoint that they provide. Alternatively, subscribers
can be notified about new objects by polling an Amazon Simple Queue Service (Amazon SQS) queue.

Subscribers are notified of
new Amazon S3 objects for a source as the objects are written to the Security Lake data lake.
Subscribers can directly access the S3 objects and receive notifications of new
objects through a subscription endpoint or by polling an Amazon Simple Queue Service (Amazon SQS) queue.
This subscription type is identified as `S3` in the
`accessTypes` parameter of the [CreateSubscriber](../APIReference/API_CreateSubscriber.md "../APIReference/API_CreateSubscriber.md") API.

###### Topics

- [Prerequisites](prereqs-creating-subscriber.md "prereqs-creating-subscriber.md")
- [Creating a subscriber with data access](create-subscriber-data-access.md "create-subscriber-data-access.md")
- [Updating a data subscriber](subscriber-update.md "subscriber-update.md")
- [Removing a data subscriber](remove-data-access-subscriber.md "remove-data-access-subscriber.md")
