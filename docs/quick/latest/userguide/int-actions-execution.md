

# Tool execution methods

AWS Quick provides multiple ways to run tools, accommodating different use cases and interaction preferences.

## Chat interface
<a name="qbs-actions-execution-qbs-actions-chat-interface"></a>

You can run implicit tools in the AWS Quick chat.

### Implicit tools
<a name="qbs-actions-execution-qbs-actions-implicit-actions"></a>

AWS Quick also supports implicit tool execution through natural conversation with agents. Using advanced natural language processing, the system can identify when your conversation indicates the need for specific tools. Conversations are analyzed to determine which tools are required to fulfill your request.

A single request might require multiple tools to complete. When this happens, the system handles these tools sequentially, guiding you through each step. For each identified tool, the system presents the appropriate form for you to complete. After each tool runs, you receive a confirmation before moving on to the next tool in the sequence.

For example, if you ask "Create a Jira ticket for this issue and notify the team in Slack," the system would:

1. First present the Jira ticket creation form.

1. After completing the ticket creation, show the Slack message form.

1. Complete both tools in sequence.

Throughout the process, you can track your progress through multiple tools. When all tools finish, the system provides a comprehensive summary showing all tools that ran and their outcomes. You can access related documentation if needed and review any error states that may have occurred during the process.