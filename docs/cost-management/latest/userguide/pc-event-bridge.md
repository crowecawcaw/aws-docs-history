

# Using EventBridge with AWS Pricing Calculator
<a name="pc-event-bridge"></a>

The in-console AWS Pricing Calculator can send events to Amazon EventBridge whenever certain events happen in your bill estimate. Unlike other destinations, you don't need to select which event types you want to deliver. After you have EventBridge set up, Pricing Calculator events can be sent to EventBridge. You can use EventBridge rules to route events to additional targets. For more information about setting up EventBridge, see [ Amazon EventBridge setup and prerequisites](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-setup.html) in the *Amazon EventBridge API Reference*.

The following lists the events AWS Pricing Calculator sends to EventBridge.



| Event type | Description | 
| --- | --- | 
| BillEstimate Created | A bill estimate was created.<br />The ARN, estimate name, and estimate ID of the bill estimate for which the event is sent to EventBridge will be emitted in the event. | 
| BillEstimate Succeeded | A bill estimate completed. This means you will now be able to view the results of the bill estimate.<br />The ARN, estimate name, and estimate ID of the bill estimate for which the event is sent to EventBridge will be emitted in the event. | 
| BillEstimate Failed | A bill estimate generation failed.<br />The ARN, estimate name, and estimate ID of the bill estimate for which the event is sent to EventBridge will be emitted in the event. | 

You can also use AWS Pricing Calculator to send event notifications with EventBridge to write rules that take actions when an event occurs pertaining to your estimate. For example, you can have it send you a notification. For more information about rules in Amazon EventBridge, see [ Create a rule in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html#eb-gs-create-rule) in the *Amazon EventBridge API Reference*.

For more information about the actions and data types you can interact with using the EventBridge API, see [ Amazon EventBridge API Reference](https://docs.aws.amazon.com/eventbridge/latest/APIReference/Welcome.html) in the *Amazon EventBridge API Reference*.

## Amazon EventBridge permissions
<a name="pc-event-bridge-permissions"></a>

AWS Pricing Calculator doesn't require any additional permissions to deliver events to Amazon EventBridge.

## Event message structure examples
<a name="pc-event-bridge-examples"></a>

**BillEstimate Created**

```
{
    "version": "0",
    "id": "00000000-0000-0000-0000-000000000001",
    "detail-type": "BillEstimate Created",
    "source": "aws.bcm-pricing-calculator",
    "account": "111122223333",
    "time": "2024-09-12T13:47:34Z",
    "region": "us-east-1",
    "resources": ["arn:aws:bcm-pricing-calculator::111122223333:bill-estimate/00000000-0000-0000-0000-000000000000"],
    "detail": {
        "id": "00000000-0000-0000-0000-000000000001",
        "name": "amzn-example-name"
     }
}
```

**BillEstimate Succeeded**

```
{
    "version": "0",
    "id": "00000000-0000-0000-0000-000000000002",
    "detail-type": "BillEstimate Succeeded",
    "source": "aws.bcm-pricing-calculator",
    "account": "111122223333",
    "time": "2024-09-12T13:47:34Z",
    "region": "us-east-1",
    "resources": ["arn:aws:bcm-pricing-calculator::111122223333:bill-estimate/00000000-0000-0000-0000-000000000002"],
    "detail": {
        "id": "00000000-0000-0000-0000-000000000002",
        "name": "amzn-example-name"
     }
}
```

**BillEstimate Failed**

```
{
    "version": "0",
    "id": "00000000-0000-0000-0000-000000000003",
    "detail-type": "BillEstimate Failed",
    "source": "aws.bcm-pricing-calculator",
    "account": "111122223333",
    "time": "2024-09-12T13:47:34Z",
    "region": "us-east-1",
    "resources": ["arn:aws:bcm-pricing-calculator::111122223333:bill-estimate/00000000-0000-0000-0000-000000000003"],
    "detail": {
        "id": "00000000-0000-0000-0000-000000000003",
        "name": "amzn-example-name",
        "failureReason": "We can't process this request right now because of an internal error. Try again later."
     }
}
```