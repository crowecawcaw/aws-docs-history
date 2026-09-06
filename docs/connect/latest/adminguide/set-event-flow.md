

# Flow block in Connect Customer: Set event flow
<a name="set-event-flow"></a>

This topic defines the flow block for specifying a flow to run during an interaction with a contact.

## Description
<a name="set-event-flow-description"></a>
+ Specifies which flow to run during a contact event.
+ The following events are supported:
  + **Default flow for agent UI**: specifies the flow to be invoked when a contact comes into the Agent Workspace. You can use this event to set up a [step-by-step](step-by-step-guided-experiences.md) guide to be played to the agent in this scenario.
  + **Disconnect flow for agent UI**: specifies the flow to be invoked when a contact that is open in the Agent Workspace ends. You can use this event to set up a [step-by-step](step-by-step-guided-experiences.md) guide to be played to the agent in this scenario.
  + ** Flow at contact pause**: Specifies the flow to be invoked when a contact comes to paused state. For more information, see [Pause and resume tasks in Connect Customer Tasks](concepts-pause-and-resume-tasks.md).
  + **Flow at contact resume**: Specifies the flow to be invoked when a contact comes to resume from paused state. For more information, see [Pause and resume tasks in Connect Customer Tasks](concepts-pause-and-resume-tasks.md).

## Supported channels
<a name="set-event-channels"></a>

The following table lists how this block routes a contact who is using the specified channel. 


| Channel | Supported? | 
| --- | --- | 
| Voice | Yes | 
| Chat | Yes | 
| Task | Yes | 
| Email | Yes | 

## Flow types
<a name="set-event-flow-types"></a>

You can use this block in the following [flow types](create-contact-flow.md#contact-flow-types):
+ All flows

## Properties
<a name="set-event-flow-properties"></a>

The following image shows the **Properties** page of the **Set event flow** block.

![The properties page of the Set event flow block.](http://docs.aws.amazon.com/connect/latest/adminguide/images/set-event-flow-properties.png)


## Configured block
<a name="set-event-flow-configured"></a>

The following image shows an example of what this block looks like when it is configured. It has the following branches: **Success** and **Error**.

![A configured Set event flow block.](http://docs.aws.amazon.com/connect/latest/adminguide/images/set-event-flow-configured.png)


## Scenarios
<a name="set-event-flow-scenario"></a>

See these topics for scenarios that use this block:
+ [Invoke a guide at the start of a contact in Connect Customer](how-to-invoke-a-flow-sg.md)