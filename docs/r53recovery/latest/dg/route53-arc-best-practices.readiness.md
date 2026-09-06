

# Best practices for readiness check in ARC
<a name="route53-arc-best-practices.readiness"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

We recommend the following best practice for readiness check in Amazon Application Recovery Controller (ARC).

**Add notifications for readiness status changes**

Set a rule in Amazon EventBridge to send a notification whenever a readiness check status changes, for example, from `READY` to `NOT READY`. When you receive a notification, you can investigate and address the issue, to make sure that your application and resources are ready for failover when you expect them to be.

You can set EventBridge rules to send notifications for several readiness check status changes, including for your recovery group (for your application), for a cell (such as an AWS Region), or for a readiness check for a resource set.

For more information, see [Using readiness check in ARC with Amazon EventBridge](eventbridge-readiness.md).