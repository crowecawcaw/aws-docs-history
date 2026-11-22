

# Use agents

You can chat with an agent, mention it in any conversation, add it to your favorites, or set it as your default. An agent can also hand work to other agents.

**Topics**
+ [Install a shared agent](#install-shared-agent)
+ [Chat with an agent](#chat-with-agent)
+ [Attach resources in a chat](#attach-resources-chat)
+ [Make an agent a favorite or your default](#make-agent-default)
+ [Multi-agent orchestration](#multi-agent-orchestration)

## Install a shared agent
<a name="install-shared-agent"></a>

Before you use an agent that someone shared with you, install it.

**To install a shared agent**

1. Choose **Customize**, and then choose the **Agents** tab.

1. Choose **Browse all**.

1. Choose an agent.

1. Choose **Install**.

## Chat with an agent
<a name="chat-with-agent"></a>

You can start a chat with an agent in the following ways:
+ Choose the agent name in the chat to open the agent switcher, and then choose the agent.
+ In a conversation, enter @ and the agent's name to mention it.
+ Open the agent's details pane and choose **Chat**, or hover over the agent's row and choose the **Chat** icon.

Responses include citations. To view them, choose **Sources** under the response. Your conversations are saved.

## Attach resources in a chat
<a name="attach-resources-chat"></a>

To attach resources to a conversation, choose the plus sign (\+) in the chat box, and then choose **Spaces** or **Upload files**. An attached space becomes the main context for that conversation only.

## Make an agent a favorite or your default
<a name="make-agent-default"></a>

You can add an agent to your favorites so you can find it with the **Favorites** filter. You can also make an agent your default, so Quick uses it for every new chat.

**To favorite an agent**

1. Choose **Customize**, and then choose the **Agents** tab.

1. Open the agent's menu, and then choose **Add to favorites**.

**To make an agent your default**

1. Choose **Customize**, and then choose the **Agents** tab.

1. Open the agent's menu, and then choose **Make default**.

**Tip**  
You can also use your agents while automating your routine tasks with Quick Flows. For more information, see [Flows](working-with-flows.md).

To learn more about chatting with agents, see [Using AWS Quick chat](https://docs.aws.amazon.com/quicksuite/latest/userguide/using-quick-chat.html).

## Multi-agent orchestration
<a name="multi-agent-orchestration"></a>

Multi-agent orchestration lets an agent delegate tasks to other agents and bring their results back into the same conversation. Each specialist agent uses its own instructions, knowledge, and memory. When an agent hands off work, the receiving agent uses its own instructions, knowledge, and memory, and works within your access. You can see the hand-offs, follow progress, and review the full response.

**To configure delegation**

1. Open the main agent's editor.

1. In the **Instructions** field, enter @ and choose each agent that this agent can hand work to. You can add up to 20 agents.

1. Describe when to use each agent.

1. Publish the agent.

You can add only published agents that you have access to.

The following limits apply to hand-offs:
+ An agent that receives a task can't hand it to another agent.
+ An agent that runs on a routine can't hand off work to other agents.

If delegation doesn't work as you expect, check the following messages:

A mentioned agent wasn't added  
The agent is deleted, unpublished, inactive, or not shared with you.

This agent's delegation is turned off  
The owner turned off hand-offs for the agent.