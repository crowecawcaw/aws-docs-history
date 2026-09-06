

# Default customer queue flow in Connect Customer: queue message and music
<a name="default-customer-queue"></a>

This default flow is run when a customer is placed in a queue. 

1.  The loop has a one-time voice prompt:

   *Thank you for calling. Your call is very important to us and will be answered in the order it was received.*

1. It plays queue music in .wav format that's been uploaded to the Connect Customer instance. 

1. The customer remains in this loop until their call is answered by an agent.

**Important**  
The **Default customer queue flow** does not support chat, tasks, or email contacts out of the box. It will fail if you use it for these contacts without any changes. The **Default customer queue** flow contains a [Loop prompts](loop-prompts.md) block, and that block only supports voice contacts.  
We recommend you create a new flow, and use it to check the channel and then route the contact to the appropriate queue. For instructions specific to tasks, see [How to send tasks to a queue](tasks.md#example-enqueue-task). 

## Change the default message a customer hears when they are put in queue
<a name="change-default-customer-queue"></a>

The following steps show how to change the default message customers hear when they are put in a queue to wait for the next available agent.

1. On the navigation menu, choose **Routing**, **Flows**.

1. On the **Flows** page, choose **Default customer queue**, as shown in the following image.  
![Default customer queue flow on the flows page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customize-default-contact-flow1.png)

1. To customize the message, choose the **Loop prompts** block to open the properties page.   
![Loop prompts block on the flow designer.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customize-default-contact-flow2.png)

1. Use the dropdown box to either choose different music, or set to **Text to Speech** and then type a message to be played,

   For example, the following image shows the message "*Thank you for calling. Did you know you can reset your own password at the login page? Choose Reset now, and following the prompts.*"   
![Loop prompts block configured with a text-to-speech message.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customize-default-contact-flow3.png)

1. Choose **Save** at the bottom of the properties page. 

1. Choose **Publish**. Connect Customer starts playing the new message almost immediately (it might take a few moments for it to fully take effect).  
![The publish button on the flow designer.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customize-default-contact-flow4.png)