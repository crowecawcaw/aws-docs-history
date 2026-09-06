

# Flow block in Connect Customer: Wait
<a name="wait"></a>

This topic defines the flow block for pausing the flow for the specified amount of time. 

## Description
<a name="wait-description"></a>

This block pauses the flow for the specified wait time or for the specified event. 

For example, if a contact stops responding to a chat, the block pauses the contact flow for the specified wait time (**Timeout** time), then branches accordingly, such as to disconnect.

## Supported channels
<a name="wait-channels"></a>

The following table lists how this block routes a contact who is using the specified channel. 


| Channel | Supported? | 
| --- | --- | 
| Voice | Yes - but only in Inbound flow when the **Keep running while waiting** option, or the **Set event-based wait** option is selected (see the image below). | 
| Chat | Yes | 
| Task | Yes - It always branches to **Time Expired** or **Error**. It never branches to **Bot participant disconnected** or **Participant not found**. The **Participant Type **setting does not affect this behavior. | 
| Email | Yes | 

## Flow types
<a name="wait-types"></a>

You can use this block in the following [flow types](create-contact-flow.md#contact-flow-types):
+ Inbound flow
+ Customer Queue flow

## Properties
<a name="wait-properties"></a>

The following image shows the **Config** tab of the **Wait** block.

![The settings the Wait block, the Config tab.](http://docs.aws.amazon.com/connect/latest/adminguide/images/wait-properties.png)


It has the following properties: 
+ **Participant Type**: Runs the **Wait** block for the specified participant type.
  + **Default** - A customer contact.
  + **Bot** - A custom participant, such as a third-party bot. For more information about using this option, see [Customize chat flow experiences in Connect Customer by integrating custom participants](chat-customize-flow.md). 
+ **Timeout**: Run this branch if the customer hasn't sent a message after a specified amount of time. Maximum is 7 days.
  + Manually set timeout: You can provide the **Number** and **Units**.
  + Dynamically set timeout: The unit of measurement is in seconds.
+ **Customer return**: Route the contact down this branch when the customer returns and sends a message. With this branch you can route the customer to the previous (same) agent, previous (same) queue, or override and set a new working queue or agent. This optional branch is available only when **Participant Type** = **Default**.
+ **Set Event based Wait**: Wait for an event to complete and route the contact down the matching branch. This optional branch is available only when **Participant Type** = **Default**. For each branch, provide a branch name and choose an event type:
  + **Lambda returned**: Wait for an asynchronous Lambda invocation to complete, then route the contact down this branch. Provide the RequestId of the Lambda invocation.
  + The following events are only available in [Amazon Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/enable-nextgeneration-amazonconnect.html) instances:
    + **Case fields updated**: Wait until an Connect Customer Cases case field meets a condition that you define. Provide the **Case ID** and define the **Conditions for Case Fields**.
      + This event is available in the same Regions as Connect Customer Cases. For the list of Regions, see [Cases availability by Region](regions.md#cases_region).
    + **External Tool returned**: Wait for an asynchronous External Tool invocation to complete.
      + This event is available in the same Regions as the [External Tool](external-tool.md) block. For the list of Regions, see [External Tool](regions.md#externaltool_region).  
![The Wait block configured with event based wait.](http://docs.aws.amazon.com/connect/latest/adminguide/images/wait-event-based.png)
+ **Keep running while waiting**: Temporarily route the contact down the **Continue** branch while waiting on the block. This optional branch is available only when **Participant Type** = **Default**.

## Configuration tips
<a name="wait-tips"></a>
+ You can configure the **Wait** block to wait for a Lambda that is invoked using the [AWS Lambda function](invoke-lambda-function-block.md) block in **Asynchronous** execution mode. To do this, select the **Set Event based Wait** option and provide the RequestId of the Lambda invocation. For more information, see [Load Lambda Result](invoke-lambda-function-block.md#properties-load-lamdba).
**Note**  
If the wrong Invocation ID is provided to the **Wait** block, it continues to wait until the **Set timeout**. 
+ You cannot have nested **Wait** blocks, such as a **Wait** block inside the **Continue** branch of another **Wait** block. 

  For example, you can't have the first **Wait** block configured with **Continue** and Lambda-returned branches to send messages with a specific delay (configured on the second Wait block in the Continue branch) while waiting for their asynchronous Lambda invocation to return. This configuration results in the following error on the second **Wait** block:
  + **Unsupported Action In Wait Action's Continue Branch**
+ You can configure the **Wait** block to run other blocks. For example, you might want to play an audio while waiting for a Lambda execution to complete. To do this, add a [Play prompt](play.md) block to the **Continue** branch.
+ You can add multiple **Wait** blocks to your flows. For example: 
  + If the customer comes back in 5 minutes, connect them to the same agent. This is because that agent has all of the context.
  + If the customer doesn't come back after 5 minutes, send a text saying "We missed you." 
  + If the customer comes back in 12 hours, connect to a flow that puts them in a priority queue. However, it doesn't route them to the same agent.
+ Each branch waits on a single event type. Use separate branches for separate sources.
+ Branch names must be static text, with a maximum of 100 characters.
+ Condition types for a **Case fields updated** branch:
  + **String condition** – field name, comparison, and value. Comparisons: **Equals**, **Starts with**, **Ends with**, **Contains**.
  + **Number condition** – field name, comparison, and value. Comparisons: **Equals**, **Greater than**, **Less than**, **Greater than or equal to**, **Less than or equal to**.
  + **Exists condition** – the field is present.
  + Compound conditions with **And** or **Or**. A compound condition needs at least two sub-conditions and cannot be nested more than one level deep.

  For example, to route a contact only after a case is resolved and a refund has been issued, add a **Case fields updated** branch, provide the **Case ID**, select **Compound Condition** as the condition type, and add two sub-conditions: a **String condition** where **status** **Equals** **resolved**, **And** a **Number condition** where **refund\_amount** **Greater than** 0. The contact routes down this branch only when both conditions are true.  
![The Wait block's Case fields updated branch with Compound Condition selected as the condition type.](http://docs.aws.amazon.com/connect/latest/adminguide/images/wait-case-fields-example.png)  
![The Wait block's Case fields updated branch fully configured with the And compound condition checking status equals resolved and refund_amount greater than 0.](http://docs.aws.amazon.com/connect/latest/adminguide/images/wait-case-fields-example-2.png)

## Configured block
<a name="wait-configured"></a>

The following image shows an example of what this block looks like when it is configured with **Participant Type** = **Default**. It has the following branches: **Time Expired** and **Error**. 

![A configured Wait block.](http://docs.aws.amazon.com/connect/latest/adminguide/images/wait-configured.png)


The following image shows an example of what this block looks like when it is configured with **Participant Type** = **Bot**. It has the following branches: **Bot participant disconnected**, **Participant not found**, **Time Expired**, and **Error**. 

![A configured Wait block.](http://docs.aws.amazon.com/connect/latest/adminguide/images/wait-configured2.png)


1. **Bot participant disconnected**: The custom participant, such as a third-party bot, has successfully disconnected to the contact. 

1. **Participant not found**: No custom participant was found to be associated to the contact. 

1. **Time Expired**: The timeout specified has lapsed before the custom participant disconnected.

The following image shows an example of what this block looks like when it is configured with **Set event based wait**. It shows the event branches configured for the block.

![A configured Wait block with event based wait branches.](http://docs.aws.amazon.com/connect/latest/adminguide/images/wait-configured-event-based.png)


## Sample flows
<a name="wait-samples"></a>

Connect Customer includes a set of sample flows. For instructions that explain how to access the sample flows in the flow designer, see [Sample flows in Connect Customer](contact-flow-samples.md). Following are topics that describe the sample flows which include this block.
+ [Sample disconnect flow in Connect Customer](sample-disconnect.md)

## Scenarios
<a name="wait-scenarios"></a>

See these topics for scenarios that use this block:
+ [Example chat scenario](web-and-mobile-chat.md#example-chat-scenario)