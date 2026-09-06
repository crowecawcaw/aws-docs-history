

# Create a queue using the Connect Customer admin website
<a name="create-queue"></a>

This topic explains how to create a queue using the Connect Customer admin website. To create queues programmatically, see the [create-queue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/create-queue.html) AWS CLI or [CreateQueue](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateQueue.html) in the *Connect Customer API Reference*.

**How many queues can I create?** To view your quota of **Queues per instance**, open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/).

**To create a queue**

1. Log in to the Connect Customer admin website at https://{{instance name}}.my.connect.aws/. Use an **Admin** account, or an account that has **Routing** - **Queues** - **Create** permission in its security profile.

1. On the Connect Customer admin website, on the navigation menu, choose **Routing**, **Queues**, **Add new queue**.

1. Add the appropriate information about your queue and choose **Add new queue**.

   The following image shows the queue information for the BasicQueue.  
![The Edit queue page for the Basic queue.](http://docs.aws.amazon.com/connect/latest/adminguide/images/add-a-new-queue.png)

   See the following topics for detailed information about each of the above areas:

   1. [Set the hours of operation and time zone for a queue using Connect Customer](set-hours-operation.md)

   1. [Set up outbound caller ID in Connect Customer](queues-callerid.md)

   1. [Set up email in Connect Customer](setup-email-channel.md)

   1. [Set the limit of maximum contacts in a queue using Connect Customer](set-maximum-queue-limit.md)

   1. [Create quick connects in Connect Customer](quick-connects.md)

   The queue is automatically active.

1. Assign the queue to a routing profile; for information, see [Create a routing profile in Connect Customer to link queues to agents](routing-profiles.md). The routing profile links the queue and agents together.

1. Add tags to identify, organize, search for, filter and control who can access this queue. For more information, see [Add tags to resources in Connect Customer](tagging.md).

To learn how queues work, see [How Connect Customer uses routing profiles](concepts-routing.md) and [Queue-based routing to route customers to a specific contact center agent](concepts-queue-based-routing.md).

## APIs to create and manage queues
<a name="apis-manage-queues"></a>

Use the following APIs to create and manage queues programmatically:
+ [CreateQueue](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateQueue.html)
+ [DeleteQueue](https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteQueue.html)
+ [DescribeQueue](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeQueue.html)
+ [ListQueues](https://docs.aws.amazon.com/connect/latest/APIReference/API_ListQueues.html)
+ [SearchQueues](https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchQueues.html)
+ [UpdateQueueHoursOfOperation](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateQueueHoursOfOperation.html)
+ [UpdateQueueMaxContacts](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateQueueMaxContacts.html)
+ [UpdateQueueName](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateQueueName.html)
+ [UpdateQueueOutboundCallerConfig](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateQueueOutboundCallerConfig.html)
+ [UpdateQueueOutboundEmailConfig](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateQueueOutboundEmailConfig.html)
+ [UpdateQueueStatus](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateQueueStatus.html)