

# Types of tools

AWS Quick supports two methods of invoking tools, each serving different use cases and authentication models.

## On-demand tools
<a name="qbs-actions-types-qbs-actions-on-demand"></a>

On-demand tools run immediately when you trigger them. These tools support interactive operations that require real-time response.

**Key characteristics:**
+ User-initiated execution - You trigger tools through natural language in the chat interface.
+ Interactive form completion - You fill out forms with required parameters before the tool runs.
+ Immediate response - Tools run in real time and provide instant feedback on success or failure.
+ Personal authentication (3LO) - Uses your individual credentials and permissions from the target service.

**Common use cases:**
+ Creating tickets in Jira.
+ Sending messages in Slack.
+ Updating Salesforce records.
+ Retrieving information from SharePoint.

## Automated workflows
<a name="qbs-actions-types-qbs-actions-automated-workflows"></a>

Automated workflows run tools on a schedule or in response to specific triggers. These are useful for background and system-level operations.

**Key characteristics:**
+ System-level execution - Tools run automatically without user intervention based on predefined triggers.
+ Scheduled or event-triggered - Run on time-based schedules or in response to specific system events.
+ Non-interactive operation - Run in the background without requiring user input or form completion.
+ Service-level authentication - Use system credentials rather than individual user authentication.

**Common use cases:**
+ Regular data synchronization.
+ Scheduled report generation.
+ Automated ticket updates.
+ System health checks.