

AWS Well-Architected Agent is in preview release and is subject to change.

# Goals and personalization in AWS Well-Architected Agent
<a name="agent-goals"></a>

AWS Well-Architected Agent uses business goals to prioritize and rank your recommendations. The goals you define during onboarding directly shape which recommendations appear first and how they align with your organization's objectives.

## Immediate value and personalized experience
<a name="agent-immediate-value"></a>

AWS WA Agent provides two tiers of value depending on how much context you provide:
+ **Immediate value (no setup):** Baseline recommendations are available out-of-the-box with no configuration. AWS WA Agent surfaces findings from AWS Trusted Advisor and CloudWatch automatically.
+ **Personalized experience (with onboarding):** When you complete the onboarding workflow and declare business goals, permission boundaries, organizational metadata, and tagging conventions, AWS WA Agent delivers fully personalized, goal-aligned recommendations ranked by business impact.

## How goals drive recommendations
<a name="agent-how-goals-work"></a>

Your personalized recommendations in AWS WA Agent are based on goals that you define in your AWS WA Agent profile. Business goals guide the analysis and recommendation prioritization. Each goal consists of the following:
+ **Goal statement:** A natural language description of your business objective. Make goals specific, measurable, and time-bound for best results.
+ **Target pillar:** The optimization pillar that the goal addresses (Cost optimization, Security, Resilience, or Performance).

AWS WA Agent uses your goals to rank recommendations by relevance and potential impact against your stated objectives. Each recommendation is annotated with the goals that contributed to its generation.

## View your goals in the dashboard
<a name="agent-view-goals-dashboard"></a>

The AWS WA Agent dashboard contains a total of five active goals. By default, the dashboard displays up to three of your active goals. To see all your active goals, choose **View all goals**.

Your active goals represent your organization's strategic objectives and priorities. Active goals help generate personalized recommendations that align with your business needs.

Each recommendation also contains the associated goals that the recommendation is based on. To see the associated goals for a recommendation, in the **Recommendation details** page, choose **view associated goals**.

## Tips for writing effective goals
<a name="agent-goal-best-practices"></a>

The quality of your business goals directly affects how well AWS WA Agent prioritizes and ranks recommendations. Follow these guidelines when defining goals:
+ **Be specific:** Vague goals like "improve security" produce broadly ranked recommendations. Specific goals like "eliminate all public Amazon S3 buckets" produce focused, actionable results.
+ **Include metrics:** Goals with quantifiable targets (for example, "reduce infrastructure cost by 20% year-over-year") allow AWS WA Agent to calculate progress and prioritize by impact.
+ **Specify timeframes:** Time-bound goals help AWS WA Agent prioritize quick wins over long-term improvements when appropriate.
+ **Name the pillar explicitly:** While AWS WA Agent can infer the pillar from goal text, explicitly associating a goal with its pillar (Cost optimization, Security, Resilience, or Performance) produces more accurate targeting.
+ **Avoid overlapping goals:** Multiple goals targeting the same pillar with similar intent can dilute prioritization. Consolidate related objectives into a single, well-defined goal.