

# Managed agents
<a name="working-with-devops-agent-managed-agents"></a>

Managed agents are the agents that AWS DevOps Agent provides and maintains for you. They power the platform's built-in capabilities, such as answering questions in chat, running incident investigations, reviewing releases, and learning your environment. Unlike [Custom Agents](working-with-devops-agent-custom-agents-index.md), which you define and configure yourself, managed agents are owned by the platform: you do not create, delete, or run them directly, and their tools and skills are managed for you.

Managed agents appear in the **Managed agents** section of the **Agents** page in your Agent Space Operator Web App, alongside the **Custom agents** section. Each managed agent has its own page, giving you the same visibility into a managed agent that you already have into a custom agent: what the agent does, the instructions it runs with, and a history of what it has done.

**Note:** Managed agent pages are a preview feature and might change. The managed agents shown in your Agent Space depend on the capabilities you have enabled.

## Viewing managed agents
<a name="viewing-managed-agents"></a>

View your managed agents to see what each one does, the instructions it runs with, and its run history.

**To view your managed agents:**

1. On the **Agents** page in your Agent Space Operator Web App, scroll to the **Managed agents** section.

1. Choose a managed agent to open its page.

The managed agents available in your Agent Space can include:
+ **Chat** - Ad-hoc questions and requests during chat sessions.
+ **Incident triage** - Alarm filtering, severity classification, and initial scoping.
+ **Incident RCA** - Root cause analysis with evidence collection and validation.
+ **Incident mitigation** - Short-term remediation and long-term fix recommendations.
+ **Incident UI** - Generation of an investigation's outputs, including those posted to other platforms, through the user interface (UI).
+ **Evaluation** - Agent performance scoring and policy compliance checks.
+ **Grader** - Quality assessment of a completed investigation. This is the agent behind a Review. For more information, see [Reviewing investigations](working-with-devops-agent-reviewing-investigations.md).
+ **Release testing** - Automated UI and API testing against deployed web applications and REST APIs.
+ **Learning** - Production and refresh of managed knowledge, covering monitor memories and topology understanding.

## Managed agent page
<a name="managed-agent-page"></a>

A managed agent's page has an **Agent definition** tab and a **Knowledge** tab. The learning agent also has a **History** tab and a **Triggers** tab. A managed agent is platform-owned, so its page has no **Run now** control and no editable system prompt. Its header shows the agent name, a **Managed** badge, a **Preview** badge, and an **Active** status.

### Agent definition tab
<a name="agent-definition-tab"></a>

The **Agent definition** tab shows the agent's instructions, stored as AGENTS.md files. It contains two sections:
+ **Global instructions (AGENTS.md)** - Shared across all managed agents. Every agent session in your Agent Space receives this content in addition to its own agent-specific instructions. Because a change here affects every managed agent, saving global instructions asks you to confirm first.
+ **Agent instructions (AGENTS.md)** - Owned by the managed agent whose page you are on. Only sessions of that agent receive this content.

Both sections are editable in place. Each shows a version number and the date it was last edited, and each provides **Preview** and **Code** views, along with upload, download, and delete controls. For a full description of how agent instructions work, their size limits, and scoping, see [Agent instructions](about-aws-devops-agent-agent-instructions.md).

**Important:** Agent instructions were previously managed on the **Instructions** tab of the **Knowledge** page. That tab now shows a notice pointing to the **Agents** page, where you set instructions on each managed agent's **Agent definition** tab.

### Knowledge tab
<a name="knowledge-tab"></a>

The **Knowledge** tab shows the skills and memory stores the agent can read, in two sections: **Skills** and **Memories**. Each entry links to its detail page, and a badge marks whether the platform manages it or you added it. This view is read-only.

### History tab
<a name="history-tab"></a>

The **History** tab shows a record of the learning agent's past runs. It lists each run with its status, title, start time, and last update, and you can open a run to see its trajectory.

Only the learning agent has a History tab. The other managed agents, including the incident agents (Incident triage, Incident RCA, Incident mitigation, and Incident UI), run as part of an investigation rather than as standalone runs, so their pages do not include a History tab. For incident activity, see [Autonomous incident response](production-operations-autonomous-incident-response.md).

### Triggers tab
<a name="triggers-tab"></a>

The learning agent also has a **Triggers** tab that lists its scheduled tasks, each with a description and the last time it ran. Choose a task to see when it runs. These tasks are platform-owned, so you cannot create, change, or delete them.

### Learning agent
<a name="learning-agent"></a>

The learning agent is the managed agent that produces most of the knowledge in your Agent Space. It reviews your Agent Space's topology, code dependencies, pipeline structure, and past investigations, and from that it generates and refreshes managed knowledge on a schedule or on demand. What it produces includes:
+ **Monitor memories** - Historical investigation memories, organized by the monitor that triggered them.
+ **Topology understanding** - A structured map of your application architecture, environments, and components that other agents read during investigations.

Downstream agents, such as the incident agents and chat, read this knowledge to navigate your environment during their work.

#### Viewing the learning agent
<a name="viewing-the-learning-agent"></a>

The learning agent appears in the **Managed agents** section of your Agent Space. Open it to see:
+ **Agent definition** - The global instructions and the learning agent's own instructions it runs with.
+ **Knowledge** - The skills and memory stores the learning agent can read.
+ **History** - A list of the learning agent's runs. Open a run to see the trajectory of what it reviewed and produced.
+ **Triggers** - The learning agent's scheduled tasks and the last time each one ran.

#### Influencing what the learning agent produces
<a name="influencing-what-the-learning-agent-produces"></a>

You influence the learning agent's output through directives and by refreshing a managed skill:
+ **Directives** - Standing preferences and instructions you create through chat. The learning agent reads your directives and uses them to steer how it regenerates knowledge. For more information, see [DevOps Agent Memories](about-aws-devops-agent-devops-agent-memories.md).
+ **Refreshing a skill** - You can ask the learning agent to regenerate a managed skill from the skill's page. For more information, see [Learned Skills](about-aws-devops-agent-learned-skills.md).

For more information about the knowledge the learning agent produces, see [DevOps Agent Memories](about-aws-devops-agent-devops-agent-memories.md) and [Learned Skills](about-aws-devops-agent-learned-skills.md).