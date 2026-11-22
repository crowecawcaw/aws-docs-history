

# Managed agents

Managed agents are the agents that AWS DevOps Agent provides and maintains for you. They power the platform's built-in capabilities, such as answering questions in chat, running incident investigations, reviewing releases, and learning your environment. Unlike [custom agents](working-with-devops-agent-custom-agents-index.md), which you define and configure yourself, managed agents are owned by the platform: you do not create, delete, or run them directly, and their tools and skills are managed for you.

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
+ **Learning** - Production, refresh, and upkeep of managed memories, from topology understanding and monitor root causes to the knowledge graph that links memories.

## Managed agent page
<a name="managed-agent-page"></a>

A managed agent's page has an **Agent definition** tab and a **Knowledge** tab. The learning agent also has a **History** tab and a **Triggers** tab. The Incident RCA and Incident mitigation agents also have a **Dashboard** tab. A managed agent is platform-owned, so its page has no **Run now** control and no editable system prompt. Its header shows the agent name, a **Managed** badge, a **Preview** badge, and an **Active** status.

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

The learning agent also has a **Triggers** tab that lists its scheduled tasks, each with a description and the last time it ran. Choose a task to see when it runs. These tasks are platform-owned, so you cannot create, change, or delete them. For what each task does, see [How memory is built and refreshed](devops-agent-memories-managed-memories.html#learning-tasks).

### Dashboard tab
<a name="dashboard-tab"></a>

The Incident RCA and Incident mitigation agents each have a **Dashboard** tab. The Dashboard shows how the agent is performing in your Agent Space. Choose **Summary** to see the numbers for one time window. Choose **Trend** to see how the numbers change over time. To print the Dashboard, choose **Print**.

The Dashboard is made up of blocks. Each block shows one measure, such as **Investigations** or **Cause found**. Most blocks read the vended Amazon CloudWatch metrics for your Agent Space. **Running now**, **Human feedback**, **Agreement summary**, and **Investigation gaps** read your Agent Space's investigations and feedback instead.

The vended metrics start on a fixed date. When a window starts before that date, every block counts from that date instead. A note on the Dashboard shows the date.

#### Using the Summary view
<a name="using-the-summary-view"></a>

The **Summary** view shows the agent's numbers for one time window. By default, it shows the last 7 days. To change the window, choose **7d**, **1d**, **12h**, or **3h**. For example, **12h** shows the latest 12 hours, up to the current minute. The window's start and end times appear next to these controls.

To show times on your local clock, choose **Local**. To show them in Coordinated Universal Time (UTC), choose **UTC**. The default is **Local**. Your clock choice also applies when you enter a custom window.

#### Setting a custom window
<a name="setting-a-custom-window"></a>

A custom window sets the Dashboard to one specific period, such as the span of an incident.

To set a custom window, complete the following steps:

1. On the agent's **Dashboard** tab, in the **Summary** view, choose the calendar icon for **Custom window**.

1. Under **From**, enter the start date and time.

1. Under **To**, enter the end date and time.

1. Choose **Apply**.

The Dashboard applies the following rules to a custom window:
+ The window can start up to 60 days ago. For an earlier start, the Dashboard asks you to use the **Trend** view instead.
+ A window that starts 14 days ago or earlier uses 5-minute steps. The Dashboard moves its start back and its end forward to the nearest 5-minute mark.
+ An end later than the current time becomes the current time.

To leave a custom window, choose **Clear**. You can also choose one of the preset windows, such as **7d**.

#### Using the Trend view
<a name="using-the-trend-view"></a>

The **Trend** view plots the agent's numbers over a span of complete days. To change the span, choose **7d**, **30d**, **3mo**, or **6mo**. The default is **7d**.

Trend divides each span into buckets of equal length. The following table shows each span's bucket size, number of buckets, and how long after the vended metrics start it becomes available.


| Span | Bucket size | Buckets | Available after | 
| --- | --- | --- | --- | 
| 7d | 1 day | 7 | 2 days | 
| 30d | 3 days | 10 | 6 days | 
| 3mo | 7 days | 13 | 14 days | 
| 6mo | 14 days | 13 | 28 days | 

Trend uses complete days in UTC. That way, every bucket is a whole period with the same boundaries for everyone. For the same reason, Trend excludes the current day until it ends. If a span starts before the vended metrics start, Trend starts at the first complete bucket after that date.

A span becomes available after the vended metrics cover two of its complete buckets. Until then, the span appears dimmed. Each span becomes available on its own, so you don't need to change any configuration.

Some numbers also show the change compared with the previous span of the same length. The previous span's value appears with the change. A change in a count is a percentage. A change in a rate is in percentage points (pp). A change in a time appears as faster or slower. No change appears when there's no comparable earlier period. **Human feedback** and **Graded** show counts for each bucket. They don't show a change.

#### Reading the Incident RCA blocks
<a name="reading-the-incident-rca-blocks"></a>

The Incident RCA agent's **Summary** view shows the following blocks:
+ **Investigations** – The number of investigations that ended in the window. If the window ends at the current time, it also includes the investigations running now.
+ **Cause found** – The percentage of completed investigations that found a cause. The counts behind the percentage appear below it.
+ **Time to first cause** – The median (p50) time that investigations took to report their first cause. Only the investigations that reported a cause count toward it.
+ **Outcome** – A bar that shows how the investigations ended: **Completed**, **Failed**, **Timed out**, or **Canceled**. If the window ends at the current time, the bar also shows **Running now**. **Running now** counts the investigations that are queued or in progress.
+ **Human feedback** – **Investigations rated** is the number of investigations that people rated in the window. **Judged correct** is the percentage of those that people marked correct.
+ **Graded** – The Grader's Reviews in the window, split into helpful and unhelpful.
+ **Agreement summary** – A grid that compares the Grader's grade with a person's verdict on the same investigation. Its rows show the Grader's grade, helpful or unhelpful. Its columns show whether a person judged the investigation correct or incorrect.
+ **Investigation gaps** – The things that the agent couldn't access, such as an AWS account or a code repository. Each row counts the investigations that encountered it. Select a row to see those investigations and the latest description of the gap.

To see the investigations that a cell in **Agreement summary** counts, select the cell. Each investigation opens on its **Review** tab.

**Human feedback**, **Graded**, and **Agreement summary** appear together under **Quality**. The **Trend** view for Incident RCA plots **Cause found**, **Time to first cause (p50)**, **Human feedback**, and **Graded**.

For more information about Reviews, see [Reviewing investigations](working-with-devops-agent-reviewing-investigations.md).

#### Reading the Incident mitigation blocks
<a name="reading-the-incident-mitigation-blocks"></a>

The Incident mitigation agent's **Summary** view shows the following blocks:
+ **Plans** – The number of investigations that completed with at least one mitigation plan. The number of investigations that completed appears below it.
+ **Time to first plan** – The median (p50) time that investigations took to produce their first mitigation plan. Only the investigations that reported a plan count toward it.
+ **Human feedback** – **Plans rated** is the number of investigations whose plan people rated in the window. **Judged appropriate** is the percentage of those that people marked appropriate.

**Human feedback** appears under **Quality**. The **Trend** view for Incident mitigation plots **Plans**, **Time to first plan (p50)**, and **Human feedback**.

#### Understanding how blocks count
<a name="understanding-how-blocks-count"></a>

**Investigations**, **Cause found**, and **Outcome** count each investigation by when it ended. The following blocks count in other ways:
+ **Human feedback** – Counts investigations, not ratings. Each investigation counts once, based on its latest feedback in the window. A second rating replaces the first instead of adding to the count. Feedback counts by when someone gave it, even if the investigation ended earlier.
+ **Plans** – Shows a count, not a percentage. It appears with the number of investigations that completed. Only **Cause found** shows a share of completed investigations.
+ **Graded** – Counts the Grader's Reviews, not the investigations that it graded. A regrade counts again. A Review in the window can grade an investigation that ended before the window.
+ **Investigation gaps** – The block counts only the investigations that both started and ended inside the window. It excludes an investigation that started before the window, even if it ended inside it.
+ **Agreement summary** – Covers only the Reviews that both started and finished inside the window. The investigation that a Review graded can be from before the window. Each investigation counts once, based on its latest Review in the window. The block compares that Review with the latest verdict that a person gave, whenever they gave it. The grid shows only the investigations that a person marked correct or incorrect.

When a window holds more data than a block can read, a note on the block says which part its counts cover.

For more information about giving feedback, see [Autonomous incident response](production-operations-autonomous-incident-response.md).

#### Resolving Not measured blocks
<a name="resolving-not-measured-blocks"></a>

When a block can't read its data, it shows **Not measured** instead of a zero. The message on the block gives one of the following reasons:
+ The window ends before the vended metrics start. Choose a window that ends on or after the start date that the note on the Dashboard shows.
+ Your account has no `AWSServiceRoleForAIDevOps` service-linked role. AWS DevOps Agent reads the vended metrics through this role and creates it for you. However, if you created your Agent Space before March 13, 2026, you need to create the role yourself. For the steps, see [Manually create the service-linked role](configuring-integrations-and-knowledge-vended-logs-and-metrics.md#manually-create-service-linked-role-for-existing-customers).
+ The service-linked role exists but can't read your Agent Space's CloudWatch metrics yet. Check the role's permissions.
+ The metrics aren't available for a reason that the Dashboard doesn't recognize.
+ The Dashboard couldn't read the data. The message shows the error. To try again, reload the Dashboard.

For more information about the service-linked role, see [Vended Logs and Metrics](configuring-integrations-and-knowledge-vended-logs-and-metrics.md).

### Learning agent
<a name="learning-agent"></a>

The learning agent is the managed agent that produces most of the knowledge in your Agent Space. It learns from your cloud resources, code, pipelines, and observability integrations, and from your past investigations, chat sessions, investigation feedback, and resolved tickets. It keeps what it learns current as managed memories. It produces:
+ **[Agent Space understanding](devops-agent-memories-managed-memories.html#build-agent-space-understanding) :** A map of your architecture, environments, components, and critical request paths.
+ **[Monitor root causes](devops-agent-memories-managed-memories.html#learn-monitor-root-causes) :** The recurring root causes of each alarm, checked against the causes your operators record on tickets.
+ **[Memory dreaming](devops-agent-memories-managed-memories.html#run-memory-dreaming) :** A review of how agents used each memory, which merges duplicates, resolves conflicts, and removes outdated claims.
+ **[Knowledge graph](devops-agent-memories-managed-memories.html#build-knowledge-graph) :** Links between related memories, so agents can follow one memory to the next.
+ **[Tool-use best practices](devops-agent-memories-managed-memories.html#learn-tool-use-best-practices) :** How to use its tools well, learned from your investigations and, separately, from your chat sessions.
+ **[Reflections](devops-agent-memories-managed-memories.html#reflect-on-investigation-feedback) :** Lessons from investigations that your feedback showed were wrong.
+ **[Pipeline topology](devops-agent-memories-managed-memories.html#map-pipeline-topology) :** How your changes move through your pipelines to production.
+ **[Service dependencies](devops-agent-memories-managed-memories.html#map-service-dependencies) :** Which services and packages depend on one another.

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
+ **Directives** - Standing preferences and instructions you create through chat. The learning agent reads your directives and uses them to steer how it regenerates knowledge. For more information, see [directives](devops-agent-memories-managed-memories.html#directives).
+ **Refreshing a skill** - You can ask the learning agent to regenerate a managed skill from the skill's page. For more information, see [Learned Skills](devops-agent-skills-learned-skills.md).

For more information about the knowledge the learning agent produces, see [Managed memories](devops-agent-memories-managed-memories.md).