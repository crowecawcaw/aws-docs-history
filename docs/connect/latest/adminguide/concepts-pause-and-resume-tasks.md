

# Pause and resume tasks in Connect Customer Tasks
<a name="concepts-pause-and-resume-tasks"></a>

You can pause and resume all tasks that aren't expired, disconnected, or scheduled for a later time. The benefit of pausing and resuming tasks is that it enables agents to free up an active slot so they can receive more critical tasks when their current task is stalled, for example, because of a missing approval or waiting on an external input. 

You can also pause fully automated tasks to address force majeure events (natural disasters, infrastructure failures, invasions) that might require you to halt all business processes temporarily, and then resume them after the emergency has passed.

**Topics**
+ [How paused and resumed tasks are queued](#pause-tasks-queue)
+ [How agents pause and resume tasks](#pause-tasks-agent-experience)
+ [How many tasks an agent can pause](#pause-tasks-number)
+ [When can a paused task be resumed?](#when-resume-tasks)
+ [Programmatically pause and resume tasks](#programmatically-pause-and-resume-tasks)
+ [Configure a flow to pause and resume tasks](#pause-and-resume-flow)
+ [Contact event stream](#ces-pause-and-resume-tasks)
+ [Pause and resume task events in contact records](#ctr-pause-and-resume-tasks)
+ [Metrics](#metrics-pause-and-resume-tasks)

## How paused and resumed tasks are queued
<a name="pause-tasks-queue"></a>
+ All paused tasks that are in queue and not yet assigned to an agent are dequeued. This way they don't consume the queue limits for your instance and instead allow other more critical contacts to be assigned to agents. 
+ After the task is resumed, it is re-queued and the flow continues running per your configuration.
+ When you design a flow to resume unassigned, paused tasks that are dequeued, be sure to add a [Transfer to queue](transfer-to-queue.md) block to the flow to queue the task after resuming. Otherwise, the task will stay in a de-queued state. 

## How agents pause and resume tasks
<a name="pause-tasks-agent-experience"></a>

Agents can pause a task from their Contact Control Panel (CCP) or agent workspace by using the **Pause** button. To update the task, the agent must choose **Resume**. The only actions the agent can take on a task that is in the Paused state are to end it or transfer it.

The following image shows the **Pause** button on the CCP. 

![The Pause button on the CCP.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tasks-pause-button-ccp.png)


The following image shows the **Pause** button on the agent workspace. 

![The Pause button on the agent workspace.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tasks-pause-button-agentworkspace.png)


After an agent pauses or resumes a task, a banner is displayed that notifies them of the current status of the task. The following image of the CCP shows the Pause banner.

![Pause and Resume banners on the CCP.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tasks-paused-ccp.png)


The following image of the agent workspace shows the Resume banner.

![Pause and Resume banners on the agent workspace.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tasks-resumed.png)


When an agent has multiple tasks open and they pause any one of them, the icon updates in the task list to notify them of the state of the task. The following image shows an example of a Paused icon.

![A task status icon.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tasks-pause-agentworkspace.png)


## How many tasks an agent can pause
<a name="pause-tasks-number"></a>

An agent can pause the up to twice the number tasks as the **Maximum tasks per agent** setting in their [routing profile](routing-profiles.md). 

For example, an agent has a **Maximum tasks per agent** setting to handle 5 active tasks simultaneously. This means they can pause up to 5 tasks, which allows them to free up their active slots to take in new more critical tasks. However, it also means that agents can have twice the number of tasks in their workspace at any point in time. In our example, this agent can have 10 tasks in their workspace: 5 paused and 5 active. 

## When can a paused task be resumed?
<a name="when-resume-tasks"></a>

A paused task can be resumed at any time. As a result, it's possible for an agent to work temporarily on twice their concurrency limit of tasks. 

For example, an agent has 10 tasks in their workspace: 5 paused and 5 active. They resume all of their paused tasks simultaneously. Now they have 10 active tasks. No new tasks are routed to them until the number of active tasks is lower than the **Maximum tasks per agent** limit in their routing profile.

## Programmatically pause and resume tasks
<a name="programmatically-pause-and-resume-tasks"></a>

You can pause and resume tasks programmatically by using the [PauseContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_PauseContact.html) and [ResumeContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_ResumeContact.html) APIs.

When pausing and resuming a task, a corresponding flow can be configured to run at the pause and resume events. For example: 
+ You might want to design a flow to automatically resume Paused tasks after a set period of time for agent lunch breaks. 
+ You might want to create a resume flow to update attributes on the task that might have changed while the task was Paused.

## Configure a flow to pause and resume tasks
<a name="pause-and-resume-flow"></a>

Configure a [Set event flow](set-event-flow.md) block to pause and resume tasks. The following image shows the **Properties** page of a **Set event flow** block configured to pause a flow. 

![The properties page of the Set event flow block.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tasks-set-event-flow.png)


Following are a couple of scenarios you might want to configure in your flows:
+ For flows that run at contact pause, configure them to notify supervisors when a task has been paused. 
+ When resuming a paused contact, configure the flow to update contact attributes to make sure that agents are always working on the latest version of attributes.

## New events in the contact event stream and agent event stream
<a name="ces-pause-and-resume-tasks"></a>

When tasks are paused and resumed, new events are generated for PAUSED and RESUMED in the contact event stream and agent event stream. 

The following image shows an example of a PAUSED event in the contact event stream. 

![PAUSED event in the contact event stream.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tasks-pause-ces.png)


The following image shows an example of a RESUMED event in the contact event stream. 

![RESUMED event in the contact event stream.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tasks-resumed-ces.png)


The following image shows an example of PAUSED tasks in the agent event stream. 

![PAUSED events in the agent event stream.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tasks-aes.png)


## Pause and resume task events in contact records
<a name="ctr-pause-and-resume-tasks"></a>

The following events are captured in the [ContactTraceRecord](ctr-data-model.md#ctr-ContactTraceRecord) section of the contact records data model. You can use the [DescribeContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeContact.html) API to return task events. 


| Name in contact record | Name returned by DescribeContact API | 
| --- | --- | 
| TotalPauseDurationInSeconds | TOTAL\_PAUSED\_TIME | 
| TotalPauseCount | TOTAL\_NUMBER\_OF\_PAUSES | 
| LastPausedTimestamp | LAST\_PAUSED\_TIMESTAMP | 
| LastResumedTimestamp | LAST\_RESUMED\_TIMESTAMP | 

The following values are available in near real time when you use the [DescribeContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeContact.html) API or view the **Contact details** page for an in progress contact. 
+ TotalPauseCount
+ LastPausedTimestamp
+ LastResumedTimestamp

A completed contact has TotalPauseDurationInSeconds. 

## Metrics
<a name="metrics-pause-and-resume-tasks"></a>

The following metrics display active, paused, and resumed time. 


| Real-time metrics | Description | 
| --- | --- | 
| **[UI]** Agent/Routing Profiles/Queue → Performance → **Average Active Time** | SUM(active\_time)/Number of contacts | 
| **[UI]** Agent/Routing Profiles/Queue → Performance → **Average Agent Pause Time** | SUM(agent\_pause\_time)/Number of contacts that were paused | 
| **[UI]** Agent → Contacts → **Contact State** | Paused state of a task contact | 


| Historical Metrics | Description | 
| --- | --- | 
| **[UI]** Agent → Agent activity audit → Support "PAUSED" state | Display paused state when the contact for an agent is in Paused state | 
| **[[GetMetricDataV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html)]** Query Average of AGENT\_PAUSE\_TIME for a queue/routing profile/task | SUM(total\_agent\_pause\_time) for all contacts that were paused from queue/routing profile/TaskAVG = SUM(total\_agent\_pause\_time)/number of paused contacts for queue/RP/Tasks | 
| **[[GetMetricDataV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html)]** Query Average of ACTIVE\_TIME for a queue/routing profile | SUM(total\_handle\_time - total\_agent\_pause\_time) for all contacts of queue/routing profile/tasks<br />AVG = SUM(total\_handle\_time - total\_agent\_pause\_time) / total number of contacts for queue/routing profile/tasks | 


| Contact details page | Description | 
| --- | --- | 
| **[UI]** Contact Search → Contact Details → Contact Summary → Last Paused Time | Last Paused Time | 
| **[UI]** Contact Search → Contact Details → Contact Summary → Last Resumed Time | Last Resumed Time | 
| **[UI]** Contact Search → Contact Details → Contact Summary → Number of Pauses | Total number of Pauses including when the contact was not connected. | 
| **[UI]** Contact Search → Contact Details → Contact Summary → Total Pause Duration | Total Pause duration includes before and after the agent was connected. | 

### Real-time Metrics page
<a name="rtm-tasks-ui"></a>

The following image of the **Real-time Metrics** page shows the task contact state as **Paused**.

![The real-time metrics page, task in paused contact state.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tasks-paused-rtm.png)


The following image of the **Real-time Metrics** page shows **Avg Active Time**, **AHT** and **Avg Agent Pause Time**.

![The real-time metrics page, task in paused contact state.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tasks-rtm-2.png)


### Agent Activity Audit report
<a name="agent-audit-tasks-ui"></a>

The following image of the **Agent Activity Audit report** shows the Paused status when a contact is paused by the agent.

![The agent activity audit report, paused status.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tasks-agent-activity-report.png)
