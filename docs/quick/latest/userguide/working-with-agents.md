

# Agents in AWS Quick

Agents are configurable AIs in AWS Quick. You give each agent its own instructions, knowledge sources, and tools so it can answer questions and get work done for you. You can use agents on the web and in the desktop app. Your agents, conversations, and routines are available across both.

Quick is the system agent provided with AWS Quick. You can also create your own agents, or install agents that others share with you. Each agent maintains memory of its own work. For more information, see [Memory and response personalization](using-quick-chat.md#chat-memory).

Agents can access only the content and actions that you have access to. Two people who use the same agent can get different answers if they have access to different content.

**Note**  
To learn more about chatting with agents, see [Using AWS Quick chat](https://docs.aws.amazon.com/quicksuite/latest/userguide/using-quick-chat.html).

**Topics**
+ [The Quick system agent](#default-assistant)
+ [The default agent](#default-agent)
+ [Create and configure agents](custom-agents.md)
+ [Use agents](use-agents.md)
+ [Share and manage agents](share-manage-agents.md)
+ [Monitor agents](monitor-agents.md)

To run an agent on a schedule, see [Routines](working-with-routines.md).

**Note**  
Embedding applies to legacy chat agents only. For more information, see [Embed chat agents (legacy)](embed-chat-agents.md).

## The Quick system agent
<a name="default-assistant"></a>

Quick is available to every user. It doesn't include preconfigured knowledge sources. Instead, it works with the content and actions you can access. Quick includes the following:
+ A default professional persona.
+ File upload.
+ General knowledge from the underlying AI model.
+ Guardrails set by your administrator.
+ Web search, when your administrator allows it.
+ Access to spaces, dashboards, topics, knowledge bases, and actions, based on your permissions.

Administrators can assign owners who customize the Quick system agent. For more information, see [Admin controls for agents](share-manage-agents.md#admin-controls-agents).

## The default agent
<a name="default-agent"></a>

The default agent is the agent used for new chats. Quick is the default agent unless a different agent is selected. Your organization can choose a different agent as the default for its users. You can also choose your own default agent. Choosing a different default agent doesn't change the Quick system agent. For more information, see [Make an agent a favorite or your default](use-agents.md#make-agent-default).