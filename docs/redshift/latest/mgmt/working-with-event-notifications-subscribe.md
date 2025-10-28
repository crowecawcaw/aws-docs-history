Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Amazon Redshift cluster event

notification subscriptions

Amazon Redshift uses the Amazon Simple Notification Service (Amazon SNS) to communicate notifications of Amazon Redshift events.
You enable notifications by creating an Amazon Redshift event subscription. You can be notified
when an event occurs for a given cluster, snapshot, security group, or parameter group.
The simplest way to create a subscription is with the Amazon SNS console. For information on
creating an Amazon SNS topic and subscribing to it, see [Getting started with Amazon SNS](../../../sns/latest/dg/GettingStarted.md "../../../sns/latest/dg/GettingStarted.md").

In the Amazon Redshift subscription, you specify a set of filters for Amazon Redshift events and an
Amazon SNS topic. Whenever an event occurs that matches the filter criteria, Amazon Redshift
publishes a notification message to the Amazon SNS topic.

Amazon SNS then transmits the message to any Amazon SNS consumers that have an Amazon SNS
subscription to the topic. The messages sent to the Amazon SNS consumers can be in any form
supported by Amazon SNS for an AWS Region, such as an email, a text message, or a call to
an HTTP endpoint. For example, all Regions support email notifications, but SMS
notifications can only be created in the US East (N. Virginia) Region.

###### Note

Currently, you can only create an event subscription to an Amazon SNS standard topic
(not to an Amazon SNS FIFO topic). For more information, see [Amazon SNS event sources](../../../sns/latest/dg/sns-event-sources.md "../../../sns/latest/dg/sns-event-sources.md") in the
_Amazon Simple Notification Service Developer Guide_.

When you create an event notification subscription, you specify one or more event
filters. Amazon Redshift sends notifications through the subscription any time an event occurs
that matches all of the filter criteria. The filter criteria include source type (such
as cluster or snapshot), source ID (such as the name of a cluster or snapshot), event
category (such as Monitoring or Security), and event severity (such as INFO or
ERROR).

If you create event notification subscriptions using the CLI or API, you must create
an Amazon Simple Notification Service topic and subscribe to that topic with the Amazon SNS console or Amazon SNS API. You
will also need to retain the Amazon Resource Name (ARN) of the topic because it is used
when submitting CLI commands or API actions.

You can easily turn off notification without deleting a subscription by setting the
**Enabled** radio button to `No` in the AWS Management Console or by
setting the `Enabled` parameter to `false` using the Amazon Redshift CLI
or API.

An Amazon Redshift event subscription can specify these event criteria:

- Source type, the values are cluster, snapshot, parameter-groups, and
  security-groups.
- Source ID of a resource, such as `my-cluster-1` or
  `my-snapshot-20130823`. The ID must be for a resource in the same
  AWS Region as the event subscription.
- Event category, the values are Configuration, Management, Monitoring,
  Security, and Pending
- Event severity, the values are INFO or ERROR.
  The event criteria can be specified independently, except that you must specify a
  source type before you can specify source IDs in the console. For example, you can
  specify an event category without having to specify a source type, source ID, or
  severity. While you can specify source IDs for resources that are not of the type
  specified in source type, no notifications will be sent for events from those resources.
  For example, if you specify a source type of cluster and the ID of a security group,
  none of the events raised by that security group would match the source type filter
  criteria, so no notifications would be sent for those events.

Amazon Redshift sends a notification for any event that matches all criteria specified in a
subscription. Some examples of the sets of events returned:

- Subscription specifies a source type of cluster, a source ID of my-cluster-1,
  a category of Monitoring, and a severity of ERROR. The subscription will send
  notifications for only monitoring events with a severity of ERROR from
  my-cluster-1.
- Subscription specifies a source type of cluster, a category of Configuration,
  and a severity of INFO. The subscription will send notifications for
  configuration events with a severity of INFO from any Amazon Redshift cluster in the
  AWS account.
- Subscription specifies a category of Configuration, and a severity of INFO.
  The subscription will send notifications for configuration events with a
  severity of INFO from any Amazon Redshift resource in the AWS account.
- Subscription specifies a severity of ERROR. The subscription will send
  notifications for all events with a severity of ERROR from any Amazon Redshift resource
  in the AWS account.
  If you delete or rename an object whose name is referenced as a source ID in an
  existing subscription, the subscription will remain active, but will have no events to
  forward from that object. If you later create a new object with the same name as is
  referenced in the subscription source ID, the subscription will start sending
  notifications for events from the new object.

Amazon Redshift publishes event notifications to an Amazon SNS topic, which is identified by its
Amazon Resource Name (ARN). When you create an event subscription using the Amazon Redshift
console, you can either specify an existing Amazon SNS topic, or request that the console
create the topic when it creates the subscription.

All Amazon Redshift event notifications sent to the Amazon SNS topic are in turn transmitted to
all Amazon SNS consumers that are subscribed to that topic. Use the Amazon SNS console to make
changes to the Amazon SNS topic, such as adding or removing consumer subscriptions to the
topic.

The following sections list all categories and events that you can be notified of. It
also provides information about subscribing to and working with Amazon Redshift event
subscriptions.
