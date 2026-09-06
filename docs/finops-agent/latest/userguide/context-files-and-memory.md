

AWS FinOps Agent is in preview release and is subject to change.

# Reflect your organization with context files and memory
<a name="context-files-and-memory"></a>

The agent uses two inputs to apply your organization's structure: context files that you upload, and memory that the agent records from your preference. The agent uses both automatically the next time it answers a question, generates a report, or runs an automation.

## Apply your accounts, owners, and policies with context files
<a name="cfm-context-files"></a>

Context files let the agent answer using your organization's terms. Upload an account-to-owner mapping and the agent attributes spend to the right teams. Upload a cost category definition and the agent uses your categories in reports. Upload custom instructions and the agent follows them on every run. Without context files, the agent works from generic AWS data; with them, the agent's answers, reports, and tickets reflect your accounts, owners, and review cycles.

Start with an account-to-team mapping. This is the most useful context file to upload first, because it lets the agent attribute cost to the team that owns each account.

```
account_id,team_name,team_lead,email
123456789012,Data Platform,Jane Smith,jsmith@example.com
234567890123,ML Training,Alex Chen,achen@example.com
345678901234,Production,Sam Lee,slee@example.com
```

Commonly useful context files:


| Context file | What it lets the agent do | 
| --- | --- | 
| Account-to-team mapping | Attribute spend to the team that owns each AWS account, and route Jira tickets to the responsible owner. | 
| Organization structure | Allocate cost across business units, and explain reporting relationships in chargeback summaries. | 
| Custom instructions | Apply your rules every time. For example: "Ignore EC2 rightsizing recommendations for accounts tagged env=production" or "When creating Jira tickets, use the FINOPS project." | 
| Company background | Calibrate the agent's communication style to your business and FinOps maturity level. | 
| Report templates | Replicate the format and structure of reports your stakeholders already expect. | 

The web application accepts the file types listed in the next section. Context files are read-only from the agent's perspective; the agent cannot modify or delete them through conversation.

**Important**  
Do not upload files that contain sensitive or personal information. Context files are visible to anyone who has access to the agent.

## Supported file types and limits
<a name="cfm-supported-file-types"></a>

The web application accepts the following file types for context file upload:
+ Plain text (`.txt`)
+ CSV (`.csv`)
+ JSON (`.json`)
+ Markdown (`.md`)
+ HTML (`.html`)
+ YAML (`.yaml`, `.yml`)

Files outside these types are rejected before upload.

The following limits apply per agent. For all per-agent quotas, see [Quotas](quotas.md).


| Limit | Value | 
| --- | --- | 
| Maximum file size per upload | 10 MB | 
| Total context file storage per agent | 100 MB | 

## Manage context files
<a name="cfm-managing-context-files"></a>

Upload, delete, and restore context files from the **Context files** workspace in the web application. Choosing **Delete** on a file soft-deletes it, removing it from the agent's active context. Choose **Restore** on a soft-deleted file to make it active again.

Keep individual files focused on a single topic (for example, one file for account-to-team mappings, another for custom instructions) so the agent can locate the right information efficiently.

## Agent memory across sessions
<a name="cfm-memory"></a>

The agent remembers preferences and corrections you provide, then applies them in future sessions. For example, tell the agent that the data platform team owns a set of accounts, that you want costs broken down by Region, or that a class of recommendation does not apply. The agent applies that preference the next time it runs.

Examples of what the agent stores in memory:
+ Your name and role.
+ AWS account IDs and their owners.
+ Preferred cost views or report formats.
+ Jira space keys and team assignments.
+ Outcomes of past investigations or tasks.
+ Corrections you provide during conversation.

You can instruct the agent to remember, update, or forget information through natural language during conversation.

## Long conversation handling
<a name="cfm-long-conversation-handling"></a>

The agent operates within a fixed-size context window based on the underlying large language model. Each message in a conversation adds to the context. When the conversation approaches the limit, the agent automatically summarizes older messages to make room for new ones. The agent retains the most recent messages in full and replaces older portions with a summary that preserves the key findings, decisions, and current state of the conversation.

For details on how context files, memory, and reports are stored and secured, see [Data protection](data-protection.md).