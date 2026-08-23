AWS FinOps Agent is in preview release and is subject to change.

# Enable Jira with AWS FinOps Agent

Enable the agent to create issues, add comments, and read issues within the Jira projects you connect. The agent cannot update issue fields (assignee, priority, status transitions), delete issues, or manage Jira workflows. This setup requires Jira Cloud and does not support on-premises Jira.

## Integration and connection model

Jira integration uses a two-level model. The **integration** is registered at the AWS account level and stores the OAuth credentials and authorization status for a Jira site. An integration is shared across all agents in the account.

A **connection** is created at the agent level and specifies which Jira project the agent can access. Each connection is bound to one **space key** — the wizard's name for the 2- to 10-letter prefix that Jira uses on issue keys (for example, `ENG` for issues `ENG-1`, `ENG-2`). You grant access only to specific projects, not the full Jira site. Each agent creates its own connections, and the agent can only access projects listed in its connections.

## Prerequisites

Before registering a Jira integration, verify that you have the following:

###### Switch out of multi-session

The Jira integration cannot be configured while the AWS Management Console is in multi-session mode. Open the account menu in the top-right corner of the console, choose **Turn off multi-session support**, then sign back in and continue this setup.

- A Jira Cloud site URL and the space keys of the Jira projects where the agent will create tickets.
- A Jira administrator who can install the AWS FinOps Agent Forge app on the Jira site and authorize the following OAuth permission scopes:

| Scope                         | Description                                                                                                    |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `read:jira-work`              | View Jira issue data.                                                                                          |
| `read:jira-user`              | View user profiles.                                                                                            |
| `write:issue:jira`            | Create issues. The agent does not use the update permission during preview.                                    |
| `write:comment:jira`          | Create and update comments.                                                                                    |
| `write:comment.property:jira` | Create and update comment properties.                                                                          |
| `write:attachment:jira`       | Create and update attachments.                                                                                 |
| `read:issue:jira`             | Read issues. Required by `write:issue:jira`.                                                                   |
| `read:comment:jira`           | Read comments. Required by `write:comment:jira`.                                                               |
| `read:user:jira`              | Read user info.                                                                                                |
| `read:group:jira`             | Read group info.                                                                                               |
| `read:project:jira`           | Read project info.                                                                                             |
| `read:project-role:jira`      | Read project roles.                                                                                            |
| `read:avatar:jira`            | Read avatars.                                                                                                  |
| `read:comment.property:jira`  | Read comment properties.                                                                                       |
| `read:app-system-token`       | Enables Forge to pass a token to a remote backend for Atlassian app REST APIs. Required to enable the service. |

If your AWS console administrator and Jira administrator are different people, the Jira administrator can configure the integration from the agent detail page within the same account after the agent is created.

## Register a Jira integration

Registering a Jira integration is a one-time setup per Jira site. The AWS FinOps Agent console provides a guided wizard with five steps. Before you begin, make sure you are signed in to the Jira Cloud site where you want to install the Forge app in the same browser.

1. **Getting started.** The wizard provides an overview of the integration process and what you will need.
2. **Install Jira Forge app.** Choose **Install** in the wizard. The console opens an Atlassian-hosted install page in a new tab, using your active Jira session. Select the Jira site to install the AWS FinOps Agent app on, and complete the installation in Jira.
3. **Enter installation ID.** After installing the Forge app, navigate to your Jira site's apps section (**Jira Settings > Apps > Manage apps**). The AWS FinOps Agent app appears in the list. Copy the installation ID (a UUID in the format `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`) and paste it into the wizard.
4. **Authorize and connect.** Choose the authorize button. The wizard redirects you to an Atlassian authorization page. Review the requested permissions and choose **Accept**. After authorization, the wizard creates the integration and advances to the next step.
5. **Complete.** The wizard confirms the integration was created and displays the integration ID and connected Jira site. Choose **Go back to Agents page** to return to the console.

The integration is now registered at the account level and available to any agent in the account.

## Create a Jira connection

The integration is registered once at the account level. A connection is created per agent. Because each agent has its own detail page, you create the connection from the detail page of the agent you want to bind to Jira, which specifies the project that agent can access.

1. Open the agent you want to connect from the AWS FinOps Agent console to go to its detail page.
2. Choose **Add connection**, then choose **Jira**. The Jira option is available only after a Jira integration is registered in your account.
3. Select the Jira integration you registered from the dropdown.
4. Enter the **Space key** (2-10 uppercase letters, for example, `ENG` or `DATA`).
5. Choose **Create**.

During preview, each connection binds one space key to the agent. To give the agent access to multiple Jira projects, create a separate connection for each space key.

## Capabilities

After a Jira connection is created, the agent has three capabilities within the connected project:

- **Create issues**. When you ask the agent to summarize a cost anomaly or optimization recommendation into a Jira ticket, the agent creates the issue in the connected project.
- **Add comments**. The agent adds follow-up comments to issues it previously created.
- **Read issues**. The agent reads issue metadata (status, assignee, labels) to track whether recommendations have been acted on.

The agent does not select assignees or route tickets to specific engineering teams beyond the connected project. The default assignee comes from your Jira project configuration.

## Issue details

Every agent-created issue includes the following:

- A summary with the anomaly or recommendation details.
- A description with affected accounts and services, estimated cost impact, root-cause analysis (for anomalies), implementation guidance (for optimizations), and a link back to the task in the AWS FinOps Agent web application.
- An issue type specified by the agent based on context, defaulting to “Task” when the user does not specify one.

The agent does not set the Assignee or Priority fields. It defers to Jira's project-level default assignee, auto-assignment rules, and priority schemes.

## Integration statuses

A Jira integration has four possible statuses:

| Status   | Meaning                                                                                                                                                                             |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pending  | The administrator has initiated registration but has not completed the OAuth authorization.                                                                                         |
| Active   | OAuth authorization is complete. The agent can use the integration.                                                                                                                 |
| Error    | The integration was previously active but encountered an issue (expired token, revoked app access, persistent authentication failures). The administrator re-authorizes to restore. |
| Inactive | The administrator explicitly disabled the integration without deleting it. Configuration and connections are preserved, but the agent does not use it.                              |

## Approval workflow

During preview, approval behavior depends on how the action is started. From a chat conversation, the agent presents the action details (issue creation or comment addition) and asks for confirmation before running it. From a scheduled or event-based automation, where you pre-authorized the workflow at setup, the agent runs the action without an additional approval prompt and writes the result to the task history. For details on approval and guardrail behavior, see [Agent guardrail controls](agent-guardrail-control.md "agent-guardrail-control.md").

## Error handling

When Jira actions fail because of authorization errors (expired OAuth token, revoked app access), the task fails with a descriptive error and the integration status updates to **Error**. The administrator re-authorizes the integration before the agent can resume Jira operations.

When actions fail because of invalid space keys (project deleted or renamed on the Jira site), the agent asks the user which project to use instead for interactive tasks. For scheduled or event-based tasks with no user present, the task fails and the user is notified. If the agent has access to multiple Jira projects and the user does not specify which one to use, the agent presents the available options and asks the user to choose.

For rate-limited requests (HTTP 429) or site unavailability (HTTP 5xx), the agent retries with exponential backoff up to three times before failing the task.
