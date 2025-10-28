# Using Neptune Event Notification

###### Topics

- [Amazon Neptune event categories and event messages](event-lists.md "event-lists.md")
- [Subscribing to Neptune event notification](events-subscribing.md "events-subscribing.md")
- [Managing Neptune event notification subscriptions](events-manage.md "events-manage.md")
  Amazon Neptune uses Amazon Simple Notification Service (Amazon SNS) to provide notifications when a Neptune event occurs.
  These notifications can be in any form that is supported by Amazon SNS for an AWS Region, such as
  an email, a text message, or a call to an HTTP endpoint.

Neptune groups these events into categories that you can subscribe to so that you can be
notified when an event in that category occurs. You can subscribe to an event category for a DB
instance, DB cluster, DB snapshot, DB cluster snapshot, or for a DB parameter
group. For example, if you subscribe to the Backup category for a given DB instance, you are
notified whenever a backup-related event occurs that affects the DB instance. You also receive
notification when an event notification subscription changes.

Events occur at both the DB cluster and the DB instance level, so you can receive events
if you subscribe to a DB cluster or a DB instance.

Event notifications are sent to the addresses you provide when you create the subscription.
You might want to create several different subscriptions, such as a subscription that receives
all event notifications and another subscription that includes only critical events for your
production DB instances. You can easily turn off notification without deleting a subscription.
To do so, set the **Enabled** radio button to **No** in the
Neptune console.

###### Important

Amazon Neptune doesn't guarantee the order of events sent in an event stream.
The event order is subject to change.

Neptune uses the Amazon Resource Name (ARN) of an Amazon SNS topic to identify each
subscription. The Neptune console creates the ARN for you when you create the subscription.

Billing for Neptune event notification is through Amazon SNS. Amazon SNS fees apply when using event
notification. For more information, see [Amazon Simple Notification Service
Pricing](https://aws.amazon.com/sns/#pricing "https://aws.amazon.com/sns/#pricing").
