

# Test the sample voice and chat experience in Connect Customer
<a name="tutorial1-explore-voice-and-chat"></a>

To better understand what the voice and chat experiences are like for your agents and customers, you can test them without doing any development. 

This tutorial shows you how to access and use the [Contact Control Panel (CCP)](agent-user-guide.md). The CCP is a web page that agents use to accept and manage voice and chat contacts.

**Test flows that you build**  
This tutorial tests the sample voice and chat experience. To test flows that you build yourself, use the Connect Customer test and simulation tools. For more information, see [Connect Customer Testing and Simulation](testing-simulation.md).

**Prerequisites**

This tutorial is part of a series. If you performed Tutorial 1, you're ready to go. If not, here's what you need:
+ An AWS account
+ A configured Connect Customer instance
+ An Connect Customer administrative account
+ A claimed phone number

**Topics**
+ [Step 1: Handle a voice contact](#tutorial1-explore-voice)
+ [Step 2: Use the CCP to handle a chat contact](#tutorial1-test-2)

## Step 1: Handle a voice contact
<a name="tutorial1-explore-voice"></a>

1. On the Connect Customer navigation menu, choose **Dashboard**.   
![The dashboard icon on the navigation menu.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-dashboard-menu.png)

1. On the **Dashboard** page, choose **Test chat**.   
![The dashboard page, the text chat link.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-test-chat.png)
**Note**  
If you do not see **Test chat** on the **Dashboard** page, choose **Channels** on the navigation menu, and then choose **Test chat**. For more information, see [Test voice, chat, and task experiences in Connect Customer](chat-testing.md).

1. On the **Test Chat** page, choose **Activate Contact Control Panel**.  
![The test chat page, the Activate Contact Control Panel link.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-activate-ccp.png)

1. If your browser prompts you to grant microphone access, choose **Allow**.  
![The browser prompts to allow your instance to access your microphone.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-allow-microphone.png)

1. If your browser prompts you to allow notifications, choose **Allow**.  
![The browser prompts to allow notifications.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-allow-notifications.png)

1. In the test CCP, set your status to **Available**.  
![The CCP, the Available status setting.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-testccp-available.png)

1. Use your mobile phone to call the phone number that you claimed earlier. If you didn't write down the number, you can find it by going to **Channels**, **Phone numbers**.

1. When your call is joined to Connect Customer you'll hear "Press 1 to be put in queue for an agent, 2 to ..." This is the [Sample inbound flow](sample-inbound-flow.md) that Connect Customer runs by default. You're going to change this later in the tutorial.

1. You can play around with the different options in the Sample inbound flow. To connect to an agent, press **1**, **1**, **1**.

1. In the CCP, choose **Accept call**.   
![The CCP, an incoming call.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-accept-call.png)

1. You'll see what the CCP looks like when an agent is connected to a customer.   
![The CCP, a connected call.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-first-call.png)

1. Choose **End call**. 

   Now the contact is in the After Contact Work (ACW) state. This is when the agent might enter some notes about the contact.  
![The CCP, after call work, the close contact button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-acw.png)

1. Choose **Close contact**. This frees the agent to take another incoming contact. 

Well done\! You've handled your first voice contact\! 

**Tip**  
As an administrator, you can launch the CCP from anywhere on the Connect Customer console by choosing the phone icon on the top of the page.  

![The phone icon at the top of the Connect Customer console that launches the CCP.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-phone-icon.png)


### Next step
<a name="tutorial1-test-voice-next-step"></a>

Go to [Step 2: Use the CCP to handle a chat contact](#tutorial1-test-2) to experience how to handle a chat contact.

## Step 2: Use the CCP to handle a chat contact
<a name="tutorial1-test-2"></a>

In Step 1, you used the Contact Control Panel (CCP) to manage a voice contact. In this step, you experience how to use the CCP to manage a chat contact. 

1. This procedure assumes you've completed [Step 1: Handle a voice contact](#tutorial1-explore-voice). If you haven't, please do so now.

1. On the **Test chat** page, choose the chat bubble to start a chat.  
![The test chat page, the chat bubble.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-chat-bubble.png)

1. The Sample inbound flow automatically transfers to you a queue. However, you can type a message as the customer and the agent receives it. For example, *I need help resetting my password*.  
![A chat conversation in the CCP, showing messages from the flow, and customer.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-start-chat.png)

1. In the CCP, accept the incoming chat.   
![The CCP, an incoming chat, the button to accept the chat.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-accept-chat.png)

1. Use the CCP to send chat messages to the customer. 

1. When you're done chatting, choose **End chat**. Then in the CCP, choose **Close contact**.

Congratulations\! You've experienced what it's like to chat using Connect Customer. 

Next, try Tutorial 3 to set up an IT Help Desk. It shows you how to set up routing, create a flow, and then test the custom voice and chat experience. Go to [Create an IT help desk in Connect Customer](tutorial1-create-helpdesk.md).