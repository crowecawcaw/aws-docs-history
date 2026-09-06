

AWS FinOps Agent is in preview release and is subject to change.

# Event-triggered cost anomaly investigation
<a name="automated-anomaly-response"></a>

<a name="cost-anomaly-detection-automated-response"></a>This topic walks through setting up an end-to-end event-triggered workflow: the agent listens for AWS Cost Anomaly Detection events, investigates each anomaly for root cause, and posts the summary to a Slack channel. After you set this up once, anomalies are investigated and delivered to your team without manual triage.

The workflow combines three pieces:
+ **A trigger** — a AWS Cost Anomaly Detection anomaly event.
+ **An action** — an investigation that the agent runs when the event arrives.
+ **A destination** — the Slack channel the agent posts the summary to.

## Prerequisites
<a name="aar-prerequisites"></a>
+ At least one anomaly monitor in AWS Cost Anomaly Detection. The agent investigates anomalies that your monitors produce. To create a monitor, see [Getting started with AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html).
+ The agent role has the AWS EventBridge permissions in [`FinOpsAgentAgentPolicy`](setting-up.md#setting-up-agent-policy). The agent uses these to create the managed rule that receives anomaly events. If you created the agent with the wizard's auto-created role, these permissions are already in place.
+ A Slack channel where the agent posts results, connected as described in Step 1.

## Step 1: Connect a Slack channel
<a name="aar-step-connect-slack"></a>

Connect the Slack channel that the agent posts investigation summaries to. If you already connected the channel during agent creation, skip to Step 2.

Connecting Slack to an agent is a two-part process: register a Slack integration at the account level, then create a connection that binds a channel to your agent.

1. Register a Slack integration for your account, if you have not already. This is a one-time setup per Slack workspace. For the full process, including adding the AWS FinOps Agent Slack app to the channel, see [Enable Slack with AWS FinOps Agent](slack-integration.md).

1. Open your agent from the AWS FinOps Agent console, where you will see an **Add connection** button.

1. Choose **Add connection**, then choose **Slack**. The Slack option is available only after a Slack integration is registered in your account.

1. Select the Slack integration, enter the channel ID of the channel the agent posts to, then choose **Create**.

## Step 2: Describe the trigger and response in chat
<a name="aar-step-describe-trigger"></a>

In the chat area, send a prompt that describes the event you want the agent to listen for and what it should do when the event arrives. State the monitor or scope, the investigation, and the Slack channel in a single prompt. The agent recognizes a prompt like this as a request to set up ongoing automation and creates the event-based automation directly, rather than running a one-time investigation.

For example, either of these prompts creates an event-based automation:
+ *“When a cost anomaly is detected on my production monitor, investigate the root cause and post the summary to {{<slack-channel>}}.”*
+ *“When a cost anomaly over $1,000 is detected, investigate the root cause and post the findings to {{<slack-channel>}}.”*

Include a filter in the prompt, such as a dollar threshold, to narrow what the agent acts on so your team's attention stays on the highest-impact changes. The second example above investigates only anomalies over $1,000.

From your prompt, the agent creates an event-based [automation](task-management.md#task-management-event-based) with a `COST_ANOMALY` trigger. The automation stores the prompt you described and the destination. Each time AWS Cost Anomaly Detection emits a matching anomaly event, the agent creates and runs a task from the automation, investigates the anomaly, and posts the summary to the Slack channel you specified.

Behind the scenes, the agent provisions an AWS EventBridge managed rule in your account to receive the anomaly events. The rule is scoped so that the agent manages only the rules it created. For the underlying permissions, see [`FinOpsAgentAgentPolicy`](setting-up.md#setting-up-agent-policy).

**Note**  
Posting to Slack does not require approval, so the automation runs end to end without prompting. If your automation also creates a Jira issue, that action is pre-authorized when you set up the automation, so it also runs without a per-event approval prompt. For the full approval model, see [Agent guardrail controls](agent-guardrail-control.md).

## Step 3: Verify and manage the automation
<a name="aar-step-verify-manage"></a>

Open the **Automations** workspace in the web application to confirm the automation was created. The workspace lists each automation with its trigger type, status, and last triggered time.

From the automation detail page, you can do the following:
+ Enable or disable the automation without deleting it.
+ Delete the automation. Deleting it stops new tasks from being created on the trigger; tasks already created remain on the agent.
+ Review the tasks the automation has run, including each investigation and its delivery result.

To investigate an anomaly on demand instead of automatically, see [Investigating cost anomalies](cost-anomaly-detection.md).