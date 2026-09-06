

AWS FinOps Agent is in preview release and is subject to change.

# Using the web application
<a name="how-do-i-interact-with-the-agent"></a>

The web application is where you do day-to-day work with AWS FinOps Agent. From it, you can chat with the agent, manage tasks and automations, upload context files, and download generated artifacts.

## Accessing the web application
<a name="accessing-the-web-application"></a>

Open the AWS FinOps Agent console in your AWS account, navigate to the Agents page, and locate your agent. Choose the web application link to open it in a new browser tab. You authenticate through your AWS console session. During preview, each session lasts 30 minutes. After the session expires, you are redirected to re-authenticate through the AWS console.

**Note**  
**Trouble accessing the web application?** If you cannot open the web application or receive a permissions error, check the following:  
Verify with your administrator that your IAM identity has the AWS FinOps Agent operator permissions attached. Without these permissions, the web application cannot authenticate your session. See [End-user web app policy](setting-up.md#setting-up-end-user-policy) for the required policy.
Check whether your AWS console session has expired. If it has, sign in to the AWS console again and reopen the web application from the AWS FinOps Agent console.

## Layout overview
<a name="webapp-layout"></a>

The web application has three sections: a **side navigation** on the left, a **chat area** in the center, and a **workspace panel** on the right that opens when you choose a side navigation item.
+ **Side navigation.** Switches between workspaces and tracks your past conversations. See [Side navigation](#webapp-side-navigation).
+ **Chat area.** The primary way to interact with the agent. See [Chat](#webapp-chat).
+ **Workspace panel.** Opens to show the workspace you choose from the side navigation: Tasks, Automations, Artifacts, or Context files. See [Workspaces](#webapp-workspaces).

## Side navigation
<a name="webapp-side-navigation"></a>

The side navigation on the left has three sections: a **New chat** button at the top, a list of **workspace links**, and a **Recent** conversation list.
+ **New chat.** Starts a new conversation while keeping the workspace panel you have open. Use this to begin a new topic without losing the page you were on.
+ **Tasks.** Opens the Tasks workspace, where you view and manage on-demand tasks the agent runs in the background.
+ **Automations.** Opens the Automations workspace, where you create, view, enable, disable, or delete recurring and event-triggered automations.
+ **Artifacts.** Opens the Artifacts workspace, where you download files the agent generated, such as HTML, PDF, and PPT reports.
+ **Context files.** Opens the Context files workspace, where you upload, soft-delete, and restore files the agent uses to understand your organization.
+ **Recent.** Lists your past conversations sorted by last activity. Choose a conversation to reopen it. Choose **Load more** at the bottom of the list to fetch additional pages.

The agent's display name appears in the bottom of the side navigation, so you can confirm which agent you are using when your team has more than one agent.

## Chat
<a name="webapp-chat"></a>

The chat area is the primary way to interact with the agent. The initial view shows a prompt input and a set of suggested prompts under **Prompts to try out**. Choose a suggested prompt or type your own message and choose send. Each chat message can be up to 1,000 characters.

For an overview of what you can ask, see [Chatting with AWS FinOps Agent](chatting-with-finops-agent.md).

**Continuing a conversation.** Each conversation maintains its own context. You can ask follow-up questions that reference earlier parts of the conversation. If you navigate to a workspace and return, your conversation is preserved.

**Starting a new conversation.** Choose **New chat** at the top of the side navigation. Your previous conversation remains accessible from the **Recent** list.

**Reopening a past conversation.** Choose any conversation in the **Recent** list to load it and continue where you left off.

## Workspaces
<a name="webapp-workspaces"></a>

Each link in the side navigation opens a workspace in the right panel. The four workspaces are described in this section.

<a name="webapp-tasks-queue"></a>**Tasks.** Lists all tasks sorted by last updated time. Filter by **All tasks**, **Awaiting approval**, **In progress**, or **Completed**. Recently created tasks appear at the top. Use the refresh button to show updated status. Each row shows the task ID, name, status, creation time, and last updated time. Choose a task to open its detail page, which includes the overview, instructions, execution activities, generated files, and status. From the task detail page, you can cancel a running task. For the task lifecycle, see [Task management](task-management.md).

<a name="webapp-automations"></a>**Automations.** Lists recurring and event-triggered automations. An automation defines what the agent does and when it runs. From this workspace, you can view all automations with their trigger type, schedule, status, and last triggered time; create a new automation with instructions and trigger configuration; and delete an automation. To enable or disable an automation without deleting it, open its detail page. Existing tasks already created by an automation are not affected when the automation is deleted.

<a name="webapp-reports"></a>**Artifacts.** Lists files the agent has generated, such as HTML, PDF, and PPT reports and analysis results. Each row shows the file name, type, size, and creation time. Choose an artifact to download the file or to open the source task that produced it.

<a name="webapp-context-files"></a>**Context files.** Lists files you have uploaded to help the agent understand your organization. From this workspace, you can view all context files with their name, type, size, status, and upload time; upload a new context file (for supported types and limits, see [Context files and memory](context-files-and-memory.md)); and soft-delete or restore files.

## Approvals
<a name="webapp-approvals"></a>

When the agent needs to create a Jira issue or add a comment to one, it pauses and requests your approval before proceeding. Pending approvals appear in the Tasks workspace under the **Awaiting approval** filter. Open the task detail page to see the proposed action, then approve or reject it.

For chat-initiated tasks, the agent asks for approval in the conversation. For scheduled and event-based automations that include Jira issue creation or comment addition, no approval is required. When you set up the automation, you pre-authorize the agent to take those actions each time the automation runs.

For details on guardrail behavior, see [Agent guardrail controls](agent-guardrail-control.md).

## Providing feedback
<a name="submitting-feedback"></a>

The simplest way to give feedback is through the thumbs up and thumbs down buttons in the web application. Use the channels in this section for documentation issues, larger asks, and account-team escalations.

### In-product feedback (thumbs up and thumbs down)
<a name="submitting-feedback-in-product"></a>

Every agent response and every task result has thumbs up and thumbs down buttons. Use them to tell the AWS FinOps Agent team whether a specific response or task result was useful.
+ **In a chat conversation.** The buttons appear after each agent response. Choose them to rate that turn.
+ **On a task result.** The buttons appear at the bottom of the task detail page. Choose them to rate the overall result of the task.

When you choose **thumbs up**, the rating is submitted immediately. No comment is required.

When you choose **thumbs down**, a dialog opens so you can explain what was wrong. Select one or more categories and add an optional free-text comment.


| Category | When to choose | 
| --- | --- | 
| Harmful | The response contained content that was harmful, unsafe, or violated policy. | 
| Not accurate | The numbers, claims, or analysis were factually wrong. | 
| Not useful or incomplete | The response missed the question, was too vague, or stopped short of what was asked. | 
| Something else | None of the categories above fits. Use the comment field to describe the issue. | 

Feedback you submit is associated with the conversation turn or task you rated.

### Documentation feedback
<a name="submitting-feedback-docs-feedback"></a>

To submit feedback about this user guide (corrections, missing information, suggestions), choose **Feedback** at the bottom of any page. Documentation feedback is routed to the AWS FinOps Agent documentation team.