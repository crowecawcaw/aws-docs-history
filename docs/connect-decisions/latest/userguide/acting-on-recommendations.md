

# Acting on Recommendations
<a name="acting-on-recommendations"></a>

The Insights Details page allows you to review and act on system-generated recommendations designed to resolve supply chain issues. This page explains how to evaluate recommendations and execute the suggested actions. You can configure Amazon Connect Decisions to interact with an external system to perform certain operations on your behalf; when enabled, Amazon Connect Decisions will offer to perform the actions recommended through the Insights (e.g.: creating, updating, or canceling Purchase Orders).

**Note**  
When you use the Actions feature, you authorize Amazon Connect Decisions to use Boomi ([boomi.com](https://boomi.com/)) as our integration middleware to transmit and process the data needed to take actions on your behalf, such as creating a purchase order after approval in our platform; no data is stored within Boomi.

## Understanding Recommendations
<a name="acting-on-recommendations-understanding"></a>

Recommendations are AI-generated suggestions for addressing insights. Each recommendation includes:
+ **Specific action**: What to do (for example, create purchase order, transfer inventory)
+ **Parameters**: Quantities, locations, dates, and other details
+ **Rationale**: Why this action is recommended
+ **Expected outcome**: How this action will resolve the insight

Recommendations are prioritized based on impact, feasibility, and urgency to help you focus on the most effective solutions.

## Reviewing Recommendations
<a name="acting-on-recommendations-reviewing"></a>

Before taking action, review the recommendation details:
+ **Read the recommendation title and description**: Understand what action is being suggested
+ **Expand the recommendation card**: Select the arrow icon to view complete details
+ **Review the rationale**: Understand why this action is recommended
+ **Check the parameters**: Verify quantities, locations, dates, and other specifics
+ **Assess the expected outcome**: Evaluate whether this action aligns with your business needs

## Available Actions
<a name="acting-on-recommendations-available-actions"></a>

For each recommendation, you have several action options:

### Accept
<a name="acting-on-recommendations-accept"></a>

Select **Accept** to approve the recommendation and proceed with the suggested action.

**When you accept a recommendation:**
+ The insight status changes to "In Progress"
+ The recommendation is marked as accepted
+ Related insights may be updated if applicable
+ The system tracks the action for future reference

**To accept a recommendation:**

1. Review the recommendation details

1. Select the **Accept** button

1. Confirm the action if prompted

1. The system updates the insight status and begins tracking implementation

### Action Taken
<a name="acting-on-recommendations-action-taken"></a>

Select **Action Taken** when you have addressed the issue through other means outside the system.

**When you mark action taken:**
+ The insight status changes to "Pending Resolution"
+ The system tracks that action was taken manually
+ The insight will be marked as complete once data confirms resolution

**To mark action taken:**

1. Complete the necessary action in your external systems

1. Return to the Insights Details page

1. Select **Action Taken**

1. The system updates the insight status

## Recommendation Lifecycle
<a name="acting-on-recommendations-lifecycle"></a>

Recommendations follow a lifecycle based on your actions:

Not Started  
The recommendation has been generated but not yet acted upon

In Progress  
You have accepted the recommendation or initiated action

Pending Resolution  
Action has been taken but the issue is not yet fully resolved in the data

Completed  
The system has confirmed through data that the action successfully resolved the insight

## Multiple Recommendations
<a name="acting-on-recommendations-multiple"></a>

Some insights may have multiple recommendations:

**Primary Recommendation**: The system's top suggestion based on analysis

**Alternative Recommendations**: Additional options if the primary recommendation is not feasible

**To choose between recommendations:**

1. Review all available recommendations

1. Compare the expected outcomes and feasibility

1. Select the recommendation that best fits your business needs and constraints

1. Take action on your chosen recommendation

You can only accept one recommendation per insight. Once you accept a recommendation, other recommendations for that insight become unavailable.

## Grouped Recommendations
<a name="acting-on-recommendations-grouped"></a>

When multiple insights share the same root cause, the system may group recommendations:

**Grouped recommendation benefits:**
+ Resolve multiple insights with a single action
+ More efficient insight management
+ Clearer view of systemic issues

**When viewing a grouped recommendation:**
+ The recommendation shows all affected insights
+ Taking action on the grouped recommendation affects all related insights
+ All related insights move to "In Progress" when you accept the grouped recommendation

## Tracking Action Progress
<a name="acting-on-recommendations-tracking"></a>

After taking action on a recommendation:
+ **Monitor the Activity Log**: Check the Activity Log section for updates on your action
+ **Review related insights**: See if related insights are also being resolved
+ **Check the insight status**: The status indicator shows current progress
+ **Wait for data confirmation**: The system monitors data for changes that indicate resolution

Once the system confirms through data that the action was successful, the insight status automatically updates to "Completed."

## Best Practices
<a name="acting-on-recommendations-best-practices"></a>

**Review thoroughly before acting**: Ensure you understand the recommendation and its implications

**Consider business constraints**: Verify that the recommended action aligns with your operational capabilities and business rules

**Act promptly on critical insights**: Critical insights with near-term impact dates require immediate attention

**Provide feedback**: Use thumbs up/down icons to help the system improve future recommendations

**Monitor outcomes**: Track whether accepted recommendations successfully resolve insights