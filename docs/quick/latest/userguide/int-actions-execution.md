

# Action execution methods
<a name="int-actions-execution"></a>

Amazon Quick provides multiple ways to execute actions, accommodating different use cases and interaction preferences.

## Chat interface
<a name="qbs-actions-execution-qbs-actions-chat-interface"></a>

You can execute implicit actions in the Amazon Quick chat.

### Implicit actions
<a name="qbs-actions-execution-qbs-actions-implicit-actions"></a>

Amazon Quick also supports implicit action execution through natural conversation with agents. Using advanced natural language processing, the system can identify when your conversation indicates the need for specific actions. Conversations are analyzed to determine which actions are required to fulfill your request.

A single request might require multiple actions to complete. When this happens, the system handles these actions sequentially, guiding you through each step. For each identified action, the system presents the appropriate form for you to complete. After each action completes, you receive a confirmation before moving on to the next action in the sequence.

For example, if you ask "Create a Jira ticket for this issue and notify the team in Slack," the system would:

1. First present the Jira ticket creation form.

1. After completing the ticket creation, show the Slack message form.

1. Complete both actions in sequence.

Throughout the process, you can track your progress through multiple actions. When all actions complete, the system provides a comprehensive summary showing all executed actions and their outcomes. You can access related documentation if needed and review any error states that may have occurred during the process.