

# Flow block in Connect Customer: Set logging behavior
<a name="set-logging-behavior"></a>

This topic defines the flow block for enabling flow logs to track events as contacts interact with flows.

## Description
<a name="set-logging-behavior-description"></a>
+ Enables flow logs so you can track events as contacts interact with flows.
+ Flow logs are stored in Amazon CloudWatch. For more information, see [Flow logs stored in an Amazon CloudWatch log group](contact-flow-logs-stored-in-cloudwatch.md).

## Supported channels
<a name="set-logging-channels"></a>

The following table lists how this block routes a contact who is using the specified channel. 


| Channel | Supported? | 
| --- | --- | 
| Voice | Yes | 
| Chat | Yes | 
| Task | Yes | 
| Email | Yes | 

## Flow types
<a name="set-logging-behavior-types"></a>

You can use this block in the following [flow types](create-contact-flow.md#contact-flow-types):
+ All flows

## Properties
<a name="set-logging-behavior-properties"></a>

The following image shows the **Properties** page of the **Set logging behavior** block. It has two options: enable logging behavior, or disable it.

![The properties page of the Set logging behavior block.](http://docs.aws.amazon.com/connect/latest/adminguide/images/set-logging-behavior-properties.png)


## Scenarios
<a name="set-logging-behavior-scenarios"></a>

See these topics for more information about flow logs:
+ [Use flow logs to track events in Connect Customer flows](about-contact-flow-logs.md)