

# Audit
<a name="acxd-audit"></a>

Audit gives governance and administrator teams a centralized place to review change activity inside an agentic CX designer workspace.

Audit logs capture write and delete events across workspace resources such as applications, flows, integrations, guardrails, and more. This makes it easier to reconstruct change history, investigate unexpected configuration changes, and support internal review or compliance processes.

Use Audit to:
+ Trace configuration changes that may affect application behavior
+ Confirm who created, updated, or removed a resource
+ Review activity around sensitive or production-impacting assets
+ Support security or governance investigations
+ Monitor adherence to internal change-management processes
+ Provide evidence of workspace activity for audit or compliance reviews

To access Audit, select your username from your workspace menu, choose **Settings**, then select **Audit**.

## Audit events
<a name="acxd-audit-events"></a>

Each row in the Audit table provides details about a workspace event.


|  |  | 
| --- |--- |
| **Description** | A short description of the change, such as updating a flow or deleting an integration. | 
| **Source** | The workspace area or system component where the change occurred, such as Canvas, Integrations, or Workspace settings. | 
| **Action** | The type of action, such as Write or Delete. | 
| **Timestamp** | When the event occurred. | 
| **User** | The user who performed the action. | 

## Filtering audit logs
<a name="acxd-audit-filters"></a>

Use filters at the top of the Audit page to narrow the log to the activity you want to review.

Filtering helps you quickly find the most relevant events when investigating a change, reviewing user activity, or confirming when a resource was updated.


|  |  | 
| --- |--- |
| **Date range** | Limit results to a specific date and time range. | 
| **User** | View events performed by a specific user. | 
| **Action type** | Filter by action type, such as Write or Delete. | 
| **Event type** | Focus on a specific kind of change, such as a deployment event or resource update. | 