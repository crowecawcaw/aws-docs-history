

# Get started with Connect Customer
<a name="amazon-connect-get-started"></a>

**Tip**  
For an online workshop that uses a case study and includes hands-on labs, see [Introduction to Connect Customer](https://catalog.workshops.aws/amazon-connect-introduction/en-US/introduction) by AWS Workshop Studio.

Use these steps to set up your contact center. 

1. [Create a Connect Customer instance](amazon-connect-instances.md). Use an instance to contain all the resources and settings related to your contact center. You specify how you plan to manage user accounts, whether your contact center will accept incoming calls and make outbound calls, and review the location where data will be stored in your Amazon S3 bucket. 

1. [Set up contact center phone numbers for your Connect Customer instance](ag-overview-numbers.md). If you're using voice, either claim a phone number that AWS provides, or port your current phone number to Connect Customer. If you choose to port your numbers, we suggest claiming a number so you can test Connect Customer and build your contact center while waiting for your numbers to be ported over. 

1. [Set up routing in Connect Customer](connect-queues.md). Create your queues and routing profiles, and set your hours of operation. In your routing profiles, specify the channels that agents should use: voice, chat, tasks, or all three. You also specify how many chats and tasks an agent can manage at the same time.

1. [Flows in Connect Customer](connect-contact-flows.md). Establish a flow to define the customer experience with your contact center from start to finish. A single flow works for voice, chat, and tasks, which makes your design more efficient. When you build flows and configure the blocks, indicate how the flow should work for voice, chat, and tasks. 

1. Add users, which are your managers and agents, and configure their settings. Assign a routing profile to each agent, specify whether they are using a softphone or desk phone, and set how long they have for **After contact work**. For instructions, see [Add users to Connect Customer](user-management.md) and [Set up your contact center agents in Connect Customer](connect-agents.md). 

1. If you're using chat, we provide several tools to help you enable your customer-facing app to engage with Connect Customer chat. For more information, see [Set up your customer's chat experience in Connect Customer](enable-chat-in-app.md). 

## Next steps
<a name="gs-options"></a>

There's a lot you can do to optimize your contact center. Here are a couple of additional steps that you might find useful: 

1. [Monitor live & recorded conversations](monitoring-amazon-connect.md). Monitor live conversations and review past conversations. This is a way that managers can coach agents and help them improve. For voice conversations, set up recording in your flows. For chat conversations, set up recording at the instance level. 

   To learn how to monitor conversations, see [Enable enhanced multi-party contact monitoring in Connect Customer](monitor-conversations.md).

1. [Create conversational AI bots in Connect Customer](connect-conversational-ai-bots.md). Use Amazon Lex in your contact center to reduce the load on your agents. For example, a bot can handle the initial interaction before the chat is routed to an agent, and also answer common questions for the customer. 

## Take a free online class
<a name="gs-class"></a>

Check out the following free online classes:
+  [Introduction to Connect Customer and the Contact Control Panel (CCP)](https://explore.skillbuilder.aws/learn/course/external/view/elearning/12303/introduction-to-amazon-connect-and-the-connect-control-panel-ccp) 
+  [Connect Customer: Introduction to the Administrative Interface](https://explore.skillbuilder.aws/learn/course/external/view/elearning/12328/amazon-connect-introduction-to-the-administrative-interface) 
+  [Connect Customer: Creating and Managing Connect Customer Instances](https://explore.skillbuilder.aws/learn/course/external/view/elearning/12304/amazon-connect-creating-and-managing-amazon-connect-instances) 
+  [Connect Customer: Implementing Chat in Connect Customer](https://explore.skillbuilder.aws/learn/course/external/view/elearning/14504/amazon-connect-implementing-chat-in-connect) 
+  [Connect Customer: Implementing Tasks in Connect Customer](https://explore.skillbuilder.aws/learn/course/external/view/elearning/14209/amazon-connect-implementing-task-on-connect) 

## Additional resources for Connect Customer
<a name="additional-resources"></a>

In addition to using the contents of this guide, you can learn more about Connect Customer by using the following resources.

**Topics**
+ [Connect Customer API Reference](#acp-api)
+ [Connect Customer Streams](#streams)
+ [Connect Customer Chat UI Examples](#chat-example)

### Connect Customer API Reference
<a name="acp-api"></a>

The [Connect Customer API Reference](https://docs.aws.amazon.com/connect/latest/APIReference/) describes the API actions that are used to set up and manage your contact center.

### Connect Customer Streams
<a name="streams"></a>

The [Connect Customer Streams](https://github.com/aws/amazon-connect-streams) documentation describes how to integrate your existing web applications with Connect Customer. Streams gives you the power to embed the Contact Control Panel (CCP) UI components into your page, or handle agent and contact state events directly giving you the power to control agent and contact state through an object oriented event driven interface. You can use the built in interface or build your own from scratch: Streams gives you the power to choose.

### Connect Customer Chat UI Examples
<a name="chat-example"></a>

The [Connect Customer Chat SDK and Sample Implementations](https://github.com/amazon-connect/amazon-connect-chat-ui-examples/) provides examples of how to enable your app to engage with Connect Customer chat. 