# Create, customize, and deploy AI-powered

chat agents in Amazon Quick Suite

Chat agents in Amazon Quick Suite help users explore data, analyze information, and take
actions. Users can interact with chat agents using the Quick Suite chat interface.
Chat agents provide assistance through open-ended conversations supported by specific goals,
sources of knowledge, and any connected tools. Chat agents can evolve from simple
question-answering interfaces to more advanced functions that orchestrate complex
workflows.

You can use chat agents to:

- Generate content and provide answers through natural language conversations
- Analyze and summarize information from connected spaces, dashboards, topics,
  datasets, and uploaded files
- Invoke actions to perform predefined steps for consistent, repeatable
  outcomes

###### Note

To learn more about chatting using chat agents, see [Using
Amazon Quick Suite chat](using-quick-chat.md "using-quick-chat.md").

###### Topics

- [Chat agent types](#agent-types "#agent-types")
- [Amazon Quick Suite user interaction with chat
  agents](#user-agent-actions "#user-agent-actions")
- [Amazon Quick Suite user permissions for chat
  agents](#user-agent-permissions "#user-agent-permissions")
- [Custom permissions for chat
  agents](#custom-permissions-chat-agents "#custom-permissions-chat-agents")
- [System chat agent](default-assistant.md "default-assistant.md")
- [Custom chat agents](custom-agents.md "custom-agents.md")
- [Chat agent context sources and
  best practices](agent-knowledge-sources-best-practices.md "agent-knowledge-sources-best-practices.md")
- [Use a chat agent](use-agents.md "use-agents.md")

## Chat agent types

Amazon Quick Suite supports two types of chat agents:

- **System chat agent** – This chat agent
  ("My assistant") is automatically available to all users by default. The system
  chat agent serves as a base planner with no inherent data or actions of its
  own—it dynamically accesses resources available to each user during chat
  time, allowing it to be tailored to individual user permissions and available
  content. Admin users control system chat agent settings by assigning specific
  users as owners so they can customize its persona and other settings.

The system chat agent is enabled with all chat capabilities, including file
upload functionality, LLM knowledge access, toxicity and other guardrails, web
search. It also includes chat data scoping mechanisms that provide access to
spaces, topics, dashboards, knowledge bases, and actions based on user
permissions.

- **Custom chat agents** – These chat agents
  can be created and customized to specific use cases by users with chat agent
  creation capabilities in Amazon Quick Suite, and shared with anyone. Admins can choose
  to restrict specific users and groups from creating custom chat agents, while
  still allowing users to use chat agents via chat. Chat agents return responses
  scoped to content that their invoking users have permissions to.

Custom chat agents can interact with Amazon Quick Suite resources in the following
ways:

- **Preconfigured with resources** – These
  chat agents use only the configured resources (for example, spaces as knowledge
  sources, action connectors as tools) when looking for answers or orchestrating
  actions as their defeault behavior. While chatting, users can attach additional
  resources as per their need or invoke actions directly. For example, chat agents
  configured with only spaces containing files can't take actions by default
  unless users explicitly invoke them. Similarly, chat agents configured with only
  actions rely on LLM knowledge unless users attach a space or dashboard for
  enterprise-specific answers. However, users may attach additional spaces or
  directly invoke other actions they may have access to within the chat
  interface.
- **Not opinionated at build time** – These
  chat agents are not initially configured with resources when they are built
  (spaces, or action connectors, or both). Chat determines the resource boundary
  for the chat agent. For example, if no space is configured for the chat agent,
  chat will default to all spaces or LLM knowledge until the user makes a change.
  If no action connectors are configured for the chat agent, during chat, all
  actions a user has access to will be available to the agent until user makes a
  resource selection that doesn't include actions.

User resource selection during chat affects chat agent behavior. If a user
selects a space, the chat agent will only answer with data within that space and
take actions available within that space (if it is not opinionated at build
time). If a user selects a dashboard, topic, or knowledge base, the chat agent
will only answer from that source and not take any actions since the focus is
changed to a specific data source. Users are expected to select all relevant
resources within chat for comprehensive assistance.

###### Note

The system chat agent is an unopinionated chat agent by design. If you
want chat agents to access all actions irrespective of data focus, configure
chat agents with action connectors.

## Amazon Quick Suite user interaction with chat

agents

The following table shows what you can do with chat agents in the admin console versus
as a Amazon Quick Suite user. For more information on which roles can access these features,
refer to the [Amazon Quick Suite
pricing](https://aws.amazon.com/quicksuite/pricing/ "https://aws.amazon.com/quicksuite/pricing/") document.

| Access Level            | Capabilities                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Admin Console           | • Assign owners for the system chat agent and custom chat<br>chat agents using [Manage assets](manage-qs-assets.md "manage-qs-assets.md")<br>• Control whether users can create chat agents using [Custom permissions](create-custom-permisions-profile.md "create-custom-permisions-profile.md")<br>• Configure instance-wide blocked words and phrases for all<br>chat agents                                                                                                                                                                                                         |
| Amazon Quick Suite user | • Create and maintain custom chat agents (with appropriate<br>permissions)<br>• Configure chat agent personality and response styles and<br>provide reference documents to inform its behavior<br>• Link chat agents with spaces (with dashboards, datasets,<br>topics) as their knowledge source to look for answers<br>• Attach action connectors to use as tools<br>• Share chat agents with specific users and teams<br>• Interact with chat agents through conversations<br>• Analyze data with chat agent assistance<br>• Receive permissions-aware responses from chat<br>agents |

## Amazon Quick Suite user permissions for chat

agents

What you can do with a chat agent also depends on the permissions you're assigned for
it. There are two permission types that users can be assigned:

- **Owner** – Owners can edit, share, and
  delete the chat agent.
- **Viewer** – Viewers can view and use the
  chat agent.

###### Note

If you don't have access to a linked resource as either a viewer or owner,
resources added to the chat agent by another owner appear as "Resource unavailable".
You can delete these resources as an owner, but you cannot list or add them because
resource-level sharing is required.

Quick Suite admins must give users the permission to create chat agents. For
information on which roles can create chat agents, refer to the [Amazon Quick Suite pricing](https://aws.amazon.com/quicksuite/pricing/ "https://aws.amazon.com/quicksuite/pricing/")
documentation. For information on how to provide access to these features, see [Custom permissions](create-custom-permisions-profile.md "create-custom-permisions-profile.md") in the Quick Suite Admin
Guide.

The following table outlines how user permissions determine what you can do with a
Amazon Quick Suite chat agent:

| Permissions type | Permissions                                                                                                                                                                                                                                                                                                                            |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Owners           | • Can access and configure agent behavior (agent persona<br>settings, reference documents) and resources (space and<br>action connectors)<br>• Can customize chat agent details like title, description,<br>and suggested prompts to improve usability<br>• Can share chat agents with users and groups<br>• Can delete the chat agent |
| Viewers          | • Can't customize the chat agent's details<br>• Can receive responses based on the permissions they have<br>to resources                                                                                                                                                                                                               |

## Custom permissions for chat

agents

By default, Amazon Quick Suite enables all new features available for the Amazon Quick Suite
account, so that users can access them immediately based on their subscription. You can
use [custom permissions](create-custom-permisions-profile.md "create-custom-permisions-profile.md") to restrict specific features. As an
admin, when you create a custom permissions profile, you can create two types of
restrictions for chat agents:

- You can completely disable all chat agent functionality for users, including
  chatting with the default agent, chatting with custom agents, and creating new
  agents. This can be done by restricting the **Chat agent**
  capability.
- You can also specifically restrict the ability to create agents without
  impacting chat with agents. This can be done by creating a custom permission
  profile and restricting only the feature **Create chat
  agents**.

###### Note

If you want your users to be able to chat using the system agent but don't want
them to create chat agents, restrict their chat agent creation abilities
only.

Agent permissions in Amazon Quick Suite can be configured in various combinations to meet
your organization's needs. To help you understand how to configure permissions, the
following section provides a use-case driven approach that groups common
scenarios:

| Use case scenario                                                                                                 | What users can do                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Agent with all capabilities**(No<br>restrictions on chat agents, spaces, knowledge bases, actions, or<br>flows) | • Chat with all default and custom chat agents<br>• Create and customize new chat agents<br>• Connect chat agents to spaces, knowledge bases, and<br>actions<br>• Trigger flows from the chat window from existing<br>conversation with a chat agent<br>• Share chat agents with other users<br>• Use all chat features and integrations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Chat-only access to<br>agents**(Agent capabilities enabled, but chat agent<br>creation restricted)              | • Chat with existing default and shared custom chat<br>agents<br>• Can't create new custom chat agents<br>• Can't edit or update custom chat agents<br>• Full access to chat interface and chat agent<br>library                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Limited access to other<br>capabilities**(Chat agents enabled, but specific<br>capabilities restricted)         | • Chat with system and custom agents but with reduced<br>functionality<br>• Can't attach knowledge bases, spaces, or actions to an<br>agent's configuration, or select these resources during<br>chat<br>• If spaces restricted: Agents configured with spaces will<br>fall back to LLM knowledge only. Users can't view or select<br>spaces in the chat resource selector<br>• If knowledge bases restricted: Users can't select<br>knowledge bases to use in chat. Any knowledge bases present<br>in spaces either attached to the agent or selected by user<br>during chat won't be used to generate responses<br>• If actions restricted: Users can't attach actions to<br>agents or invoke actions from chat. Any actions<br>preconfigured with agents won't be used to execute<br>tasks<br>• If flows restricted: Chat won't show flows anymore, so<br>users can't invoke flows while chatting with an agent |
| **No chat agent access**(Agent<br>capabilities completely restricted)                                             | • Can't view or access any chat agents<br>• Agent library and navigation are hidden<br>• Can still access and create other Amazon Quick Suite resources,<br>such as creating spaces for file sharing with teams or flows<br>for structured interactions (as long as those capabilities<br>are not also restricted)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
