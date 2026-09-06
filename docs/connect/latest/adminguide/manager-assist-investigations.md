

# Investigations and recommendations in manager assist
<a name="manager-assist-investigations"></a>

When you ask a question that starts with **why**, or when you request an investigation into a metric change, an investigation runs. An investigation is a multi-step analysis that goes beyond returning a single metric value: it examines multiple related data points across your contact center to identify which factors contributed to the change, and what you can do about it.

**Important**  
Responses generated during investigations might contain inaccuracies. Investigations identify correlations in your data, and cannot confirm definitive root causes. Always validate investigation findings before you make operational decisions.

## How investigations work
<a name="manager-assist-investigations-how"></a>

When you ask an investigative question, the following steps are performed:

1. **Identify** – determines the metric or condition that you want explained.

1. **Investigate** – examines related metrics across multiple dimensions, including agent activity, contact patterns, and historical trends.

1. **Correlate** – identifies patterns and contributing factors across your contact center data.

1. **Recommend** – returns the findings with recommended actions.

## Example investigation
<a name="manager-assist-investigations-example"></a>

The following example shows an investigation of a service level drop, starting with this question: **Our service level is impacted in the last hour but volume looks normal. Investigate what happened.**

When a potential issue is identified, investigation prompts are also suggested. Choosing a prompt starts the multi-step analysis.

![A response that reports a service level of 40.6 percent against an 80 percent target, followed by suggested prompts to investigate the low service level, break it down by queue, and show the trend by day.](http://docs.aws.amazon.com/connect/latest/adminguide/images/manager-assistant-investigation-prompts.png)


During the investigation, a processing state is displayed while multiple data dimensions are examined. Investigations require more processing time than standard metric lookups, so expect responses to take longer than they do for a simple question.

![An investigation prompt in the chat, with a processing indicator displayed while the analysis runs.](http://docs.aws.amazon.com/connect/latest/adminguide/images/manager-assistant-investigation-progress.png)


When the investigation is complete, a structured analysis is returned. The format varies with the complexity of the issue, and typically includes the major contributing factors, the factors that were eliminated, and recommended actions.

![Investigation results that list a staffing shortage as the primary driver, abandonment as an amplifying factor, and contact volume and handle time as factors that did not contribute.](http://docs.aws.amazon.com/connect/latest/adminguide/images/manager-assistant-investigation-results.png)


Following the analysis of the major contributing factors, prioritized recommended actions are provided. Each recommendation includes the reasoning for why it addresses the identified issue, and might include a confidence indicator that reflects how directly the action addresses that issue. The following table shows example recommended actions for this investigation.


| Priority | Action | Confidence | 
| --- | --- | --- | 
| Immediate | Escalate to workforce management to restore staffing for the remainder of today. Identify why agents are absent: unscheduled absences, status misuse, or a scheduling gap. With volume down 28 percent, even a partial staffing restoration should recover service level quickly. | High | 
| Now | Enable queue callbacks to deflect the 59 percent of contacts that are currently abandoning. Each callback converts an abandonment into a recoverable contact, and reduces the wait for other customers. | Medium | 
| Avoid | Do not increase agent concurrency as a substitute for headcount. Handle time is already low (about 122 seconds), so the bottleneck is the number of agents online, not how quickly they handle contacts. Adding concurrency to an understaffed queue does not resolve the issue, and risks quality degradation. | Not applicable | 
| Strategic | Investigate the Friday baseline. Last Friday's service level of 48.7 percent was also well below target, which suggests that this is not a one-time event. A structural review of Friday staffing is warranted. | High | 

## Characteristics of investigation responses
<a name="manager-assist-investigations-characteristics"></a>
+ **Baseline comparison** – each finding is compared against the same day of the week in the prior period, rather than against an arbitrary threshold.
+ **Primary and secondary attribution** – investigations distinguish contributing factors from symptoms. For example, because abandoned contacts are excluded from average speed of answer, that metric can appear healthy while customers are abandoning.
+ **Explicit elimination** – when a factor did not contribute, such as contact volume in the preceding example, the response states that with supporting data.
+ **Reasoning in recommendations** – each recommended action explains why it addresses the issue.
+ **Signal strength** – when the available data is insufficient to support a conclusion, such as a low number of evaluations, the response reports the absence of a signal instead of drawing an unsupported conclusion.

## Tips for effective investigation questions
<a name="manager-assist-investigations-tips"></a>


| Instead of this | Try this | 
| --- | --- | 
| Why are things bad? | Our service level dropped to 40 percent in the last hour but volume looks normal. What happened? | 
| What is wrong? | Why is average handle time higher today compared to last Tuesday? | 
| Fix the queue. | What caused the abandonment spike in the Support queue between 2 PM and 3 PM? | 

## Supported investigations
<a name="manager-assist-investigations-supported"></a>

You can start an investigation by asking why questions such as the following.


| Investigation type | Example question | 
| --- | --- | 
| Service level drop | Our service level dropped to 40.6 percent but volume looks normal. What happened? | 
| Handle time increase | Why is handle time 2 minutes higher today than last Tuesday? | 
| Abandonment spike | What caused the abandonment spike in the last hour? | 
| Volume anomaly | Why did volume spike 50 percent today? | 
| Occupancy change | Why is occupancy at 30 percent when we are fully staffed? | 
| Adherence gap | Why is adherence low today across the billing team? | 
| Agent performance variance | Why are 3 agents handling twice the average handle time of the rest of the team? | 

## Important considerations
<a name="manager-assist-investigations-considerations"></a>
+ Investigations are read-only. They cannot make changes to your contact center configuration.
+ Findings identify correlations and relationships in your data. They are not guaranteed root causes.
+ When the available data is insufficient to support a conclusion, the response states that explicitly instead of speculating.
+ Investigations examine the same data that is available in your Connect Customer dashboards and reports.