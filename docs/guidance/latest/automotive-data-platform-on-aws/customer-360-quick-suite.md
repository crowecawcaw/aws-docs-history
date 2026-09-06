

# Quick Suite Analytics
<a name="customer-360-quick-suite"></a>

Quick Suite is AWS’s unified business intelligence platform that combines interactive dashboards, AI-powered analytics agents, and automated workflows to help organizations move from insight to action in a single integrated experience.

## Value proposition
<a name="value-proposition"></a>

Dashboards show what happened, but they can’t tell you why or what to do next—that still requires hours of manual investigation. Quick Suite goes beyond visualization by:
+ Automatically analyzing root causes when metrics decline
+ Matching issues to proven remediation playbooks
+ Triggering approval workflows before problems escalate
+ Generating executive-ready reports with actionable recommendations

Instead of manually sifting through data and coordinating across departments, agentic workflows instantly generate reports, create approval tasks, and notify the right people via Slack—all without writing code. What used to take days of cross-team coordination now happens in minutes, with built-in human approval checkpoints that keep you in control.

## Building dashboards
<a name="building-dashboards"></a>

Quick Suite dashboards visualize customer sentiment, NPS scores, and quality issues across all touchpoints.

![Quick Suite Dashboard - Executive Summary and Trends](http://docs.aws.amazon.com/guidance/latest/automotive-data-platform-on-aws/images/quick-suite-dashboard1.jpg)


![Quick Suite Dashboard - Detailed Analytics](http://docs.aws.amazon.com/guidance/latest/automotive-data-platform-on-aws/images/quick-suite-dashboard-2.jpg)


### Dashboard components
<a name="dashboard-components"></a>

 **Executive summary**: \* Current NPS score with trend indicator \* Customer health score distribution \* Total at-risk revenue \* Month-over-month changes

 **Sentiment analysis**: \* Sentiment trend over 12 months \* Breakdown by channel (mobile, dealer, contact center, in-vehicle) \* Top issues driving negative sentiment \* Correlation with service quality

 **Quality issues**: \* Issue category breakdown (battery, software, connectivity) \* Battery issue trend (15% → 40%) \* Geographic distribution \* Vehicle model comparison

 **Revenue impact**: \* Revenue by stream (sales, service, subscriptions) \* At-risk revenue by segment \* Churn impact on lifetime value \* Recovery opportunity sizing

### Creating datasets
<a name="creating-datasets"></a>

Quick Suite datasets connect to Athena views:

 **Pre-built datasets**: 1. kpi\_trends - Monthly NPS and health scores 2. sentiment\_analysis - Sentiment by channel 3. issue\_categories - Issue breakdown 4. revenue\_streams - Revenue by stream 5. at\_risk\_revenue - Revenue at risk 6. customer\_segments - Segment analysis 7. service\_quality - Operational metrics 8. churn\_analysis - Churn risk factors

### Dashboard features
<a name="dashboard-features"></a>

 **Interactive elements**: \* Drill-down to underlying data \* Filters for time range, segment, model, region \* Parameters for dynamic thresholds \* Actions to navigate or link to external systems

 **AI-powered insights**: \* Anomaly detection for unusual patterns \* Forecasting future trends \* Natural language queries \* Auto-generated narrative summaries

### Using the AI chat agent
<a name="using-the-ai-chat-agent"></a>

Quick Suite integrates Bedrock agents for conversational analytics:

```
"What's causing declining customer sentiment?"
"Show me battery issues by vehicle model"
"Which segments have highest churn risk?"
"What's the revenue impact of thermal issues?"
```

## Building Quick Suite automations
<a name="building-quick-suite-automations"></a>

Quick Automate combines Bedrock agents with your knowledge base to continuously monitor customer sentiment, automatically identify root causes when scores drop, and match issues to proven remediation playbooks. The result is an executive-ready report with recommended actions and approval workflows—delivered in minutes instead of days of manual analysis.

![Quick Suite Automate - Workflow Configuration](http://docs.aws.amazon.com/guidance/latest/automotive-data-platform-on-aws/images/quick-suite-automate.jpg)


### Customer sentiment automation
<a name="customer-sentiment-automation"></a>

This workflow monitors sentiment daily and triggers remediation when critical issues are detected. The automation runs without code, using natural language prompts to configure each step.

 **Workflow steps**:

1.  **Sentiment Analysis** (Bedrock Agent - Steps 1-3)
   + Query customer sentiment data from Athena
   + Analyze trends and identify critical issues
   + Generate three agent responses with different perspectives
   + Output: agent\_response\_41, agent\_response\_42, agent\_response\_43

1.  **Criticality Check** (Code Block - Step 4.4)
   + Combine all agent responses
   + Check for "critical" sentiment indicators
   + Identify needed workflows (Battery Replacement, BMS Repair, Thermal Management)
   + Output: tasks\_to\_create list with workflow details

1.  **Loop Through Critical Items** (Step 4.5)
   + Iterate over each workflow needing action
   + Process each issue independently

1.  **Prepare Task Data** (Code Block - Steps 4.6-4.7)
   + Generate unique reference ID for tracking
   + Build custom data JSON with issue details
   + Calculate revenue at risk

1.  **Case Creation** (Step 4.8)
   + Create case in Task Center
   + Case Type: Customer Sentiment
   + Store case\_id for tracking

1.  **Create Approval Tasks** (Step 4.9)
   + Create human-in-the-loop (HITL) approval task
   + Assign to appropriate resolver based on issue type
   + Set 24-hour due date for critical issues
   + Include context and revenue at risk

1.  **Search and Retrieve Cases** (Steps 4.10-4.11)
   + Retrieve all created cases with IDs
   + Prepare data for report generation

1.  **Generate Executive Report** (Step 4.12\+)
   + Agent generates HTML report using natural language prompts
   + Include root causes, revenue impact, and remediation workflows
   + Upload to S3 bucket
   + Serve via CloudFront at public URL
   + Report includes one-click buttons to launch approval flows

1.  **Notification** (Final Step)
   + Alert \#customer-experience-alerts in Slack
   + Include report link and approval workflows
   + @mention stakeholders based on severity

 **Key capabilities**:
+ No code required - entire workflow built with natural language prompts
+ Bedrock agents query your knowledge base for context-aware analysis
+ Human approval checkpoints keep you in control
+ Executive reports generated automatically with customizable format
+ Integrates with existing tools (Slack, Jira, Task Center)

### Executive sentiment report
<a name="executive-sentiment-report"></a>

The executive sentiment report is generated entirely through natural language prompts—no code, no templates, no IT tickets required. It automatically surfaces critical customer issues, calculates revenue at risk, and presents actionable remediation workflows with clear approval checkpoints.

 **Report components**:
+  **Executive summary** - High-level overview of sentiment trends and critical issues
+  **Root cause analysis** - AI-generated analysis of why sentiment declined
+  **Revenue impact** - Calculated revenue at risk by issue category
+  **Remediation workflows** - Proven playbooks matched to each issue type
+  **Approval checkpoints** - Clear indication of where human judgment is needed
+  **One-click actions** - Buttons to launch approval flows directly from report

 **Customization**:

Business users can customize the report format, add new workflows, or change approval routing simply by updating the prompt—putting control in the hands of the people closest to the customer. No development required.

 **Example report sections**:

```
Critical Issues Detected:
- Battery degradation affecting 847 vehicles
- Revenue at risk: $2.3M
- Recommended action: Battery Replacement Program
- [Start Approval Flow] button

Thermal Management Issues:
- 312 vehicles reporting cabin temperature problems
- Revenue at risk: $890K
- Recommended action: BMS Software Update
- [Start Approval Flow] button
```

### Agent prompts
<a name="agent-prompts"></a>

The automation uses natural language prompts to configure Bedrock agents. Here are the actual prompts used in the workflow:

 **Sentiment analysis prompt (Steps 1-3)**:

```
Analyze customer sentiment over the last 90 days. Provide a brief summary in this format:

- Sentiment Status: [Declining/Stable/Improving]
- Decline Percentage: [X%]
- Top 3 Root Causes (identify SPECIFIC, MEASURABLE issues from the data -
  examples: Battery degradation, Service appointment delays, ADAS malfunctions,
  Connectivity failures, Support response time. Do NOT use vague categories
  like 'General Dissatisfaction'):
  1. [Specific Cause] - $[Amount] at risk, [X] customers
  2. [Specific Cause] - $[Amount] at risk, [X] customers
  3. [Specific Cause] - $[Amount] at risk, [X] customers
- Recommended Action: [One sentence]
```

 **Root cause analysis prompt**:

```
What specific product defects or issues are causing {sentiment_data['top_cause']}?
Provide exactly 3 issues in this format:

1. [Issue Name] - [Brief description]
2. [Issue Name] - [Brief description]
3. [Issue Name] - [Brief description]

Return nothing more.
```

 **Technical defect analysis prompt**:

```
What specific battery, charging, or vehicle component defects are causing
{agent_response_34['top_issue']}? List 3 specific technical problems in this format:

1. [Issue Name] - [Brief description]
2. [Issue Name] - [Brief description]
3. [Issue Name] - [Brief description]
```

 **Deep dive diagnostic prompt**:

```
Deep dive: {agent_response_37['defect_1']}

Return:
- severity: Critical/High/Medium
- customers: [count]
- revenue_at_risk: $[amount]
- diagnostic_pattern: [symptom matching playbook]
- key_indicator: [primary telemetry signal]
- evidence: [1 sentence]
```

 **Key prompt design principles**:
+ Be specific about output format - use exact templates
+ Request measurable data - dollar amounts, customer counts, percentages
+ Avoid vague categories - require specific, actionable issues
+ Limit response length - "exactly 3 issues", "one sentence"
+ Reference data sources - "from the data", "over the last 90 days"
+ Use examples - show what good responses look like

### Creating a workflow
<a name="creating-a-workflow"></a>

1. Navigate to Quick Automate

1. Click "Create automation"

1. Configure daily trigger at 6 AM

1. Add Bedrock agent step for analysis

1. Add code block for criticality check

1. Add loop for case creation

1. Add approval task step

1. Add report generation step

1. Add Slack notification

1. Test and deploy

### Best practices
<a name="best-practices"></a>

 **Workflow design**: \* Keep focused on single process \* Use clear naming conventions \* Add error handling \* Include retry logic

 **Agent prompts**: \* Be specific about requirements \* Include expected output format \* Reference knowledge base \* Iterate based on quality

## Creating approval flows with Quick Flows
<a name="creating-approval-flows-with-quick-flows"></a>

Quick Flows transforms the executive report from a static document into an interactive action center—one click launches a guided approval workflow that gathers context, notifies stakeholders via Slack, and routes decisions to the right people. Business users build these flows in minutes using plain English, connecting approvals to notifications without writing code or waiting on IT. The flows integrate directly with your existing tools like Slack and Task Center, so approvers act where they already work instead of logging into another system.

![Quick Flows - Approval Process Configuration](http://docs.aws.amazon.com/guidance/latest/automotive-data-platform-on-aws/images/quick-suite-flow.jpg)


### Campaign approval flow
<a name="campaign-approval-flow"></a>

Enables marketing managers to instantly notify stakeholders via Slack and route critical customer outreach campaigns for approval—turning a multi-day email chain into a one-click workflow.

 **Flow components**:

1.  **Context gathering** 
   + Retrieve campaign details from executive report
   + Calculate affected customers and segments
   + Pull historical campaign performance
   + Estimate revenue impact

1.  **Stakeholder notification** 
   + Send Slack message to \#marketing-campaigns
   + Include campaign summary and approval link
   + Set priority based on urgency and revenue
   + @mention relevant team members

1.  **Approval routing** 
   + Route to marketing manager for campaigns < $10K
   + Route to VP Marketing for campaigns > $10K
   + Escalate to CMO if no response in 4 hours
   + Track approval status in real-time

1.  **Action execution** 
   + On approval: Trigger campaign in marketing automation system
   + On rejection: Log reason and notify requester
   + Update dashboard status automatically
   + Send confirmation to all stakeholders

### Service repair authorization flow
<a name="service-repair-authorization-flow"></a>

Empowers service managers to review repair scope, cost estimates, and customer impact in seconds, then trigger approvals directly from Jira without logging into multiple systems.

 **Flow components**:

1.  **Repair scope review** 
   + Display affected VINs and vehicle models
   + Show cost per vehicle and total program cost
   + Include parts availability and lead times
   + Calculate customer impact and downtime

1.  **Cost impact analysis** 
   + Total program cost
   + Warranty claim impact
   + Customer satisfaction projection

1.  **Jira integration** 
   + Create ticket on approval
   + Assign to service operations
   + Link to quality report

1.  **Customer communication** 
   + Trigger notification workflow
   + Schedule appointments
   + Update customer portal

### Building a flow
<a name="building-a-flow"></a>

1. Navigate to Quick Flows

1. Click "Create flow"

1. Select "Approval workflow" template

1. Define trigger from automation

1. Add form inputs for review

1. Configure approval logic

1. Add Slack integration

1. Add action steps

1. Test and deploy

## Integration with existing tools
<a name="integration-with-existing-tools"></a>

Quick Suite workflows integrate with collaboration tools.

### Slack integration
<a name="slack-integration"></a>

 **Capabilities**: \* Real-time notifications for critical issues \* One-click approval buttons \* Thread-based discussions \* Status updates posted automatically

 **Message template**:

```
🚨 *Critical Customer Sentiment Alert*

*Issue*: Battery complaints increased 15%
*Affected Customers*: 12,450 (Premium)
*Revenue at Risk*: $2.3M
*Action*: Battery replacement program

📊 <link|Executive Report>
✅ <link|Approve> ❌ <link|Reject>
```

### Jira integration
<a name="jira-integration"></a>

 **Capabilities**: \* Automatic ticket creation \* Bi-directional status sync \* Custom fields from workflow data \* Links back to Quick Suite reports

### Email notifications
<a name="email-notifications"></a>

 **Capabilities**: \* Executive summaries on schedule \* Approval requests with links \* Digest emails for multiple issues \* Customizable templates

## Measuring effectiveness
<a name="measuring-effectiveness"></a>

Track metrics to optimize workflows and demonstrate value.

![Quick Suite Reports - Metrics Dashboard](http://docs.aws.amazon.com/guidance/latest/automotive-data-platform-on-aws/images/quick-suite-report.jpg)


### Automation metrics
<a name="automation-metrics"></a>

 **Workflow performance**: \* Time from detection to action: Target < 1 hour \* Completion rate: Target > 95% \* False positive rate: Target < 5% \* Manual intervention: Target < 20%

### Business impact metrics
<a name="business-impact-metrics"></a>

 **Customer outcomes**: \* Issues resolved proactively \* Customer satisfaction improvement \* Churn reduction vs baseline \* Response time improvement

 **Financial impact**: \* Revenue protected monthly \* Cost savings from automation \* Campaign ROI \* Service program effectiveness

### Approval metrics
<a name="approval-metrics"></a>

 **Approval efficiency**: \* Average response time: Target < 4 hours \* Approval rate by workflow type \* Escalation frequency: Target < 10% \* Approver engagement