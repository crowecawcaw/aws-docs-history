

# Flow block in Connect Customer: Resume contact
<a name="resume-contact"></a>

This topic defines the flow block for resuming a task or email contact from a paused state.

## Description
<a name="resume-contact-description"></a>
+ Resumes a task or email contact from a paused state. This lets agents free up an active slot to receive more critical contacts. For example, a contact might be stalled because of a missing approval or because it is waiting on external input.
+ For more information how pausing and resuming tasks works in Connect Customer, see [Pause and resume tasks in Connect Customer Tasks](concepts-pause-and-resume-tasks.md). 
+ For more information about how pausing and resuming emails works in Connect Customer, see [Pause and resume emails in Connect Customer](concepts-pause-and-resume-emails.md). 

## Supported channels
<a name="resume-contact-channels"></a>

The following table lists how this block routes a contact who is using the specified channel. 


| Channel | Supported? | 
| --- | --- | 
| Voice | No - Error branch | 
| Chat | No - Error branch | 
| Task | Yes | 
| Email | Yes | 

## Flow types
<a name="resume-contact-types"></a>

You can use this block on all flow types. 

## Properties
<a name="resume-contact-properties"></a>

The following image shows the **Properties** page of the **Resume contact** block.

![The properties page of the resume contact block.](https://docs.aws.amazon.com/connect/latest/adminguide/images/resume-contact.png)


## Configuration tips
<a name="resume-contact-tips"></a>

When you design a flow to resume unassigned, paused tasks that are dequeued, be sure to add a [Transfer to queue](transfer-to-queue.md) block to the flow to queue the task after resuming. Otherwise, the task will stay in a de-queued state. 

## Configured block
<a name="resume-contact-configured"></a>

The following image shows an example of what this block looks like when it is configured. It has an **Error event** branch.

![A configured Resume contact block.](https://docs.aws.amazon.com/connect/latest/adminguide/images/resume-contact-configured.png)
