

# Flow block in Connect Customer: Check hours of operation
<a name="check-hours-of-operation"></a>

This topic defines the flow block to checks whether a contact occurs within or outside of the defined hours of operation.

## Description
<a name="check-hours-of-operation-description"></a>

Set up the **Check hours of operation** flow block to determine what path a contact should take at any given time.
+ It checks for hours of operation defined directly on the block.
+ If none are specified, it checks the hours for the current defined on the queue.
+ It checks if the designed hours of operations are open (in hours) or closed (out of hours), and provides configuration for each branch.
+ If optionally provides a way to create additional branches for overrides related to the hours of operation, for example to play a special greeting on a holiday before taking the standard out of hours path.

## Supported channels
<a name="check-hours-of-operation-channels"></a>

The following table lists how this block routes a contact who is using the specified channel. 


| Channel | Supported? | 
| --- | --- | 
| Voice | Yes | 
| Chat | Yes | 
| Task | Yes | 
| Email | Yes | 

## Flow types
<a name="check-hours-of-operation-types"></a>

You can use this block in the following [flow types](create-contact-flow.md#contact-flow-types):
+ Inbound flow
+ Customer queue flow
+ Transfer to Agent flow
+ Transfer to Queue flow

## Properties
<a name="check-hours-of-operation-properties"></a>

Select the **Check hours of operation** flow block to view its properties and define what path a contact should take based on the current date and time.

1. Within Connect Customer, navigate to the **Routing** menu.

1. Select the **Flows** page.

1. Open the desired resource.

1. Find its **Check hours of operation** block. It has default branches:

   1. **In hours**

   1. **Out of hours**

   1. **Error**

1. Choose on the flow block to optionally specify an hours of operation for this flow.

   1. If not specified, Connect Customer will use the hours associated with a contact's queue.

1. If you wish to set up special branching for certain dates, find the **Optional branches** section.  
![Check hours of operation properties.](http://docs.aws.amazon.com/connect/latest/adminguide/images/check-hours-of-operation-properties.png)

1. Select **Check override**.

1. Specify the name of the override that should have its own path.

1. Select **Confirm** then save your change.

1. Repeat as needed.  
![Check hours of operation branches.](http://docs.aws.amazon.com/connect/latest/adminguide/images/check-hours-of-operation-branches.png)

1. Build out the desired flow path for each new node.

For more information on standard day-of-the-week configurations, see [Set the hours of operation and time zone for a queue using Connect Customer](set-hours-operation.md).

To learn more about overrides, see [Set overrides for extended, reduced, and holiday hours](hours-of-operation-overrides.md).

## Agent queues
<a name="hours-of-operation-with-agent-queues"></a>

Agent queues that are automatically created for each agent in your instance do not include an hours of operation.

If you use this block to check the hours of operation for an agent queue, the check fails and the contact is routed down the **Error** branch.

## Sample flows
<a name="check-hours-of-operation-samples"></a>

Connect Customer includes a set of sample flows. For instructions that explain how to access the sample flows in the flow designer, see [Sample flows in Connect Customer](contact-flow-samples.md). Following are topics that describe the sample flows which include this block.

[Sample inbound flow in Connect Customer for the first contact experience](sample-inbound-flow.md)