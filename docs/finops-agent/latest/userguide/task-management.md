

AWS FinOps Agent is in preview release and is subject to change.

# Task management
<a name="task-management"></a>

AWS FinOps Agent supports three task types: on-demand, scheduled, and event-based. Each runs through a shared task queue.

## On-demand tasks
<a name="task-management-on-demand"></a>

On-demand tasks run in the background without blocking the conversation. When you ask the agent to create a task, it runs the work in the background and continues the conversation. This is useful for requests that require extended processing, such as generating a report or investigating an anomaly. The agent creates a task only when you ask it to; it answers other requests directly in the conversation.

You can create on-demand tasks in two ways:
+ **From the chat area.** Ask the agent to create a task in conversation. For example: “Create a task to generate a cost report for last month.” The agent creates the task and runs it in the background.
+ **From the Tasks workspace.** In the side navigation, choose **Tasks**, then choose **Create tasks** to open the task creation form. The form includes instructions for how you want the task to be structured.

## Scheduled tasks
<a name="task-management-scheduled"></a>

Scheduled tasks run recurring workflows at specified intervals. Define the schedule through natural language (for example, “every Monday at 9 AM” or “on the first business day of each month”) and the agent creates a recurring automation in its queue. Each time the schedule triggers, the agent creates and runs a new task from the automation.

To view all automations, open the **Automations** workspace from the side navigation. To stop a recurring workflow, disable or delete the automation.

## Event-based tasks
<a name="task-management-event-based"></a>

Event-based tasks trigger automated responses when conditions are met. During preview, the agent supports cost anomaly detection events from [AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html). When an anomaly is detected on a monitor that matches the event-based task, the agent runs the prompt you specified.

You configure event-based tasks by describing the trigger condition and desired response in conversation. For example: *“When a cost anomaly is detected on my production monitor, investigate the root cause and post the summary to my finance Slack channel.”* The agent registers an event-based automation that runs the prompt each time a matching event arrives.

Behind the scenes, the agent provisions an AWS EventBridge managed rule to receive the events. For details on the underlying IAM permissions, see [`FinOpsAgentAgentPolicy`](setting-up.md#setting-up-agent-policy). For the end-to-end walkthrough, see [Event-triggered cost anomaly investigation](automated-anomaly-response.md).

## Approvals for read-write actions
<a name="task-management-approvals"></a>

During preview, the agent requires approval before creating a Jira issue or adding a comment to one, and only when the action is started from a chat conversation or from an on-demand task. The agent shows the action details (for an issue: project, summary, description; for a comment: target issue and body) in the conversation, and you confirm or revise before the action runs.

Automations that include Jira ticket creation (scheduled or event-based) do not prompt for approval. When you set up the automation, you pre-authorize the agent to create tickets each time the automation runs, so the workflow completes end to end without manual intervention.

Posting a message to a Slack channel does not require approval, including from a chat conversation or an on-demand task. The agent posts to the channel you specify and records the result in the task history. For the full read-write action model, see [Agent guardrail controls](agent-guardrail-control.md).

All other agent actions (querying cost data, retrieving recommendations, posting to a Slack channel, generating reports) run without approval. You can review every action the agent took in the task history.

For details on guardrail policies, see [Agent guardrail controls](agent-guardrail-control.md).