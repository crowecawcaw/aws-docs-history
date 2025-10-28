# Get started with Amazon Connect

###### Tip

For an online workshop that leverages a case study and includes hands-on labs, see
[Introduction to Amazon Connect](https://catalog.workshops.aws/amazon-connect-introduction/en-US/introduction "https://catalog.workshops.aws/amazon-connect-introduction/en-US/introduction") by AWS Workshop Studio.

Use these steps to set up your contact center.

1. [Create an Amazon Connect instance](amazon-connect-instances.md "amazon-connect-instances.md"). Use an instance to contain all the resources and settings related to your
   contact center. You specify how you plan to manage user accounts, whether your
   contact center will accept incoming calls and make outbound calls, and review the
   location where data will be stored in your Amazon S3 bucket.
2. [Set up contact center phone numbers for your Amazon Connect
   instance](ag-overview-numbers.md "ag-overview-numbers.md"). If you're using voice, either
   claim a phone number that AWS provides, or port your current phone number to
   Amazon Connect. If you choose to port your numbers, we suggest claiming a number so you can
   test Amazon Connect and build your contact center while waiting for your numbers to be ported
   over.
3. [Set up routing in Amazon Connect](connect-queues.md "connect-queues.md"). Create your
   queues and routing profiles, and set your hours of operation. In your routing
   profiles, specify the channels that agents should use: voice, chat, tasks, or all
   three. You also specify how many chats and tasks an agent can manage at the same
   time.
4. [Flows in Amazon Connect](connect-contact-flows.md "connect-contact-flows.md").
   Establish a flow to define the customer experience with your contact center
   from start to finish. A single flow works for voice, chat, and tasks, which
   makes your design more efficient. When you build flows and configure the
   blocks, indicate how the flow should work for voice, chat, and tasks.
5. Add users, which are your managers and agents, and configure their settings.
   Assign a routing profile to each agent, specify whether they are using a softphone
   or desk phone, and set how long they have for **After contact
   work**. For instructions, see [Add users to Amazon Connect](user-management.md "user-management.md") and [Set up your contact center agents in Amazon Connect](connect-agents.md "connect-agents.md").
6. If you're using chat, we provide several tools to help you enable your
   customer-facing app to engage with Amazon Connect chat. For more information, see [Set up your customer's chat experience in Amazon Connect](enable-chat-in-app.md "enable-chat-in-app.md").

## Next steps

There's a lot you can do to optimize your contact center. Here are a couple of
additional steps that you may find useful:

1. [Monitor live & recorded
   conversations](monitoring-amazon-connect.md "monitoring-amazon-connect.md").
   Monitor live conversations and review past conversations. This is a way that
   managers can coach agents and help them improve. For voice conversations, set up
   recording in your flows. For chat conversations, set up recording at the
   instance level.

To learn how to monitor conversations, see [Enable enhanced multi-party contact monitoring
in Amazon Connect](monitor-conversations.md "monitor-conversations.md"). 2. [Create conversational AI bots in
Amazon Connect](connect-conversational-ai-bots.md "connect-conversational-ai-bots.md"). Use Amazon Lex in your
contact center to reduce the load on your agents. For example, a bot can handle
the initial interaction before the chat is routed to an agent, and also answer
common questions for the customer.

## Take a free online class

Check out the following free online classes:

- [Introduction to Amazon Connect and the Contact Control Panel (CCP)](https://explore.skillbuilder.aws/learn/course/external/view/elearning/12303/introduction-to-amazon-connect-and-the-connect-control-panel-ccp "https://explore.skillbuilder.aws/learn/course/external/view/elearning/12303/introduction-to-amazon-connect-and-the-connect-control-panel-ccp")
- [Amazon Connect: Introduction to the Administrative Interface](https://explore.skillbuilder.aws/learn/course/external/view/elearning/12328/amazon-connect-introduction-to-the-administrative-interface "https://explore.skillbuilder.aws/learn/course/external/view/elearning/12328/amazon-connect-introduction-to-the-administrative-interface")
- [Amazon Connect: Creating and Managing Amazon Connect Instances](https://explore.skillbuilder.aws/learn/course/external/view/elearning/12304/amazon-connect-creating-and-managing-amazon-connect-instances "https://explore.skillbuilder.aws/learn/course/external/view/elearning/12304/amazon-connect-creating-and-managing-amazon-connect-instances")
- [Amazon Connect: Implementing Chat in Amazon Connect](https://explore.skillbuilder.aws/learn/course/external/view/elearning/14504/amazon-connect-implementing-chat-in-connect "https://explore.skillbuilder.aws/learn/course/external/view/elearning/14504/amazon-connect-implementing-chat-in-connect")
- [Amazon Connect: Implementing Tasks in Amazon Connect](https://explore.skillbuilder.aws/learn/course/external/view/elearning/14209/amazon-connect-implementing-task-on-connect "https://explore.skillbuilder.aws/learn/course/external/view/elearning/14209/amazon-connect-implementing-task-on-connect")

## Additional resources for Amazon Connect

In addition to using the contents of this guide, you can learn more about Amazon Connect by using
the following resources.

###### Resources

- [Amazon Connect API Reference](#acp-api "#acp-api")
- [Amazon Connect Streams](#streams "#streams")
- [Amazon Connect Chat UI Examples](#chat-example "#chat-example")

### Amazon Connect API Reference

The [Amazon Connect API Reference](../APIReference.md "../APIReference.md")
describes the API actions that are used to set up and manage your contact center.

### Amazon Connect Streams

The [Amazon Connect Streams](https://github.com/aws/amazon-connect-streams "https://github.com/aws/amazon-connect-streams")
documentation describes how to integrate your existing web applications with Amazon Connect.
Streams gives you the power to embed the Contact Control Panel (CCP) UI components into
your page, and/or handle agent and contact state events directly giving you the power to
control agent and contact state through an object oriented event driven interface. You
can use the built in interface or build your own from scratch: Streams gives you the
power to choose.

### Amazon Connect Chat UI Examples

The [Amazon Connect Chat SDK and Sample Implementations](https://github.com/amazon-connect/amazon-connect-chat-ui-examples/ "https://github.com/amazon-connect/amazon-connect-chat-ui-examples/") provides examples of how to
enable your app to engage with Amazon Connect chat.
