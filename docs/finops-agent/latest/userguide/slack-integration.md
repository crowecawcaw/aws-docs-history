AWS FinOps Agent is in preview release and is subject to change.

# Enable Slack with AWS FinOps Agent

Enable the agent to post task and automation results to Slack channels you connect. During preview, the connection is one-way: the agent posts to Slack but does not read messages, accept commands, or respond to mentions. The agent cannot edit or delete posts, manage channel membership, or interact with threads after posting.

## Integration and connection model

Slack integration uses the same two-level model as Jira. The **integration** is registered at the AWS account level and stores the OAuth credentials and authorization status for a Slack workspace. An integration is shared across all agents in the account.

###### Move a Slack workspace to another AWS account

A Slack workspace can be registered with one AWS account at a time. To use the workspace with another account, first remove all Slack connections that use the integration from the current account. On the Agents page, choose **Disconnect Slack** to remove the integration, then register the workspace from the other account.

A **connection** is created at the agent level and specifies which Slack channel the agent posts to. Each agent creates its own connections, and the agent can only post to channels listed in its connections.

## Prerequisites

Before registering a Slack integration, verify that you have the following:

###### Switch out of multi-session

The Slack integration cannot be configured while the AWS Management Console is in multi-session mode. Open the account menu in the top-right corner of the console, choose **Turn off multi-session support**, then sign back in and continue this setup.

- A Slack workspace where you have permission to install apps and authorize third-party OAuth apps.
- The channel IDs of any channels the agent will post to. To find a channel ID in Slack, right-click the channel name, choose **View channel details**, and copy the ID at the bottom (for example, `C04ABCDEF12`).

## Register a Slack integration

Registering a Slack integration is a one-time setup in an AWS account. The AWS FinOps Agent console provides a guided wizard with three steps. Before you begin, make sure you are signed in to the Slack workspace where you want to install the AWS FinOps Agent Slack app in the same browser.

1. **Getting started.** The wizard provides an overview of the integration process and what you will need.
2. **Authorize and connect.** Choose **Authorize with Slack**. The wizard redirects you to Slack to grant permission to the AWS FinOps Agent app. Review the requested permissions and approve. After authorization, Slack returns you to the wizard, which creates the integration automatically.
3. **Complete.** The wizard confirms that Slack is connected and displays the integration ID and the connected workspace name. Choose **Go back to Agents page** to return to the console.

The integration is now registered at the account level and available to any agent in the account.

## Create a Slack connection

The integration is registered once at the account level. A connection is created per agent. Because each agent has its own detail page, you create the connection from the detail page of the agent you want to bind to Slack, which specifies the channel that agent can post to.

###### Important

Add the AWS FinOps Agent Slack app to the channel before you create the connection. From Slack, open the channel, choose the channel name, choose the **Integrations** tab, and add the AWS FinOps Agent app. Without the app in the channel, the agent cannot post messages to this channel.

1. Open the agent you want to connect from the AWS FinOps Agent console to go to its detail page.
2. Choose **Add connection**, then choose **Slack**. The Slack option is available only after a Slack integration is registered in your account.
3. Select the Slack integration you registered from the dropdown.
4. Enter the Slack channel ID. Nine to twelve uppercase alphanumeric characters (for example, `C04ABCDEF12`).
5. Choose **Create**.

Each connection binds one channel to the agent. To give the agent access to multiple Slack channels, create a separate connection for each channel.

## Capabilities

After a Slack connection is created, the agent has one capability within the connected channel:

- **Post messages and artifacts**. The agent posts task and automation results, including HTML, PDF, and PPT artifacts, to the connected channel.

## Message details

Every agent-posted message includes the following:

- A summary line that identifies the source (task name, automation name, or conversation turn) and a link back to the AWS FinOps Agent web application.
- The result content, formatted in Slack markdown (headings, bold, lists, tables, code blocks).
- Any artifacts the user attached to the message, uploaded as files in the channel. Supported artifact types are `.html`, `.pdf`, and `.pptx`.

## Integration statuses

A Slack integration has four possible statuses:

| Status   | Meaning                                                                                                                                                                                                                          |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pending  | The administrator has initiated registration but has not completed the OAuth authorization with Slack.                                                                                                                           |
| Active   | OAuth authorization is complete. The agent can post to channels.                                                                                                                                                                 |
| Error    | The integration was previously active but encountered an issue (revoked OAuth token, the AWS FinOps Agent Slack app removed from the workspace, persistent authentication failures). The administrator re-authorizes to restore. |
| Inactive | The administrator explicitly disabled the integration without deleting it. Configuration and connections are preserved, but the agent does not use it.                                                                           |

## Error handling

When Slack actions fail because of authorization errors, the task fails with a descriptive error and the integration status updates to **Error**. The administrator re-authorizes the integration before the agent can resume Slack operations.

When actions fail because the AWS FinOps Agent Slack app is not a member of the connected channel, the post fails. Add the app to the channel from Slack to restore posting.

For rate-limited requests (HTTP 429) or workspace unavailability (HTTP 5xx), the agent retries with exponential backoff up to three times before failing the task.
