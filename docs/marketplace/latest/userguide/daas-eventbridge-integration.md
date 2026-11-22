

# Managing DaaS subscription events with Amazon EventBridge

AWS Marketplace sends events to Amazon EventBridge in your seller account when a buyer subscribes to your Data as a Service (DaaS) product, when their entitlement changes, and when they cancel. Use these events to know when to grant, change, or remove a buyer's access to your data.

**Amazon SNS notifications aren't available to new sellers**  
If you registered your seller account after July 15, 2026, use Amazon EventBridge to receive events. If you registered on or before that date, you can continue to use Amazon SNS. New notifications are available only in EventBridge. For all notification options, see [Seller notifications for AWS Marketplace events](notifications.md).

**Update buyer access from your application**  
Grant and remove access through your application when you receive an event. Don't edit buyer records by hand in your data store. Automated updates are easier to audit and less likely to cause errors.

## Events for DaaS products
<a name="daas-eventbridge-event-types"></a>

At launch, you sell DaaS products directly to buyers through public and private offers, so you're both the manufacturer and the proposer of each agreement. For the Purchase Agreement Created, Amended, and Ended events, AWS Marketplace sends you only the proposer version. For the other events, you receive the manufacturer version.

When a buyer's agreement or license changes, EventBridge sends an event to the default event bus in your seller account. The following table lists the events for DaaS products:


**DaaS subscription events**  

| Event name | When it's sent | What to do | 
| --- | --- | --- | 
| Purchase Agreement Created - Proposer | A buyer creates a new agreement, replaces an existing one, or renews one. | Record the agreement and take any post-sale actions. To find out whether the agreement is a free trial, call the DescribeAgreement API. Don't activate the buyer's subscription until you receive a License Updated event. | 
| Purchase Agreement Amended - Proposer | A buyer amends an existing agreement. | Update the buyer's record. | 
| Purchase Agreement Ended - Proposer | An agreement expires, or the buyer cancels or terminates it. For a free trial that converts automatically, AWS Marketplace doesn't send this event when the free trial ends. It sends the event only if the buyer cancels. | Record that the agreement ended and start removing the buyer's access. | 
| Purchase Agreement Free Trial Converted - Manufacturer | A buyer's free trial converts to a paid subscription on the conversion date. | Update the buyer's status. The subscription continues. | 
| Purchase Agreement Advisory Issued - Manufacturer | AWS found an issue that might affect billing or service access for an agreement. Causes include account closure, compromise, abuse, or fraud. | Contact the buyer, and decide whether to change their access. | 
| Purchase Agreement Advisory Resolved - Manufacturer | AWS resolved the issue that affected the agreement. | If you changed the buyer's access, you can restore it when you decide to. | 
| License Updated - Manufacturer | The buyer's entitlement to the product changed. | Check the buyer's entitlements with the GetEntitlements API, and provision access to match. | 
| License Deprovisioned - Manufacturer | The buyer's entitlement to the product ended. For a free trial that converts automatically, AWS Marketplace sends this event only if the buyer cancels. | For products that use usage-based pricing, this event starts a 1-hour final reporting window. Report any usage that you haven't reported yet with the BatchMeterUsage API. After the window closes, AWS Marketplace stops accepting usage for that buyer. | 

For the full list of event types and their schemas, see [Amazon EventBridge events](notifications-eventbridge.md).

## Final usage reporting window
<a name="daas-eventbridge-final-usage"></a>

If your product uses pay as you go or contract with consumption pricing, AWS Marketplace gives you 1 hour to report final usage for a buyer whose entitlement has ended. The **License Deprovisioned** event marks the start of that hour. After that hour, `BatchMeterUsage` rejects usage for that buyer, and you can't bill them for it. For more information about pricing models, see [DaaS product pricing in AWS Marketplace](daas-pricing-models.md).

## Setting up events for your DaaS product
<a name="daas-eventbridge-setup"></a>

Use an EventBridge rule to send the events to a place where your application can read them. We recommend an Amazon Simple Queue Service (Amazon SQS) queue as the target, but you can use other targets that EventBridge supports. Complete the following procedures in the AWS account that you registered as your AWS Marketplace seller account, in the US East (N. Virginia) Region.

### Creating a queue
<a name="daas-eventbridge-queue"></a>

Create a queue to hold the events until your application reads them. Save the queue ARN, which you need when you create the rule.

**To create a queue**

1. Open the [Amazon SQS console](https://console.aws.amazon.com/sqs/).

1. Choose **Create queue**.

1. For **Type**, choose **Standard**.

1. For **Name**, enter a name that is unique in your account.

1. Configure the remaining settings to meet your requirements, and then choose **Create queue**.

1. Copy the queue ARN.

### Creating a rule
<a name="daas-eventbridge-rule"></a>

Create an EventBridge rule that matches the AWS Marketplace agreement and license events, and sends them to your queue. You define the event pattern first, and then add the queue as the target. For more information about EventBridge rules, see [Getting started: Create an Amazon EventBridge event bus rule](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html) in the *Amazon EventBridge User Guide*.

**To define the event pattern for the rule**

1. Open the [EventBridge console](https://console.aws.amazon.com/events/).

1. In the navigation pane, choose **Rules**, and then choose **Create rule**.

1. Enter a name for the rule, and keep the **default** event bus.

1. Choose **Rule with an event pattern**, and then choose **Next**.

1. For **Event source**, choose **AWS services**.

1. For **AWS service**, choose **AWS Marketplace Agreements and Licenses**.

1. For **Event type**, choose **All Events** to receive every agreement and license event, or choose specific event types. Then choose **Next**.

An event pattern for a specific event type uses the following structure. The event source is the same for all agreement and license events.

```
{
"detail-type": ["Purchase Agreement Ended - Proposer"],
"source": ["aws.agreement-marketplace"]
}
```

**To add the queue as the target of the rule**

1. For **Target**, choose **AWS service**.

1. Choose **SQS queue**, and then choose your queue. EventBridge adds the permission that the queue needs.

1. Choose **Next** twice, and then choose **Create rule**.

### Processing the events
<a name="daas-eventbridge-process"></a>

Have your application read events from the queue and update your buyer records. Use the table in [Events for DaaS products](#daas-eventbridge-event-types) to decide what to do for each event.