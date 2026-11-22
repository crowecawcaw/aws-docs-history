

# Monitor and manage agents and flows with Mission Control

Mission Control is a centralized command center in AWS Quick that gives you full visibility and management over all your agents and flows in one place.

You monitor agent and flow activity, review outputs, and track performance metrics, so you do not need to check on agents and flows individually.

**Note**  
Routines have moved out of Mission Control and now have their own page. For more information about routines, see [Routines](working-with-routines.md).

**Note**  
The metric and dashboard widgets that previously appeared in the home page **My stuff** area now live in Mission Control. Your content items, such as recently viewed, shared, and favorite items, live in Library. For more information, see [Use Library to find your work](working-with-library.md).

## Why use Mission Control
<a name="mission-control-web-why"></a>

As you scale your use of agents and flows with background tasks and automated workflows, keeping track of everything becomes complex. Mission Control provides these benefits:
+ Centralized visibility – View all agent and flow activity without switching between conversations, agents, or flows.
+ Faster unblocking – Agents and flows that need your input are surfaced clearly, so you respond quickly.
+ Operational awareness – Key performance indicators (KPIs) and run history confirm your agents and flows are working correctly.
+ Efficiency at scale – Whether you have two agents or 20, Mission Control keeps you in control.

## Capabilities
<a name="mission-control-web-capabilities"></a>

Mission Control provides these capabilities for managing your agents and flows.


| Capability | Description | 
| --- | --- | 
| Monitor all agent and flow activity | View a unified list of what every agent and flow has done across all runs. | 
| Filter by name | Drill into a specific agent's or flow's history and access its outputs. | 
| Unblock agents and flows | Filter on agents and flows that need your input and provide it directly. | 
| View running agents and flows | See which agents and flows are currently active and monitor their progress. | 
| Track KPIs | Understand error rates, active agents and flows, and total runs. | 
| View creator analytics | See insights on how your shared agents, flows, and apps are being adopted. | 

## Working with agent and flow runs
<a name="mission-control-web-runs"></a>

Mission Control organizes agent and flow activity into runs. Depending on the state of a run, you can take different actions.

For a completed run, you view what the agent or flow did and access the artifacts it produced, get an in-depth summary, track events of all sub-tasks, and chat to follow up on results. For an ongoing run, you view live events as the agent or flow works, pause the run, or cancel it. For a run that needs input, you approve or deny authorization requests for third-party applications, or chat with the agent to provide clarifications.

## KPIs and metrics
<a name="mission-control-web-kpis"></a>

Mission Control displays key performance indicators that help you understand agent and flow health and productivity at a glance. These metrics are available.


| Metric | Description | 
| --- | --- | 
| Failed runs | Number of agent and flow runs that ended with an error. | 
| Active now | Count of agents and flows that are currently running. | 
| Runs this week | Total agent runs and app visits in the selected period, showing how your deployed agents and apps are being adopted. | 
| Total assets shared | Adoption insights across your shared agents, flows, and apps. | 
| Agent hours | Total agent hours consumed. | 

## Viewing your runs and creator analytics
<a name="mission-control-web-analytics"></a>

You can reach your run activity and creator analytics in two ways. From the Mission Control landing page, choose the **Runs this week** KPI to open the activity page, which has two views: **Runs** and **Creator analytics**. To view analytics for the assets you share, you can also open Mission Control and choose the **Analytics** tab, which shows the creator analytics view.

The **Runs** view shows your agent, flow, and app run activity for the selected time range (this week, last week, this month, last month, or last 90 days). It displays:
+ Summary cards – A Runs this week card (a total with a trend chart broken down by Agents, Flows, and Apps) and an Agent hours card (the amount of agent runtime used, with the reset period).
+ Runs list – A searchable, sortable list of runs that you can filter by all, agents, flows, or apps. The list has the columns run name, run type (agent, flow, or app), uses, run status, and last run (shown as last visited for apps). Rows expand to show more detail.

The **Creator analytics** view shows activity across the assets you have published or have co-owner access to, for the selected time range (this week, last week, this month, last month, or past 12 months). Choose the range from the **Time range** list, and search by name. You can filter by all, agents, flows, or apps:
+ All – Summary cards for total assets shared and total assets used (each broken down by agents, flows, and apps), and a table with the columns asset name, type, usage, active users, and shared with.
+ Agents – Summary cards for total agents shared and total conversations, and a table with the columns agent name, total active users, total conversations, average queries per user, and shared with.
+ Flows – Summary cards for total flows shared and total runs, and a table with the columns flow name, total active users, total runs, average runs per user, and shared with.
+ Apps – Summary cards for total apps shared and total app views, and a table with the columns app name, total active users, total app views, and shared with.

A Last updated timestamp shows when the analytics were refreshed. The creator analytics page refreshes every hour.

## Accessing Mission Control
<a name="mission-control-web-access"></a>

You can access Mission Control from anywhere in AWS Quick. Choose **Mission Control** from the navigation. A quick-access popover appears showing agent and flow runs and pending inputs. To view the full Mission Control landing page, choose the Mission Control header or the **View all** button in the popover. Work from the lightweight popover for quick actions such as unblocking an agent, or open the full page for a comprehensive view of all agent and flow activity.