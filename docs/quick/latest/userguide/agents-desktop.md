

# Agents
<a name="agents-desktop"></a>

Agents are configurable AIs in Amazon Quick. You give each one its own instructions, knowledge sources, and tools so it can answer questions and get work done for you. Quick is the built-in agent, and you can also build your own or install ones shared with you. Each agent can work with you in chat or run on its own on a routine. Agents can only access the same resources and services that you have access to, and you control what each agent is allowed to do.

Users can browse agents that are shared with them on the Agents page by choosing **Browse all**. This view presents available agents in a read-only detail view along with the description and knowledge sources each one uses. From this view, you can install an agent to add it to your agent list. Once installed, an agent is ready to use anywhere you work: you can chat with it, @ mention it inline in any conversation, and run it on a routine, and it appears in your agent switcher for quick access. From the Agents page, you can favorite an agent for easy access or set an agent as your default. A published agent can also be accessed from Quick on the web.

## Creating an agent
<a name="desktop-creating-an-agent"></a>

You can create an agent through the interface or through natural language. To create an agent through natural language, enter "I want to create an agent" in the conversation.

**To create an agent**

1. Choose **Customize** in the navigation, and then choose the **Agents** tab.

1. Choose **Create**, and then choose **From chat** (or say "create an agent" in chat). To import an existing agent definition, choose **From file** instead.

1. Describe what you want the agent to do in natural language.

1. Quick generates a draft configuration including name, description, and instructions.

1. Review and refine the configuration through conversation or by editing fields directly.

1. Publish the agent when you are ready. Agents cannot be shared with other users until published. Agents are private unless shared explicitly.

You can attach reference documents during creation to provide additional context. You can also start editing an agent by mentioning it with an at-sign in chat, which opens the agent editor in a session tab.

## Agent configuration
<a name="desktop-agent-configuration"></a>

The agent editor organizes configuration into two tabs.

**Instructions tab**: set the agent's Name, Description, and Instructions. Instructions support rich formatting (headings, lists, emphasis, code, and quotes) and a welcome message with starter prompts. Instructions can be up to 50,000 characters.

The Capabilities tab has these fields.


| Capability | Description | 
| --- | --- | 
| Web search | Toggle to allow the agent to search the web. | 
| Skills | The skills the agent can use. By default an agent can use all skills; if you add specific skills, the agent is limited to those. Remove them to re-enable all skills. | 
| Spaces | Connected data sources the agent reads from. | 
| Connections | Connectors and the tools that the agent can be configured to use. | 

## Using an agent
<a name="desktop-using-an-agent"></a>

Use one of the following ways to use your agent.
+ **Agent switcher**: choose an agent at the top of chat to start a conversation with it.
+ **At-mention**: mention an agent by name in any chat to invoke it inline.
+ **Chat button**: start a new conversation from an agent's landing page.
+ **Run it on a routine**: pair the agent with a routine to run on a recurring basis without prompting. Routines run in the cloud, so they keep running even when your laptop is closed or offline. The agent stores deliverables in its **Agent Files** and surfaces results on its **Agent briefing** page (when briefing is turned on) and **Mission Control** activity page.

You ask questions and get responses shaped by the agent's instructions and connected data sources, applications, and skills. Have it perform tasks using its configured tools and connections.

## Monitoring agents
<a name="desktop-monitoring-agents"></a>

You can monitor agent activity in two places.
+ **Agent landing page**: the agent's overall page, with Overview (including an AI-generated agent briefing), Activities, Agent Files, and Settings tabs. View a specific agent's runs, approvals, routines, and deliverables.
+ **Mission Control**: a centralized command center that gives you visibility across all your agents in one place. Monitor all agent activity, unblock agents that need input, view running agents, manage routines, and track KPIs, without switching between individual agent pages. For more information, see [Mission Control](mission-control-desktop.md). Access Mission Control from the icon in the top-right navigation bar.

### Agent landing page
<a name="desktop-agent-landing-page"></a>

Each agent has a landing page with four tabs.


| Tab | Description | 
| --- | --- | 
| Overview | Summary of the agent's purpose, items needing your input, and an AI-generated agent briefing. | 
| Activities | Activity log with filter tabs: All, Needs input, Running, and Routines. | 
| Agent Files | Persistent file storage: artifacts and deliverables the agent has produced across runs. | 
| Settings | Agent preferences, such as automatic briefing updates. Instructions and capabilities are edited from Configuration, not here. | 

The Overview tab includes the following sections.
+ **Needs input**: when the agent pauses on an action that requires your decision, an approval card appears. Each card shows a description of the proposed action with **Approve** and **Deny** buttons.
+ **Agent briefing**: an AI-generated summary of the agent's work (for example, top findings, trend analysis, or status dashboards). It updates after each run and can be regenerated on demand.

The Activities tab shows past and current agent work. You can filter the view using the following sub-tabs.
+ **All**: shows all activities in reverse chronological order. Each entry includes a title, summary, agent name, and timestamp.
+ **Needs input**: items where the agent paused and is waiting for your decision. Each item shows **Approve** and **Deny** buttons.
+ **Running**: tasks in progress.
+ **Routines**: lists the agent's configured routines. Time-based routines (schedules), for example, "Every Monday at 9 AM" or "Every weekday at 8:30 AM," are supported on the desktop today. Each routine has a play button to trigger a run and a toggle to turn it on or off. Choose **Create** to add a new routine.

Activities can include file attachments (for example, drafted documents or reports) that you can open and review.

### Run status
<a name="desktop-agent-run-status"></a>

Each run shows its current status. A run is Running while it is in progress, and Needs input when it has finished or paused with one or more actions awaiting your decision. Once a run ends, it is Completed if it finished with no issues, Interrupted if it was stopped before completing, or Failed if it ended with an error. An agent that has not run yet shows No runs yet. On the Agents list, the Status column summarizes each agent's most recent run, so these finished states appear there as "Last run completed," "Last run interrupted," or "Last run failed."

## Managing agents
<a name="desktop-managing-agents"></a>

Agents are versioned. You work on a draft, add release notes that are shown to your team on publish, and then publish. You can manage versions and discard a draft. Agents cannot be shared with other users until published, and a routine always runs the published version.

From an agent's menu you can **make it your default**, so Quick uses it for every new chat until you pick another, as well as **share** it, **export** its configuration to a JSON file, **duplicate** it, **manage its versions** (switch between the published and draft versions), **manage its routines** (the routines that run it on its own), **uninstall** it, or **delete** it. Uninstall removes the agent from your list only; it stays available to everyone else it is shared with. Delete removes an agent you own for everyone. The Agents list supports search, filtering (including by status and version), sorting (including by last run and last modified), favoriting, and list or grid views. The list shows each agent's description, last-modified time, and run status.

For others to use your agent's connected sources, you must share those with the intended recipients. Otherwise, they will only get responses from the sources they have access to. You do not need to share all underlying resources.