

AWS FinOps Agent is in preview release and is subject to change.

# Creating an agent
<a name="creating-an-agent"></a>

This topic walks through creating a AWS FinOps Agent agent in the AWS FinOps Agent console. The wizard has five steps: name your agent, choose what AWS resources the agent can access, give the web app access to your agent, third-party integrations (optional), and review and create.

A FinOps agent is an independent instance of AWS FinOps Agent that you configure in your AWS account. Each agent operates independently with its own IAM permissions, context files, memory, task queue, and third-party integrations. No data, resources, or permissions are shared across agents.

## Prerequisites
<a name="creating-an-agent-prerequisites"></a>

Verify that you have the following in place:
+ **Administrator setup permissions.** Your IAM identity needs permissions to create the agent and, when you choose **Auto-create a new role**, to create the agent and operator service roles. These permissions are defined in the [`FinOpsAgentSetupPolicy`](setting-up.md#setting-up-administrator-policy).
+ **Existing service roles (optional).** The wizard can create the agent's roles for you. If you would rather provide your own, prepare a role for the agent (with [`FinOpsAgentAgentPolicy`](setting-up.md#setting-up-agent-policy)) and a role for the operator (with [`FinOpsAgentOperatorPolicy`](setting-up.md#setting-up-operator-policy)). Both roles must trust `finops-agent.amazonaws.com`. For the trust policy, see [Trust policy](setting-up.md#setting-up-trust-policy).
+ **Third-party integrations (optional).** For Jira, see [Enable Jira with AWS FinOps Agent](jira-integration.md). For Slack, see [Enable Slack with AWS FinOps Agent](slack-integration.md). You can skip this step during agent creation and add integrations later from the agent detail page.

## The creation wizard
<a name="creating-an-agent-wizard"></a>

On the Agents page in the AWS FinOps Agent console, choose **Create** to launch the wizard.

### Step 1: Name your agent
<a name="creating-an-agent-step-1"></a>

Enter a name and an optional description.
+ **Agent name.** Letters, numbers, spaces, and hyphens only. Up to 128 characters. Underscores, dots, and other special characters are not allowed.
+ **Description (optional).** Letters, numbers, spaces, and common punctuation (`- . , ! ? ; : ' " ( ) & /`). Up to 512 characters.

### Step 2: Choose what AWS resources the agent can access
<a name="creating-an-agent-step-2"></a>

Choose the IAM role that AWS FinOps Agent assumes to read your AWS cost and operational data, and to manage event-based automations. You have two options.

**Option 1: Auto-create a new role (recommended).** The wizard creates the agent role with [`FinOpsAgentAgentPolicy`](setting-up.md#setting-up-agent-policy) attached and a trust policy scoped to your account and to this agent. No manual IAM configuration is required.

**Option 2: Use an existing role.** Select a role you have already created. The role must have `FinOpsAgentAgentPolicy` (or an equivalent policy) attached, and must trust `finops-agent.amazonaws.com`. For the required actions and trust policy, see [`FinOpsAgentAgentPolicy`](setting-up.md#setting-up-agent-policy) and [Trust policy](setting-up.md#setting-up-trust-policy).

### Step 3: Give the web app access to your agent
<a name="creating-an-agent-step-3"></a>

Choose the IAM role that AWS FinOps Agent assumes to run web application operations such as conversations, tasks, automations, and document management. The two options match Step 2.

**Option 1: Auto-create a new role (recommended).** The wizard creates the operator role with [`FinOpsAgentOperatorPolicy`](setting-up.md#setting-up-operator-policy) attached.

**Option 2: Use an existing role.** Select a role you have already created. The role must have `FinOpsAgentOperatorPolicy` (or an equivalent policy) attached, and must trust `finops-agent.amazonaws.com`.

### Step 4: Third-party integrations (optional)
<a name="creating-an-agent-step-4"></a>

Optionally connect Jira and Slack to this agent. Both selections require that you have already installed the integration at the account level. If you have not, skip this step and add connections later from the agent detail page.

#### Connect with Jira
<a name="creating-an-agent-step-4-jira"></a>

Authorize the agent to create Jira issues for cost anomalies, optimization recommendations, and other actionable findings you ask it to act on.
+ **Jira integration.** Select an existing Jira integration registered in this account.
+ **Space key.** Enter the Jira project space key the agent should use. Two to ten uppercase letters, starting with a letter (for example, `ENG`, `KAN`, or `FIN`).

For the integration setup process, see [Enable Jira with AWS FinOps Agent](jira-integration.md).

#### Connect with Slack
<a name="creating-an-agent-step-4-slack"></a>

Authorize the agent to post task and automation results to Slack channels you choose.
+ **Slack integration.** Select an existing Slack integration registered in this account.
+ **Channel ID.** Enter a Slack channel ID. Nine to twelve uppercase alphanumeric characters (for example, `C04ABCDEF12`). To find the channel ID in Slack, right-click the channel name, choose **View channel details**, and copy the ID at the bottom. Before you connect, add the AWS FinOps Agent Slack app to the channel.

For the integration setup process, see [Enable Slack with AWS FinOps Agent](slack-integration.md).

### Step 5: Review and create
<a name="creating-an-agent-step-5"></a>

Review the summary of your agent name, what AWS resources the agent can access, web app access, and integration selections. Choose **Edit** on any step to make changes.

### Complete agent creation
<a name="creating-an-agent-complete"></a>

When the configuration is correct, choose **Create agent**. AWS FinOps Agent creates the agent, provisions any auto-created roles, attaches the integration connections, and generates the web application.

## Verifying your agent setup
<a name="creating-an-agent-verify"></a>

After creation, the agent appears on the Agents page in the AWS FinOps Agent console. Open the agent detail page to confirm the following:
+ The agent role and operator role are listed under **Permissions**.
+ Any Jira or Slack connections you added in Step 4 appear under **Integrations**.
+ Choose **Open agent** to open the web application in a new browser tab. The web application authenticates through your AWS console session.

## Accessing the web application
<a name="creating-an-agent-access-web-app"></a>

After the agent is created, access the web application from the AWS FinOps Agent console. Navigate to the Agents page and locate your agent. You have two ways to open the web application:
+ Choose **Open** in the **Open agent** column of the Agents table.
+ Choose the agent name to open the agent detail page, then choose **Open agent**.

The web application opens in a new browser tab.

## Sharing access with your team
<a name="creating-an-agent-share-access"></a>

To give other users access to the agent, share the AWS account ID and the agent name. Users navigate to the AWS FinOps Agent console in the same AWS account, locate the agent by name, and launch the web application from there. Each user authenticates through their own AWS console session. Users need the [end-user web app policy](setting-up.md#setting-up-end-user-policy) attached to their IAM identity.

## Managing your agent after creation
<a name="creating-an-agent-manage"></a>

From the agent detail page in the console, you can do the following:
+ View the agent configuration, including IAM roles and integration connections.
+ Connect or disconnect Jira projects and Slack channels.
+ Access the web application.
+ View and manage historical chat conversations in the web application.
+ Delete the agent.

Before you can delete an agent, you must delete both its Jira and Slack connections. Open the agent detail page, choose the **Integrations** tab, and delete each connection.

To delete an agent, select it on the Agents page and choose **Delete**. You can select multiple agents for bulk deletion. After deletion, the web application link and previous interaction data are removed.

## Next steps
<a name="creating-an-agent-next-steps"></a>
+ Learn [how to interact with the agent](how-do-i-interact-with-the-agent.md) in the web application, including chatting, creating tasks, and uploading context files.
+ [Configure Jira](jira-integration.md) or [configure Slack](slack-integration.md) if you skipped these during setup.