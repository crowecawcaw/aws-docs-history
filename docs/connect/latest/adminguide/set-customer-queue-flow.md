

# Flow block in Connect Customer: Set customer queue flow
<a name="set-customer-queue-flow"></a>

This topic defines the flow block for specifying the flow to invoke when a customer is transferred to a queue.

## Description
<a name="set-contact-attributes-description"></a>
+ Specifies the flow to invoke when a customer is transferred to a queue.

## Supported channels
<a name="set-customer-queue-flow-channels"></a>

The following table lists how this block routes a contact who is using the specified channel. 


| Channel | Supported? | 
| --- | --- | 
| Voice | Yes | 
| Chat | Yes | 
| Task | Yes | 
| Email | Yes | 

## Flow types
<a name="set-contact-attributes-types"></a>

You can use this block in the following [flow types](create-contact-flow.md#contact-flow-types):
+ Inbound flow
+ Transfer to Agent flow
+ Transfer to Queue flow

## Properties
<a name="set-contact-attributes-properties"></a>

The following image shows the **Properties** page of the **Set customer queue flow** block.

![The properties page of the Set customer queue flow block.](http://docs.aws.amazon.com/connect/latest/adminguide/images/set-customer-queue-properties.png)


For information about using attributes, see [Use Connect Customer contact attributes](connect-contact-attributes.md).

## Configured block
<a name="set-contact-attributes-configured"></a>

The following image shows an example of what this block looks like when it is configured. It has the following branches: **Success** and **Error**.

![A configured set customer queue flow block.](http://docs.aws.amazon.com/connect/latest/adminguide/images/set-customer-queue-configured.png)


## Sample flows
<a name="set-contact-attributes-samples"></a>

Connect Customer includes a set of sample flows. For instructions that explain how to access the sample flows in the flow designer, see [Sample flows in Connect Customer](contact-flow-samples.md). Following are topics that describe the sample flows which include this block.
+ [Sample queued callback flow in Connect Customer](sample-queued-callback.md)