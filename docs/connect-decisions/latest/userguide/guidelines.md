

# Guidelines
<a name="guidelines"></a>

## Guidelines for Root Causes and Recommendations
<a name="guidelines-root-causes-and-recommendations"></a>

Guidelines help shape how Amazon Connect Decisions generates root cause analysis and recommendations for insights. These guidelines act as policies that ensure AI-generated explanations and suggested actions align with your business practices and operational constraints.

**Accessing Guidelines:** From the Insights Configuration page, select the **Root Causes & Recommendations** tab.

**What Guidelines Do:** Guidelines provide context and constraints that influence how the system:
+ Analyzes root causes of insights and alerts
+ Generates actionable recommendations for resolution
+ Prioritizes remediation approaches based on your business rules
+ Adapts guidance to your operational environment and supply chain constraints

## Working with your onboarding teammate
<a name="guidelines-working-with-onboarding-teammate"></a>

Use your onboarding teammate to create and refine guidelines conversationally. Ask questions like:
+ "Create a guideline to prioritize replenishment for high-velocity SKUs during promotional periods"
+ "Add a guideline to flag slow-moving inventory exceeding 45 days of cover for markdown review"
+ "Can we create a guideline that ensures minimum order quantities align with vendor lead times?"

Share your standard operating procedures or business policies to help the teammate understand your requirements. The teammate analyzes your inputs and translates them into guidelines and guardrails that shape AI teammate's behavior.

## Creating Guidelines
<a name="guidelines-creating"></a>

To create a new guideline, you can either:
+ **Use natural language:** Ask the onboarding teammate to create guidelines for you. For example: "Create a guideline that prioritizes inventory reduction strategies over expedited shipping when addressing excess inventory."
+ **Use the Create Guideline button:** Click **Add guidelines** to define parameters directly.

## Example Guidelines
<a name="guidelines-examples"></a>
+ "Prioritize replenishment for high-velocity SKUs during promotional periods"
+ "Ensure minimum order quantities align with vendor lead times"
+ "Monitor for demand spikes driven by seasonal or promotional activity"
+ "Escalate stockout risks for A-class products to planning managers within 24 hours"

## Reviewing and Editing Guidelines
<a name="guidelines-reviewing-and-editing"></a>

Select any guideline to view its configuration. Work with the onboarding teammate to understand how the guideline influences insights. Ask questions like:
+ "How does this guideline affect recommendations for excess inventory insights?"
+ "Can we make this guideline more specific to A-class products?"
+ "Show me examples of recommendations before and after applying this guideline"

## Activating Guidelines
<a name="guidelines-activating"></a>

Guidelines operate with a Draft/Ready status model:

1. Create and refine guidelines in Draft status to test their impact

1. Iterate with the onboarding teammate until the guideline produces desired behavior

1. Change status to **Ready** to apply the guideline to all future root cause analysis and recommendations

1. Click **Save changes** to activate

Active guidelines immediately influence how the system analyzes insights and generates recommendations.