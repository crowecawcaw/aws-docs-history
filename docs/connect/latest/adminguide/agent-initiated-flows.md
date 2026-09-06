

# Enable agent-initiated flows during active chat sessions
<a name="agent-initiated-flows"></a>

Agent-initiated workflows are interactive workflows that agents can trigger during active chat sessions with customers. This feature enables agents to send forms for data collection, process payments, update customer profiles, and initiate automated processes while maintaining direct interaction with customers within the chat experience.

## Benefits
<a name="agent-initiated-flows-benefits"></a>

Agent-initiated flows provides the following benefits:
+ Simplify customer task completion by keeping interactions within the chat interface
+ Enable agents to provide real-time assistance during form completion
+ Support sensitive data collection through Show View blocks with [sensitive data configuration options](https://aws.amazon.com/about-aws/whats-new/2024/12/amazon-connect-collect-sensitive-customer-data-chats/)

## Where you can use agent-initiated flows
<a name="agent-initiated-flows-channels"></a>

You can use agent-initiated flows in chat channels, including:
+ Web chat
+ SMS
+ WhatsApp Business
+ Apple Messages for Business

Voice and other channels are not currently supported.

## Limitations
<a name="agent-initiated-flows-limitations"></a>
+ The supported Quick Connect "FLOW" type only work for chat channels (web chat, SMS, WhatsApp Business, Apple Messages for Business).
+ Only [Inbound Flows](https://docs.aws.amazon.com/connect/latest/adminguide/sample-inbound-flow.html) are supported
+ Transfers and adding new participants will not work during an ongoing agent-initiated workflow. The workflow needs to be either completed or cancelled before adding a new agent or contact.
+ Only one agent-initiated flow can execute at a time per contact
+ The following flow blocks are not supported: [Connect assistant](https://docs.aws.amazon.com/connect/latest/adminguide/connect-assistant-block.html), [Authenticate Customer](https://docs.aws.amazon.com/connect/latest/adminguide/authenticate-customer.html), [Create Persistent Contact Association](https://docs.aws.amazon.com/connect/latest/adminguide/create-persistent-contact-association-block.html), [Get Customer Input](https://docs.aws.amazon.com/connect/latest/adminguide/get-customer-input.html)
+ Limited to 10 Agent-initiated flows per Chat

## Security profile permissions for agent-initiated flows
<a name="agent-initiated-flows-permissions"></a>

Before you can create agent-initiated flows, you must have permissions in your security profile.

The required permissions are:
+ **Channels and flows - Views**
+ **Routing - Quick Connects**

![Security profile permissions for agent-initiated flows.](http://docs.aws.amazon.com/connect/latest/adminguide/images/SecurityProfile_cloudscape_channels_flows.png)


## Create Quick Connect for agent-initiated flow
<a name="agent-initiated-flows-create-quick-connect"></a>

1. On the navigation menu, choose **Routing**, **Quick connects**.

1. Choose **Add new**.

1. For **Type**, select **Flow**.

1. Select a specific **Inbound Flow** for agents to send.

1. Choose **Save**.

![Create Quick Connect for agent-initiated flow.](http://docs.aws.amazon.com/connect/latest/adminguide/images/agent-initiated-flows-quick-connect-config.png)


## Associate Quick Connect with queue
<a name="agent-initiated-flows-associate-queue"></a>

1. On the navigation menu, choose **Routing**, **Queues**.

1. Select the queue where agents will use this flow.

1. In the **Quick connects** section, add your Quick Connect.

1. Choose **Save**.

![Associate Quick Connect with queue.](http://docs.aws.amazon.com/connect/latest/adminguide/images/agent-initiated-flows-add-quick-connect.png)


For additional details on quick connects, see [Create quick connects in Connect Customer](quick-connects.md).

## Send Form to Customer
<a name="agent-initiated-flows-send-form"></a>

1. On **agent control panel**, select the **Quick connect** button at the action bar

1. On the selection menu, choose the appropriate form

1. Select **Add to chat**

![Agent control panel Quick connect button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/agent-initiated-flows-agent-example-1.png)


![Form and Add to chat.](http://docs.aws.amazon.com/connect/latest/adminguide/images/agent-initiated-flows-agent-example-2.png)


When the form is active, the agent might cancel the workflow. Agents will see events for the status of the workflow.

![Active workflow status.](http://docs.aws.amazon.com/connect/latest/adminguide/images/agent-initiated-flows-agent-example-3.png)


![Workflow events for agent.](http://docs.aws.amazon.com/connect/latest/adminguide/images/agent-initiated-flows-agent-example-4.png)


## Receive Form from Agent
<a name="agent-initiated-flows-receive-form"></a>
+ Customer will receive the respective form to fill out
+ Customers and agents continue ongoing conversation during the active form
+ Upon submission, the agent will be notified through new events

![Customer receives form.](http://docs.aws.amazon.com/connect/latest/adminguide/images/agent-initiated-flows-customer-example-1.png)


![Form submission notification.](http://docs.aws.amazon.com/connect/latest/adminguide/images/agent-initiated-flows-customer-example-2.png)
