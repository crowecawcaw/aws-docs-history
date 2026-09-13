

# Mission Control
<a name="mission-control-desktop"></a>

Mission Control is a centralized command center in the Amazon Quick desktop application that gives you full visibility and management over all your agents in one place. You monitor agent activity, review outputs, manage routines, and track performance metrics, so you do not need to check on agents individually.

## Why use Mission Control
<a name="mission-control-why"></a>

As you scale your use of agents with background tasks and automated workflows, keeping track of everything becomes complex. Mission Control provides these benefits.
+ Centralized visibility: view all agent activity without switching between conversations or agents.
+ Faster unblocking: agents that need your input are surfaced clearly, so you respond quickly.
+ Operational awareness: key performance indicators (KPIs) and run history confirm your agents are working correctly.
+ Efficiency at scale: whether you have 2 agents or 20, Mission Control keeps you in control.

## Capabilities
<a name="mission-control-capabilities"></a>

Mission Control provides these capabilities for managing your agents.


| Capability | Description | 
| --- | --- | 
| Monitor all agent activity | View a unified list of what every agent has done across all runs. | 
| Filter by agent name | Drill into a specific agent's history and access its outputs. | 
| Unblock agents | Filter on agents that need your input and provide it directly. | 
| View running agents | See which agents are currently active and monitor their progress. | 
| Manage routines | View and edit routines for all agents in one place. | 
| Track KPIs | Understand error rates, active agents, completed tasks, and total runs. | 
| View creator analytics | See insights on how your shared agents and apps are being adopted. | 

## Routines
<a name="mission-control-routines"></a>

The desktop application runs your agents automatically through routines. A schedule, an agent that runs at recurring times, is the first routine type. You define what the agent does, when it runs, its capabilities, and its response mode. Quick delivers each run to your feed or a connected app. Schedules are currently the available routine type.

You configure a routine in a modal with two tabs: Overview and Activity.

The Overview tab has these fields.


| Field | Description | 
| --- | --- | 
| Repeats | How often the routine runs (for example, daily) and the time of day it runs. | 
| Custom time range | Optionally set a start date and time, an end date and time, and a time zone that bound when the routine is active. | 
| Triggers | Select the agent that you want to run when the routine starts. | 
| Uses | The capabilities, such as MCP servers and tools, the routine can use. Choose \+ Add to attach more. | 
| Instructions | What the agent should accomplish each time the routine runs. | 
| Model details | Expand to configure the model, thinking effort, memory, and sub-task settings for the routine. | 

Expand Model details to configure these options.
+ Model: choose Fast, Balanced, or Smart.
+ Thinking effort: have the agent apply additional reasoning before responding.
+ Include memory: allow the agent to use profile and search tools.
+ Allow spawning sub-tasks: let the agent break work into parallel sub-tasks.

The Activity tab shows the run history for the routine. From the modal, you can also enable or disable the routine, run it immediately, edit it with chat, and choose Done to save.

Quick includes pre-configured routines, such as a feed agent that processes items from your connected services and populates the activity feed. You customize a built-in routine's cadence, capabilities, instructions, and model.

**To create a routine**

1. Open Mission Control from the top bar.

1. Choose Create to define a new routine.

1. Configure how often it repeats, its capabilities, instructions, and model.

1. Turn it on when you are ready for it to run.

You can also ask Quick in chat to create a routine. For example, "check my channels every morning at 9 AM and summarize what I missed."

Routines run in the cloud, so they run at their configured time even when the desktop application is closed or your computer is off. The exception is a run that needs a local tool, such as reading a file on your machine, browser automation, or local code execution. For those steps, your computer must be on with the desktop application running and connected at that time. Otherwise the run proceeds but the local step is unavailable until the desktop reconnects.

## Working with agent runs
<a name="mission-control-runs"></a>

Mission Control organizes agent activity into runs. Depending on the state of a run, you can take different actions.

For a completed run, you view what the agent did and access the artifacts it produced, get an in-depth summary, track events of all sub-tasks, and chat to follow up on results. For an ongoing run, you view live events as the agent works, pause the run, or cancel it. For a run that needs input, you approve or deny authorization requests for third-party applications, or chat with the agent to provide clarifications.

## KPIs and metrics
<a name="mission-control-kpis"></a>

Mission Control displays key performance indicators that help you understand agent health and productivity at a glance. These metrics are available.


| Metric | Description | 
| --- | --- | 
| Failed runs | Number of agent runs that ended with an error. | 
| Active now | Count of agents that are currently running. | 
| Routines completed | Number of routines completed today. | 
| Runs this week | Total agent runs and app visits in the selected period, showing how your deployed agents and apps are being adopted. | 

## Viewing your runs and creator analytics
<a name="mission-control-analytics"></a>

From the Mission Control landing page, choose the Runs this week KPI to open the activity page. The activity page has two views: Runs and Creator analytics.

The Runs view shows your agent and app run activity for the selected time range (this week, last week, this month, last month, or last 90 days). It displays:
+ Summary cards: a Runs this week card (a total with a trend chart broken down by Agents and Apps) and an Agent hours card (the amount of agent runtime used, with the reset period).
+ Runs list: a searchable, sortable list of runs that you can filter by all, agents, or apps. The list has the columns run name, run type (agent or app), uses, run status, and last run (shown as last visited for apps). Rows expand to show more detail.

The Creator analytics view shows activity across the assets you have published or have co-owner access to, for the selected time range (this week, last week, this month, last month, or past 12 months). You can filter by all, agents, or apps.
+ All: summary cards for total assets shared and total assets used (each broken down by agents and apps), and a table with the columns asset name, type, usage, active users, and shared with.
+ Agents: summary cards for total agents shared and total conversations, and a table with the columns agent name, total active users, total conversations, average queries per user, and shared with.
+ Apps: summary cards for total apps shared and total app views, and a table with the columns app name, total active users, total app views, and shared with.

A Last updated timestamp shows when the analytics were refreshed. The creator analytics page refreshes every hour.

## Accessing Mission Control
<a name="mission-control-access"></a>

You can access Mission Control from anywhere in the desktop application. Choose the Mission Control icon in the top-right navigation bar. A quick-access popover appears showing agent runs, pending inputs, and routine management. To view the full Mission Control landing page, choose the Mission Control header or the View all button in the popover. Work from the lightweight popover for quick actions such as unblocking an agent, or open the full page for a comprehensive view of all agent activity.

## Examples of routines
<a name="mission-control-examples"></a>
+ Morning brief: every morning, summarize unread messages, new email, and today's calendar.
+ Inbox triage: every 30 minutes, scan new email and flag anything urgent.
+ Project monitor: daily, check a channel for updates on a project and compile a summary.
+ Meeting prep: before each meeting, gather relevant context and prepare a brief.
+ Competitive monitor: weekly, search the web for news about specified companies and produce a report.