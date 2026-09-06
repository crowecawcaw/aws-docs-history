

# In-Canvas analytics
<a name="acxd-in-canvas-analytics"></a>

In-Canvas analytics helps you understand how users move through a deployed flow directly from the Canvas.

When analytics mode is enabled, each node displays traffic data showing how many unique conversations reached that node. This helps you identify common paths, underused branches, drop-off points, A/B testing results, and whether users are reaching the intended completion steps.

Use In-Canvas analytics to answer questions like:
+ Which nodes are users reaching most often?
+ Where are users dropping off?
+ Are users reaching the expected success path?
+ Are fallback or escalation paths being used more than expected?
+ Did a specific conversation follow the path you expected?
+ Does the flow behave as expected after deployment?

**Important**  
A build that includes the flow must be deployed before In-Canvas analytics can display conversation traffic.

## Viewing In-Canvas analytics
<a name="acxd-in-canvas-analytics-view"></a>

**To view In-Canvas analytics**

1. Open **Flows** from the workspace menu.

1. Select **Canvas**.

1. Choose the flow you want to review.

1. Select the **Analytics** icon from the Canvas toolbar.

1. Review the traffic indicators displayed on each node.

To turn off In-Canvas analytics, select the Analytics icon again.

You can continue editing a flow while analytics mode is enabled. If you make changes that should affect live behavior, create a new build and deploy it before expecting updated deployed traffic to reflect the new flow version.

## Traffic indicators
<a name="acxd-in-canvas-analytics-indicators"></a>

When In-Canvas analytics is enabled, each node displays a number that represents how many unique conversations reached that node during the selected filter period.

Use these indicators to quickly compare:


|  |  | 
| --- |--- |
| **High traffic** | Many users are reaching this point in the flow. | 
| **Low traffic** | Users may not be reaching the intended route. | 
| **Unexpected fallback traffic** | Users may be confused, unsupported, or encountering errors. | 
| **Drop-off before completion** | The flow may be too long, unclear, or blocked by missing information. | 
| **Uneven split traffic** | Routing, conditions, or state may need review. | 

In-Canvas analytics is especially useful when you want to connect a performance signal to the exact path users took inside a flow.

## Filters
<a name="acxd-in-canvas-analytics-filters"></a>

Use filters to refine the analytics view and focus on the conversations that matter most.


|  |  | 
| --- |--- |
| **Application** | Review data for a specific application, especially when a flow is attached to more than one application. | 
| **Conversation ID** | View the path taken during one specific conversation retrieved from conversation history. | 
| **Start date** | Set the beginning of the date and time range. | 
| **End date** | Set the end of the date and time range. | 
| **Analytics tags** | Focus on conversations that reached nodes with selected analytics tags. | 

Filters help you narrow your review when investigating a release window, a specific user session, a known issue, or a tagged milestone.

## Using a Conversation ID
<a name="acxd-in-canvas-analytics-conversation-id"></a>

You can use a Conversation ID to inspect the exact path from one conversation:

1. Open the deployed application.

1. Go to **Observe**.

1. Open a conversation from the **Conversation history** table.

1. Copy the **Conversation ID**.

1. Open the flow involved in that conversation.

1. Enable **In-Canvas analytics**.

1. Paste the Conversation ID into the filter field.

1. Review the path the user took through the flow.

This is helpful when a transcript shows unexpected fallback behavior, repeated questions, missed routing, a failed integration, or user drop-off.