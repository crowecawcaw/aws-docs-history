

# Skills and agents
<a name="skills-and-agents-desktop"></a>

The Amazon Quick desktop application supports skills and scheduled tasks that extend what Quick can do on your behalf. Skills are modular instruction sets that equip Quick with specialized capabilities, and scheduled tasks execute automatically on a recurring basis.

## Skills
<a name="sad-desktop-skills"></a>

A skill is a self-contained instruction set that Quick loads on demand to perform a specific type of task. Each skill includes a name, a description, detailed step-by-step instructions, and can optionally include attached tools and reference files. When you invoke a skill, Quick loads its instructions and tools into the active conversation, giving it the specialized knowledge and capabilities needed to complete the task.

Skills are more than simple prompt templates. A skill can define the following components.
+ **Instructions** – A structured `SKILL.md` file with detailed, multi-step workflows, validation criteria, and failure-handling guidance.
+ **Tools** – One or more callable tools that the skill makes available to Quick. For example, the Coding Agents (ACP) skill includes a `Send Message To Acp Agent` tool, and the Agent Management skill includes 17 tools for creating, updating, and managing scheduled tasks.
+ **Reference files** – Supporting documents, templates, or configuration files that the skill can access during execution.

### Built-in skills
<a name="sad-desktop-builtin-skills"></a>

Amazon Quick on desktop comes with built-in skills that are pre-installed and ready to use. Built-in skills cover capabilities such as document creation, web browsing, image generation, code execution, knowledge graph management, agent orchestration, and transcription. You can toggle built-in skills on or off as a group.

To view the full list of built-in skills, choose **Agents & skills** in the left navigation, choose the **Skills** tab, and scroll to **BUILT-IN SKILLS**.

### Creating a skill
<a name="sad-desktop-creating-skills"></a>

You can create custom skills in the Amazon Quick desktop application using one of the following methods.

**To create a skill with AI**  
Use the following procedure.

1. Choose **Agents & skills** in the left navigation, and then choose the **Skills** tab.

1. Choose **\+ Create**, and then choose **Create with AI**.

1. Describe the skill you want to create. Quick generates the skill instructions, selects appropriate tools, and creates the `SKILL.md` file.

1. Review and edit the generated skill before saving.

**To upload a skill file**  
Use the following procedure.

1. Choose **Agents & skills** in the left navigation, and then choose the **Skills** tab.

1. Choose **\+ Create**, and then choose **Import from file**.

1. Select a `SKILL.md` file from your local machine.

1. Review and edit the uploaded skill before saving.

Skills that you create appear under the **MY SKILLS** section in the Skills tab.

**Tip**  
When you complete a multi-step task successfully, Quick might offer to save the workflow as a reusable skill. This is a convenient way to capture effective workflows without writing instructions manually.

### Using a skill
<a name="sad-desktop-using-skills"></a>

You can use a skill in one of the following ways.
+ **By name** – Mention the skill by name in your chat message. For example, enter "use the Web Browser skill to check this page" or "create a presentation."
+ **Automatic selection** – Quick automatically detects when a skill is relevant to your request and loads it without you needing to ask. For example, if you ask Quick to create a PowerPoint file, the Presentations skill loads automatically.
+ **Run button** – In the Skills tab, choose a skill and then choose **Run** to start a conversation with the skill already loaded.

When a skill activates, its tools load automatically into the conversation. You can see which tools are available in the skill's detail view.

### Managing skills
<a name="sad-desktop-managing-skills"></a>

You can manage your skills from **Agents & skills** in the left navigation > **Skills** tab.
+ **Search** – Use the search bar to find skills by name or description.
+ **Toggle built-in skills** – Use the master toggle next to **BUILT-IN SKILLS** to enable or disable all built-in skills at once.
+ **View details** – Choose a skill to view its description, attached tools and files, and full instructions.
+ **Edit instructions** – Choose **Edit** in a skill's detail view to modify its instructions.
+ **Run** – Choose **Run** to start a new conversation with the skill pre-loaded.

The Skills tab also displays a **How skills work** guide at the top of the page with the following three steps.

1. **Create a skill** – Write instructions, attach tools, and add reference files. Each skill is a folder that Quick loads on demand.

1. **Invoke in chat** – Mention a skill by name or let Quick auto-select it. Tools load automatically when the skill activates.

1. **Iterate and refine** – Edit instructions, add sub-files for edge cases, or attach skills to scheduled tasks so they run on autopilot.

## Scheduled tasks
<a name="desktop-scheduled-agents"></a>

Scheduled tasks are automated tasks that run on a recurring schedule. You define what the agent does, when it runs, what capabilities it uses, and which response mode powers it. Quick runs the agent at the specified times and delivers the results to your activity feed.

### How scheduled tasks work
<a name="desktop-how-agents-work"></a>

Each scheduled task is configured with four components, accessible through tabs in the agent detail view.


| Tab | Description | 
| --- | --- | 
| Overview | Summary of the agent's type, source, schedule, capabilities, and model. | 
| Schedule | Configure when and how often the agent runs (for example, every 15 minutes, daily, weekly). | 
| Capabilities | Attach MCP servers to give the agent access to additional tools and data sources. | 
| Prompt | Define the agent's instructions — what it does each time it runs. | 

The Overview tab displays the following information.


| Field | Description | 
| --- | --- | 
| Type | The agent's category (for example, Feed). | 
| Source | Whether the agent is Built-in or custom. | 
| Schedule | How often the agent runs (for example, Every 15 min). | 
| Capabilities | The number of MCP servers attached to the agent. | 
| Response mode | The response mode the agent uses (Fast, Balanced, or Smart). | 

### Built-in agents
<a name="desktop-builtin-agents"></a>

Amazon Quick on desktop includes pre-configured agents that are ready to use. The following table describes the built-in agents.


| Agent | Schedule | Description | 
| --- | --- | --- | 
| Feed Agent | Every 15 minutes (default, configurable) | Processes items from your connected services (messaging, email, calendar) and populates the activity feed with prioritized, AI-summarized items and suggested actions. | 

Built-in agents are pre-configured with sensible defaults, but you can customize their schedule, capabilities, prompt, and model selection.

### Creating a scheduled agent
<a name="desktop-creating-agents"></a>

You can create a scheduled task using one of the following methods.

**To create an agent from Settings**  
Use the following procedure.

1. Open **Mission Control** from the top bar.

1. Choose **\+ Create** to define a new scheduled task.

1. Configure the agent's schedule, capabilities, prompt, and model.

1. Toggle the agent on when you're ready for it to start running.

**To create an agent from chat**  
You can ask Quick to create a scheduled task directly in chat. For example:
+ "Create an agent that checks my Slack channels every morning at 9 AM and summarizes what I missed."
+ "Set up a daily agent to monitor my inbox for urgent emails."

Quick creates the agent and adds it to your Scheduled Tasks.

### Agent controls
<a name="desktop-agent-controls"></a>

Each scheduled task provides the following controls.


| Control | Icon | Description | 
| --- | --- | --- | 
| Edit | Pencil | Open the agent configuration for editing. | 
| Run now | Play | Run the agent immediately, regardless of its schedule. | 
| Toggle | Switch | Turn the agent on or off. When off, the agent does not run at its scheduled times. | 

You can also select which response mode the agent uses. Choose from **Fast**, **Balanced**, or **Smart** based on the complexity of the agent's task and your preferences for speed versus quality.

### Accessing scheduled tasks
<a name="desktop-accessing-agents"></a>

You can access and manage your scheduled tasks from **Mission Control**, accessible from the top bar. Mission Control shows all your scheduled tasks with their schedule, status, and controls for editing, running, and toggling them on or off.

**Important**  
Scheduled tasks run locally on your computer. Your computer must be turned on and the Amazon Quick desktop application must be running for scheduled tasks to execute at their configured times. If your computer is off or the application is closed when an agent is scheduled to run, the agent does not run until the next scheduled time.

### Examples of scheduled tasks
<a name="desktop-agent-examples"></a>

The following are examples of scheduled tasks you can create.
+ **Morning brief** – Every morning at 8 AM, summarize unread Slack messages, new emails, and today's calendar events.
+ **Inbox triage** – Every 30 minutes, scan new emails and flag anything that needs urgent attention.
+ **Project monitor** – Daily at 5 PM, check a Slack channel for updates on a specific project and compile a summary.
+ **Meeting prep** – 15 minutes before each calendar meeting, gather relevant context from Slack, email, and files, and prepare a brief.
+ **Competitive monitor** – Weekly, search the web for news about specified companies and produce a summary report.